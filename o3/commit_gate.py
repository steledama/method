"""Gate deterministico di /commit: formatter e controlli prima, trailer dopo.

La skill `commit` tiene il giudizio (delega, filing back, messaggio,
`Autonomia`); qui sta ciò che una macchina verifica da sola, lanciabile da
qualunque harness, da terminale o da un hook git (`kb/skill-composition.md`).

- `prima`: formatta i file cambiati e lancia i controlli del profilo;
- `dopo [--giro]`: verifica i trailer dell'ultimo commit; `--giro` aggiunge
  quelli che `/cycle` richiede. Avvisa, senza fallire, se il `Prossimo:`
  scavalca la prima riga pronta di `o1/plan.md`.

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
PLAN = Path("o1/plan.md")
STADI = {"perceive", "interpret", "compare", "plan", "specify", "perform"}
IMPATTI = ["basso", "medio", "alto"]
PROSSIMO = re.compile(r"nessuno \(.+\)$|.+ \((confermato|cambiato, era .+; .+)\)$")
TASK_PROSSIMO = re.compile(r"(.+?) \((?:confermato|cambiato, era .+; .+)\)$")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
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
            errori.append(
                f"Prossimo senza (confermato), (cambiato, era …; …) o nessuno (…): {prossimo}"
            )
    if giro:
        for richiesto in ("Esiti", "Prossimo", "Impatto-motivo"):
            if not valori.get(richiesto):
                errori.append(f"giro: {richiesto} assente")
        if not agente:
            errori.append("giro: Autonomia deve essere agente")
        if impatto and impatto[0] == "basso":
            errori.append("giro: Impatto almeno medio")
    return errori


def righe_plan(testo: str) -> list[tuple[str, str]]:
    """Coppie (Task, Dip.) della tabella dei task, in ordine; un link
    markdown nella cella vale per il suo testo."""
    colonne: list[str] = []
    righe = []
    for riga in testo.splitlines():
        if not riga.startswith("|"):
            if colonne:
                break
            continue
        celle = [LINK.sub(r"\1", c).strip() for c in riga.strip().strip("|").split("|")]
        if not colonne:
            if "Task" in celle and "Dip." in celle:
                colonne = celle
            continue
        if set("".join(celle)) <= set("-: "):
            continue
        voce = dict(zip(colonne, celle))
        righe.append((voce.get("Task", ""), voce.get("Dip.", "")))
    return righe


def prima_pronta(testo: str) -> str | None:
    """Titolo della prima riga con `Dip.` a `—` nella tabella dei task."""
    return next((task for task, dip in righe_plan(testo) if dip == "—"), None)


def avvisi_prossimo(coppie: list[tuple[str, str]], root: Path) -> list[str]:
    """Il `Prossimo:` contro la coda: scavalcare la prima riga pronta si
    può (lettura strategica di `exec plan`), ma va visto e motivato."""
    plan = root / PLAN
    if not plan.exists():
        return []
    testo = plan.read_text(encoding="utf-8")
    pronta = prima_pronta(testo)
    tasks = {task for task, _ in righe_plan(testo)}
    avvisi = []
    for chiave, valore in coppie:
        trovato = TASK_PROSSIMO.match(valore) if chiave == "Prossimo" else None
        if not trovato or trovato.group(1) == pronta:
            continue
        if trovato.group(1) not in tasks:
            avvisi.append(
                f"avviso: Prossimo {trovato.group(1)} non è una riga di {PLAN}; "
                "senza task pronti la forma è nessuno (<motivo>)"
            )
        elif pronta is None:
            avvisi.append(f"avviso: Prossimo {trovato.group(1)} con nessuna riga pronta in {PLAN}")
        else:
            avvisi.append(
                f"avviso: Prossimo {trovato.group(1)} scavalca la prima riga pronta "
                f"di {PLAN}, {pronta}: il corpo nomina la riga scavalcata e il motivo"
            )
    return avvisi


def dopo(root: Path, giro: bool) -> int:
    coppie = trailer(root)
    errori = errori_trailer(coppie, giro)
    for errore in errori:
        print(errore)
    for avviso in avvisi_prossimo(coppie, root):
        print(avviso)
    pubblicato = run(["git", "log", "--oneline", "@{u}..HEAD"], root)
    if errori:
        if pubblicato.returncode == 0 and pubblicato.stdout.strip():
            print("commit non pubblicato: correggibile prima del push, con l'amend dove è concesso")
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
