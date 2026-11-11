"""Esecutore canonico di Codex per il lanciatore: stesso prompt, stessa politica.

Il lanciatore lo chiama al posto di `claude -p` quando il profilo del repo mette
`codex` fra i `motori` (`o3/ciclo/lanciatore.toml`). Riceve il prompt e le
impostazioni del giro (`permessi.json` con l'hook sul commit e l'`env`),
lancia `codex exec` e traduce gli eventi nel contratto del lanciatore: una
`tool_use` per ogni strumento, `error` per i fallimenti, un `result` finale.
All'host restano recinto, arresto e percorso del binario (`--codex`).

Traduzione della politica, verificata su Codex CLI 0.166.0 il 2026-11-11:

- un solo hook `PreToolUse` inline (`-c hooks.PreToolUse=…`), questo file con
  `--hook`, giudica ogni chiamata contro le regole `allow`/`deny` di Claude:
  `Bash(…)` per i comandi, `Edit(…)`/`Write(…)` per i file di `apply_patch`
  e per le scritture dei comandi (redirezioni in uscita, `tee`, `--output`),
  `Read(…)` negato per ogni parola che può essere un path, con o senza barre,
  quotata, attraverso symlink, glob e `cd` (correzione del 2026-11-12 dopo le
  riproduzioni di nixos `5aa20f9`, BI `39d63da` e Baserow) e, per i comandi
  di lettura (`cat`, `head`, `ls`…), `Read(…)` ammesso per i path fuori dal
  checkout, perché Codex non ha un tool Read. La riga si divide come la
  legge la shell; variabili, sostituzioni e graffe cadono. Le regole `Bash`
  si confrontano coi valori, con la riga com'è scritta e con la quotatura
  canonica, così le regole esatte con virgolette reggono; poi gli hook `Bash` delle
  impostazioni, cioè quello del lanciatore sul commit. Il rifiuto è il JSON
  `permissionDecision: deny`; `--dangerously-bypass-hook-trust` è necessario
  perché l'hook è inline, e la fonte è questo file del canone;
- senza recinto dell'host, sandbox `workspace-write` con rete e con la
  cartella git scrivibile, senza la quale il commit fallisce (`index.lock` in
  sola lettura); col recinto dell'host (`--recinto-host`, che passa il
  lanciatore quando l'host dà `--recinto`) Codex non aggiunge il proprio e
  vale quello dell'host, come per Claude: la sandbox di Codex chiudeva la home
  scrivibile del recinto, e con lei cache e demone di Nix e il bus utente
  (giro di nixos dell'11/11/2026, decisione del custode); approvazioni `never`;
- `--ignore-user-config` e `--ignore-rules`: niente server MCP, profili o regole
  dell'utente; `--ephemeral`: nessun rollout, così il giro non vede sé stesso
  come sessione concorrente.

Non c'è un tetto in USD: Codex conta token. La chiusura lo dichiara
(`budget_usd_imposto: false`, decisione del custode del 2026-11-11). Gli errori
di quota di Codex non sono documentati: li riconosce dal testo (`usage limit`,
`rate limit`, `429`), e un caso nuovo va aggiunto quando lo si osserva.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import posixpath
import re
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

WINDOWS = os.name == "nt"
PATCH = re.compile(r"^\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)$", re.MULTILINE)
REGOLA = re.compile(r"^([A-Za-z_][\w-]*)(?:\((.*)\))?$", re.DOTALL)
QUOTA = re.compile(r"usage limit|rate.?limit|quota|too many requests|\b429\b", re.IGNORECASE)
AUTENTICAZIONE = re.compile(
    r"unauthori[sz]ed|not logged in|authentication|login required|\b401\b|\b403\b", re.IGNORECASE
)
# Codex non ha un tool Read: legge con questi comandi. Fuori dal checkout un loro
# path deve essere ammesso da un `Read(…)` del giro, lo stesso perimetro del tool
# Read di Claude (giro di method dell'11/11/2026, che non poteva leggere fetch.json).
LETTORI = {"cat", "head", "tail", "ls", "wc", "grep", "rg", "jq", "diff", "sort", "uniq", "cut"}
LETTORI |= {"readlink", "sed", "stat", "file", "egrep", "fgrep", "less", "more", "nl", "tac"}
LETTORI |= {"od", "xxd", "strings", "base64", "md5sum", "sha256sum", "awk"}
# PowerShell e cmd su Windows (nomi confrontati in minuscolo).
LETTORI |= {"get-content", "gc", "type", "select-string", "sls", "get-childitem", "gci", "dir"}
# Lettori che senza path leggono la cartella corrente invece dello stdin.
SU_CARTELLA = {"ls", "rg", "get-childitem", "gci", "dir"}
# Il primo argomento non è un file ma un pattern o uno script, salvo che lo dia
# un'opzione: non lo si giudica come path (nixos, 5aa20f9: non trattare i
# pattern come file).
PATTERN_PRIMO = {
    "grep": {"-e", "-f", "--regexp", "--file"},
    "egrep": {"-e", "-f", "--regexp", "--file"},
    "fgrep": {"-e", "-f", "--regexp", "--file"},
    "rg": {"-e", "-f", "--regexp", "--file"},
    "sed": {"-e", "-f", "--expression", "--file"},
    "awk": {"-f", "--file"},
    "jq": {"-f", "--from-file"},
    "select-string": {"-pattern"},
    "sls": {"-pattern"},
}
# Opzioni corte che prendono un valore; quelle in FILE_OPZIONE il valore è un file.
CON_VALORE = {
    "head": "nc",
    "tail": "nc",
    "grep": "efABCmdD",
    "egrep": "efABCmdD",
    "fgrep": "efABCmdD",
    "rg": "efgtTABCmMj",
    "sed": "efl",
    "awk": "fvF",
    "jq": "fL",
    "cut": "dfbc",
    "sort": "ktoST",
    "uniq": "fsw",
    "ls": "IwT",
    "stat": "c",
    "file": "mf",
    "nl": "bdfhilnsvw",
    "git": "Cc",
}
FILE_OPZIONE = {"-f", "--file", "--from-file", "--slurpfile", "--rawfile"}
# Opzioni lunghe con due valori (jq): il secondo è un file per slurpfile/rawfile.
DUE_VALORI = {"--arg", "--argjson", "--slurpfile", "--rawfile"}
SCRITTURA_OPZIONE = {"--output", "-o"}  # `-o` scrive solo per `sort`.
RICORSIVE = {"-r", "-R", "--recursive", "--dereference-recursive", "--directories=recurse"}
CAMBIA_CARTELLA = {"cd", "pushd", "chdir", "set-location", "sl"}
SCRITTORI = {"tee", "tee-object", "set-content", "out-file", "add-content"}
CANALI = {"/dev/null", "/dev/stdout", "/dev/stderr", "/dev/tty", "nul"}
# Strumenti locali di Codex senza effetti fuori dalla sessione.
INNOCUI = {"update_plan"}
STRUMENTI_FILE = {"apply_patch", "Edit", "Write"}
DRIVE = re.compile(r"^/?([A-Za-z]):(?:[/\\]|$)")
VARIABILE = re.compile(r"[A-Za-z_0-9{(@*#?$!\-'\"]")
GRAFFE = re.compile(r"\{[^{}]*(?:,|\.\.)[^{}]*\}")
PERCENTO = re.compile(r"%[A-Za-z_][\w()]*%")
MAX_GLOB = 5000


# --- politica: regole -----------------------------------------------------------


def regole(impostazioni: dict, tipo: str) -> list[tuple[str, str | None]]:
    """Le regole `allow` o `deny` come coppie (strumento, argomento)."""
    coppie = []
    for voce in (impostazioni.get("permissions") or {}).get(tipo) or []:
        trovata = REGOLA.match(str(voce).strip())
        if trovata:
            coppie.append((trovata.group(1), trovata.group(2)))
    return coppie


def comando_ammesso(pezzo: str, modello: str) -> bool:
    """Un pezzo di comando contro un modello `Bash(…)` di Claude.

    Come in Claude, l'unico jolly è `*`: `?` e `[` restano lettere (la regola
    Baserow con `count(*)` e le parentesi graffe di `--format`)."""
    if modello.endswith(":*"):
        radice = modello[:-2]
        return pezzo == radice or pezzo.startswith(radice + " ")
    if modello.endswith(" *") and pezzo == modello[:-2]:
        return True
    regex = ".*".join(re.escape(parte) for parte in modello.split("*"))
    return re.fullmatch(regex, pezzo, re.DOTALL) is not None


# --- politica: lessico della shell ----------------------------------------------


class NonScomponibile(ValueError):
    """La riga contiene ciò che la shell espanderebbe a tempo di esecuzione."""


class Parola:
    """Una parola della riga: il valore che riceve il comando (`testo`), come è
    scritta (`grezzo`), se ha un glob fuori dalle virgolette e i caratteri fuori
    dalle virgolette (`libero`, quelle dentro come `Q`)."""

    def __init__(self, testo: str = "", grezzo: str = "", glob: bool = False, libero: str = ""):
        self.testo, self.grezzo, self.glob, self.libero = testo, grezzo, glob, libero


class Pezzo:
    """Un comando semplice: parole e redirezioni (operatore, bersaglio)."""

    def __init__(self) -> None:
        self.parole: list[Parola] = []
        self.redirezioni: list[tuple[str, Parola]] = []

    @property
    def forme(self) -> list[str]:
        """Le forme confrontate con le regole `Bash(…)`: i valori, la riga come è
        scritta e la quotatura canonica. Un diniego basta su una sola, come
        un'ammissione: il comando eseguito è lo stesso in tutte."""
        valori = [p.testo for p in self.parole]
        forme = [" ".join(valori), " ".join(p.grezzo for p in self.parole)]
        if not WINDOWS:
            forme.append(shlex.join(valori))
        return list(dict.fromkeys(forme))

    @property
    def nome(self) -> str:
        if not self.parole:
            return ""
        nome = self.parole[0].testo
        return nome.lower() if WINDOWS else nome


REDIREZIONI = ("<<<", "<<-", "&>>", "<<", "<>", "<&", ">>", ">|", ">&", "&>", "<", ">")


def analizza(comando: str) -> list[Pezzo]:
    """Divide una riga di shell in comandi semplici, come la shell la legge.

    Rifiuta (NonScomponibile) sostituzioni, variabili, graffe e virgolette
    aperte: il loro valore lo conosce solo la shell. Su Windows la barra
    rovescia è un separatore di path, non un escape."""
    posix = not WINDOWS
    pezzi_: list[Pezzo] = []
    pezzo = Pezzo()
    parola: Parola | None = None
    redirezione: str | None = None
    i, n = 0, len(comando)

    def chiudi_parola() -> None:
        nonlocal parola, redirezione
        if parola is None:
            return
        if posix and GRAFFE.search(parola.libero):
            raise NonScomponibile("espansione di graffe")
        if not posix and PERCENTO.search(parola.libero):
            raise NonScomponibile("variabile di cmd")
        if redirezione:
            if redirezione in (">&", "<&") and re.fullmatch(r"\d+-?|-", parola.testo):
                pass  # duplica un descrittore: nessun file
            else:
                pezzo.redirezioni.append((redirezione, parola))
            redirezione = None
        else:
            pezzo.parole.append(parola)
        parola = None

    def chiudi_pezzo() -> None:
        nonlocal pezzo
        chiudi_parola()
        if redirezione:
            raise NonScomponibile("redirezione senza bersaglio")
        if pezzo.parole or pezzo.redirezioni:
            pezzi_.append(pezzo)
        pezzo = Pezzo()

    def variabile(j: int) -> None:
        if j + 1 < n and VARIABILE.match(comando[j + 1]):
            raise NonScomponibile("variabile o sostituzione")

    while i < n:
        c = comando[i]
        if c in " \t\r":
            chiudi_parola()
            i += 1
            continue
        if c == "\n":
            chiudi_pezzo()  # una riga nuova separa; il corpo di un heredoc diventa comandi, e cade
            i += 1
            continue
        if c == "#" and parola is None:
            while i < n and comando[i] != "\n":
                i += 1
            continue
        if c == "`":
            raise NonScomponibile("sostituzione o escape con l'accento grave")
        if c in ";&|()":
            if c == "&" and comando.startswith("&>", i):
                pass  # `&>` è una redirezione, sotto
            else:
                chiudi_pezzo()
                i += 1
                continue
        if c in "<>&":
            if parola is not None and re.fullmatch(r"\d+", parola.grezzo):
                parola = None  # il descrittore davanti a `>`
            chiudi_parola()
            if redirezione:
                raise NonScomponibile("redirezione senza bersaglio")
            operatore = next(op for op in REDIREZIONI if comando.startswith(op, i))
            i += len(operatore)
            if i < n and comando[i] == "(":
                raise NonScomponibile("sostituzione di processo")
            redirezione = operatore
            continue
        if parola is None:
            parola = Parola()
        if c == "\\" and posix:
            if i + 1 < n and comando[i + 1] == "\n":
                i += 2  # continuazione di riga
                continue
            if i + 1 < n:
                parola.testo += comando[i + 1]
                parola.grezzo += comando[i : i + 2]
                parola.libero += "Q"
            i += 2
            continue
        if c == "'":
            fine = comando.find("'", i + 1)
            if fine < 0:
                raise NonScomponibile("virgolette aperte")
            parola.testo += comando[i + 1 : fine]
            parola.grezzo += comando[i : fine + 1]
            parola.libero += "Q"
            i = fine + 1
            continue
        if c == '"':
            j = i + 1
            while True:
                if j >= n:
                    raise NonScomponibile("virgolette aperte")
                d = comando[j]
                if d == '"':
                    break
                if d == "`":
                    raise NonScomponibile("sostituzione o escape con l'accento grave")
                if d == "$":
                    variabile(j)
                if d == "\\" and posix and j + 1 < n and comando[j + 1] in '$`"\\\n':
                    parola.testo += comando[j + 1] if comando[j + 1] != "\n" else ""
                    j += 2
                    continue
                parola.testo += d
                j += 1
            parola.grezzo += comando[i : j + 1]
            parola.libero += "Q"
            i = j + 1
            continue
        if c == "$":
            variabile(i)
        if c in "*?[":
            parola.glob = True
        parola.testo += c
        parola.grezzo += c
        parola.libero += c
        i += 1
    chiudi_pezzo()
    return pezzi_


def pezzi(comando: str) -> list[str] | None:
    """I comandi semplici di una riga di shell; None se non si sa dividerla."""
    try:
        return [
            " ".join(p.testo for p in pezzo.parole) for pezzo in analizza(comando) if pezzo.parole
        ]
    except NonScomponibile:
        return None


# --- politica: path ---------------------------------------------------------------


def forma(percorso: str) -> str:
    """Un path con barre `/` e il disco come `/c/…`, la forma delle regole di
    Claude su Windows (`//c/Users/…`)."""
    percorso = percorso.replace("\\", "/")
    percorso = percorso.removeprefix("//?/")
    trovato = DRIVE.match(percorso)
    if trovato:
        percorso = "/" + trovato.group(1).lower() + "/" + percorso[trovato.end() :]
    return posixpath.normpath(percorso) if percorso else percorso


def _reale(nativo: str) -> str:
    """`realpath`, salvo un path di Windows giudicato su un altro sistema (i test)."""
    if DRIVE.match(nativo.replace("\\", "/")) and os.name != "nt":
        return nativo
    return os.path.realpath(nativo)


def _regex_percorso(modello: str) -> re.Pattern[str]:
    parti = re.split(r"(\*\*/?|\*|\?)", modello)
    tradotte = []
    for parte in parti:
        if parte in ("**", "**/"):
            tradotte.append(".*")
        elif parte == "*":
            tradotte.append("[^/]*")
        elif parte == "?":
            tradotte.append("[^/]")
        else:
            tradotte.append(re.escape(parte))
    return re.compile("".join(tradotte) + "$", re.IGNORECASE if WINDOWS else 0)


def assoluto(modello: str, radice: Path | str) -> str:
    """Un modello di path di Claude come path assoluto con barre `/`."""
    radice = forma(str(radice) if isinstance(radice, str) else radice.as_posix())
    if modello.startswith("//"):
        base = modello[1:]
        disco = r"^/[A-Za-z](?:/|$)"
        if WINDOWS and re.match(disco, radice) and not re.match(disco, base):
            base = radice[:2] + base  # `//stato/…` su Windows: il disco della radice
    elif modello.startswith("~/"):
        base = forma(str(Path.home())) + modello[1:]
    elif modello.startswith("./"):
        base = f"{radice}/{modello[2:]}"
    elif modello.startswith("/"):
        base = f"{radice}{modello}"
    else:
        base = f"{radice}/{modello}"
    return forma(base)


def _nativo(percorso: str, base: Path | str) -> str:
    percorso = os.path.expanduser(percorso)
    if os.path.isabs(percorso) or DRIVE.match(percorso.replace("\\", "/")):
        return percorso
    return os.path.join(str(base), percorso)


def percorso_reale(percorso: str, radice: Path | str) -> str:
    return forma(os.path.normpath(_nativo(percorso, radice)))


def percorsi(percorso: str, radice: Path | str) -> tuple[str, str]:
    """Il path come scritto e dove punta davvero: la shell segue i symlink
    (`method/../o3` esce dal checkout, osservato da economia l'11/11/2026),
    anche verso una destinazione che non esiste (nixos, 5aa20f9)."""
    nativo = _nativo(percorso, radice)
    return forma(os.path.normpath(nativo)), forma(_reale(nativo))


def dentro(percorso: str, cartella: str) -> bool:
    if WINDOWS:
        percorso, cartella = percorso.lower(), cartella.lower()
    cartella = cartella.rstrip("/")
    return percorso == cartella or percorso.startswith(cartella + "/")


def cartelle_aggiuntive(impostazioni: dict, radice: Path) -> list[str]:
    """Le `additionalDirectories` del giro: cartelle di lavoro, lette come il checkout."""
    voci = (impostazioni.get("permissions") or {}).get("additionalDirectories") or []
    return [percorsi(str(v), radice)[1] for v in voci]


def percorso_in(percorso: str, modello: str, radice: Path | str) -> bool:
    return bool(_regex_percorso(assoluto(modello, radice)).match(forma(percorso)))


def sotto(cartella: str, modello: str, radice: Path | str) -> bool:
    """Se qualcosa dentro `cartella` può ricadere nel modello: per chi legge
    ricorsivo (`grep -r`, `rg`), che apre file che la riga non nomina."""
    letterale = re.split(r"[*?\[]", assoluto(modello, radice), maxsplit=1)[0]
    cartella = forma(cartella).rstrip("/") + "/"
    if WINDOWS:
        letterale, cartella = letterale.lower(), cartella.lower()
    return letterale.startswith(cartella) or cartella.startswith(letterale)


def nascosto(cartella: str, modello: str, radice: Path | str) -> bool:
    """Se il modello, sotto la cartella, passa da un nome nascosto (`.env`,
    `.ssh/`): `rg` senza `--hidden` non ci entra."""
    letterale = re.split(r"[*?\[]", assoluto(modello, radice), maxsplit=1)[0]
    cartella = forma(cartella).rstrip("/") + "/"
    if WINDOWS:
        letterale, cartella = letterale.lower(), cartella.lower()
    if not letterale.startswith(cartella):
        return False
    return any(nome.startswith(".") for nome in letterale[len(cartella) :].split("/") if nome)


def giudica_file(
    percorso: str, impostazioni: dict, radice: Path, base: Path | None = None
) -> str | None:
    """Il motivo del rifiuto di una scrittura, o None se ammessa.

    Negata se lo nega il path scritto o quello vero; ammessa solo se il path
    vero è ammesso, perché è lì che la scrittura arriva. `base` è la cartella
    da cui si risolve un path relativo, se non è la radice."""
    scritto, vero = percorsi(percorso, base or radice)
    radice_vera = _reale(str(radice))
    for strumento, argomento in regole(impostazioni, "deny"):
        if strumento in ("Edit", "Write") and argomento:
            if percorso_in(scritto, argomento, radice) or percorso_in(vero, argomento, radice_vera):
                return f"scrittura negata da {strumento}({argomento}): {percorso}"
    for strumento, argomento in regole(impostazioni, "allow"):
        if strumento in ("Edit", "Write") and argomento:
            if percorso_in(vero, argomento, radice_vera) or (
                vero == scritto and percorso_in(scritto, argomento, radice)
            ):
                return None
    return f"scrittura non ammessa dai permessi del giro: {percorso}"


# --- politica: comandi ------------------------------------------------------------


class Argomenti:
    """Gli argomenti di un comando per ruolo: `file` letti (dinieghi e
    perimetro), `valori` di opzioni (solo dinieghi), `scritture`."""

    def __init__(self, ricorsivo: bool = False) -> None:
        self.file: list[Parola] = []
        self.valori: list[Parola] = []
        self.scritture: list[Parola] = []
        self.ricorsivo = ricorsivo
        self.salta_nascosti = False  # `rg` senza `--hidden`/`-uu`/`-.`


def _parola(testo: str, origine: Parola) -> Parola:
    return Parola(testo=testo, grezzo=testo, glob=origine.glob, libero=testo)


def _gruppo_ricorsivo(testo: str, corte: str) -> bool:
    """`-rn`, `-Rl`: una `r`/`R` prima di una lettera che prende un valore."""
    if testo.startswith("--") or not testo.startswith("-"):
        return False
    for lettera in testo[1:]:
        if lettera in "rR":
            return True
        if lettera in corte:
            return False
    return False


def argomenti(pezzo: Pezzo) -> Argomenti:
    """Separa file, valori di opzioni e scritture. Nel dubbio una parola è un
    file: si giudica di più, non di meno."""
    nome = pezzo.nome
    esito = Argomenti(ricorsivo=nome == "rg")
    corte = CON_VALORE.get(nome, "")
    pattern_da_opzione = False
    posizionali: list[Parola] = []
    resto = pezzo.parole[1:]
    finite = False
    k = 0
    while k < len(resto):
        parola = resto[k]
        testo = parola.testo
        k += 1
        if finite or not testo.startswith("-") or testo == "-":
            if testo != "-":
                posizionali.append(parola)
            continue
        if testo == "--":
            finite = True
            continue
        if testo in RICORSIVE or (
            nome in ("grep", "egrep", "fgrep", "diff") and _gruppo_ricorsivo(testo, corte)
        ):
            esito.ricorsivo = True
        if testo.startswith("--"):
            opzione, uguale, valore = testo.partition("=")
            opzione_cf = opzione.lower() if WINDOWS else opzione
            if opzione_cf in PATTERN_PRIMO.get(nome, ()):
                pattern_da_opzione = True
            if opzione_cf in DUE_VALORI:
                coppia = resto[k : k + 2]
                k += 2
                esito.valori.extend(coppia[:1])
                destinazione = esito.file if opzione_cf in FILE_OPZIONE else esito.valori
                destinazione.extend(coppia[1:])
                continue
            if uguale:
                voce = _parola(valore, parola)
            else:
                continue  # non si sa se prende un valore: la parola dopo resta posizionale
            if opzione_cf in PATTERN_PRIMO.get(nome, ()) and opzione_cf not in FILE_OPZIONE:
                continue  # `--regexp=…`: un pattern
            if opzione_cf == "--output":
                esito.scritture.append(voce)
            elif opzione_cf in FILE_OPZIONE:
                esito.file.append(voce)
            else:
                esito.valori.append(voce)
            continue
        # Opzioni corte, anche in gruppo (`-rn`, `-n5`, `-f.env`).
        lettere = testo[1:]
        if WINDOWS and ("-" + lettere.lower()) in PATTERN_PRIMO.get(nome, ()):
            pattern_da_opzione = True
        for posizione, lettera in enumerate(lettere):
            if lettera not in corte:
                continue
            opzione = "-" + lettera
            pattern = opzione in PATTERN_PRIMO.get(nome, ()) and opzione != "-f"
            if opzione in PATTERN_PRIMO.get(nome, ()):
                pattern_da_opzione = True
            attaccato = lettere[posizione + 1 :]
            if attaccato:
                voce = _parola(attaccato, parola)
            elif k < len(resto):
                voce = resto[k]
                k += 1
            else:
                break
            if pattern:
                pass  # `-e PATTERN`: un pattern, non un path
            elif nome == "sort" and opzione == "-o":
                esito.scritture.append(voce)
            elif opzione == "-f" and nome in PATTERN_PRIMO:
                esito.file.append(voce)
            else:
                esito.valori.append(voce)
            break
        else:
            if len(lettere) > 1:
                # Un gruppo sconosciuto può nascondere un valore attaccato (`-f.env`).
                esito.valori.append(_parola(lettere[1:], parola))
    if nome == "rg":
        testi = [p.testo for p in pezzo.parole[1:]]
        esito.salta_nascosti = not any(
            t in ("--hidden", "-.", "--unrestricted")
            or (t.startswith("-") and not t.startswith("--") and (t.count("u") >= 2 or "." in t))
            for t in testi
        )
    if nome in PATTERN_PRIMO and not pattern_da_opzione and posizionali:
        posizionali = posizionali[1:]
    if nome in SCRITTORI:
        esito.scritture.extend(posizionali)
    else:
        esito.file.extend(posizionali)
    if nome == "git":
        # `git show HEAD:.env` legge un path dal repo.
        for parola in pezzo.parole[1:]:
            prima, due_punti, dopo = parola.testo.partition(":")
            if due_punti and dopo and "/" not in prima and not dopo.startswith("//"):
                esito.valori.append(_parola(dopo, parola))
    return esito


def espandi(parola: Parola, base: str) -> list[str]:
    """Il testo della parola e, se ha un glob, i path in cui la shell lo espande
    (senza i file nascosti per `*`, come bash senza `dotglob`)."""
    testi = [parola.testo]
    if parola.glob:
        modello = os.path.expanduser(parola.testo)
        trovati = (
            glob.glob(modello, root_dir=base) if not os.path.isabs(modello) else glob.glob(modello)
        )
        testi.extend(trovati[:MAX_GLOB])
    return testi


class Giudice:
    """Il giudizio dei comandi di una riga, con le cartelle in cui può girare."""

    def __init__(self, impostazioni: dict, radice: Path, cartella: Path | None = None):
        self.impostazioni = impostazioni
        self.radice = radice
        self.radice_vera = _reale(str(radice))
        self.negati = [a for s, a in regole(impostazioni, "deny") if s == "Bash" and a]
        self.ammessi = [a for s, a in regole(impostazioni, "allow") if s == "Bash" and a]
        self.letture_negate = [a for s, a in regole(impostazioni, "deny") if s == "Read" and a]
        self.letture_ammesse = [a for s, a in regole(impostazioni, "allow") if s == "Read" and a]
        self.aperte = [forma(self.radice_vera), *cartelle_aggiuntive(impostazioni, radice)]
        iniziale = cartella if cartella is not None else radice
        # Ogni cartella in cui la riga può trovarsi: `cd` aggiunge, non toglie,
        # perché può fallire o stare in una pipeline.
        self.cartelle = [_reale(_nativo(str(iniziale), radice))]

    def lettura_negata(self, testo: str) -> str | None:
        for base in self.cartelle:
            scritto, vero = percorsi(testo, base)
            for modello in self.letture_negate:
                if percorso_in(scritto, modello, self.radice) or percorso_in(
                    vero, modello, self.radice_vera
                ):
                    return f"lettura negata da Read({modello}): {testo}"
        return None

    def fuori(self, testo: str) -> str | None:
        for base in self.cartelle:
            vero = percorsi(testo, base)[1]
            if any(dentro(vero, cartella) for cartella in self.aperte):
                continue
            if any(percorso_in(vero, m, self.radice_vera) for m in self.letture_ammesse):
                continue
            return f"lettura fuori dalle cartelle del giro non ammessa da un Read: {testo}"
        return None

    def ricorsione_negata(self, testo: str, salta_nascosti: bool = False) -> str | None:
        for base in self.cartelle:
            vero = percorsi(testo, base)[1]
            if not os.path.isdir(vero):
                continue
            for modello in self.letture_negate:
                if salta_nascosti and nascosto(vero, modello, self.radice_vera):
                    continue
                if sotto(vero, modello, self.radice) or sotto(vero, modello, self.radice_vera):
                    return f"lettura ricorsiva su una cartella che contiene Read({modello}) negato: {testo}"
        return None

    def scrittura(self, testo: str) -> str | None:
        if testo.lower() in CANALI or testo.startswith("/dev/fd/"):
            return None
        for base in self.cartelle:
            motivo = giudica_file(testo, self.impostazioni, self.radice, Path(base))
            if motivo:
                return motivo
        return None

    def regola(self, pezzo: Pezzo) -> str | None:
        forme = pezzo.forme
        # Su Windows i nomi dei comandi non distinguono maiuscole: il diniego
        # neanche (`RM x`); l'ammissione resta esatta.
        negabili = [f.lower() for f in forme] if WINDOWS else forme
        for modello in self.negati:
            for forma_ in negabili:
                if comando_ammesso(forma_, modello.lower() if WINDOWS else modello):
                    return f"comando negato da Bash({modello}): {forme[0]}"
        if not any(comando_ammesso(f, m) for f in forme for m in self.ammessi):
            return f"comando non ammesso dai permessi del giro: {forme[0]}"
        return None

    def giudica(self, pezzo: Pezzo) -> str | None:
        if pezzo.parole:
            motivo = self.regola(pezzo)
            if motivo:
                return motivo
        ruoli = argomenti(pezzo) if pezzo.parole else Argomenti()
        lettore = pezzo.nome in LETTORI
        letti = list(ruoli.file)
        for operatore, bersaglio in pezzo.redirezioni:
            if operatore in ("<<", "<<-", "<<<"):
                continue  # delimitatore o testo, non un file
            if operatore in ("<", "<&", "<>"):
                letti.append(bersaglio)
            if operatore != "<" and operatore != "<&":
                ruoli.scritture.append(bersaglio)
        for parola in [*letti, *ruoli.valori]:
            for testo in espandi(parola, self.cartelle[0]):
                motivo = self.lettura_negata(testo)
                if motivo:
                    return motivo
        controllati = [p for p in letti if p not in ruoli.file or lettore]
        for parola in controllati:
            if parola.testo.lower() in CANALI:
                continue
            for testo in espandi(parola, self.cartelle[0]):
                motivo = self.fuori(testo)
                if motivo:
                    return motivo
        if lettore and not ruoli.file and pezzo.nome in SU_CARTELLA:
            motivo = self.fuori(".")
            if motivo:
                return motivo
        if ruoli.ricorsivo:
            for testo in [p.testo for p in ruoli.file] or ["."]:
                motivo = self.ricorsione_negata(testo, ruoli.salta_nascosti)
                if motivo:
                    return motivo
        for parola in ruoli.scritture:
            for testo in espandi(parola, self.cartelle[0]):
                motivo = self.scrittura(testo)
                if motivo:
                    return motivo
        if pezzo.nome in CAMBIA_CARTELLA:
            if any(p.testo == "-" for p in pezzo.parole[1:]):
                raise NonScomponibile("`cd -` non determinabile")
            self.cambia(ruoli)
        return None

    def cambia(self, ruoli: Argomenti) -> None:
        bersagli = [p.testo for p in ruoli.file]
        if not bersagli:
            bersaglio = "~"
        elif bersagli[0] == "-" or len(bersagli) > 1 or ruoli.file[0].glob:
            raise NonScomponibile("cambio di cartella non determinabile")
        else:
            bersaglio = bersagli[0]
        nuove = [_reale(_nativo(bersaglio, base)) for base in self.cartelle]
        self.cartelle = list(dict.fromkeys([*self.cartelle, *nuove]))


def giudica_comando(
    comando: str, impostazioni: dict, radice: Path, cartella: Path | None = None
) -> str | None:
    """Il motivo del rifiuto di un comando, o None se ammesso.

    Ogni parola che può essere un path si giudica contro i `Read(…)` negati,
    con o senza barre (`cat .env`, `head alias` col symlink: BI e nixos
    dell'11/11/2026); i lettori restano nel perimetro del giro; redirezioni e
    `tee` in uscita sono scritture. `cartella` è la cartella di lavoro del
    comando, se Codex la dà diversa dalla radice."""
    try:
        divisi = analizza(comando)
        giudice = Giudice(impostazioni, radice, cartella)
        for pezzo in divisi:
            motivo = giudice.giudica(pezzo)
            if motivo:
                return motivo
    except NonScomponibile as errore:
        return f"comando non scomponibile ({errore}): {comando}"
    return None


def hook_impostazioni(impostazioni: dict, ingresso: dict) -> str | None:
    """Gli hook `PreToolUse` delle impostazioni sui comandi: uscita 2 è un rifiuto."""
    for voce in (impostazioni.get("hooks") or {}).get("PreToolUse") or []:
        if voce.get("matcher") not in (None, "", "*", "Bash"):
            continue
        for hook in voce.get("hooks") or []:
            if hook.get("type") != "command":
                continue
            esito = subprocess.run(
                hook["command"],
                shell=True,
                input=json.dumps({**ingresso, "tool_name": "Bash"}),
                capture_output=True,
                text=True,
                timeout=hook.get("timeout", 60),
                check=False,
            )
            if esito.returncode == 2:
                return (esito.stderr or esito.stdout).strip() or "bloccato da un hook del giro"
    return None


def giudica(ingresso: dict, impostazioni: dict) -> str | None:
    strumento = str(ingresso.get("tool_name") or "")
    dati = ingresso.get("tool_input") or {}
    radice = Path(ingresso.get("cwd") or os.getcwd())
    if strumento in INNOCUI:
        return None
    if strumento in STRUMENTI_FILE:
        testo = dati.get("command") or dati.get("input") or dati.get("patch") or ""
        percorsi = PATCH.findall(str(testo)) or [
            str(dati[k]) for k in ("file_path", "path") if dati.get(k)
        ]
        if not percorsi:
            return f"{strumento} senza percorsi riconoscibili"
        for percorso in percorsi:
            motivo = giudica_file(percorso.strip(), impostazioni, radice)
            if motivo:
                return motivo
        return None
    if strumento == "Bash":
        comando = dati.get("command")
        if isinstance(comando, list):
            comando = shlex.join(str(parte) for parte in comando)
        if not isinstance(comando, str):
            return "Bash senza comando"
        cartella = dati.get("workdir") or dati.get("cwd")
        cartella = Path(_nativo(str(cartella), radice)) if cartella else None
        return giudica_comando(comando, impostazioni, radice, cartella) or hook_impostazioni(
            impostazioni, ingresso
        )
    nomi = {s for s, a in regole(impostazioni, "allow") if a is None}
    negati = {s for s, a in regole(impostazioni, "deny") if a is None}
    if any(strumento == n or strumento.startswith(n + "__") for n in negati):
        return f"strumento negato: {strumento}"
    if strumento in nomi:
        return None
    return f"strumento non ammesso dai permessi del giro: {strumento}"


def hook(impostazioni_path: Path, dinieghi: Path | None) -> int:
    """`PreToolUse` di Codex: stampa il rifiuto in JSON, oppure tace."""
    try:
        ingresso = json.loads(sys.stdin.read())
        impostazioni = json.loads(impostazioni_path.read_text(encoding="utf-8"))
        motivo = giudica(ingresso, impostazioni)
    except Exception as errore:  # un hook rotto non lascia passare
        ingresso, motivo = {}, f"esecutore: hook non valutabile ({errore!r})"
    if motivo is None:
        return 0
    if dinieghi:
        voce = {"tool_name": ingresso.get("tool_name"), "tool_input": ingresso.get("tool_input")}
        try:
            with dinieghi.open("a", encoding="utf-8") as file:
                file.write(json.dumps(voce, ensure_ascii=False) + "\n")
        except OSError:
            pass
    decisione = {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": motivo,
    }
    print(json.dumps({"hookSpecificOutput": decisione}, ensure_ascii=False))
    return 0


# --- eventi ---------------------------------------------------------------------


def chiamata(nome: str, dati: dict) -> dict:
    contenuto = [{"type": "tool_use", "name": nome, "input": dati}]
    return {"type": "assistant", "message": {"content": contenuto}}


def stato_errore(testo: str) -> tuple[str | None, int | None]:
    if QUOTA.search(testo):
        return "rate_limit", 429
    if AUTENTICAZIONE.search(testo):
        return "authentication_failed", 401
    return None, None


class Traduttore:
    """Dagli eventi JSONL di `codex exec` al contratto del lanciatore."""

    def __init__(self) -> None:
        self.completato = False
        self.fallito: str | None = None
        self.ultimo_messaggio = ""
        self.usage: dict = {}
        self.turni = 0

    def traduci(self, evento: dict) -> list[dict]:
        tipo = evento.get("type")
        voce = evento.get("item") or {}
        genere = voce.get("type")
        if tipo == "thread.started":
            return [{"type": "system", "subtype": "init", "session_id": evento.get("thread_id")}]
        if tipo == "turn.started":
            self.turni += 1
            return []
        if tipo == "turn.completed":
            self.completato = True
            self.usage = evento.get("usage") or {}
            return []
        if tipo in ("turn.failed", "error"):
            dettaglio = evento.get("error") or {}
            testo = (
                dettaglio.get("message") if isinstance(dettaglio, dict) else str(dettaglio)
            ) or str(evento.get("message") or evento)
            self.fallito = testo
            errore, stato = stato_errore(testo)
            return [
                {"type": "error", "error": errore or "codex", "message": testo, "status": stato}
            ]
        if tipo in ("item.started", "item.updated", "item.completed"):
            if genere == "agent_message":
                if tipo == "item.completed":
                    self.ultimo_messaggio = voce.get("text") or ""
                    return [
                        {
                            "type": "assistant",
                            "message": {"content": [{"type": "text", "text": voce.get("text")}]},
                        }
                    ]
                return []
            if genere in ("reasoning", "todo_list"):
                return []
            if genere == "error":
                # Avvisi della CLI dentro il turno, non fallimenti del turno.
                return [{"type": "system", "subtype": "avviso", "message": voce.get("message")}]
            if tipo != "item.started":
                return []
            if genere == "command_execution":
                return [chiamata("Bash", {"command": voce.get("command")})]
            if genere == "file_change":
                percorsi = [c.get("path") for c in voce.get("changes") or []]
                return [chiamata("Edit", {"paths": percorsi})]
            # mcp_tool_call, web_search e i tipi nuovi: uno strumento è partito.
            return [chiamata(str(genere or "codex"), {k: v for k, v in voce.items() if k != "id"})]
        # Evento sconosciuto: lo si conserva, e il lanciatore lo legge come traccia incompleta.
        return [{"type": f"codex.{tipo}", "evento": evento}]

    def risultato(self, uscita: int, stderr: str, dinieghi: list[dict]) -> dict:
        successo = uscita == 0 and self.completato and not self.fallito
        testo = self.fallito or ("" if successo else stderr.strip()[-2000:])
        errore, stato = stato_errore(testo) if not successo else (None, None)
        return {
            "type": "result",
            "is_error": not successo,
            "terminal_reason": "completed" if successo else (errore or "codex_error"),
            "api_error_status": stato,
            "total_cost_usd": None,
            "result": self.ultimo_messaggio if successo else testo,
            "num_turns": self.turni,
            "usage": self.usage,
            "permission_denials": dinieghi,
        }


# --- esecuzione -----------------------------------------------------------------


def comando_hook(impostazioni: Path, dinieghi: Path) -> str:
    parti = [sys.executable, str(Path(__file__).resolve()), "--hook"]
    parti += ["--settings", str(impostazioni), "--dinieghi", str(dinieghi)]
    return subprocess.list2cmdline(parti) if WINDOWS else shlex.join(parti)


def toml(valore: object) -> str:
    """Un valore per `-c`: le stringhe JSON sono stringhe TOML valide."""
    if isinstance(valore, list):
        return "[" + ", ".join(toml(v) for v in valore) + "]"
    if isinstance(valore, dict):
        return "{" + ", ".join(f"{k} = {toml(v)}" for k, v in valore.items()) + "}"
    return json.dumps(valore)


def comando_codex(
    codex: str, radice: Path, cartella_git: str, hook_cmd: str, recinto_host: bool = False
) -> list[str]:
    hooks = [{"matcher": "*", "hooks": [{"type": "command", "command": hook_cmd, "timeout": 120}]}]
    if recinto_host:
        sandbox = ["--sandbox", "danger-full-access"]
    else:
        sandbox = [
            "--sandbox",
            "workspace-write",
            "-c",
            "sandbox_workspace_write.network_access=true",
            "-c",
            f"sandbox_workspace_write.writable_roots={toml([cartella_git])}",
        ]
    return [
        codex,
        "exec",
        "--json",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--dangerously-bypass-hook-trust",
        *sandbox,
        "-C",
        str(radice),
        "-c",
        'approval_policy="never"',
        "-c",
        f"hooks.PreToolUse={toml(hooks)}",
        "-",
    ]


def esegui(codex: str, prompt: Path, impostazioni_path: Path, recinto_host: bool = False) -> int:
    impostazioni = json.loads(impostazioni_path.read_text(encoding="utf-8"))
    radice = Path.cwd()
    cartella_git = subprocess.run(
        ["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.strip()
    if not cartella_git:
        print(json.dumps({"type": "error", "error": "codex", "message": "non è un repo git"}))
        return 14
    ambiente = {**os.environ, **{k: str(v) for k, v in (impostazioni.get("env") or {}).items()}}
    with tempfile.TemporaryDirectory(prefix="esecutore-codex-") as temporanea:
        dinieghi = Path(temporanea) / "dinieghi.jsonl"
        dinieghi.touch()
        traduttore = Traduttore()
        try:
            processo = subprocess.Popen(
                comando_codex(
                    codex,
                    radice,
                    cartella_git,
                    comando_hook(impostazioni_path, dinieghi),
                    recinto_host,
                ),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=ambiente,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        except OSError as errore:
            fine = traduttore.risultato(127, f"codex non avviato: {errore}", [])
            fine["terminal_reason"] = "executable_missing"
            print(json.dumps(fine, ensure_ascii=False))
            return 127
        assert processo.stdin and processo.stdout and processo.stderr
        processo.stdin.write(prompt.read_text(encoding="utf-8"))
        processo.stdin.close()
        for riga in processo.stdout:
            try:
                evento = json.loads(riga)
            except ValueError:
                evento = None
            uscite = traduttore.traduci(evento) if isinstance(evento, dict) else []
            if evento is None and riga.strip():
                uscite = [{"type": "codex.testo", "riga": riga.rstrip("\n")[:2000]}]
            for uscita in uscite:
                print(json.dumps(uscita, ensure_ascii=False), flush=True)
        stderr = processo.stderr.read()
        codice = processo.wait()
        negati = [
            json.loads(r) for r in dinieghi.read_text(encoding="utf-8").splitlines() if r.strip()
        ]
    for riga in stderr.splitlines():
        errore, stato = stato_errore(riga)
        if errore and " ERROR " in f" {riga} ":
            print(json.dumps({"type": "error", "error": errore, "message": riga, "status": stato}))
    fine = traduttore.risultato(codice, stderr, negati)
    print(json.dumps(fine, ensure_ascii=False), flush=True)
    return 0 if fine["is_error"] is False else (codice or 1)


def main(argv: list[str] | None = None) -> int:
    for flusso in (sys.stdout, sys.stderr):
        if flusso is not None and hasattr(flusso, "reconfigure"):
            flusso.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--codex", default="codex", help="eseguibile di Codex")
    parser.add_argument("--prompt", type=Path)
    parser.add_argument("--settings", type=Path, required=True)
    parser.add_argument(
        "--recinto-host",
        action="store_true",
        help="l'host racchiude il giro nel suo recinto: Codex non aggiunge il proprio",
    )
    parser.add_argument("--hook", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--dinieghi", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.hook:
        return hook(args.settings, args.dinieghi)
    if args.prompt is None:
        parser.error("--prompt è richiesto")
    return esegui(args.codex, args.prompt, args.settings, args.recinto_host)


if __name__ == "__main__":
    raise SystemExit(main())
