"""Contratti della lettura degli adottanti: elenco da world.md o dai membri di un gruppo."""

import importlib.util
import subprocess
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
            dichiarati = MODULE.dichiarati(world)
        self.assertEqual(list(dichiarati), ["uno", "due"])
        self.assertEqual(dichiarati["due"], (None, "due", "svezia"))

    def test_host_on_the_line_after_the_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            world = Path(tmp) / "world.md"
            world.write_text(
                "- **[lavoro](https://github.com/org/lavoro)** — Dominio — checkout `~/nixos`\n"
                "  su `svezia`; accento `#a16207`\n"
                "- **[capo](https://github.com/org/capo)** — Dominio — checkout\n"
                "  `~/capo` su `deck`\n",
                encoding="utf-8",
            )
            dichiarati = MODULE.dichiarati(world)
        self.assertEqual(dichiarati["lavoro"], ("org/lavoro", "nixos", "svezia"))
        self.assertEqual(dichiarati["capo"], ("org/capo", "capo", "deck"))

    def test_checkout_found_by_origin_not_by_folder_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            for cartella, url in (
                ("nixos", "git@github.com:org/lavoro.git"),
                ("nixos-casa", "https://github.com/io/casa"),
            ):
                subprocess.run(["git", "init", "-q", str(home / cartella)], check=True)
                subprocess.run(
                    ["git", "-C", str(home / cartella), "remote", "add", "origin", url], check=True
                )
            world = home / "world.md"
            world.write_text(
                "- **[casa](https://github.com/io/casa)** — checkout `~/nixos` su `deck`\n"
                "- **[lavoro](https://github.com/org/lavoro)** — checkout `~/nixos-lavoro` su `svezia`\n"
                "- **[altro](https://github.com/io/altro)** — checkout `~/altro` su `deck`\n",
                encoding="utf-8",
            )
            trovati = MODULE.adottanti(world, home)
            self.assertEqual(trovati, {"casa": home / "nixos-casa", "lavoro": home / "nixos"})
            self.assertEqual(MODULE.mancanti(world, home, "deck"), {"altro": MODULE.ASSENTE})

    def test_declared_on_another_host_is_outside_not_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            world = home / "world.md"
            world.write_text(
                "- **[lavoro](https://github.com/org/lavoro)** — checkout `~/nixos` su `svezia`\n"
                "- **[casa](https://github.com/io/casa)** — checkout `~/casa` su `deck`\n"
                "- **[libero](https://github.com/io/libero)** — checkout `~/libero`\n",
                encoding="utf-8",
            )
            self.assertEqual(MODULE.adottanti(world, home), {})
            self.assertEqual(
                MODULE.mancanti(world, home, "deck"),
                {"lavoro": MODULE.FUORI, "casa": MODULE.ASSENTE, "libero": MODULE.ASSENTE},
            )

    def test_instance_reads_only_its_members_and_itself(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            istanza = home / "capo"
            for cartella, url in (
                ("capo", "https://github.com/io/capo"),
                ("uno", "https://github.com/io/uno"),
                ("fuori", "https://github.com/io/fuori"),
            ):
                subprocess.run(["git", "init", "-q", str(home / cartella)], check=True)
                subprocess.run(
                    ["git", "-C", str(home / cartella), "remote", "add", "origin", url], check=True
                )
            world = istanza / "world.md"
            world.write_text(
                "# World\n\n- **[fuori](https://github.com/io/fuori)** — checkout `~/fuori`\n\n"
                "## Membri\n\n- **[uno](https://github.com/io/uno)** — Dominio —\n"
                "  checkout `~/uno` su `deck`\n- **[due](https://github.com/io/due)** —\n"
                "  checkout `~/due` su `svezia`\n\n## Superfici della membrana\n\n"
                "- **[altro](https://github.com/io/altro)** — checkout `~/altro`\n",
                encoding="utf-8",
            )
            trovati = MODULE.adottanti(world, home, istanza=istanza)
            self.assertEqual(trovati, {"capo": istanza, "uno": home / "uno"})
            self.assertEqual(MODULE.mancanti(world, home, "deck"), {"due": MODULE.FUORI})

    def test_shell_metacharacters_never_reach_git(self):
        self.assertFalse(MODULE.ammesso(".claude/skills/x&calc/SKILL.md"))
        self.assertTrue(MODULE.ammesso(".claude/skills/exec/SKILL.md"))
        with self.assertRaises(SystemExit):
            MODULE.main(["log", "nixos", "--ref", "HEAD&calc"])

    def test_real_world_lists_checkouts_in_home(self):
        dichiarati = MODULE.dichiarati()
        self.assertIn("nixos", dichiarati)
        trovati = MODULE.adottanti()
        self.assertTrue(set(trovati) <= set(dichiarati))
        self.assertTrue(all(c.parent == MODULE.HOME for c in trovati.values()))
        self.assertEqual(set(trovati) | set(MODULE.mancanti()), set(dichiarati))

    def test_show_only_reads_the_canon_interface(self):
        for path in ("CLAUDE.md", "i3/allineamento-metodo.md", ".claude/skills/eval/SKILL.md"):
            self.assertTrue(MODULE.ammesso(path), path)
        for path in ("README.md", "i1/misure.md", ".claude/skills/../../i1/SKILL.md", ".env"):
            self.assertFalse(MODULE.ammesso(path), path)


if __name__ == "__main__":
    unittest.main()
