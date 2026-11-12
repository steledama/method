"""La root del repo da rendere: quella dei builder, o un'altra con `--root`.

I builder sono canone e vivono nel checkout di `method`. Un adottante li
lancia da lì sul proprio repo, come `commit_gate.py`:

    python3 method/../o3/view/build.py --root .

e in `o3/view/` tiene solo ciò che è suo: `project.py`, i moduli di dominio
(`DECK_BUILDER`) e i test. La cartella locale va in testa a `sys.path`, così
`import project` trova l'identità del repo reso e non quella del canone.
Senza `--root` i builder rendono il repo che li contiene.

La root è esplicita e non dedotta dalla cartella corrente: un servizio
lanciato da un'altra cartella renderebbe il repo sbagliato senza dirlo.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_attiva: Path | None = None


def _argomento(argv: list[str]) -> str | None:
    for index, arg in enumerate(argv):
        if arg == "--root":
            if index + 1 == len(argv):
                raise SystemExit("--root richiede una cartella")
            return argv[index + 1]
        if arg.startswith("--root="):
            return arg.split("=", 1)[1]
    return None


def attiva(argv: list[str] | None = None) -> Path:
    """Risolve la root e mette la sua `o3/view/` davanti ai builder.

    Va chiamata prima di importare `project` o i moduli che lo importano.
    Le chiamate successive rendono la stessa root.
    """
    global _attiva
    if _attiva is None:
        _attiva = _risolvi(argv)
    return _attiva


def _risolvi(argv: list[str] | None) -> Path:
    value = _argomento(sys.argv[1:] if argv is None else argv)
    if value is None:
        return HERE.parents[1]
    root = Path(value).resolve()
    local = root / "o3" / "view"
    if local == HERE:
        return root
    if not (local / "project.py").is_file():
        raise SystemExit(f"--root {root}: manca o3/view/project.py, l'identità del repo")
    # Una copia dei builder rimasta accanto a `project.py` coprirebbe il
    # canone con una versione ferma: la resa mescolerebbe due revisioni.
    canonici = {path.name for path in HERE.glob("*.py")} - {"project.py"}
    ombre = sorted(path.name for path in local.glob("*.py") if path.name in canonici)
    if ombre:
        raise SystemExit(
            f"--root {root}: o3/view/ contiene copie dei builder canonici "
            f"({', '.join(ombre)}); rimuovile o lancia i builder locali"
        )
    sys.path.insert(0, str(local))
    return root
