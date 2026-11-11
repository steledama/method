# Engine fallback contract

The canonical launcher owns preflight, lock, deadline, remaining budget,
execution, concurrency checks, protected-path checks and closure. There is
one repository prompt, `o3/ciclo/prompt.md`. Claude and Codex must use that
same source and the repository's existing delegation. Switching engine grants
no additional authority.

## Observation and retry

Every closure records `engine`, ordered `engine_attempts` (engine, exit status,
trace path and observation), and `provider_observation` for the final engine.
An exit status of null means execution did not return (for example timeout).
Existing `claude_exit` remains Claude's exit status, even after fallback.
`costo_usd` totals the known costs of both attempts. Each attempt and the
closure record `budget_usd_imposto`: `false` when the Codex attempt ran without
a USD ceiling (see below).
Each observation preserves all `result` records, quota events, structured
errors, terminal reason and API error status. Raw traces remain available.
Missing fields remain unknown, rather than becoming success or quota exhaustion.

`allowed_warning` and `overageStatus: rejected` with
`overageDisabledReason: out_of_credits` do not establish unavailability.
Only an explicit quota rejection, recognized provider availability/authentication
error, or missing Claude executable can admit fallback. A successful result
prevents classifying that execution as unavailable. A builder panic, generic
nonzero exit, missing result, malformed trace or timeout does not trigger retry.

At most one Codex attempt follows Claude. It requires no tool invocation
(including reads), no permission denial, no malformed or unknown event, no
changed HEAD or tracked/untracked working tree, known spent cost, remaining
time and budget (budget only when a USD ceiling applies), and no concurrent
session detected. Any partial execution
stops for review: an unchanged working tree alone does not prove that external
acts have not occurred. There is no automatic replay or resume after partial acts.
The original deadline and budget cover both attempts; results report cumulative
cost within one engine, so only its last cumulative cost is debited.

## USD ceiling: preferred, not required (custodian, 2026-11-11)

Decision of the custodian, forwarded by the nixos session on 2026-11-11: the
custodian and both accounts (Claude and Codex) are on flat-rate plans. A USD
ceiling is preferable whenever it can be enforced, but its absence must not
block the fallback: having the fallback matters more than that detail.

The host chooses with `--codex-senza-tetto-usd`. Without it the launcher passes
`--budget-usd REMAINING` and the executor must enforce it or fail before
starting Codex. With it the launcher passes `--senza-tetto-usd` instead, an
unknown Claude cost no longer blocks the fallback, and the closure declares
`budget_usd_imposto: false`. The choice is explicit and visible in every
closure; a token budget is never reported as a USD ceiling. The wall-clock
deadline still covers both attempts.

The other constraints are unchanged and still to be evaluated for Codex:
allowed commands, protected paths, the commit concurrency hook, sandbox and
stop. Neither this decision nor flat-rate pricing relaxes them.

## Codex integration boundary

Enable with `--codex-adapter /absolute/path/to/executor`. This is an explicit
host integration, not an alias for the `codex` binary. The launcher calls it
inside the same `--recinto`, with the same termination mechanism:

```
executor --prompt /absolute/path/to/o3/ciclo/prompt.md \
  --settings /absolute/path/to/.git/lanciatore/settings.json \
  (--budget-usd REMAINING | --senza-tetto-usd)
```

The settings carry an `env` map (today `GIT_REFLOG_ACTION=lanciatore <id>`,
which lets the closure tell the run's commits from other sessions'): the
executor must export it to Codex and its tool processes.

The executor must run Codex noninteractively, read the given prompt without
copying it, enforce the supplied permission policy, deny unattended approval,
apply the supplied commit concurrency hook, enforce the remaining monetary
ceiling when `--budget-usd` is given, and preserve the host's filesystem/network/process restrictions.
It must fail before starting Codex if it cannot enforce any required boundary.
The launcher enforces the remaining wall-clock limit and kills the process tree.

The executor emits JSONL using the launcher's existing event contract:
`assistant.message.content[].type: tool_use` for every tool invocation,
`rate_limit_event.rate_limit_info` for quota observations, `error` for failures,
and a final `result` with `is_error`, `terminal_reason`, `api_error_status`,
`total_cost_usd`, `result` and available usage fields. Native Codex events must
be normalized by the executor; do not claim a successful result without a
successful terminal event. Preserve native diagnostics in the trace as structured
error data. Failures must return nonzero. No prompt, lock, preflight, retry or
closure logic belongs in this executor.

A generic Codex `workspace-write` sandbox does not enforce Claude's command
allowlist, protected reads or commit hook. This change therefore supplies the
canonical orchestration and adapter contract, **not a verified Codex executor**.
Without an explicitly configured equivalent executor, fallback remains disabled
and the closure explains why. Never pass the bare Codex binary to this option.

### Where the executor lives (2026-11-11)

The custodian wants the fallback on danea-auto (Windows) too. The executor's
work (JSONL normalization, translation of the permission policy, hooks) is
portable, so it belongs in the canon next to `o3/lanciatore.py`, in Python like
it: one executor for every host, Windows included, instead of one per host.
Hosts keep only what is theirs today with `--claude`: sandbox (`--recinto`),
stop (`--recinto-ferma`) and the path of the Codex binary. Proposed by nixos,
adopted by method; the canonical executor is not written yet and the task is
`o2/lanciatore-ciclo-nel-metodo.md`.

Official reference for native JSONL execution:
[Codex non-interactive mode](https://developers.openai.com/codex/noninteractive).

## Adoption, including nixos

1. Update the method checkout through the adopter's normal `/method` process.
   Repositories already using `o3/lanciatore.py` receive observation without
   changing their invocation. Legacy `ciclo-chiusura.sh` does not gain it.
2. For legacy systemd cycles, migrate the host adapter to the canonical launcher;
   retain its sandbox, lock ownership, stop command, deadline and local delegation.
   Keep the nixos timer suspended during the server-only migration.
3. Implement and validate the equivalent Codex executor in the host integration.
   Exercise rejected quota, allowed warning, authentication failure, missing
   executable, timeout, partial external acts, denied paths/commands, commit
   concurrency and monetary ceiling. Test with fake agents before live use.
4. Only then configure `--codex-adapter`. Do not reactivate a timer as part of
   receiving this contract. Host activation remains with its local session.

Canonical tests: `python3 -m unittest discover -s tests -p test_lanciatore.py`.

## Host verification received on 2026-11-11

The nixos session reported a read-only inspection of the installed inactive
unit on norvegia and Codex CLI 0.166.0; no agent or host change was performed.
The unit has writable home/checkout, no effective network or inaccessible-path
filter, and only `o3/ciclo` read-only. `ReadWritePaths` is not a global whitelist
without an enclosing read-only filesystem. `NoNewPrivileges` does not revoke
services or sockets already accessible to the UID. BI/Baserow configuration
also leaves checkout and service surfaces writable; these were configuration
findings, not remote observations.

Reusable primitives are read-only/inaccessible mounts, cgroups, deadline and
entry guards. They do not enforce Claude's command allowlist, an in-run commit
hook or a USD ceiling. PATH wrappers cannot prevent absolute executable paths.
The installed Codex `exec` help exposes no USD budget option. Documented hooks
and experimental token rollout budgets do not establish equivalent enforcement;
no hook validation on that installed version has been performed.

Therefore the current server-only host integration cannot enable this fallback.
Keep `--codex-adapter` unset and the timer suspended. A future implementation
should reuse one validator of the source policy and minimal harness backends,
with explicit tests for capabilities it cannot reproduce. Do not silently
downgrade policy. The missing USD ceiling is no longer a blocker: since the
custodian's decision above it is an explicit host choice declared in the
closure, never a token budget presented as a USD ceiling.
