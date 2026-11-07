"""Contratti delle copie tradotte: sorgente, `fonte:` e ritardo non bloccante."""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "traduzioni", Path(__file__).resolve().parents[1] / "o3" / "traduzioni.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def blob(path: Path) -> str:
    return subprocess.run(
        ["git", "hash-object", str(path)], capture_output=True, text=True, check=True
    ).stdout.strip()


class TraduzioniTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "kb").mkdir()
        self.src = self.root / "kb" / "node.md"
        self.src.write_text("# Node\n\nCanonical text.\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def twin(self, fonte: str | None) -> Path:
        path = self.root / "kb" / "node.it.md"
        head = f"---\nfonte: {fonte}\n---\n\n" if fonte else ""
        path.write_text(head + "# Node\n\nTesto.\n", encoding="utf-8")
        return path

    def test_source_of_twin(self):
        self.assertEqual(MODULE.sorgente(Path("kb/node.it.md")), Path("kb/node.md"))
        self.assertIsNone(MODULE.sorgente(Path("kb/node.md")))
        self.assertIsNone(MODULE.sorgente(Path("kb/kb-tools.md")))

    def test_aligned_twin_passes(self):
        self.twin(blob(self.src))
        self.assertEqual(MODULE.verifica(self.root), ([], []))

    def test_changed_source_is_delay_not_error(self):
        self.twin(blob(self.src))
        self.src.write_text("# Node\n\nCanonical text, revised.\n", encoding="utf-8")
        errori, ritardi = MODULE.verifica(self.root)
        self.assertEqual(errori, [])
        self.assertEqual(len(ritardi), 1)

    def test_missing_fonte_and_orphan_are_errors(self):
        self.twin(None)
        (self.root / "kb" / "gone.it.md").write_text("---\nfonte: x\n---\n", encoding="utf-8")
        errori, _ = MODULE.verifica(self.root)
        self.assertEqual(len(errori), 2)


if __name__ == "__main__":
    unittest.main()
