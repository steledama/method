"""Contratti della lettura degli adottanti: elenco da world.md e interfaccia col canone."""

import importlib.util
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
            trovati = MODULE.adottanti(world)
        self.assertEqual(list(trovati), ["uno", "due"])
        self.assertEqual(trovati["due"], MODULE.HOME / "due")

    def test_checkout_found_by_origin_not_by_folder_name(self):
        import subprocess

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
            self.assertEqual(MODULE.assenti(world, home), ["altro"])

    def test_real_world_lists_checkouts_in_home(self):
        dichiarati = MODULE.dichiarati()
        self.assertIn("nixos", dichiarati)
        trovati = MODULE.adottanti()
        self.assertTrue(set(trovati) <= set(dichiarati))
        self.assertTrue(all(path.parent == MODULE.HOME for path in trovati.values()))

    def test_show_only_reads_the_canon_interface(self):
        for path in ("CLAUDE.md", "i3/allineamento-metodo.md", ".claude/skills/eval/SKILL.md"):
            self.assertTrue(MODULE.ammesso(path), path)
        for path in ("README.md", "i1/misure.md", ".claude/skills/../../i1/SKILL.md", ".env"):
            self.assertFalse(MODULE.ammesso(path), path)


class AuditTests(unittest.TestCase):
    def test_world_entries_carry_accent_and_view_address(self):
        voci = MODULE.voci()
        for nome in MODULE.adottanti():
            self.assertRegex(voci[nome], MODULE.ACCENTO, nome)
            self.assertRegex(voci[nome], MODULE.VISTA, nome)
        self.assertRegex(MODULE.di_metodo(), MODULE.VISTA)

    def test_plan_counts_only_table_rows(self):
        plan = (
            "| Ciclo | Ob. | Task | Dip. |\n| --- | --- | --- | --- |\n"
            "| dev | S | Uno | — |\n| runtime | 1 | Due | w1 |\n| runtime | 2 | Tre | — |\n"
            "Un dev in prosa non conta.\n"
        )
        self.assertEqual(MODULE.conteggio_plan(plan), (1, 2))

    def test_open_prescriptions_stop_before_procedures(self):
        indice = (
            "# Prescrizioni\n\n## Contenuti\n\n- [Una](una-cosa.md) — testo\n"
            "  che continua, cfr. [nodo](../kb/x.md)\n\n## Procedure\n\n- [Ingresso](ingresso.md)\n"
        )
        self.assertEqual(MODULE.prescrizioni_aperte(indice), ["una-cosa"])

    def test_cases_to_forward_from_body_and_index(self):
        file = {
            "i1/perceptions.md": (
                "Gli stati sono «da inoltrare» o «acquisita da method».\n\n"
                "- [Uno](uno.md) — caso; da inoltrare.\n"
                "- [Due](due.md) — caso; acquisita da method.\n"
            ),
            "i1/tre.md": "**Questione per il metodo.** Due punti, da inoltrare:\n",
            "i1/quattro.md": "Nessuno stato qui.\n",
            "i1/due.md": "Corpo rimasto com'era: da inoltrare.\n",
        }
        self.assertEqual(MODULE.casi_da_inoltrare(file), ["tre.md", "uno.md"])

    def test_repeated_accents_are_named(self):
        ripetuti = MODULE.accenti_ripetuti({"a": "#ABCDEF", "b": "#abcdef", "c": "#123456"})
        self.assertEqual(ripetuti, ["#abcdef in a, b"])

    def test_marker_line_spans_continuation_and_flags_satisfied(self):
        marker = (
            "- `esiti-per-stadio`: già\n  soddisfatta nei fork.\n"
            "- `altra`: in corso, punti 4-6\n  nel task.\nfuori\n"
        )
        riga = MODULE.riga_marker(marker, "esiti-per-stadio")
        self.assertEqual(riga, "`esiti-per-stadio`: già soddisfatta nei fork.")
        self.assertRegex(riga, MODULE.SODDISFATTA)
        self.assertNotRegex(MODULE.riga_marker(marker, "altra"), MODULE.SODDISFATTA)
        self.assertIsNone(MODULE.riga_marker(marker, "assente"))

    def test_frontmatter_reads_marker_fields(self):
        testo = "---\nmethod_commit: abc\nstatus: aligned\n---\n# Corpo: con due punti\n"
        self.assertEqual(MODULE.frontmatter(testo), {"method_commit": "abc", "status": "aligned"})


if __name__ == "__main__":
    unittest.main()
