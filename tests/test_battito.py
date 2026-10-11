"""Il battito nella vista: semaforo, stati senza tentativi, rotte di serve.py.

Lo stato è finto, scritto in una cartella temporanea con la forma del modulo
`battiti` di `nixos`. Eseguire con python3 -m unittest discover -s tests.
"""

import json
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

BUILDERS = Path(__file__).resolve().parents[1] / "o3" / "view"
sys.path.insert(0, str(BUILDERS))

import battito

NOW = datetime.fromisoformat("2026-10-11T12:00:00+02:00")


def ident(char: str) -> str:
    return char * 32


class StateCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.state = self.root / "prova"
        (self.state / "giri").mkdir(parents=True)
        self.decide({"state": "manuale", "maxRuntime": "45min"})

    def tearDown(self):
        self.tmp.cleanup()

    def decide(self, decision: dict) -> None:
        (self.root / "decisioni.json").write_text(json.dumps({"prova": decision}))

    def attempt(self, char: str, ts: str, close: dict | None, result: str | None = None):
        rows = [{"evento": "partenza", "id": ident(char), "ts": ts}]
        if close is not None:
            rows.append({"evento": "chiusura", "id": ident(char), **close})
        with (self.state / "tentativi.jsonl").open("a") as out:
            out.writelines(json.dumps(row) + "\n" for row in rows)
        if result is not None:
            event = {"type": "result", "result": result}
            (self.state / "giri" / f"{ident(char)}.jsonl").write_text(json.dumps(event) + "\n")

    def colors(self) -> list[tuple[str, list[str]]]:
        view = battito.load(self.state, NOW)
        return [(a.color, a.reasons) for a in view["tentativi"]]


OK = {"esito": "riuscito", "commit": True, "push": True, "permission_denials": 0}


class Semaphore(StateCase):
    def test_green_needs_explicit_no_attention(self):
        self.attempt("a", "2026-10-11T05:30:00+02:00", OK, "Fatto.\n\n**Attenzione:** nessuna")
        self.assertEqual(self.colors(), [("verde", [])])

    def test_missing_attention_line_is_yellow(self):
        self.attempt("a", "2026-10-11T05:30:00+02:00", OK, "Fatto.")
        self.assertEqual(self.colors()[0][0], "giallo")

    def test_attention_items_and_denials_are_yellow(self):
        close = {**OK, "permission_denials": 2}
        self.attempt("a", "2026-10-11T05:30:00+02:00", close, "Attenzione: foto da decidere")
        color, reasons = self.colors()[0]
        self.assertEqual(color, "giallo")
        self.assertIn("foto da decidere", reasons)

    def test_agent_cannot_lower_a_block(self):
        close = {"esito": "arresto", "motivo": "tree-sporco"}
        self.attempt("a", "2026-10-11T05:30:00+02:00", close, "Attenzione: nessuna")
        self.assertEqual(self.colors(), [("rosso", ["tree-sporco"])])

    def test_commit_without_push_is_red(self):
        close = {**OK, "push": False}
        self.attempt("a", "2026-10-11T05:30:00+02:00", close, "Attenzione: nessuna")
        self.assertEqual(self.colors()[0][0], "rosso")

    def test_open_attempt_turns_red_past_max_runtime(self):
        self.attempt("a", "2026-10-11T11:50:00+02:00", None)
        self.attempt("b", "2026-10-11T09:00:00+02:00", None)
        self.assertEqual([c for c, _ in self.colors()], ["in-corso", "rosso"])

    def test_missed_daily_start_is_red(self):
        self.decide({"state": "timer", "cadence": "*-*-*", "time": "05:30"})
        self.attempt("a", "2026-10-10T05:30:00+02:00", OK, "Attenzione: nessuna")
        view = battito.load(self.state, NOW)
        self.assertTrue(view["tentativi"][0].missed)
        self.assertEqual(view["tentativi"][0].color, "rosso")

    def test_manual_state_has_no_missed_start(self):
        self.attempt("a", "2026-10-01T05:30:00+02:00", OK, "Attenzione: nessuna")
        self.assertFalse(any(a.missed for a in battito.load(self.state, NOW)["tentativi"]))


class WithoutAttempts(StateCase):
    def test_no_state_declared(self):
        self.assertEqual(battito.load(None, NOW)["stato"], "none")

    def test_external(self):
        self.decide({"state": "esterno", "note": "fuori nixos (Task Scheduler)"})
        self.assertEqual(battito.load(self.state, NOW)["stato"], "external")

    def test_never_started(self):
        self.assertEqual(battito.load(self.state, NOW)["stato"], "never")

    def test_unreadable(self):
        self.assertEqual(battito.load(self.root / "assente", NOW)["stato"], "unreadable")


class Routes(StateCase):
    def test_latest_and_attempt_page(self):
        self.attempt("a", "2026-10-11T05:30:00+02:00", OK, "# Giro\n\n- uno\n\nAttenzione: nessuna")
        kind, body = battito.respond("/_battito/ultimi.json", self.state)
        self.assertTrue(kind.startswith("application/json"))
        self.assertEqual(json.loads(body)["tentativi"][0]["colore"], "verde")
        kind, body = battito.respond(f"/_battito/{ident('a')}", self.state)
        self.assertIn("<li>uno</li>", body.decode())

    def test_rejects_paths_outside_the_ids(self):
        self.assertIsNone(battito.respond("/_battito/../tentativi.jsonl", self.state))
        self.assertIsNone(battito.respond("/_battito/zzz.jsonl", self.state))

    def test_report_escapes_html(self):
        self.assertNotIn("<script>", battito.report_html("<script>x</script>"))


if __name__ == "__main__":
    unittest.main()
