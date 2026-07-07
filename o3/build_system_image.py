#!/usr/bin/env python3
"""Genera la home statica della system image: la mappa del ciclo d'azione.

La home orienta sul Goal runtime, sui sei atti del ciclo e sul Mondo runtime.
Runtime cycle e development meta-cycle restano nel modello (cfr. `development-meta-cycle`), ma la home non
li espone come modalità: ogni slot ha un solo collegamento primario.
"""

from __future__ import annotations

import html
from pathlib import Path

from presentation import canonical_readme_section

# --- CONFIG specifico del repo ------------------------------------------------

# Le due colonne del ciclo e le posizioni di slot, nell'ordine fedele a Norman:
# l'esecuzione scende dal Goal al Mondo (o1->o2->o3), la valutazione risale dal
# Mondo al Goal (i3->i2->i1).
COLUMNS = {
    "Esecuzione": ("scende ↓", ["o1", "o2", "o3"]),
    "Valutazione": ("↑ risale", ["i3", "i2", "i1"]),
}

TITLES = {
    "o1": "Piano",
    "o2": "Compiti",
    "o3": "Prescrizioni",
    "i1": "Percezioni",
    "i2": "Interpretazioni",
    "i3": "Confronti",
}

# Per ciascuno slot: (href, descrizione).
SLOTS = {
    "o1": ("../o1/plan.md", "Task aperti, prioritizzati, con dipendenze."),
    "o2": ("tasks.html", "La specifica concreta dei task del piano."),
    "o3": (
        "../o3/prescriptions.md",
        "Prescrizioni ed esecutori deterministici del metodo.",
    ),
    "i3": ("verdict.html", "I verdetti correnti per filo aperto."),
    "i2": ("interpretations.html", "La sintesi illustrata del metodo e dei nodi."),
    "i1": (
        "../i1/perceptions.md",
        "I segnali catturati dallo stadio Perceive.",
    ),
}

RUNTIME_GOAL = (
    "Coltivare il metodo e propagarne il canone agli adottanti custodendo la "
    "portabilità, indipendenza dal modello, adattabilità, autocorrezione e "
    "rigore delle fonti."
)

GITHUB_OWNER = "steledama"
GITHUB_REPOS = {
    "bi": "https://github.com/tt-sviluppo/bi",
}


# --- Helpers ------------------------------------------------------------------


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def readme_title(root: Path) -> str:
    for line in (root / "README.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise SystemExit("README.md: H1 mancante")


def adopter_grid(root: Path) -> str:
    """Griglia degli adottanti derivata dalla sezione `### World` del README."""
    import re

    world = canonical_readme_section(root, "World")
    cards: list[str] = []
    for line in world.splitlines():
        match = re.match(r"- \*\*\[([^\]]+)\]\(([^)]+)\)\*\* — (.+)", line)
        if match:
            name, _href, desc = match.groups()
            href = GITHUB_REPOS.get(name, f"https://github.com/{GITHUB_OWNER}/{name}")
            cards.append(
                f"""          <article class="world-item">
            <a href="{html.escape(href, quote=True)}">{html.escape(name)}</a>
            <p>{html.escape(desc)}</p>
          </article>"""
            )
    if not cards:
        return ""
    grid = "\n".join(cards)
    return f'        <div class="world-grid">\n{grid}\n        </div>'


# --- Sezioni ------------------------------------------------------------------


def goal_pole_html() -> str:
    return f"""      <section class="pole pole-goal">
        <p class="kicker">Obiettivi · Goal</p>
        <p>{RUNTIME_GOAL}</p>
      </section>"""


def world_pole_html(root: Path) -> str:
    return f"""      <section class="pole pole-world">
        <p class="kicker">Mondo · World</p>
{adopter_grid(root)}
      </section>"""


def card_html(key: str) -> str:
    href, desc = SLOTS[key]
    return f"""          <div class="cycle-card" data-slot="{key}">
            <span class="cycle-key">{html.escape(key)}</span>
            <h3>
              <a class="card-title" href="{html.escape(href, quote=True)}">{html.escape(TITLES[key])}</a>
            </h3>
            <small>{desc}</small>
          </div>"""


def cycle_html() -> str:
    columns = []
    for name, (direction, keys) in COLUMNS.items():
        cards = "\n".join(card_html(key) for key in keys)
        columns.append(
            f'          <div class="cycle-column">\n'
            f"            <h2>{html.escape(name)} "
            f'<span class="arc-dir">{html.escape(direction)}</span></h2>\n'
            f"{cards}\n          </div>"
        )
    grid = "\n".join(columns)
    return f"""      <section class="cycle" aria-label="I sei atti del ciclo">
        <div class="cycle-grid">
{grid}
        </div>
      </section>"""


def render(root: Path) -> str:
    title = readme_title(root)
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
      <p class="kicker">Artefatto · Artifact</p>
      <h1>{html.escape(title)}</h1>
    </header>

    <main>
{goal_pole_html()}
{cycle_html()}
{world_pole_html(root)}
    </main>
  </body>
</html>
"""


def main() -> None:
    root = repo_root()
    (root / "presentation" / "index.html").write_text(render(root), encoding="utf-8")


if __name__ == "__main__":
    main()
