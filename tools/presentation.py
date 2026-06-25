#!/usr/bin/env python3
"""Parsing condiviso per viste generate e system image."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PlanRow:
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


def parse_plan(root: Path) -> list[PlanRow]:
    plan = root / "plan.md"
    text = plan.read_text(encoding="utf-8")
    detail_links = {
        match.group(1).strip(): match.group(2)
        for match in re.finditer(r"- \[([^\]]+)\]\((tasks/[^)]+\.md)\)", text)
    }
    rows: list[PlanRow] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2 or cells[0] == "Task" or set(cells[0]) <= {"-"}:
            continue
        link = re.search(r"\[([^\]]+)\]\((tasks/[^)]+\.md)\)", cells[0])
        task = link.group(1) if link else cells[0]
        rows.append(
            PlanRow(
                task=task,
                dependency=cells[1],
                source=link.group(2) if link else detail_links.get(task),
            )
        )
    return rows


def parse_task(root: Path, relative: str) -> TaskDetail:
    path = root / relative
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    missing = [key for key in ("data", "stato", "sintesi") if not meta.get(key)]
    if missing:
        raise SystemExit(f"{relative}: frontmatter incompleto ({', '.join(missing)})")
    return TaskDetail(
        path=path,
        title=first_h1(body, path.stem),
        data=meta["data"],
        stato=meta["stato"],
        sintesi=meta["sintesi"],
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
