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


@dataclass(frozen=True)
class TaskDetail:
    path: Path
    title: str
    data: str
    stato: str
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


def parse_plan(root: Path) -> list[PlanRow]:
    plan = root / "o1" / "plan.md"
    text = plan.read_text(encoding="utf-8")
    detail_links = {
        match.group(1).strip(): match.group(2).removeprefix("../")
        for match in re.finditer(r"- \[([^\]]+)\]\(((?:\.\./)?o2/[^)]+\.md)\)", text)
    }
    rows: list[PlanRow] = []
    position = 0
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [
            cell.strip().replace("<<PIPE>>", "|")
            for cell in line.replace(r"\|", "<<PIPE>>").strip().strip("|").split("|")
        ]
        if len(cells) not in {2, 3}:
            continue
        if cells[0] in {"#", "Task"} or set(cells[0]) == {"-"}:
            continue
        if len(cells) == 3 and cells[1] in {"dev", "runtime"}:
            position += 1
            position_value, task_cell, dependency = str(position), cells[0], cells[2]
        elif len(cells) == 3:
            position_value, task_cell, dependency = cells
        else:
            position += 1
            position_value, task_cell, dependency = str(position), cells[0], cells[1]
        link = re.search(r"\[([^\]]+)\]\(((?:\.\./)?o2/[^)]+\.md)\)", task_cell)
        task = link.group(1) if link else task_cell
        source = (
            link.group(2).removeprefix("../")
            if link
            else _detail_source(detail_links, task)
        )
        rows.append(
            PlanRow(
                position=position_value,
                task=task,
                dependency=dependency,
                source=source,
            )
        )
    return rows


def parse_task(root: Path, relative: str) -> TaskDetail:
    path = root / relative
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if not meta.get("stato"):
        raise SystemExit(f"{relative}: frontmatter incompleto (stato)")
    return TaskDetail(
        path=path,
        title=first_h1(body, path.stem),
        data=meta.get("data", "—"),
        stato=meta["stato"],
        sintesi=meta.get("sintesi") or first_paragraph(body),
    )


def canonical_readme_section(root: Path, heading: str) -> str:
    text = (root / "README.md").read_text(encoding="utf-8")
    pattern = re.compile(
        rf"^### {re.escape(heading)}\n(?P<body>.*?)(?=^#{{2,3}} |\Z)",
        re.M | re.S,
    )
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"README.md: sezione canonica mancante: {heading}")
    return match.group("body").strip()
