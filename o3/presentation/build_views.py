"""Genera sorgenti Markdown derivate per le viste Reveal."""

from __future__ import annotations

import argparse
import re
from html import escape
from pathlib import Path

from sources import (
    check_plan_contract,
    check_verdict_contract,
    demote_headings,
    goal_titles,
    label,
    parse_plan,
    parse_task,
)


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


def goals_slide(root: Path, back: str, anchor: str) -> list[str]:
    lines = [f"## {label('goals')} {{#obiettivi}}", ""]
    for key, title in goal_titles(root).items():
        lines.append(f"- **{key}** — {title}")
    return lines + ["", f"[↩ {label(back)}](#/{anchor})", ""]


_WAKE_KEY = re.compile(r"\b[pw]\d+\b")


def plan_notes(root: Path) -> str:
    """Ciò che in `o1/plan.md` segue la tabella: legenda, risvegli, scadenze.

    Si prende per struttura, non per nome d'intestazione (le forme variano tra
    repo: paragrafi o liste, `p1` in codice o nudo). Le intestazioni scendono
    di un livello, così tutto sta in una slide sotto il titolo della vista.
    """
    lines = (root / "o1" / "plan.md").read_text(encoding="utf-8").splitlines()
    table = [index for index, line in enumerate(lines) if line.startswith("|")]
    if not table:
        return ""
    notes: list[str] = []
    fenced = False
    for line in lines[table[-1] + 1 :]:
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5}\s", line):
            line = "#" + line
        notes.append(line)
    return "\n".join(notes).strip()


def dependency_cell(dependency: str, notes: str) -> str:
    """Le chiavi `p<n>`/`w<n>` portano alla loro chiosa; una chiave senza voce rompe."""
    for key in _WAKE_KEY.findall(dependency):
        if not re.search(rf"\b{key}\b", notes):
            raise SystemExit(f"o1/plan.md: la chiave «{key}» non ha voce nella legenda del plan")
    return _WAKE_KEY.sub(
        lambda match: f'<a href="#/dipendenze">{match.group(0)}</a>', escape(dependency)
    )


def task_view(root: Path) -> str:
    lines: list[str] = []
    rows = parse_plan(root)
    check_plan_contract(root, rows)
    notes = plan_notes(root)
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
        (
            '<colgroup><col class="plan-cycle"><col class="plan-goal">'
            '<col class="plan-task"><col class="plan-dependency"></colgroup>'
        ),
        (
            '<thead><tr><th scope="col">Ciclo</th><th scope="col">Ob.</th>'
            '<th scope="col">Task</th><th scope="col">Dip.</th></tr></thead><tbody>'
        ),
    ]
    for index, row in enumerate(rows, 1):
        lines.append(
            f"<tr><td>{escape(row.ciclo or '—')}</td>"
            f"<td>{goal_links(row.obiettivo, markdown=False)}</td>"
            f'<td><a href="#/task-{index}">{escape(row.task)}</a></td>'
            f"<td>{dependency_cell(row.dependency, notes)}</td></tr>"
        )
    lines += [
        "</tbody></table></div>",
        "",
    ]
    if notes:
        lines += [
            f"## {label('wake')} {{#dipendenze}}",
            "",
            "::: plan-notes",
            notes,
            ":::",
            "",
            f"[↩ {label('plan')}](#/plan)",
            "",
        ]
    lines += goals_slide(root, "plan", "plan")

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
    """Indice dei fili nell'ordine di `i3/verdicts.md`, poi un filo per slide.

    Stessa forma della coda del plan (Ciclo · Ob. · Filo): ogni filo dichiara
    l'obiettivo che misura, e il contratto l'ha già verificato contro il
    register. Le intestazioni interne del filo scendono di un livello, così
    il filo resta una slide che scorre invece di spezzarsi in slide sciolte.
    """
    threads = check_verdict_contract(root)
    lines = [f"## {label('verdict')} {{#verdetti}}", ""]
    if not threads:
        return "\n".join(lines + ["Nessun filo aperto.", ""])
    lines += [
        '<div class="plan-overview" tabindex="0" role="region" aria-label="Indice dei fili">',
        "<table><caption>Fili aperti, misurati contro gli obiettivi</caption>",
        (
            '<colgroup><col class="plan-cycle"><col class="plan-goal">'
            '<col class="verdict-thread"></colgroup>'
        ),
        (
            '<thead><tr><th scope="col">Ciclo</th><th scope="col">Ob.</th>'
            '<th scope="col">Filo</th></tr></thead><tbody>'
        ),
    ]
    for index, thread in enumerate(threads, 1):
        lines.append(
            f"<tr><td>{escape(thread.ciclo)}</td>"
            f"<td>{goal_links(thread.obiettivo, markdown=False)}</td>"
            f'<td><a href="#/filo-{index}">{escape(re.sub(r"`", "", thread.title))}</a></td></tr>'
        )
    lines += ["</tbody></table></div>", ""]
    lines += goals_slide(root, "verdict", "verdetti")
    for index, thread in enumerate(threads, 1):
        meta = f"ciclo: `{thread.ciclo}` · obiettivo: {goal_links(thread.obiettivo, markdown=True)}"
        lines += [
            f"## {thread.title} {{#filo-{index}}}",
            "",
            "::: thread",
            meta,
            "",
            demote_headings(thread.body),
            ":::",
            "",
            f"[↩ {label('verdict')}](#/verdetti)",
            "",
        ]
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera Markdown per viste derivate")
    parser.add_argument("kind", choices=["tasks", "verdict"])
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    root = repo_root()
    content = task_view(root) if args.kind == "tasks" else verdict_view(root)
    args.output.write_text(content, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
