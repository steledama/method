#!/usr/bin/env python3
"""Parsing condiviso per viste generate e system image."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


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
        if stripped.startswith("#") or stripped.startswith("---"):
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


_INDEX_ENTRY = re.compile(r"^- \[[^\]]+\]\(([^)]+\.md)\)", re.M)


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


_GOAL_HEADING = re.compile(r"^#{2,4}\s+(\d+)[.)]\s", re.M)


def goal_keys(root: Path) -> set[str]:
    """Le chiavi che la colonna `Ob.` del plan può assumere, lette da `goal.md`.

    Il numero dell'obiettivo runtime, più `S` per il Goal di sviluppo: sono le
    chiavi del register, non una lista da tenere in sincronia (`kb/goal.md`).
    """
    goal = root / "goal.md"
    if not goal.exists():
        return set()
    text = goal.read_text(encoding="utf-8")
    keys = set(_GOAL_HEADING.findall(text))
    if re.search(r"^##\s+Goal di sviluppo\s*$", text, re.M):
        keys.add("S")
    return keys


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


def register_intro(root: Path, name: str) -> str:
    """Intro di un register di polo (`goal.md`/`world.md`): dall'H1 al primo H2.

    È il contratto machine-readable dei register: l'intro è il polo in sintesi,
    reso fedelmente dalla home; le sezioni successive sono profondità on-demand.
    """
    text = (root / f"{name}.md").read_text(encoding="utf-8")
    pattern = re.compile(r"^# .+?\n(?P<body>.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    if not match or not match.group("body").strip():
        raise SystemExit(f"{name}.md: intro del register mancante (H1 → primo H2)")
    return match.group("body").strip()
