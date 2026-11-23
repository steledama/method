"""Contratti del gate di /commit: trailer e controlli del profilo."""

import contextlib
import importlib.util
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "commit_gate", Path(__file__).resolve().parents[1] / "o3" / "commit_gate.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TrailerTests(unittest.TestCase):
    def test_concordato_is_enough_and_impact_belongs_to_agent(self):
        self.assertEqual(MODULE.errori_trailer([("Autonomia", "concordato")]), [])
        self.assertTrue(MODULE.errori_trailer([]))
        self.assertTrue(MODULE.errori_trailer([("Autonomia", "concordato"), ("Impatto", "medio")]))

    def test_agent_needs_impact_and_reason(self):
        ok = [("Autonomia", "agente"), ("Impatto", "medio"), ("Impatto-motivo", "x")]
        self.assertEqual(MODULE.errori_trailer(ok), [])
        self.assertTrue(MODULE.errori_trailer(ok[:2]))
        self.assertTrue(MODULE.errori_trailer([("Autonomia", "agente"), ("Impatto", "forte")]))

    def test_outcomes_next_task_and_attribution(self):
        base = [("Autonomia", "concordato")]
        self.assertEqual(
            MODULE.errori_trailer([*base, ("Esiti", "plan=materia perform=vuoto")]), []
        )
        self.assertTrue(MODULE.errori_trailer([*base, ("Esiti", "plan=fatto")]))
        self.assertTrue(MODULE.errori_trailer([*base, ("Prossimo", "Task")]))
        self.assertEqual(
            MODULE.errori_trailer([*base, ("Prossimo", "Task (cambiato, era Altro; fonte)")]),
            [],
        )
        self.assertEqual(MODULE.errori_trailer([*base, ("Prossimo", "nessuno (coda vuota)")]), [])
        for motivato in ("Task (confermato; riesame)", "Task (confermato: riesame)"):
            self.assertIn(
                "(confermato) non prende motivo",
                MODULE.errori_trailer([*base, ("Prossimo", motivato)])[0],
            )
        self.assertTrue(MODULE.errori_trailer([*base, ("Co-Authored-By", "Qualcuno")]))


class ProssimoTests(unittest.TestCase):
    PLAN = """# Plan

| Ciclo | Ob. | Task   | Dip.    |
| ----- | --- | ------ | ------- |
| dev   | 1   | Atteso | w1      |
| dev   | S   | Primo  | —       |
| dev   | S   | Altro  | —       |
| dev   | S   | Dopo   | ↳ Primo |

`w1` = attesa.
"""

    def avvisi(self, prossimo, plan=PLAN):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            if plan is not None:
                (root / "o1").mkdir()
                (root / "o1" / "plan.md").write_text(plan, encoding="utf-8")
            return MODULE.avvisi_prossimo([("Prossimo", prossimo)], root)

    def test_first_ready_row_is_the_head(self):
        self.assertEqual(MODULE.prima_pronta(self.PLAN), "Primo")
        self.assertEqual(self.avvisi("Primo (confermato)"), [])
        self.assertEqual(self.avvisi("Primo (cambiato, era Altro; chiuso)"), [])

    def test_linked_task_cell_counts_as_its_text(self):
        plan = self.PLAN.replace("| Primo  |", "| [Primo](../o2/primo.md) |", 1)
        self.assertEqual(MODULE.prima_pronta(plan), "Primo")
        self.assertEqual(self.avvisi("Primo (confermato)", plan=plan), [])

    def test_skipping_the_head_warns(self):
        self.assertIn("scavalca", self.avvisi("Altro (confermato)")[0])
        self.assertTrue(
            self.avvisi(
                "Primo (confermato)",
                plan=self.PLAN.replace("| —       |", "| p1      |", 1),
            )
        )

    def test_none_and_missing_plan_are_silent(self):
        self.assertEqual(self.avvisi("nessuno (coda vuota)"), [])
        self.assertEqual(self.avvisi("Altro (confermato)", plan=None), [])

    def test_none_mixed_with_other_forms_warns(self):
        for misto in (
            "nessuno (confermato; riesame)",
            "nessuno (cambiato, era Primo; fonte)",
        ):
            self.assertIn("mescola le forme", self.avvisi(misto)[0])
            self.assertIn("mescola le forme", self.avvisi(misto, plan=None)[0])

    def test_next_task_outside_the_plan_warns(self):
        self.assertIn("nessuno (<motivo>)", self.avvisi("nessun task aperto (confermato)")[0])


class PrimaTests(unittest.TestCase):
    def test_checks_run_when_due_and_fail_on_declared_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / "o3").mkdir()
            (root / "o3" / "commit_gate.toml").write_text(
                "[[controllo]]\n"
                'comando = ["python3", "-c", "print(\'- 2 problemi strutturali\')"]\n'
                "fallisce_se = '^- [1-9]\\d* problemi'\n"
                "[[controllo]]\n"
                'quando = "kb/*"\n'
                'comando = ["python3", "-c", "raise SystemExit(1)"]\n',
                encoding="utf-8",
            )
            uscita = io.StringIO()
            with contextlib.redirect_stdout(uscita):
                esito = MODULE.prima(root)
        self.assertEqual(esito, 1)
        self.assertIn("FALLITO", uscita.getvalue())
        self.assertIn("non dovuto (kb/* invariato)", uscita.getvalue())

    def test_missing_check_command_fails_without_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / "o3").mkdir()
            (root / "o3" / "commit_gate.toml").write_text(
                '[[controllo]]\ncomando = ["comando-che-non-esiste-xyz"]\n',
                encoding="utf-8",
            )
            uscita = io.StringIO()
            with contextlib.redirect_stdout(uscita):
                esito = MODULE.prima(root)
        self.assertEqual(esito, 1)
        self.assertIn("non disponibile, FALLITO", uscita.getvalue())


FORMATTER = (
    "[[formatter]]\n"
    'glob = "*.md"\n'
    'comando = ["python3", "-c", '
    "\"import sys; [open(f, 'a').write('F') for f in sys.argv[1:]]\"]\n"
)


class PerimetroTests(unittest.TestCase):
    """Il gate non scrive sui file di un'altra sessione (proposta di economia, 2026-11-11)."""

    def setUp(self):
        temporanea = tempfile.TemporaryDirectory()
        self.addCleanup(temporanea.cleanup)
        self.root = Path(temporanea.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "o3").mkdir()
        (self.root / "o3" / "commit_gate.toml").write_text(FORMATTER, encoding="utf-8")
        git = [
            "git",
            "-C",
            str(self.root),
            "-c",
            "user.name=P",
            "-c",
            "user.email=p@example.org",
        ]
        subprocess.run([*git, "add", "-A"], check=True)
        subprocess.run([*git, "commit", "-q", "-m", "profilo"], check=True)
        (self.root / "mio.md").write_text("mio\n", encoding="utf-8")
        ambiente = patch.dict(os.environ)
        ambiente.start()
        self.addCleanup(ambiente.stop)
        os.environ.pop("GIT_REFLOG_ACTION", None)

    def prima(self, perimetro=None):
        uscita = io.StringIO()
        with contextlib.redirect_stdout(uscita):
            esito = MODULE.prima(self.root, perimetro)
        return esito, uscita.getvalue()

    def verifica(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return MODULE.verifica(self.root)

    def test_file_estraneo_ferma_senza_scrivere(self):
        (self.root / "altrui.md").write_text("altrui\n", encoding="utf-8")
        esito, uscita = self.prima(["mio.md"])
        self.assertEqual(esito, MODULE.FUORI_PERIMETRO)
        self.assertIn("altrui.md", uscita)
        self.assertEqual((self.root / "altrui.md").read_bytes(), b"altrui\n")
        self.assertEqual((self.root / "mio.md").read_bytes(), b"mio\n")

    def test_solo_il_perimetro_si_comporta_come_prima(self):
        esito, _ = self.prima(["./mio.md"])
        self.assertEqual(esito, 0)
        self.assertEqual((self.root / "mio.md").read_text(), "mio\nF")

    def test_il_perimetro_accetta_i_glob(self):
        (self.root / "i1").mkdir()
        (self.root / "i1" / "nota.md").write_text("n\n", encoding="utf-8")
        self.assertEqual(self.prima(["mio.md", "i1/*"])[0], 0)

    def test_fuori_da_un_giro_senza_perimetro_resta_com_era(self):
        (self.root / "altro.md").write_text("a\n", encoding="utf-8")
        self.assertEqual(self.prima()[0], 0)
        self.assertEqual((self.root / "altro.md").read_text(), "a\nF")

    def test_l_impronta_vede_un_file_cambiato_o_comparso_dopo_il_gate(self):
        self.assertEqual(self.prima(["mio.md"])[0], 0)
        self.assertEqual(self.verifica(), 0)
        (self.root / "altrui.md").write_text("altrui\n", encoding="utf-8")
        self.assertEqual(self.verifica(), MODULE.FUORI_PERIMETRO)
        (self.root / "altrui.md").unlink()
        self.assertEqual(self.verifica(), 0)
        (self.root / "mio.md").write_text("cambiato\n", encoding="utf-8")
        self.assertEqual(self.verifica(), MODULE.FUORI_PERIMETRO)

    def test_verifica_senza_impronta(self):
        self.assertEqual(self.verifica(), MODULE.FUORI_PERIMETRO)


if __name__ == "__main__":
    unittest.main()
