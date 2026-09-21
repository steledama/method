"""Rende gli indici i1/o3 con Pandoc, già richiesto dalla build delle viste.

L'intero corpo Markdown conserva gerarchie, liste, codice e riferimenti;
solo l'H1 iniziale è sostituito dal titolo configurato della pagina. Il formato
letto è il Markdown di Pandoc, come nelle viste Reveal. I target Markdown di
link e immagini sono ribasati sull'AST, senza alterare codice o testo letterale.
HTML grezzo incorporato resta responsabilità della fonte, inclusi i suoi URL.
"""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import subprocess
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

# kind -> (sorgente relativa alla root, prefisso per i link relativi, titolo pagina)
PAGES: dict[str, tuple[str, str, str]] = {
    "prescriptions": ("o3/prescriptions.md", "../o3/", "Prescrizioni"),
    "perceptions": ("i1/perceptions.md", "../i1/", "Percezioni"),
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def rebase_target(target: str, prefix: str) -> str:
    """Mantiene schema, ancore e URL assoluti; normalizza solo il path relativo."""
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
        return target
    return urlunsplit(parts._replace(path=posixpath.normpath(prefix + parts.path)))


def rebase_links(value: object, prefix: str) -> None:
    """Visita l'AST Pandoc: Link e Image hanno il target nell'ultimo campo."""
    if isinstance(value, list):
        for child in value:
            rebase_links(child, prefix)
    elif isinstance(value, dict):
        if value.get("t") in {"Link", "Image"}:
            target = value["c"][-1]
            target[0] = rebase_target(target[0], prefix)
        for child in value.values():
            rebase_links(child, prefix)


def render_markdown(text: str, prefix: str) -> str:
    parsed = subprocess.run(
        ["pandoc", "--from=markdown-native_divs", "--to=json"],
        input=text,
        text=True,
        capture_output=True,
        check=True,
    )
    document = json.loads(parsed.stdout)
    blocks = document["blocks"]
    if blocks and blocks[0]["t"] == "Header" and blocks[0]["c"][0] == 1:
        blocks.pop(0)
    rebase_links(document, prefix)
    return subprocess.run(
        ["pandoc", "--from=json", "--to=html5", "--wrap=none"],
        input=json.dumps(document),
        text=True,
        capture_output=True,
        check=True,
    ).stdout.rstrip()


def render(root: Path, kind: str) -> str:
    source_rel, link_prefix, title = PAGES[kind]
    text = (root / source_rel).read_text(encoding="utf-8")
    body = render_markdown(text, link_prefix)
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
