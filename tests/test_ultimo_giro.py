"""Contratto del lettore dell'ultimo giro."""

import importlib.util
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

O3 = Path(__file__).resolve().parents[1] / "o3"


def carica(nome):
    import sys

    sys.path.insert(0, str(O3))
    spec = importlib.util.spec_from_file_location(nome, O3 / f"{nome}.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


U = carica("ultimo_giro")


class UltimoGiro(unittest.TestCase):
    def test_giro_con_esiti_e_ultimo_prossimo(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = {
                **os.environ,
                "GIT_AUTHOR_NAME": "t",
                "GIT_AUTHOR_EMAIL": "t@t",
                "GIT_COMMITTER_NAME": "t",
                "GIT_COMMITTER_EMAIL": "t@t",
            }

            def git(*a):
                subprocess.run(["git", *a], cwd=tmp, env=env, check=True, capture_output=True)

            git("init", "-q")
            git(
                "commit",
                "-q",
                "--allow-empty",
                "-m",
                "docs(ciclo): giro del 10/11",
                "-m",
                "Esiti: perceive=vuoto\nProssimo: Uno (confermato)",
            )
            git("commit", "-q", "--allow-empty", "-m", "docs(ciclo): runbook di sessione")
            git(
                "commit",
                "-q",
                "--allow-empty",
                "-m",
                "fix: altro",
                "-m",
                "Prossimo: Due (cambiato)",
            )
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                righe = U.ultimo(U.storia())
            finally:
                os.chdir(cwd)
        self.assertTrue(righe[0].endswith("docs(ciclo): giro del 10/11"))
        self.assertEqual(righe[1], "Esiti: perceive=vuoto")
        self.assertTrue(righe[2].startswith("Prossimo: Due (cambiato) ("))


if __name__ == "__main__":
    unittest.main()
