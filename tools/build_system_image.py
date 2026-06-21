#!/usr/bin/env python3
"""Genera la home statica della system image."""

from __future__ import annotations

import html
import re
from pathlib import Path

from presentation import canonical_readme_section, parse_plan, parse_task


VIEW_PATHS = {
    "tasks": "views/tasks.html",
    "verdict": "views/verdict.html",
    "interpretations": "views/interpretations.html",
}


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
        raise SystemExit("README.md World: nessun adottante esplicito trovato")
    return "\n".join(intro).strip(), items, "\n".join(outro).strip()


def plan_cards(root: Path) -> str:
    cards: list[str] = []
    for row in parse_plan(root):
        detail = parse_task(root, row.source) if row.source else None
        href = html.escape(row.source, quote=True) if row.source else None
        title = html.escape(row.task)
        summary = inline_markdown(detail.sintesi) if detail else ""
        source = (
            f'<a class="source-link" href="{href}">sorgente</a>'
            if href is not None
            else ""
        )
        cards.append(
            "\n".join(
                [
                    '<article class="plan-item">',
                    f'<div class="plan-index">#{html.escape(row.position)}</div>',
                    f"<h3>{title}</h3>",
                    f"<p>{summary}</p>",
                    '<div class="plan-meta">',
                    f"<span>Dip. {html.escape(row.dependency)}</span>",
                    source,
                    "</div>",
                    "</article>",
                ]
            )
        )
    if not cards:
        return '<p class="empty-state">Nessun task aperto.</p>'
    return "\n".join(cards)


def cycle_card(
    key: str,
    label: str,
    title: str,
    description: str,
    href: str | None = None,
    muted: bool = False,
) -> str:
    classes = "cycle-card"
    if muted:
        classes += " muted"
    content = "\n".join(
        [
            f'<span class="cycle-key">{html.escape(key)}</span>',
            f"<strong>{html.escape(title)}</strong>",
            f"<small>{html.escape(description)}</small>",
        ]
    )
    if href:
        return f'<a class="{classes}" href="{html.escape(href, quote=True)}" aria-label="{html.escape(label, quote=True)}">\n{content}\n</a>'
    return f'<div class="{classes}" aria-label="{html.escape(label, quote=True)}">\n{content}\n</div>'


def render(root: Path) -> str:
    title = readme_title(root)
    goal = canonical_readme_section(root, "Goal")
    world = canonical_readme_section(root, "World")
    world_intro, adopters, world_outro = world_items(world)

    adopter_html = "\n".join(
        "\n".join(
            [
                '<article class="world-item">',
                f'<a href="{html.escape(href, quote=True)}">{html.escape(name)}</a>',
                f"<p>{inline_markdown(description)}</p>",
                "</article>",
            ]
        )
        for name, href, description in adopters
    )

    return f"""<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)} · system image</title>
    <link rel="stylesheet" href="assets/system-image.css" />
  </head>
  <body class="home">
    <header class="home-hero">
      <p class="kicker">GOAL</p>
      <h1>{html.escape(title)}</h1>
      <div class="hero-copy">
        {paragraphs(goal)}
      </div>
    </header>

    <main>
      <section class="cycle" aria-label="Ciclo di azione">
        <div class="cycle-pole top">GOAL</div>
        <div class="cycle-grid">
          <div class="cycle-column execution" aria-label="Arco di esecuzione">
            <h2>Esecuzione</h2>
            {cycle_card("o1", "Plan", "Plan", "Task aperti e dipendenze", "#plan")}
            {cycle_card("o2", "Specify", "Specify", "Vista Tasks", VIEW_PATHS["tasks"])}
            {cycle_card("o3", "Perform", "Perform", "Prescrizioni on-demand", None, True)}
          </div>
          <div class="cycle-column evaluation" aria-label="Arco di valutazione">
            <h2>Valutazione</h2>
            {cycle_card("i3", "Compare", "Compare", "Vista Verdict", VIEW_PATHS["verdict"])}
            {cycle_card("i2", "Interpret", "Interpret", "Vista Interpretations", VIEW_PATHS["interpretations"])}
            {cycle_card("i1", "Perceive", "Perceive", "Segnali on-demand", None, True)}
          </div>
        </div>
        <div class="cycle-pole bottom">WORLD</div>
      </section>

      <section id="plan" class="home-section">
        <div class="section-heading">
          <p class="kicker">PLAN</p>
          <h2>Task aperti</h2>
        </div>
        <div class="plan-list">
          {plan_cards(root)}
        </div>
      </section>

      <section class="home-section world-section">
        <div class="section-heading">
          <p class="kicker">WORLD</p>
          <h2>Adottanti</h2>
          {paragraphs(world_intro)}
        </div>
        <div class="world-grid">
          {adopter_html}
        </div>
        <div class="world-note">
          {paragraphs(world_outro)}
        </div>
      </section>
    </main>
  </body>
</html>
"""


def main() -> None:
    root = repo_root()
    (root / "index.html").write_text(render(root), encoding="utf-8")


if __name__ == "__main__":
    main()
