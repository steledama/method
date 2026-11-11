"""Lanciatore canonico del ciclo autonomo: uguale per ogni repo, per ogni sistema.

Fa solo ciò che l'agente non può fare da sé: lock, `pull --ff-only`, avvio di
`claude -p` coi permessi del repo e l'hook sulle sessioni concorrenti, tetto di
tempo e di costo, righe `partenza` e `chiusura` in `i1/giri/`, scritte anche
quando l'agente si pianta. Il ciclo vive nell'artefatto (`o3/ciclo/prompt.md`,
`o3/ciclo/permessi.json`), all'host resta il trigger. Decisione del custode del
2026-11-08 (`o2/lanciatore-ciclo-nel-metodo.md`).

Si lancia nella radice del repo, dal checkout del canone:
`python3 method/../o3/lanciatore.py`. Con `--controlli` esegue i controlli in sola
lettura, senza lock, tracce né agente.

Il profilo locale `o3/ciclo/lanciatore.toml` è opzionale:

    branch = "main"
    minuti = 45
    budget_usd = 5
    protetti = ["o3/mio-recinto/*"]     # si aggiungono a quelli canonici
    prima = "o3/ciclo/prima.py"         # controlli locali, prima dell'agente
    pull_fermo = ["o3/runtime/*"]       # un pull che li tocca resta al custode
    motori = ["claude", "codex"]        # chi lavora e chi subentra; default ["claude"]

`pull_fermo` è per i repo in cui il checkout è anche la produzione: lì il pull è
un rilascio, e il suo momento lo sceglie una persona.

L'host può asserire `--branch` uguale al profilo (11 se diverso) e passare
`--max-minuti` e `--max-budget-usd`: valori positivi finiti, applicati come
minimo col profilo, anche sotto `--controlli`. Non possono ampliare la delega.

Il motore lo sceglie il repo, non l'host (custode, 2026-11-11): `motori` dà
l'ordine, il primo lavora e il secondo subentra una volta sola, solo se il primo
era indisponibile prima di qualunque atto. Vale nei due versi, `["codex",
"claude"]` compreso. Codex passa dall'esecutore canonico `o3/esecutore_codex.py`,
che traduce permessi e hook; l'host dà solo i binari, `--claude` e `--codex`,
se non sono nel PATH. `budget_usd` è il tetto dove il motore lo sa imporre:
Codex non ne ha uno, il giro procede e la chiusura dichiara
`budget_usd_imposto: false`. Contratto in `o3/ciclo/fallback.md`.

L'aggancio `prima` è uno script Python in `o3/ciclo/`, dove il giro non scrive.
Esce con 0 per proseguire o con 16, 18 o 19 per fermare il giro, con
il motivo sulla prima riga dell'uscita. Con 0 può stampare un oggetto JSON:
`minuti` accorcia il tetto, senza poterlo alzare, `attenzione` aggiunge un
avviso alla chiusura, `salta: true` esce senza lasciare tracce. L'aggancio
riceve `LANCIATORE_MODO`, `giro` o `controlli`: sotto `--controlli` dà la
diagnosi senza attese, per esempio quella di uno slot.

All'avvio il lanciatore aggiorna con `pull --ff-only` anche il proprio checkout
del canone, se è un altro repo e pulito: vale dal giro successivo, e se non
riesce è un avviso con la prima riga dell'errore di git. Un lock nella cartella
git del canone mette in fila i pull di giri partiti insieme da repo diversi.
L'host che non vuole il pull lo spegne con `--senza-pull-canone`.

La chiusura conta come commit del giro solo quelli fatti dall'agente: il
lanciatore gli passa `GIT_REFLOG_ACTION=lanciatore <id>`, nell'ambiente e nelle
impostazioni, e legge il reflog di HEAD. `commit_giro` li elenca, `oggetto` e
`push` guardano l'ultimo; `commit_altri` conta quelli entrati nel frattempo da
altre sessioni, che il cambio di HEAD da solo scambierebbe per il giro.

Le sessioni aperte non fermano il giro (custode, 2026-11-10): una sessione
Claude o Codex lasciata aperta e ferma nel checkout è innocua. Conta quella che
lavora mentre il giro gira, perché il commit del giro potrebbe portarsi dietro le
sue modifiche. Il lanciatore tocca `.git/lanciatore/inizio-giro` prima
dell'agente e gli passa un hook `PreToolUse` che, davanti a un `git commit`,
cerca transcript Claude e rollout Codex nel checkout con una chiamata a uno
strumento dopo il marker: se ne trova blocca il commit. Scrivere non basta, la
sessione che avvia il giro a mano scrive la propria risposta dopo il marker. Dopo l'agente, un giro senza commit con il tree
sporco e una sessione concorrente chiude con 15 `sessione-concorrente` e le
sessioni nella riga di chiusura; il tree resta al custode.

Il recinto sta nei permessi dell'harness. La rete è in chiusura: se i commit del
giro toccano un percorso protetto la chiusura è rossa e i giri successivi si
fermano finché una persona non toglie `.git/lanciatore/fermo`. Un host con una
sandbox la passa con `--recinto "comando con argomenti"`, che precede l'agente:
il lanciatore resta fuori, dove può leggere i processi e fare il pull. L'opzione è
dell'host, mai del repo, che non può allargarsi il recinto da solo. Se la sandbox
non muore con il proprio comando, come un'unità di `systemd-run`, l'host passa con
`--recinto-ferma` il comando che la ferma e ne attende la fine: il lanciatore lo
lancia prima di chiudere, così nessun commit dell'agente cade dopo la chiusura.
Lo scheduler che ferma il lanciatore gli lascia quindi più tempo di quanto la
sandbox ne lasci all'agente: altrimenti il lanciatore muore mentre aspetta, e
la chiusura non si scrive.

La rete guarda i commit del giro anche quando il giro finisce male (tetto,
uscita con errore, interruzione): un percorso protetto toccato vale 23 e ferma i
giri successivi qualunque sia stata la fine. Fra i protetti entra anche la
cartella di `core.hooksPath`, se è versionata nel repo.

Il lanciatore gira fuori dal recinto e usa git nel checkout: ciò che git esegue da
lì non lo deve scrivere il giro. Ogni repo nega quindi al giro, nei permessi e
nella sandbox dove c'è, `o3/lanciatore.py` se il repo è il canone, `.git/config`,
`.git/hooks`, `.git/lanciatore` e la cartella degli hook versionati. I primi due
coprono anche `core.fsmonitor`, `core.hooksPath` e gli alias.

Codici di uscita, gli stessi dell'unità di `nixos`: 0 riuscito, 10 tree sporco,
11 branch inatteso o senza upstream, 12 divergente, 13 fetch o pull falliti,
14 prompt, permessi, profilo, aggancio o `i1/giri` non adatti, 15 sessione
concorrente durante il giro,
16, 18 e 19 riservati all'aggancio `prima`, 17 pull fermo, 20 agente
uscito con errore, 21 errore riportato dall'agente, 22 tetto di tempo, 23 percorso
protetto toccato dal giro, 24 giri fermi dopo un 23 o 25,
25 arresto del recinto non verificato, 75 lock.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import math
import os
import re
import shlex
import shutil
import signal
import socket
import subprocess
import sys
import time
import tomllib
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field, replace
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

PROMPT = Path("o3/ciclo/prompt.md")
PERMESSI = Path("o3/ciclo/permessi.json")
PROFILO = Path("o3/ciclo/lanciatore.toml")
GIRI = Path("i1/giri")
STATO = Path(".git/lanciatore")
INIZIO = STATO / "inizio-giro"
STREAM_TENUTI = 60
CODA_BYTE = 4 * 1024 * 1024  # la coda di un transcript che basta a coprire un giro
GIT_SECONDI = 120
GRAZIA_SECONDI = 15
FERMA_SECONDI = 120
PRIMA_SECONDI = 20 * 60  # un aggancio può aspettare, per esempio la fine di un run
CODICI_PRIMA = (16, 18, 19)
DINIEGO_CARATTERI = 1000
# Ciò che definisce il giro non lo modifica il giro.
PROTETTI = (
    "o3/ciclo/*",
    "o3/lanciatore.py",
    ".claude/*",
    ".codex/*",
    "autonomy.md",
    "CLAUDE.md",
    "AGENTS.md",
)
# `git commit`, anche come `git -C <dir> commit` o dopo altri comandi.
COMMIT = re.compile(r"(^|[^\w-])git(\s[^;&|]*)?\scommit(\s|$)")
ATTENZIONE = re.compile(r"^\s*\**Attenzione:?\**:?\s*(.*)$", re.IGNORECASE)
WINDOWS = os.name == "nt"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
USCITA_PERCORSI_PROTETTI = 23
# I motori che il profilo del repo può scegliere e se sanno imporre un tetto in USD.
# Codex non ne ha uno: il giro procede e la chiusura lo dichiara (custode, 2026-11-11).
MOTORI = {"claude": True, "codex": False}
ESECUTORE_CODEX = Path(__file__).resolve().parent / "esecutore_codex.py"


class Arresto(Exception):
    """Un controllo non è passato: il giro non parte, o non è valido."""

    def __init__(self, codice: int, motivo: str, dettaglio: str = ""):
        super().__init__(motivo)
        self.codice = codice
        self.motivo = motivo
        self.dettaglio = dettaglio


class Interrotto(Exception):
    """Lo scheduler ha chiesto di terminare: la chiusura si scrive lo stesso."""


@dataclass(frozen=True)
class Profilo:
    branch: str = "main"
    minuti: float = 45
    budget_usd: float = 5
    protetti: tuple[str, ...] = PROTETTI
    prima: str | None = None
    pull_fermo: tuple[str, ...] = ()
    motori: tuple[str, ...] = ("claude",)


def leggi_profilo(path: Path) -> Profilo:
    if not path.exists():
        return Profilo()
    try:
        dati = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as errore:
        raise Arresto(14, "profilo-invalido", str(errore)) from errore
    ignote = dati.keys() - {
        "branch",
        "minuti",
        "budget_usd",
        "protetti",
        "prima",
        "pull_fermo",
        "motori",
    }
    if ignote:
        raise Arresto(14, "profilo-invalido", f"chiavi sconosciute {sorted(ignote)}")
    motori = dati.get("motori", ["claude"])
    if (
        not isinstance(motori, list)
        or not 1 <= len(motori) <= 2
        or len(set(motori)) != len(motori)
        or any(m not in MOTORI for m in motori)
    ):
        raise Arresto(
            14, "profilo-invalido", f"motori: uno o due fra {sorted(MOTORI)}, senza ripetizioni"
        )
    return Profilo(
        dati.get("branch", "main"),
        dati.get("minuti", 45),
        dati.get("budget_usd", 5),
        (*PROTETTI, *dati.get("protetti", [])),
        dati.get("prima"),
        tuple(dati.get("pull_fermo", [])),
        tuple(motori),
    )


@dataclass(frozen=True)
class EsitoPrima:
    profilo: Profilo
    attenzione: str | None = None
    salta: bool = False
    accorciato: bool = False


def limiti_host(
    profilo: Profilo, branch: str | None, minuti: float | None, budget: float | None
) -> Profilo:
    """Host assertions and caps never widen repository authority."""
    if branch is not None and branch != profilo.branch:
        raise Arresto(11, "branch-host-incoerente", branch)
    valori = {}
    for nome, limite in (("minuti", minuti), ("budget_usd", budget)):
        valore = getattr(profilo, nome)
        if (
            isinstance(valore, bool)
            or not isinstance(valore, (int, float))
            or not math.isfinite(valore)
            or valore <= 0
        ):
            raise Arresto(14, "profilo-invalido", nome)
        if limite is not None:
            if not math.isfinite(limite) or limite <= 0:
                raise Arresto(14, "limite-host-invalido", nome)
            valori[nome] = min(valore, limite)
    return replace(profilo, **valori)


def tetto_residuo(esito: EsitoPrima, trascorsi: float) -> Profilo:
    """Il tetto dell'aggancio vale dal suo orologio, non dall'avvio dell'agente.

    Fetch e pull fra i due si scalano: un limite come «entro le :50» non si sfora.
    """
    if not esito.accorciato:
        return esito.profilo
    minuti = esito.profilo.minuti - trascorsi / 60
    if minuti <= 0:
        raise Arresto(22, "tetto-di-tempo", "esaurito prima dell'avvio dell'agente")
    return replace(esito.profilo, minuti=minuti)


def esegui_prima(profilo: Profilo, modo: str = "giro") -> EsitoPrima:
    """I controlli locali del repo: possono fermare, accorciare, mai allargare."""
    if profilo.prima is None:
        return EsitoPrima(profilo)
    percorso = Path(profilo.prima)
    if (
        not profilo.prima.startswith("o3/ciclo/")
        or ".." in percorso.parts
        or not percorso.is_file()
    ):
        raise Arresto(14, "prima-invalido", profilo.prima)
    try:
        esito = subprocess.run(
            [sys.executable, percorso.as_posix()],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdin=subprocess.DEVNULL,
            env={**os.environ, "LANCIATORE_MODO": modo},
            timeout=PRIMA_SECONDI,
            creationflags=NO_WINDOW,
            check=False,
        )
    except subprocess.TimeoutExpired as errore:
        raise Arresto(14, "prima-tetto", profilo.prima) from errore
    testo = esito.stdout.strip()
    if esito.returncode in CODICI_PRIMA:
        raise Arresto(esito.returncode, testo.splitlines()[0] if testo else "prima")
    if esito.returncode != 0:
        dettaglio = esito.stderr.strip().splitlines()[-1:] or [""]
        raise Arresto(14, f"prima-codice-{esito.returncode}", dettaglio[0])
    try:
        dati = json.loads(testo) if testo else {}
    except ValueError as errore:
        raise Arresto(14, "prima-invalido", "uscita non JSON") from errore
    if not isinstance(dati, dict) or dati.keys() - {"minuti", "attenzione", "salta"}:
        raise Arresto(14, "prima-invalido", "uscita con chiavi sconosciute")
    minuti = dati.get("minuti", profilo.minuti)
    if not isinstance(minuti, int | float) or minuti <= 0:
        raise Arresto(14, "prima-invalido", f"minuti {minuti}")
    return EsitoPrima(
        replace(profilo, minuti=min(profilo.minuti, minuti)),
        dati.get("attenzione"),
        dati.get("salta") is True,
        minuti < profilo.minuti,
    )


def ora() -> datetime:
    return datetime.now().astimezone()


def iso(momento: datetime) -> str:
    return momento.isoformat(timespec="seconds")


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdin=subprocess.DEVNULL,
        timeout=GIT_SECONDI,
        creationflags=NO_WINDOW,
        check=False,
    )


def git_testo(*args: str) -> str:
    return git(*args).stdout.strip()


def _dentro(cwd: str, checkout: Path | str, percorsi: Any = os.path) -> bool:
    """`cwd` è il checkout o una sua sottocartella, con le regole del sistema."""
    interno = percorsi.normcase(cwd)
    radice = percorsi.normcase(str(checkout))
    return interno == radice or interno.startswith(f"{radice}{percorsi.sep}")


def cartella_claude() -> Path:
    return Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "projects"


def cartella_codex() -> Path:
    return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex") / "sessions"


def _cwd_transcript(file: Path, righe: int = 50) -> str | None:
    """La cwd dichiarata nelle prime righe di un transcript Claude."""
    try:
        with file.open(encoding="utf-8", errors="replace") as testo:
            for numero, riga in enumerate(testo):
                if numero >= righe:
                    break
                try:
                    evento = json.loads(riga)
                except ValueError:
                    continue
                if isinstance(evento, dict) and isinstance(evento.get("cwd"), str):
                    return evento["cwd"]
    except OSError:
        return None
    return None


def _chiamata(evento: dict) -> bool:
    """Una chiamata a uno strumento: in Claude un `tool_use`, in Codex un `*_call`."""
    if evento.get("type") == "assistant":
        contenuto = (evento.get("message") or {}).get("content")
        return isinstance(contenuto, list) and any(
            isinstance(parte, dict) and parte.get("type") in {"tool_use", "server_tool_use"}
            for parte in contenuto
        )
    if evento.get("type") == "response_item":
        tipo = (evento.get("payload") or {}).get("type")
        return isinstance(tipo, str) and tipo.endswith("_call")
    return False


def _istante(evento: dict) -> float | None:
    try:
        return datetime.fromisoformat(evento["timestamp"]).timestamp()
    except (KeyError, AttributeError, TypeError, ValueError):
        return None


def lavora_dopo(file: Path, dopo: float, coda: int = CODA_BYTE) -> bool:
    """La sessione ha chiamato uno strumento dopo l'istante `dopo`.

    Scrivere non basta: la sessione che avvia il giro a mano ne scrive la
    risposta subito dopo il marker, e non lavora nel checkout (sessione
    economia, 2026-11-10). Si legge la coda del file, dal fondo, fino al primo
    evento anteriore al marker.
    """
    try:
        if file.stat().st_mtime <= dopo:
            return False
        with file.open("rb") as testo:
            testo.seek(max(0, file.stat().st_size - coda))
            righe = testo.read().decode("utf-8", errors="replace").splitlines()
    except OSError:
        return False
    for riga in reversed(righe):
        try:
            evento = json.loads(riga)
        except ValueError:
            continue
        if not isinstance(evento, dict):
            continue
        momento = _istante(evento)
        if momento is None:
            continue
        if momento <= dopo:
            return False
        if _chiamata(evento):
            return True
    return False


def concorrenti(
    checkout: Path, dopo: float, claude: Path | None = None, codex: Path | None = None
) -> list[str]:
    """Le sessioni Claude o Codex che hanno lavorato nel checkout dopo l'istante `dopo`.

    Una sessione aperta e ferma non conta (custode, 2026-11-10); lavorare è
    chiamare uno strumento, non solo scrivere il transcript (`lavora_dopo`).
    Claude tiene i transcript in `projects/<checkout codificato>`, ogni carattere
    non alfanumerico del path diventato `-`; una sottocartella aggiunge un
    suffisso, e lì la cwd del transcript decide. Il giro gira con
    `--no-session-persistence` e non ne lascia di suoi. Le sessioni Codex sono
    thread di un demone: la cwd sta nella `session_meta` del rollout.
    """
    trovate = []
    claude = claude or cartella_claude()
    codex = codex or cartella_codex()
    codifica = os.path.normcase(re.sub(r"[^A-Za-z0-9]", "-", str(checkout)))
    if claude.is_dir():
        for cartella in sorted(claude.iterdir()):
            nome = os.path.normcase(cartella.name)
            if nome != codifica and not nome.startswith(f"{codifica}-"):
                continue
            for file in sorted(cartella.glob("*.jsonl")):
                if not lavora_dopo(file, dopo):
                    continue
                cwd = _cwd_transcript(file)
                if (cwd and _dentro(cwd, checkout)) or (not cwd and nome == codifica):
                    trovate.append(f"claude: {file}")
    if codex.is_dir():
        for rollout in sorted(codex.rglob("rollout-*.jsonl")):
            if not lavora_dopo(rollout, dopo):
                continue
            try:
                with rollout.open(encoding="utf-8") as file:
                    testa = json.loads(file.readline())
            except (OSError, ValueError):
                continue
            meta = testa.get("payload") if isinstance(testa, dict) else None
            cwd = meta.get("cwd") if testa.get("type") == "session_meta" and meta else None
            if isinstance(cwd, str) and _dentro(cwd, checkout):
                trovate.append(f"codex: {rollout}")
    return trovate


def comando_hook() -> str:
    """L'hook `PreToolUse` del giro: questo file, con l'interprete che lo esegue.

    `pythonw` non ha stderr, e l'hook ci scrive il motivo del blocco.
    """
    interprete = Path(sys.executable)
    if interprete.name.lower() == "pythonw.exe":
        interprete = interprete.with_name("python.exe")
    script = Path(__file__).resolve()
    return f"{shlex.quote(interprete.as_posix())} {shlex.quote(script.as_posix())} --hook-commit"


def hook_commit(ingresso: str) -> int:
    """Davanti a un `git commit` del giro: 2 lo blocca, 0 lo lascia passare.

    Blocca se un'altra sessione ha lavorato nel checkout dopo il marker
    `inizio-giro`, che il lanciatore tocca subito prima dell'agente: il commit
    del giro potrebbe portarsi dietro le sue modifiche. Senza marker non è un
    giro e l'hook tace.
    """
    try:
        dati = json.loads(ingresso)
    except ValueError:
        return 0
    comando = (dati.get("tool_input") or {}).get("command") if isinstance(dati, dict) else None
    if not isinstance(comando, str) or not COMMIT.search(comando):
        return 0
    cwd = dati.get("cwd") if isinstance(dati.get("cwd"), str) else os.getcwd()
    radice = git_testo("-C", cwd, "rev-parse", "--show-toplevel")
    if not radice:
        return 0
    checkout = Path(radice).resolve()
    try:
        dopo = (checkout / INIZIO).stat().st_mtime
    except OSError:
        return 0
    trovate = concorrenti(checkout, dopo)
    if not trovate:
        return 0
    righe = [
        "lanciatore: commit bloccato, un'altra sessione ha lavorato nel checkout durante il giro:",
        *(f"  {voce}" for voce in trovate),
        "Non committare e non riprovare: lascia il working tree com'è, chiudi il giro e",
        "dichiaralo nella riga Attenzione: del resoconto (sessione-concorrente).",
        "Il custode riconcilia le modifiche.",
    ]
    print("\n".join(righe), file=sys.stderr)
    return 2


def commit_del_giro(etichetta: str) -> list[str]:
    """I commit fatti dal giro, dal più vecchio: le voci del reflog con la sua etichetta.

    Il cambio di HEAD non basta: una sessione del custode può committare mentre
    il giro gira. Il lanciatore dà all'agente `GIT_REFLOG_ACTION`, che git scrive
    nel reflog di ogni spostamento di HEAD fatto da lì.
    """
    voci = git_testo("reflog", "show", "--format=%H%x00%gs", "HEAD").splitlines()
    trovati: list[str] = []
    for voce in reversed(voci):
        sha, _, messaggio = voce.partition("\0")
        if messaggio.startswith(f"{etichetta}:") and sha not in trovati:
            trovati.append(sha)
    return trovati


def controlla_concorrenti(tentativo: Tentativo, checkout: Path, dopo: float) -> None:
    """Dopo l'agente: lavoro lasciato fuori dal commit mentre un'altra sessione scriveva.

    Un commit del giro è passato dall'hook, quindi la sessione ha scritto dopo:
    la trova fatta, come dopo un pull. Senza commit e a tree pulito non c'è
    niente da riconciliare.
    """
    if commit_del_giro(tentativo.etichetta):
        return
    if not git_testo("status", "--porcelain"):
        return
    trovate = concorrenti(checkout, dopo)
    if trovate:
        tentativo.sessioni = trovate
        raise Arresto(15, "sessione-concorrente", ", ".join(trovate))


def giri_ignorata() -> bool:
    return git("check-ignore", "-q", f"{GIRI.as_posix()}/x").returncode == 0


def controlla_file() -> None:
    if not PROMPT.is_file():
        raise Arresto(14, "prompt-mancante", str(PROMPT))
    if not PERMESSI.is_file():
        raise Arresto(14, "settings-mancante", str(PERMESSI))
    try:
        json.loads(PERMESSI.read_text(encoding="utf-8"))
    except ValueError as errore:
        raise Arresto(14, "settings-invalide", str(errore)) from errore


def controlla_tree(profilo: Profilo) -> None:
    branch = git_testo("symbolic-ref", "--short", "-q", "HEAD")
    if branch != profilo.branch:
        raise Arresto(11, "branch-inatteso", branch or "(detached)")
    if git_testo("status", "--porcelain"):
        raise Arresto(10, "checkout-sporco")


def prepara_repo(profilo: Profilo) -> str:
    """Fetch e `pull --ff-only`: ritorna l'HEAD da cui parte il giro."""
    if git("fetch", "--quiet", "origin").returncode != 0:
        raise Arresto(13, "fetch-fallito")
    if git("rev-parse", "-q", "--verify", "@{u}").returncode != 0:
        raise Arresto(11, "upstream-mancante")
    avanti, dietro = git_testo("rev-list", "--left-right", "--count", "HEAD...@{u}").split()
    if int(avanti) and int(dietro):
        raise Arresto(12, "branch-divergente", f"{avanti} avanti, {dietro} dietro")
    if int(dietro):
        fermi = percorsi_protetti("HEAD", "@{u}", profilo.pull_fermo)
        if fermi:
            raise Arresto(17, "pull-fermo", ", ".join(fermi))
        if git("pull", "--ff-only", "--quiet").returncode != 0:
            raise Arresto(13, "pull-fallito")
    return git_testo("rev-parse", "HEAD")


def aggiorna_canone(checkout: Path) -> str | None:
    """Tiene fresco il checkout del canone, se è un altro repo: ritorna un avviso."""
    canone = Path(__file__).resolve().parents[1]
    if canone == checkout or not (canone / ".git").exists():
        return None
    try:
        # Giri di repo diversi partono insieme dallo stesso canone: un pull alla volta.
        cartella = git_testo("-C", str(canone), "rev-parse", "--absolute-git-dir")
        try:
            lock = Lock(Path(cartella) / "lanciatore-pull-canone", attendi=True)
        except (OSError, Arresto):
            return "canone non aggiornato: lock del pull non ottenuto"
        if git_testo("-C", str(canone), "status", "--porcelain"):
            return "canone non aggiornato: checkout sporco"
        pull = git("-C", str(canone), "pull", "--ff-only", "--quiet")
        if pull.returncode != 0:
            righe = (pull.stderr or pull.stdout).strip().splitlines()
            causa = righe[0][:200] if righe else f"uscita {pull.returncode}"
            return f"canone non aggiornato: pull fallito ({causa})"
        lock.file.close()
    except (OSError, subprocess.SubprocessError):
        return "canone non aggiornato: git non ha risposto"
    return None


class Lock:
    """Lock del sistema operativo: muore col processo, niente file orfani da pulire."""

    def __init__(self, path: Path, attendi: bool = False):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open("a+")
        try:
            if WINDOWS:
                import msvcrt

                self.file.seek(0)
                modo = msvcrt.LK_LOCK if attendi else msvcrt.LK_NBLCK
                msvcrt.locking(self.file.fileno(), modo, 1)
            else:
                import fcntl

                fcntl.flock(self.file, fcntl.LOCK_EX | (0 if attendi else fcntl.LOCK_NB))
        except OSError as errore:
            self.file.close()
            raise Arresto(75, "lock") from errore


def impostazioni(destinazione: Path, etichetta: str = "") -> Path:
    """I permessi del repo, senza trailer di attribuzione, con l'hook sul commit."""
    dati = json.loads(PERMESSI.read_text(encoding="utf-8"))
    dati["attribution"] = {"commit": "", "pr": ""}
    if etichetta:
        # Arriva all'agente anche dentro un recinto che non eredita l'ambiente.
        dati.setdefault("env", {})["GIT_REFLOG_ACTION"] = etichetta
    hook = {"matcher": "Bash", "hooks": [{"type": "command", "command": comando_hook()}]}
    dati.setdefault("hooks", {}).setdefault("PreToolUse", []).append(hook)
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(json.dumps(dati, indent=2), encoding="utf-8")
    return destinazione


def ferma_recinto(ferma: list[str]) -> None:
    """Il comando dell'host che ferma la sandbox e ne attende la fine."""
    if not ferma:
        return
    try:
        esito = subprocess.run(
            ferma,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            timeout=FERMA_SECONDI,
            creationflags=NO_WINDOW,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as errore:
        raise Arresto(25, "recinto-arresto-non-verificato", str(errore)) from errore
    if esito.returncode != 0:
        raise Arresto(25, "recinto-arresto-non-verificato", str(esito.returncode))


def termina(processo: subprocess.Popen[bytes], ferma: list[str] = ()) -> None:
    """Chiude l'agente con tutti i suoi figli, e la sandbox se non muore con lui."""
    if WINDOWS:
        subprocess.run(
            ["taskkill", "/T", "/F", "/PID", str(processo.pid)],
            capture_output=True,
            creationflags=NO_WINDOW,
            check=False,
        )
        processo.wait()
        return
    try:
        os.killpg(processo.pid, signal.SIGTERM)
        processo.wait(timeout=GRAZIA_SECONDI)
    except subprocess.TimeoutExpired:
        os.killpg(processo.pid, signal.SIGKILL)
        processo.wait()
    except ProcessLookupError:
        pass


def lancia_agente(
    comando: list[str],
    stream: Path,
    profilo: Profilo,
    ferma: list[str] = (),
    etichetta: str = "",
) -> int:
    """L'agente col suo tetto di tempo; alla fine l'albero dei processi non resta."""
    stream.parent.mkdir(parents=True, exist_ok=True)
    ambiente = {**os.environ, "GIT_REFLOG_ACTION": etichetta} if etichetta else None
    with stream.open("wb") as uscita:
        processo = subprocess.Popen(
            comando,
            env=ambiente,
            stdin=subprocess.DEVNULL,
            stdout=uscita,
            stderr=subprocess.STDOUT,  # un'uscita con errore si spiega dallo stream
            start_new_session=not WINDOWS,
            creationflags=NO_WINDOW,
        )
        try:
            return processo.wait(timeout=profilo.minuti * 60)
        except subprocess.TimeoutExpired as errore:
            termina(processo, ferma)
            raise Arresto(22, "tetto-di-tempo", f"{profilo.minuti} minuti") from errore
        except Interrotto:
            termina(processo, ferma)
            raise
        finally:
            # Also stop on normal exit: the wrapper may have detached children.
            ferma_recinto(list(ferma))


def osserva(stream: Path) -> dict:
    """Keep provider evidence separate from the decision to retry."""
    eventi = []
    incompleto = False
    try:
        righe = stream.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        righe = []
    for riga in righe:
        try:
            evento = json.loads(riga)
        except ValueError:
            incompleto = True
            continue
        if isinstance(evento, dict):
            eventi.append(evento)
        else:
            incompleto = True
    risultati = [e for e in eventi if e.get("type") == "result"]
    quote = [e.get("rate_limit_info", {}) for e in eventi if e.get("type") == "rate_limit_event"]
    errori = [
        e
        for e in eventi
        if e.get("type") == "error"
        or e.get("error")
        or (e.get("message") if isinstance(e.get("message"), dict) else {}).get("error")
    ]
    ultimo = risultati[-1] if risultati else {}
    successo = any(e.get("is_error") is False for e in risultati)
    # Only explicit provider rejection; overage rejection alone is not rejection.
    rifiuto = any(q.get("status") == "rejected" for q in quote)
    rifiuto = rifiuto or any(
        e.get("error")
        in ("rate_limit", "authentication_failed", "billing_error", "overloaded_error")
        for e in eventi
        if isinstance(e.get("error"), str)
    )
    stati = [e.get("api_error_status") for e in risultati + errori]
    indisponibile = not successo and (
        rifiuto or any(x in (401, 403, 429, 503, "401", "403", "429", "503") for x in stati)
    )
    strumenti = any(_chiamata(e) or e.get("permission_denials") for e in eventi)
    tipi_noti = {"system", "assistant", "user", "result", "rate_limit_event", "error"}
    incompleto = incompleto or any(e.get("type") not in tipi_noti for e in eventi)
    return {
        "result": ultimo,
        "results": risultati,
        "rate_limit_events": quote,
        "errors": errori,
        "terminal_reason": ultimo.get("terminal_reason"),
        "api_error_status": ultimo.get("api_error_status"),
        "unavailable": indisponibile,
        "tools_started": strumenti,
        "trace_incomplete": incompleto or not eventi,
    }


def risultato(stream: Path) -> dict:
    return osserva(stream)["result"]


def dinieghi(fine: dict) -> list[dict]:
    voci = []
    for diniego in fine.get("permission_denials") or []:
        dati = diniego.get("tool_input") or {}
        valore = (
            dati.get("command")
            or dati.get("file_path")
            or dati.get("url")
            or json.dumps(dati, ensure_ascii=False)
        )
        voci.append({"tool": diniego.get("tool_name"), "input": str(valore)[:DINIEGO_CARATTERI]})
    return voci


def attenzione(testo: str) -> str | None:
    for riga in reversed(testo.splitlines()):
        trovata = ATTENZIONE.match(riga)
        if trovata:
            return trovata.group(1).strip().strip("*").strip()
    return None


def percorsi_protetti(prima: str, dopo: str, protetti: tuple[str, ...]) -> list[str]:
    """I file toccati dai commit del giro che il giro non doveva toccare."""
    nomi = git_testo("diff", "--name-only", f"{prima}..{dopo}").splitlines()
    return [nome for nome in nomi if any(fnmatch.fnmatch(nome, modello) for modello in protetti)]


def cartella_hook() -> str | None:
    """La cartella di `core.hooksPath`, se sta dentro il repo."""
    valore = git_testo("config", "--get", "core.hooksPath")
    if not valore or os.path.isabs(valore) or valore.startswith("~"):
        return None
    relativo = os.path.normpath(valore).replace("\\", "/")
    return None if relativo.startswith("..") else relativo


def rete(
    tentativo: Tentativo, profilo: Profilo, fermo: Path, causa: str | None = None
) -> Arresto | None:
    """La rete in chiusura: i commit del giro su percorsi protetti, comunque sia finito."""
    toccati = percorsi_protetti(
        tentativo.head_prima, git_testo("rev-parse", "HEAD"), profilo.protetti
    )
    if not toccati:
        return None
    fermo.write_text(
        f"il giro {tentativo.id} ha toccato {', '.join(toccati)}: rivedi e togli questo file\n",
        encoding="utf-8",
    )
    motivo = f"percorsi-protetti: {', '.join(toccati)}"
    return Arresto(USCITA_PERCORSI_PROTETTI, f"{motivo} (dopo {causa})" if causa else motivo)


def pota(cartella: Path, tenuti: int = STREAM_TENUTI) -> None:
    if not cartella.is_dir():
        return
    stream = sorted(cartella.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    for vecchio in stream[tenuti:]:
        vecchio.unlink(missing_ok=True)


@dataclass
class Tentativo:
    repo: str
    id: str = field(default_factory=lambda: os.environ.get("INVOCATION_ID") or uuid.uuid4().hex)
    inizio: datetime = field(default_factory=ora)
    head_prima: str | None = None
    claude_exit: int | None = None
    avviso: str | None = None
    partito: bool = False
    sessioni: list[str] | None = None
    engine: str = "claude"
    tentativi_engine: list[dict] = field(default_factory=list)
    budget_usd_imposto: bool = True

    @property
    def etichetta(self) -> str:
        return f"lanciatore {self.id}"

    def avvisa(self, testo: str | None) -> None:
        if testo:
            self.avviso = f"{self.avviso}; {testo}" if self.avviso else testo

    @property
    def stream(self) -> Path:
        suffisso = ".codex" if self.engine == "codex" else ""
        return GIRI / "giri" / f"{self.id}{suffisso}.jsonl"

    def scrivi(self, riga: dict) -> None:
        GIRI.mkdir(parents=True, exist_ok=True)
        with (GIRI / "tentativi.jsonl").open("a", encoding="utf-8") as file:
            file.write(json.dumps(riga, ensure_ascii=False) + "\n")

    def partenza(self) -> None:
        if self.partito:
            return
        self.partito = True
        self.scrivi(
            {
                "evento": "partenza",
                "id": self.id,
                "repo": self.repo,
                "host": socket.gethostname(),
                "ts": iso(self.inizio),
                "head": git_testo("rev-parse", "HEAD"),
                "branch": git_testo("symbolic-ref", "--short", "-q", "HEAD") or "(detached)",
            }
        )

    def chiusura(self, esito: str, motivo: str | None, codice: int) -> None:
        self.partenza()
        dopo = git_testo("rev-parse", "HEAD")
        propri = commit_del_giro(self.etichetta) if self.head_prima else []
        commit = bool(propri)
        altri = (
            [
                sha
                for sha in git_testo("rev-list", f"{self.head_prima}..{dopo}").splitlines()
                if sha not in propri
            ]
            if self.head_prima and dopo
            else []
        )
        osservazione = osserva(self.stream)
        fine = osservazione["result"]
        costi = [t["observation"]["result"].get("total_cost_usd") for t in self.tentativi_engine]
        # I costi noti in USD; un motore senza (Codex conta token) lo dichiara
        # `budget_usd_imposto: false`, e se nessuno è noto il costo resta ignoto.
        noti = [c for c in costi if isinstance(c, (int, float))]
        costo = sum(noti) if noti else fine.get("total_cost_usd")
        nota = attenzione(str(fine.get("result") or ""))
        if self.avviso:
            nota = "; ".join(parte for parte in (self.avviso, nota) if parte)
        riga = {
            "evento": "chiusura",
            "id": self.id,
            "repo": self.repo,
            "ts": iso(ora()),
            "esito": esito,
            "motivo": motivo,
            "stato_finale_verificato": codice != 25,
            "service_result": "success" if codice == 0 else "exit-code",
            "exit_code": "exited",
            "exit_status": str(codice),
            "head_prima": self.head_prima,
            "head_dopo": dopo,
            "commit": commit,
            "commit_giro": propri,
            "oggetto": git_testo("log", "-1", "--format=%s", propri[-1]) if commit else None,
            # Senza commit non c'è push da giudicare: `false` direbbe push fallito.
            "push": (
                git("merge-base", "--is-ancestor", propri[-1], "@{u}").returncode == 0
                if commit
                else None
            ),
            # Commit entrati fra head_prima e head_dopo che il giro non ha fatto.
            "commit_altri": len(altri),
            "tree_sporco_dopo": bool(git_testo("status", "--porcelain")),
            "claude_exit": self.claude_exit,
            "engine": self.engine,
            "engine_attempts": self.tentativi_engine,
            "budget_usd_imposto": self.budget_usd_imposto,
            "provider_observation": osservazione,
            "giro": str(self.stream.resolve()) if self.stream.exists() else None,
            "is_error": fine.get("is_error"),
            "permission_denials": len(fine.get("permission_denials") or []),
            "dinieghi": dinieghi(fine),
            "costo_usd": costo,
            "turni": fine.get("num_turns"),
            "durata_ms": fine.get("duration_ms")
            or int((ora() - self.inizio) / timedelta(milliseconds=1)),
        }
        if fine or self.avviso:
            riga["attenzione"] = nota
        if self.sessioni:
            riga["sessioni_concorrenti"] = self.sessioni
        self.scrivi(riga)
        (GIRI / "ultimo.json").write_text(json.dumps(riga, ensure_ascii=False), encoding="utf-8")


def esito_di(codice: int) -> str:
    if codice == 22:
        return "timeout"
    return "errore" if codice in {20, 21, 25, USCITA_PERCORSI_PROTETTI} else "arresto"


def _alza_interrotto(_numero: int, _frame: object) -> None:
    raise Interrotto


def comando_engine(engine: str, eseguibile: str, settings: Path, budget: float) -> list[str]:
    if engine == "codex":
        # L'esecutore canonico traduce permessi e hook e normalizza gli eventi.
        return [
            sys.executable,
            str(ESECUTORE_CODEX),
            "--codex",
            eseguibile,
            "--prompt",
            str(PROMPT.resolve()),
            "--settings",
            str(settings),
        ]
    return [
        eseguibile,
        "-p",
        PROMPT.read_text(encoding="utf-8"),
        "--settings",
        str(settings),
        "--setting-sources",
        "project",
        "--permission-mode",
        "dontAsk",
        "--no-session-persistence",
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-budget-usd",
        str(budget),
    ]


def esegui_engine(
    tentativo: Tentativo,
    profilo: Profilo,
    eseguibili: dict[str, str],
    recinto: list[str],
    ferma: list[str],
    checkout: Path,
    inizio: float,
) -> None:
    """I motori nell'ordine del profilo del repo: il secondo solo se il primo era indisponibile."""
    settings = impostazioni(STATO / "settings.json", tentativo.etichetta).resolve()
    scadenza = time.monotonic() + profilo.minuti * 60
    budget = profilo.budget_usd
    for posizione, engine in enumerate(profilo.motori):
        minuti = (scadenza - time.monotonic()) / 60
        impone = MOTORI[engine]
        if minuti <= 0 or (impone and budget <= 0):
            raise Arresto(22, "fallback-budget-esaurito")
        tentativo.engine = engine
        record = {
            "engine": engine,
            "exit": None,
            "giro": str(tentativo.stream.resolve()),
            "budget_usd_imposto": impone,
        }
        if not impone:
            tentativo.budget_usd_imposto = False
        tentativo.tentativi_engine.append(record)
        eseguibile = eseguibili.get(engine) or engine
        try:
            if shutil.which(eseguibile) is None:
                record["exit"] = 127
                # Launcher evidence, not a fabricated provider quota/API error.
                tentativo.stream.parent.mkdir(parents=True, exist_ok=True)
                tentativo.stream.write_text(
                    json.dumps(
                        {
                            "type": "result",
                            "is_error": True,
                            "total_cost_usd": 0,
                            "terminal_reason": "executable_missing",
                        }
                    )
                    + "\n",
                    encoding="utf-8",
                )
            else:
                record["exit"] = lancia_agente(
                    [*recinto, *comando_engine(engine, eseguibile, settings, budget)],
                    tentativo.stream,
                    replace(profilo, minuti=minuti, budget_usd=budget),
                    ferma,
                    tentativo.etichetta,
                )
        finally:
            record["observation"] = osserva(tentativo.stream)
            if engine == "claude":
                tentativo.claude_exit = record["exit"]
        controlla_concorrenti(tentativo, checkout, inizio)
        evidenza = record["observation"]
        fine = evidenza["result"]
        if record["exit"] == 0 and fine.get("is_error") is False:
            return
        indisponibile = (
            evidenza["unavailable"] or fine.get("terminal_reason") == "executable_missing"
        )
        if posizione + 1 < len(profilo.motori) and indisponibile:
            sicuro = (
                not evidenza["tools_started"]
                and not evidenza["trace_incomplete"]
                and git_testo("rev-parse", "HEAD") == tentativo.head_prima
                and not git_testo("status", "--porcelain")
            )
            if not sicuro:
                tentativo.avvisa("fallback blocked: partial acts or incomplete evidence")
            else:
                costo = fine.get("total_cost_usd")
                if isinstance(costo, (int, float)) and costo >= 0:
                    budget -= costo
                else:
                    # Non blocca (custode, 2026-11-11): lo si dichiara.
                    tentativo.avvisa(f"{engine}: costo ignoto, non scalato dal tetto")
                continue
        if record["exit"] != 0:
            raise Arresto(20, f"{engine}-uscita-non-zero", str(record["exit"]))
        raise Arresto(21, f"{engine}-errore")


def giro(
    profilo: Profilo,
    eseguibili: dict[str, str],
    recinto: list[str],
    checkout: Path,
    pull_canone: bool,
    ferma: list[str] = (),
) -> int:
    tentativo = Tentativo(checkout.name)
    tentativo.head_prima = git_testo("rev-parse", "HEAD")
    signal.signal(signal.SIGTERM, _alza_interrotto)
    fermo = STATO / "fermo"
    lanciato = False
    try:
        lock = Lock(STATO / "lock")
        if fermo.exists():
            raise Arresto(
                24, "fermo-dopo-percorsi-protetti", fermo.read_text(encoding="utf-8").strip()
            )
        locale = esegui_prima(profilo)
        if locale.salta:
            return 0
        fine_aggancio = time.monotonic()
        profilo = locale.profilo
        tentativo.partenza()
        tentativo.avvisa(locale.attenzione)
        controlla_tree(profilo)
        controlla_file()
        tentativo.head_prima = prepara_repo(profilo)
        if pull_canone:
            tentativo.avvisa(aggiorna_canone(checkout))
        profilo = tetto_residuo(locale, time.monotonic() - fine_aggancio)
        hook = cartella_hook()
        if hook:
            profilo = replace(profilo, protetti=(*profilo.protetti, f"{hook}/*"))
        INIZIO.touch()
        inizio = INIZIO.stat().st_mtime
        lanciato = True
        esegui_engine(tentativo, profilo, eseguibili, recinto, ferma, checkout, inizio)
        protetto = rete(tentativo, profilo, fermo)
        if protetto:
            raise protetto
    except Arresto as arresto:
        if arresto.codice == 25:
            fermo.write_text(arresto.motivo + "\n", encoding="utf-8")
            tentativo.avvisa(
                "Sandbox termination unverified; repository state is not final. Custodian must reconcile before removing fermo."
            )
        if lanciato and arresto.codice not in (25, USCITA_PERCORSI_PROTETTI):
            arresto = rete(tentativo, profilo, fermo, arresto.motivo) or arresto
        print(f"lanciatore: {arresto.motivo} {arresto.dettaglio}".rstrip(), file=sys.stderr)
        tentativo.chiusura(esito_di(arresto.codice), arresto.motivo, arresto.codice)
        return arresto.codice
    except Interrotto:
        protetto = rete(tentativo, profilo, fermo, "interrotto") if lanciato else None
        if protetto:
            tentativo.chiusura("errore", protetto.motivo, protetto.codice)
            return protetto.codice
        tentativo.chiusura("errore", "interrotto", 143)
        return 143
    except Exception as errore:  # la chiusura si scrive comunque
        tentativo.chiusura("errore", f"lanciatore: {errore!r}"[:300], 1)
        raise
    finally:
        INIZIO.unlink(missing_ok=True)
        pota(GIRI / "giri")
    tentativo.chiusura("riuscito", None, 0)
    del lock  # tenuto fino a qui: il file aperto è il lock
    return 0


def controlli(profilo: Profilo, checkout: Path) -> int:
    """I controlli in sola lettura, tutti: è una diagnosi, non si ferma al primo.

    Il codice di uscita è quello del primo arresto, come nel giro.
    """
    arresti: list[Arresto] = []

    def prova(controllo: Callable[..., Any], *argomenti: object) -> Any:
        try:
            return controllo(*argomenti)
        except Arresto as arresto:
            arresti.append(arresto)
            return None

    def fermo() -> None:
        if (STATO / "fermo").exists():
            raise Arresto(24, "fermo-dopo-percorsi-protetti")

    prova(fermo)
    locale = prova(esegui_prima, profilo, "controlli")
    avvisi = [locale.attenzione if locale else None]
    prova(controlla_tree, profilo)
    prova(controlla_file)
    for arresto in arresti:
        print(f"arresto {arresto.codice}: {arresto.motivo} {arresto.dettaglio}".rstrip())
    for avviso in filter(None, avvisi):
        print(f"attenzione: {avviso}")
    if arresti:
        return arresti[0].codice
    print(
        "controlli: l'aggancio salterebbe il giro"
        if locale.salta
        else "controlli: il giro potrebbe partire"
    )
    return 0


def segnala(testo: str) -> None:
    """Un arresto prima delle tracce: con `pythonw` lo stderr non esiste."""
    print(f"lanciatore: {testo}", file=sys.stderr)
    try:
        STATO.mkdir(parents=True, exist_ok=True)
        with (STATO / "arresti.log").open("a", encoding="utf-8") as file:
            file.write(f"{iso(ora())} {testo}\n")
    except OSError:
        pass


def main(argv: list[str] | None = None) -> int:
    for flusso in (sys.stdout, sys.stderr):
        if flusso is not None and hasattr(flusso, "reconfigure"):
            flusso.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Lanciatore canonico del ciclo autonomo")
    parser.add_argument(
        "--controlli", action="store_true", help="solo i controlli, in sola lettura"
    )
    parser.add_argument("--branch", help="expected repository profile branch (assertion)")
    parser.add_argument("--max-minuti", type=float, help="host duration cap; can only restrict")
    parser.add_argument("--max-budget-usd", type=float, help="host USD cap; can only restrict")
    parser.add_argument("--claude", default=None, help="eseguibile di Claude, se non è nel PATH")
    parser.add_argument("--codex", default=None, help="eseguibile di Codex, se non è nel PATH")
    parser.add_argument("--recinto", default="", help="sandbox dell'host, messa davanti all'agente")
    parser.add_argument(
        "--recinto-ferma",
        default="",
        help="comando dell'host che ferma la sandbox e ne attende la fine",
    )
    parser.add_argument(
        "--senza-pull-canone", action="store_true", help="non aggiornare il checkout del canone"
    )
    parser.add_argument("--hook-commit", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.hook_commit:
        return hook_commit(sys.stdin.read())
    os.environ.setdefault("GIT_TERMINAL_PROMPT", "0")
    radice = git_testo("rev-parse", "--show-toplevel")
    if not radice:
        print("lanciatore: non è un repository git", file=sys.stderr)
        return 14
    checkout = Path(radice).resolve()
    os.chdir(checkout)
    # Senza `i1/giri` ignorata scrivere la traccia sporcherebbe il tree.
    if not giri_ignorata():
        segnala(f"giri-non-ignorati {GIRI}")
        return 14
    try:
        profilo = limiti_host(
            leggi_profilo(PROFILO), args.branch, args.max_minuti, args.max_budget_usd
        )
    except Arresto as arresto:
        segnala(f"{arresto.motivo} {arresto.dettaglio}")
        return arresto.codice
    if args.controlli:
        return controlli(profilo, checkout)
    eseguibili = {"claude": args.claude or "claude", "codex": args.codex or "codex"}
    # Un motore assente è un fallback verso l'altro; nessuno dei due è un errore di forma.
    if not any(shutil.which(eseguibili[motore]) for motore in profilo.motori):
        segnala(f"agente non trovato: {', '.join(profilo.motori)}")
        return 14
    return giro(
        profilo,
        eseguibili,
        shlex.split(args.recinto),
        checkout,
        not args.senza_pull_canone,
        shlex.split(args.recinto_ferma),
    )


if __name__ == "__main__":
    raise SystemExit(main())
