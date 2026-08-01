---
sintesi: "Applicare il rename sostantivo per cinque skill (kb-review→kb, method-review→method, adopters-review→adottanti, aggiorna-overlay→overlay, categorizza confermata categorizzazione senza cambio) e propagare i tre casi canonici ai quattro adottanti via prescrizione o3, secondo la decisione ratificata in i3/nome-skill-dominio-verbo-o-sostantivo.md."
ciclo: dev
---

# Rinomina le skill secondo la regola sostantivo, propaga i casi canonici

Verdetto e razionale vivono in
[i3/nome-skill-dominio-verbo-o-sostantivo.md](../i3/nome-skill-dominio-verbo-o-sostantivo.md);
qui restano la tabella di riferimento e il lavoro da fare.

## Tabella verificata (`ls` reale di `.claude/skills/`, 2026-08-01 — non la
fotografia di `kb/skill.md`, già stale su nixos alla data del controllo)

Canone (uguale nei cinque repo):

| Nome attuale | Bersaglio | Propagazione |
| --- | --- | --- |
| `eval` | invariato (abbreviazione, ambigua per costruzione) | — |
| `exec` | invariato (idem) | — |
| `kb-review` | `kb` | sì, 4 adottanti |
| `commit` | invariato (coincide già in inglese) | — |
| `method-review` (solo adottanti) | `method` | sì, 4 adottanti |

Dominio, per repo:

| Repo | Nome attuale | Bersaglio | Propagazione |
| --- | --- | --- | --- |
| metodo | `adopters-review` | `adottanti` | no, locale (non si forka) |
| nixos | `manutenzione` | invariato (già sostantivo) | — |
| nixos | `aggiorna-overlay` | `overlay` | no, locale |
| bi | `ordini` | invariato | — |
| bi | `categorizza` | `categorizzazione` | no, locale |
| bi | `tassonomia` | invariato | — |
| economia | `eval finanze` (scope) | invariato | — |
| economia | `eval posta` (scope) | invariato | — |
| economia | `eval registrazioni` (scope) | invariato | — |
| salute | `eval trascrizione` (scope) | invariato | — |

## Lavoro

1. **Canone** (`metodo`): rinominare le cartelle `.claude/skills/kb-review/`
   → `.claude/skills/kb/` e `.claude/skills/method-review/` →
   `.claude/skills/method/` (più wrapper Codex in `.codex/skills/`);
   aggiornare i riferimenti (`CLAUDE.md`, `commit/SKILL.md` passo 1, nodi
   collegati in `kb/`).
2. Emettere la prescrizione `o3/` per la propagazione ai quattro adottanti
   dei due rename canonici (stesso schema di `skill-per-arco`).
3. **Locale**: rinominare `adopters-review`→`adottanti` in `metodo`
   (nessuna propagazione — non forka).
4. Segnalare a `nixos` (prossimo `method-review` locale, non con
   propagazione forzata da qui) il bersaglio `aggiorna-overlay`→`overlay`:
   è una skill autonoma nixos, la rinomina la fa `nixos` stesso.
5. `categorizza`/`categorizzazione` in `bi`: nessuna azione, il nome attuale
   è già corretto.

## Criterio di chiusura

Task chiuso quando: le due cartelle canoniche sono rinominate in `metodo`, la
prescrizione di propagazione è recepita dai quattro adottanti (marker
`method-review.md` aggiornati), e `adopters-review`→`adottanti` è applicato
localmente. Il punto 4 (`aggiorna-overlay`) non blocca la chiusura: è un
suggerimento a `nixos`, non un obbligo di propagazione da questo repo.
