"""Parsing condiviso per viste generate e system image."""

from __future__ import annotations

import html
import json
import posixpath
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

import project

# Titoli delle viste nelle due lingue ammesse: la sigla la mette `project.py`.
LABELS = {
    "en": {
        "plan": "Plan",
        "goals": "Goals",
        "verdict": "Verdicts",
        "interpretations": "Interpretations",
        "prescriptions": "Prescriptions",
        "perceptions": "Perceptions",
        "wake": "Dependencies and deadlines",
    },
    "it": {
        "plan": "Piano",
        "goals": "Obiettivi",
        "verdict": "Confronti",
        "interpretations": "Interpretazioni",
        "prescriptions": "Prescrizioni",
        "perceptions": "Percezioni",
        "wake": "Dipendenze e scadenze",
    },
}


def label(kind: str) -> str:
    """Il titolo di una vista con la sigla del repo: «Method Plan», «BI Piano»."""
    if project.LINGUA not in LABELS:
        raise SystemExit(f"project.py: LINGUA «{project.LINGUA}» non ammessa ({', '.join(LABELS)})")
    return f"{project.SIGLA} {LABELS[project.LINGUA][kind]}"


@dataclass(frozen=True)
class PlanRow:
    position: str
    task: str
    dependency: str
    source: str | None
    ciclo: str | None = None
    obiettivo: str | None = None


@dataclass(frozen=True)
class TaskDetail:
    path: Path
    title: str
    ciclo: str
    sintesi: str


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, parts[2].lstrip()


def first_h1(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def first_paragraph(markdown: str, limit: int = 220) -> str:
    block: list[str] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith(("#", "---")):
            continue
        if not stripped:
            if block:
                break
            continue
        block.append(stripped)
    text = " ".join(block)
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _detail_source(detail_links: dict[str, str], task: str) -> str | None:
    task_norm = _norm(task)
    if task in detail_links:
        return detail_links[task]
    for title, source in detail_links.items():
        title_norm = _norm(title)
        if title_norm.startswith(task_norm) or task_norm.startswith(title_norm):
            return source
    return None


_INDEX_ENTRY = re.compile(r"^- \[[^\]]+\]\(([^)]+\.md)\)", re.MULTILINE)


def o2_index(root: Path) -> list[str]:
    """I file `o2/` indicizzati da `o2/tasks.md`, come path relativi alla root.

    `o2/tasks.md` è l'**unico** indice dei dettagli (cfr. `kb/tasks.md`): è la
    chiave con cui una riga del plan risolve al proprio file. Le voci che
    puntano fuori da `o2/` (rimandi ai nodi nel preambolo) non sono voci
    d'indice.
    """
    index = root / "o2" / "tasks.md"
    if not index.exists():
        return []
    entries: list[str] = []
    for match in _INDEX_ENTRY.finditer(index.read_text(encoding="utf-8")):
        href = match.group(1).removeprefix("../")
        if "/" in href.removeprefix("o2/"):
            continue
        relative = href if href.startswith("o2/") else f"o2/{href}"
        if relative not in entries:
            entries.append(relative)
    return entries


def _index_titles(root: Path) -> dict[str, str]:
    titles: dict[str, str] = {}
    for relative in o2_index(root):
        if (root / relative).exists():
            titles[parse_task(root, relative).title] = relative
    return titles


def parse_plan(root: Path) -> list[PlanRow]:
    plan = root / "o1" / "plan.md"
    text = plan.read_text(encoding="utf-8")
    # L'indice unico `o2/tasks.md` è la chiave canonica; i bullet `- [x](o2/…)`
    # nel plan sono la forma precedente, ancora in uso negli adottanti.
    detail_links = _index_titles(root)
    detail_links.update(
        {
            match.group(1).strip(): match.group(2).removeprefix("../")
            for match in re.finditer(r"- \[([^\]]+)\]\(((?:\.\./)?o2/[^)]+\.md)\)", text)
        }
    )
    rows: list[PlanRow] = []
    position = 0
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [
            cell.strip().replace("<<PIPE>>", "|")
            for cell in line.replace(r"\|", "<<PIPE>>").strip().strip("|").split("|")
        ]
        if cells[0] in {"#", "Task", "Ciclo"} or set(cells[0]) == {"-"}:
            continue
        if len(cells) not in {2, 3, 4}:
            # Una riga di tabella che il parser non sa leggere non si salta in
            # silenzio: sarebbe un task invisibile alla vista mentre il plan lo
            # dichiara (`kb/view.md`, «Derivata implica verificata»).
            raise SystemExit(
                f"o1/plan.md: riga di tabella con {len(cells)} colonne, "
                f"forma non riconosciuta — «{line.strip()}»"
            )
        ciclo: str | None = None
        obiettivo: str | None = None
        if len(cells) == 4:
            # Forma canonica: Ciclo · Ob. · Task · Dip.
            position += 1
            position_value, task_cell, dependency = str(position), cells[2], cells[3]
            ciclo, obiettivo = cells[0], cells[1]
        elif len(cells) == 3 and cells[0] in {"dev", "runtime"}:
            # Forma precedente (Ciclo · Task · Dip.), ancora in uso negli adottanti.
            position += 1
            position_value, task_cell, dependency = str(position), cells[1], cells[2]
            ciclo = cells[0]
        elif len(cells) == 3 and cells[1] in {"dev", "runtime"}:
            # Forma precedente (Task · Ciclo · Dip.), ancora in uso negli adottanti.
            position += 1
            position_value, task_cell, dependency = str(position), cells[0], cells[2]
            ciclo = cells[1]
        elif len(cells) == 3:
            position_value, task_cell, dependency = cells
        else:
            position += 1
            position_value, task_cell, dependency = str(position), cells[0], cells[1]
        link = re.search(r"\[([^\]]+)\]\(((?:\.\./)?o2/[^)]+\.md)\)", task_cell)
        task = link.group(1) if link else task_cell
        source = link.group(2).removeprefix("../") if link else _detail_source(detail_links, task)
        rows.append(
            PlanRow(
                position=position_value,
                task=task,
                dependency=dependency,
                source=source,
                ciclo=ciclo,
                obiettivo=obiettivo,
            )
        )
    return rows


_GOAL_HEADING = re.compile(r"^#{2,4}\s+((\d+)[.)]\s.*?)\s*$", re.MULTILINE)
_DEV_GOAL_HEADING = re.compile(r"^##\s+(Goal di sviluppo)\s*$", re.MULTILINE)


def heading_slug(title: str) -> str:
    """L'ancora che il renderer Markdown della forge assegna a un'intestazione."""
    text = re.sub(r"`([^`]+)`", r"\1", title)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def goal_anchors(root: Path) -> dict[str, str]:
    """Le chiavi che la colonna `Ob.` del plan può assumere, con la loro ancora.

    Il numero dell'obiettivo runtime, più `S` per il Goal di sviluppo: sono le
    chiavi del register, non una lista da tenere in sincronia (`kb/goal.md`).
    L'ancora è quella dell'intestazione in `goal.md`, così la vista può
    collegare la chiave all'obiettivo invece di ripeterne il numero.
    """
    goal = root / "goal.md"
    if not goal.exists():
        return {}
    text = goal.read_text(encoding="utf-8")
    anchors = {key: heading_slug(title) for title, key in _GOAL_HEADING.findall(text)}
    dev = _DEV_GOAL_HEADING.search(text)
    if dev:
        anchors["S"] = heading_slug(dev.group(1))
    return anchors


def goal_titles(root: Path) -> dict[str, str]:
    """Le chiavi del register con il titolo dell'obiettivo, nell'ordine di `goal.md`."""
    goal = root / "goal.md"
    if not goal.exists():
        return {}
    text = goal.read_text(encoding="utf-8")
    titles = {key: re.sub(r"^\d+[.)]\s+", "", title) for title, key in _GOAL_HEADING.findall(text)}
    dev = _DEV_GOAL_HEADING.search(text)
    if dev:
        titles["S"] = dev.group(1)
    return titles


def goal_keys(root: Path) -> set[str]:
    return set(goal_anchors(root))


def _check_obiettivi(root: Path, rows: list[PlanRow]) -> list[str]:
    """La colonna `Ob.` è derivata dal register: si verifica, non si assume.

    La direzione task→obiettivo vive solo qui (`kb/plan.md`): una chiave vuota
    è un task che non serve nessun obiettivo, una chiave che il register non ha
    è una numerazione andata alla deriva. Entrambe rompono, invece di produrre
    una vista che tace.
    """
    declared = {row.obiettivo for row in rows if row.obiettivo is not None}
    if not declared:
        return []
    keys = goal_keys(root)
    if not keys:
        return ["goal.md: nessun obiettivo numerato, ma o1/plan.md dichiara la colonna Ob."]
    errors: list[str] = []
    for row in rows:
        if row.obiettivo is None:
            continue
        if not row.obiettivo:
            errors.append(f"o1/plan.md: «{row.task}» senza obiettivo (colonna Ob. vuota)")
            continue
        unknown = [key for key in row.obiettivo.split(",") if key.strip() not in keys]
        if unknown:
            errors.append(
                f"o1/plan.md: «{row.task}» punta a obiettivi assenti dal register "
                f"({', '.join(key.strip() for key in unknown)})"
            )
    return errors


def check_plan_contract(root: Path, rows: list[PlanRow]) -> None:
    """Legge plan e `o2/` come un contratto: rompe invece di degradare.

    Una riga del plan **può** non avere dettaglio (`kb/tasks.md`: il file serve
    «quando serve contesto»), ma un file `o2/` scollegato, non indicizzato o in
    contraddizione col plan è una divergenza tra due fonti dello stesso fatto —
    la vista che la ignora invita ad agire su ciò che il plan non dice più
    (`kb/view.md`, «Derivata implica verificata»).
    """
    errors: list[str] = []
    indexed = o2_index(root)
    on_disk = sorted(
        f"o2/{path.name}" for path in (root / "o2").glob("*.md") if path.name != "tasks.md"
    )

    for relative in indexed:
        if not (root / relative).exists():
            errors.append(f"{relative}: voce di o2/tasks.md senza file")
    for relative in on_disk:
        if relative not in indexed:
            errors.append(f"{relative}: file non indicizzato in o2/tasks.md")

    bound: dict[str, list[str]] = {}
    for row in rows:
        if row.source:
            bound.setdefault(row.source, []).append(row.task)
    for relative in on_disk:
        if relative not in bound:
            errors.append(
                f"{relative}: nessuna riga di o1/plan.md risolve a questo file "
                f"(titolo «{parse_task(root, relative).title}»)"
            )
        elif len(bound[relative]) > 1:
            errors.append(
                f"{relative}: risolto da più righe del plan ({', '.join(bound[relative])})"
            )

    for row in rows:
        if not row.source or not row.ciclo:
            continue
        detail_ciclo = parse_task(root, row.source).ciclo
        if detail_ciclo != row.ciclo:
            errors.append(
                f"{row.source}: ciclo divergente — plan «{row.ciclo}», frontmatter «{detail_ciclo}»"
            )

    errors += _check_obiettivi(root, rows)

    if errors:
        raise SystemExit("contratto plan × o2 violato:\n- " + "\n- ".join(errors))


@dataclass(frozen=True)
class Thread:
    name: str
    title: str
    ciclo: str
    obiettivo: str
    body: str


def i3_index(root: Path) -> list[str]:
    """I file di `i3/` nell'ordine curato dell'indice `i3/verdicts.md`."""
    index = root / "i3" / "verdicts.md"
    if not index.exists():
        return []
    names: list[str] = []
    for match in _INDEX_ENTRY.finditer(index.read_text(encoding="utf-8")):
        href = match.group(1)
        if "/" not in href and href != "verdicts.md" and href not in names:
            names.append(href)
    return names


def parse_thread(root: Path, name: str) -> Thread:
    meta, body = split_frontmatter((root / "i3" / name).read_text(encoding="utf-8"))
    title = first_h1(body, name.removesuffix(".md"))
    body = re.sub(r"^# .*\n?", "", body, count=1, flags=re.MULTILINE).strip()
    return Thread(
        name=name,
        title=title,
        ciclo=meta.get("ciclo", ""),
        obiettivo=meta.get("obiettivo", ""),
        body=body,
    )


def check_verdict_contract(root: Path) -> list[Thread]:
    """Legge `i3/` come contratto: indice, file e obiettivi devono coincidere.

    Un filo misura un obiettivo di `goal.md` o non è un filo (`kb/verdict.md`,
    «Che cosa è un filo»): una chiave vuota o assente dal register rompe la
    build, come la colonna `Ob.` del plan. Un file fuori indice o una voce
    senza file sono due fonti dello stesso fatto che divergono.
    """
    errors: list[str] = []
    indexed = i3_index(root)
    on_disk = sorted(path.name for path in (root / "i3").glob("*.md") if path.name != "verdicts.md")
    for name in indexed:
        if name not in on_disk:
            errors.append(f"i3/{name}: voce di i3/verdicts.md senza file")
    for name in on_disk:
        if name not in indexed:
            errors.append(f"i3/{name}: file non indicizzato in i3/verdicts.md")
    keys = goal_keys(root)
    threads: list[Thread] = []
    for name in (name for name in indexed if name in on_disk):
        thread = parse_thread(root, name)
        if thread.ciclo not in {"dev", "runtime"}:
            errors.append(f"i3/{name}: frontmatter ciclo «{thread.ciclo}» non è dev|runtime")
        if not thread.obiettivo:
            errors.append(f"i3/{name}: nessun obiettivo nel frontmatter (obiettivo:)")
        else:
            unknown = [k.strip() for k in thread.obiettivo.split(",") if k.strip() not in keys]
            if unknown:
                errors.append(f"i3/{name}: obiettivi assenti dal register ({', '.join(unknown)})")
        threads.append(thread)
    if errors:
        raise SystemExit("contratto i3 × goal violato:\n- " + "\n- ".join(errors))
    return threads


def demote_headings(markdown: str) -> str:
    """Scende ogni intestazione di un livello, fuori dai blocchi di codice."""
    lines: list[str] = []
    fenced = False
    for line in markdown.splitlines():
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5}\s", line):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines)


def parse_task(root: Path, relative: str) -> TaskDetail:
    path = root / relative
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if not meta.get("sintesi"):
        raise SystemExit(f"{relative}: frontmatter incompleto (sintesi)")
    return TaskDetail(
        path=path,
        title=first_h1(body, path.stem),
        ciclo=meta.get("ciclo", "—"),
        sintesi=meta["sintesi"],
    )


# Gli unici schemi che portano fuori dal checkout senza portarsi dietro il
# disco di chi costruisce: `file:` e i path Windows (`C:\…`, letto come
# schema `c:`) non sono esterni, e il presidio li ferma.
_EXTERNAL_SCHEMES = {"http", "https", "mailto"}


def is_external(target: str) -> bool:
    """Un URL web o mail, o un'ancora: resta link anche fuori dal checkout."""
    parts = urlsplit(target)
    if target.startswith("#"):
        return True
    if parts.scheme:
        return parts.scheme.lower() in _EXTERNAL_SCHEMES
    return target.startswith("//")


def inline_markdown(text: str) -> str:
    """Rende inline markdown (code, bold, link) per la home.

    La presentazione è chiusa su se stessa (`kb/presentation.md`): un link
    relativo porterebbe a una fonte fuori da `presentation/`, quindi se ne
    rende solo l'etichetta. Restano link gli URL con schema e le ancore.
    """
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)

    def link(match: re.Match[str]) -> str:
        label_html, href = match.group(1), html.unescape(match.group(2))
        if not is_external(href):
            return label_html
        return f'<a href="{html.escape(href, quote=True)}">{label_html}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, escaped)


# --- Pandoc e compartimento stagno ---------------------------------------------


def pandoc_ast(markdown: str) -> dict:
    """Il Markdown di Pandoc come AST JSON, il formato su cui la build lavora."""
    parsed = subprocess.run(
        ["pandoc", "--from=markdown-native_divs", "--to=json"],
        input=markdown,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
    )
    return json.loads(parsed.stdout)


def pandoc_render(document: dict, args: list[str]) -> str:
    return subprocess.run(
        ["pandoc", "--from=json", *args],
        input=json.dumps(document),
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
    ).stdout


def _inside(presentation: Path, target: str) -> bool:
    path = urlsplit(target).path
    if not path:
        return True
    normal = posixpath.normpath(path)
    return (
        not normal.startswith(("../", "/")) and normal != ".." and (presentation / normal).exists()
    )


def close_links(value: object, presentation: Path, source: str) -> object:
    """Chiude l'AST dentro `presentation/`: il compartimento stagno.

    Un link che esce dalla cartella diventa la sua etichetta; un'immagine,
    anche di sfondo, deve stare nella cartella, altrimenti la build rompe:
    una tavola che manca non si rende in silenzio (`kb/view.md`).
    """
    if isinstance(value, list):
        out: list[object] = []
        for child in value:
            closed = close_links(child, presentation, source)
            if isinstance(child, dict) and child.get("t") == "Link" and closed is None:
                out.extend(close_links(child["c"][1], presentation, source))
            else:
                out.append(closed)
        return out
    if not isinstance(value, dict):
        return value
    kind = value.get("t")
    if kind == "Link":
        target = value["c"][-1][0]
        if not is_external(target) and not _inside(presentation, target):
            return None
    if kind == "Image":
        target = value["c"][-1][0]
        if not is_external(target) and not _inside(presentation, target):
            raise SystemExit(f"{source}: immagine fuori da presentation/ o assente — «{target}»")
    if kind == "Header":
        for key, target in value["c"][1][2]:
            if key == "data-background-image" and not _inside(presentation, target):
                raise SystemExit(f"{source}: tavola fuori da presentation/ o assente — «{target}»")
    return {key: close_links(child, presentation, source) for key, child in value.items()}


_URL_ATTR = re.compile(r'(?:href|src|data-background-image)="([^"]*)"|url\(([^)]*)\)')


def check_closed(presentation: Path) -> None:
    """Presidio finale: nessun URL emesso esce da `presentation/` o punta al vuoto."""
    errors: list[str] = []
    # Anche le pagine nelle sottocartelle (viste di dominio generate) stanno
    # dentro il compartimento.
    for page in sorted(presentation.rglob("*.html")) + sorted(presentation.rglob("*.css")):
        base = page.parent
        for match in _URL_ATTR.finditer(page.read_text(encoding="utf-8")):
            target = html.unescape((match.group(1) or match.group(2) or "").strip("'\""))
            if not target or is_external(target):
                continue
            path = urlsplit(target).path
            resolved = (base / path).resolve()
            if (
                presentation.resolve() not in resolved.parents
                and resolved != presentation.resolve()
            ):
                errors.append(f"{page.relative_to(presentation)}: esce dalla cartella — «{target}»")
            elif not resolved.exists():
                errors.append(
                    f"{page.relative_to(presentation)}: destinazione assente — «{target}»"
                )
    if errors:
        raise SystemExit("presentation/ non è chiusa su se stessa:\n- " + "\n- ".join(errors))


def register_intro(root: Path, name: str) -> str:
    """Intro di un register di polo (`goal.md`/`world.md`): dall'H1 al primo H2.

    È il contratto machine-readable dei register: l'intro è il polo in sintesi,
    reso fedelmente dalla home; le sezioni successive sono profondità on-demand.
    """
    text = (root / f"{name}.md").read_text(encoding="utf-8")
    pattern = re.compile(r"^# .+?\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    if not match or not match.group("body").strip():
        raise SystemExit(f"{name}.md: intro del register mancante (H1 → primo H2)")
    return match.group("body").strip()


def reveal_page(markdown: str, source: str, title: str, reveal_url: str, presentation: Path) -> str:
    """Una vista Reveal canonica da Markdown: stile, accento e link chiusi.

    È la resa di tutte le viste Reveal, e la usa anche un builder di dominio
    che parte da Markdown (`DECK_BUILDER` in `project.py`).
    """
    document = close_links(pandoc_ast(markdown), presentation, source)
    return pandoc_render(
        document,
        [
            "--standalone",
            "--to=revealjs",
            "--slide-level=2",
            "--css=assets/deck.css",
            "--css=assets/theme.css",
            *(f"--css=assets/{name}" for name in project.CSS_LOCALI),
            f"--metadata=pagetitle:{title}",
            f"--variable=revealjs-url:{reveal_url}",
            "--variable=theme:white",
            "--variable=width:1180",
            "--variable=height:740",
            "--variable=margin:0.05",
            "--variable=center:false",
            "--variable=slideNumber:true",
        ],
    )
