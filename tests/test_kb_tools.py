"""Il nucleo dell'audit KB lanciato dal canone su un altro repo.

Il repo di prova non copia `kb_tools.py`: dichiara un profilo
(`o3/kb_tools.toml`) e i controlli di dominio (`o3/kb_domain.py`).
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "o3" / "kb_tools.py"

NODE = "---\nstato: maturo\nmondo: {mondo}\n---\n\n# {name}\n\nConnessioni:\n\n- [{other}]({other}.md)\n"

DOMAIN = '''
def facts(root, core):
    """Un controllo che è codice: usa il nucleo col profilo applicato."""
    return {"nodi": len(core.doc_files(root)), "catalogo": core.CATALOG_NAME}


def inventory(root, core):
    return {"dominio": True}


def audit(root, core):
    return {"fatti": ["modulo senza nodo: rete"]}


COMMANDS = {"facts": facts, "inventory": inventory}
'''


def run(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(TOOL), "--root", str(root), *args],
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )


class KbToolsRootTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "kb").mkdir()
        (self.root / "o3").mkdir()
        for name, other, mondo in (("alfa", "beta", "casa"), ("beta", "alfa", "lavoro")):
            (self.root / "kb" / f"{name}.md").write_text(
                NODE.format(name=name, other=other, mondo=mondo), encoding="utf-8"
            )
        (self.root / "kb" / "indice.md").write_text(
            "# Indice\n\n- [alfa](alfa.md)\n- [beta](beta.md)\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def profile(self, text: str) -> None:
        (self.root / "o3" / "kb_tools.toml").write_text(text, encoding="utf-8")

    def audit(self) -> dict:
        result = run(self.root, "audit", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_verifica_il_repo_indicato_non_il_canone(self) -> None:
        self.assertEqual(self.audit()["total_nodes"], 3)

    def test_il_profilo_dichiara_catalogo_e_facet(self) -> None:
        self.profile(
            'catalog = "kb/indice.md"\n\n[facets.mondo]\nvalues = ["casa"]\nrequired = true\n'
        )
        data = self.audit()
        self.assertEqual(data["total_nodes"], 2)
        self.assertEqual(data["catalog_missing_nodes"], [])
        self.assertTrue(any("beta" in item for item in data["facet_violations"]))

    def test_chiave_sconosciuta_nel_profilo_ferma(self) -> None:
        self.profile('catalogo = "kb/indice.md"\n')
        result = run(self.root, "audit")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("catalogo", result.stderr)

    def test_il_dominio_aggiunge_comandi_e_sostituisce_inventory(self) -> None:
        self.profile('catalog = "kb/indice.md"\n')
        (self.root / "o3" / "kb_domain.py").write_text(DOMAIN, encoding="utf-8")
        facts = json.loads(run(self.root, "facts").stdout)
        self.assertEqual(facts, {"nodi": 2, "catalogo": "kb/indice.md"})
        self.assertEqual(json.loads(run(self.root, "inventory").stdout), {"dominio": True})
        self.assertIn("code_files_total", json.loads(run(self.root, "coverage").stdout))

    def test_i_controlli_di_dominio_entrano_nell_audit(self) -> None:
        (self.root / "o3" / "kb_domain.py").write_text(DOMAIN, encoding="utf-8")
        self.assertEqual(self.audit()["domain"], {"fatti": ["modulo senza nodo: rete"]})
        self.assertIn("[FATTI] modulo senza nodo: rete", run(self.root, "audit").stdout)

    def test_il_dominio_non_sostituisce_i_comandi_base(self) -> None:
        (self.root / "o3" / "kb_domain.py").write_text(
            "COMMANDS = {'audit': lambda root, core: {}}\n", encoding="utf-8"
        )
        result = run(self.root, "audit")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("audit", result.stderr)


if __name__ == "__main__":
    unittest.main()
