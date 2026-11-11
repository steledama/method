"""Contratto dell'esecutore Codex: politica tradotta, eventi normalizzati.

Codex è un eseguibile finto che emette gli eventi nella forma osservata su
Codex CLI 0.166.0 il 2026-11-11: nessun `codex` reale parte da questi test.
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "o3" / "esecutore_codex.py"
SPEC = importlib.util.spec_from_file_location("esecutore_codex", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

RADICE = Path("/repo")
IMPOSTAZIONI = {
    "permissions": {
        "allow": [
            "Read(./**)",
            "Bash(git status*)",
            "Bash(git commit *)",
            "Bash(git push)",
            "Bash(ls *)",
            "Bash(head *)",
            "Bash(cat *)",
            "Bash(python3 o3/commit_gate.py *)",
            "Edit(./i1/**)",
            "Write(./i1/**)",
            "Edit(./o1/plan.md)",
            "WebSearch",
        ],
        "deny": [
            "Edit(./o3/**)",
            "Edit(./.git/**)",
            "Read(~/.ssh/**)",
            "Bash(rm *)",
            "Bash(sed -i*)",
            "mcp__claude_ai_Claude_Docs",
        ],
    },
    "env": {"GIT_REFLOG_ACTION": "lanciatore prova"},
}


def comando(testo):
    return MODULE.giudica_comando(testo, IMPOSTAZIONI, RADICE)


def chiamata(strumento, dati):
    ingresso = {"tool_name": strumento, "tool_input": dati, "cwd": str(RADICE)}
    return MODULE.giudica(ingresso, {**IMPOSTAZIONI, "hooks": {}})


class PoliticaTests(unittest.TestCase):
    def test_comandi_ammessi_anche_composti(self):
        self.assertIsNone(comando("git status --short"))
        self.assertIsNone(comando("git commit -m 'docs: giro' && git push"))
        self.assertIsNone(comando("ls -la | head -3"))
        self.assertIsNone(comando("ls"))

    def test_basta_un_pezzo_negato_o_fuori_elenco(self):
        self.assertIn("Bash(rm *)", comando("ls; rm -rf x"))
        self.assertIn("non ammesso", comando("git push --force"))
        self.assertIn("non ammesso", comando("git status\ncurl x"))

    def test_le_sostituzioni_non_si_giudicano_e_cadono(self):
        self.assertIn("non scomponibile", comando("cat $(echo x)"))
        self.assertIn("non scomponibile", comando("cat `x`"))

    def test_le_letture_negate_valgono_anche_nei_comandi(self):
        self.assertIn("Read(~/.ssh/**)", comando("cat ~/.ssh/id_rsa"))

    def test_patch_su_percorsi_ammessi_e_negati(self):
        patch = "*** Begin Patch\n*** Add File: i1/nota.md\n+x\n*** End Patch"
        self.assertIsNone(chiamata("apply_patch", {"command": patch}))
        patch = "*** Begin Patch\n*** Update File: o3/lanciatore.py\n*** End Patch"
        self.assertIn("Edit(./o3/**)", chiamata("apply_patch", {"command": patch}))
        patch = "*** Begin Patch\n*** Update File: README.md\n*** End Patch"
        self.assertIn("non ammessa", chiamata("apply_patch", {"command": patch}))

    def test_una_patch_che_sposta_giudica_anche_la_destinazione(self):
        patch = (
            "*** Begin Patch\n*** Update File: i1/a.md\n*** Move to: .git/hooks/pre-commit\n"
            "*** End Patch"
        )
        self.assertIn(".git", chiamata("apply_patch", {"command": patch}))

    def test_strumenti_per_nome(self):
        self.assertIsNone(chiamata("update_plan", {}))
        self.assertIsNone(chiamata("WebSearch", {}))
        self.assertIn("negato", chiamata("mcp__claude_ai_Claude_Docs__create", {}))
        self.assertIn("non ammesso", chiamata("mcp__altro__x", {}))

    def test_l_hook_del_lanciatore_rifiuta_con_uscita_2(self):
        bloccante = f"{sys.executable} -c \"import sys; print('concorrente', file=sys.stderr); sys.exit(2)\""
        impostazioni = {
            **IMPOSTAZIONI,
            "hooks": {
                "PreToolUse": [
                    {"matcher": "Bash", "hooks": [{"type": "command", "command": bloccante}]}
                ]
            },
        }
        ingresso = {
            "tool_name": "Bash",
            "tool_input": {"command": "git commit -m x"},
            "cwd": str(RADICE),
        }
        self.assertEqual(MODULE.giudica(ingresso, impostazioni), "concorrente")

    def test_l_hook_risponde_col_rifiuto_di_codex_e_registra_il_diniego(self):
        with tempfile.TemporaryDirectory() as tmp:
            impostazioni = Path(tmp) / "settings.json"
            impostazioni.write_text(json.dumps(IMPOSTAZIONI), encoding="utf-8")
            dinieghi = Path(tmp) / "dinieghi.jsonl"
            ingresso = {"tool_name": "Bash", "tool_input": {"command": "rm x"}, "cwd": tmp}
            esito = subprocess.run(
                [sys.executable, str(SCRIPT), "--hook", "--settings", str(impostazioni)]
                + ["--dinieghi", str(dinieghi)],
                input=json.dumps(ingresso),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(esito.returncode, 0)
            uscita = json.loads(esito.stdout)["hookSpecificOutput"]
            self.assertEqual(uscita["permissionDecision"], "deny")
            self.assertIn("rm", uscita["permissionDecisionReason"])
            voce = json.loads(dinieghi.read_text(encoding="utf-8"))
            self.assertEqual(voce["tool_input"], {"command": "rm x"})

    def test_un_hook_che_non_si_valuta_non_lascia_passare(self):
        with tempfile.TemporaryDirectory() as tmp:
            esito = subprocess.run(
                [sys.executable, str(SCRIPT), "--hook", "--settings", f"{tmp}/manca.json"],
                input="{}",
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(
            json.loads(esito.stdout)["hookSpecificOutput"]["permissionDecision"], "deny"
        )


AVVIO = [
    {"type": "thread.started", "thread_id": "t1"},
    {"type": "item.completed", "item": {"id": "item_0", "type": "error", "message": "hook trust"}},
    {"type": "turn.started"},
]
COMANDO = {
    "type": "item.started",
    "item": {"id": "item_1", "type": "command_execution", "command": "bash -lc 'git status'"},
}
MESSAGGIO = {"type": "item.completed", "item": {"type": "agent_message", "text": "Fatto."}}
FINE = {"type": "turn.completed", "usage": {"input_tokens": 10, "output_tokens": 2}}


class TraduttoreTests(unittest.TestCase):
    def traduci(self, eventi):
        traduttore = MODULE.Traduttore()
        uscite = [u for e in eventi for u in traduttore.traduci(e)]
        return traduttore, uscite

    def test_giro_riuscito(self):
        traduttore, uscite = self.traduci([*AVVIO, COMANDO, MESSAGGIO, FINE])
        tipi = [u["type"] for u in uscite]
        self.assertEqual(tipi, ["system", "system", "assistant", "assistant"])
        self.assertEqual(uscite[2]["message"]["content"][0]["name"], "Bash")
        fine = traduttore.risultato(0, "", [])
        self.assertIs(fine["is_error"], False)
        self.assertEqual(fine["result"], "Fatto.")
        self.assertIsNone(fine["total_cost_usd"])
        self.assertEqual(fine["usage"]["input_tokens"], 10)

    def test_quota_rifiutata_e_indisponibilita(self):
        guasto = {"type": "turn.failed", "error": {"message": "You've hit your usage limit."}}
        traduttore, uscite = self.traduci([*AVVIO, guasto])
        self.assertEqual(uscite[-1]["error"], "rate_limit")
        fine = traduttore.risultato(1, "", [])
        self.assertEqual(fine["api_error_status"], 429)
        self.assertTrue(fine["is_error"])

    def test_senza_turno_completo_non_e_un_successo(self):
        traduttore, _ = self.traduci([*AVVIO, COMANDO])
        self.assertTrue(traduttore.risultato(0, "", [])["is_error"])

    def test_evento_sconosciuto_resta_visibile(self):
        _, uscite = self.traduci([{"type": "nuovo.evento", "x": 1}])
        self.assertEqual(uscite[0]["type"], "codex.nuovo.evento")

    def test_strumento_nuovo_conta_come_chiamata(self):
        evento = {"type": "item.started", "item": {"id": "i", "type": "mcp_tool_call"}}
        _, uscite = self.traduci([evento])
        self.assertEqual(uscite[0]["message"]["content"][0]["name"], "mcp_tool_call")


@unittest.skipIf(os.name == "nt", "Codex finto in shell POSIX")
class EsecuzioneTests(unittest.TestCase):
    def esegui(self, eventi, uscita=0, stderr=""):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            subprocess.run(["git", "init", "-q", str(base / "repo")], check=True)
            righe = "\n".join(json.dumps(e) for e in eventi)
            codex = base / "codex"
            codex.write_text(
                "#!/bin/sh\n"
                f'printf "%s\\n" "$@" > {base}/argomenti\n'
                f"cat > {base}/prompt-ricevuto\n"
                f'echo "$GIT_REFLOG_ACTION" > {base}/ambiente\n'
                f"cat <<'FINE'\n{righe}\nFINE\n"
                f"echo '{stderr}' >&2\n"
                f"exit {uscita}\n",
                encoding="utf-8",
            )
            codex.chmod(0o755)
            prompt = base / "prompt.md"
            prompt.write_text("Fai il giro.\n", encoding="utf-8")
            impostazioni = base / "settings.json"
            impostazioni.write_text(json.dumps(IMPOSTAZIONI), encoding="utf-8")
            esito = subprocess.run(
                [sys.executable, str(SCRIPT), "--codex", str(codex), "--prompt", str(prompt)]
                + ["--settings", str(impostazioni)],
                cwd=base / "repo",
                capture_output=True,
                text=True,
                check=False,
            )
            self.argomenti = (base / "argomenti").read_text().splitlines()
            self.prompt = (base / "prompt-ricevuto").read_text()
            self.ambiente = (base / "ambiente").read_text().strip()
            self.repo = (base / "repo").resolve()
        return esito, [json.loads(r) for r in esito.stdout.splitlines()]

    def test_riuscito_con_la_politica_passata_a_codex(self):
        esito, righe = self.esegui([*AVVIO, COMANDO, MESSAGGIO, FINE])
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertIs(righe[-1]["is_error"], False)
        self.assertEqual(self.prompt, "Fai il giro.\n")
        self.assertEqual(self.ambiente, "lanciatore prova")
        for atteso in (
            "exec",
            "--json",
            "--ephemeral",
            "--ignore-user-config",
            "--ignore-rules",
            "workspace-write",
            'approval_policy="never"',
            "sandbox_workspace_write.network_access=true",
        ):
            self.assertIn(atteso, self.argomenti)
        radici = next(a for a in self.argomenti if a.startswith("sandbox_workspace_write.writable"))
        self.assertIn(str(self.repo / ".git"), radici)
        hook = next(a for a in self.argomenti if a.startswith("hooks.PreToolUse="))
        self.assertIn("--hook", hook)

    def test_quota_rifiutata_esce_non_zero_con_429(self):
        guasto = {"type": "turn.failed", "error": {"message": "usage limit reached"}}
        esito, righe = self.esegui([*AVVIO, guasto], uscita=1)
        self.assertNotEqual(esito.returncode, 0)
        self.assertEqual(righe[-1]["api_error_status"], 429)

    def test_codex_assente(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp], check=True)
            (Path(tmp) / "s.json").write_text("{}", encoding="utf-8")
            (Path(tmp) / "p.md").write_text("x", encoding="utf-8")
            esito = subprocess.run(
                [sys.executable, str(SCRIPT), "--codex", f"{tmp}/manca", "--prompt"]
                + [f"{tmp}/p.md", "--settings", f"{tmp}/s.json"],
                cwd=tmp,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(esito.returncode, 127)
        self.assertEqual(json.loads(esito.stdout)["terminal_reason"], "executable_missing")


if __name__ == "__main__":
    unittest.main()
