"""Ricorrenza dei dinieghi nei giri autonomi, per classe di grafia e fra repo.

Il passo 4 del perceive legge i dinieghi dell'ultimo giro; questo script vede
ciò che un giro solo non vede: la grafia che torna. Legge le chiusure con
`giro` non nullo degli ultimi `FINESTRA` giri di ogni repo leggibile da qui
(`method` e gli adottanti di `world.md` con un clone sull'host), assegna a ogni
comando negato una o più classi di grafia e stampa una riga per classe
ricorrente: almeno `SOGLIA` giri distinti, anche di repo diversi (decisioni
del custode del 2026-10-27, `o2/ricorrenza-dinieghi.md`).

Per ogni classe ricorrente dice se un commit di `method` la segnala
(`SEGNALI`, la mappa canonica coperta dai test) e, per ogni repo, se il
segnale c'era quando il diniego è avvenuto: per un adottante, dal cursore
`method_commit` e dalla data `reviewed_at` del marker; per `method`, dalla data
del commit. Tre esiti: segnale assente (una proposta), non recepito
(`/method`), recepito e ricorre (serve un permesso o uno strumento che renda
superflua la grafia, non un'altra frase). Una classe non riconosciuta esce
come «altro» col comando, perché una grafia nuova è proprio ciò che il giro
deve vedere.

Limiti dichiarati: i permessi sono quelli di oggi e l'abbinamento dei pattern
`Bash(…)` imita quello dell'harness senza esserlo; un recepimento puntuale che
non avanza il cursore del marker non si vede; i `tentativi.jsonl` degli
adottanti senza clone sull'host non si leggono, e l'uscita li nomina. La
classe del diniego (vincolo voluto, lacuna, attrito) e la causa accertata
restano al perceive. Sola lettura, solo stdlib.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from adottanti import adottanti, dichiarati, frontmatter, mostra  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STATO = Path.home() / ".local" / "state" / "ciclo"
FINESTRA = 10  # ultimi giri per repo
SOGLIA = 2  # giri distinti perché una classe ricorra

# Classe → commit di `method` che la segnala nel punto d'uso. È canone, non un
# parametro degli adottanti: una classe nuova entra qui col suo test.
SEGNALI: dict[str, str | None] = {
    "composto": "e88d81f",  # cycle: un comando per chiamata
    "for": "e88d81f",
    "graffe": "e88d81f",
    "python3-c": "e88d81f",
    "heredoc": "e88d81f",
    "fuori-perimetro": "e88d81f",
    "sostituzione": "dd0cfb2",  # cycle: $(…) e cd nel composto, dalla sonda di nixos
    "cd-composto": "dd0cfb2",
    "parentesi": None,
    "backslash": None,
    "non-concesso": None,
}

SEPARATORI = re.compile(r"&&|\|\||;|\|")
PERCORSO = re.compile(r"(?<![\w.~/-])(~/[^\s'\"]*|/home/[^\s'\"]+)")


def fuori_virgolette(comando: str) -> str:
    """Il comando con il contenuto fra virgolette sostituito da spazi."""
    uscita, aperta, prima = [], None, ""
    for c in comando:
        if aperta:
            if c == aperta and not (aperta == '"' and prima == "\\"):
                aperta = None
                uscita.append(c)
            else:
                uscita.append(" ")
        elif c in "'\"" and prima != "\\":
            aperta = c
            uscita.append(c)
        else:
            uscita.append(c)
        prima = c
    return "".join(uscita)


def pezzi(comando: str) -> list[str]:
    """I comandi di un composto, tagliati sui separatori fuori dalle virgolette."""
    nudo = fuori_virgolette(comando)
    tagli, inizio = [], 0
    for m in SEPARATORI.finditer(nudo):
        tagli.append(comando[inizio : m.start()].strip())
        inizio = m.end()
    tagli.append(comando[inizio:].strip())
    return [t for t in tagli if t]


def regole(permessi: dict) -> tuple[list[str], list[str]]:
    """I pattern `Bash(…)` di allow e deny."""

    def bash(voci: list[str]) -> list[str]:
        return [v[5:-1] for v in voci if v.startswith("Bash(") and v.endswith(")")]

    p = permessi.get("permissions", {})
    return bash(p.get("allow", [])), bash(p.get("deny", []))


def corrisponde(pezzo: str, schema: str) -> bool:
    if schema.endswith(":*"):
        schema = schema[:-2] + " *"
    if schema.endswith(" *") and pezzo == schema[:-2]:
        return True
    return fnmatch.fnmatchcase(pezzo, schema)


def concesso(pezzo: str, allow: list[str], deny: list[str]) -> bool:
    if any(corrisponde(pezzo, s) for s in deny):
        return False
    return any(corrisponde(pezzo, s) for s in allow)


def classi_bash(comando: str, checkout: Path, allow: list[str], deny: list[str]) -> list[str]:
    """Le classi di grafia di un comando Bash negato; vuota se nessuna."""
    nudo = fuori_virgolette(comando)
    parti = pezzi(comando)
    composto = len(parti) > 1
    trovate = []
    if "$(" in nudo or "`" in nudo:
        trovate.append("sostituzione")
    if re.search(r"(?<!\$)\(", nudo.replace("$(", "")) or (")" in nudo and "$(" not in nudo):
        trovate.append("parentesi")
    if re.search(r"(?<!\$)\{[^}\s]*(,|\.\.)[^}\s]*\}", nudo):
        trovate.append("graffe")
    if "\\" in nudo:
        trovate.append("backslash")
    if re.search(r"(^|[;&|]\s*)(for|while|until)\b", nudo.strip()):
        trovate.append("for")
    if re.search(r"\bpython3?\s+-c\b", nudo):
        trovate.append("python3-c")
    if "<<" in nudo and composto:
        trovate.append("heredoc")
    if composto and any(p.split()[:1] == ["cd"] for p in parti):
        trovate.append("cd-composto")
    if any(not concesso(p, allow, deny) for p in parti):
        trovate.append("composto" if composto else "non-concesso")
    if any(fuori(m, checkout) for m in PERCORSO.findall(comando)):
        trovate.append("fuori-perimetro")
    return trovate


def fuori(percorso: str, checkout: Path) -> bool:
    assoluto = Path(percorso.replace("~", str(Path.home()), 1))
    return not str(assoluto).startswith(str(checkout))


def classi(diniego: dict, checkout: Path, allow: list[str], deny: list[str]) -> list[str]:
    strumento, testo = diniego.get("tool", ""), diniego.get("input") or ""
    if strumento == "Bash":
        return classi_bash(testo, checkout, allow, deny)
    if PERCORSO.search(testo) and any(fuori(m, checkout) for m in PERCORSO.findall(testo)):
        return ["fuori-perimetro"]
    return []


def tentativi(nome: str, checkout: Path) -> Path | None:
    for candidato in (
        checkout / "i1" / "giri" / "tentativi.jsonl",
        STATO / nome / "tentativi.jsonl",
    ):
        if candidato.exists():
            return candidato
    return None


def giri(file: Path, finestra: int = FINESTRA) -> list[dict]:
    """Le ultime `finestra` chiusure con `giro` non nullo."""
    chiusure = []
    for riga in file.read_text(encoding="utf-8").splitlines():
        try:
            voce = json.loads(riga)
        except ValueError:
            continue
        if voce.get("evento") == "chiusura" and voce.get("giro"):
            chiusure.append(voce)
    return chiusure[-finestra:]


def data_commit(commit: str) -> dt.date | None:
    esito = subprocess.run(
        ["git", "-C", str(ROOT), "log", "-1", "--format=%cs", commit],
        capture_output=True,
        text=True,
        check=False,
    )
    return dt.date.fromisoformat(esito.stdout.strip()) if esito.returncode == 0 else None


def antenato(commit: str, discendente: str) -> bool:
    return (
        subprocess.run(
            ["git", "-C", str(ROOT), "merge-base", "--is-ancestor", commit, discendente],
            capture_output=True,
            check=False,
        ).returncode
        == 0
    )


def recepimento(nome: str, checkout: Path) -> tuple[str, dt.date | None]:
    """(method_commit, reviewed_at) del marker; per `method` vuoto: il canone è lui."""
    if checkout == ROOT:
        return "", None
    marker = frontmatter(mostra(checkout, "i3/allineamento-metodo.md", "HEAD"))
    try:
        quando = dt.date.fromisoformat(marker.get("reviewed_at", ""))
    except ValueError:
        quando = None
    return marker.get("method_commit", ""), quando


def stato_segnale(classe: str, nome: str, checkout: Path, giorno: dt.date) -> str:
    """`assente`, `non recepito` o `recepito` al giorno del diniego."""
    segnale = SEGNALI.get(classe)
    if not segnale:
        return "assente"
    if checkout == ROOT:
        nato = data_commit(segnale)
        return "recepito" if nato and giorno >= nato else "non recepito"
    cursore, quando = recepimento(nome, checkout)
    if cursore and antenato(segnale, cursore) and quando and giorno >= quando:
        return "recepito"
    return "non recepito"


def repo_leggibili() -> tuple[dict[str, Path], list[str]]:
    leggibili = {"method": ROOT}
    for nome, checkout in adottanti().items():
        leggibili[nome] = checkout
    mancanti = [n for n in dichiarati() if n not in leggibili]
    return leggibili, mancanti


def raccogli(leggibili: dict[str, Path], finestra: int = FINESTRA):
    """(occorrenze, altri, letti): occorrenze per classe, comandi senza classe."""
    occorrenze: dict[str, list[tuple[str, str, dt.date]]] = {}
    altri, letti = [], []
    for nome, checkout in leggibili.items():
        file = tentativi(nome, checkout)
        if file is None:
            continue
        permessi = checkout / "o3" / "ciclo" / "permessi.json"
        allow, deny = regole(json.loads(permessi.read_text())) if permessi.exists() else ([], [])
        chiusure = giri(file, finestra)
        letti.append(f"{nome} ({len(chiusure)} giri)")
        for voce in chiusure:
            giorno = dt.date.fromisoformat(voce["ts"][:10])
            for diniego in voce.get("dinieghi") or []:
                trovate = classi(diniego, checkout, allow, deny)
                if not trovate:
                    motore = f" ({voce['engine']})" if voce.get("engine") else ""
                    testo = (diniego.get("input") or "")[:120]
                    altri.append(f"{nome} {giorno:%d/%m}{motore} {diniego.get('tool')}: {testo}")
                for classe in set(trovate):
                    occorrenze.setdefault(classe, []).append((nome, voce["id"], giorno))
    return occorrenze, altri, letti


def rapporto(occorrenze, altri, letti, mancanti, leggibili, soglia: int = SOGLIA) -> list[str]:
    righe = [f"Letti: {', '.join(letti)}."]
    if mancanti:
        righe.append(f"Non letti da qui: {', '.join(mancanti)} (tentativi sul loro host).")
    ricorrenti = {c: o for c, o in occorrenze.items() if len({g for _, g, _ in o}) >= soglia}
    if not ricorrenti:
        righe.append("Nessuna classe ricorrente.")
    for classe in sorted(ricorrenti, key=lambda c: -len({g for _, g, _ in ricorrenti[c]})):
        voci = ricorrenti[classe]
        numero = len({g for _, g, _ in voci})
        repo = sorted({n for n, _, _ in voci})
        date = sorted({d for _, _, d in voci})
        stati: dict[str, set[str]] = {}
        for nome, _, giorno in voci:
            stati.setdefault(nome, set()).add(stato_segnale(classe, nome, leggibili[nome], giorno))
        segnale = SEGNALI.get(classe)
        if not segnale:
            esito = "segnale assente: proposta in o2/"
        else:
            dopo = [n for n in repo if "recepito" in stati[n]]
            prima = [n for n in repo if "non recepito" in stati[n]]
            parti = []
            if dopo:
                parti.append(
                    f"recepito e ricorre in {', '.join(dopo)}: serve un permesso o uno strumento"
                )
            if prima:
                parti.append(f"non recepito in {', '.join(prima)}: /method")
            esito = f"segnale {segnale}; " + "; ".join(parti)
        righe.append(
            f"- {classe}: {numero} giri, {', '.join(repo)}, "
            f"{', '.join(f'{d:%d/%m}' for d in date)} — {esito}"
        )
    if altri:
        righe.append("Altro, grafie senza classe:")
        righe += [f"- {a}" for a in altri]
    return righe


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-n", type=int, default=FINESTRA, help="giri per repo")
    args = parser.parse_args(argv)
    leggibili, mancanti = repo_leggibili()
    occorrenze, altri, letti = raccogli(leggibili, args.n)
    print("\n".join(rapporto(occorrenze, altri, letti, mancanti, leggibili)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
