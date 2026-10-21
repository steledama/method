"""Gate deterministico di /commit: formatter e controlli prima, trailer dopo.

La skill `commit` tiene il giudizio (delega, filing back, messaggio,
`Autonomia`); qui sta ciò che una macchina verifica da sola, lanciabile da
qualunque harness, da terminale o da un hook git (`kb/skill-composition.md`).

- `prima`: formatta i file cambiati e lancia i controlli del profilo;
- `dopo [--giro]`: verifica i trailer dell'ultimo commit; `--giro` aggiunge
  quelli che `/cycle` richiede.

Il profilo è locale, `o3/commit_gate.toml` del repo: formatter per glob e
controlli, sempre o quando cambia un glob, con l'uscita che li fa fallire.
Un adottante lancia lo script dal checkout del canone col proprio profilo.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

PROFILO = Path("o3/commit_gate.toml")
STADI = {"perceive", "interpret", "compare", "plan", "specify", "perform"}
IMPATTI = ["basso", "medio", "alto"]
PROSSIMO = re.compile(r".+ \((confermato|cambiato, era .+; .+)\)$")
COAUTORIA = re.compile(r"^(co-authored-by|generated-by|assisted-by)$", re.IGNORECASE)


def run(args: list[str], root: Path) -> subprocess.CompletedProcess:
    """Lancia col path risolto: su Windows CreateProcess non trova `prettier.cmd`,
    e l'uscita dei comandi di sistema può non essere UTF-8."""
    eseguibile = shutil.which(args[0]) or args[0]
    return subprocess.run(
        [eseguibile, *args[1:]],
        cwd=root,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def cambiati(root: Path) -> list[str]:
    """File modificati, aggiunti o non tracciati, esclusi i rimossi."""
    uscita = run(["git", "status", "--porcelain", "--untracked-files=all"], root).stdout
    files = []
    for riga in uscita.splitlines():
        stato, path = riga[:2], riga[3:]
        if "D" in stato:
            continue
        files.append(path.split(" -> ")[-1].strip('"'))
    return files


def profilo(root: Path) -> dict:
    path = root / PROFILO
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def prima(root: Path) -> int:
    conf = profilo(root)
    files = cambiati(root)
    falliti = 0
    if not conf:
        print(f"profilo {PROFILO} assente: nessun formatter né controllo dichiarato")
    for fmt in conf.get("formatter", []):
        scelti = [f for f in files if fnmatch.fnmatch(f, fmt["glob"])]
        if not scelti:
            continue
        if shutil.which(fmt["comando"][0]) is None:
            print(f"formatter non disponibile, saltato: {fmt['comando'][0]} ({fmt['glob']})")
            continue
        esito = run([*fmt["comando"], *scelti], root)
        stato = "ok" if esito.returncode == 0 else f"errore {esito.returncode}"
        print(f"formatter {' '.join(fmt['comando'])}: {len(scelti)} file, {stato}")
        if esito.returncode:
            falliti += 1
            print(esito.stdout + esito.stderr, end="")
    for ctrl in conf.get("controllo", []):
        quando = ctrl.get("quando")
        if quando and not any(fnmatch.fnmatch(f, quando) for f in files):
            print(f"controllo {' '.join(ctrl['comando'])}: non dovuto ({quando} invariato)")
            continue
        if shutil.which(ctrl["comando"][0]) is None:
            falliti += 1
            print(f"controllo {' '.join(ctrl['comando'])}: non disponibile, FALLITO")
            continue
        esito = run(ctrl["comando"], root)
        uscita = esito.stdout + esito.stderr
        regola = ctrl.get("fallisce_se")
        fallito = esito.returncode != 0 or bool(regola and re.search(regola, uscita, re.MULTILINE))
        print(f"controllo {' '.join(ctrl['comando'])}: {'FALLITO' if fallito else 'ok'}")
        if fallito:
            falliti += 1
            print(uscita[-3000:], end="" if uscita.endswith("\n") else "\n")
    return 1 if falliti else 0


def trailer(root: Path, ref: str = "HEAD") -> list[tuple[str, str]]:
    uscita = run(["git", "log", "-1", "--format=%(trailers:unfold)", ref], root).stdout
    coppie = []
    for riga in uscita.splitlines():
        if ":" in riga:
            chiave, valore = riga.split(":", 1)
            coppie.append((chiave.strip(), valore.strip()))
    return coppie


def errori_trailer(coppie: list[tuple[str, str]], giro: bool = False) -> list[str]:
    valori: dict[str, list[str]] = {}
    for chiave, valore in coppie:
        valori.setdefault(chiave, []).append(valore)
    errori = [f"trailer di coautoria o attribuzione: {k}" for k in valori if COAUTORIA.match(k)]
    autonomia = valori.get("Autonomia", [])
    if autonomia not in (["concordato"], ["agente"]):
        errori.append(f"Autonomia deve essere una, concordato o agente: {autonomia or 'assente'}")
    agente = autonomia == ["agente"]
    impatto = valori.get("Impatto", [])
    if agente:
        if len(impatto) != 1 or impatto[0] not in IMPATTI:
            errori.append(
                f"Impatto deve essere uno fra {', '.join(IMPATTI)}: {impatto or 'assente'}"
            )
        if not valori.get("Impatto-motivo"):
            errori.append("Impatto-motivo assente con Autonomia: agente")
    elif impatto or valori.get("Impatto-motivo"):
        errori.append("Impatto e Impatto-motivo valgono solo con Autonomia: agente")
    for esiti in valori.get("Esiti", []):
        for voce in esiti.split():
            stadio, _, esito = voce.partition("=")
            if stadio not in STADI or esito not in {"materia", "vuoto"}:
                errori.append(f"voce di Esiti non valida: {voce}")
    for prossimo in valori.get("Prossimo", []):
        if not PROSSIMO.match(prossimo):
            errori.append(f"Prossimo senza (confermato) o (cambiato, era …; …): {prossimo}")
    if giro:
        for richiesto in ("Esiti", "Prossimo", "Impatto-motivo"):
            if not valori.get(richiesto):
                errori.append(f"giro: {richiesto} assente")
        if not agente:
            errori.append("giro: Autonomia deve essere agente")
        if impatto and impatto[0] == "basso":
            errori.append("giro: Impatto almeno medio")
    return errori


def dopo(root: Path, giro: bool) -> int:
    errori = errori_trailer(trailer(root), giro)
    for errore in errori:
        print(errore)
    pubblicato = run(["git", "log", "--oneline", "@{u}..HEAD"], root)
    if errori:
        if pubblicato.returncode == 0 and pubblicato.stdout.strip():
            print("commit non ancora pubblicato: correggibile con git commit --amend")
        else:
            print("commit già pubblicato o senza upstream: non si riscrive, si dichiara")
        return 1
    print("trailer ok")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("prima", help="formatter e controlli sui file cambiati")
    p_dopo = sub.add_parser("dopo", help="trailer dell'ultimo commit")
    p_dopo.add_argument("--giro", action="store_true", help="trailer richiesti da /cycle")
    args = parser.parse_args(argv)
    return prima(args.root) if args.comando == "prima" else dopo(args.root, args.giro)


if __name__ == "__main__":
    sys.exit(main())
