#!/usr/bin/env python3
"""Genera la home statica della system image (layout condiviso, look lean).

Solo il blocco CONFIG è specifico del repo: deck-band e card del ciclo puntano
agli artefatti reali di questo repo. La logica di rendering, `presentation.py` e
`assets/system-image.css` sono condivisi e identici tra i repo adottanti.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from presentation import canonical_readme_section, parse_plan, parse_task


# --- CONFIG specifico del repo ------------------------------------------------

DECK_BAND = {
    "kicker": "View principale",
    "title": "Interpretazioni",
    "description": (
        "Deck Reveal delle sintesi interpretative i2/o2 del metodo, "
        "generato dal sorgente corposo in <code>interpretations/</code>."
    ),
    "href": "views/interpretations.html",
    "cta": "Apri deck",
}

CYCLE = {
    "Esecuzione": [
        ("o1", "Plan", "Task aperti, dipendenze e ordine di esecuzione.", "#plan"),
        (
            "o2",
            "Specify",
            "Vista Tasks: la coda operativa derivata.",
            "views/tasks.html",
        ),
    ],
    "Valutazione": [
        (
            "i2",
            "Interpret",
            "Vista Interpretations: le sintesi i2/o2.",
            "views/interpretations.html",
        ),
        (
            "i3",
            "Compare",
            "Vista Verdict: i verdetti correnti per filo aperto.",
            "views/verdict.html",
        ),
    ],
}

# World statico (card descrittive, non soggette a drift). Se None, la sezione
# World viene derivata dalla sezione `### World` del README.
WORLD = None


# --- Helpers ------------------------------------------------------------------


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)

    def link(match: re.Match[str]) -> str:
        label = match.group(1)
        href = html.escape(match.group(2), quote=True)
        return f'<a href="{href}">{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, escaped)


def paragraphs(markdown: str) -> str:
    blocks = [block.strip().replace("\n", " ") for block in markdown.split("\n\n")]
    return "\n".join(f"<p>{inline_markdown(block)}</p>" for block in blocks if block)


def readme_title(root: Path) -> str:
    for line in (root / "README.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise SystemExit("README.md: H1 mancante")


def world_items(world: str) -> tuple[str, list[tuple[str, str, str]], str]:
    intro: list[str] = []
    items: list[tuple[str, str, str]] = []
    outro: list[str] = []
    in_list = False
    for line in world.splitlines():
        if line.startswith("- "):
            in_list = True
            match = re.match(r"- \*\*\[([^\]]+)\]\(([^)]+)\)\*\* — (.+)", line)
            if not match:
                raise SystemExit(f"README.md World: voce non riconosciuta: {line}")
            items.append((match.group(1), match.group(2), match.group(3)))
        elif in_list:
            outro.append(line)
        else:
            intro.append(line)
    if not items:
        return world.strip(), [], ""
    return "\n".join(intro).strip(), items, "\n".join(outro).strip()


# --- Sezioni ------------------------------------------------------------------


def deck_band_html() -> str:
    if not DECK_BAND:
        return ""
    return f"""      <section class="deck-band">
        <div class="section">
          <article class="deck-card">
            <div>
              <p class="kicker">{html.escape(DECK_BAND["kicker"])}</p>
              <h2>{html.escape(DECK_BAND["title"])}</h2>
              <p>{DECK_BAND["description"]}</p>
            </div>
            <a class="deck-link" href="{html.escape(DECK_BAND["href"], quote=True)}">{html.escape(DECK_BAND["cta"])}</a>
          </article>
        </div>
      </section>
"""


def cycle_card(key: str, title: str, description: str, href: str | None) -> str:
    content = "\n".join(
        [
            f'            <span class="cycle-key">{html.escape(key)}</span>',
            f"            <strong>{html.escape(title)}</strong>",
            f"            <small>{html.escape(description)}</small>",
        ]
    )
    if href:
        return (
            f'          <a class="cycle-card" href="{html.escape(href, quote=True)}">\n'
            f"{content}\n          </a>"
        )
    return f'          <div class="cycle-card muted">\n{content}\n          </div>'


def cycle_html() -> str:
    columns = []
    for name, cards in CYCLE.items():
        rendered = "\n".join(cycle_card(*card) for card in cards)
        columns.append(
            f'          <div class="cycle-column">\n'
            f"            <h2>{html.escape(name)}</h2>\n"
            f"{rendered}\n          </div>"
        )
    grid = "\n".join(columns)
    return f"""      <section class="cycle" aria-label="Ciclo dell'artefatto">
        <div class="cycle-grid">
{grid}
        </div>
      </section>
"""


def task_items(root: Path) -> str:
    cards: list[str] = []
    for row in parse_plan(root):
        detail = parse_task(root, row.source) if row.source else None
        title = html.escape(row.task)
        summary = (
            f"\n            <p>{inline_markdown(detail.sintesi)}</p>"
            if detail and detail.sintesi
            else ""
        )
        meta_bits = [f"Dip. {html.escape(row.dependency)}"]
        if row.source:
            href = html.escape(row.source, quote=True)
            meta_bits.append(f'<a class="source-link" href="{href}">sorgente</a>')
        meta = " · ".join(meta_bits)
        cards.append(
            f"""          <article class="task-item">
            <h3>{title}</h3>
            <p class="task-meta">{meta}</p>{summary}
          </article>"""
        )
    if not cards:
        return '          <p class="empty-state">Nessun task aperto.</p>'
    return "\n".join(cards)


def world_html(root: Path) -> str:
    if WORLD:
        cards = "\n".join(
            f"""          <article class="world-item">
            <h3>{html.escape(title)}</h3>
            <p>{desc}</p>
          </article>"""
            for title, desc in WORLD["items"]
        )
        return f"""      <section class="section">
        <p class="kicker">World</p>
        <h2>{html.escape(WORLD["heading"])}</h2>
        <div class="world-grid">
{cards}
        </div>
      </section>
"""
    world = canonical_readme_section(root, "World")
    intro, items, outro = world_items(world)
    title = "Adottanti" if items else "Mondo"
    if items:
        cards = "\n".join(
            f"""          <article class="world-item">
            <a href="{html.escape(href, quote=True)}">{html.escape(name)}</a>
            <p>{inline_markdown(description)}</p>
          </article>"""
            for name, href, description in items
        )
        body = f'        <div class="world-grid">\n{cards}\n        </div>'
    else:
        body = "\n".join(f"        {line}" for line in paragraphs(intro).splitlines())
    note = (
        f'\n        <div class="world-note">\n{paragraphs(outro)}\n        </div>'
        if outro
        else ""
    )
    intro_html = (
        "\n".join(f"          {p}" for p in paragraphs(intro).splitlines())
        if items and intro
        else ""
    )
    return f"""      <section class="section">
        <p class="kicker">World</p>
        <h2>{title}</h2>
{intro_html}
{body}{note}
      </section>
"""


def render(root: Path) -> str:
    title = readme_title(root)
    goal = canonical_readme_section(root, "Goal")
    return f"""<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)} · system image</title>
    <link rel="stylesheet" href="assets/system-image.css" />
  </head>
  <body>
    <header class="hero">
      <p class="kicker">Goal</p>
      <h1>{html.escape(title)}</h1>
      <div class="hero-copy">
        {paragraphs(goal)}
      </div>
    </header>

    <main>
{deck_band_html()}
{cycle_html()}
      <section id="plan" class="section">
        <p class="kicker">Plan</p>
        <h2>Task aperti</h2>
        <div class="task-list">
{task_items(root)}
        </div>
      </section>

{world_html(root)}    </main>
  </body>
</html>
"""


def main() -> None:
    root = repo_root()
    (root / "index.html").write_text(render(root), encoding="utf-8")


if __name__ == "__main__":
    main()
