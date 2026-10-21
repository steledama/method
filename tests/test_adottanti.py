"""Contratti della lettura degli adottanti: elenco da world.md e interfaccia col canone."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "adottanti", Path(__file__).resolve().parents[1] / "o3" / "adottanti.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AdottantiTests(unittest.TestCase):
    def test_world_entries_with_checkout_on_continuation_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            world = Path(tmp) / "world.md"
            world.write_text(
                "- **[uno](https://x/uno)** — Dominio — checkout `~/uno` su `deck`\n"
                "- **[due](https://x/due)** — Dominio lungo\n"
                "  ancora — checkout `~/due` su `svezia`; accento `#000`\n"
                "- **[tre](https://x/tre)** — senza checkout\n"
                "- `gdrive/` — checkout `~/fuori` non è un adottante\n",
                encoding="utf-8",
            )
            trovati = MODULE.adottanti(world)
        self.assertEqual(list(trovati), ["uno", "due"])
        self.assertEqual(trovati["due"], MODULE.HOME / "due")

    def test_real_world_lists_checkouts_in_home(self):
        trovati = MODULE.adottanti()
        self.assertIn("nixos", trovati)
        self.assertTrue(all(path.parent == MODULE.HOME for path in trovati.values()))

    def test_show_only_reads_the_canon_interface(self):
        for path in ("CLAUDE.md", "i3/allineamento-metodo.md", ".claude/skills/eval/SKILL.md"):
            self.assertTrue(MODULE.ammesso(path), path)
        for path in ("README.md", "i1/misure.md", ".claude/skills/../../i1/SKILL.md", ".env"):
            self.assertFalse(MODULE.ammesso(path), path)


if __name__ == "__main__":
    unittest.main()
