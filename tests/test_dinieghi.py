"""Contratti della ricorrenza dei dinieghi e dell'ultimo giro."""

import datetime as dt
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


D = carica("dinieghi")
U = carica("ultimo_giro")
ALLOW = ["git log*", "git status*", "ls *", "hostname", "cat *"]
DENY = ["python3 -c*", "ssh *"]
CO = Path("/home/stele/repo")


def classi(comando):
    return set(D.classi_bash(comando, CO, ALLOW, DENY))


class Classi(unittest.TestCase):
    def test_parentesi_solo_fuori_dalle_virgolette(self):
        self.assertEqual(classi("git log -1 --grep=^docs(ciclo) --format=%h"), {"parentesi"})
        self.assertEqual(classi("git log -1 --grep='^docs(ciclo)' --format=%h"), set())
        self.assertEqual(
            classi("git log --format=%(trailers:key=Prossimo,valueonly)"), {"parentesi"}
        )

    def test_backslash_e_graffe(self):
        self.assertIn("backslash", classi("git log --format=%h\\ %s"))
        self.assertIn("graffe", classi("ls kb/{a,b}.md"))
        self.assertNotIn("graffe", classi("ls 'kb/{a,b}.md'"))

    def test_composto_solo_con_un_pezzo_non_concesso(self):
        self.assertEqual(classi("git status && git log -1"), set())
        self.assertEqual(classi("git status && printenv X"), {"composto"})
        self.assertIn("cd-composto", classi("hostname; cd /home/stele/repo && git status"))

    def test_singolo_non_concesso_e_deny(self):
        self.assertEqual(classi("printenv X"), {"non-concesso"})
        self.assertIn("python3-c", classi("python3 -c 'print(1)'"))
        self.assertIn("non-concesso", classi("python3 -c 'print(1)'"))

    def test_sostituzione_heredoc_for_fuori_perimetro(self):
        self.assertIn("sostituzione", classi("cat $(ls)"))
        self.assertIn("heredoc", classi("cat <<EOF && ls"))
        self.assertNotIn("heredoc", classi("cat <<EOF"))
        self.assertIn("for", classi("for f in a b; do cat $f; done"))
        self.assertIn("fuori-perimetro", classi("git log /home/stele/altro"))
        self.assertNotIn("fuori-perimetro", classi("cat /home/stele/repo/x.md"))

    def test_mappa_dei_segnali_copre_ogni_classe(self):
        trovabili = {
            "composto",
            "for",
            "graffe",
            "python3-c",
            "heredoc",
            "fuori-perimetro",
            "sostituzione",
            "cd-composto",
            "parentesi",
            "backslash",
            "non-concesso",
        }
        self.assertEqual(set(D.SEGNALI), trovabili)
        for commit in filter(None, D.SEGNALI.values()):
            self.assertIsNotNone(D.data_commit(commit), commit)


class Ricorrenza(unittest.TestCase):
    def test_ricorre_in_due_giri_anche_di_repo_diversi(self):
        giorno = dt.date(2026, 11, 9)
        occorrenze = {
            "parentesi": [("uno", "g1", giorno), ("due", "g2", giorno)],
            "backslash": [("uno", "g1", giorno), ("uno", "g1", giorno)],
        }
        righe = D.rapporto(occorrenze, [], ["uno", "due"], [], {"uno": CO, "due": CO})
        testo = "\n".join(righe)
        self.assertIn("- parentesi: 2 giri, due, uno", testo)
        self.assertIn("segnale assente", testo)
        self.assertNotIn("backslash", testo)

    def test_finestra_sulle_chiusure_con_giro(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / "t.jsonl"
            righe = ['{"evento": "chiusura", "giro": null, "id": "a"}']
            righe += [f'{{"evento": "chiusura", "giro": "g", "id": "{i}"}}' for i in range(12)]
            f.write_text("\n".join(righe) + "\nnon json\n")
            self.assertEqual([v["id"] for v in D.giri(f, 3)], ["9", "10", "11"])


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
