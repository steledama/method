#!/usr/bin/env python3
"""Strumenti deterministici portabili per repository basati sul metodo."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WORD_RE = re.compile(r"\b[a-zàèéìòù][a-zàèéìòù-]{5,}\b", re.IGNORECASE)
CATALOG_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<path>[^)]+\.md)\)")

DOC_DIRS = ("kb", "metodo")
CATALOG_NAME = "kb/kb.md"
OPTIONAL_DOC_DIRS = ("tech", "docs")
STAGE_INDEXES = {
    "i1": "perceptions.md",
    "i2": "interpretations.md",
    "i3": "verdicts.md",
    "o1": None,  # o1/plan.md è anche l'istanza corrente del Plan.
    "o2": "tasks.md",
    "o3": "prescriptions.md",
}
CODE_EXTENSIONS = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".sh",
    ".nix",
    ".mjs",
    ".cjs",
}
CODE_EXCLUDE_PARTS = {
    ".git",
    ".direnv",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "target",
    "__pycache__",
}

STOPWORDS = {
    "anche",
    "attraverso",
    "caratteristiche",
    "connessioni",
    "della",
    "delle",
    "degli",
    "dell",
    "essere",
    "forma",
    "markdown",
    "maturo",
    "nella",
    "nelle",
    "nello",
    "nodi",
    "nodo",
    "parte",
    "perché",
    "prima",
    "processo",
    "progetto",
    "propria",
    "qualcosa",
    "quella",
    "quelle",
    "quello",
    "questi",
    "questa",
    "questo",
    "quando",
    "relazione",
    "richiede",
    "senza",
    "stabile",
    "stessa",
    "stesso",
    "struttura",
    "verso",
    "viene",
}


@dataclass(frozen=True)
class Facet:
    """Attributo intrinseco di dominio di un nodo (faceted classification).

    `values` è l'insieme chiuso dei valori ammessi; `required=True` esige la facet
    su ogni nodo (es. `mondo` in nixos, che partiziona l'intera KB), `False` ne
    verifica solo il dominio quando presente (es. `tipo` in economia, sui soli
    nodi-entità). Cfr. il criterio dei quattro requisiti in `kb/node.md`.
    """

    values: frozenset[str]
    required: bool = False


# Attributi di dominio dichiarati dall'adottante. Vuoto in `method` (il suo
# dominio è astratto, nessuna facet); l'adottante parametrizza questa costante nel
# proprio fork, come fa già per DOC_DIRS o CATALOG_NAME. Esempi reali:
#   economia: {"tipo": Facet(frozenset({"persona", "immobile", "successione"}))}
#   nixos:    {"mondo": Facet(frozenset({"lavoro", "casa", "trasversale"}), required=True)}
EXTENDED_FACETS: dict[str, Facet] = {}
CYCLE_FACET = Facet(frozenset({"dev", "runtime"}), required=True)


@dataclass
class AuditResult:
    total_nodes: int
    total_links: int
    catalog_links: int
    catalog_unique_links: int
    catalog_broken: list[str]
    catalog_missing_nodes: list[str]
    broken_links: list[str]
    orphans: list[str]
    isolated: list[str]
    invalid_names: list[str]
    accented_names: list[str]
    frontmatter_count: int
    connessioni_count: int
    body_inline_links: list[str]
    clusters_total: int
    cluster_isolated: list[str]
    cluster_out_counts: dict[str, int]
    term_candidates: list[dict[str, int | str]]
    hubs: list[dict[str, int | str]]
    recent_commits: list[str]
    facet_violations: list[str]
    stage_cycle_count: int


@dataclass
class CodeInventory:
    files_total: int
    by_extension: dict[str, int]
    top_level_dirs: dict[str, int]
    files: list[str]


@dataclass
class CodeCoverage:
    documented: list[str]
    missing: list[str]
    docs_count: int
    code_files_total: int


@dataclass
class TaskFrontmatter:
    total: int
    complete: int
    missing: list[str]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def deaccent(value: str) -> str:
    return value.translate(str.maketrans("àèéìòù", "aeeiou"))


def existing_doc_dirs(root: Path, include_optional: bool = True) -> list[Path]:
    names = [*DOC_DIRS, *(OPTIONAL_DOC_DIRS if include_optional else ())]
    return [root / name for name in names if (root / name).is_dir()]


def doc_files(root: Path) -> list[Path]:
    catalog = catalog_path(root)
    catalog_resolved = catalog.resolve() if catalog else None
    return sorted(
        path
        for directory in existing_doc_dirs(root)
        for path in directory.glob("*.md")
        if path.resolve() != catalog_resolved
    )


def catalog_path(root: Path) -> Path | None:
    candidate = root / CATALOG_NAME
    if candidate.exists():
        return candidate
    legacy_root = root / "kb.md"
    if legacy_root.exists():
        return legacy_root
    for directory in existing_doc_dirs(root):
        legacy = directory / "index.md"
        if legacy.exists():
            return legacy
    return None


def node_key(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def markdown_links(text: str) -> list[str]:
    return [target for target in LINK_RE.findall(text) if target.endswith(".md")]


def resolve_link(source: Path, target: str) -> Path | None:
    if "://" in target or target.startswith("#"):
        return None
    return (source.parent / target.split("#", 1)[0]).resolve()


def link_map(root: Path) -> tuple[dict[str, list[str]], list[str]]:
    inventory = {path.resolve(): node_key(root, path) for path in doc_files(root)}
    links: dict[str, list[str]] = {}
    broken: list[str] = []

    for path in doc_files(root):
        source = node_key(root, path)
        targets: list[str] = []
        for target in markdown_links(path.read_text(encoding="utf-8")):
            resolved = resolve_link(path, target)
            if resolved is None:
                continue
            if resolved not in inventory:
                # Fuori inventario ma esistente su disco: link esterno valido
                # (cross-repo via symlink `method/`, altre collezioni) — la
                # stessa semantica di catalog_index. Rotto solo se non esiste.
                if not resolved.exists():
                    broken.append(f"{source} -> {target}")
                continue
            targets.append(inventory[resolved])
        links[source] = targets
    return links, broken


def backlink_map(
    links: dict[str, list[str]], inventory: set[str]
) -> dict[str, set[str]]:
    backlinks: dict[str, set[str]] = defaultdict(set)
    for source, targets in links.items():
        for target in targets:
            if target in inventory and target != source:
                backlinks[target].add(source)
    return backlinks


def catalog_index(root: Path) -> tuple[list[str], list[str], list[str]]:
    catalog = catalog_path(root)
    if catalog is None:
        return [], [CATALOG_NAME], [node_key(root, path) for path in doc_files(root)]

    text = catalog.read_text(encoding="utf-8")
    paths: list[str] = []
    broken: list[str] = []
    for match in CATALOG_LINK_RE.finditer(text):
        target = match.group("path")
        resolved = resolve_link(catalog, target)
        if resolved is None:
            continue
        if not resolved.exists():
            broken.append(target)
            continue
        paths.append(node_key(root, resolved))
    indexed = set(paths)
    missing = sorted(
        node_key(root, path)
        for path in doc_files(root)
        if node_key(root, path) not in indexed
    )
    return paths, broken, missing


def filename_findings(root: Path) -> tuple[list[str], list[str]]:
    accented: list[str] = []
    invalid: list[str] = []
    for path in doc_files(root):
        rel = node_key(root, path)
        if re.search(r"[A-Z ]", rel):
            invalid.append(rel)
            continue
        if re.search(r"[^a-z0-9./\-]", rel):
            if all(
                char.islower() or char.isdigit() or char in "./-" or ord(char) > 127
                for char in rel
            ):
                accented.append(rel)
            else:
                invalid.append(rel)
    return accented, invalid


def migration_state(root: Path) -> tuple[int, int, list[str]]:
    frontmatter = 0
    connessioni = 0
    body_inline: list[str] = []
    for path in doc_files(root):
        text = path.read_text(encoding="utf-8")
        fm = (
            text.split("---", 2)[1]
            if text.startswith("---\n") and text.count("---") >= 2
            else ""
        )
        if text.startswith("---\n") and "\nstato:" in fm:
            frontmatter += 1
        if "\nConnessioni:\n" in text:
            connessioni += 1
        body = text.split("\nConnessioni:\n", 1)[0]
        if re.search(r"\[[^\]]+\]\([^)]+\.md\)", body):
            body_inline.append(node_key(root, path))
    return frontmatter, connessioni, body_inline


def frontmatter_block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return (
        text.split("---", 2)[1]
        if text.startswith("---\n") and text.count("---") >= 2
        else ""
    )


def facet_value(fm: str, name: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(name)}:[ \t]*(.+?)[ \t]*$", fm)
    return match.group(1).strip() if match else None


def validate_facet(
    key: str, fm: str, name: str, facet: Facet, violations: list[str]
) -> None:
    value = facet_value(fm, name)
    if value is None:
        if facet.required:
            violations.append(f"{key}: manca `{name}`")
        return
    if value not in facet.values:
        violations.append(
            f"{key}: `{name}: {value}` fuori dominio {sorted(facet.values)}"
        )


def facet_violations(root: Path) -> list[str]:
    """Verifica gli attributi di dominio dichiarati in EXTENDED_FACETS.

    Per ogni facet controlla che il valore nel frontmatter sia dentro il dominio
    chiuso; se la facet è `required`, ne esige anche la presenza su ogni nodo. In
    `method` la costante è vuota e la funzione non rileva nulla.
    """
    if not EXTENDED_FACETS:
        return []
    violations: list[str] = []
    for path in doc_files(root):
        fm = frontmatter_block(path)
        key = node_key(root, path)
        for name, facet in EXTENDED_FACETS.items():
            validate_facet(key, fm, name, facet, violations)
    return violations


def stage_cycle_state(root: Path) -> tuple[int, list[str]]:
    checked = 0
    violations: list[str] = []
    for dirname, index_name in STAGE_INDEXES.items():
        directory = root / dirname
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if index_name and path.name == index_name:
                continue
            checked += 1
            validate_facet(
                node_key(root, path),
                frontmatter_block(path),
                "ciclo",
                CYCLE_FACET,
                violations,
            )
    return checked, violations


def cluster_state(
    root: Path, links: dict[str, list[str]]
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    catalog = catalog_path(root)
    if catalog is None:
        return {}, {}

    clusters: dict[str, set[str]] = defaultdict(set)
    current: str | None = None
    for line in catalog.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"## (.+)", line)
        if heading:
            current = heading.group(1).strip()
            continue
        if line.startswith("# "):
            current = None
        if current:
            for match in CATALOG_LINK_RE.finditer(line):
                resolved = resolve_link(catalog, match.group("path"))
                if resolved is not None and resolved.exists():
                    clusters[current].add(node_key(root, resolved))

    node_cluster: dict[str, str] = {}
    for cluster, nodes in clusters.items():
        for node in nodes:
            node_cluster.setdefault(node, cluster)

    cluster_out: dict[str, set[str]] = defaultdict(set)
    for source, targets in links.items():
        source_cluster = node_cluster.get(source)
        if not source_cluster:
            continue
        for target in targets:
            target_cluster = node_cluster.get(target)
            if target_cluster and target_cluster != source_cluster:
                cluster_out[source_cluster].add(target_cluster)
    return clusters, cluster_out


def term_candidates(root: Path, limit: int = 12) -> list[dict[str, int | str]]:
    existing = {path.stem for path in doc_files(root)}
    file_occurrences: dict[str, set[str]] = defaultdict(set)
    total_occurrences: Counter[str] = Counter()

    for path in doc_files(root):
        text = path.read_text(encoding="utf-8").lower()
        if text.startswith("---"):
            text = text.split("---", 2)[2]
        text = text.split("\nconnessioni:\n", 1)[0]
        for word in WORD_RE.findall(text):
            word = word.strip("-").lower()
            singular = word[:-1] if word.endswith("i") else word
            singular_e = f"{word[:-1]}e" if word.endswith("i") else word
            if word in STOPWORDS or deaccent(word) in STOPWORDS:
                continue
            if word in existing or deaccent(word) in existing:
                continue
            if singular in existing or deaccent(singular) in existing:
                continue
            if singular_e in existing or deaccent(singular_e) in existing:
                continue
            file_occurrences[word].add(node_key(root, path))
            total_occurrences[word] += 1

    candidates = [
        {"termine": word, "file": len(files), "occorrenze": total_occurrences[word]}
        for word, files in file_occurrences.items()
        if len(files) >= 3 and total_occurrences[word] >= 6
    ]
    return sorted(
        candidates,
        key=lambda item: (int(item["file"]), int(item["occorrenze"])),
        reverse=True,
    )[:limit]


def recent_commits(root: Path) -> list[str]:
    try:
        output = subprocess.check_output(
            ["git", "log", "--oneline", "-15"], cwd=root, text=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return [line for line in output.splitlines() if line.strip()]


def code_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in CODE_EXTENSIONS:
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in CODE_EXCLUDE_PARTS for part in rel_parts):
            continue
        if rel_parts[0] in {*DOC_DIRS, *OPTIONAL_DOC_DIRS}:
            continue
        files.append(path)
    return sorted(files)


def run_code_inventory(root: Path) -> CodeInventory:
    files = code_files(root)
    by_extension = Counter(path.suffix for path in files)
    top_level = Counter(path.relative_to(root).parts[0] for path in files)
    return CodeInventory(
        files_total=len(files),
        by_extension=dict(sorted(by_extension.items())),
        top_level_dirs=dict(sorted(top_level.items())),
        files=[node_key(root, path) for path in files],
    )


def run_code_coverage(root: Path) -> CodeCoverage:
    documented = {path.stem for path in doc_files(root)}
    doc_corpus = "\n".join(
        [
            (root / "README.md").read_text(encoding="utf-8")
            if (root / "README.md").exists()
            else "",
            *[path.read_text(encoding="utf-8") for path in doc_files(root)],
        ]
    )
    docs: list[str] = []
    missing: list[str] = []
    for path in code_files(root):
        rel = node_key(root, path)
        if path.stem in documented or rel in doc_corpus or path.name in doc_corpus:
            docs.append(rel)
        else:
            missing.append(rel)
    return CodeCoverage(
        documented=docs,
        missing=missing,
        docs_count=len(docs),
        code_files_total=len(docs) + len(missing),
    )


def run_task_frontmatter(root: Path) -> TaskFrontmatter:
    missing: list[str] = []
    # Esclude l'indice di collezione omonimo (o2/tasks.md): è una porta, non un task.
    task_files = [p for p in sorted((root / "o2").glob("*.md")) if p.name != "tasks.md"]
    for path in task_files:
        text = path.read_text(encoding="utf-8")
        fm = (
            text.split("---", 2)[1]
            if text.startswith("---\n") and text.count("---") >= 2
            else ""
        )
        absent = [key for key in ("sintesi",) if f"\n{key}:" not in f"\n{fm}"]
        if "\nstato:" in f"\n{fm}":
            absent.append(
                "stato presente (soppresso: un task in o2/ è aperto per esistenza)"
            )
        if absent:
            missing.append(f"{node_key(root, path)}: {', '.join(absent)}")
    return TaskFrontmatter(
        total=len(task_files),
        complete=len(task_files) - len(missing),
        missing=missing,
    )


def run_audit(root: Path) -> AuditResult:
    inventory = {node_key(root, path) for path in doc_files(root)}
    links, broken = link_map(root)
    backlinks = backlink_map(links, inventory)
    catalog_paths, catalog_broken, catalog_missing = catalog_index(root)
    accented, invalid = filename_findings(root)
    frontmatter, connessioni, body_inline = migration_state(root)
    clusters, cluster_out = cluster_state(root, links)
    stage_cycle_count, stage_cycle_issues = stage_cycle_state(root)
    facet_issues = [*facet_violations(root), *stage_cycle_issues]

    orphans = sorted(node for node in inventory if not backlinks[node])
    isolated = sorted(
        node
        for node in inventory
        if len(links.get(node, [])) == 0 and len(backlinks[node]) <= 1
    )
    hubs = [
        {"nodo": node, "backlink": count}
        for count, node in sorted(
            ((len(sources), node) for node, sources in backlinks.items()), reverse=True
        )[:10]
    ]

    return AuditResult(
        total_nodes=len(inventory),
        total_links=sum(len(targets) for targets in links.values()),
        catalog_links=len(catalog_paths),
        catalog_unique_links=len(set(catalog_paths)),
        catalog_broken=catalog_broken,
        catalog_missing_nodes=catalog_missing,
        broken_links=broken,
        orphans=orphans,
        isolated=isolated,
        invalid_names=sorted(set(invalid)),
        accented_names=accented,
        frontmatter_count=frontmatter,
        connessioni_count=connessioni,
        body_inline_links=body_inline,
        clusters_total=len(clusters),
        cluster_isolated=sorted(
            cluster for cluster in clusters if not cluster_out.get(cluster)
        ),
        cluster_out_counts={
            cluster: len(cluster_out.get(cluster, set()))
            for cluster in sorted(clusters)
        },
        term_candidates=term_candidates(root),
        hubs=hubs,
        recent_commits=recent_commits(root),
        facet_violations=facet_issues,
        stage_cycle_count=stage_cycle_count,
    )


def markdown_report(result: AuditResult) -> str:
    problem_count = (
        len(result.orphans)
        + len(result.broken_links)
        + len(result.catalog_broken)
        + len(result.catalog_missing_nodes)
        + len(result.invalid_names)
        + len(result.cluster_isolated)
        + len(result.body_inline_links)
        + len(result.facet_violations)
    )
    lines = [
        f"## [{date.today().isoformat()}] kb-review",
        "",
        "### OK",
        "",
        f"- {result.total_nodes} nodi verificati",
        f"- {result.total_links} link interni tra nodi, {len(result.broken_links)} link rotti",
        f"- {result.catalog_links} link {CATALOG_NAME} ({result.catalog_unique_links} unici)",
        f"- {result.total_nodes - len(result.catalog_missing_nodes)} nodi indicizzati in {CATALOG_NAME}",
        f"- {result.frontmatter_count}/{result.total_nodes} nodi con frontmatter `stato`",
        f"- {result.connessioni_count}/{result.total_nodes} nodi con footer `Connessioni:`",
        f"- {result.stage_cycle_count} item di collezione con facet `ciclo` valida",
        f"- {len(result.body_inline_links)} nodi con link markdown nel corpo",
        f"- {len(result.isolated)} nodi isolati",
        *(
            [
                f"- attributi di dominio: {', '.join(EXTENDED_FACETS)} "
                f"({len(result.facet_violations)} violazioni)"
            ]
            if EXTENDED_FACETS
            else []
        ),
        f"- {problem_count} problemi strutturali",
        "",
        "### Problemi",
        "",
    ]

    problems: list[str] = []
    problems += [f"- [ORFANO] {node} — nessun backlink" for node in result.orphans]
    problems += [f"- [LINK-ROTTO] {item}" for item in result.broken_links]
    problems += [
        f"- [CATALOGO-LINK-ROTTO] {CATALOG_NAME} -> {item}"
        for item in result.catalog_broken
    ]
    problems += [
        f"- [CATALOGO-MISSING] {item}" for item in result.catalog_missing_nodes
    ]
    problems += [f"- [NOME-INVALIDO] {item}" for item in result.invalid_names]
    problems += [f"- [CLUSTER-ISOLATO] {item}" for item in result.cluster_isolated]
    problems += [f"- [LINK-INLINE-CORPO] {item}" for item in result.body_inline_links]
    problems += [f"- [FACET] {item}" for item in result.facet_violations]
    lines += problems[:30] if problems else ["- Nessun problema strutturale rilevato"]
    if len(problems) > 30:
        lines.append(f"- ... altri {len(problems) - 30} problemi non mostrati")

    lines += [
        "",
        "### Concetti ricorrenti senza nodo",
        "",
    ]
    if result.term_candidates:
        lines += [
            f"- {item['termine']} — {item['file']} file, {item['occorrenze']} occorrenze"
            for item in result.term_candidates
        ]
    else:
        lines.append("- Nessun candidato forte")

    lines += ["", "### Hub principali", ""]
    lines += [f"- {item['nodo']} — {item['backlink']} backlink" for item in result.hubs]
    return "\n".join(lines) + "\n"


def print_json(data: object) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def output_result(data: object, fmt: str) -> None:
    if fmt == "json":
        print_json(asdict(data) if hasattr(data, "__dataclass_fields__") else data)
    elif isinstance(data, AuditResult):
        print(markdown_report(data), end="")
    else:
        print_json(asdict(data) if hasattr(data, "__dataclass_fields__") else data)


def command_audit(args: argparse.Namespace) -> None:
    result = run_audit(repo_root())
    output_result(result, args.format)


def command_backlinks(args: argparse.Namespace) -> None:
    root = repo_root()
    requested = args.node
    links, broken = link_map(root)
    inventory = {node_key(root, path) for path in doc_files(root)}
    matches = [
        node
        for node in inventory
        if node == requested or Path(node).name == Path(requested).name
    ]
    if not matches:
        raise SystemExit(f"Nodo non trovato: {requested}")
    node = sorted(matches)[0]
    backlinks = backlink_map(links, inventory)
    print_json(
        {
            "nodo": node,
            "out": links.get(node, []),
            "in": sorted(backlinks.get(node, set())),
            "broken_total": len(broken),
        }
    )


def command_orphans(args: argparse.Namespace) -> None:
    root = repo_root()
    inventory = {node_key(root, path) for path in doc_files(root)}
    links, _ = link_map(root)
    backlinks = backlink_map(links, inventory)
    for node in sorted(node for node in inventory if not backlinks[node]):
        print(node)


def command_readme(args: argparse.Namespace) -> None:
    paths, broken, missing = catalog_index(repo_root())
    print_json(
        {
            "links": len(paths),
            "unique": len(set(paths)),
            "broken": broken,
            "missing_nodes": missing,
        }
    )


def command_migration(args: argparse.Namespace) -> None:
    root = repo_root()
    frontmatter, connessioni, body_inline = migration_state(root)
    print_json(
        {
            "total": len(doc_files(root)),
            "frontmatter": frontmatter,
            "connessioni": connessioni,
            "body_inline_links": body_inline,
        }
    )


def command_terms(args: argparse.Namespace) -> None:
    print_json(term_candidates(repo_root(), limit=args.limit))


def command_inventory(args: argparse.Namespace) -> None:
    output_result(run_code_inventory(repo_root()), args.format)


def command_coverage(args: argparse.Namespace) -> None:
    output_result(run_code_coverage(repo_root()), args.format)


def command_tasks(args: argparse.Namespace) -> None:
    output_result(run_task_frontmatter(repo_root()), args.format)


def command_facets(args: argparse.Namespace) -> None:
    print_json(
        {
            "declared": {
                name: {"values": sorted(facet.values), "required": facet.required}
                for name, facet in {"ciclo": CYCLE_FACET, **EXTENDED_FACETS}.items()
            },
            "violations": [
                *facet_violations(repo_root()),
                *stage_cycle_state(repo_root())[1],
            ],
        }
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Utility portabili per knowledge base")
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="audit strutturale della KB")
    audit.add_argument("--format", choices=["markdown", "json"], default="markdown")
    audit.set_defaults(func=command_audit)

    backlinks = sub.add_parser("backlinks", help="mostra link in/out di un nodo")
    backlinks.add_argument("node")
    backlinks.set_defaults(func=command_backlinks)

    orphans = sub.add_parser("orphans", help="lista nodi senza backlink")
    orphans.set_defaults(func=command_orphans)

    readme = sub.add_parser(
        "readme", help=f"verifica copertura del catalogo {CATALOG_NAME}"
    )
    readme.set_defaults(func=command_readme)

    migration = sub.add_parser(
        "migration", help="verifica frontmatter e footer Connessioni"
    )
    migration.set_defaults(func=command_migration)

    terms = sub.add_parser("terms", help="candidati a nuovi nodi da termini ricorrenti")
    terms.add_argument("--limit", type=int, default=12)
    terms.set_defaults(func=command_terms)

    inventory = sub.add_parser("inventory", help="inventario generico dei file codice")
    inventory.add_argument("--format", choices=["json"], default="json")
    inventory.set_defaults(func=command_inventory)

    coverage = sub.add_parser("coverage", help="copertura generica codice -> nodi KB")
    coverage.add_argument("--format", choices=["json"], default="json")
    coverage.set_defaults(func=command_coverage)

    tasks = sub.add_parser("tasks", help="verifica frontmatter dei task aperti")
    tasks.add_argument("--format", choices=["json"], default="json")
    tasks.set_defaults(func=command_tasks)

    facets = sub.add_parser(
        "facets", help="verifica gli attributi di dominio dichiarati (EXTENDED_FACETS)"
    )
    facets.set_defaults(func=command_facets)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
