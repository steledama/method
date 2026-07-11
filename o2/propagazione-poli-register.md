---
sintesi: Seguire il recepimento della prescrizione poli-register (o3/poli-register.md) nei quattro adottanti. Recepita da economia (pilota, 74c56c6), nixos (2026-07-10, marker a 33f9cd8) e bi (2026-07-11, marker a 2f2f39a). Resta salute.
ciclo: runtime
---

# Propagazione poli-register e quartetto di review

Il canone è ratificato (filo
[poli-register-goal-world](../i3/poli-register-goal-world.md)) e la
prescrizione è **scritta**: [`o3/poli-register.md`](../o3/poli-register.md) —
ricetta in sette passi (passo-cuore: il register `goal.md` col custode umano),
touchpoint per-repo e ordine. `metodo` è già materializzato. Questo task
traccia il recepimento, che ogni adottante compie col proprio `method-review`.

## Recepimento

- **`economia`** — **recepito** (2026-07-09, commit `74c56c6`, marker
  `method-review.md` a `3609404`). Pilota completato: `goal.md` e `world.md`
  sono register di root, `tasks-review` è diventata `plan-review`,
  `verdicts-review` è installata, README/CLAUDE/AGENTS/home sono riallineati e
  il primo giro ha spostato il peso valutativo su fili i3 con `misura:` verso
  `goal.md`. Il plan resta coda pura: le cause delle attese sono ancora
  motivate, ma non più l'unico luogo della narrativa di stato.
- **`nixos`** — **recepito** (2026-07-10, marker `method-review.md` a
  `33f9cd8`): prescrizione recepita per intero nel giro `9af40939..33f9cd84`;
  `plan-review`/`verdicts-review` parametrizzate sui segnali di dominio
  (rebuild/boot, dipendenze `world`, drift facts/fidelity), home che rende i
  poli dall'intro dei register come il canone.
- **`bi`** — **recepito** (2026-07-11, marker `method-review.md` a `2f2f39a`,
  `status: aligned`, intervallo `bc0b860..2f2f39a`): register gemelli
  `goal.md`/`world.md` (fusione `map.md` compiuta, superfici `world` in home
  dichiarate nel register), quartetto completo in `.claude/skills/`,
  README/home riallineati. Origine di register e coppia (`52b2b600`): il suo
  marker registra che il canone li ha ratificati a valle.
- **`salute`** — ultimo; attenzione alla divergenza dichiarata su
  `sources.md` (la sezione fonti non è un obbligo) e alla centralità del
  custode (motivo non esternalizzabile). Non verificabile da questo host
  (nessun checkout locale): il recepimento passa dal suo `method-review`.

Il task chiude quando i quattro marker sono avanzati e la prescrizione si
rimuove dalla collezione (la storia resta in git).
