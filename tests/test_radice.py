"""I builder del canone lanciati su un altro repo con `--root`.

Il repo di prova ha in `o3/view/` il solo `project.py`: è la forma
dell'adottante che non copia i builder. Usa Pandoc e Prettier come la build.
"""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CANON = Path(__file__).resolve().parents[1]
BUILD = CANON / "o3" / "view" / "build.py"

PROJECT = """SIGLA = "Prova"
LINGUA = "it"
ACCENTO = "#123456"
DESCRIZIONI = {"i1": "Catture del dominio di prova."}
DECK = None
DECK_BUILDER = None
CSS_LOCALI = []
ESCLUSE = []
"""

FILES = {
    "README.md": "# Repo di prova\n",
    "goal.md": "# Goal\n\nIntro.\n\n## Obiettivi runtime\n\n### 1. Primo\n\nTesto.\n",
    "world.md": "# World\n\nIntro.\n",
    "o1/plan.md": "# Plan\n\n| Ciclo | Ob. | Task | Dip. |\n| --- | --- | --- | --- |\n",
    "o2/tasks.md": "# Task\n",
    "o3/prescriptions.md": "# Prescriptions\n",
    "o3/view/project.py": PROJECT,
    "i1/perceptions.md": "# Perceptions\n",
    "i2/interpretations.md": "# Interpretazioni\n",
    "i3/verdicts.md": "# Verdetti\n",
}


def build(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(BUILD), *args],
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )


@unittest.skipUnless(shutil.which("pandoc") and shutil.which("prettier"), "serve il toolchain")
class RootTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        for relative, text in FILES.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_rende_il_repo_indicato_con_la_sua_identita(self) -> None:
        result = build("--root", str(self.root))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        home = (self.root / "view" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Prova · Repo di prova", home)
        self.assertIn("Catture del dominio di prova.", home)
        theme = (self.root / "view" / "assets" / "theme.css").read_text(encoding="utf-8")
        self.assertIn("#123456", theme)
        self.assertTrue((self.root / "view" / "assets" / "page.css").exists())

    def test_la_provenienza_dichiara_il_canone(self) -> None:
        out = Path(self.tmp.name) / "out"
        result = build(
            "--root", str(self.root), "--out", str(out), "--commit", "c" * 40, "--canon", "d" * 40
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"canon": "' + "d" * 40, (out / "provenance.json").read_text("utf-8"))
        self.assertIn("method dddddddddddd", (out / "index.html").read_text("utf-8"))

    def test_senza_identita_si_ferma(self) -> None:
        (self.root / "o3" / "view" / "project.py").unlink()
        result = build("--root", str(self.root), "--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("project.py", result.stderr)

    def test_una_copia_dei_builder_accanto_ferma_la_build(self) -> None:
        (self.root / "o3" / "view" / "sources.py").write_text("", encoding="utf-8")
        result = build("--root", str(self.root), "--check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("sources.py", result.stderr)


if __name__ == "__main__":
    unittest.main()
