"""Contratti della lettura del canone: intervallo dal cursore e cursore sconosciuto."""

import contextlib
import importlib.util
import io
import subprocess
import sys
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "canone", Path(__file__).resolve().parents[1] / "o3" / "canone.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def esegui(*argv: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        codice = MODULE.main(list(argv))
    return codice, out.getvalue(), err.getvalue()


class CanoneTests(unittest.TestCase):
    def test_distance_and_log_from_cursor(self):
        tre_fa = subprocess.run(
            ["git", "-C", str(MODULE.ROOT), "rev-parse", "HEAD~3"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        self.assertEqual(esegui("distanza", "--da", tre_fa), (0, "3\n", ""))
        codice, uscita, _ = esegui("log", "--da", tre_fa)
        self.assertEqual(codice, 0)
        self.assertGreaterEqual(sum(1 for r in uscita.splitlines() if not r.startswith(" ")), 3)

    def test_unknown_cursor_is_declared(self):
        codice, uscita, errore = esegui("distanza", "--da", "0" * 40)
        self.assertEqual(codice, 2)
        self.assertEqual(uscita, "")
        self.assertIn("non è un commit di method", errore)


if __name__ == "__main__":
    unittest.main()
