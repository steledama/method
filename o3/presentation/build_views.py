"""Genera sorgenti Markdown derivate per le viste Reveal."""

from __future__ import annotations

import argparse
import re
from html import escape
from pathlib import Path

from sources import check_plan_contract, goal_titles, label, parse_plan, parse_task


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def goal_links(obiettivo: str | None, markdown: bool) -> str:
    """Ogni chiave della colonna `Ob.` porta alla legenda degli obiettivi.

    La legenda è una slide della vista, con i titoli letti da `goal.md`: il
    legame task→obiettivo resta dentro `presentation/` (compartimento
    stagno). Il contratto del plan ha già verificato che ogni chiave esista.
    """
    if not obiettivo:
        return "—"
    links = []
    for key in (part.strip() for part in obiettivo.split(",")):
        if markdown:
            links.append(f"[`{key}`](#/obiettivi)")
        else:
            links.append(f'<a href="#/obiettivi">{escape(key)}</a>')
    return ", ".join(links)


def goals_slide(root: Path) -> list[str]:
    lines = [f"## {label('goals')} {{#obiettivi}}", ""]
    for key, title in goal_titles(root).items():
        lines.append(f"- **{key}** — {title}")
    return lines + ["", f"[↩ {label('plan')}](#/plan)", ""]


def task_view(root: Path) -> str:
    lines: list[str] = []
    rows = parse_plan(root)
    check_plan_contract(root, rows)
    if not rows:
        lines += [f"## {label('plan')} {{#plan}}", "", "Nessun task aperto: la coda è vuota.", ""]
        return "\n".join(lines).rstrip() + "\n"

    # Gli indirizzi sono locali alla vista: tabella e dettagli li condividono,
    # senza imitare gli auto-identifier di Pandoc (accenti, markup, collisioni).
    lines += [
        f"## {label('plan')} {{#plan}}",
        "",
        '<div class="plan-overview" tabindex="0" role="region" aria-label="Coda dei task">',
        "<table><caption>Task in ordine di esecuzione</caption>",
        '<colgroup><col class="plan-cycle"><col class="plan-goal">'
        '<col class="plan-task"><col class="plan-dependency"></colgroup>',
        '<thead><tr><th scope="col">Ciclo</th><th scope="col">Ob.</th>'
        '<th scope="col">Task</th><th scope="col">Dip.</th></tr></thead><tbody>',
    ]
    for index, row in enumerate(rows, 1):
        lines.append(
            f"<tr><td>{escape(row.ciclo or '—')}</td>"
            f"<td>{goal_links(row.obiettivo, markdown=False)}</td>"
            f'<td><a href="#/task-{index}">{escape(row.task)}</a></td>'
            f"<td>{escape(row.dependency)}</td></tr>"
        )
    lines += [
        "</tbody></table></div>",
        "",
    ]
    lines += goals_slide(root)

    for index, row in enumerate(rows, 1):
        # Una riga senza dettaglio `o2/` è legittima (`kb/tasks.md`: il file
        # serve quando serve contesto) e si rende con i soli dati del plan;
        # ciò che non è legittimo — e che il contratto ha già intercettato — è
        # saltarla in silenzio.
        task = parse_task(root, row.source) if row.source else None
        meta = [f"ciclo: `{task.ciclo if task else row.ciclo or '—'}`"]
        if row.obiettivo:
            meta.append(f"obiettivo: {goal_links(row.obiettivo, markdown=True)}")
        meta.append(f"dipendenza: `{row.dependency}`")
        lines += [
            f"## {task.title if task else row.task} {{#task-{index}}}",
            "",
            " · ".join(meta),
            "",
            task.sintesi if task else "Riga di piano senza dettaglio in `o2/`.",
            "",
        ]
        lines += [f"[↩ {label('plan')}](#/plan)", ""]
    return "\n".join(lines).rstrip() + "\n"


def verdict_view(root: Path) -> str:
    parts: list[str] = []
    for path in sorted((root / "i3").glob("*.md")):
        if path.name == "verdicts.md":
            continue
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            text = text.split("---\n", 2)[2].lstrip()
        text = re.sub(r"^# ", "## ", text, count=1, flags=re.MULTILINE)
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
