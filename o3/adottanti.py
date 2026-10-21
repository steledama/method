"""Lettura degli adottanti per il giro e per le sessioni: storia e interfaccia col canone.

Il giro non concede `git -C` (aggirerebbe i pattern dei permessi) e fuori dalla
cartella di lavoro nega anche le letture: questo script è il gesto concesso al
posto loro (`kb/agent-as-user.md`). È di sola lettura per costruzione: nessun
sottocomando scrive, e git gira senza lock opzionali.

Gli adottanti e i checkout vengono da `world.md`, il register che li dichiara.
`show` legge solo i file con cui un adottante recepisce il canone; il resto del
dominio, dati personali compresi, resta fuori.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()

# L'interfaccia di un adottante col canone: regole, delega, marker, ciclo, skill.
INTERFACCIA = [
    "CLAUDE.md",
    "AGENTS.md",
    "autonomy.md",
    "i3/allineamento-metodo.md",
    "o3/ciclo/prompt.md",
    "o3/ciclo/permessi.json",
    ".claude/ciclo-prompt.md",
    ".claude/settings.json",
    ".claude/skills/*/SKILL.md",
    ".codex/skills/*/SKILL.md",
]

VOCE = re.compile(r"^- \*\*\[([\w-]+)\]\([^)]*\)\*\*(.*)")
CHECKOUT = re.compile(r"checkout `~/([\w.-]+)`")


def adottanti(world: Path = ROOT / "world.md") -> dict[str, Path]:
    """Nome → checkout, dalle voci in grassetto di `world.md` col loro checkout."""
    trovati: dict[str, Path] = {}
    voce = None
    for riga in world.read_text(encoding="utf-8").splitlines():
        if match := VOCE.match(riga):
            voce = match.group(1)
            riga = match.group(2)
        elif not riga.startswith("  "):
            voce = None
        if voce and (match := CHECKOUT.search(riga)):
            trovati[voce] = HOME / match.group(1)
            voce = None
    return trovati


def ammesso(path: str) -> bool:
    if ".." in Path(path).parts:
        return False
    return any(fnmatch.fnmatchcase(path, schema) for schema in INTERFACCIA)


def git(checkout: Path, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    return subprocess.run(
        ["git", "-C", str(checkout), *args], capture_output=True, text=True, env=env, check=False
    )


def commit(checkout: Path, ref: str) -> str:
    esito = git(checkout, "log", "-1", "--format=%h %ad %s", "--date=iso-strict", ref)
    return esito.stdout.strip() if esito.returncode == 0 else f"assente ({ref})"


def stato(nome: str, checkout: Path) -> list[str]:
    if not (checkout / ".git").exists():
        return [f"{nome}: checkout assente in {checkout}"]
    righe = [f"{nome} ({checkout})"]
    righe.append(f"  HEAD         {commit(checkout, 'HEAD')}")
    righe.append(f"  origin/main  {commit(checkout, 'origin/main')}")
    conto = git(checkout, "rev-list", "--left-right", "--count", "HEAD...origin/main")
    if conto.returncode == 0:
        avanti, indietro = conto.stdout.split()
        righe.append(f"  rispetto a origin/main: {avanti} avanti, {indietro} indietro")
    tree = git(checkout, "status", "--porcelain")
    if tree.returncode == 0:
        sporchi = len(tree.stdout.splitlines())
        righe.append(f"  working tree: {'pulito' if not sporchi else f'{sporchi} file modificati'}")
    return righe


def scegli(nome: str, tutti: dict[str, Path]) -> Path:
    if nome not in tutti:
        sys.exit(f"adottante sconosciuto: {nome}; adottanti in world.md: {', '.join(tutti)}")
    return tutti[nome]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        epilog="File leggibili con show: " + ", ".join(INTERFACCIA),
    )
    sub = parser.add_subparsers(dest="comando", required=True)
    p_stato = sub.add_parser("stato", help="HEAD, origin/main, distanza e working tree")
    p_stato.add_argument("nomi", nargs="*", help="adottanti; tutti se omessi")
    p_log = sub.add_parser("log", help="ultimi commit con data e trailer")
    p_log.add_argument("nome")
    p_log.add_argument("-n", type=int, default=5)
    p_log.add_argument("--ref", default="HEAD", help="origin/main per i repo di svezia")
    p_show = sub.add_parser("show", help="un file dell'interfaccia col canone")
    p_show.add_argument("nome")
    p_show.add_argument("path")
    p_show.add_argument("--ref", default="HEAD", help="origin/main per i repo di svezia")
    args = parser.parse_args(argv)

    tutti = adottanti()
    if args.comando == "stato":
        for nome in args.nomi or tutti:
            print("\n".join(stato(nome, scegli(nome, tutti))))
        return 0
    checkout = scegli(args.nome, tutti)
    if args.comando == "log":
        formato = "%h %ad %s%n%(trailers:unfold,separator=%x0a  )"
        esito = git(
            checkout, "log", f"-{args.n}", f"--format={formato}", "--date=iso-strict", args.ref
        )
    else:
        if not ammesso(args.path):
            sys.exit(
                f"{args.path} è fuori dall'interfaccia col canone; leggibili: "
                + ", ".join(INTERFACCIA)
            )
        esito = git(checkout, "show", f"{args.ref}:{args.path}")
    sys.stdout.write(esito.stdout)
    sys.stderr.write(esito.stderr)
    return esito.returncode


if __name__ == "__main__":
    sys.exit(main())
