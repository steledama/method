"""Contratti del profilo: corpus, impronte e maturità; nessun giudizio simulato."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "kb_profile", Path(__file__).resolve().parents[1] / "o3" / "kb_profile.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
STATES = {"bozza", "iniziale", "maturo"}


class ProfileTests(unittest.TestCase):
    def test_frontmatter_not_body_and_invalid_states(self):
        state, issues = MODULE.maturity("# Nodo\n\nstato: maturo\n", STATES)
        self.assertIsNone(state)
        self.assertTrue(issues)
        self.assertEqual(
            MODULE.maturity("---\nstato: 'maturo' # commento\n---\n", STATES),
            ("maturo", []),
        )
        for header in ("stato: ignoto", "stato: bozza\nstato: maturo", "stato: [maturo]"):
            self.assertTrue(MODULE.maturity(f"---\n{header}\n---\n", STATES)[1])
        self.assertTrue(MODULE.maturity("---\nstato: maturo\n", STATES)[1])
        self.assertTrue(MODULE.maturity("---\nstato: iniziale\n---", {"bozza", "maturo"})[1])

    def test_corpus_excludes_catalog_hidden_and_symlinks(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            kb = root / "kb"
            kb.mkdir()
            (kb / "nested").mkdir()
            (kb / ".hidden").mkdir()
            text = "---\nstato: maturo\n---\n# Nodo\n"
            for name in ("a.md", "kb.md", ".hidden.md", ".hidden/x.md", "nested/b.md"):
                (kb / name).write_text(text)
            (kb / "alias.md").symlink_to(kb / "a.md")
            (kb / "outside").symlink_to(kb / "nested", target_is_directory=True)
            result = MODULE.profile(root, STATES)
            self.assertEqual(result["nodes_total"], 2)
            self.assertEqual(result["lines"], {"total": 8, "median": 4.0, "min": 4, "max": 4})
            self.assertEqual([n["path"] for n in result["manifest"]], ["kb/a.md", "kb/nested/b.md"])
            self.assertEqual(result["maturity"]["valid"], 2)
            original_hash = result["corpus_sha256"]
            (kb / "kb.md").write_text("catalogo diverso")
            self.assertEqual(MODULE.profile(root, STATES)["corpus_sha256"], original_hash)
            (kb / "a.md").write_text(text + "Nuova conoscenza\n")
            self.assertNotEqual(MODULE.profile(root, STATES)["corpus_sha256"], original_hash)

    def test_empty_and_missing_corpus(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            with self.assertRaises(ValueError):
                MODULE.profile(root, STATES)
            (root / "kb").mkdir()
            result = MODULE.profile(root, STATES)
            self.assertEqual(result["nodes_total"], 0)
            self.assertIsNone(result["lines"]["median"])


if __name__ == "__main__":
    unittest.main()
