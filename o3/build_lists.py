"""Genera le due viste a elenco puntato semplice: o3 e i1, senza slide.

A differenza di `build_views.py` (viste Reveal), queste due pagine sono HTML
statico minimale: il solo elenco puntato aperto, non una sintesi da scorrere
(cfr. `kb/view.md` — la forma segue la domanda). Ogni pagina deriva da una
sorgente sola: il blocco puntato contiguo sotto l'intestazione `## Contenuti`
dell'indice di collezione, che nei due indici tiene già solo i segnali/le
prescrizioni aperti — la storia dei fili chiusi resta prosa dopo la prima riga
vuota e non entra nella vista.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from presentation import inline_markdown

# kind -> (sorgente relativa alla root, prefisso per i link relativi, titolo pagina)
PAGES: dict[str, tuple[str, str, str]] = {
    "prescriptions": ("o3/prescriptions.md", "../o3/", "Prescrizioni"),
    "perceptions": ("i1/perceptions.md", "../i1/", "Percezioni"),
}

_CONTENUTI = re.compile(r"^## Contenuti\s*$", re.MULTILINE)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def contenuti_items(text: str, source: str) -> list[str]:
    """Gli item del blocco puntato contiguo sotto `## Contenuti`.

    Un item può avvolgersi su più righe (continuazione indentata, senza `- `):
    si ricompongono in una sola riga logica. Il blocco finisce alla prima riga
    vuota — lista vuota è uno stato legittimo (nessun aperto), non un errore;
    l'intestazione mancante lo è (`kb/view.md`, «Derivata implica verificata»).
    """
    match = _CONTENUTI.search(text)
    if not match:
        raise SystemExit(f"{source}: sezione «## Contenuti» mancante")
    items: list[str] = []
    current: list[str] = []
    for raw in text[match.end() :].splitlines():
        line = raw.strip()
        if line.startswith(("- ", "* ")):
            if current:
                items.append(" ".join(current))
            current = [line[2:].strip()]
        elif not line:
            if items or current:
                break
        elif current:
            current.append(line)
    if current:
        items.append(" ".join(current))
    return items


def render(root: Path, kind: str) -> str:
    source_rel, link_prefix, title = PAGES[kind]
    text = (root / source_rel).read_text(encoding="utf-8")
    items = contenuti_items(text, source_rel)
    body = (
        "<ul>\n"
        + "".join(f"          <li>{inline_markdown(item, link_prefix)}</li>\n" for item in items)
        + "        </ul>"
        if items
        else "<p>Nessun elemento aperto.</p>"
    )
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
      <p class="kicker">Elenco · List</p>
      <h1>{html.escape(title)}</h1>
    </header>

    <main>
      <section class="pole">
        {body}
      </section>
    </main>
  </body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera le viste a elenco o3/i1")
    parser.add_argument("kind", choices=sorted(PAGES))
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.write_text(render(repo_root(), args.kind), encoding="utf-8")


if __name__ == "__main__":
    main()
