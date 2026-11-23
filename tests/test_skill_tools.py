"""Contratti del guardiano delle skill: permessi, comandi, divieti e chiamate."""

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "skill_tools", Path(__file__).resolve().parents[1] / "o3" / "skill_tools.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def scrivi(root: Path, rel: str, testo: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(testo, encoding="utf-8")


class PermessiTests(unittest.TestCase):
    def test_patterns_follow_prefix_semantics(self):
        self.assertTrue(MODULE.corrisponde("git add -u", "git add *"))
        self.assertTrue(MODULE.corrisponde("git add", "git add *"))
        self.assertTrue(MODULE.corrisponde("git status --short", "git status*"))
        self.assertTrue(MODULE.corrisponde("npm run test", "npm run:*"))
        self.assertFalse(MODULE.corrisponde("git push --force", "git push"))

    def test_composite_denied_by_any_part(self):
        deny = ["git reset*"]
        self.assertFalse(MODULE.negato("git status && ls i1/", deny))
        self.assertTrue(MODULE.negato("git status && git reset --hard", deny))

    def test_placeholders_and_scripts_without_interpreter(self):
        self.assertEqual(MODULE.parti("git -C <repo> log … | head"), ["git -C X log X", "head"])
        self.assertEqual(MODULE.parti("o3/kb_tools.py audit"), ["python3 o3/kb_tools.py audit"])

    def test_usage_forms_are_models_not_pipes(self):
        forma = "python3 o3/commit_gate.py prima|dopo [--perimetro]"
        self.assertEqual(MODULE.parti(forma), ["python3 o3/commit_gate.py primaXdopo X"])
        self.assertEqual(MODULE.tipo(forma, f"`{forma}`"), "modello")
        self.assertEqual(MODULE.parti("git log | head"), ["git log", "head"])


class EstrazioneTests(unittest.TestCase):
    def test_spans_with_arguments_and_code_blocks(self):
        righe = [
            "Leggi `kb/skill.md` e lancia `git status --short`.",
            "La parola `git` da sola non è un comando.",
            "```bash",
            "python3 o3/kb_tools.py audit",
            "```",
        ]
        self.assertEqual(
            MODULE.comandi(righe),
            [(1, "git status --short"), (4, "python3 o3/kb_tools.py audit")],
        )


class ClassificazioneTests(unittest.TestCase):
    def test_declared_composition_in_frontmatter(self):
        righe = ["---", "name: cycle", "metadata:", "  compone: eval, exec commit", "---", "x"]
        self.assertEqual(MODULE.composizione(righe), ["eval", "exec", "commit"])
        self.assertIsNone(MODULE.composizione(["---", "compone: eval", "---"]))
        self.assertIsNone(MODULE.composizione(["# senza frontmatter"]))

    def test_announcement_model_and_command(self):
        self.assertEqual(MODULE.tipo("git -C", "dal repo, senza `git -C`: i permessi"), "annuncio")
        riga = "un `echo rc=$?` aggiunto le fa negare tutte"
        self.assertEqual(MODULE.tipo("echo rc=$?", riga), "annuncio")
        riga = "Un giro senza file cambiati si chiude con `git commit --allow-empty`"
        self.assertEqual(MODULE.tipo("git commit --allow-empty", riga), "comando")
        riga = "`git -C <repo> log`"
        self.assertEqual(MODULE.tipo("git -C <repo> log", riga), "modello")
        riga = '`git -C "$method_repo" status`'
        self.assertEqual(MODULE.tipo('git -C "$method_repo" status', riga), "modello")


class AuditTests(unittest.TestCase):
    def test_next_task_examples_against_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            gate = Path(__file__).resolve().parents[1] / "o3" / "commit_gate.py"
            scrivi(root, "o3/commit_gate.py", gate.read_text(encoding="utf-8"))
            scrivi(
                root,
                ".claude/skills/exec/SKILL.md",
                "```\nProssimo: <task> (confermato)\nProssimo: nessuno (<motivo>)\n```\n"
                "Con `Prossimo: <task> (confermato; <riesame>)` nel commit.\n",
            )
            report = MODULE.audit(root)
        self.assertIn("exec:5 `Prossimo: <task> (confermato; <riesame>)` — il gate", report)
        self.assertNotIn("exec:2", report)
        self.assertNotIn("exec:3", report)
        self.assertNotIn("exec:4", report)

    def test_prose_binding_confirmation_reason_to_trailer(self):
        righe = [
            "- prossimo task, con la causa del cambio o il motivo della conferma",
            "  (stesso valore del trailer `Prossimo:`);",
            "- prossimo task nella forma del trailer; il motivo della conferma",
            "  sta nel corpo del commit, mai nel trailer;",
            "",
            "Il riesame di una conferma va nel corpo, non fra le parentesi del trailer.",
            "```",
            "motivo della conferma nel trailer",
            "```",
        ]
        self.assertEqual(MODULE.prosa_prossimo(righe), [1])

    def test_branches_beside_skill_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scrivi(
                root,
                ".claude/settings.json",
                json.dumps({"permissions": {"deny": ["Bash(git reset*)"]}}),
            )
            scrivi(
                root,
                ".claude/skills/cycle/SKILL.md",
                "---\nmetadata:\n  compone: exec\n---\nEsegui `/exec all`.\n",
            )
            scrivi(root, ".claude/skills/exec/SKILL.md", "Leggi `plan.md` se dovuto.\n")
            scrivi(
                root,
                ".claude/skills/exec/plan.md",
                "Lancia `jq . x.json`.\n"
                "Non usare `git add -A`.\n"
                "Poi esegui `/commit`.\n"
                "```\nProssimo: <task>\n```\n",
            )
            scrivi(root, ".claude/skills/commit/SKILL.md", "Committa.\n")
            report = MODULE.audit(root)
        self.assertIn("- exec: 1 righe; 6 nei file accanto", report)
        self.assertIn("exec/plan.md:2 — deny non trovato nella stessa grafia", report)
        self.assertIn("exec: base che chiama altre skill → commit (exec/plan.md:3)", report)

    def test_calls_mentions_and_instruction_surfaces(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scrivi(
                root,
                ".claude/settings.json",
                json.dumps({"permissions": {"deny": ["Bash(git reset*)"]}}),
            )
            scrivi(root, ".claude/skills/exec/SKILL.md", "Coda.\n")
            scrivi(
                root,
                ".claude/skills/commit/SKILL.md",
                "Se cambia il plan, usare `/exec plan`.\n"
                "Per la coda si\n"
                "lancia `/exec plan`.\n"
                "Nuovi task — `/exec plan`.\n",
            )
            scrivi(root, "CLAUDE.md", "Non usare `git push --force` né `git reset --hard`.\n")
            report = MODULE.audit(root)
        self.assertIn("commit: base che chiama altre skill → exec (riga 1), exec (riga 3)", report)
        self.assertIn("- commit: exec (riga 4)", report)
        self.assertIn("CLAUDE.md:1 — con deny", report)


if __name__ == "__main__":
    unittest.main()
