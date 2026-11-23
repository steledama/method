"""Lettura degli adottanti o dei membri di un gruppo: storia e interfaccia col canone.

Lo script è di sola lettura: nessun sottocomando scrive e git gira senza lock
opzionali.

Senza `--root` gli adottanti vengono da `world.md` di `method`, il register del
territorio. Con `--root DIR` vengono dall'istanza di un gruppo: la sezione
`## Membri` del suo `world.md`, la stessa del sito di gruppo, più l'istanza
stessa (`kb/view-publishing.md`, «Sito di gruppo»). Così il coordinatore legge
i propri membri, e `method` non legge più i gruppi che non coordina.

Il checkout si riconosce dal remote `origin`, fra le cartelle della home,
perché la disposizione cambia da host a host (su `svezia` `~/nixos` è il repo
di lavoro, su `deck` quello di casa); il nome dichiarato vale solo senza un
remote GitHub. Un adottante dichiarato `su` un altro host non si legge da qui:
è «fuori host», e per lui fa fede la versione del canone che dichiara
(`kb/method-development.md`, «Versioni»). È «assente» solo chi è dichiarato su
questo host senza un clone. `show` legge solo i file con cui un adottante
recepisce il canone; il resto del dominio, dati personali compresi, resta
fuori.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import socket
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
QUI = socket.gethostname()

Checkout = Path

ASSENTE = "dichiarato su questo host, ma senza un clone"
FUORI = "fuori da questo host: fa fede la versione dichiarata"

# L'interfaccia di un adottante col canone: regole, delega, marker, skill.
INTERFACCIA = [
    "CLAUDE.md",
    "AGENTS.md",
    "autonomy.md",
    "i3/allineamento-metodo.md",
    ".claude/settings.json",
    ".claude/skills/*/SKILL.md",
    ".codex/skills/*/SKILL.md",
]

VOCE = re.compile(r"^- \*\*\[([\w-]+)\]\(([^)]*)\)\*\*(.*)")
REPO = re.compile(r"github\.com[:/]([\w.-]+/[\w.-]+?)(?:\.git)?/?$")
CHECKOUT = re.compile(r"checkout\s+`~/([\w.-]+)`(?:\s+su\s+`([\w.-]+)`)?")
MEMBRI = re.compile(r"^## Membri[ \t]*\n(?P<corpo>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)


def territorio(world: Path) -> str:
    """Il testo da cui si leggono gli adottanti: la sezione `## Membri` se c'è, se no tutto."""
    testo = world.read_text(encoding="utf-8")
    match = MEMBRI.search(testo)
    return match.group("corpo") if match else testo


def dichiarati(world: Path = ROOT / "world.md") -> dict[str, tuple[str | None, str, str | None]]:
    """Nome → (repo GitHub `owner/nome` o None, cartella e host dichiarati), dalle voci col checkout."""
    trovati: dict[str, tuple[str | None, str, str | None]] = {}
    repo: dict[str, str | None] = {}
    for riga in territorio(world).splitlines():
        if match := VOCE.match(riga):
            repo[match.group(1)] = repo_di(match.group(2))
    # Il testo intero della voce: cartella e host possono stare su righe diverse.
    for nome, testo in voci(world).items():
        if match := CHECKOUT.search(testo):
            trovati[nome] = (repo[nome], match.group(1), match.group(2))
    return trovati


def repo_di(url: str) -> str | None:
    match = REPO.search(url.strip())
    return match.group(1).lower() if match else None


def cloni(home: Path = HOME) -> dict[str, Path]:
    """Repo GitHub `owner/nome` → primo checkout della home col remote `origin` su quel repo."""
    trovati: dict[str, Path] = {}
    try:
        cartelle = sorted(p for p in home.iterdir() if (p / ".git").exists())
    except OSError:
        return trovati
    for cartella in cartelle:
        repo = repo_di(git(cartella, "config", "--get", "remote.origin.url").stdout)
        if repo:
            trovati.setdefault(repo, cartella)
    return trovati


def adottanti(
    world: Path = ROOT / "world.md", home: Path = HOME, istanza: Path | None = None
) -> dict[str, Checkout]:
    """Nome → checkout locale; con un'istanza, anche l'istanza stessa per prima."""
    trovati: dict[str, Checkout] = {istanza.name: istanza} if istanza else {}
    presenti = None
    for nome, (repo, cartella, _host) in dichiarati(world).items():
        if repo is None:
            if (home / cartella / ".git").exists():
                trovati[nome] = home / cartella
            continue
        presenti = cloni(home) if presenti is None else presenti
        if repo in presenti:
            trovati[nome] = presenti[repo]
    return trovati


def mancanti(world: Path = ROOT / "world.md", home: Path = HOME, qui: str = QUI) -> dict[str, str]:
    """Nome → motivo, per i dichiarati senza clone: fuori host, oppure assente qui."""
    presenti = adottanti(world, home)
    return {
        nome: FUORI if host and host != qui else ASSENTE
        for nome, (_repo, _cartella, host) in dichiarati(world).items()
        if nome not in presenti
    }


def voci(world: Path = ROOT / "world.md") -> dict[str, str]:
    """Nome → testo intero della voce in grassetto di `world.md`, righe di seguito comprese."""
    trovate: dict[str, str] = {}
    voce = None
    for riga in territorio(world).splitlines():
        if match := VOCE.match(riga):
            voce = match.group(1)
            trovate[voce] = match.group(3)
        elif voce and riga.startswith("  "):
            trovate[voce] += " " + riga.strip()
        else:
            voce = None
    return trovate


# Ref e path non portano metacaratteri: un argomento non diventa un secondo comando.
SICURO = re.compile(r"^[A-Za-z0-9_./-]+$")


def ammesso(path: str) -> bool:
    if ".." in Path(path).parts or not SICURO.match(path):
        return False
    return any(fnmatch.fnmatchcase(path, schema) for schema in INTERFACCIA)


def git(checkout: Checkout, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    return subprocess.run(
        ["git", "-C", str(checkout), *args], capture_output=True, text=True, env=env, check=False
    )


def commit(checkout: Checkout, ref: str) -> str:
    esito = git(checkout, "log", "-1", "--format=%h %ad %s", "--date=iso-strict", ref)
    return esito.stdout.strip() if esito.returncode == 0 else f"assente ({ref})"


def stato(nome: str, checkout: Checkout) -> list[str]:
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


def scegli(nome: str, tutti: dict[str, Checkout], senza: dict[str, str]) -> Checkout:
    if nome not in tutti:
        if nome in senza:
            sys.exit(f"{nome}: {senza[nome]}")
        sys.exit(f"adottante sconosciuto: {nome}; leggibili da qui: {', '.join(tutti)}")
    return tutti[nome]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        epilog="File leggibili con show: " + ", ".join(INTERFACCIA),
    )
    parser.add_argument(
        "--root",
        type=Path,
        help="istanza di un gruppo: legge i membri della sua sezione `## Membri`",
    )
    sub = parser.add_subparsers(dest="comando", required=True)
    p_stato = sub.add_parser("stato", help="HEAD, origin/main, distanza e working tree")
    p_stato.add_argument("nomi", nargs="*", help="adottanti; tutti se omessi")
    p_log = sub.add_parser("log", help="ultimi commit con data e trailer")
    p_log.add_argument("nome")
    p_log.add_argument("-n", type=int, default=5)
    p_log.add_argument("--ref", default="HEAD")
    p_show = sub.add_parser("show", help="un file dell'interfaccia col canone")
    p_show.add_argument("nome")
    p_show.add_argument("path")
    p_show.add_argument("--ref", default="HEAD")
    args = parser.parse_args(argv)
    if not SICURO.match(getattr(args, "ref", "HEAD")):
        sys.exit(f"ref non ammesso: {args.ref}")

    istanza = args.root.expanduser().resolve() if args.root else None
    world = (istanza or ROOT) / "world.md"
    tutti = adottanti(world, istanza=istanza)
    senza = mancanti(world)
    if args.comando == "stato":
        for nome in args.nomi or [*tutti, *senza]:
            if nome in senza:
                print(f"{nome}: {senza[nome]}")
                continue
            print("\n".join(stato(nome, scegli(nome, tutti, senza))))
        return 0
    checkout = scegli(args.nome, tutti, senza)
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
