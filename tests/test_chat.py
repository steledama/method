"""La chat del coordinatore: sessioni ACP, permessi e presidi del server.

L'adattatore è finto (`ADATTATORE_FINTO` qui sotto): parla ACP su stdin e
stdout come `claude-agent-acp`, così si prova la meccanica della chat senza
un harness né un abbonamento. Eseguire con python3 -m unittest discover -s tests.
"""

import http.client
import importlib.util
import json
import sys
import tempfile
import textwrap
import threading
import time
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path

CHAT = Path(__file__).resolve().parents[1] / "o3" / "chat"
sys.path.insert(0, str(CHAT))

import acp

# `serve` è anche il servitore delle viste (`o3/view/serve.py`), che altri test
# importano con quel nome: la chat si carica sotto un nome suo.
_spec = importlib.util.spec_from_file_location("chat_serve", CHAT / "serve.py")
serve = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(serve)

ADATTATORE_FINTO = textwrap.dedent(
    """
    import json, sys
    def scrivi(m):
        sys.stdout.write(json.dumps(m) + "\\n"); sys.stdout.flush()
    def update(u):
        scrivi({"jsonrpc": "2.0", "method": "session/update", "params": {"sessionId": "s1", "update": u}})
    attesa = None
    for riga in sys.stdin:
        m = json.loads(riga)
        metodo = m.get("method")
        if metodo == "initialize":
            scrivi({"jsonrpc": "2.0", "id": m["id"], "result": {"protocolVersion": 1}})
        elif metodo == "session/new":
            modi = {"currentModeId": "default", "availableModes": [{"id": "default", "name": "Default"}, {"id": "plan", "name": "Plan"}]}
            scrivi({"jsonrpc": "2.0", "id": m["id"], "result": {"sessionId": "s1", "modes": modi}})
        elif metodo == "session/set_mode":
            scrivi({"jsonrpc": "2.0", "id": m["id"], "result": {}})
        elif metodo == "session/prompt":
            attesa = m["id"]
            update({"sessionUpdate": "agent_message_chunk", "content": {"type": "text", "text": "eco: " + m["params"]["prompt"][0]["text"]}})
            update({"sessionUpdate": "tool_call", "toolCallId": "t1", "title": "Scrive a.txt", "kind": "edit", "status": "pending"})
            diff = {"type": "diff", "path": "a.txt", "oldText": "uno", "newText": "due"}
            opzioni = [{"optionId": "si", "name": "Consenti", "kind": "allow_once"}, {"optionId": "no", "name": "Rifiuta", "kind": "reject_once"}]
            scrivi({"jsonrpc": "2.0", "id": 900, "method": "session/request_permission",
                    "params": {"sessionId": "s1", "toolCall": {"toolCallId": "t1", "content": [diff]}, "options": opzioni}})
            scrivi({"jsonrpc": "2.0", "id": 901, "method": "fs/read_text_file", "params": {}})
        elif m.get("id") == 900:
            esito = m["result"]["outcome"]
            update({"sessionUpdate": "tool_call_update", "toolCallId": "t1", "status": "completed" if esito.get("optionId") == "si" else "failed"})
            scrivi({"jsonrpc": "2.0", "id": attesa, "result": {"stopReason": "end_turn" if esito.get("optionId") else "cancelled"}})
        elif metodo == "session/cancel":
            pass
    """
)


class Gruppo(unittest.TestCase):
    """L'istanza e i membri con un checkout accanto."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.istanza = base / "casa"
        for nome in ("casa", "nixos"):
            (base / nome / ".git").mkdir(parents=True)
        (self.istanza / "world.md").write_text(
            "# W\n\nIntro.\n\n## Membri\n\n- **nixos** — host\n- **salute** — senza checkout\n"
        )
        self.finto = base / "adattatore.py"
        self.finto.write_text(ADATTATORE_FINTO)

    def tearDown(self):
        self.tmp.cleanup()

    def test_repo_con_checkout(self):
        self.assertEqual(list(serve.repo_del_gruppo(self.istanza)), ["casa", "nixos"])


class Sito(Gruppo):
    def setUp(self):
        super().setUp()
        gestore = type(
            "G",
            (serve.Chat,),
            {
                "istanza": self.istanza,
                "sessioni": {},
                "blocco": threading.Lock(),
                "comandi": {h: [sys.executable, "-I", str(self.finto)] for h in acp.ADATTATORI},
            },
        )
        self.gestore = gestore
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), gestore)
        self.server.daemon_threads = True
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.porta = self.server.server_address[1]

    def tearDown(self):
        for sessione in self.gestore.sessioni.values():
            sessione.chiudi()
        self.server.shutdown()
        self.server.server_close()
        super().tearDown()

    def chiama(self, metodo, path, dati=None, intestazioni=None):
        conn = http.client.HTTPConnection("127.0.0.1", self.porta, timeout=10)
        corpo = None if dati is None else json.dumps(dati)
        h = {"Content-Type": "application/json"} | (intestazioni or {})
        conn.request(metodo, path, corpo, h)
        r = conn.getresponse()
        dati = r.read()
        conn.close()
        return r.status, json.loads(dati) if dati and r.getheader("Content-Type", "").startswith(
            "application/json"
        ) else dati

    def aspetta(self, sessione, tipo, timeout=10):
        fine = time.time() + timeout
        while time.time() < fine:
            trovati = [e for e in sessione.eventi if e["tipo"] == tipo]
            if trovati:
                return trovati[-1]
            time.sleep(0.02)
        self.fail(f"nessun evento {tipo}: {[e['tipo'] for e in sessione.eventi]}")

    def test_pagina_e_repo(self):
        status, corpo = self.chiama("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn(b"Chat del gruppo", corpo)
        status, info = self.chiama("GET", "/repo")
        self.assertEqual(info["repo"], ["casa", "nixos"])

    def test_turno_con_permesso_consentito(self):
        status, aperta = self.chiama("POST", "/sessioni", {"repo": "nixos", "harness": "claude"})
        self.assertEqual(status, 200, aperta)
        sessione = self.gestore.sessioni[aperta["id"]]
        self.assertEqual(self.aspetta(sessione, "aperta")["modi"][1]["id"], "plan")
        self.assertEqual(
            self.chiama("POST", f"/sessioni/{sessione.id}/prompt", {"testo": "ciao"})[0], 200
        )
        permesso = self.aspetta(sessione, "permesso")
        self.assertEqual(permesso["toolCall"]["content"][0]["newText"], "due")
        # Un secondo prompt durante il turno è rifiutato.
        self.assertEqual(
            self.chiama("POST", f"/sessioni/{sessione.id}/prompt", {"testo": "altro"})[0], 409
        )
        # Un'opzione non offerta non passa.
        stato, _ = self.chiama(
            "POST", f"/sessioni/{sessione.id}/permesso", {"id": permesso["id"], "optionId": "forse"}
        )
        self.assertEqual(stato, 400)
        stato, _ = self.chiama(
            "POST", f"/sessioni/{sessione.id}/permesso", {"id": permesso["id"], "optionId": "si"}
        )
        self.assertEqual(stato, 200)
        fine = self.aspetta(sessione, "fine-turno")
        self.assertEqual(fine["stopReason"], "end_turn")
        aggiornamenti = [e["update"] for e in sessione.eventi if e["tipo"] == "update"]
        self.assertIn("completed", [u.get("status") for u in aggiornamenti])
        self.assertEqual(aggiornamenti[0]["content"]["text"], "eco: ciao")

    def test_annulla_chiude_il_permesso(self):
        _, aperta = self.chiama("POST", "/sessioni", {"repo": "casa", "harness": "codex"})
        sessione = self.gestore.sessioni[aperta["id"]]
        self.chiama("POST", f"/sessioni/{sessione.id}/prompt", {"testo": "x"})
        self.aspetta(sessione, "permesso")
        self.assertEqual(self.chiama("POST", f"/sessioni/{sessione.id}/annulla", {})[0], 200)
        self.assertEqual(self.aspetta(sessione, "fine-turno")["stopReason"], "cancelled")
        self.assertIsNone(self.aspetta(sessione, "permesso-chiuso")["optionId"])

    def test_modo_e_chiusura(self):
        _, aperta = self.chiama("POST", "/sessioni", {"repo": "casa", "harness": "claude"})
        sid = aperta["id"]
        self.assertEqual(self.chiama("POST", f"/sessioni/{sid}/modo", {"modo": "plan"})[0], 200)
        self.assertEqual(self.chiama("POST", f"/sessioni/{sid}/chiudi", {})[0], 200)
        self.assertEqual(self.chiama("POST", f"/sessioni/{sid}/prompt", {"testo": "x"})[0], 409)
        # Il flusso di una sessione chiusa rende tutti gli eventi e si chiude.
        status, corpo = self.chiama("GET", f"/sessioni/{sid}/eventi?da=0")
        self.assertEqual(status, 200)
        self.assertIn(b'"tipo": "chiusa"', corpo)

    def test_repo_e_harness_fuori_dal_gruppo(self):
        self.assertEqual(
            self.chiama("POST", "/sessioni", {"repo": "salute", "harness": "claude"})[0], 400
        )
        self.assertEqual(
            self.chiama("POST", "/sessioni", {"repo": "casa", "harness": "altro"})[0], 400
        )

    def test_presidi_host_e_origin(self):
        self.assertEqual(self.chiama("GET", "/repo", intestazioni={"Host": "evil.example"})[0], 403)
        estranea = {"Origin": "http://evil.example"}
        self.assertEqual(
            self.chiama("POST", "/sessioni", {"repo": "casa", "harness": "claude"}, estranea)[0],
            403,
        )
        propria = {"Origin": f"http://127.0.0.1:{self.porta}"}
        self.assertEqual(
            self.chiama("POST", "/sessioni", {"repo": "salute", "harness": "claude"}, propria)[0],
            400,
        )


class Avvio(unittest.TestCase):
    def test_rifiuta_bind_fuori_da_loopback(self):
        self.assertTrue(serve.loopback("127.0.0.1"))
        self.assertTrue(serve.loopback("::1"))
        self.assertTrue(serve.loopback("localhost"))
        self.assertFalse(serve.loopback("0.0.0.0"))
        self.assertFalse(serve.loopback("192.168.1.10"))


if __name__ == "__main__":
    unittest.main()
