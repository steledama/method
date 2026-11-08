"""Contratto del lanciatore: arresti, tracce, tetto e rete in chiusura.

L'agente è un eseguibile finto, i repository sono veri e temporanei: nessun
`claude` reale parte da questi test.
"""

import importlib.util
import json
import ntpath
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "o3" / "lanciatore.py"
SPEC = importlib.util.spec_from_file_location("lanciatore", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

RISULTATO = (
    '{"type":"result","is_error":false,"total_cost_usd":1.5,"num_turns":7,"duration_ms":900,'
    '"result":"Fatto.\\n\\nAttenzione: niente da segnalare",'
    '"permission_denials":[{"tool_name":"Bash","tool_input":{"command":"ls {a,b}"}}]}'
)


def agente(corpo: str) -> str:
    return f'#!/bin/sh\necho "$@" > .git/argomenti\n{corpo}\n'


OK = agente(f"echo '{RISULTATO}'")


@unittest.skipIf(os.name == "nt", "repository e agente finti in shell POSIX")
class LanciatoreTests(unittest.TestCase):
    def setUp(self):
        temporanea = tempfile.TemporaryDirectory()
        self.addCleanup(temporanea.cleanup)
        self.base = Path(temporanea.name)
        self.origin = self.base / "origin.git"
        self.repo = self.base / "repo"
        self.env = {
            **os.environ,
            "HOME": str(self.base),
            "GIT_CONFIG_GLOBAL": str(self.base / "gitconfig"),
            "GIT_CONFIG_NOSYSTEM": "1",
        }
        self.env.pop("INVOCATION_ID", None)
        (self.base / "gitconfig").write_text(
            "[user]\n\tname = Prova\n\temail = prova@example.org\n[init]\n\tdefaultBranch = main\n",
            encoding="utf-8",
        )
        self.sh("git", "init", "-q", "--bare", str(self.origin), cwd=self.base)
        self.sh("git", "init", "-q", str(self.repo), cwd=self.base)
        (self.repo / ".gitignore").write_text("i1/giri/\n", encoding="utf-8")
        (self.repo / "o3" / "ciclo").mkdir(parents=True)
        (self.repo / "o3" / "ciclo" / "prompt.md").write_text("Fai il giro.\n", encoding="utf-8")
        (self.repo / "o3" / "ciclo" / "permessi.json").write_text(
            '{"permissions": {"allow": ["Read(./**)"]}}\n', encoding="utf-8"
        )
        self.committa("inizio")
        self.sh("git", "remote", "add", "origin", str(self.origin))
        self.sh("git", "push", "-q", "-u", "origin", "main")
        self.imposta_agente(OK)

    def sh(self, *comando, cwd=None):
        return subprocess.run(
            comando, cwd=cwd or self.repo, env=self.env, capture_output=True, text=True, check=True
        ).stdout.strip()

    def committa(self, messaggio):
        self.sh("git", "add", "-A")
        self.sh("git", "commit", "-q", "-m", messaggio)

    def imposta_agente(self, testo):
        self.claude = self.base / "claude-finto"
        self.claude.write_text(testo, encoding="utf-8")
        self.claude.chmod(0o755)

    def lancia(self, *argomenti, env=None):
        return subprocess.run(
            [*self.comando(), *argomenti],
            cwd=self.repo,
            env={**self.env, **(env or {})},
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )

    def comando(self):
        # Senza l'opzione un test aggiornerebbe il vero checkout del canone.
        return [
            sys.executable,
            str(SCRIPT),
            "--claude",
            str(self.claude),
            "--senza-pull-canone",
        ]

    def righe(self):
        testo = (self.repo / "i1" / "giri" / "tentativi.jsonl").read_text(encoding="utf-8")
        return [json.loads(riga) for riga in testo.splitlines()]

    def chiusura(self):
        return self.righe()[-1]

    def assert_arresto(self, codice, motivo):
        esito = self.lancia()
        self.assertEqual(esito.returncode, codice, esito.stderr)
        chiusura = self.chiusura()
        self.assertEqual(chiusura["motivo"], motivo)
        self.assertEqual(chiusura["esito"], "arresto")
        self.assertEqual(chiusura["exit_status"], str(codice))
        self.assertFalse((self.repo / ".git" / "argomenti").exists())

    def test_giro_riuscito_con_le_tracce_che_la_vista_legge(self):
        self.imposta_agente(
            agente(
                "echo fatto > nota.md\ngit add -A\ngit commit -q -m 'docs: giro'\ngit push -q\n"
                f"echo '{RISULTATO}'"
            )
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 0, esito.stderr)
        partenza, chiusura = self.righe()
        self.assertEqual(partenza["evento"], "partenza")
        self.assertEqual(partenza["id"], chiusura["id"])
        self.assertEqual(partenza["branch"], "main")
        self.assertEqual(chiusura["esito"], "riuscito")
        self.assertIsNone(chiusura["motivo"])
        self.assertTrue(chiusura["commit"])
        self.assertTrue(chiusura["push"])
        self.assertEqual(chiusura["oggetto"], "docs: giro")
        self.assertFalse(chiusura["tree_sporco_dopo"])
        self.assertEqual(chiusura["costo_usd"], 1.5)
        self.assertEqual(chiusura["turni"], 7)
        self.assertEqual(chiusura["attenzione"], "niente da segnalare")
        self.assertEqual(chiusura["dinieghi"], [{"tool": "Bash", "input": "ls {a,b}"}])
        ultimo = json.loads((self.repo / "i1" / "giri" / "ultimo.json").read_text(encoding="utf-8"))
        self.assertEqual(ultimo, chiusura)
        self.assertTrue(Path(chiusura["giro"]).is_file())

    def test_argomenti_dell_agente_e_attribuzione_vuota(self):
        self.assertEqual(self.lancia().returncode, 0)
        argomenti = (self.repo / ".git" / "argomenti").read_text(encoding="utf-8")
        self.assertIn("-p Fai il giro.", argomenti)
        self.assertIn("--setting-sources project", argomenti)
        self.assertIn("--permission-mode dontAsk", argomenti)
        self.assertIn("--max-budget-usd 5", argomenti)
        impostazioni = json.loads((self.repo / ".git/lanciatore/settings.json").read_text())
        self.assertEqual(impostazioni["attribution"], {"commit": "", "pr": ""})
        self.assertEqual(impostazioni["permissions"]["allow"], ["Read(./**)"])

    def test_tree_sporco(self):
        (self.repo / "sporco.md").write_text("x\n", encoding="utf-8")
        self.assert_arresto(10, "checkout-sporco")

    def test_branch_inatteso(self):
        self.sh("git", "switch", "-q", "-c", "altro")
        self.assert_arresto(11, "branch-inatteso")

    def test_senza_upstream(self):
        self.sh("git", "branch", "--unset-upstream")
        self.assert_arresto(11, "upstream-mancante")

    def altro_clone(self):
        clone = self.base / "clone"
        self.sh("git", "clone", "-q", str(self.origin), str(clone), cwd=self.base)
        return clone

    def spingi_dal_clone(self, percorso="altro.md"):
        clone = self.altro_clone()
        destinazione = clone / percorso
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        destinazione.write_text("altro\n", encoding="utf-8")
        self.sh("git", "add", "-A", cwd=clone)
        self.sh("git", "commit", "-q", "-m", "da altrove", cwd=clone)
        self.sh("git", "push", "-q", cwd=clone)
        return self.sh("git", "rev-parse", "HEAD", cwd=clone)

    def test_divergente(self):
        self.spingi_dal_clone()
        (self.repo / "mio.md").write_text("x\n", encoding="utf-8")
        self.committa("locale")
        self.assert_arresto(12, "branch-divergente")

    def test_indietro_si_fa_il_pull_anche_sui_percorsi_protetti(self):
        testa = self.spingi_dal_clone("o3/ciclo/prompt.md")
        esito = self.lancia()
        self.assertEqual(esito.returncode, 0, esito.stderr)
        chiusura = self.chiusura()
        self.assertEqual(chiusura["head_prima"], testa)
        self.assertEqual(chiusura["esito"], "riuscito")

    def con_pull_fermo(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            'pull_fermo = ["o3/runtime/*", "o3/scheduler/*"]\n', encoding="utf-8"
        )
        self.committa("profilo")
        self.sh("git", "push", "-q")
        return self.sh("git", "rev-parse", "HEAD")

    def test_pull_che_tocca_la_produzione_resta_al_custode(self):
        testa = self.con_pull_fermo()
        self.spingi_dal_clone("o3/runtime/export.ahk")
        self.assert_arresto(17, "pull-fermo")
        self.assertEqual(self.sh("git", "rev-parse", "HEAD"), testa)

    def test_pull_che_non_tocca_la_produzione_procede(self):
        self.con_pull_fermo()
        testa = self.spingi_dal_clone("kb/nodo.md")
        self.assertEqual(self.lancia().returncode, 0)
        self.assertEqual(self.chiusura()["head_prima"], testa)

    def test_fetch_fallito(self):
        self.sh("git", "remote", "set-url", "origin", str(self.base / "non-esiste.git"))
        self.assert_arresto(13, "fetch-fallito")

    def test_prompt_mancante(self):
        (self.repo / "o3" / "ciclo" / "prompt.md").unlink()
        self.committa("via il prompt")
        self.assert_arresto(14, "prompt-mancante")

    def test_permessi_invalidi(self):
        (self.repo / "o3" / "ciclo" / "permessi.json").write_text("{rotto", encoding="utf-8")
        self.committa("permessi rotti")
        self.assert_arresto(14, "settings-invalide")

    def test_giri_non_ignorata_non_sporca_il_tree(self):
        (self.repo / ".gitignore").write_text("", encoding="utf-8")
        self.committa("niente ignore")
        esito = self.lancia()
        self.assertEqual(esito.returncode, 14)
        self.assertIn("giri-non-ignorati", esito.stderr)
        self.assertFalse((self.repo / "i1").exists())

    def test_profilo_con_chiave_sconosciuta(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            "ignota = 1\n", encoding="utf-8"
        )
        self.committa("profilo")
        esito = self.lancia()
        self.assertEqual(esito.returncode, 14)
        self.assertIn("chiavi sconosciute", esito.stderr)

    def test_agente_uscito_con_errore(self):
        self.imposta_agente(agente("exit 3"))
        esito = self.lancia()
        self.assertEqual(esito.returncode, 20)
        chiusura = self.chiusura()
        self.assertEqual(
            (chiusura["esito"], chiusura["motivo"]), ("errore", "claude-uscita-non-zero")
        )
        self.assertEqual(chiusura["claude_exit"], 3)

    def test_errore_riportato_o_risultato_assente(self):
        for corpo in ['echo \'{"type":"result","is_error":true}\'', "echo niente"]:
            with self.subTest(corpo):
                self.imposta_agente(agente(corpo))
                self.assertEqual(self.lancia().returncode, 21)
                self.assertEqual(self.chiusura()["motivo"], "claude-errore")

    def test_tetto_di_tempo_chiude_l_albero_dei_processi(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            "minuti = 0.01\n", encoding="utf-8"
        )
        self.committa("tetto basso")
        self.imposta_agente(agente("sleep 30 &\necho $! > .git/figlio\nwait"))
        inizio = time.monotonic()
        esito = self.lancia()
        self.assertLess(time.monotonic() - inizio, 15)
        self.assertEqual(esito.returncode, 22)
        chiusura = self.chiusura()
        self.assertEqual((chiusura["esito"], chiusura["motivo"]), ("timeout", "tetto-di-tempo"))
        figlio = int((self.repo / ".git" / "figlio").read_text(encoding="utf-8"))
        with self.assertRaises(ProcessLookupError):
            os.kill(figlio, 0)

    def test_sigterm_scrive_la_chiusura(self):
        self.imposta_agente(agente("sleep 30"))
        processo = subprocess.Popen(
            self.comando(),
            cwd=self.repo,
            env=self.env,
            stderr=subprocess.DEVNULL,
        )
        limite = time.monotonic() + 10
        while not (self.repo / ".git" / "argomenti").exists() and time.monotonic() < limite:
            time.sleep(0.05)
        processo.terminate()
        self.assertEqual(processo.wait(timeout=30), 143)
        chiusura = self.chiusura()
        self.assertEqual((chiusura["esito"], chiusura["motivo"]), ("errore", "interrotto"))

    def test_percorso_protetto_ferma_i_giri_successivi(self):
        self.imposta_agente(
            agente(
                "echo altro > o3/ciclo/prompt.md\ngit add -A\ngit commit -q -m 'scavalca'\ngit push -q\n"
                f"echo '{RISULTATO}'"
            )
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 23)
        chiusura = self.chiusura()
        self.assertEqual(chiusura["esito"], "errore")
        self.assertEqual(chiusura["motivo"], "percorsi-protetti: o3/ciclo/prompt.md")
        self.imposta_agente(OK)
        (self.repo / ".git" / "argomenti").unlink()
        self.assert_arresto(24, "fermo-dopo-percorsi-protetti")
        (self.repo / ".git" / "lanciatore" / "fermo").unlink()
        self.assertEqual(self.lancia().returncode, 0)

    def test_protetti_del_profilo_si_aggiungono(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            'protetti = ["secret/*"]\n', encoding="utf-8"
        )
        self.committa("profilo")
        self.imposta_agente(
            agente(
                "mkdir secret\necho x > secret/a\ngit add -A\ngit commit -q -m 'x'\ngit push -q\n"
                f"echo '{RISULTATO}'"
            )
        )
        self.assertEqual(self.lancia().returncode, 23)

    def test_lock_tenuto(self):
        self.imposta_agente(agente("sleep 3"))
        primo = subprocess.Popen(
            self.comando(),
            cwd=self.repo,
            env=self.env,
            stderr=subprocess.DEVNULL,
        )
        limite = time.monotonic() + 10
        while not (self.repo / ".git" / "argomenti").exists() and time.monotonic() < limite:
            time.sleep(0.05)
        esito = self.lancia()
        self.assertEqual(esito.returncode, 75)
        primo.wait(timeout=30)

    def test_recinto_dell_host_precede_l_agente(self):
        involucro = self.base / "recinto.sh"
        involucro.write_text('#!/bin/sh\ntouch .git/nel-recinto\nexec "$@"\n', encoding="utf-8")
        involucro.chmod(0o755)
        self.assertEqual(self.lancia("--recinto", str(involucro)).returncode, 0)
        self.assertTrue((self.repo / ".git" / "nel-recinto").exists())

    def test_controlli_non_scrivono_tracce(self):
        esito = self.lancia("--controlli")
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertIn("potrebbe partire", esito.stdout)
        self.assertFalse((self.repo / "i1").exists())
        (self.repo / "sporco.md").write_text("x\n", encoding="utf-8")
        esito = self.lancia("--controlli")
        self.assertEqual(esito.returncode, 10)
        self.assertFalse((self.repo / "i1").exists())

    def con_prima(self, corpo, extra=""):
        cartella = self.repo / "o3" / "ciclo"
        (cartella / "prima.py").write_text(corpo, encoding="utf-8")
        (cartella / "lanciatore.toml").write_text(
            f'prima = "o3/ciclo/prima.py"\n{extra}', encoding="utf-8"
        )
        self.committa("aggancio")

    def test_prima_ferma_col_suo_codice_e_il_suo_motivo(self):
        self.con_prima('print("fuori-slot")\nraise SystemExit(16)\n')
        self.assert_arresto(16, "fuori-slot")

    def test_prima_con_codice_non_ammesso_e_un_errore_di_forma(self):
        self.con_prima('raise RuntimeError("rotto")\n')
        self.assert_arresto(14, "prima-codice-1")

    def test_prima_accorcia_il_tetto_e_avvisa(self):
        self.con_prima('print(\'{"minuti": 0.01, "attenzione": "login in scadenza"}\')\n')
        self.imposta_agente(agente("sleep 30"))
        self.assertEqual(self.lancia().returncode, 22)
        self.assertEqual(self.chiusura()["attenzione"], "login in scadenza")

    def test_prima_non_allunga_il_tetto(self):
        self.con_prima("print('{\"minuti\": 999}')\n", "minuti = 10\n")
        cartella = os.getcwd()
        self.addCleanup(os.chdir, cartella)
        os.chdir(self.repo)
        profilo = MODULE.leggi_profilo(MODULE.PROFILO)
        self.assertEqual(MODULE.esegui_prima(profilo).profilo.minuti, 10)

    def test_prima_salta_senza_lasciare_tracce(self):
        self.con_prima("print('{\"salta\": true}')\n")
        self.assertEqual(self.lancia().returncode, 0)
        self.assertFalse((self.repo / "i1" / "giri" / "tentativi.jsonl").exists())
        self.assertFalse((self.repo / ".git" / "argomenti").exists())

    def test_prima_fuori_da_o3_ciclo_e_rifiutato(self):
        (self.repo / "fuori.py").write_text("", encoding="utf-8")
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            'prima = "fuori.py"\n', encoding="utf-8"
        )
        self.committa("aggancio fuori posto")
        self.assert_arresto(14, "prima-invalido")

    def test_prima_con_uscita_non_json(self):
        self.con_prima('print("ciao")\n')
        self.assert_arresto(14, "prima-invalido")

    def test_i_controlli_eseguono_l_aggancio(self):
        self.con_prima('print("fuori-slot")\nraise SystemExit(16)\n')
        esito = self.lancia("--controlli")
        self.assertEqual(esito.returncode, 16)
        self.assertIn("fuori-slot", esito.stdout)

    def test_l_aggancio_sa_se_e_un_giro_o_una_diagnosi(self):
        self.con_prima(
            'import os\nprint(os.environ["LANCIATORE_MODO"])\nraise SystemExit(16)\n'
        )
        self.assertIn("controlli", self.lancia("--controlli").stdout)
        self.assert_arresto(16, "giro")

    def test_i_controlli_non_si_fermano_al_primo_arresto(self):
        self.con_prima('print("fuori-slot")\nraise SystemExit(16)\n')
        (self.repo / "sporco.md").write_text("x\n", encoding="utf-8")
        (self.repo / "o3" / "ciclo" / "permessi.json").write_text("{rotto", encoding="utf-8")
        esito = self.lancia("--controlli")
        self.assertEqual(esito.returncode, 16)
        for motivo in ("fuori-slot", "checkout-sporco", "settings-invalide"):
            self.assertIn(motivo, esito.stdout)
        self.assertNotIn("potrebbe partire", esito.stdout)

    def test_il_tetto_dell_aggancio_sconta_fetch_e_pull(self):
        profilo = MODULE.Profilo(minuti=10)
        esito = MODULE.EsitoPrima(profilo, accorciato=True)
        self.assertEqual(MODULE.tetto_residuo(esito, 120).minuti, 8)

    def test_il_tetto_del_profilo_vale_dall_avvio_dell_agente(self):
        profilo = MODULE.Profilo(minuti=10)
        self.assertEqual(MODULE.tetto_residuo(MODULE.EsitoPrima(profilo), 120).minuti, 10)

    def test_tetto_esaurito_prima_dell_avvio(self):
        esito = MODULE.EsitoPrima(MODULE.Profilo(minuti=1), accorciato=True)
        with self.assertRaises(MODULE.Arresto) as contesto:
            MODULE.tetto_residuo(esito, 61)
        self.assertEqual(contesto.exception.codice, 22)

    def test_stderr_dell_agente_finisce_nello_stream(self):
        self.imposta_agente(agente("echo spiegazione >&2\nexit 3"))
        self.assertEqual(self.lancia().returncode, 20)
        stream = Path(self.chiusura()["giro"]).read_text(encoding="utf-8")
        self.assertIn("spiegazione", stream)

    def test_arresto_prima_delle_tracce_resta_in_git(self):
        (self.repo / ".gitignore").write_text("", encoding="utf-8")
        self.committa("niente ignore")
        self.lancia()
        registro = (self.repo / ".git" / "lanciatore" / "arresti.log").read_text(encoding="utf-8")
        self.assertIn("giri-non-ignorati", registro)

    def canone(self):
        """Un checkout del canone a parte, col lanciatore copiato dentro."""
        origine = self.base / "canone.git"
        self.sh("git", "init", "-q", "--bare", str(origine), cwd=self.base)
        checkout = self.base / "canone"
        self.sh("git", "clone", "-q", str(origine), str(checkout), cwd=self.base)
        (checkout / "o3").mkdir()
        (checkout / "o3" / "lanciatore.py").write_text(
            SCRIPT.read_text(encoding="utf-8"), encoding="utf-8"
        )
        self.sh("git", "add", "-A", cwd=checkout)
        self.sh("git", "commit", "-q", "-m", "canone", cwd=checkout)
        self.sh("git", "push", "-q", "-u", "origin", "main", cwd=checkout)
        altro = self.base / "canone-altro"
        self.sh("git", "clone", "-q", str(origine), str(altro), cwd=self.base)
        (altro / "nuovo.md").write_text("x\n", encoding="utf-8")
        self.sh("git", "add", "-A", cwd=altro)
        self.sh("git", "commit", "-q", "-m", "nuovo", cwd=altro)
        self.sh("git", "push", "-q", cwd=altro)
        return checkout, self.sh("git", "rev-parse", "HEAD", cwd=altro)

    def lancia_dal_canone(self, checkout, *argomenti):
        return subprocess.run(
            [
                sys.executable,
                str(checkout / "o3" / "lanciatore.py"),
                "--claude",
                str(self.claude),
                *argomenti,
            ],
            cwd=self.repo,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )

    def test_il_giro_aggiorna_il_checkout_del_canone(self):
        checkout, testa = self.canone()
        esito = self.lancia_dal_canone(checkout)
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertEqual(self.sh("git", "rev-parse", "HEAD", cwd=checkout), testa)

    def test_l_host_puo_spegnere_il_pull_del_canone(self):
        checkout, testa = self.canone()
        self.assertEqual(self.lancia_dal_canone(checkout, "--senza-pull-canone").returncode, 0)
        self.assertNotEqual(self.sh("git", "rev-parse", "HEAD", cwd=checkout), testa)

    def test_canone_sporco_e_un_avviso_non_un_arresto(self):
        checkout, _ = self.canone()
        (checkout / "sporco.md").write_text("x\n", encoding="utf-8")
        self.assertEqual(self.lancia_dal_canone(checkout).returncode, 0)
        self.assertIn("canone non aggiornato", self.chiusura()["attenzione"])

    def test_pota_gli_stream_oltre_il_limite(self):
        cartella = self.base / "stream"
        cartella.mkdir()
        for numero in range(5):
            file = cartella / f"{numero}.jsonl"
            file.write_text("x", encoding="utf-8")
            os.utime(file, (numero + 1, numero + 1))
        MODULE.pota(cartella, tenuti=2)
        self.assertEqual(sorted(p.name for p in cartella.iterdir()), ["3.jsonl", "4.jsonl"])


@unittest.skipIf(os.name == "nt", "symlink di /proc simulati")
class SessioniTests(unittest.TestCase):
    def setUp(self):
        temporanea = tempfile.TemporaryDirectory()
        self.addCleanup(temporanea.cleanup)
        self.base = Path(temporanea.name)
        self.proc = self.base / "proc"
        self.proc.mkdir()
        self.checkout = self.base / "repo"

    def processo(self, pid, nome, cwd):
        cartella = self.proc / str(pid)
        cartella.mkdir()
        (cartella / "comm").write_text(f"{nome}\n", encoding="utf-8")
        (cartella / "cwd").symlink_to(cwd)

    def test_claude_nel_checkout_o_in_una_sottocartella(self):
        self.processo(10, "claude", f"{self.checkout}/kb")
        arresto, _ = MODULE.sessioni_posix(self.checkout, self.proc)
        self.assertEqual((arresto.codice, arresto.motivo), (15, "sessione-claude-attiva"))

    def test_altri_processi_e_altri_checkout_non_contano(self):
        self.processo(11, "python3", str(self.checkout))
        self.processo(12, "claude", f"{self.checkout}-altro")
        self.assertEqual(MODULE.sessioni_posix(self.checkout, self.proc), (None, 0))

    def rollout(self, cwd, eta_minuti=1):
        cartella = self.base / "sessions" / "2026" / "11"
        cartella.mkdir(parents=True, exist_ok=True)
        file = cartella / "rollout-a.jsonl"
        file.write_text(
            json.dumps({"type": "session_meta", "payload": {"cwd": str(cwd)}}) + "\n",
            encoding="utf-8",
        )
        momento = time.time() - eta_minuti * 60
        os.utime(file, (momento, momento))

    def test_rollout_codex_recente_nel_checkout(self):
        self.rollout(self.checkout)
        arresto = MODULE.sessioni_codex(self.checkout, self.base / "sessions")
        self.assertEqual(arresto.motivo, "sessione-codex-attiva")

    def test_rollout_codex_vecchio_o_altrove(self):
        self.rollout(self.checkout, eta_minuti=120)
        self.assertIsNone(MODULE.sessioni_codex(self.checkout, self.base / "sessions"))
        self.rollout(self.base / "altrove")
        self.assertIsNone(MODULE.sessioni_codex(self.checkout, self.base / "sessions"))


class WindowsTests(unittest.TestCase):
    """Il ramo Windows, per quanto si può provare fuori da Windows."""

    def tasklist(self, stdout="", returncode=0, errore=None):
        finto = mock.Mock(stdout=stdout, returncode=returncode)
        with mock.patch.object(MODULE.subprocess, "run", return_value=finto, side_effect=errore):
            return MODULE.sessioni_windows()

    def test_claude_vivo_sull_host_ferma_il_giro(self):
        arresto, _ = self.tasklist('"claude.exe","1234","Services","0","10 K"')
        self.assertEqual(arresto.motivo, "sessione-claude-attiva")

    def test_nessun_processo(self):
        self.assertEqual(
            self.tasklist("INFORMAZIONI: nessuna attività in esecuzione."), (None, None)
        )

    def test_tasklist_che_fallisce_non_vuol_dire_nessuna_sessione(self):
        for caso in [{"returncode": 1}, {"errore": OSError("assente")}]:
            with self.subTest(caso):
                arresto, avviso = self.tasklist(**caso)
                self.assertIsNone(arresto)
                self.assertIn("non verificabili", avviso)

    def test_percorsi_con_maiuscole_e_barre_miste(self):
        radice = r"C:\Users\danea\danea-auto"
        self.assertTrue(MODULE._dentro("c:/users/Danea/danea-auto/kb", radice, ntpath))
        self.assertTrue(MODULE._dentro(r"C:\USERS\danea\danea-auto", radice, ntpath))
        self.assertFalse(MODULE._dentro(r"C:\Users\danea\danea-auto-altro", radice, ntpath))


class ProtettiTests(unittest.TestCase):
    def test_cio_che_definisce_il_giro_e_protetto(self):
        for percorso in [
            "o3/ciclo/prompt.md",
            "o3/lanciatore.py",
            ".claude/skills/a/SKILL.md",
            "autonomy.md",
        ]:
            with self.subTest(percorso):
                self.assertTrue(
                    any(__import__("fnmatch").fnmatch(percorso, m) for m in MODULE.PROTETTI)
                )

    def test_le_collezioni_non_sono_protette(self):
        for percorso in ["o1/plan.md", "i3/filo.md", "kb/plan.md", "o3/altro.py"]:
            with self.subTest(percorso):
                self.assertFalse(
                    any(__import__("fnmatch").fnmatch(percorso, m) for m in MODULE.PROTETTI)
                )


if __name__ == "__main__":
    unittest.main()
