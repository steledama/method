#!/usr/bin/env python3
"""Genera sorgenti Markdown derivate per le viste Reveal."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from presentation import check_plan_contract, parse_plan, parse_task


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def task_view(root: Path) -> str:
    lines: list[str] = []
    rows = parse_plan(root)
    if not rows:
        lines += ["## Nessun task aperto", "", "La coda operativa è vuota.", ""]
        return "\n".join(lines).rstrip() + "\n"

    check_plan_contract(root, rows)

    for row in rows:
        # Una riga senza dettaglio `o2/` è legittima (`kb/tasks.md`: il file
        # serve quando serve contesto) e si rende con i soli dati del plan;
        # ciò che non è legittimo — e che il contratto ha già intercettato — è
        # saltarla in silenzio.
        task = parse_task(root, row.source) if row.source else None
        meta = [f"ciclo: `{task.ciclo if task else row.ciclo or '—'}`"]
        if row.obiettivo:
            meta.append(f"obiettivo: `{row.obiettivo}`")
        meta.append(f"dipendenza: `{row.dependency}`")
        lines += [
            f"## {task.title if task else row.task}",
            "",
            " · ".join(meta),
            "",
            task.sintesi if task else "Riga di piano senza dettaglio in `o2/`.",
            "",
        ]
        if row.source:
            lines += [f"Sorgente: [`{row.source}`](../{row.source})", ""]
    return "\n".join(lines).rstrip() + "\n"


def verdict_view(root: Path) -> str:
    parts: list[str] = []
    for path in sorted((root / "i3").glob("*.md")):
        if path.name == "verdicts.md":
            continue
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            text = text.split("---\n", 2)[2].lstrip()
        text = re.sub(r"^# ", "## ", text, count=1, flags=re.M)
        parts += [text.rstrip(), ""]
    return "\n".join(parts).rstrip() + "\n"


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
