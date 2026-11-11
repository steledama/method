# Engine choice and fallback contract

The canonical launcher owns preflight, lock, deadline, remaining budget,
execution, concurrency checks, protected-path checks and closure. There is
one repository prompt, `o3/ciclo/prompt.md`, and one permission source,
`o3/ciclo/permessi.json`. Every engine uses that same source and the
repository's existing delegation. Switching engine grants no additional
authority.

## The repository chooses the engines (custodian, 2026-11-11)

The method is agnostic about model and operating system, so the engine is a
repository setting, not a host one. `o3/ciclo/lanciatore.toml`:

```toml
motori = ["claude", "codex"]   # the first works, the second takes over once
minuti = 45
budget_usd = 5                 # ceiling where the engine can enforce it
```

`motori` holds one or two of `claude` and `codex`, without repetitions;
default `["claude"]`. The order works both ways: `["codex", "claude"]` is
as valid as the reverse. An unknown engine or a malformed list exits 14.

The host supplies only what belongs to the machine: executable paths
(`--claude`, `--codex`, when not on PATH), sandbox (`--recinto`), stop
(`--recinto-ferma`) and trigger. It may still restrict with `--max-minuti`
and `--max-budget-usd`, never widen. The host does not choose the engine.
If none of the profile's engines is found, the launcher exits 14; a missing
first engine is an unavailability, and the second takes over.

## USD ceiling: preferred, not required

Decision of the custodian, 2026-11-11: custodian and both accounts are on
flat-rate plans. A USD ceiling is preferable where it can be enforced, but
its absence must not block a run or a fallback.

Claude enforces `--max-budget-usd`; Codex has no USD ceiling (it counts
tokens). Each attempt records `budget_usd_imposto`, and the closure declares
`budget_usd_imposto: false` whenever an engine ran without a ceiling. An
exhausted budget stops only an engine that enforces it. An unknown cost of a
previous attempt is not debited and does not block: the closure warns
(`<engine>: costo ignoto`). `costo_usd` sums the known USD costs. A token
budget is never reported as a USD ceiling. The wall-clock deadline always
covers all attempts.

## Observation and retry

Every closure records `engine`, ordered `engine_attempts` (engine, exit
status, trace path, observation, `budget_usd_imposto`), and
`provider_observation` for the final engine. An exit status of null means
execution did not return (for example timeout). `claude_exit` remains
Claude's exit status. Each observation preserves all `result` records, quota
events, structured errors, terminal reason and API error status. Raw traces
remain available. Missing fields remain unknown, rather than becoming success
or quota exhaustion.

`allowed_warning` and `overageStatus: rejected` with
`overageDisabledReason: out_of_credits` do not establish unavailability. Only
an explicit quota rejection, recognized availability/authentication error, or
missing executable can admit fallback. A successful result prevents
classifying that execution as unavailable. A builder panic, generic nonzero
exit, missing result, malformed trace or timeout does not trigger retry.

At most one attempt follows the first. It requires no tool invocation
(including reads), no permission denial, no malformed or unknown event, no
changed HEAD or tracked/untracked working tree, remaining time, and no
concurrent session detected. Any partial execution stops for review: an
unchanged working tree alone does not prove that external acts have not
occurred. There is no automatic replay or resume after partial acts.

## The canonical Codex executor

`o3/esecutore_codex.py`, in Python like the launcher, so one executor serves
every host, Windows included. The launcher calls it inside the same
`--recinto`, with the same termination mechanism:

```
python esecutore_codex.py --codex /path/to/codex \
  --prompt /abs/o3/ciclo/prompt.md --settings /abs/.git/lanciatore/settings.json
```

It runs `codex exec` with:

- `--json --ephemeral`: native events on stdout, no rollout, so the run is not
  seen as a concurrent Codex session;
- `--ignore-user-config --ignore-rules`: no user MCP servers, profiles or
  execpolicy rules; authentication still comes from `CODEX_HOME`;
- `--sandbox workspace-write` with `network_access=true` and the git common
  directory in `writable_roots`: without it `.git` is read-only and
  `git add` fails on `index.lock`;
- `approval_policy="never"`;
- one inline `PreToolUse` hook (`-c hooks.PreToolUse=…`), the executor itself
  in `--hook` mode, with `--dangerously-bypass-hook-trust`: an inline hook has
  no persisted trust, and its source is this canonical file;
- the `env` map of the settings exported to Codex and its commands (today
  `GIT_REFLOG_ACTION=lanciatore <id>`, which tells the run's commits apart).

The hook judges every call against the repository's Claude rules. `Bash`:
the command is split on `&&`, `||`, `;`, `|` and newlines; every piece must
match an `allow` pattern and no `deny` pattern; command or process
substitution is refused, being unjudgeable. Path arguments are checked
against `Read(…)` deny rules. `apply_patch`: every `Add`, `Update`, `Delete`
and `Move to` path must match an `Edit`/`Write` allow rule and no deny rule.
Other tools pass only if named in `allow`; `update_plan` is harmless and
passes. Then the settings' `Bash` hooks run with Claude-shaped input: the
launcher's commit-concurrency hook blocks with exit 2. Refusals answer with
`permissionDecision: deny`, are recorded and reach the closure as
`permission_denials`. A hook that cannot be evaluated refuses.

Events are normalized to the launcher's contract: `command_execution`,
`file_change` and every other started item become `assistant` `tool_use`;
`agent_message` becomes text; `turn.failed` and `error` become `error`;
in-turn CLI warnings (`item.type: error`) become `system`; an unknown
top-level event stays visible as `codex.<type>`, which the launcher reads as
an incomplete trace. The final `result` is successful only after
`turn.completed`, with exit 0 and no failure; `total_cost_usd` is null.

## Verified and still open

Verified live on Codex CLI 0.166.0 on 2026-11-11 (deck, throwaway repository,
custodian's explicit authorization): inline `-c` hooks run; a JSON deny
blocks the command (`Command blocked by PreToolUse hook`); `apply_patch`
reaches the hook with the patch in `tool_input.command`; settings env reaches
commands; `workspace-write` makes `.git` read-only and `writable_roots`
including it lets the commit succeed. Canonical tests cover the policy and
the normalization with a fake Codex: `python3 -m unittest tests.test_esecutore_codex`.

Still open, to verify before relying on the fallback:

- the end-to-end run through the launcher with real Codex
  (scratch script of 2026-11-11, to be run by the custodian);
- the form of a real Codex quota or authentication error: today recognized
  from the text (`usage limit`, `rate limit`, `429`, `unauthorized`); a new
  form must be added when observed;
- `git push` from inside the Codex sandbox (network enabled, not yet observed);
- Windows (danea-auto): the Codex sandbox there and the hook command quoting;
- hosted tools that hooks do not cover (web search): today they pass only if
  the repository allows `WebSearch`; otherwise they are not disabled in Codex.

## Adoption

1. Update the method checkout through the adopter's normal `/method`
   process. Repositories already using `o3/lanciatore.py` keep Claude alone:
   without `motori` nothing changes.
2. To enable a second engine, the repository adds `motori` to its profile.
   The host makes sure the binary is reachable inside the sandbox
   (`--codex` path, `CODEX_HOME` with `auth.json` readable, network allowed).
3. The host removes per-repository policy it still holds for other
   repositories (duration, budget): the profile is the source, and the host
   keeps only a physical backstop above the profile's `minuti`.
4. A first run with the fallback is a manual run with the custodian present.
   Timer activation stays with the host's local session.

Canonical tests:
`python3 -m unittest tests.test_lanciatore tests.test_esecutore_codex`.
