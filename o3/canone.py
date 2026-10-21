"""Lettura della storia del canone per gli adottanti, dal giro o in sessione.

Un adottante lo lancia dal checkout del canone, `python3 method/../o3/canone.py`,
al posto di `git -C <method> log`: il giro non concede `git -C`, che aggirerebbe
i pattern dei permessi (`kb/agent-as-user.md`). Legge solo il checkout di
`method`, mai gli altri adottanti, ed è di sola lettura per costruzione.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMATO = "%h %ad %s%n%(trailers:unfold,separator=%x0a  )"


def git(*args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True, env=env, check=False
    )


def cursore_valido(sha: str) -> str | None:
    """Messaggio d'errore se il cursore non è un commit di method, altrimenti None."""
    if git("cat-file", "-e", f"{sha}^{{commit}}").returncode:
        return f"{sha} non è un commit di method: checkout indietro o cursore sbagliato"
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="comando", required=True)
    p_log = sub.add_parser("log", help="commit del canone con data e trailer")
    p_log.add_argument("--da", help="cursore del marker: solo i commit successivi")
    p_log.add_argument("-n", type=int, default=20)
    p_log.add_argument("--ref", default="HEAD")
    p_dist = sub.add_parser("distanza", help="commit del canone arrivati dopo il cursore")
    p_dist.add_argument("--da", required=True)
    p_dist.add_argument("--ref", default="HEAD")
    args = parser.parse_args(argv)

    if args.da and (errore := cursore_valido(args.da)):
        print(errore, file=sys.stderr)
        return 2
    intervallo = f"{args.da}..{args.ref}" if args.da else args.ref
    if args.comando == "distanza":
        esito = git("rev-list", "--count", intervallo)
    else:
        esito = git("log", f"-{args.n}", f"--format={FORMATO}", "--date=iso-strict", intervallo)
    sys.stdout.write(esito.stdout)
    sys.stderr.write(esito.stderr)
    return esito.returncode


if __name__ == "__main__":
    sys.exit(main())
