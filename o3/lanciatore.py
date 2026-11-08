"""Lanciatore canonico del ciclo autonomo: uguale per ogni repo, per ogni sistema.

Fa solo ciò che l'agente non può fare da sé: lock, controllo delle sessioni
aperte, `pull --ff-only`, avvio di `claude -p` coi permessi del repo, tetto di
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

L'aggancio `prima` è uno script Python in `o3/ciclo/`, dove il giro non scrive.
Esce con 0 per proseguire o con un codice da 16 a 19 per fermare il giro, con
il motivo sulla prima riga dell'uscita. Con 0 può stampare un oggetto JSON:
`minuti` accorcia il tetto, senza poterlo alzare, `attenzione` aggiunge un
avviso alla chiusura, `salta: true` esce senza lasciare tracce.

All'avvio il lanciatore aggiorna con `pull --ff-only` anche il proprio checkout
del canone, se è un altro repo e pulito: vale dal giro successivo, e se non
riesce è un avviso. L'host che non vuole lo spegne con `--senza-pull-canone`.

Il recinto sta nei permessi dell'harness. La rete è in chiusura: se i commit del
giro toccano un percorso protetto la chiusura è rossa e i giri successivi si
fermano finché una persona non toglie `.git/lanciatore/fermo`. Un host con una
sandbox la passa con `--recinto "comando con argomenti"`, che precede l'agente:
il lanciatore resta fuori, dove può leggere i processi e fare il pull. L'opzione è
dell'host, mai del repo, che non può allargarsi il recinto da solo.

Codici di uscita, gli stessi dell'unità di `nixos`: 0 riuscito, 10 tree sporco,
11 branch inatteso o senza upstream, 12 divergente, 13 fetch o pull falliti,
14 prompt, permessi, profilo, aggancio o `i1/giri` non adatti, 15 sessione aperta,
16-19 riservati all'aggancio `prima`, 20 agente
uscito con errore, 21 errore riportato dall'agente, 22 tetto di tempo, 23 percorso
protetto toccato dal giro, 24 giri fermi dopo un 23, 75 lock.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
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
from dataclasses import dataclass, field, replace
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

PROMPT = Path("o3/ciclo/prompt.md")
PERMESSI = Path("o3/ciclo/permessi.json")
PROFILO = Path("o3/ciclo/lanciatore.toml")
GIRI = Path("i1/giri")
STATO = Path(".git/lanciatore")
STREAM_TENUTI = 60
CODEX_MINUTI = 60
GIT_SECONDI = 120
GRAZIA_SECONDI = 15
PRIMA_SECONDI = 20 * 60  # un aggancio può aspettare, per esempio la fine di un run
CODICI_PRIMA = range(16, 20)
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
ATTENZIONE = re.compile(r"^\s*\**Attenzione:?\**:?\s*(.*)$", re.IGNORECASE)
WINDOWS = os.name == "nt"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
USCITA_PERCORSI_PROTETTI = 23


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


def leggi_profilo(path: Path) -> Profilo:
    if not path.exists():
        return Profilo()
    try:
        dati = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as errore:
        raise Arresto(14, "profilo-invalido", str(errore)) from errore
    ignote = dati.keys() - {"branch", "minuti", "budget_usd", "protetti", "prima"}
    if ignote:
        raise Arresto(14, "profilo-invalido", f"chiavi sconosciute {sorted(ignote)}")
    return Profilo(
        dati.get("branch", "main"),
        dati.get("minuti", 45),
        dati.get("budget_usd", 5),
        (*PROTETTI, *dati.get("protetti", [])),
        dati.get("prima"),
    )


@dataclass(frozen=True)
class EsitoPrima:
    profilo: Profilo
    attenzione: str | None = None
    salta: bool = False


def esegui_prima(profilo: Profilo) -> EsitoPrima:
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


def sessioni_posix(checkout: Path, proc: Path = Path("/proc")) -> tuple[Arresto | None, int]:
    """Un processo Claude nel checkout; quanti processi Claude non si sono letti.

    Dentro un namespace `/proc/<pid>/cwd` degli altri processi è negato: chi
    non si legge non si conta come assente, si dichiara.
    """
    illeggibili = 0
    for voce in proc.iterdir():
        if not voce.name.isdigit():
            continue
        try:
            nome = (voce / "comm").read_text(encoding="utf-8", errors="replace").strip()
        except OSError:
            continue
        if "claude" not in nome:
            continue
        try:
            cwd = os.readlink(voce / "cwd")
        except PermissionError:
            illeggibili += 1
            continue
        except OSError:
            continue
        if _dentro(cwd, checkout):
            return Arresto(15, "sessione-claude-attiva", f"pid {voce.name}, {cwd}"), illeggibili
    return None, illeggibili


def sessioni_windows() -> tuple[Arresto | None, str | None]:
    """Su Windows la cwd degli altri processi non si legge: vale l'intero host.

    Un `tasklist` che fallisce non vuol dire «nessuna sessione»: si dichiara.
    """
    non_verificabile = "sessioni non verificabili: tasklist fallito"
    try:
        esito = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq claude.exe", "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            errors="replace",
            timeout=GIT_SECONDI,
            creationflags=NO_WINDOW,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None, non_verificabile
    if esito.returncode != 0:
        return None, non_verificabile
    if "claude.exe" in esito.stdout.lower():
        return Arresto(15, "sessione-claude-attiva", "claude.exe vivo sull'host"), None
    return None, None


def sessioni_codex(checkout: Path, cartella: Path, minuti: int = CODEX_MINUTI) -> Arresto | None:
    """Le sessioni Codex sono thread di un demone: si leggono dai rollout recenti."""
    if not cartella.is_dir():
        return None
    soglia = time.time() - minuti * 60
    for rollout in cartella.rglob("rollout-*.jsonl"):
        try:
            if rollout.stat().st_mtime < soglia:
                continue
            with rollout.open(encoding="utf-8") as file:
                testa = json.loads(file.readline())
        except (OSError, ValueError):
            continue
        cwd = (
            (testa.get("payload") or {}).get("cwd") if testa.get("type") == "session_meta" else None
        )
        if cwd and _dentro(cwd, checkout):
            return Arresto(15, "sessione-codex-attiva", f"{rollout}, {cwd}")
    return None


def controlla_sessioni(checkout: Path) -> str | None:
    """Ferma il giro se qualcuno lavora nel checkout; ritorna un eventuale avviso."""
    avviso = None
    if WINDOWS:
        trovata, avviso = sessioni_windows()
    elif Path("/proc/self").exists():
        trovata, illeggibili = sessioni_posix(checkout)
        if illeggibili:
            avviso = f"sessioni non verificabili: {illeggibili} processi Claude illeggibili"
    else:
        trovata, avviso = None, "sessioni non verificabili su questo sistema"
    if trovata:
        raise trovata
    casa = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    trovata = sessioni_codex(checkout, casa / "sessions")
    if trovata:
        raise trovata
    return avviso


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


def prepara_repo() -> str:
    """Fetch e `pull --ff-only`: ritorna l'HEAD da cui parte il giro."""
    if git("fetch", "--quiet", "origin").returncode != 0:
        raise Arresto(13, "fetch-fallito")
    if git("rev-parse", "-q", "--verify", "@{u}").returncode != 0:
        raise Arresto(11, "upstream-mancante")
    avanti, dietro = git_testo("rev-list", "--left-right", "--count", "HEAD...@{u}").split()
    if int(avanti) and int(dietro):
        raise Arresto(12, "branch-divergente", f"{avanti} avanti, {dietro} dietro")
    if int(dietro) and git("pull", "--ff-only", "--quiet").returncode != 0:
        raise Arresto(13, "pull-fallito")
    return git_testo("rev-parse", "HEAD")


def aggiorna_canone(checkout: Path) -> str | None:
    """Tiene fresco il checkout del canone, se è un altro repo: ritorna un avviso."""
    canone = Path(__file__).resolve().parents[1]
    if canone == checkout or not (canone / ".git").exists():
        return None
    try:
        if git_testo("-C", str(canone), "status", "--porcelain"):
            return "canone non aggiornato: checkout sporco"
        if git("-C", str(canone), "pull", "--ff-only", "--quiet").returncode != 0:
            return "canone non aggiornato: pull fallito"
    except (OSError, subprocess.SubprocessError):
        return "canone non aggiornato: git non ha risposto"
    return None


class Lock:
    """Lock del sistema operativo: muore col processo, niente file orfani da pulire."""

    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open("a+")
        try:
            if WINDOWS:
                import msvcrt

                self.file.seek(0)
                msvcrt.locking(self.file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl

                fcntl.flock(self.file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as errore:
            self.file.close()
            raise Arresto(75, "lock") from errore


def impostazioni(destinazione: Path) -> Path:
    """I permessi del repo, senza trailer di attribuzione nei commit del giro."""
    dati = json.loads(PERMESSI.read_text(encoding="utf-8"))
    dati["attribution"] = {"commit": "", "pr": ""}
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(json.dumps(dati, indent=2), encoding="utf-8")
    return destinazione


def termina(processo: subprocess.Popen[bytes]) -> None:
    """Chiude l'agente con tutti i suoi figli."""
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


def lancia_agente(comando: list[str], stream: Path, profilo: Profilo) -> int:
    """L'agente col suo tetto di tempo; alla fine l'albero dei processi non resta."""
    stream.parent.mkdir(parents=True, exist_ok=True)
    with stream.open("wb") as uscita:
        processo = subprocess.Popen(
            comando,
            stdin=subprocess.DEVNULL,
            stdout=uscita,
            stderr=subprocess.STDOUT,  # un'uscita con errore si spiega dallo stream
            start_new_session=not WINDOWS,
            creationflags=NO_WINDOW,
        )
        try:
            return processo.wait(timeout=profilo.minuti * 60)
        except subprocess.TimeoutExpired as errore:
            termina(processo)
            raise Arresto(22, "tetto-di-tempo", f"{profilo.minuti} minuti") from errore
        except Interrotto:
            termina(processo)
            raise


def risultato(stream: Path) -> dict:
    """L'evento finale `result`, assente se il giro è stato interrotto."""
    ultimo: dict = {}
    try:
        righe = stream.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ultimo
    for riga in righe:
        try:
            evento = json.loads(riga)
        except ValueError:
            continue
        if isinstance(evento, dict) and evento.get("type") == "result":
            ultimo = evento
    return ultimo


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

    def avvisa(self, testo: str | None) -> None:
        if testo:
            self.avviso = f"{self.avviso}; {testo}" if self.avviso else testo

    @property
    def stream(self) -> Path:
        return GIRI / "giri" / f"{self.id}.jsonl"

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
        commit = bool(self.head_prima and dopo and self.head_prima != dopo)
        fine = risultato(self.stream)
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
            "service_result": "success" if codice == 0 else "exit-code",
            "exit_code": "exited",
            "exit_status": str(codice),
            "head_prima": self.head_prima,
            "head_dopo": dopo,
            "commit": commit,
            "oggetto": git_testo("log", "-1", "--format=%s") if commit else None,
            "push": bool(dopo) and dopo == git_testo("rev-parse", "@{u}"),
            "tree_sporco_dopo": bool(git_testo("status", "--porcelain")),
            "claude_exit": self.claude_exit,
            "giro": str(self.stream.resolve()) if self.stream.exists() else None,
            "is_error": fine.get("is_error"),
            "permission_denials": len(fine.get("permission_denials") or []),
            "dinieghi": dinieghi(fine),
            "costo_usd": fine.get("total_cost_usd"),
            "turni": fine.get("num_turns"),
            "durata_ms": fine.get("duration_ms")
            or int((ora() - self.inizio) / timedelta(milliseconds=1)),
        }
        if fine or self.avviso:
            riga["attenzione"] = nota
        self.scrivi(riga)
        (GIRI / "ultimo.json").write_text(json.dumps(riga, ensure_ascii=False), encoding="utf-8")


def esito_di(codice: int) -> str:
    if codice == 22:
        return "timeout"
    return "errore" if codice in {20, 21, USCITA_PERCORSI_PROTETTI} else "arresto"


def _alza_interrotto(_numero: int, _frame: object) -> None:
    raise Interrotto


def giro(
    profilo: Profilo, claude: str, recinto: list[str], checkout: Path, pull_canone: bool
) -> int:
    tentativo = Tentativo(checkout.name)
    tentativo.head_prima = git_testo("rev-parse", "HEAD")
    signal.signal(signal.SIGTERM, _alza_interrotto)
    fermo = STATO / "fermo"
    try:
        lock = Lock(STATO / "lock")
        if fermo.exists():
            raise Arresto(
                24, "fermo-dopo-percorsi-protetti", fermo.read_text(encoding="utf-8").strip()
            )
        locale = esegui_prima(profilo)
        if locale.salta:
            return 0
        profilo = locale.profilo
        tentativo.partenza()
        tentativo.avvisa(locale.attenzione)
        tentativo.avvisa(controlla_sessioni(checkout))
        controlla_tree(profilo)
        controlla_file()
        tentativo.head_prima = prepara_repo()
        if pull_canone:
            tentativo.avvisa(aggiorna_canone(checkout))
        comando = [
            *recinto,
            claude,
            "-p",
            PROMPT.read_text(encoding="utf-8"),
            "--settings",
            str(impostazioni(STATO / "settings.json").resolve()),
            "--setting-sources",
            "project",
            "--permission-mode",
            "dontAsk",
            "--no-session-persistence",
            "--output-format",
            "stream-json",
            "--verbose",
            "--max-budget-usd",
            str(profilo.budget_usd),
        ]
        tentativo.claude_exit = lancia_agente(comando, tentativo.stream, profilo)
        if tentativo.claude_exit != 0:
            raise Arresto(20, "claude-uscita-non-zero", str(tentativo.claude_exit))
        fine = risultato(tentativo.stream)
        if not fine or fine.get("is_error") is not False:
            raise Arresto(21, "claude-errore")
        toccati = percorsi_protetti(
            tentativo.head_prima, git_testo("rev-parse", "HEAD"), profilo.protetti
        )
        if toccati:
            fermo.write_text(
                f"il giro {tentativo.id} ha toccato {', '.join(toccati)}: rivedi e togli questo file\n",
                encoding="utf-8",
            )
            raise Arresto(USCITA_PERCORSI_PROTETTI, f"percorsi-protetti: {', '.join(toccati)}")
    except Arresto as arresto:
        print(f"lanciatore: {arresto.motivo} {arresto.dettaglio}".rstrip(), file=sys.stderr)
        tentativo.chiusura(esito_di(arresto.codice), arresto.motivo, arresto.codice)
        return arresto.codice
    except Interrotto:
        tentativo.chiusura("errore", "interrotto", 143)
        return 143
    except Exception as errore:  # la chiusura si scrive comunque
        tentativo.chiusura("errore", f"lanciatore: {errore!r}"[:300], 1)
        raise
    finally:
        pota(GIRI / "giri")
    tentativo.chiusura("riuscito", None, 0)
    del lock  # tenuto fino a qui: il file aperto è il lock
    return 0


def controlli(profilo: Profilo, checkout: Path) -> int:
    """I controlli in sola lettura: dicono se il giro partirebbe adesso."""
    try:
        if (STATO / "fermo").exists():
            raise Arresto(24, "fermo-dopo-percorsi-protetti")
        locale = esegui_prima(profilo)
        avvisi = [locale.attenzione, controlla_sessioni(checkout)]
        controlla_tree(profilo)
        controlla_file()
    except Arresto as arresto:
        print(f"arresto {arresto.codice}: {arresto.motivo} {arresto.dettaglio}".rstrip())
        return arresto.codice
    for avviso in filter(None, avvisi):
        print(f"attenzione: {avviso}")
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
    parser.add_argument("--claude", default=None, help="eseguibile dell'agente, se non è nel PATH")
    parser.add_argument("--recinto", default="", help="sandbox dell'host, messa davanti all'agente")
    parser.add_argument(
        "--senza-pull-canone", action="store_true", help="non aggiornare il checkout del canone"
    )
    args = parser.parse_args(argv)
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
        profilo = leggi_profilo(PROFILO)
    except Arresto as arresto:
        segnala(f"{arresto.motivo} {arresto.dettaglio}")
        return arresto.codice
    if args.controlli:
        return controlli(profilo, checkout)
    claude = args.claude or shutil.which("claude")
    if not claude:
        segnala("agente non trovato nel PATH")
        return 14
    return giro(profilo, claude, shlex.split(args.recinto), checkout, not args.senza_pull_canone)


if __name__ == "__main__":
    raise SystemExit(main())
