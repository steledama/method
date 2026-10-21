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


class AuditTests(unittest.TestCase):
    def test_giro_denials_signs_and_calls(self):
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
                root, ".claude/skills/cycle/SKILL.md", "Compone `eval all`, poi esegui `/commit`.\n"
            )
            scrivi(
                root,
                ".claude/skills/eval/SKILL.md",
                "Lancia `git status --short` e `jq . x.json`.\n"
                "Non usare `git reset --hard`.\n"
                "Non usare `git add -A`.\n",
            )
            scrivi(root, ".claude/skills/commit/SKILL.md", "Committa.\n")
            scrivi(root, ".claude/skills/kb/SKILL.md", "Lancia `jq . y.json`.\n")
            report = MODULE.audit(root)
        self.assertIn("Skill del giro: commit, cycle, eval.", report)
        self.assertIn("eval:1 `jq . x.json` — non concesso nel giro", report)
        self.assertNotIn("kb:1", report)
        self.assertIn("eval:2 `git reset --hard` — negato in sessione", report)
        self.assertIn("eval:2 — con deny", report)
        self.assertIn("eval:3 — senza deny", report)
        self.assertIn("cycle → commit (riga 1)", report)


if __name__ == "__main__":
    unittest.main()
