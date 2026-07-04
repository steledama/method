#!/usr/bin/env python3
"""Genera la home statica della system image: la matrice del ciclo d'azione.

La home rende i **due cicli annidati** (sviluppo / runtime, cfr. `nested-cycles`)
come matrice a 8 slot ciascuno — sei atti più i due poli — con uno switch in
testa che cambia *cosa è il Mondo* in fondo, e con esso Goal, poli e i sei atti.

Principio di copertura: **tutti gli slot appaiono sempre**. Uno slot è
*cliccabile* quando esiste una destinazione, *dimesso* quando non c'è ancora.
Nessuno slot è mai omesso: l'assenza si mostra, non si nasconde.

Solo il blocco CONFIG è specifico del repo: i poli e i sei atti puntano agli
artefatti reali di questo repo (o a `None` quando lo slot è ancora vuoto). La
logica di rendering, `presentation.py` e `assets/system-image.css` sono condivisi
e identici tra i repo adottanti — gli adottanti forkano la sola CONFIG.
"""

from __future__ import annotations

import html
from pathlib import Path

from presentation import canonical_readme_section

# --- CONFIG specifico del repo ------------------------------------------------

# Le due colonne del ciclo e le posizioni di slot, nell'ordine fedele a Norman:
# l'esecuzione scende dal Goal al Mondo (o1→o2→o3), la valutazione risale dal
# Mondo al Goal (i3→i2→i1). Questa geometria è condivisa tra tutti i repo.
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

# Per ciascun ciclo e slot: (href | None, etichetta-link, descrizione).
# href None ⇒ slot dimesso (nessuna destinazione ancora). La descrizione si
# mostra comunque, così lo slot vuoto resta leggibile.
SLOTS = {
    "dev": {
        "o1": (
            "../o1/plan.md",
            "plan.md",
            "Task aperti, prioritizzati, con dipendenze.",
        ),
        "o2": (
            "tasks.html",
            "vista Tasks",
            "La specifica concreta dei task del piano.",
        ),
        "o3": (
            "../o3/prescriptions.md",
            "prescriptions",
            "Prescrizioni ed esecutori deterministici del ciclo di sviluppo.",
        ),
        "i3": (
            "verdict.html",
            "vista Verdict",
            "I verdetti correnti per filo aperto.",
        ),
        "i2": (
            "interpretations.html",
            "deck",
            "La sintesi illustrata del metodo e dei nodi.",
        ),
        "i1": (
            "../o3/kb_tools.py",
            "kb-review",
            "Audit, backlink e copertura del catalogo via <code>kb_tools.py</code>.",
        ),
    },
    "runtime": {
        "o1": (
            None,
            None,
            "Protocollo d'audit periodico top-down degli adottanti: da costruire.",
        ),
        "o2": (
            "../i2/baricentro-kb-adottanti.md",
            "osservatorio",
            "Vista di decisione cross-repo: prima istanza, da estendere ai 4 domini.",
        ),
        "o3": (
            "../o3/prescriptions.md",
            "prescriptions",
            "Runbook di propagazione del canone agli adottanti.",
        ),
        "i3": (
            "../kb/adopter-comparison.md",
            "adopter-comparison",
            "Confronto cross-repo contro gli obiettivi; oggi sparso nei thread di verdict.",
        ),
        "i2": (
            "../i2/baricentro-kb-adottanti.md",
            "osservatorio",
            "Rilettura comparativa dei cataloghi <code>kb/</code> dei 4 domini.",
        ),
        "i1": (
            "../i1/perceptions.md",
            "perceptions",
            "Segnali metodologici che emergono dagli adottanti.",
        ),
    },
}

# Poli per ciclo. `goal` è prosa HTML breve (sommario navigazionale che punta al
# README/nodi, non una seconda fonte). `world` è prosa HTML; se None, il polo
# Mondo è derivato dalla sezione `### World` del README (la griglia adottanti).
POLES = {
    "dev": {
        "goal": (
            'Il Goal di <strong>sviluppo</strong> (<a href="../kb/development-goal.md">'
            "development-goal</a>): la posizione auspicata dell'artefatto-metodo "
            "lungo le dimensioni comuni — basso attrito di lettura, KB riflessiva "
            "coerente, loop di propagazione che si chiude."
        ),
        "world": (
            'Il Mondo di <strong>sviluppo</strong> (<a href="../kb/world.md">world</a>): '
            'l\'artefatto stesso — i nodi <a href="../kb/kb.md"><code>kb/</code></a> e la '
            "loro coerenza. È anche la macchina del ciclo runtime: qui passa la "
            "cucitura tra i due cicli."
        ),
    },
    "runtime": {
        "goal": (
            'Il Goal <strong>runtime</strong> (<a href="../kb/goal.md">goal</a>): '
            "custodire il metodo portabile e propagarne il canone agli adottanti "
            "senza micromanagiarne la coda — portabilità, indipendenza dal modello, "
            "adattabilità, autocorrezione, rigore delle fonti."
        ),
        "world": None,  # derivato dal README: la griglia dei quattro adottanti
    },
}

INTRO = (
    "I sei atti più i due poli del ciclo (cfr. "
    '<a href="../kb/action-cycle.md">action-cycle</a>), resi sui due cicli annidati '
    'di <code>metodo</code> (<a href="../kb/nested-cycles.md">nested-cycles</a>). Lo '
    "switch cambia <em>cosa è il Mondo</em> in fondo — e con esso Goal, poli e i "
    "sei atti. La geometria delle celle è la mappa-sorgente di <a "
    'href="../kb/action-cycle-matrix.md">action-cycle-matrix</a>; ogni slot è '
    "cliccabile dove c'è una destinazione, dimesso dove non c'è ancora."
)

MODES = (("dev", "Ciclo di sviluppo"), ("runtime", "Ciclo runtime"))


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
            name, href, desc = match.groups()
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


def toggle_html() -> str:
    rows = []
    for mode, label in MODES:
        active = ' class="is-active"' if mode == MODES[0][0] else ""
        rows.append(
            f'        <button type="button" data-mode="{mode}"{active}>'
            f"{html.escape(label)}</button>"
        )
    buttons = "\n".join(rows)
    return f"""      <div class="mode-toggle" role="tablist" aria-label="Ciclo annidato">
{buttons}
      </div>"""


def goal_pole_html() -> str:
    bodies = "\n".join(
        f'        <div class="{mode}-only"><p>{POLES[mode]["goal"]}</p></div>'
        for mode, _ in MODES
    )
    return f"""      <section class="pole pole-goal">
        <p class="kicker">Obiettivi · Goal</p>
{bodies}
      </section>"""


def world_pole_html(root: Path) -> str:
    bodies = []
    for mode, _ in MODES:
        world = POLES[mode]["world"]
        inner = f"<p>{world}</p>" if world else adopter_grid(root)
        bodies.append(f'        <div class="{mode}-only">{inner}</div>')
    joined = "\n".join(bodies)
    return f"""      <section class="pole pole-world">
        <p class="kicker">Mondo · World</p>
{joined}
      </section>"""


def slot_body(mode: str, key: str) -> str:
    href, label, desc = SLOTS[mode][key]
    if href:
        head = (
            f'<a class="slot-link" href="{html.escape(href, quote=True)}">'
            f"{html.escape(label)}</a>"
        )
    else:
        head = '<span class="slot-gap">vuoto</span>'
    return f'<div class="{mode}-only slot-body">{head}<small>{desc}</small></div>'


def card_html(key: str) -> str:
    empties = " ".join(
        f"data-{mode}-empty" for mode, _ in MODES if SLOTS[mode][key][0] is None
    )
    attr = f" {empties}" if empties else ""
    bodies = "\n".join(f"            {slot_body(mode, key)}" for mode, _ in MODES)
    return f"""          <div class="cycle-card" data-slot="{key}"{attr}>
            <span class="cycle-key">{html.escape(key)}</span>
            <strong>{html.escape(TITLES[key])}</strong>
{bodies}
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
  <body class="mode-dev">
    <header class="hero">
      <p class="kicker">Matrice del ciclo d'azione</p>
      <h1>{html.escape(title)}</h1>
      <p class="hero-copy">{INTRO}</p>
{toggle_html()}
    </header>

    <main>
{goal_pole_html()}
{cycle_html()}
{world_pole_html(root)}
    </main>

    <script>
      (function () {{
        const body = document.body;
        const buttons = document.querySelectorAll(".mode-toggle button");
        function setMode(mode) {{
          body.classList.toggle("mode-dev", mode === "dev");
          body.classList.toggle("mode-runtime", mode === "runtime");
          buttons.forEach((b) =>
            b.classList.toggle("is-active", b.dataset.mode === mode),
          );
        }}
        buttons.forEach((b) =>
          b.addEventListener("click", () => setMode(b.dataset.mode)),
        );
      }})();
    </script>
  </body>
</html>
"""


def main() -> None:
    root = repo_root()
    (root / "presentation" / "index.html").write_text(render(root), encoding="utf-8")


if __name__ == "__main__":
    main()
