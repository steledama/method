"""Genera la home statica della system image: la mappa del ciclo d'azione.

La home orienta sul Goal runtime, sui sei atti del ciclo e sul Mondo runtime.
Runtime cycle e development meta-cycle restano nel modello (cfr. `development-meta-cycle`), ma la home non
li espone come modalità: ogni slot ha un solo collegamento primario.
Il CSS condiviso fra i repo resta il contratto minimale delle classi emesse qui,
non un archivio di componenti previsionali.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import project
from sources import (
    goal_anchor,
    goal_titles,
    inline_markdown,
    label,
    pending_proposals,
    register_intro,
)

# --- Struttura della home, canone ------------------------------------------------

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

# Per ciascuno slot: (href, descrizione). L'href è l'indice della collezione,
# reso allo stesso path del repo. La descrizione è quella del canone: il
# repo la sostituisce in `project.py` (`DESCRIZIONI`), non qui, così questo
# file resta uguale in ogni repo.
SLOTS = {
    "o1": ("o1/plan.html", "Task aperti, prioritizzati, con dipendenze."),
    "o2": ("o2/tasks.html", "La specifica concreta dei task del piano."),
    "o3": ("o3/prescriptions.html", "Prescrizioni ed esecutori deterministici."),
    "i3": ("i3/verdicts.html", "I verdetti correnti per filo aperto."),
    "i2": ("i2/interpretations.html", "Le sintesi che interpretano i segnali."),
    "i1": ("i1/perceptions.html", "I segnali catturati dallo stadio Perceive."),
}


def slot_description(key: str) -> str:
    """La descrizione dello slot: quella di `project.py` se c'è, o il canone.

    `getattr` regge un `project.py` scritto prima del campo.
    """
    local = getattr(project, "DESCRIZIONI", {})
    unknown = sorted(set(local) - set(SLOTS))
    if unknown:
        raise SystemExit(f"project.py: DESCRIZIONI nomina slot inesistenti: {', '.join(unknown)}")
    return local.get(key, SLOTS[key][1])


# --- Helpers ------------------------------------------------------------------


def readme_title(root: Path) -> str:
    for line in (root / "README.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise SystemExit("README.md: H1 mancante")


_INCIPIT = re.compile(r"<!--\s*incipit\s*-->(?P<body>.*?)<!--\s*/incipit\s*-->", re.DOTALL)
# Righe che non aprono un paragrafo di prosa: titoli, liste, codice, HTML, immagini, tabelle.
_NOT_PROSE = re.compile(r"^(#|[-*+] |\d+[.)] |```|~~~|<|!\[|\||>)")


def readme_incipit(root: Path) -> str | None:
    """L'incipit del README, in Markdown: cosa fa l'artefatto, in tre o quattro righe.

    È il blocco fra `<!-- incipit -->` e `<!-- /incipit -->`, se c'è, oppure
    il primo paragrafo di prosa subito sotto l'H1. La home della vista lo
    mostra sotto il titolo e lo pubblica in `<meta name="description">`, da
    cui lo legge la home del gruppo.
    """
    text = (root / "README.md").read_text(encoding="utf-8")
    marked = _INCIPIT.search(text)
    if marked:
        body = " ".join(line.strip() for line in marked.group("body").splitlines() if line.strip())
        return body or None
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if start is None:
        return None
    para: list[str] = []
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if not stripped:
            if para:
                break
            continue
        if not para and _NOT_PROSE.match(stripped):
            return None
        para.append(stripped)
    return " ".join(para) or None


def emphasis(rendered: str) -> str:
    """Il corsivo `_x_` o `*x*`, che `inline_markdown` lascia com'è."""
    return re.sub(r"(?<![\w*])([_*])(?=\S)([^_*<]+?)(?<=\S)\1(?![\w*])", r"<em>\2</em>", rendered)


def plain_text(markdown: str) -> str:
    """Il Markdown inline ridotto a testo: link al loro testo, marcatori tolti."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    text = re.sub(r"(\*\*|__|\*|_|`)(?=\S)(.+?)(?<=\S)\1", r"\2", text)
    return re.sub(r"\s+", " ", text).strip()


def render_block(block: str) -> str:
    """Rende un blocco markdown fedele: prosa in <p>, liste puntate in <ul>,
    e il misto lead-in + lista dentro lo stesso blocco."""
    parts: list[str] = []
    para: list[str] = []
    items: list[str] = []

    def flush_para() -> None:
        if para:
            parts.append(f"<p>{inline_markdown(' '.join(para))}</p>")
            para.clear()

    def flush_list() -> None:
        if items:
            lis = "".join(f"<li>{inline_markdown(item)}</li>" for item in items)
            parts.append(f"<ul>{lis}</ul>")
            items.clear()

    for raw in block.splitlines():
        line = raw.strip()
        match = re.match(r"^[-*]\s+(.*)$", line)
        if match:
            flush_para()
            items.append(match.group(1))
        elif line:
            flush_list()
            para.append(line)
    flush_para()
    flush_list()
    return "\n".join(parts)


def render_markdown(markdown: str) -> str:
    blocks = (block.strip() for block in markdown.split("\n\n"))
    return "\n".join(render_block(block) for block in blocks if block)


def pole_links(items: list[tuple[str, str]], label: str) -> str:
    if not items:
        return ""
    links = "\n".join(
        f'          <a href="{html.escape(href, quote=True)}">{inline_markdown(title)}</a>'
        for title, href in items
    )
    return f"""        <nav class="pole-links" aria-label="{html.escape(label, quote=True)}">
{links}
        </nav>"""


def goal_links(root: Path) -> list[tuple[str, str]]:
    """Ogni obiettivo porta alla sua ancora stabile in `goal.html`."""
    links = [(title, f"goal.html#{goal_anchor(key)}") for key, title in goal_titles(root).items()]
    return links + [(label("register"), "goal.html")]


# --- Sezioni ------------------------------------------------------------------


def goal_pole_html(root: Path) -> str:
    goal = register_intro(root, "goal")
    return f"""      <section class="pole pole-goal">
        <p class="kicker">Obiettivi · Goal</p>
{render_markdown(goal)}
{pole_links(goal_links(root), "Obiettivi")}
      </section>"""


def world_pole_html(root: Path) -> str:
    world = register_intro(root, "world")
    return f"""      <section class="pole pole-world">
        <p class="kicker">Mondo · World</p>
{render_markdown(world)}
{pole_links([(label("register"), "world.html")], "World")}
      </section>"""


def proposals_html(root: Path) -> str:
    """Le proposte in attesa del custode, dalla release: restano raggiungibili
    anche quando escono dagli ultimi giri, e il register della delega è a un clic."""
    items = [
        f'          <li><a href="{html.escape(relative.removesuffix(".md") + ".html", quote=True)}">'
        f"{html.escape(task.title)}</a> — {inline_markdown(task.decidere)}</li>"
        for relative, task in pending_proposals(root)
    ] or [f"          <li>{html.escape(label('no-pending'))}</li>"]
    links = (
        pole_links([(label("delegation"), "autonomy.html")], label("delegation"))
        if (root / "autonomy.md").exists()
        else ""
    )
    body = "\n".join(items)
    return f"""      <section class="pole proposte">
        <h2>{html.escape(label("pending"))}</h2>
        <ul>
{body}
        </ul>
{links}
      </section>"""


def card_html(key: str) -> str:
    href = SLOTS[key][0]
    desc = slot_description(key)
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


def provenance_html(provenance: dict[str, str] | None) -> str:
    """La revisione costruita e il toolchain; senza, la vista si dichiara anteprima.

    La build locale rende il working tree, modifiche e file non tracciati
    compresi: non le attribuisce a nessun commit (`kb/view.md`).
    """
    if not provenance:
        return (
            '\n    <footer class="provenance">\n'
            f"      <p>{html.escape(label('preview'))}</p>\n    </footer>"
        )
    tools = " · ".join(provenance[key] for key in ("pandoc", "prettier") if provenance.get(key))
    if provenance.get("canon"):
        tools = f"method {provenance['canon'][:12]} · {tools}"
    return (
        '\n    <footer class="provenance">\n'
        f"      <p>Commit <code>{html.escape(provenance['commit'][:12])}</code>"
        f" · {html.escape(tools)}</p>\n    </footer>"
    )


def render(root: Path, deck: bool, provenance: dict[str, str] | None = None) -> str:
    title = readme_title(root)
    incipit = readme_incipit(root)
    meta = (
        f'\n    <meta name="description" content="{html.escape(plain_text(incipit), quote=True)}" />'
        if incipit
        else ""
    )
    lead = f'\n      <p class="lead">{emphasis(inline_markdown(incipit))}</p>' if incipit else ""
    # Il deck è il racconto curato dell'artefatto, non uno stadio: la home lo
    # linka come voce a sé.
    deck_link = (
        f'\n      <p><a class="deck-link" href="presentation.html">{label("presentation")}</a></p>'
        if deck
        else ""
    )
    return f"""<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />{meta}
    <title>{html.escape(project.SIGLA)} · {html.escape(title)}</title>
    <link rel="stylesheet" href="assets/system-image.css" />
    <link rel="stylesheet" href="assets/theme.css" />
  </head>
  <body>
    <header class="hero">
      <p class="kicker">Artefatto · Artifact</p>
      <h1>{html.escape(title)}</h1>{lead}{deck_link}
    </header>

    <main>
{proposals_html(root)}
{goal_pole_html(root)}
{cycle_html()}
{world_pole_html(root)}
    </main>{provenance_html(provenance)}
  </body>
</html>
"""
