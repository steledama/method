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

    def test_name_as_path_file_or_link(self):
        self.assertTrue(
            MODULE.recepita("`o3/uno.md` (v0.3.0) è recepita: host verificato\n", "uno")
        )
        self.assertTrue(MODULE.recepita("- `uno.md`: recepita\n", "uno"))
        self.assertTrue(MODULE.recepita("- [Uno](../method/o3/uno.md): recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("- `o3/uno-due.md`: recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("- [Due](o3/due-uno.md): recepita\n", "uno"))

    def test_wrapped_entry_is_read_whole(self):
        self.assertTrue(
            MODULE.recepita("La prescrizione `uno` (v0.3.0) è\nrecepita in `abc1234`.\n", "uno")
        )
        self.assertTrue(MODULE.recepita("- `uno`, letta con\n  `/method`: recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("La prescrizione `uno` è\n\nrecepita altrove.\n", "uno"))

    def test_negations_across_words_and_lines(self):
        self.assertFalse(MODULE.recepita("- `uno`: non\n  recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("- `uno` non risulta recepita\n", "uno"))
        self.assertFalse(MODULE.recepita("- `uno`: non ancora recepita\n", "uno"))
        self.assertTrue(MODULE.recepita("- `uno`: non era chiara, ora recepita\n", "uno"))

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

    def test_outside_host_follows_the_version_absent_stops(self):
        fuori = MODULE.FUORI
        self.assertTrue(MODULE.passa({"casa": True, "lavoro": fuori}))
        self.assertFalse(MODULE.passa({"casa": True, "lavoro": fuori, "salute": False}))
        self.assertFalse(MODULE.passa({"casa": True, "spento": "dichiarato qui, senza clone"}))

    def test_coordinator_verifies_but_never_closes(self):
        self.assertEqual(MODULE.main(["chiudi", "x", "--root", "."]), 2)


if __name__ == "__main__":
    unittest.main()
