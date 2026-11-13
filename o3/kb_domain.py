"""Controlli di dominio di `method` per `kb_tools.py audit`.

Il dominio di `method` è il metodo stesso: i suoi strumenti sono canone che gli
adottanti lanciano da questo checkout, quindi l'indice `o3/prescriptions.md`
deve nominarli tutti. Uno strumento presente ma non registrato è invisibile a
chi legge l'indice, e l'audit del nucleo non lo vede.
"""

from __future__ import annotations

import re
from pathlib import Path

INDICE = "o3/prescriptions.md"
# Moduli che non sono strumenti: questo file è il profilo di dominio dell'audit.
ESCLUSI = {"kb_domain.py"}


def strumenti(root: Path) -> list[str]:
    """Gli script e le cartelle di `o3/`, col path relativo a `o3/`."""
    base = root / "o3"
    trovati = [
        path.relative_to(base).as_posix()
        for path in sorted(base.rglob("*.py"))
        if "__pycache__" not in path.parts and path.name not in ESCLUSI
    ]
    cartelle = [
        f"{path.name}/"
        for path in sorted(base.iterdir())
        if path.is_dir() and path.name != "__pycache__"
    ]
    return [*trovati, *cartelle]


def non_registrati(root: Path) -> list[str]:
    indice = (root / INDICE).read_text(encoding="utf-8")
    # Sotto una cartella l'indice nomina i file col solo nome (`build.py`), e
    # uno strumento può comparire col suo sottocomando (`traduzioni.py check`).
    return [
        nome
        for nome in strumenti(root)
        if not re.search(rf"`{re.escape(nome.rsplit('/', 1)[-1] or nome)}[` ]", indice)
    ]


def audit(root: Path, core) -> dict[str, list[str]]:
    return {f"strumenti di o3/ non registrati in {INDICE}": non_registrati(root)}
