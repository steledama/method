"""Contratto del controllo di scadenze e ricorrenze (`kb/plan.md`)."""

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "o3" / "view"))

import sources  # noqa: E402

SPEC = importlib.util.spec_from_file_location("scadenze", ROOT / "o3" / "scadenze.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

ISO = MODULE.Profilo()
IT = MODULE.Profilo(formati=("iso", "it"))
OGGI = date(2026, 11, 8)


def ricorrenze(*righe):
    corpo = "\n".join(righe)
    return (
        "## Ricorrenze\n\n"
        "| Prossima | Cadenza | Esecutore | Ob. | Ricorrenza |\n"
        "| -------- | ------- | --------- | --- | ---------- |\n"
        f"{corpo}\n"
    )


class GrammaticaCondivisaTests(unittest.TestCase):
    def test_cadenze_e_legenda_coincidono_con_le_viste(self):
        self.assertEqual(set(MODULE.CADENZE), sources._CADENZE)
        self.assertEqual(MODULE.LEGENDA.pattern, sources._LEGEND_ENTRY.pattern)

    def test_prossima_coincide_con_le_viste(self):
        for caso in ["2027-11", "2026-12-01", "entro 2027-08-10", "config", "2027-1", "~2027-01"]:
            with self.subTest(caso):
                self.assertEqual(
                    bool(MODULE.PROSSIMA.fullmatch(caso)),
                    bool(sources._PROSSIMA.fullmatch(caso)),
                )


class ScadenzeTests(unittest.TestCase):
    def test_ogni_voce_e_una_data_o_un_rilievo(self):
        testo = (
            "## Scadenze\n\n"
            "Introduzione in prosa, che non è una voce.\n\n"
            "- **2026-11-01** — data piena.\n"
            "- **entro 2026-11-02** — con entro.\n"
            "- **2 novembre 2026** — illeggibile.\n"
            "- 2026-11-03 — senza grassetto.\n"
            "- 2026-11-04 → con la freccia.\n"
            "- **~2026-11-05** — col marcatore che il canone esclude.\n"
            "- **2027-13** — mese impossibile.\n"
            "- **2028-03-1** — giorno troncato.\n"
            "- export giornaliero senza data\n"
        )
        voci, rilievi = MODULE.leggi_scadenze(testo, ISO)
        self.assertEqual(
            [voce.data for voce in voci],
            [date(2026, 11, 1), date(2026, 11, 2), date(2026, 11, 3), date(2026, 11, 4)],
        )
        self.assertEqual(len(voci) + len(rilievi), 9)
        self.assertTrue(all(tipo == "RIGA_NON_RICONOSCIUTA" for tipo, _ in rilievi))
        self.assertIn("- **2 novembre 2026** — illeggibile.", [riga for _, riga in rilievi])

    def test_continuazioni_e_nota_nel_grassetto(self):
        testo = "## Scadenze\n\n- **2027-08-02 (annuale)** — Rinnovo\n  della polizza.\n"
        voci, rilievi = MODULE.leggi_scadenze(testo, ISO)
        self.assertEqual(voci[0].testo, "Rinnovo della polizza.")
        self.assertEqual(rilievi, [])

    def test_solo_mese_vale_il_suo_ultimo_giorno(self):
        voci, _ = MODULE.leggi_scadenze("## Scadenze\n\n- **2028-02** — Bollo.\n", ISO)
        self.assertEqual(voci[0].data, date(2028, 2, 29))
        self.assertEqual(voci[0].stato(date(2028, 2, 15), 45), "14 giorni")
        self.assertFalse(voci[0].scaduta(date(2028, 2, 29), 45))
        self.assertTrue(voci[0].scaduta(date(2028, 3, 1), 45))

    def test_ogni_data_passata_e_scaduta_anche_senza_entro(self):
        voci, _ = MODULE.leggi_scadenze("## Scadenze\n\n- **2026-11-01** — Appuntamento.\n", ISO)
        self.assertEqual(voci[0].stato(OGGI, 45), "SCADUTA")
        self.assertTrue(voci[0].scaduta(OGGI, 45))

    def test_fuori_ordine_e_un_rilievo_e_la_voce_resta(self):
        testo = "## Scadenze\n\n- **2026-12-01** — Dopo.\n- **2026-11-20** — Prima.\n"
        voci, rilievi = MODULE.leggi_scadenze(testo, ISO)
        self.assertEqual(len(voci), 2)
        self.assertEqual([tipo for tipo, _ in rilievi], ["FUORI_ORDINE"])

    def test_formato_it_solo_col_profilo(self):
        testo = (
            "## Scadenze\n\n"
            "- mer 9/12/26 9:00 — Ecografia.\n"
            "- entro 15/12/26 ⚠️ — Prelievi.\n"
            "- mar 12/1/27 15:30 — Visita.\n"
            "- entro nov 2027 — Controllo annuale.\n"
        )
        voci, rilievi = MODULE.leggi_scadenze(testo, IT)
        self.assertEqual(
            [voce.data for voce in voci],
            [date(2026, 12, 9), date(2026, 12, 15), date(2027, 1, 12), date(2027, 11, 30)],
        )
        self.assertEqual(rilievi, [])
        voci, rilievi = MODULE.leggi_scadenze(testo, ISO)
        self.assertEqual((len(voci), len(rilievi)), (0, 4))

    def test_marcatori_di_chiusura_del_profilo(self):
        profilo = MODULE.Profilo(marcatori_chiusura=("eseguito",))
        voci, _ = MODULE.leggi_scadenze(
            "## Scadenze\n\n- **2026-11-01** — Fatto: **Eseguito**.\n", profilo
        )
        self.assertEqual(voci[0].stato(OGGI, 45), "CHIUSA_DA_ARCHIVIARE")


class RicorrenzeTests(unittest.TestCase):
    def voce(self, riga):
        voci, rilievi, _ = MODULE.leggi_ricorrenze(ricorrenze(riga))
        self.assertEqual(rilievi, [])
        return voci[0]

    def test_config_contata_senza_data(self):
        voci, rilievi, config = MODULE.leggi_ricorrenze(
            ricorrenze("| config | quotidiano | scheduler | S | [Ciclo](a) |")
        )
        self.assertEqual((voci, rilievi, config), ([], [], 1))

    def test_righe_illeggibili_sono_rilievi(self):
        _, rilievi, _ = MODULE.leggi_ricorrenze(
            ricorrenze(
                "| quando capita | annuale | sessione | 4 | [Vaga](a) |",
                "| 2027-05 | ogni tanto | sessione | 4 | [Cadenza](a) |",
                "| 2027-13 | annuale | sessione | 4 | [Mese](a) |",
                "| 2027-05 | annuale | sessione |",
            )
        )
        self.assertEqual(len(rilievi), 4)

    def test_dovuta_poi_saltata_senza_toccare_l_uscita(self):
        voce = self.voce("| 2026-12-05 | mensile | sessione | 3 | [Finanze](a) |")
        self.assertEqual(voce.testo, "Finanze (mensile, sessione)")
        self.assertEqual(voce.stato(date(2026, 12, 1), 45), "4 giorni")
        self.assertEqual(voce.stato(date(2026, 12, 5), 45), "dovuta")
        self.assertEqual(voce.stato(date(2027, 1, 5), 45), "dovuta")
        self.assertEqual(voce.stato(date(2027, 1, 6), 45), "saltata (1)")
        self.assertEqual(voce.stato(date(2027, 2, 6), 45), "saltata (2)")
        self.assertFalse(voce.scaduta(date(2027, 2, 6), 45))

    def test_entro_passato_e_scaduto(self):
        voce = self.voce("| entro 2027-01 | annuale | sessione | 1 | [Bollo](a) |")
        self.assertFalse(voce.scaduta(date(2027, 1, 31), 45))
        self.assertEqual(voce.stato(date(2027, 2, 1), 45), "SCADUTA; dovuta")
        self.assertTrue(voce.scaduta(date(2027, 2, 1), 45))

    def test_solo_mese_resta_a_fine_mese_lungo_la_cadenza(self):
        voce = self.voce("| 2026-11 | mensile | sessione | 1 | [Giro](a) |")
        self.assertEqual(voce.stato(date(2026, 12, 31), 45), "dovuta")
        self.assertEqual(voce.stato(date(2027, 1, 1), 45), "saltata (1)")

    def test_giorno_limitato_al_mese_di_arrivo(self):
        voce = self.voce("| 2027-01-31 | mensile | sessione | 1 | [Giro](a) |")
        self.assertEqual(voce.stato(date(2027, 2, 28), 45), "dovuta")
        self.assertEqual(voce.stato(date(2027, 3, 1), 45), "saltata (1)")


class AtteseTests(unittest.TestCase):
    PLAN = (
        "## Task\n\n"
        "| Ciclo | Ob. | Task    | Dip. |\n"
        "| ----- | --- | ------- | ---- |\n"
        "| dev   | S   | Primo   | w1!  |\n"
        "| dev   | S   | Secondo | p2   |\n"
        "| dev   | S   | Terzo   | —    |\n\n"
        "- `w<n>` — attesa del mondo, definizione della legenda.\n"
        "- `w1` — causa. Risveglio: arrival: esito, via email; by:\n"
        "  2026-11-07.\n"
        "- **p2 · Secondo** — pausa; by: 2026-11.\n"
        "- `w3` — senza risveglio; by: 2027-01.\n"
        "- `p4` — senza termine.\n"
        "- `p5` — termine rotto; by: 2026-13.\n"
    )

    def test_finestre_leggono_le_colonne_per_nome(self):
        self.assertEqual(MODULE.finestre(self.PLAN), [("w1!", "Primo")])

    def test_entrambe_le_forme_di_legenda_e_le_continuazioni(self):
        trovate = {attesa.indice: attesa for attesa in MODULE.attese(self.PLAN)}
        self.assertEqual(set(trovate), {"w1", "p2", "w3", "p4", "p5"})
        self.assertEqual(trovate["w1"].by, date(2026, 11, 7))
        self.assertEqual(trovate["w1"].task, "Primo")

    def test_by_col_solo_mese_vale_l_ultimo_giorno(self):
        trovate = {attesa.indice: attesa for attesa in MODULE.attese(self.PLAN)}
        self.assertEqual(trovate["p2"].by, date(2026, 11, 30))

    def test_rilievi_di_chiosa(self):
        trovate = {attesa.indice: attesa for attesa in MODULE.attese(self.PLAN)}
        self.assertEqual(trovate["w3"].rilievo(), "SENZA_PROBE_NE_ARRIVAL")
        self.assertEqual(trovate["p4"].rilievo(), "SENZA_BY")
        self.assertEqual(trovate["p5"].rilievo(), "BY_NON_VALIDO")

    def test_riesame_solo_a_termine_passato_e_senza_scaduta(self):
        uscita, scaduta = MODULE.rapporto(self.PLAN, ISO, date(2026, 11, 7), 45)
        self.assertNotIn("RIESAME", uscita)
        uscita, scaduta = MODULE.rapporto(self.PLAN, ISO, OGGI, 45)
        self.assertIn("RIESAME — w1 — by 2026-11-07 — Primo", uscita)
        self.assertNotIn("RIESAME — p2", uscita)
        self.assertFalse(scaduta)

    def test_by_in_arrivo_entra_nella_catena_senza_scaduta(self):
        uscita, scaduta = MODULE.rapporto(self.PLAN, ISO, date(2026, 11, 5), 45)
        self.assertIn("- riesame fra 2 giorni — 2026-11-07 — w1 · Primo", uscita)
        self.assertIn("- riesame fra 25 giorni — 2026-11-30 — p2 · Secondo", uscita)
        self.assertNotIn("2027-01-31", uscita)
        self.assertFalse(scaduta)

    def test_by_di_oggi_e_in_catena_e_non_ancora_riesame_passato(self):
        uscita, _ = MODULE.rapporto(self.PLAN, ISO, date(2026, 11, 7), 45)
        self.assertIn("- riesame oggi — 2026-11-07 — w1 · Primo", uscita)
        self.assertNotIn("RIESAME — w1", uscita)

    def test_by_in_arrivo_segue_l_ordine_cronologico(self):
        plan = self.PLAN + "\n## Scadenze\n\n- **2026-11-20** — Mondo.\n"
        uscita, _ = MODULE.rapporto(plan, ISO, date(2026, 11, 5), 45)
        self.assertLess(uscita.index("w1 · Primo"), uscita.index("Mondo"))
        self.assertLess(uscita.index("Mondo"), uscita.index("p2 · Secondo"))

    def test_finestre_stampate_senza_condizione_di_distanza(self):
        uscita, _ = MODULE.rapporto(self.PLAN, ISO, date(2030, 1, 1), 1)
        self.assertIn("- w1! — Primo", uscita)


class MainTests(unittest.TestCase):
    def lancia(self, plan, profilo=None):
        with tempfile.TemporaryDirectory() as cartella:
            root = Path(cartella)
            (root / "plan.md").write_text(plan, encoding="utf-8")
            (root / "scadenze.toml").write_text(profilo or "", encoding="utf-8")
            uscita, errori = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(uscita), contextlib.redirect_stderr(errori):
                codice = MODULE.main(
                    [
                        "--plan",
                        str(root / "plan.md"),
                        "--profilo",
                        str(root / "scadenze.toml"),
                        "--today",
                        "2026-11-08",
                    ]
                )
            return codice, uscita.getvalue()

    def test_uscita_zero_e_conteggio_anche_senza_voci_in_finestra(self):
        codice, uscita = self.lancia(ricorrenze("| 2027-11 | annuale | sessione | 2 | [Seed](a) |"))
        self.assertEqual(codice, 0)
        self.assertIn("Nessuna voce entro 45 giorni", uscita)
        self.assertIn("Lette: 1 voci datate, 0 config, 0 non riconosciute.", uscita)

    def test_uscita_uno_solo_per_le_scadute(self):
        codice, _ = self.lancia("## Scadenze\n\n- **2026-11-01** — Passata.\n")
        self.assertEqual(codice, 1)
        codice, uscita = self.lancia("## Scadenze\n\n- boh — illeggibile.\n")
        self.assertEqual(codice, 0)
        self.assertIn("RIGA_NON_RICONOSCIUTA — - boh — illeggibile.", uscita)

    def test_catena_cronologica_unisce_le_sezioni(self):
        plan = "## Scadenze\n\n- **2026-11-20** — Mondo.\n\n" + ricorrenze(
            "| 2026-11-10 | mensile | sessione | 1 | [Nostra](a) |"
        )
        _, uscita = self.lancia(plan)
        self.assertLess(uscita.index("Nostra"), uscita.index("Mondo"))

    def test_uscita_due_per_profilo_invalido_o_plan_assente(self):
        for profilo in ["ignota = 1\n", 'formati_data = ["klingon"]\n', "= rotto"]:
            with self.subTest(profilo):
                self.assertEqual(self.lancia("## Scadenze\n", profilo)[0], 2)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(MODULE.main(["--plan", "/inesistente/plan.md"]), 2)


if __name__ == "__main__":
    unittest.main()
