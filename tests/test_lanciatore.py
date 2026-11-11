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
from unittest.mock import patch
from datetime import UTC, datetime
from pathlib import Path

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
        for variabile in ("INVOCATION_ID", "CLAUDE_CONFIG_DIR", "CODEX_HOME"):
            self.env.pop(variabile, None)
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

    def rifiuto(self, prefisso="", costo=0):
        evento = json.dumps(
            {
                "type": "result",
                "is_error": True,
                "api_error_status": 429,
                "terminal_reason": "rate_limit",
                "total_cost_usd": costo,
            }
        )
        self.imposta_agente(agente(prefisso + f"echo '{evento}'\nexit 1"))

    def motori(self, *motori, codex_eventi=None, codex_uscita=0):
        """Il profilo del repo sceglie i motori; Codex è finto e parla il suo JSONL."""
        voci = ", ".join(f'"{m}"' for m in motori)
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            f"motori = [{voci}]\n", encoding="utf-8"
        )
        self.committa("profilo")
        self.sh("git", "push", "-q")
        eventi = codex_eventi or [
            {"type": "thread.started", "thread_id": "t"},
            {"type": "turn.started"},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Fatto."}},
            {"type": "turn.completed", "usage": {"input_tokens": 3}},
        ]
        righe = "\n".join(json.dumps(e) for e in eventi)
        self.codex = self.base / "codex-finto"
        self.codex.write_text(
            f'#!/bin/sh\nprintf "%s\\n" "$@" > .git/argomenti-codex\ncat > /dev/null\n'
            f"cat <<'FINE'\n{righe}\nFINE\nexit {codex_uscita}\n",
            encoding="utf-8",
        )
        self.codex.chmod(0o755)
        return str(self.codex)

    def test_fallback_rifiuto_prima_degli_atti(self):
        self.rifiuto()
        esito = self.lancia("--codex", self.motori("claude", "codex"))
        self.assertEqual(esito.returncode, 0, esito.stderr)
        fine = self.chiusura()
        self.assertEqual(fine["engine"], "codex")
        self.assertEqual([e["engine"] for e in fine["engine_attempts"]], ["claude", "codex"])
        self.assertEqual(fine["claude_exit"], 1)
        self.assertEqual(fine["attenzione"], None)
        self.assertTrue(Path(fine["engine_attempts"][0]["giro"]).exists())
        args = (self.repo / ".git/argomenti-codex").read_text().splitlines()
        self.assertIn("exec", args)
        self.assertIn("workspace-write", args)
        self.assertIs(fine["budget_usd_imposto"], False)
        self.assertEqual([e["budget_usd_imposto"] for e in fine["engine_attempts"]], [True, False])

    def test_senza_codex_nei_motori_niente_fallback(self):
        self.rifiuto()
        esito = self.lancia()
        self.assertEqual(esito.returncode, 20)
        self.assertEqual(len(self.chiusura()["engine_attempts"]), 1)

    def test_codex_primo_e_claude_di_riserva(self):
        guasto = [
            {"type": "thread.started", "thread_id": "t"},
            {"type": "turn.failed", "error": {"message": "You've hit your usage limit."}},
        ]
        esito = self.lancia(
            "--codex", self.motori("codex", "claude", codex_eventi=guasto, codex_uscita=1)
        )
        self.assertEqual(esito.returncode, 0, esito.stderr)
        fine = self.chiusura()
        self.assertEqual([e["engine"] for e in fine["engine_attempts"]], ["codex", "claude"])
        self.assertEqual(fine["engine"], "claude")
        self.assertIn("codex: costo ignoto", fine["attenzione"])
        self.assertIn("--max-budget-usd 5", (self.repo / ".git/argomenti").read_text())

    def test_solo_codex(self):
        esito = self.lancia("--codex", self.motori("codex"))
        self.assertEqual(esito.returncode, 0, esito.stderr)
        fine = self.chiusura()
        self.assertEqual(fine["engine"], "codex")
        self.assertIsNone(fine["claude_exit"])
        self.assertIs(fine["budget_usd_imposto"], False)

    def test_motori_invalidi(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            'motori = ["claude", "gemini"]\n', encoding="utf-8"
        )
        self.committa("profilo")
        self.sh("git", "push", "-q")
        self.assertEqual(self.lancia().returncode, 14)

    def test_il_costo_noto_resta_in_chiusura(self):
        codex = self.motori("claude", "codex")
        self.rifiuto(costo=1.25)
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertEqual(self.chiusura()["costo_usd"], 1.25)

    def test_budget_esaurito_non_ferma_un_motore_senza_tetto(self):
        self.rifiuto(costo=5)
        esito = self.lancia("--codex", self.motori("claude", "codex"))
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertEqual(self.chiusura()["engine"], "codex")

    def test_costo_ignoto_non_blocca_e_si_dichiara(self):
        self.rifiuto(costo=None)
        esito = self.lancia("--codex", self.motori("claude", "codex"))
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertIn("claude: costo ignoto", self.chiusura()["attenzione"])

    def test_codex_fallisce_senza_terzo_tentativo(self):
        self.rifiuto()
        guasto = [{"type": "thread.started", "thread_id": "t"}]
        esito = self.lancia(
            "--codex", self.motori("claude", "codex", codex_eventi=guasto, codex_uscita=7)
        )
        self.assertEqual(esito.returncode, 20)
        self.assertEqual(self.chiusura()["motivo"], "codex-uscita-non-zero")
        self.assertEqual(len(self.chiusura()["engine_attempts"]), 2)

    def test_claude_assente(self):
        codex = self.motori("claude", "codex")
        self.claude.unlink()
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertEqual(self.chiusura()["engine"], "codex")
        self.assertEqual(self.chiusura()["claude_exit"], 127)

    def test_nessun_motore_disponibile(self):
        self.motori("claude", "codex")
        self.claude.unlink()
        self.assertEqual(self.lancia("--codex", str(self.base / "manca")).returncode, 14)

    def test_fallback_bloccato_da_modifica_senza_tool_in_traccia(self):
        codex = self.motori("claude", "codex")
        self.rifiuto("echo partial > nuovo.md\n")
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 20)
        self.assertEqual(self.chiusura()["engine"], "claude")

    def test_warning_non_attiva_fallback(self):
        quota = json.dumps(
            {
                "type": "rate_limit_event",
                "rate_limit_info": {
                    "status": "allowed_warning",
                    "overageStatus": "rejected",
                    "overageDisabledReason": "out_of_credits",
                    "utilization": 0.92,
                },
            }
        )
        codex = self.motori("claude", "codex")
        self.imposta_agente(agente(f"echo '{quota}'\necho '{RISULTATO}'"))
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 0, esito.stderr)
        fine = self.chiusura()
        self.assertEqual(fine["engine"], "claude")
        self.assertEqual(len(fine["provider_observation"]["rate_limit_events"]), 1)
        self.assertFalse(fine["provider_observation"]["unavailable"])

    def test_fallback_bloccato_dopo_strumento(self):
        tool = json.dumps(
            {
                "type": "assistant",
                "message": {
                    "content": [{"type": "tool_use", "name": "Bash", "input": {"command": "true"}}]
                },
            }
        )
        codex = self.motori("claude", "codex")
        self.rifiuto(f"echo '{tool}'\n")
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 20, esito.stderr)
        self.assertEqual(len(self.chiusura()["engine_attempts"]), 1)
        self.assertIn("partial acts", self.chiusura()["attenzione"])

    def test_fallback_bloccato_da_traccia_incompleta(self):
        codex = self.motori("claude", "codex")
        self.rifiuto("echo 'not-json'\n")
        esito = self.lancia("--codex", codex)
        self.assertEqual(esito.returncode, 20, esito.stderr)
        self.assertEqual(self.chiusura()["engine"], "claude")

    def test_col_solo_claude_la_chiusura_dichiara_il_tetto(self):
        self.assertEqual(self.lancia().returncode, 0)
        self.assertIs(self.chiusura()["budget_usd_imposto"], True)

    def test_errore_builder_non_attiva_fallback(self):
        self.imposta_agente(agente("echo 'aws-lc-sys panic exit 101'\nexit 101"))
        esito = self.lancia("--codex", self.motori("claude", "codex"))
        self.assertEqual(esito.returncode, 20)
        self.assertEqual(self.chiusura()["engine"], "claude")

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

    def test_giro_senza_commit_non_giudica_il_push(self):
        self.assertEqual(self.lancia().returncode, 0)
        chiusura = self.righe()[-1]
        self.assertFalse(chiusura["commit"])
        self.assertIsNone(chiusura["push"])

    def sessione_concorrente(self):
        """Un transcript Claude nel checkout con una chiamata mentre l'agente gira."""
        cartella = "".join(c if c.isalnum() else "-" for c in str(self.repo.resolve()))
        transcript = self.base / ".claude" / "projects" / cartella / "s.jsonl"
        riga = json.dumps(
            {
                "type": "assistant",
                "cwd": str(self.repo.resolve()),
                "timestamp": "2099-01-01T00:00:00Z",
                "message": {"content": [{"type": "tool_use", "name": "Edit"}]},
            }
        )
        return f"mkdir -p '{transcript.parent}'\necho '{riga}' > '{transcript}'\n"

    def test_una_sessione_aperta_non_ferma_il_giro(self):
        cartella = "".join(c if c.isalnum() else "-" for c in str(self.repo.resolve()))
        transcript = self.base / ".claude" / "projects" / cartella / "s.jsonl"
        transcript.parent.mkdir(parents=True)
        riga = {
            "type": "assistant",
            "cwd": str(self.repo),
            "timestamp": "2020-01-01T00:00:00Z",
            "message": {"content": [{"type": "tool_use", "name": "Edit"}]},
        }
        transcript.write_text(json.dumps(riga) + "\n", encoding="utf-8")
        os.utime(transcript, (time.time() - 30, time.time() - 30))
        self.imposta_agente(agente(f"echo x > nota.md\necho '{RISULTATO}'"))
        esito = self.lancia()
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertNotIn("sessioni_concorrenti", self.chiusura())
        self.assertFalse((self.repo / ".git" / "lanciatore" / "inizio-giro").exists())

    def test_lavoro_lasciato_mentre_un_altra_sessione_scrive(self):
        self.imposta_agente(
            agente(f"echo x > nota.md\n{self.sessione_concorrente()}echo '{RISULTATO}'")
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 15, esito.stderr)
        chiusura = self.chiusura()
        self.assertEqual(chiusura["motivo"], "sessione-concorrente")
        self.assertTrue(chiusura["tree_sporco_dopo"])
        self.assertEqual(len(chiusura["sessioni_concorrenti"]), 1)

    # Un commit di un'altra sessione: senza l'etichetta che il lanciatore dà all'agente.
    ALTRA = "echo c > custode.md\ngit add custode.md\nenv -u GIT_REFLOG_ACTION git commit -q -m 'Autonomia: concordato'\n"

    def test_il_commit_di_un_altra_sessione_non_e_del_giro(self):
        self.imposta_agente(agente(f"{self.ALTRA}echo '{RISULTATO}'"))
        esito = self.lancia()
        self.assertEqual(esito.returncode, 0, esito.stderr)
        chiusura = self.chiusura()
        self.assertNotEqual(chiusura["head_prima"], chiusura["head_dopo"])
        self.assertFalse(chiusura["commit"])
        self.assertIsNone(chiusura["oggetto"])
        self.assertIsNone(chiusura["push"])
        self.assertEqual(chiusura["commit_giro"], [])
        self.assertEqual(chiusura["commit_altri"], 1)

    def test_il_commit_altrui_non_nasconde_il_lavoro_lasciato(self):
        self.imposta_agente(
            agente(f"{self.ALTRA}echo x > nota.md\n{self.sessione_concorrente()}echo '{RISULTATO}'")
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 15, esito.stderr)
        chiusura = self.chiusura()
        self.assertFalse(chiusura["commit"])
        self.assertEqual(chiusura["motivo"], "sessione-concorrente")

    def test_l_oggetto_e_quello_del_giro_anche_dopo_un_commit_altrui(self):
        self.imposta_agente(
            agente(
                "echo fatto > nota.md\ngit add nota.md\ngit commit -q -m 'docs: giro'\n"
                f"git push -q\n{self.ALTRA}echo '{RISULTATO}'"
            )
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 0, esito.stderr)
        chiusura = self.chiusura()
        self.assertTrue(chiusura["commit"])
        self.assertEqual(chiusura["oggetto"], "docs: giro")
        self.assertTrue(chiusura["push"])
        self.assertEqual(len(chiusura["commit_giro"]), 1)
        self.assertEqual(chiusura["commit_altri"], 1)
        impostazioni = json.loads((self.repo / ".git/lanciatore/settings.json").read_text())
        self.assertEqual(impostazioni["env"]["GIT_REFLOG_ACTION"], f"lanciatore {chiusura['id']}")

    def test_tree_pulito_senza_commit_non_e_concorrenza(self):
        self.imposta_agente(agente(f"{self.sessione_concorrente()}echo '{RISULTATO}'"))
        self.assertEqual(self.lancia().returncode, 0)

    def hook(self, comando, marker=True):
        impostazioni = json.loads((self.repo / ".git/lanciatore/settings.json").read_text())
        (voce,) = impostazioni["hooks"]["PreToolUse"]
        self.assertEqual(voce["matcher"], "Bash")
        if marker:
            (self.repo / ".git/lanciatore/inizio-giro").touch()
            passato = time.time() - 5
            os.utime(self.repo / ".git/lanciatore/inizio-giro", (passato, passato))
        else:
            (self.repo / ".git/lanciatore/inizio-giro").unlink(missing_ok=True)
        ingresso = json.dumps({"cwd": str(self.repo), "tool_input": {"command": comando}})
        return subprocess.run(
            voce["hooks"][0]["command"],
            shell=True,
            input=ingresso,
            cwd=self.repo,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )

    def test_l_hook_blocca_il_commit_di_un_giro_con_una_sessione_concorrente(self):
        self.assertEqual(self.lancia().returncode, 0)
        self.assertEqual(self.hook("git commit -m x").returncode, 0)
        subprocess.run(["sh", "-c", self.sessione_concorrente()], check=True)
        bloccato = self.hook("git add -A && git commit -m x")
        self.assertEqual(bloccato.returncode, 2)
        self.assertIn("sessione-concorrente", bloccato.stderr)
        self.assertEqual(self.hook("git status").returncode, 0)
        self.assertEqual(self.hook("git commit -m x", marker=False).returncode, 0)

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

    def test_la_rete_vale_anche_al_tetto(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            "minuti = 0.01\n", encoding="utf-8"
        )
        self.committa("tetto basso")
        self.imposta_agente(
            agente("echo altro > o3/ciclo/prompt.md\ngit add -A\ngit commit -q -m x\nsleep 30")
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 23)
        chiusura = self.chiusura()
        self.assertEqual(chiusura["esito"], "errore")
        self.assertEqual(
            chiusura["motivo"], "percorsi-protetti: o3/ciclo/prompt.md (dopo tetto-di-tempo)"
        )
        self.assertTrue((self.repo / ".git" / "lanciatore" / "fermo").exists())

    def test_la_rete_vale_anche_con_uscita_non_zero(self):
        self.imposta_agente(
            agente("echo altro > autonomy.md\ngit add -A\ngit commit -q -m x\nexit 7")
        )
        self.assertEqual(self.lancia().returncode, 23)
        self.assertEqual(
            self.chiusura()["motivo"],
            "percorsi-protetti: autonomy.md (dopo claude-uscita-non-zero)",
        )

    def test_la_cartella_degli_hook_versionati_e_protetta(self):
        self.sh("git", "config", "core.hooksPath", "o3/hooks")
        self.imposta_agente(
            agente(
                "mkdir -p o3/hooks\necho x > o3/hooks/post-merge\ngit add -A\n"
                f"git commit -q -m x\necho '{RISULTATO}'"
            )
        )
        esito = self.lancia()
        self.assertEqual(esito.returncode, 23)
        self.assertEqual(self.chiusura()["motivo"], "percorsi-protetti: o3/hooks/post-merge")

    def test_al_tetto_il_recinto_si_ferma_prima_della_chiusura(self):
        (self.repo / "o3" / "ciclo" / "lanciatore.toml").write_text(
            "minuti = 0.01\n", encoding="utf-8"
        )
        self.committa("tetto basso")
        self.imposta_agente(agente("sleep 30"))
        ferma = self.base / "ferma.sh"
        ferma.write_text(
            "#!/bin/sh\ntest -f i1/giri/tentativi.jsonl && grep -c chiusura i1/giri/tentativi.jsonl"
            " > .git/chiusure-al-fermo || echo 0 > .git/chiusure-al-fermo\n",
            encoding="utf-8",
        )
        ferma.chmod(0o755)
        esito = self.lancia("--recinto-ferma", str(ferma))
        self.assertEqual(esito.returncode, 22)
        self.assertEqual(
            (self.repo / ".git" / "chiusure-al-fermo").read_text(encoding="utf-8").strip(), "0"
        )

    def test_stop_fallito_ferma_anche_un_giro_riuscito(self):
        esito = self.lancia("--recinto-ferma", f'{sys.executable} -c "raise SystemExit(1)"')
        self.assertEqual(esito.returncode, 25)
        self.assertEqual(self.chiusura()["motivo"], "recinto-arresto-non-verificato")
        self.assertIn("not final", self.chiusura()["attenzione"])
        self.assertTrue((self.repo / ".git/lanciatore/fermo").exists())
        self.assertEqual(self.lancia().returncode, 24)

    def test_stop_eseguito_anche_su_successo(self):
        self.assertEqual(
            self.lancia("--recinto-ferma", f'{sys.executable} -c "pass"').returncode, 0
        )

    def test_caps_host_e_branch(self):
        self.assertEqual(self.lancia("--branch", "altro").returncode, 11)
        for valore in ("nan", "inf", "0", "-1"):
            self.assertEqual(self.lancia("--max-minuti", valore).returncode, 14)
        self.assertEqual(self.lancia("--max-budget-usd", "2").returncode, 0)
        self.assertIn("2.0", (self.repo / ".git/argomenti").read_text())
        self.assertEqual(self.lancia("--max-budget-usd", "99").returncode, 0)
        self.assertIn("5", (self.repo / ".git/argomenti").read_text())

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
        self.con_prima('import os\nprint(os.environ["LANCIATORE_MODO"])\nraise SystemExit(16)\n')
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

    def test_il_pull_del_canone_passa_dal_lock_e_dice_perche_fallisce(self):
        checkout, _ = self.canone()
        self.sh("git", "remote", "set-url", "origin", str(self.base / "manca.git"), cwd=checkout)
        self.assertEqual(self.lancia_dal_canone(checkout).returncode, 0)
        attenzione = self.chiusura()["attenzione"]
        self.assertIn("canone non aggiornato: pull fallito (", attenzione)
        self.assertTrue((checkout / ".git" / "lanciatore-pull-canone").exists())

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


class HostBoundaryTests(unittest.TestCase):
    def test_stop_timeout_o_comando_assente_non_sono_successo(self):
        for errore in (OSError("missing"), subprocess.TimeoutExpired("stop", 120)):
            with (
                self.subTest(errore=errore),
                patch.object(MODULE.subprocess, "run", side_effect=errore),
            ):
                with self.assertRaises(MODULE.Arresto) as catturato:
                    MODULE.ferma_recinto(["stop"])
                self.assertEqual(catturato.exception.codice, 25)

    def test_caps_non_allargano_e_tempo_si_restringe(self):
        profilo = MODULE.Profilo(minuti=10, budget_usd=2)
        self.assertEqual(MODULE.limiti_host(profilo, "main", 99, 99), profilo)
        self.assertEqual(MODULE.limiti_host(profilo, "main", 3, 1).minuti, 3)


class ConcorrentiTests(unittest.TestCase):
    """Sessioni che scrivono nel checkout dopo l'inizio del giro."""

    def setUp(self):
        temporanea = tempfile.TemporaryDirectory()
        self.addCleanup(temporanea.cleanup)
        self.base = Path(temporanea.name)
        self.checkout = self.base / "repo"
        self.claude = self.base / "claude" / "projects"
        self.codex = self.base / "codex" / "sessions"
        self.inizio = time.time() - 60

    def istante(self, secondi_dopo):
        momento = datetime.fromtimestamp(self.inizio + secondi_dopo, UTC)
        return momento.isoformat().replace("+00:00", "Z")

    def scrivi(self, file, righe):
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("".join(json.dumps(r) + "\n" for r in righe), encoding="utf-8")

    def claude_evento(self, secondi_dopo, chiamata):
        parte = {"type": "tool_use", "name": "Edit"} if chiamata else {"type": "text"}
        tipo = "assistant"
        return {
            "type": tipo,
            "timestamp": self.istante(secondi_dopo),
            "message": {"content": [parte]},
        }

    def transcript(self, cartella, cwd=None, eta_secondi=-30, chiamata=True, prima=()):
        righe = [
            {"type": "summary"},
            *([{"type": "user", "cwd": str(cwd), "timestamp": self.istante(-600)}] if cwd else []),
            *prima,
            self.claude_evento(-eta_secondi, chiamata),
        ]
        self.scrivi(self.claude / cartella / "s.jsonl", righe)

    def rollout(self, cwd, eta_secondi=-30, tipo="function_call"):
        file = self.codex / "2026" / "11" / "rollout-a.jsonl"
        righe = [
            {"type": "session_meta", "timestamp": self.istante(-600), "payload": {"cwd": str(cwd)}},
            {
                "type": "response_item",
                "timestamp": self.istante(-eta_secondi),
                "payload": {"type": tipo},
            },
        ]
        self.scrivi(file, righe)

    def trovate(self):
        return MODULE.concorrenti(self.checkout, self.inizio, self.claude, self.codex)

    def codifica(self, percorso):
        return "".join(c if c.isalnum() else "-" for c in str(percorso))

    def test_claude_che_scrive_durante_il_giro(self):
        self.transcript(self.codifica(self.checkout), self.checkout)
        self.assertEqual(len(self.trovate()), 1)
        self.assertTrue(self.trovate()[0].startswith("claude: "))

    def test_la_sessione_che_avvia_il_giro_risponde_ma_non_lavora(self):
        self.transcript(
            self.codifica(self.checkout),
            self.checkout,
            chiamata=False,
            prima=[self.claude_evento(-5, True)],
        )
        self.assertEqual(self.trovate(), [])

    def test_l_output_di_una_chiamata_codex_non_e_lavoro(self):
        self.rollout(self.checkout, tipo="function_call_output")
        self.assertEqual(self.trovate(), [])

    def test_claude_in_una_sottocartella(self):
        self.transcript(self.codifica(self.checkout / "kb"), self.checkout / "kb")
        self.assertEqual(len(self.trovate()), 1)

    def test_sessione_aperta_e_ferma_non_conta(self):
        self.transcript(self.codifica(self.checkout), self.checkout, eta_secondi=120)
        self.rollout(self.checkout, eta_secondi=120)
        self.assertEqual(self.trovate(), [])

    def test_un_checkout_dal_nome_simile_non_conta(self):
        altro = Path(f"{self.checkout}-altro")
        self.transcript(self.codifica(altro), altro)
        self.assertEqual(self.trovate(), [])

    def test_codex_che_scrive_durante_il_giro(self):
        self.rollout(self.checkout / "o2")
        self.assertEqual(len(self.trovate()), 1)
        self.assertTrue(self.trovate()[0].startswith("codex: "))

    def test_codex_altrove_non_conta(self):
        self.rollout(self.base / "altrove")
        self.assertEqual(self.trovate(), [])

    def test_il_commit_si_riconosce_anche_composto(self):
        for comando, atteso in [
            ("git commit -m x", True),
            ("git add -A && git commit -q -F msg", True),
            ("git -C /r commit", True),
            ("git log --oneline", False),
            ("git-commit-tree", False),
            ("echo commit", False),
        ]:
            with self.subTest(comando):
                self.assertEqual(bool(MODULE.COMMIT.search(comando)), atteso)


class WindowsTests(unittest.TestCase):
    """Il ramo Windows, per quanto si può provare fuori da Windows."""

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
