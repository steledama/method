"""Gate deterministico di /commit: formatter e controlli prima, trailer dopo.

La skill `commit` tiene il giudizio (delega, filing back, messaggio,
`Autonomia`); qui sta ciò che una macchina verifica da sola, lanciabile da
qualunque harness, da terminale o da un hook git (`kb/skill-composition.md`).

- `prima [--perimetro FILE...]`: formatta i file cambiati e lancia i
  controlli del profilo. Col perimetro (i file della sessione, anche come glob)
  confronta prima di scrivere: un file cambiato fuori dal perimetro esce con 3
  senza formattare nulla, perché è di un'altra sessione. Alla fine registra l'impronta del working
  tree in `.git/commit-gate-impronta`;
- `verifica`: subito prima dello staging confronta il working tree con
  l'impronta di `prima`; un file cambiato o comparso nel frattempo esce con 3.
  Proposta di economia (giro dell'11/11/2026, prettier su file di una sessione
  concorrente), recepita il 2026-11-11;
- `dopo`: verifica i trailer dell'ultimo commit. Avvisa, senza fallire, se il `Prossimo:`
  scavalca la prima riga pronta di `o1/plan.md` o se `nessuno (…)` mescola
  le forme;
Il profilo è locale, `o3/commit_gate.toml` del repo: formatter per glob e
controlli, sempre o quando cambia un glob, con l'uscita che li fa fallire.
Un adottante lancia lo script dal checkout del canone col proprio profilo.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
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
CONFERMA_MOTIVATA = re.compile(r"\(confermato[^)]")
NESSUNO_MISTO = re.compile(r"nessuno \((?:confermato|cambiato)\b")
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
COAUTORIA = re.compile(r"^(co-authored-by|generated-by|assisted-by)$", re.IGNORECASE)
FUORI_PERIMETRO = 3
IMPRONTA = "commit-gate-impronta"


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


def nel_perimetro(path: str, perimetro: list[str]) -> bool:
    return any(path == voce or fnmatch.fnmatch(path, voce) for voce in perimetro)


def normalizza_perimetro(perimetro: list[str]) -> list[str]:
    voci = []
    for voce in perimetro:
        voce = voce.replace("\\", "/")
        while voce.startswith("./"):
            voce = voce[2:]
        voci.append(voce)
    return voci


def impronta(root: Path) -> dict[str, str]:
    """Path e hash del contenuto dei file cambiati: ciò che lo staging prenderà."""
    voci = {}
    for path in sorted(cambiati(root)):
        file = root / path
        voci[path] = hashlib.sha256(file.read_bytes()).hexdigest() if file.is_file() else "-"
    return voci


def file_impronta(root: Path) -> Path:
    cartella = run(["git", "rev-parse", "--absolute-git-dir"], root).stdout.strip()
    return Path(cartella) / IMPRONTA


def verifica(root: Path) -> int:
    file = file_impronta(root)
    if not file.exists():
        print("impronta assente: lancia prima `commit_gate.py prima`")
        return FUORI_PERIMETRO
    attesa = json.loads(file.read_text(encoding="utf-8"))
    attuale = impronta(root)
    diversi = sorted(p for p in attesa.keys() | attuale.keys() if attesa.get(p) != attuale.get(p))
    if diversi:
        print("working tree cambiato dopo il gate: " + ", ".join(diversi))
        print("non fare lo staging: un'altra sessione sta scrivendo nel checkout")
        return FUORI_PERIMETRO
    print("impronta ok")
    return 0


def profilo(root: Path) -> dict:
    path = root / PROFILO
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def prima(root: Path, perimetro: list[str] | None = None) -> int:
    conf = profilo(root)
    files = cambiati(root)
    if perimetro is not None:
        perimetro = normalizza_perimetro(perimetro)
        fuori = [f for f in files if not nel_perimetro(f, perimetro)]
        if fuori:
            # Prima di qualunque scrittura: quei file sono di un'altra sessione.
            print("file cambiati fuori dal perimetro, nessun file formattato: " + ", ".join(fuori))
            return FUORI_PERIMETRO
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
    file_impronta(root).write_text(json.dumps(impronta(root), indent=1), encoding="utf-8")
    return 1 if falliti else 0


def trailer(root: Path, ref: str = "HEAD") -> list[tuple[str, str]]:
    uscita = run(["git", "log", "-1", "--format=%(trailers:unfold)", ref], root).stdout
    coppie = []
    for riga in uscita.splitlines():
        if ":" in riga:
            chiave, valore = riga.split(":", 1)
            coppie.append((chiave.strip(), valore.strip()))
    return coppie


def errori_trailer(coppie: list[tuple[str, str]]) -> list[str]:
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
        if not PROSSIMO.match(prossimo) and CONFERMA_MOTIVATA.search(prossimo):
            errori.append(
                "Prossimo: (confermato) non prende motivo, il riesame va nel corpo "
                f"del commit e nel resoconto: {prossimo}"
            )
        elif not PROSSIMO.match(prossimo):
            errori.append(
                f"Prossimo senza (confermato), (cambiato, era …; …) o nessuno (…): {prossimo}"
            )
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
    avvisi = [
        f"avviso: Prossimo {valore} mescola le forme; nessuno (<motivo>) prende solo il motivo"
        for chiave, valore in coppie
        if chiave == "Prossimo" and NESSUNO_MISTO.match(valore)
    ]
    plan = root / PLAN
    if not plan.exists():
        return avvisi
    testo = plan.read_text(encoding="utf-8")
    pronta = prima_pronta(testo)
    tasks = {task for task, _ in righe_plan(testo)}
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


def dopo(root: Path) -> int:
    coppie = trailer(root)
    errori = errori_trailer(coppie)
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
    p_prima = sub.add_parser("prima", help="formatter e controlli sui file cambiati")
    p_prima.add_argument(
        "--perimetro",
        nargs="+",
        help="i file della sessione; fuori perimetro esce con 3",
    )
    sub.add_parser("verifica", help="prima dello staging: working tree uguale all'impronta")
    sub.add_parser("dopo", help="trailer dell’ultimo commit")
    args = parser.parse_args(argv)
    if args.comando == "verifica":
        return verifica(args.root)
    return prima(args.root, args.perimetro) if args.comando == "prima" else dopo(args.root)


if __name__ == "__main__":
    sys.exit(main())
