"""Rigenera l'intera presentazione: viste Reveal, liste, home e asset.

È l'unico entrypoint di build, con lo stesso path in ogni repo
(`python3 o3/presentation/build.py`, su Windows `py o3\\presentation\\build.py`).
È Python e non bash perché deve girare anche sugli host Windows. Due build
consecutive producono lo stesso output; alla fine il presidio verifica che
nessun URL emesso esca da `presentation/` (`kb/presentation.md`).
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import project
from build_lists import PAGES
from build_lists import render as render_list
from build_system_image import render as render_home
from build_views import task_view, verdict_view
from sources import check_closed, close_links, label, pandoc_ast, pandoc_render

ROOT = Path(__file__).resolve().parents[2]
PRESENTATION = ROOT / "presentation"
ASSETS = PRESENTATION / "assets"


def require(tool: str) -> str:
    path = shutil.which(tool)
    if not path:
        raise SystemExit(f"build: «{tool}» non trovato nel PATH")
    return path


def revealjs_url() -> str:
    """La versione di reveal.js la detta il template di pandoc, non noi.

    Fino alla 3.11 i percorsi dei plugin sono quelli della serie 5
    (plugin/notes/notes.js), dalla 3.12 quelli della 6 (dist/plugin/notes.js).
    Un URL che non corrisponde lascia le slide bianche senza errori.
    """
    first = subprocess.run(
        ["pandoc", "--version"], text=True, encoding="utf-8", capture_output=True, check=True
    ).stdout.splitlines()[0]
    match = re.match(r"\S+\s+(\d+)\.(\d+)", first)
    if not match:
        raise SystemExit(f"build: versione di pandoc non riconosciuta: «{first}»")
    major, minor = int(match.group(1)), int(match.group(2))
    if (major, minor) >= (3, 12):
        return "https://cdn.jsdelivr.net/npm/reveal.js@6.0.2"
    return "https://cdn.jsdelivr.net/npm/reveal.js@5.1.0"


def write(path: Path, content: str | bytes) -> None:
    """Scrive solo se cambia: la rigenerazione resta un gesto senza rumore.

    I testi si scrivono in byte UTF-8 con i loro `\n`: su Windows la
    scrittura in modo testo li tradurrebbe in CRLF.
    """
    data = content.encode("utf-8") if isinstance(content, str) else content
    if not path.exists() or path.read_bytes() != data:
        path.write_bytes(data)


def theme_css() -> str:
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", project.ACCENTO):
        raise SystemExit(f"project.py: ACCENTO «{project.ACCENTO}» non è un colore #rrggbb")
    return (
        "/* Generato da o3/presentation/build.py da project.py: non modificare. */\n"
        f":root {{\n  --accent: {project.ACCENTO};\n  --accent-ink: {project.ACCENTO};\n}}\n"
    )


def copy_plates(deck: Path) -> None:
    """Le tavole hanno la fonte accanto al deck e si citano come `assets/<nome>`.

    La copia tiene `presentation/` fatta di file generati; git salva una
    volta sola i file identici, quindi la storia non raddoppia.
    """
    text = deck.read_text(encoding="utf-8")
    for name in sorted(set(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|svg|webp))", text))):
        source = deck.parent / name
        if source.exists():
            write(ASSETS / name, source.read_bytes())


def reveal(markdown: str, source: str, title: str, reveal_url: str) -> str:
    document = close_links(pandoc_ast(markdown), PRESENTATION, source)
    return pandoc_render(
        document,
        [
            "--standalone",
            "--to=revealjs",
            "--slide-level=2",
            "--css=assets/deck.css",
            "--css=assets/theme.css",
            *(f"--css=assets/{name}" for name in project.CSS_LOCALI),
            f"--metadata=pagetitle:{title}",
            f"--variable=revealjs-url:{reveal_url}",
            "--variable=theme:white",
            "--variable=width:1180",
            "--variable=height:740",
            "--variable=margin:0.05",
            "--variable=center:false",
            "--variable=slideNumber:true",
        ],
    )


def main() -> None:
    require("pandoc")
    prettier = require("prettier")
    reveal_url = revealjs_url()
    write(ASSETS / "theme.css", theme_css())

    outputs: dict[str, str] = {}
    # Un repo senza deck delle Interpretazioni dichiara `DECK = None`.
    if project.DECK:
        deck = ROOT / project.DECK
        copy_plates(deck)
        outputs["interpretations.html"] = reveal(
            deck.read_text(encoding="utf-8"), project.DECK, label("interpretations"), reveal_url
        )
    outputs |= {
        "tasks.html": reveal(task_view(ROOT), "o1/plan.md", label("plan"), reveal_url),
        "verdict.html": reveal(verdict_view(ROOT), "i3/", label("verdict"), reveal_url),
        "index.html": render_home(ROOT),
    }
    for kind in PAGES:
        outputs[f"{kind}.html"] = render_list(ROOT, kind)

    for name, content in outputs.items():
        (PRESENTATION / name).write_text(content, encoding="utf-8", newline="\n")
    subprocess.run(
        [prettier, "--log-level=warn", "--write", *(str(PRESENTATION / name) for name in outputs)],
        check=True,
    )

    check_closed(PRESENTATION)


if __name__ == "__main__":
    main()
