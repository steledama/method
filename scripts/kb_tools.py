#!/usr/bin/env python3
"""Strumenti deterministici portabili per repository basati sul metodo KB."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WORD_RE = re.compile(r"\b[a-zàèéìòù][a-zàèéìòù-]{5,}\b", re.IGNORECASE)
README_DOC_RE = re.compile(r"\((?P<path>(?:kb|metodo)/[^)]*\.md)\)")

DOC_DIRS = ("kb", "metodo")
OPTIONAL_DOC_DIRS = ("tech", "docs")
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


@dataclass
class AuditResult:
    total_nodes: int
    total_links: int
    readme_links: int
    readme_unique_links: int
    readme_broken: list[str]
    readme_missing_nodes: list[str]
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


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def deaccent(value: str) -> str:
    return value.translate(str.maketrans("àèéìòù", "aeeiou"))


def existing_doc_dirs(root: Path, include_optional: bool = True) -> list[Path]:
    names = [*DOC_DIRS, *(OPTIONAL_DOC_DIRS if include_optional else ())]
    return [root / name for name in names if (root / name).is_dir()]


def doc_files(root: Path) -> list[Path]:
    return sorted(
        path
        for directory in existing_doc_dirs(root)
        for path in directory.glob("*.md")
    )


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


def readme_index(root: Path) -> tuple[list[str], list[str], list[str]]:
    readme_path = root / "README.md"
    if not readme_path.exists():
        return [], ["README.md"], [node_key(root, path) for path in doc_files(root)]

    readme = readme_path.read_text(encoding="utf-8")
    paths = [match.group("path") for match in README_DOC_RE.finditer(readme)]
    broken = [path for path in paths if not (root / path).exists()]
    indexed = set(paths)
    missing = sorted(node_key(root, path) for path in doc_files(root) if node_key(root, path) not in indexed)
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
            if all(char.islower() or char.isdigit() or char in "./-" or ord(char) > 127 for char in rel):
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
        fm = text.split("---", 2)[1] if text.startswith("---\n") and text.count("---") >= 2 else ""
        if text.startswith("---\n") and "\ndata:" in fm and "\nstato:" in fm:
            frontmatter += 1
        if "\nConnessioni:\n" in text:
            connessioni += 1
        body = text.split("\nConnessioni:\n", 1)[0]
        if re.search(r"\[[^\]]+\]\([^)]+\.md\)", body):
            body_inline.append(node_key(root, path))
    return frontmatter, connessioni, body_inline


def cluster_state(root: Path, links: dict[str, list[str]]) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    readme_path = root / "README.md"
    if not readme_path.exists():
        return {}, {}

    clusters: dict[str, set[str]] = defaultdict(set)
    current: str | None = None
    for line in readme_path.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"### (.+)", line)
        if heading:
            current = heading.group(1).strip()
            continue
        if line.startswith("## "):
            current = None
        if current:
            for match in README_DOC_RE.finditer(line):
                clusters[current].add(match.group("path"))

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
    return sorted(candidates, key=lambda item: (int(item["file"]), int(item["occorrenze"])), reverse=True)[:limit]


def recent_commits(root: Path) -> list[str]:
    try:
        output = subprocess.check_output(["git", "log", "--oneline", "-15"], cwd=root, text=True)
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
            (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else "",
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


def run_audit(root: Path) -> AuditResult:
    inventory = {node_key(root, path) for path in doc_files(root)}
    links, broken = link_map(root)
    backlinks = backlink_map(links, inventory)
    readme_paths, readme_broken, readme_missing = readme_index(root)
    accented, invalid = filename_findings(root)
    frontmatter, connessioni, body_inline = migration_state(root)
    clusters, cluster_out = cluster_state(root, links)

    orphans = sorted(node for node in inventory if not backlinks[node])
    isolated = sorted(node for node in inventory if len(links.get(node, [])) == 0 and len(backlinks[node]) <= 1)
    hubs = [
        {"nodo": node, "backlink": count}
        for count, node in sorted(((len(sources), node) for node, sources in backlinks.items()), reverse=True)[:10]
    ]

    return AuditResult(
        total_nodes=len(inventory),
        total_links=sum(len(targets) for targets in links.values()),
        readme_links=len(readme_paths),
        readme_unique_links=len(set(readme_paths)),
        readme_broken=readme_broken,
        readme_missing_nodes=readme_missing,
        broken_links=broken,
        orphans=orphans,
        isolated=isolated,
        invalid_names=sorted(set(invalid)),
        accented_names=accented,
        frontmatter_count=frontmatter,
        connessioni_count=connessioni,
        body_inline_links=body_inline,
        clusters_total=len(clusters),
        cluster_isolated=sorted(cluster for cluster in clusters if not cluster_out.get(cluster)),
        cluster_out_counts={cluster: len(cluster_out.get(cluster, set())) for cluster in sorted(clusters)},
        term_candidates=term_candidates(root),
        hubs=hubs,
        recent_commits=recent_commits(root),
    )


def markdown_report(result: AuditResult) -> str:
    problem_count = (
        len(result.orphans)
        + len(result.broken_links)
        + len(result.readme_broken)
        + len(result.readme_missing_nodes)
        + len(result.invalid_names)
        + len(result.cluster_isolated)
        + len(result.body_inline_links)
    )
    lines = [
        f"## [{date.today().isoformat()}] audit-kb",
        "",
        "### OK",
        "",
        f"- {result.total_nodes} nodi verificati",
        f"- {result.total_links} link interni tra nodi, {len(result.broken_links)} link rotti",
        f"- {result.readme_links} link README.md ({result.readme_unique_links} unici)",
        f"- {result.total_nodes - len(result.readme_missing_nodes)} nodi indicizzati nel README",
        f"- {result.frontmatter_count}/{result.total_nodes} nodi con frontmatter `data` + `stato`",
        f"- {result.connessioni_count}/{result.total_nodes} nodi con footer `Connessioni:`",
        f"- {len(result.body_inline_links)} nodi con link markdown nel corpo",
        f"- {len(result.isolated)} nodi isolati",
        f"- {problem_count} problemi strutturali",
        "",
        "### Problemi",
        "",
    ]

    problems: list[str] = []
    problems += [f"- [ORFANO] {node} — nessun backlink" for node in result.orphans]
    problems += [f"- [LINK-ROTTO] {item}" for item in result.broken_links]
    problems += [f"- [README-LINK-ROTTO] README.md -> {item}" for item in result.readme_broken]
    problems += [f"- [README-MISSING] {item}" for item in result.readme_missing_nodes]
    problems += [f"- [NOME-INVALIDO] {item}" for item in result.invalid_names]
    problems += [f"- [CLUSTER-ISOLATO] {item}" for item in result.cluster_isolated]
    problems += [f"- [LINK-INLINE-CORPO] {item}" for item in result.body_inline_links]
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


def append_log(root: Path, report: str) -> None:
    log_path = root / "log.md"
    current = log_path.read_text(encoding="utf-8") if log_path.exists() else "# log.md\n"
    separator = "" if current.endswith("\n\n") else "\n"
    log_path.write_text(current + separator + report, encoding="utf-8")


def command_audit(args: argparse.Namespace) -> None:
    result = run_audit(repo_root())
    if args.append_log:
        if args.format != "markdown":
            raise SystemExit("--append-log richiede --format markdown")
        append_log(repo_root(), markdown_report(result))
    output_result(result, args.format)


def command_backlinks(args: argparse.Namespace) -> None:
    root = repo_root()
    requested = args.node
    links, broken = link_map(root)
    inventory = {node_key(root, path) for path in doc_files(root)}
    matches = [node for node in inventory if node == requested or Path(node).name == Path(requested).name]
    if not matches:
        raise SystemExit(f"Nodo non trovato: {requested}")
    node = sorted(matches)[0]
    backlinks = backlink_map(links, inventory)
    print_json({"nodo": node, "out": links.get(node, []), "in": sorted(backlinks.get(node, set())), "broken_total": len(broken)})


def command_orphans(args: argparse.Namespace) -> None:
    root = repo_root()
    inventory = {node_key(root, path) for path in doc_files(root)}
    links, _ = link_map(root)
    backlinks = backlink_map(links, inventory)
    for node in sorted(node for node in inventory if not backlinks[node]):
        print(node)


def command_readme(args: argparse.Namespace) -> None:
    paths, broken, missing = readme_index(repo_root())
    print_json({"links": len(paths), "unique": len(set(paths)), "broken": broken, "missing_nodes": missing})


def command_migration(args: argparse.Namespace) -> None:
    root = repo_root()
    frontmatter, connessioni, body_inline = migration_state(root)
    print_json({"total": len(doc_files(root)), "frontmatter": frontmatter, "connessioni": connessioni, "body_inline_links": body_inline})


def command_terms(args: argparse.Namespace) -> None:
    print_json(term_candidates(repo_root(), limit=args.limit))


def command_inventory(args: argparse.Namespace) -> None:
    output_result(run_code_inventory(repo_root()), args.format)


def command_coverage(args: argparse.Namespace) -> None:
    output_result(run_code_coverage(repo_root()), args.format)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Utility portabili per knowledge base")
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="audit strutturale della KB")
    audit.add_argument("--format", choices=["markdown", "json"], default="markdown")
    audit.add_argument("--append-log", action="store_true", help="appende il report markdown a log.md")
    audit.set_defaults(func=command_audit)

    backlinks = sub.add_parser("backlinks", help="mostra link in/out di un nodo")
    backlinks.add_argument("node")
    backlinks.set_defaults(func=command_backlinks)

    orphans = sub.add_parser("orphans", help="lista nodi senza backlink")
    orphans.set_defaults(func=command_orphans)

    readme = sub.add_parser("readme", help="verifica copertura README")
    readme.set_defaults(func=command_readme)

    migration = sub.add_parser("migration", help="verifica frontmatter e footer Connessioni")
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
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
