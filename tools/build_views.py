#!/usr/bin/env python3
"""Genera sorgenti Markdown derivate per le viste Reveal."""

from __future__ import annotations

import argparse
from pathlib import Path

from presentation import parse_plan, parse_task


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def task_view(root: Path) -> str:
    lines = [
        "% Tasks",
        "% metodo",
        "",
        "# Tasks",
        "",
        "Coda operativa aperta, derivata da `plan.md` e dai file in `tasks/`.",
        "",
    ]
    for row in parse_plan(root):
        if not row.source:
            continue
        task = parse_task(root, row.source)
        lines += [
            f"## {task.title}",
            "",
            f"**#{row.position}** · dipendenza: `{row.dependency}` · stato: `{task.stato}` · aperto: `{task.data}`",
            "",
            task.sintesi,
            "",
            f"Sorgente: [`{row.source}`](../{row.source})",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def verdict_view(root: Path) -> str:
    text = (root / "verdict.md").read_text(encoding="utf-8")
    text = text.replace("# verdict.md", "% Verdict\n% metodo", 1)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera Markdown per viste derivate")
    parser.add_argument("kind", choices=["tasks", "verdict"])
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    root = repo_root()
    content = task_view(root) if args.kind == "tasks" else verdict_view(root)
    args.output.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
