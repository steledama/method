"""Genera le due viste a elenco: o3 e i1, fedeli all'intera struttura markdown
della collezione sorgente.

A differenza di `build_views.py` (viste Reveal), queste due pagine sono HTML
statico minimale (cfr. `kb/view.md` — la forma segue la domanda). Il contratto
non è un nome di intestazione: è **strutturale**, agnostico a come ogni repo
organizza la propria collezione (`kb/method-development.md`, «il confine
canone↔adottante: dichiara e taci» — lo strumento canonico non impone il
proprio lessico interno a ciò che legge).

Ogni pagina deriva da una sorgente sola: l'intero indice di collezione.
Renderizza, nell'ordine della fonte, l'intro prima della prima `##` e ogni
sezione `##` per intero (paragrafi e liste puntate, senza tagli su un nome o
un blocco specifico) — nessuna parte del file è esclusa per assunzione del
generatore. Se una fonte non vuole che una porzione compaia nella vista (per
esempio la prosa storica di un filo consumato), la esclude alla fonte, non
qui: il generatore mostra, non indovina cosa sia "storia" (`kb/view.md` —
«derivata implica verificata»).
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

_H2 = re.compile(r"^## (.+?)\s*$", re.MULTILINE)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def sections(text: str) -> list[tuple[str | None, str]]:
    """(titolo, corpo) per l'intro (titolo `None`) e ogni sezione `##`, in ordine.

    L'H1 iniziale non entra nel corpo dell'intro (la pagina rende il proprio
    `<h1>` dal titolo configurato); il resto del file, compresa ogni sezione
    `##`, è tutto corpo della collezione.
    """
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    result: list[tuple[str | None, list[str]]] = [(None, [])]
    for line in lines:
        match = re.match(r"^## (.+?)\s*$", line)
        if match:
            result.append((match.group(1).strip(), []))
        else:
            result[-1][1].append(line)
    return [(title, "\n".join(body)) for title, body in result]


def _blocks(body: str) -> list[str]:
    """Blocchi separati da una riga vuota."""
    return [b.strip() for b in re.split(r"\n\s*\n", body.strip()) if b.strip()]


def _render_block(block: str, link_prefix: str) -> str:
    """Un blocco è una lista puntata (righe di continuazione indentate incluse
    nell'ultimo item) o un paragrafo — mai un taglio a metà blocco."""
    lines = block.splitlines()
    if lines[0].strip().startswith(("- ", "* ")):
        items: list[str] = []
        current: list[str] = []
        for raw in lines:
            line = raw.strip()
            if line.startswith(("- ", "* ")):
                if current:
                    items.append(" ".join(current))
                current = [line[2:].strip()]
            elif current:
                current.append(line)
        if current:
            items.append(" ".join(current))
        return (
            "<ul>\n"
            + "".join(f"          <li>{inline_markdown(it, link_prefix)}</li>\n" for it in items)
            + "        </ul>"
        )
    paragraph = " ".join(line.strip() for line in lines)
    return f"<p>{inline_markdown(paragraph, link_prefix)}</p>"


def render_section(title: str | None, body: str, link_prefix: str) -> str:
    blocks = _blocks(body)
    if not blocks:
        return (
            ""
            if title is None
            else f"<h2>{html.escape(title)}</h2>\n        <p><em>(sezione vuota)</em></p>"
        )
    content = "\n        ".join(_render_block(b, link_prefix) for b in blocks)
    if title is None:
        return content
    return f"<h2>{html.escape(title)}</h2>\n        {content}"


def render(root: Path, kind: str) -> str:
    source_rel, link_prefix, title = PAGES[kind]
    text = (root / source_rel).read_text(encoding="utf-8")
    body = "\n\n        ".join(
        rendered for t, s in sections(text) if (rendered := render_section(t, s, link_prefix))
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
