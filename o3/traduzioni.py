"""Allineamento delle copie tradotte ai sorgenti canonici (cfr. `kb/translation.md`).

Una copia è il file gemello `nome.<lingua>.md` accanto a `nome.md`. Il suo
frontmatter porta `fonte:`, l'hash git del blob del sorgente da cui deriva
(`git hash-object nome.md`, lo stampa `fonte <file>`). L'hash del contenuto, e
non il commit, regge anche quando sorgente e copia cambiano nello stesso commit.

`check` esce con errore per una copia senza sorgente o senza `fonte:` valida;
una copia rimasta indietro è un ritardo dichiarato, si segnala e non ferma il
commit. Una copia mancante non si segnala: si traduce a lotti.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

GEMELLO = re.compile(r"^(?P<base>.+)\.(?P<lingua>[a-z]{2})\.md$")
FONTE = re.compile(r"^fonte:\s*\"?(?P<hash>[0-9a-f]{40})\"?\s*$", re.MULTILINE)
ESCLUSE = {".git", "view", "cache", "gdrive", "node_modules", "__pycache__"}


def sorgente(path: Path) -> Path | None:
    """Il sorgente canonico di una copia gemella, o None se il file non è una copia."""
    match = GEMELLO.match(path.name)
    return path.with_name(match["base"] + ".md") if match else None


def fonte(path: Path) -> str | None:
    testo = path.read_text(encoding="utf-8")
    if not testo.startswith("---\n"):
        return None
    blocco = testo[4:].split("\n---", 1)[0]
    match = FONTE.search(blocco)
    return match["hash"] if match else None


def hash_blob(path: Path) -> str:
    uscita = subprocess.run(
        ["git", "hash-object", str(path)], capture_output=True, text=True, check=True
    )
    return uscita.stdout.strip()


def copie(root: Path) -> list[Path]:
    trovate: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ESCLUSE and not d.startswith(".")]
        trovate += [Path(dirpath) / n for n in filenames if GEMELLO.match(n)]
    return sorted(trovate)


def verifica(root: Path) -> tuple[list[str], list[str]]:
    """Restituisce (errori, ritardi)."""
    errori: list[str] = []
    ritardi: list[str] = []
    for copia in copie(root):
        chiave = copia.relative_to(root).as_posix()
        origine = sorgente(copia)
        if origine is None or not origine.is_file():
            errori.append(f"{chiave}: sorgente assente")
            continue
        registrato = fonte(copia)
        if registrato is None:
            errori.append(f"{chiave}: frontmatter senza `fonte:` valida")
        elif registrato != hash_blob(origine):
            ritardi.append(f"{chiave}: indietro rispetto a {origine.relative_to(root).as_posix()}")
    return errori, ritardi


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("check", help="verifica le copie gemelle")
    p_fonte = sub.add_parser("fonte", help="stampa la riga `fonte:` per un sorgente")
    p_fonte.add_argument("file", type=Path)
    args = parser.parse_args(argv)

    if args.comando == "fonte":
        print(f"fonte: {hash_blob(args.file)}")
        return 0
    root = Path.cwd()
    errori, ritardi = verifica(root)
    print(f"copie tradotte: {len(copie(root))}, errori {len(errori)}, indietro {len(ritardi)}")
    for riga in errori:
        print(f"- errore: {riga}")
    for riga in ritardi:
        print(f"- indietro: {riga}")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
