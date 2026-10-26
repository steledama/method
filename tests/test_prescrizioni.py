"""Contratti della chiusura delle prescrizioni: marker recepito e voce d'indice."""

import importlib.util
import sys
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "prescrizioni", Path(__file__).resolve().parents[1] / "o3" / "prescrizioni.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PrescrizioniTests(unittest.TestCase):
    def test_marker_line_names_it_and_says_received(self):
        self.assertTrue(MODULE.recepita("- `uno` — diretta, recepita il 2026-10-26\n", "uno"))
        self.assertTrue(MODULE.recepita("  - `uno` (`789a324`): Recepita.\n", "uno"))
        self.assertFalse(MODULE.recepita("- `uno`: non recepita, in attesa\n", "uno"))
        self.assertFalse(MODULE.recepita("- `uno-due`: recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("- `uno` in lettura\n- `due` recepita\n", "uno"))

    def test_index_entry_removed_across_wrapped_lines(self):
        indice = (
            "## Contenuti\n\n"
            "- [Prima](prima.md) — resta.\n"
            "- [Seconda su\n"
            "  due righe](seconda.md) — se ne va,\n"
            "  anche la coda.\n"
            "- [Terza](terza.md) — resta.\n\n"
            "Chiusura.\n"
        )
        atteso = "## Contenuti\n\n- [Prima](prima.md) — resta.\n- [Terza](terza.md) — resta.\n\nChiusura.\n"
        self.assertEqual(MODULE.senza_voce(indice, "seconda"), atteso)
        self.assertIsNone(MODULE.senza_voce(indice, "quarta"))


if __name__ == "__main__":
    unittest.main()
