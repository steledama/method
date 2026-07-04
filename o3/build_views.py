#!/usr/bin/env python3
"""Genera sorgenti Markdown derivate per le viste Reveal."""

from __future__ import annotations

import argparse
import re
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
        "Coda operativa aperta, derivata da `o1/plan.md` e dai file in `o2/`.",
        "",
    ]
    rows = parse_plan(root)
    if not rows:
        lines += ["## Nessun task aperto", "", "La coda operativa è vuota.", ""]
        return "\n".join(lines).rstrip() + "\n"

    for row in rows:
        if not row.source:
            continue
        task = parse_task(root, row.source)
        lines += [
            f"## {task.title}",
            "",
            f"dipendenza: `{row.dependency}` · stato: `{task.stato}` · aperto: `{task.data}`",
            "",
            task.sintesi,
            "",
            f"Sorgente: [`{row.source}`](../{row.source})",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def verdict_view(root: Path) -> str:
    # Prima slide di livello 2 (non blocco-titolo pandoc `%`, non H1): titolo e
    # paragrafi introduttivi restano su un'unica slide, mentre i fili `##` restano
    # slide orizzontali piatte. Con `%` pandoc generava una title-slide separata
    # seguita dall'intro come slide a sé; con un H1 avrebbe annidato i fili come
    # slide verticali.
    parts = [
        "% Verdict",
        "% metodo",
        "",
        "# Verdict",
        "",
        "Verdetti correnti per filo aperto, derivati dai file in `i3/`.",
        "",
    ]
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
