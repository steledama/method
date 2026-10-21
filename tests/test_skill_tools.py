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

    def test_composite_needs_every_part(self):
        allow, deny = ["git status*", "ls *"], ["git reset*"]
        self.assertTrue(MODULE.concesso("git status && ls i1/", allow, deny))
        self.assertFalse(MODULE.concesso("git status; echo rc=$?", allow, deny))
        self.assertFalse(MODULE.concesso("git status && git reset --hard", allow + ["git *"], deny))

    def test_placeholders_and_scripts_without_interpreter(self):
        self.assertEqual(MODULE.parti("git -C <repo> log … | head"), ["git -C X log X", "head"])
        self.assertEqual(MODULE.parti("o3/kb_tools.py audit"), ["python3 o3/kb_tools.py audit"])


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
    def test_giro_from_declared_composition(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scrivi(
                root,
                ".claude/settings.json",
                json.dumps(
                    {"permissions": {"deny": ["Bash(git reset*)", "Bash(git push --force*)"]}}
                ),
            )
            scrivi(
                root,
                "o3/ciclo/permessi.json",
                json.dumps({"permissions": {"allow": ["Bash(git status*)"], "deny": []}}),
            )
            scrivi(
                root,
                ".claude/skills/cycle/SKILL.md",
                "---\nmetadata:\n  compone: eval commit\n---\n"
                "Esegui `/eval all`, poi `/commit`; il repo `method` non gira, né `/kb`.\n"
                "Lancia `/method` quando serve.\n",
            )
            scrivi(
                root,
                ".claude/skills/eval/SKILL.md",
                "Lancia `git status --short` e `jq . x.json`.\n"
                "Non usare `git reset --hard`.\n"
                "Non usare `git add -A`.\n"
                "Lavora senza `jq . y.json` e con `git -C <repo> log`.\n"
                "Poi esegui `/commit`.\n",
            )
            scrivi(root, ".claude/skills/commit/SKILL.md", "Committa.\n")
            scrivi(root, ".claude/skills/kb/SKILL.md", "Lancia `jq . z.json`.\n")
            scrivi(root, ".claude/skills/method/SKILL.md", "Recepisce.\n")
            report = MODULE.audit(root)
        self.assertIn("dalle composizioni dichiarate: commit, cycle, eval.", report)
        self.assertIn("eval:1 `jq . x.json` — non concesso nel giro", report)
        self.assertNotIn("kb:1", report)
        self.assertNotIn("eval:2 `git reset --hard`", report)
        self.assertNotIn("eval:4 `jq . y.json`", report)
        self.assertIn("eval:4 `git -C <repo> log` — non concesso nel giro", report)
        self.assertLess(report.index("### Modelli"), report.index("eval:4 `git -C <repo> log`"))
        self.assertIn("eval:2 — con deny", report)
        self.assertIn("eval:3 — deny non trovato nella stessa grafia", report)
        self.assertIn("cycle: composta che chiama skill non dichiarate → method (riga 6)", report)
        self.assertIn("eval: base che chiama altre skill → commit (riga 5)", report)

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
            scrivi(root, "o3/ciclo/prompt.md", "```\nProssimo: <task>\n```\n")
            report = MODULE.audit(root)
        self.assertIn("exec:5 `Prossimo: <task> (confermato; <riesame>)` — il gate", report)
        self.assertIn("o3/ciclo/prompt.md:2 `Prossimo: <task>` — il gate", report)
        self.assertNotIn("exec:2", report)
        self.assertNotIn("exec:3", report)
        self.assertNotIn("exec:4", report)

    def test_undeclared_cycle_checks_only_itself(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scrivi(root, "o3/ciclo/permessi.json", json.dumps({"permissions": {"allow": []}}))
            scrivi(root, ".claude/skills/cycle/SKILL.md", "Compone `eval all`.\n")
            scrivi(root, ".claude/skills/eval/SKILL.md", "Lancia `jq . x.json`.\n")
            report = MODULE.audit(root)
        self.assertIn("`cycle` non dichiara `metadata: compone:`", report)
        self.assertNotIn("eval:1", report)


if __name__ == "__main__":
    unittest.main()
