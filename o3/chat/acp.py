"""Una sessione ACP vista dalla chat: l'adattatore, gli eventi, i permessi.

Lancia un adattatore ACP (`claude-agent-acp` o `codex-acp`) nella cartella di
un repo, apre la sessione e traduce il protocollo in una sequenza di eventi
che la pagina legge in ordine (`Sessione.eventi`). Il client non dichiara
capacità su file e terminale, come nella prova (`prova_acp.py`): l'agente usa
i propri strumenti, con i permessi del repo e dell'harness. Le richieste di
permesso restano in attesa finché il custode non sceglie un'opzione dalla
pagina; nessuna risposta automatica.

Eventi, ciascuno con `n` progressivo:

- `aperta`: sessione pronta, con `modi` (quelli che l'adattatore dichiara) e
  `modo` corrente;
- `utente`: il prompt inviato;
- `update`: un `session/update` dell'agente, passato com'è (messaggi,
  pensieri, chiamate di strumenti, piano, cambio di modo);
- `permesso`: una richiesta di permesso, con `id`, `toolCall` e `options`;
  `permesso-chiuso` quando ha avuto risposta;
- `fine-turno`: la risposta a `session/prompt`, con `stopReason` o `errore`;
- `errore`, `chiusa`.

Solo libreria standard: gira anche su Windows.
"""

from __future__ import annotations

import contextlib
import json
import os
import shlex
import subprocess
import threading
import time
import uuid
from pathlib import Path

# Versioni provate il 2026-11-14 (task `chat-del-coordinatore`, «Punto di partenza»).
ADATTATORI = {
    "claude": "npx -y @agentclientprotocol/claude-agent-acp@0.107.0",
    "codex": "npx -y @agentclientprotocol/codex-acp@2.6.0",
}
CLIENTE = {"name": "chat-metodo", "version": "0.1"}


class Occupata(Exception):
    """Un turno è già in corso: ACP ne regge uno per sessione."""


class Sessione:
    """Un adattatore ACP lanciato in una cartella, con gli eventi per la pagina."""

    def __init__(self, repo: str, cartella: Path, harness: str, comando: list[str] | None = None):
        self.id = uuid.uuid4().hex[:12]
        self.repo, self.cartella, self.harness = repo, cartella, harness
        self.eventi: list[dict] = []
        self.cambio = threading.Condition()
        self.attese: dict[int, list] = {}
        self.permessi: dict[str, dict] = {}
        self.prossimo_id = 0
        self.sid: str | None = None
        self.in_turno = False
        self.chiusa = False
        argv = comando or shlex.split(
            os.environ.get(f"ADATTATORE_{harness.upper()}", ADATTATORI[harness])
        )
        self.proc = subprocess.Popen(
            argv,
            cwd=cartella,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            bufsize=1,
        )
        self.scrittura = threading.Lock()
        threading.Thread(target=self._lettore, daemon=True).start()

    # --- eventi -----------------------------------------------------------------

    def evento(self, tipo: str, **dati) -> None:
        with self.cambio:
            self.eventi.append(
                {"n": len(self.eventi), "t": round(time.time(), 2), "tipo": tipo, **dati}
            )
            self.cambio.notify_all()

    def attendi(self, da: int, timeout: float) -> list[dict]:
        """Gli eventi dal numero `da`, aspettandone uno nuovo fino a `timeout`."""
        with self.cambio:
            if len(self.eventi) <= da and not self.chiusa:
                self.cambio.wait(timeout)
            return self.eventi[da:]

    # --- JSON-RPC -----------------------------------------------------------------

    def _invia(self, msg: dict) -> None:
        with self.scrittura:
            if self.proc.stdin is None or self.proc.stdin.closed:
                raise BrokenPipeError("adattatore chiuso")
            self.proc.stdin.write(json.dumps(msg) + "\n")
            self.proc.stdin.flush()

    def richiesta(self, metodo: str, params: dict, timeout: float = 900) -> dict:
        evento = threading.Event()
        with self.scrittura:
            self.prossimo_id += 1
            mio = self.prossimo_id
        self.attese[mio] = [evento, None]
        self._invia({"jsonrpc": "2.0", "id": mio, "method": metodo, "params": params})
        if not evento.wait(timeout):
            self.attese.pop(mio, None)
            raise TimeoutError(metodo)
        return self.attese.pop(mio)[1]

    def _lettore(self) -> None:
        assert self.proc.stdout is not None
        try:
            for riga in self.proc.stdout:
                self._messaggio(riga)
        except (ValueError, OSError):
            pass  # stdout chiuso da `chiudi` mentre si leggeva
        self._chiusura("l'adattatore è uscito")

    def _messaggio(self, riga: str) -> None:
        try:
            msg = json.loads(riga)
        except ValueError:
            return
        if not isinstance(msg, dict):
            return
        if "method" in msg and "id" in msg:
            with contextlib.suppress(BrokenPipeError, OSError):
                self._richiesta_agente(msg)
        elif "id" in msg:
            attesa = self.attese.get(msg["id"])
            if attesa:
                attesa[1] = msg
                attesa[0].set()
        elif msg.get("method") == "session/update":
            self.evento("update", update=msg.get("params", {}).get("update", {}))

    def _richiesta_agente(self, msg: dict) -> None:
        if msg["method"] == "session/request_permission":
            chiave = str(msg["id"])
            params = msg.get("params", {})
            self.permessi[chiave] = msg
            self.evento(
                "permesso",
                id=chiave,
                toolCall=params.get("toolCall", {}),
                options=params.get("options", []),
            )
            return
        # Nessuna capacità dichiarata su file e terminale: il resto non è supportato.
        errore = {"code": -32601, "message": f"{msg['method']} non supportato dal client"}
        self._invia({"jsonrpc": "2.0", "id": msg["id"], "error": errore})

    # --- atti della pagina ----------------------------------------------------------

    def apri(self, timeout: float = 300) -> None:
        self.richiesta(
            "initialize",
            {"protocolVersion": 1, "clientCapabilities": {}, "clientInfo": CLIENTE},
            timeout,
        )
        aperta = self.richiesta(
            "session/new", {"cwd": str(self.cartella), "mcpServers": []}, timeout
        )
        if "error" in aperta:
            raise RuntimeError(aperta["error"].get("message", "session/new fallita"))
        risultato = aperta["result"]
        self.sid = risultato["sessionId"]
        modi = risultato.get("modes") or {}
        self.evento(
            "aperta",
            repo=self.repo,
            harness=self.harness,
            modi=modi.get("availableModes", []),
            modo=modi.get("currentModeId"),
        )

    def prompt(self, testo: str) -> None:
        with self.cambio:
            if self.in_turno:
                raise Occupata()
            self.in_turno = True
        self.evento("utente", testo=testo)
        threading.Thread(target=self._turno, args=(testo,), daemon=True).start()

    def _turno(self, testo: str) -> None:
        try:
            risposta = self.richiesta(
                "session/prompt",
                {"sessionId": self.sid, "prompt": [{"type": "text", "text": testo}]},
                timeout=6 * 3600,
            )
            if "error" in risposta:
                self.evento("fine-turno", errore=risposta["error"].get("message", "errore"))
            else:
                self.evento("fine-turno", stopReason=risposta["result"].get("stopReason"))
        except (TimeoutError, BrokenPipeError, OSError) as errore:
            self.evento("fine-turno", errore=str(errore) or errore.__class__.__name__)
        finally:
            with self.cambio:
                self.in_turno = False

    def rispondi(self, chiave: str, opzione: str | None) -> None:
        """Risponde a una richiesta di permesso; `None` la annulla."""
        msg = self.permessi.pop(chiave, None)
        if msg is None:
            raise KeyError(chiave)
        if opzione is None:
            esito = {"outcome": "cancelled"}
        else:
            valide = {o.get("optionId") for o in msg.get("params", {}).get("options", [])}
            if opzione not in valide:
                self.permessi[chiave] = msg
                raise ValueError(opzione)
            esito = {"outcome": "selected", "optionId": opzione}
        self._invia({"jsonrpc": "2.0", "id": msg["id"], "result": {"outcome": esito}})
        self.evento("permesso-chiuso", id=chiave, optionId=opzione)

    def modo(self, modo: str) -> None:
        risposta = self.richiesta("session/set_mode", {"sessionId": self.sid, "modeId": modo}, 60)
        if "error" in risposta:
            raise RuntimeError(risposta["error"].get("message", "set_mode fallito"))
        self.evento(
            "update", update={"sessionUpdate": "current_mode_update", "currentModeId": modo}
        )

    def annulla(self) -> None:
        """Interrompe il turno: annulla i permessi in attesa e manda `session/cancel`."""
        for chiave in list(self.permessi):
            self.rispondi(chiave, None)
        self._invia(
            {"jsonrpc": "2.0", "method": "session/cancel", "params": {"sessionId": self.sid}}
        )

    def chiudi(self) -> None:
        if self.proc.poll() is None:
            try:
                self.proc.stdin.close()
                self.proc.wait(timeout=10)
            except (OSError, subprocess.TimeoutExpired):
                self.proc.kill()
                self.proc.wait()
        self._chiusura("chiusa dal custode")
        if self.proc.stdout is not None:
            self.proc.stdout.close()

    def _chiusura(self, motivo: str) -> None:
        with self.cambio:
            if self.chiusa:
                return
            self.chiusa = True
        for attesa in list(self.attese.values()):
            attesa[1] = {"error": {"message": motivo}}
            attesa[0].set()
        self.evento("chiusa", motivo=motivo)
