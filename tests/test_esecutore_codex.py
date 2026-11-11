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
from typing import ClassVar
from unittest import mock

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
            "Read(//stato/ciclo/**)",
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

    def test_fuori_dal_checkout_si_legge_solo_cio_che_read_ammette(self):
        self.assertIsNone(comando("cat /stato/ciclo/method/fetch.json"))
        self.assertIsNone(comando("head -3 /stato/ciclo/salute/ultimo.json"))
        self.assertIsNone(comando("cat i1/giri/ultimo.json"))
        self.assertIn("fuori dalle cartelle", comando("cat /etc/passwd"))
        self.assertIn("fuori dalle cartelle", comando("ls ../altro/"))
        self.assertIn("fuori dalle cartelle", comando("cat ~/.bashrc"))

    def test_2_e_1_non_spezza_il_comando(self):
        self.assertIsNone(comando("git status --short 2>&1 | head -5"))
        self.assertIsNone(comando("ls -la >&2"))
        self.assertIn("Bash(rm *)", comando("ls & rm x"))

    def test_symlink_e_cartelle_aggiuntive(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp).resolve()
            (base / "repo" / "i1").mkdir(parents=True)
            (base / "canone" / "o3").mkdir(parents=True)
            (base / "segreto").mkdir()
            (base / "repo" / "method").symlink_to(base / "canone")
            (base / "repo" / "fuga").symlink_to(base / "segreto")
            (base / "repo" / "i1" / "trappola").symlink_to(base / "repo" / "o3")
            radice = base / "repo"
            regole_giro = {
                "permissions": {
                    **IMPOSTAZIONI["permissions"],
                    "additionalDirectories": [str(base / "canone")],
                }
            }
            giudica = MODULE.giudica_comando
            self.assertIsNone(giudica("cat method/o3/x.py", regole_giro, radice))
            self.assertIsNone(giudica(f"cat {base}/canone/o3/x.py", regole_giro, radice))
            self.assertIn("fuori dalle cartelle", giudica("cat fuga/x", regole_giro, radice))
            self.assertIn("fuori dalle cartelle", giudica("cat fuga/x", IMPOSTAZIONI, radice))
            self.assertIn(
                "Edit(./o3/**)", MODULE.giudica_file("i1/trappola/a.py", regole_giro, radice)
            )

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


# Regole reali di Baserow (o3/ciclo/permessi.json, 11/11/2026): comandi esatti con
# virgolette, che la normalizzazione toglieva (o3/riproduci-policy-codex.py).
BASEROW = [
    "docker inspect baserow --format '{{.Config.Image}}'",
    "docker inspect baserow --format '{{.State.Health.Status}}'",
    (
        "docker exec -u postgres baserow psql -d baserow -Atc "
        "'select pg_database_size(current_database())'"
    ),
    (
        "docker exec -u postgres baserow psql -d baserow -Atc "
        "'select relname, pg_total_relation_size(relid) from pg_statio_user_tables "
        "order by 2 desc limit 10'"
    ),
    (
        "docker exec -u postgres baserow psql -d baserow -Atc "
        "'select (select count(*) from core_workspace), (select count(*) from database_table)'"
    ),
    (
        "docker exec -u postgres baserow psql -d baserow -Atc "
        "'select relname, n_live_tup, n_dead_tup, last_autovacuum, autovacuum_count "
        "from pg_stat_user_tables order by pg_total_relation_size(relid) desc limit 4'"
    ),
]
LETTURE = {
    "permissions": {
        "allow": [
            "Read(./**)",
            *(f"Bash({c} *)" for c in ("cat", "head", "tail", "grep", "rg", "ls", "sort", "cd")),
            "Bash(git status*)",
            "Bash(git show *)",
            *(f"Bash({c})" for c in BASEROW),
            "Bash(docker compose ps)",
            "Edit(./i1/**)",
        ],
        "deny": [
            "Read(./.env)",
            "Read(./backup/**)",
            "Read(~/.config/**)",
            "Edit(./CLAUDE.md)",
            "Bash(cat .env)",
            "Bash(rm *)",
            "Bash(docker compose up*)",
        ],
    }
}


class LettureNegateTests(unittest.TestCase):
    """Dinieghi `Read` per nomi semplici, symlink, virgolette e cartella corrente
    (BI 39d63da, nixos 5aa20f9, Baserow): nessun comando giudicato viene eseguito
    e la fixture `.env` contiene solo un valore finto."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.radice = Path(self._tmp.name).resolve() / "repo"
        (self.radice / "sub").mkdir(parents=True)
        (self.radice / "i1").mkdir()
        (self.radice / ".env").write_text("FIXTURE_NON_SECRET=example\n", encoding="utf-8")
        (self.radice / "goal.md").write_text("# goal\n", encoding="utf-8")
        (self.radice / "sub" / "nota.md").write_text("x\n", encoding="utf-8")
        destinazione = Path.home() / ".config" / "codex-policy-fixture-inesistente"
        self.assertFalse(destinazione.exists())
        self.symlink = True
        try:
            (self.radice / "alias").symlink_to(destinazione)
        except OSError:  # Windows senza privilegio di symlink
            self.symlink = False

    def tearDown(self):
        self._tmp.cleanup()

    def giudica(self, testo, cartella=None):
        return MODULE.giudica_comando(testo, LETTURE, self.radice, cartella)

    def negato(self, testo, atteso="", cartella=None):
        motivo = self.giudica(testo, cartella)
        self.assertIsNotNone(motivo, testo)
        self.assertIn(atteso, motivo, testo)

    def test_env_negato_in_ogni_forma(self):
        for testo in (
            "cat .env",
            "head .env",
            "tail .env",
            "head -n 3 .env",
            "tail -n3 .env",
            "cat '.env'",
            'cat ".env"',
            "cat \\.env",
            "cat -- .env",
            "cat goal.md .env",
            "cat .env | head",
            "cat ./.env",
            "cat sub/../.env",
            "cat .e*",
            "cat .en?",
            "cat < .env",
            "head<.env",
            "grep -f .env goal.md",
            "grep -f.env goal.md",
            "grep x .env",
            "git show HEAD:.env",
            "cd sub && cat ../.env",
            "cd sub; cat ../.env",
        ):
            self.negato(testo, ".env")

    def test_lettori_ricorsivi_sulle_cartelle_con_un_diniego(self):
        (self.radice / "backup").mkdir()
        for testo in (
            "grep -r x .",
            "grep -rn x",
            "grep -R x .",
            "rg x",
            "rg --hidden x",
            "rg -uu x .",
            "rg x backup",
        ):
            self.negato(testo, "ricorsiva")
        # `rg` salta i nascosti: `.env` non lo raggiunge, `backup/` sì.
        self.assertIsNone(self.giudica("rg x sub"))
        self.assertIsNone(self.giudica("grep -rn x sub"))
        self.assertIsNone(self.giudica("rg x sub goal.md"))

    def test_symlink_verso_un_diniego_anche_senza_barra(self):
        if not self.symlink:
            self.skipTest("symlink non creabili qui")
        for testo in ("head alias", "cat alias", "tail alias", "cat ./alias", "cat 'alias'"):
            self.negato(testo, "Read(~/.config/**)")

    def test_espansioni_che_solo_la_shell_conosce_cadono(self):
        for testo in (
            "cat $HOME/.config/x",
            "cat ${HOME}/x",
            'cat "$HOME/x"',
            "cat .{e,x}nv",
            "cat $'.env'",
            "cat <(cat .env)",
            "cat 'aperta",
            "cd - && cat x",
        ):
            self.negato(testo, "non scomponibile")

    def test_ammessi_i_pattern_le_opzioni_e_le_virgolette(self):
        for testo in (
            "cat goal.md",
            "cat 'goal.md'",
            "grep .env goal.md",
            "grep -n env goal.md",
            "grep -e .env goal.md",
            "head -n 5 goal.md",
            "cat *.md",
            "cat '*'",
            "cat goal.md # .env",
            "ls",
            "ls sub",
            "git status 2>&1 | head -5",
            "ls >/dev/null 2>&1",
            "cat goal.md > i1/copia.md",
            "grep 'a;b' goal.md",
            "grep '$(x)' goal.md",
            "cd sub && cat nota.md",
            "git show HEAD:goal.md",
        ):
            self.assertIsNone(self.giudica(testo), testo)

    def test_le_redirezioni_in_uscita_sono_scritture(self):
        self.negato("cat goal.md > CLAUDE.md", "Edit(./CLAUDE.md)")
        self.negato("cat goal.md >> o3/x.py", "non ammessa")
        self.negato("ls >&uscita.txt", "non ammessa")
        self.negato("ls; > CLAUDE.md", "Edit(./CLAUDE.md)")

    def test_cartella_di_lavoro_di_codex(self):
        self.negato("cat ../.env", "Read(./.env)", self.radice / "sub")
        self.assertIsNone(self.giudica("cat nota.md", self.radice / "sub"))
        ingresso = {
            "tool_name": "Bash",
            "tool_input": {"command": "cat ../.env", "workdir": "sub"},
            "cwd": str(self.radice),
        }
        self.assertIn("Read(./.env)", MODULE.giudica(ingresso, LETTURE))

    def test_regole_baserow_esatte_con_virgolette(self):
        for testo in BASEROW:
            self.assertIsNone(self.giudica(testo), testo)
            self.assertIsNone(self.giudica(testo + " 2>&1"), testo)
            self.assertIsNone(self.giudica(testo.replace("'", '"')), testo)
            self.negato(testo + " ; rm x", "Bash(rm *)")
        self.negato("docker inspect baserow --format '{{.Config.Env}}'", "non ammesso")
        self.negato("docker compose up -d", "docker compose up")
        self.negato("'cat' .env", "Bash(cat .env)")
        self.assertIsNone(self.giudica("docker compose ps"))

    def test_caricabile_senza_registrarsi_in_sys_modules(self):
        # Come lo caricano le riproduzioni degli adottanti (Baserow, BI).
        spec = importlib.util.spec_from_file_location("esecutore_isolato", SCRIPT)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        self.assertIsNotNone(modulo.giudica_comando("cat .env", LETTURE, self.radice))

    def test_nelle_regole_bash_solo_l_asterisco_e_jolly(self):
        self.assertTrue(MODULE.comando_ammesso("echo [x]", "echo [x]"))
        self.assertFalse(MODULE.comando_ammesso("echo y", "echo ?"))
        self.assertTrue(MODULE.comando_ammesso("echo y z", "echo *"))
        self.assertTrue(MODULE.comando_ammesso("cat", "cat *"))


class WindowsTests(unittest.TestCase):
    """La forma Windows simulata: barra rovescia letterale, dischi come `//c/…`,
    maiuscole indifferenti. Il comportamento reale di Codex su Windows resta da
    provare (danea-auto ce2a2f6)."""

    REGOLE: ClassVar[dict] = {
        "permissions": {
            "allow": ["Read(./**)", "Bash(cat *)", "Bash(type *)", "Edit(./i1/**)"],
            "deny": [
                "Read(//c/Users/me/.ssh/**)",
                "Edit(//c/Users/me/.ssh/**)",
                "Read(./.env)",
                "Bash(rm *)",
            ],
        }
    }

    def setUp(self):
        patcher = mock.patch.object(MODULE, "WINDOWS", True)
        patcher.start()
        self.addCleanup(patcher.stop)

    def giudica(self, testo):
        return MODULE.giudica_comando(testo, self.REGOLE, Path("C:/repo"))

    def test_path_di_windows_contro_le_regole_di_claude(self):
        for testo in (
            r"cat C:\Users\me\.ssh\id_rsa",
            "cat C:/Users/me/.ssh/id_rsa",
            r"cat c:\users\ME\.SSH\id_rsa",
            r"cat 'C:\Users\me\.ssh\id rsa'",
        ):
            self.assertIn("Read(//c/Users/me/.ssh/**)", self.giudica(testo) or "", testo)
        motivo = MODULE.giudica_file(r"C:\Users\me\.ssh\config", self.REGOLE, Path("C:/repo"))
        self.assertIn("Edit(//c/Users/me/.ssh/**)", motivo)

    def test_variabili_e_accento_grave_cadono(self):
        for testo in (
            r"cat $env:USERPROFILE\.ssh\x",
            r"type %USERPROFILE%\.ssh\x",
            "cat `$x",
        ):
            self.assertIn("non scomponibile", self.giudica(testo), testo)

    def test_maiuscole_nel_nome_e_nel_path(self):
        self.assertIn("Read(./.env)", self.giudica(r"type .\.ENV") or "")
        self.assertIn("non ammesso", self.giudica(r"TYPE goal.md") or "")
        self.assertIn("Bash(rm *)", self.giudica("RM x") or "")


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
    def esegui(self, eventi, uscita=0, stderr="", *extra):
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
                + ["--settings", str(impostazioni), *extra],
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

    def test_col_recinto_dell_host_codex_non_aggiunge_il_proprio(self):
        esito, _ = self.esegui([*AVVIO, MESSAGGIO, FINE], 0, "", "--recinto-host")
        self.assertEqual(esito.returncode, 0, esito.stderr)
        self.assertIn("danger-full-access", self.argomenti)
        self.assertNotIn("workspace-write", self.argomenti)
        self.assertFalse(any(a.startswith("sandbox_workspace_write") for a in self.argomenti))
        self.assertTrue(any(a.startswith("hooks.PreToolUse=") for a in self.argomenti))

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
