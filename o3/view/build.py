"""Rigenera l'intera `view/`: pagine 1:1, deck, home e asset.

È l'unico entrypoint di build, con lo stesso path in ogni repo
(`python3 o3/view/build.py`, su Windows `py o3\\view\\build.py`). È Python e
non bash perché deve girare anche sugli host Windows. `view/` è tutta
generata: ciò che la build non produce più si rimuove, così una fonte
cancellata non lascia una pagina orfana. Due build consecutive producono lo
stesso output; alla fine il presidio verifica che nessun URL emesso esca da
`view/` (`kb/view.md`).
"""

from __future__ import annotations

import importlib
import re
import shutil
import subprocess
from pathlib import Path

import project
from build_pages import render_all
from build_system_image import render as render_home
from sources import (
    check_closed,
    check_plan_contract,
    check_verdict_contract,
    label,
    parse_plan,
    reveal_page,
)

ROOT = Path(__file__).resolve().parents[2]
VIEW = ROOT / "view"
ASSETS = VIEW / "assets"
CANONICAL_ASSETS = Path(__file__).resolve().parent / "assets"
PRESENTATION = ROOT / "presentation"


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
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_bytes() != data:
        path.write_bytes(data)


def theme_css() -> str:
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", project.ACCENTO):
        raise SystemExit(f"project.py: ACCENTO «{project.ACCENTO}» non è un colore #rrggbb")
    return (
        "/* Generato da o3/view/build.py da project.py: non modificare. */\n"
        f":root {{\n  --accent: {project.ACCENTO};\n  --accent-ink: {project.ACCENTO};\n}}\n"
    )


def plates(deck: Path) -> dict[str, bytes]:
    """Le tavole hanno la fonte accanto al deck e si citano come `assets/<nome>`."""
    text = deck.read_text(encoding="utf-8")
    found: dict[str, bytes] = {}
    for name in sorted(set(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|svg|webp))", text))):
        source = deck.parent / name
        if source.exists():
            found[f"assets/{name}"] = source.read_bytes()
    return found


def deck_page(reveal_url: str) -> str | None:
    """Il deck: un Markdown in `DECK`, un builder di dominio in `DECK_BUILDER`, o nessuno.

    Il builder di dominio vive accanto ai builder canonici ed espone
    `render(root, reveal_url) -> str`, la pagina completa. Il presidio finale
    vale anche per questa pagina.
    """
    if project.DECK and project.DECK_BUILDER:
        raise SystemExit("project.py: DECK e DECK_BUILDER sono alternativi, dichiarane uno")
    if project.DECK_BUILDER:
        return importlib.import_module(project.DECK_BUILDER).render(ROOT, reveal_url)
    if project.DECK:
        deck = ROOT / project.DECK
        return reveal_page(
            deck.read_text(encoding="utf-8"), project.DECK, label("presentation"), reveal_url, VIEW
        )
    return None


def main() -> None:
    require("pandoc")
    prettier = require("prettier")
    reveal_url = revealjs_url()

    # I contratti fra le fonti si verificano prima di rendere: una vista
    # plausibile su fonti che si contraddicono è il difetto da evitare.
    rows = parse_plan(ROOT)
    check_plan_contract(ROOT, rows)
    check_verdict_contract(ROOT)

    binaries: dict[str, bytes] = {"assets/theme.css": theme_css().encode("utf-8")}
    for css in sorted(CANONICAL_ASSETS.glob("*.css")):
        binaries[f"assets/{css.name}"] = css.read_bytes()
    for name in project.CSS_LOCALI:
        binaries[f"assets/{name}"] = (PRESENTATION / name).read_bytes()
    if project.DECK:
        binaries |= plates(ROOT / project.DECK)

    pages, images = render_all(ROOT, rows)
    for relative, path in images.items():
        binaries[relative] = path.read_bytes()

    # Le tavole e le immagini devono esistere prima di rendere il deck: il suo
    # presidio verifica che stiano nella cartella.
    for relative, data in binaries.items():
        write(VIEW / relative, data)

    texts = dict(pages)
    deck = deck_page(reveal_url)
    if deck is not None:
        texts["presentation.html"] = deck
    texts["index.html"] = render_home(ROOT, deck is not None)

    for relative, content in texts.items():
        write(VIEW / relative, content)

    expected = {VIEW / relative for relative in [*binaries, *texts]}
    for path in sorted(VIEW.rglob("*"), reverse=True):
        if path.is_file() and path not in expected:
            path.unlink()
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()

    subprocess.run(
        [prettier, "--log-level=warn", "--write", *(str(VIEW / name) for name in texts)],
        check=True,
    )
    check_closed(VIEW)


if __name__ == "__main__":
    main()
