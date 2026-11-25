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
    status: dict | None = None,
    incipit: str | None = None,
) -> None:
    folder = base / name / "releases" / "r1"
    (folder / "assets").mkdir(parents=True)
    # Come prettier lo rende: il meta va a capo fra gli attributi.
    meta = f'<meta\n      name="description"\n      content="{incipit}"\n    />' if incipit else ""
    (folder / "index.html").write_text(f'{meta}<title>{title}</title><a href="o1/plan.html">p</a>')
    (folder / "assets" / "theme.css").write_text(f":root {{\n  --accent: {accent};\n}}\n")
    (folder / "o1").mkdir()
    (folder / "o1" / "plan.html").write_text("piano")
    if deck:
        (folder / "presentation.html").write_text("deck")
    if members is not None:
        (folder / gruppo.FILE).write_text(json.dumps({"lingua": "it", "membri": members}))
    (base / name / "current").write_text("r1\n")
    (base / name / "status.json").write_text(json.dumps(status or {"ok": True}))


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

    def test_campi_annidati_e_titolo(self):
        (self.root / "world.md").write_text(
            "# W\n\n## Membri\n\nTitolo: TT Artefatti\n\n"
            "- **bi** — Business Intelligence — checkout `~/bi`\n"
            "  - descrizione: Raccoglie i dati di vendita e li\n"
            "    rende consultabili.\n"
            "- **danea-auto** — Automazioni\n"
            "  - indirizzo: http://10.0.0.4:8001/\n"
            "- **gestionale** — Danea Easyfatt\n"
            "  - fuori metodo\n"
        )
        group = gruppo.gruppo(self.root)
        self.assertEqual(group.titolo, "TT Artefatti")
        bi, danea, gestionale = group.membri
        self.assertEqual(bi.descrizione, "Business Intelligence")
        self.assertEqual(bi.testo, "Raccoglie i dati di vendita e li rende consultabili.")
        self.assertEqual(danea.indirizzo, "http://10.0.0.4:8001/")
        self.assertFalse(danea.locale)
        self.assertTrue(gestionale.fuori)
        data = json.loads(gruppo.manifest(group, "it"))
        self.assertEqual(data["titolo"], "TT Artefatti")
        self.assertEqual(
            data["membri"][2],
            {"nome": "gestionale", "descrizione": "Danea Easyfatt", "fuori_metodo": True},
        )

    def test_campi_non_validi_rifiutati(self):
        for body in (
            "- **a** — x\n  - colore: rosso\n",
            "- **a** — x\n  - indirizzo: danea2:8001\n",
            "- **a** — x\n  - fuori metodo\n  - indirizzo: http://10.0.0.1/\n",
            "- **a** — x\n  - descrizione: uno\n  - descrizione: due\n",
            "- **a** — x\n\n  - descrizione: staccata\n",
        ):
            (self.root / "world.md").write_text("# W\n\n## Membri\n\n" + body)
            with self.subTest(body=body), self.assertRaises(SystemExit):
                gruppo.gruppo(self.root)

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
        self.assertEqual(json.loads(self.get("/nixos/_stato")[1]), {"ok": True})

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


class Schede(unittest.TestCase):
    """Titolo, coordinatore, versione servita, membri fuori metodo e remoti."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.servers = []

    def tearDown(self):
        for server in self.servers:
            server.shutdown()
            server.server_close()
        self.tmp.cleanup()

    def remote(self) -> str:
        """Un altro host che serve la propria vista pubblicata, come danea2."""
        other = self.base / "altrove"
        publish(
            other,
            "danea-auto",
            "Danea Auto",
            "#7e22ce",
            deck=True,
            incipit="Automatizza Easyfatt &amp; altro.",
            status={
                "ok": True,
                "served_commit": "c" * 40,
                "requested": "c" * 40,
                "served_date": "2026-11-20T09:00:00+01:00",
            },
        )
        handler = type("H", (serve.PublishedHandler,), {"root": other / "danea-auto"})
        handler.log_message = lambda *args: None
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.servers.append(server)
        return f"http://127.0.0.1:{server.server_address[1]}/"

    def test_home_completa(self):
        address = self.remote()
        publish(
            self.base,
            "nixos",
            "NixOS",
            "#a16207",
            members=[
                {"nome": "nixos", "descrizione": "Host", "testo": "Coordina il gruppo."},
                {"nome": "bi", "descrizione": "BI", "testo": "Raccoglie i dati di vendita."},
                {"nome": "danea-auto", "descrizione": "Automazioni", "indirizzo": address},
                {
                    "nome": "gestionale",
                    "descrizione": "Danea Easyfatt",
                    "testo": "Il gestionale.",
                    "fuori_metodo": True,
                },
                {"nome": "spento", "descrizione": "Giù", "indirizzo": "http://127.0.0.1:9/"},
            ],
            status={"ok": True, "served_commit": "a" * 40, "requested": "a" * 40},
        )
        (self.base / "nixos" / "releases" / "r1" / gruppo.FILE).write_text(
            json.dumps(
                {
                    "lingua": "it",
                    "titolo": "TT Artefatti",
                    "membri": json.loads(
                        (self.base / "nixos" / "releases" / "r1" / gruppo.FILE).read_text()
                    )["membri"],
                }
            )
        )
        publish(
            self.base,
            "bi",
            "BI",
            "#0f766e",
            incipit="Incipit del README di bi.",
            status={
                "ok": True,
                "served_commit": "b" * 40,
                "requested": "d" * 40,
                "served_date": "2026-11-25T10:08:17+01:00",
                "served_marker": {"method_version": "v0.4.0", "method_commit": "e" * 40},
            },
        )
        body = gruppo.home(self.base, "nixos")
        self.assertIn("<title>TT Artefatti</title>", body)
        self.assertIn('<span class="badge">coordinatore del gruppo</span>', body)
        self.assertEqual(body.count("Coordina il gruppo."), 1)
        self.assertLess(body.index("Coordina il gruppo."), body.index("Incipit del README"))
        # L'incipit pubblicato dalla vista vince sul testo dichiarato.
        self.assertIn("Incipit del README di bi.", body)
        self.assertNotIn("Raccoglie i dati di vendita.", body)
        self.assertIn("Automatizza Easyfatt &amp; altro.", body)
        self.assertIn("canone <code>v0.4.0</code>", body)
        self.assertIn("commit servito <code>bbbbbbb</code> · 2026-11-25", body)
        self.assertIn("richiesto ddddddd, non ancora servito", body)
        # Il membro remoto: link, deck e stato letti dal suo host.
        self.assertIn(f'href="{address}"', body)
        self.assertIn(f'href="{address}presentation.html"', body)
        self.assertIn("--accent: #7e22ce", body)
        self.assertIn("commit servito <code>ccccccc</code> · 2026-11-20", body)
        # Il membro fuori metodo: riquadro statico, nessun link.
        self.assertIn('<li class="member static">', body)
        self.assertIn('Danea Easyfatt <span class="outside">fuori metodo</span>', body)
        self.assertNotIn('href="gestionale/"', body)
        self.assertIn("stato non raggiungibile", body)
        self.assertEqual(gruppo.nomi(self.base, "nixos"), {"nixos", "bi"})


if __name__ == "__main__":
    unittest.main()
