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
  `Bash(…)` per i comandi, `Edit(…)`/`Write(…)` per i file di `apply_patch`,
  `Read(…)` negato per i path che un comando nomina e, per i comandi di
  lettura (`cat`, `head`, `ls`…), `Read(…)` ammesso per i path fuori dal
  checkout, perché Codex non ha un tool Read; poi gli hook `Bash` delle
  impostazioni, cioè quello del lanciatore sul commit. Il rifiuto è il JSON
  `permissionDecision: deny`; `--dangerously-bypass-hook-trust` è necessario
  perché l'hook è inline, e la fonte è questo file del canone;
- sandbox `workspace-write` con rete e con la cartella git scrivibile, senza la
  quale il commit fallisce (`index.lock` in sola lettura); approvazioni `never`;
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
import fnmatch
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

WINDOWS = os.name == "nt"
OPERATORI = {"&&", "||", ";", "|", "&", "\n"}
SOSTITUZIONE = re.compile(r"\$\(|`|<\(|>\(")
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
LETTORI |= {"readlink", "sed", "stat", "file"}
# Strumenti locali di Codex senza effetti fuori dalla sessione.
INNOCUI = {"update_plan"}
STRUMENTI_FILE = {"apply_patch", "Edit", "Write"}


# --- politica -------------------------------------------------------------------


def regole(impostazioni: dict, tipo: str) -> list[tuple[str, str | None]]:
    """Le regole `allow` o `deny` come coppie (strumento, argomento)."""
    coppie = []
    for voce in (impostazioni.get("permissions") or {}).get(tipo) or []:
        trovata = REGOLA.match(str(voce).strip())
        if trovata:
            coppie.append((trovata.group(1), trovata.group(2)))
    return coppie


def comando_ammesso(pezzo: str, modello: str) -> bool:
    """Un pezzo di comando contro un modello `Bash(…)` di Claude."""
    if modello.endswith(":*"):
        radice = modello[:-2]
        return pezzo == radice or pezzo.startswith(radice + " ")
    if modello.endswith(" *") and pezzo == modello[:-2]:
        return True
    return fnmatch.fnmatchcase(pezzo, modello)


def pezzi(comando: str) -> list[str] | None:
    """I comandi semplici di una riga di shell; None se non si sa dividerla."""
    if SOSTITUZIONE.search(comando):
        return None
    # Una riga nuova separa i comandi; un heredoc diventa comandi da ammettere, e cade.
    comando = comando.replace("\r\n", "\n").replace("\n", " ; ")
    lessico = shlex.shlex(comando, posix=True, punctuation_chars=";&|")
    lessico.whitespace_split = True
    lessico.whitespace = " \t\r"
    risultato: list[str] = []
    corrente: list[str] = []
    try:
        for parola in lessico:
            if parola in OPERATORI or set(parola) <= set(";&|\n"):
                if corrente:
                    risultato.append(" ".join(corrente))
                corrente = []
            else:
                corrente.append(parola)
    except ValueError:
        return None
    if corrente:
        risultato.append(" ".join(corrente))
    return risultato


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


def assoluto(modello: str, radice: Path) -> str:
    """Un modello di path di Claude come path assoluto con barre `/`."""
    if modello.startswith("//"):
        base = modello[1:]
    elif modello.startswith("~/"):
        base = str(Path.home()) + modello[1:]
    elif modello.startswith("./"):
        base = f"{radice.as_posix()}/{modello[2:]}"
    elif modello.startswith("/"):
        base = f"{radice.as_posix()}{modello}"
    else:
        base = f"{radice.as_posix()}/{modello}"
    return base.replace("\\", "/")


def percorso_reale(percorso: str, radice: Path) -> str:
    pieno = Path(percorso) if os.path.isabs(percorso) else radice / percorso
    return os.path.normpath(str(pieno)).replace("\\", "/")


def percorso_in(percorso: str, modello: str, radice: Path) -> bool:
    return bool(_regex_percorso(assoluto(modello, radice)).match(percorso))


def giudica_file(percorso: str, impostazioni: dict, radice: Path) -> str | None:
    """Il motivo del rifiuto di una scrittura, o None se ammessa."""
    reale = percorso_reale(percorso, radice)
    for strumento, argomento in regole(impostazioni, "deny"):
        if strumento in ("Edit", "Write") and argomento and percorso_in(reale, argomento, radice):
            return f"scrittura negata da {strumento}({argomento}): {percorso}"
    for strumento, argomento in regole(impostazioni, "allow"):
        if strumento in ("Edit", "Write") and argomento and percorso_in(reale, argomento, radice):
            return None
    return f"scrittura non ammessa dai permessi del giro: {percorso}"


def giudica_comando(comando: str, impostazioni: dict, radice: Path) -> str | None:
    """Il motivo del rifiuto di un comando, o None se ammesso."""
    divisi = pezzi(comando)
    if divisi is None:
        return f"comando non scomponibile (sostituzioni o virgolette): {comando}"
    negati = [a for s, a in regole(impostazioni, "deny") if s == "Bash" and a]
    ammessi = [a for s, a in regole(impostazioni, "allow") if s == "Bash" and a]
    letture_negate = [a for s, a in regole(impostazioni, "deny") if s == "Read" and a]
    letture_ammesse = [a for s, a in regole(impostazioni, "allow") if s == "Read" and a]
    interno = os.path.normpath(str(radice)).replace("\\", "/")
    for pezzo in divisi:
        for modello in negati:
            if comando_ammesso(pezzo, modello):
                return f"comando negato da Bash({modello}): {pezzo}"
        if not any(comando_ammesso(pezzo, modello) for modello in ammessi):
            return f"comando non ammesso dai permessi del giro: {pezzo}"
        for parola in pezzo.split()[1:]:
            parola = parola.lstrip("<>").strip("'\"")
            if "/" not in parola and "\\" not in parola and not parola.startswith("~"):
                continue
            parola = os.path.expanduser(parola)
            reale = percorso_reale(parola, radice)
            for modello in letture_negate:
                if percorso_in(reale, modello, radice):
                    return f"lettura negata da Read({modello}): {parola}"
            fuori = reale != interno and not reale.startswith(interno + "/")
            if (
                fuori
                and pezzo.split()[0] in LETTORI
                and not any(percorso_in(reale, m, radice) for m in letture_ammesse)
            ):
                return f"lettura fuori dal checkout non ammessa da un Read del giro: {parola}"
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
        return giudica_comando(comando, impostazioni, radice) or hook_impostazioni(
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


def comando_codex(codex: str, radice: Path, cartella_git: str, hook_cmd: str) -> list[str]:
    hooks = [{"matcher": "*", "hooks": [{"type": "command", "command": hook_cmd, "timeout": 120}]}]
    return [
        codex,
        "exec",
        "--json",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--dangerously-bypass-hook-trust",
        "--sandbox",
        "workspace-write",
        "-C",
        str(radice),
        "-c",
        'approval_policy="never"',
        "-c",
        "sandbox_workspace_write.network_access=true",
        "-c",
        f"sandbox_workspace_write.writable_roots={toml([cartella_git])}",
        "-c",
        f"hooks.PreToolUse={toml(hooks)}",
        "-",
    ]


def esegui(codex: str, prompt: Path, impostazioni_path: Path) -> int:
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
                    codex, radice, cartella_git, comando_hook(impostazioni_path, dinieghi)
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
    parser.add_argument("--hook", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--dinieghi", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.hook:
        return hook(args.settings, args.dinieghi)
    if args.prompt is None:
        parser.error("--prompt è richiesto")
    return esegui(args.codex, args.prompt, args.settings)


if __name__ == "__main__":
    raise SystemExit(main())
