"""Rende gli indici i1/o3 con Pandoc, già richiesto dalla build delle viste.

L'intero corpo Markdown conserva gerarchie, liste, codice e riferimenti;
solo l'H1 iniziale è sostituito dal titolo della pagina, con la sigla del
repo. Il formato letto è il Markdown di Pandoc, come nelle viste Reveal. La
pagina è chiusa su `presentation/`: i link alle fonti diventano la loro
etichetta, restano link solo URL con schema, ancore e file della cartella.
HTML grezzo incorporato resta responsabilità della fonte, inclusi i suoi URL.
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path

from sources import close_links, label, pandoc_ast, pandoc_render

# kind -> sorgente relativa alla root
PAGES: dict[str, str] = {
    "prescriptions": "o3/prescriptions.md",
    "perceptions": "i1/perceptions.md",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def render_markdown(text: str, presentation: Path, source: str = "") -> str:
    document = pandoc_ast(text)
    blocks = document["blocks"]
    if blocks and blocks[0]["t"] == "Header" and blocks[0]["c"][0] == 1:
        blocks.pop(0)
    document = close_links(document, presentation, source)
    return pandoc_render(document, ["--to=html5", "--wrap=none"]).rstrip()


def render(root: Path, kind: str) -> str:
    source_rel = PAGES[kind]
    title = label(kind)
    text = (root / source_rel).read_text(encoding="utf-8")
    body = render_markdown(text, root / "presentation", source_rel)
    return f"""<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" href="assets/system-image.css" />
    <link rel="stylesheet" href="assets/theme.css" />
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

    args.output.write_text(render(repo_root(), args.kind), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
