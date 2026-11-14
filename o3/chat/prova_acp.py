"""Client ACP della prova del 2026-11-14: punto di partenza della chat.

Lancia un adattatore ACP (`claude-agent-acp` o `codex-acp`), apre una sessione
in una cartella e manda una serie di prompt, registrando ogni messaggio in un
log JSON Lines. È il client con cui la prova ha verificato, in `casa`, che una
sessione aperta via ACP si comporta come il terminale con Claude Code e con
Codex (task `o2/chat-del-coordinatore.md`, «Punto di partenza»). Non è ancora
la chat: niente interfaccia, prompt scritti in anticipo.

Uso: python3 -I o3/chat/prova_acp.py <cartella> <file-prompt.json> <log.jsonl> [modo]

L'adattatore si sceglie con la variabile ADATTATORE (predefinito
`npx -y @agentclientprotocol/claude-agent-acp@0.107.0`); per Codex
`ADATTATORE="npx -y @agentclientprotocol/codex-acp@2.6.0"` e `CODEX_PATH`.
Il file dei prompt è una lista di oggetti `{"testo", "rifiuta", "modo"}`: una
richiesta di permesso il cui contenuto nomina una delle parole di `rifiuta` si
rifiuta, le altre si accettano una volta; `modo` cambia il modo di permesso
prima del prompt. Il client non dichiara capacità su file e terminale, così
l'agente usa i propri strumenti, come nel terminale. Solo libreria standard.
"""

import json
import os
import subprocess
import sys
import threading
import time

PREDEFINITO = "npx -y @agentclientprotocol/claude-agent-acp@0.107.0"


class Sessione:
    """Un adattatore ACP lanciato in una cartella, con il suo log."""

    def __init__(self, cartella, log, errori):
        self.log = log
        self.proc = subprocess.Popen(
            os.environ.get("ADATTATORE", PREDEFINITO).split(),
            cwd=cartella,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=errori,
            text=True,
            bufsize=1,
        )
        self.prossimo_id = 0
        self.attese = {}
        self.rifiuta = []
        threading.Thread(target=self.lettore, daemon=True).start()

    def scrivi(self, tipo, dati):
        voce = {"t": round(time.time(), 2), "tipo": tipo, "dati": dati}
        self.log.write(json.dumps(voce, ensure_ascii=False) + "\n")
        self.log.flush()

    def invia(self, msg):
        self.scrivi("inviato", msg)
        self.proc.stdin.write(json.dumps(msg) + "\n")
        self.proc.stdin.flush()

    def richiesta(self, metodo, params, timeout=900):
        self.prossimo_id += 1
        mio = self.prossimo_id
        evento = threading.Event()
        self.attese[mio] = [evento, None]
        self.invia({"jsonrpc": "2.0", "id": mio, "method": metodo, "params": params})
        if not evento.wait(timeout):
            raise TimeoutError(metodo)
        return self.attese.pop(mio)[1]

    def permesso(self, msg):
        p = msg["params"]
        testo = json.dumps(p.get("toolCall", {}), ensure_ascii=False)
        tipo = "reject_once" if any(w in testo for w in self.rifiuta) else "allow_once"
        scelta = next((o for o in p["options"] if o["kind"] == tipo), p["options"][0])
        self.scrivi("permesso", {"richiesta": p, "scelta": scelta["optionId"]})
        esito = {"outcome": "selected", "optionId": scelta["optionId"]}
        self.invia({"jsonrpc": "2.0", "id": msg["id"], "result": {"outcome": esito}})

    def lettore(self):
        for riga in self.proc.stdout:
            try:
                msg = json.loads(riga)
            except ValueError:
                self.scrivi("non-json", riga)
                continue
            if "method" in msg and "id" in msg:  # richiesta dall'agente
                if msg["method"] == "session/request_permission":
                    self.permesso(msg)
                else:
                    self.scrivi("richiesta-non-gestita", msg)
                    errore = {"code": -32601, "message": "non supportato"}
                    self.invia({"jsonrpc": "2.0", "id": msg["id"], "error": errore})
            elif "id" in msg:  # risposta
                self.scrivi("risposta", msg)
                if msg["id"] in self.attese:
                    self.attese[msg["id"]][1] = msg
                    self.attese[msg["id"]][0].set()
            else:  # notifica
                self.scrivi("notifica", msg)

    def modo(self, sid, modo):
        r = self.richiesta("session/set_mode", {"sessionId": sid, "modeId": modo}, 60)
        print("set_mode", modo, ":", r.get("result", r.get("error")), flush=True)


def main(argv):
    cartella, file_prompt, file_log = argv[1], argv[2], argv[3]
    with open(file_prompt, encoding="utf-8") as f:
        prompt = json.load(f)
    with (
        open(file_log, "w", encoding="utf-8") as log,
        open(file_log + ".stderr", "w", encoding="utf-8") as errori,
    ):
        s = Sessione(cartella, log, errori)
        cliente = {"name": "prova-metodo", "version": "0.1"}
        s.richiesta(
            "initialize", {"protocolVersion": 1, "clientCapabilities": {}, "clientInfo": cliente}
        )
        aperta = s.richiesta("session/new", {"cwd": cartella, "mcpServers": []}, 300)
        if "error" in aperta:
            print("session/new:", aperta["error"])
            return 1
        sid = aperta["result"]["sessionId"]
        print("sessione", sid, flush=True)
        if len(argv) > 4:
            s.modo(sid, argv[4])
        for i, p in enumerate(prompt, 1):
            s.rifiuta[:] = p.get("rifiuta", [])
            if p.get("modo"):
                s.modo(sid, p["modo"])
            testo = [{"type": "text", "text": p["testo"]}]
            r = s.richiesta("session/prompt", {"sessionId": sid, "prompt": testo})
            print(f"prompt {i}:", r.get("result", r.get("error")), flush=True)
        s.proc.stdin.close()
        s.proc.wait(timeout=30)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
