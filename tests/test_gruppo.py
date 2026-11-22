"""Il sito di gruppo: membri dal world dell'istanza, home e rotte di serve.py.

Eseguire con python3 -m unittest discover -s tests.
"""

import json
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

BUILDERS = Path(__file__).resolve().parents[1] / "o3" / "view"
sys.path.insert(0, str(BUILDERS))

import gruppo
import serve

WORLD = """# World

Intro.

## Membri

- **[nixos](https://example.org/nixos)** — Configurazione degli host — checkout `~/nixos`
- **salute** — Benessere

## Altro

- **non-membro** — fuori sezione
"""


def publish(
    base: Path,
    name: str,
    title: str,
    accent: str = "#123456",
    deck: bool = False,
    members: list[dict] | None = None,
) -> None:
    folder = base / name / "releases" / "r1"
    (folder / "assets").mkdir(parents=True)
    (folder / "index.html").write_text(f'<title>{title}</title><a href="o1/plan.html">p</a>')
    (folder / "assets" / "theme.css").write_text(f":root {{\n  --accent: {accent};\n}}\n")
    (folder / "o1").mkdir()
    (folder / "o1" / "plan.html").write_text("piano")
    if deck:
        (folder / "presentation.html").write_text("deck")
    if members is not None:
        (folder / gruppo.FILE).write_text(json.dumps({"lingua": "it", "membri": members}))
    (base / name / "current").write_text("r1\n")
    (base / name / "status.json").write_text('{"ok": true}')


class Membri(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_sezione_letta(self):
        (self.root / "world.md").write_text(WORLD)
        members = gruppo.membri(self.root)
        self.assertEqual([m.nome for m in members], ["nixos", "salute"])
        self.assertEqual(members[0].descrizione, "Configurazione degli host")

    def test_voce_a_capo(self):
        (self.root / "world.md").write_text(
            "# W\n\n## Membri\n\n- **[salute](u)** — Salute del\n  custode —\n  checkout `~/salute`\n"
        )
        self.assertEqual(gruppo.membri(self.root)[0].descrizione, "Salute del custode")

    def test_senza_sezione_non_e_istanza(self):
        (self.root / "world.md").write_text("# World\n\nIntro.\n")
        self.assertIsNone(gruppo.membri(self.root))

    def test_sezione_vuota_caso_minimo(self):
        (self.root / "world.md").write_text("# World\n\nIntro.\n\n## Membri\n\nNessuno.\n")
        self.assertEqual(gruppo.membri(self.root), [])

    def test_doppione_rifiutato(self):
        (self.root / "world.md").write_text("# W\n\n## Membri\n\n- **a** — x\n- **a** — y\n")
        with self.assertRaises(SystemExit):
            gruppo.membri(self.root)

    def test_voce_senza_grassetto_rifiutata(self):
        (self.root / "world.md").write_text("# W\n\n## Membri\n\n- a — x\n")
        with self.assertRaises(SystemExit):
            gruppo.membri(self.root)


class Sito(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        publish(
            self.base,
            "casa",
            "Casa",
            "#db2777",
            members=[
                {"nome": "nixos", "descrizione": "Host"},
                {"nome": "salute", "descrizione": "Benessere"},
            ],
        )
        publish(self.base, "nixos", "NixOS", "#c2410c", deck=True)
        # `salute` è dichiarato ma non ancora pubblicato.
        handler = type("H", (serve.GroupHandler,), {"base": self.base, "istanza": "casa"})
        handler.log_message = lambda *args: None
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.tmp.cleanup()

    def get(self, path: str) -> tuple[int, str]:
        try:
            with urllib.request.urlopen(self.url + path) as response:
                return response.status, response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            error.close()
            return error.code, ""

    def test_home_elenca_istanza_e_membri(self):
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn('href="casa/"', body)
        self.assertIn('href="nixos/presentation.html"', body)
        self.assertIn("--accent: #c2410c", body)
        self.assertIn("non ancora pubblicato", body)
        self.assertNotIn('href="salute/"', body)
        self.assertNotIn("<iframe", body)

    def test_home_incorpora_la_chat(self):
        body = gruppo.home(self.base, "casa", "http://localhost:8100/")
        self.assertIn('<iframe src="http://localhost:8100/"', body)
        self.assertIn('href="http://localhost:8100/" target="_blank"', body)

    def test_vista_di_un_membro(self):
        self.assertEqual(self.get("/nixos/o1/plan.html"), (200, "piano"))
        self.assertEqual(self.get("/nixos/_stato"), (200, '{"ok": true}'))

    def test_rotte_fuori_dal_gruppo(self):
        self.assertEqual(self.get("/altro/")[0], 404)
        self.assertEqual(self.get("/salute/")[0], 404)
        # Un `..` resta confinato nella versione del membro, non sale alla base.
        self.assertEqual(self.get("/nixos/../casa/current")[0], 404)
        self.assertEqual(self.get("/nixos/../../casa/current")[0], 404)
        self.assertEqual(self.get("/nixos/.git/config")[0], 404)

    def test_prefisso_senza_barra_reindirizza(self):
        status, body = self.get("/nixos")
        self.assertEqual(status, 200)
        self.assertIn("NixOS", body)

    def test_istanza_sola(self):
        (self.base / "casa" / "releases" / "r1" / gruppo.FILE).unlink()
        status, body = self.get("/")
        self.assertEqual(status, 200)
        self.assertIn('href="casa/"', body)
        self.assertNotIn("nixos", body)
        self.assertEqual(self.get("/nixos/")[0], 404)


if __name__ == "__main__":
    unittest.main()
