"""Chiusura di una prescrizione recepita da tutti gli adottanti.

Il giro non scrive in `o3/` (deny in `o3/ciclo/permessi.json`): questo script è
il gesto concesso per l'unico atto che lì gli è delegato, chiudere una
prescrizione che tutti hanno recepito (`autonomy.md`, `ciclo-autonomo`).
`verifica <nome>` dice per ogni adottante di `world.md` se il marker
`i3/allineamento-metodo.md` la dà recepita, su HEAD o su `origin/main`; un
adottante senza clone sull'host è «checkout assente», e la chiusura non passa.
Con `--ssh`, in sessione, legge via ssh gli adottanti dichiarati su altri host
(`o3/adottanti.py`); il giro lo passa, come per `adottanti.py`.
`chiudi <nome>` ripete la verifica e solo se passa per tutti toglie file e voce
da `o3/prescriptions.md`, in stage. I rimandi altrove restano al chiamante.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import adottanti as lettura
from adottanti import adottanti, assenti, git

ROOT = Path(__file__).resolve().parents[1]
INDICE = ROOT / "o3" / "prescriptions.md"
MARKER = "i3/allineamento-metodo.md"
NOME = re.compile(r"^[a-z0-9-]+$")
RECEPITA = re.compile(r"(?<!non )recepit", re.IGNORECASE)


def recepita(testo: str, nome: str) -> bool:
    """Una riga del marker nomina la prescrizione e la dà recepita."""
    return any(f"`{nome}`" in r and RECEPITA.search(r) for r in testo.splitlines())


def esiti(nome: str) -> dict[str, bool | None]:
    """Adottante → recepita sì o no; None se il checkout manca su questo host."""
    trovati: dict[str, bool | None] = {}
    for adottante, checkout in adottanti().items():
        testi = (git(checkout, "show", f"{ref}:{MARKER}").stdout for ref in ("HEAD", "origin/main"))
        trovati[adottante] = any(recepita(t, nome) for t in testi)
    return trovati | dict.fromkeys(assenti())


def senza_voce(indice: str, nome: str) -> str | None:
    """L'indice senza la voce che punta a `<nome>.md`, o None se non c'è."""
    righe = indice.splitlines(keepends=True)
    link = next((i for i, r in enumerate(righe) if f"]({nome}.md)" in r), None)
    if link is None:
        return None
    inizio = link
    while inizio > 0 and not righe[inizio].startswith("- ["):
        inizio -= 1
    fine = link + 1
    while fine < len(righe) and righe[fine].startswith("  "):
        fine += 1
    return "".join(righe[:inizio] + righe[fine:])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("comando", choices=["verifica", "chiudi"])
    parser.add_argument("nome", help="nome del file in o3/, senza .md")
    parser.add_argument(
        "--ssh", action="store_true", help="legge via ssh gli adottanti su altri host"
    )
    args = parser.parse_args(argv)
    lettura.REMOTI = args.ssh
    if not NOME.match(args.nome) or not (ROOT / "o3" / f"{args.nome}.md").exists():
        print(f"prescrizione sconosciuta: o3/{args.nome}.md")
        return 2
    trovati = esiti(args.nome)
    etichetta = {
        True: "recepita",
        False: "non risulta recepita",
        None: "checkout assente su questo host",
    }
    for adottante, ok in trovati.items():
        print(f"{adottante}: {etichetta[ok]}")
    if not all(trovati.values()):
        return 1
    if args.comando == "verifica":
        return 0
    nuovo = senza_voce(INDICE.read_text(encoding="utf-8"), args.nome)
    if nuovo is None:
        print(f"voce di {args.nome} assente in o3/prescriptions.md: niente da chiudere")
        return 2
    INDICE.write_text(nuovo, encoding="utf-8")
    for comando in (["rm", "-q", f"o3/{args.nome}.md"], ["add", "o3/prescriptions.md"]):
        subprocess.run(["git", "-C", str(ROOT), *comando], check=True)
    print(f"chiusa: o3/{args.nome}.md rimossa e voce tolta dall'indice, in stage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
