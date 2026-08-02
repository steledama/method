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

| Nome attuale                     | Bersaglio                                          | Propagazione    |
| -------------------------------- | -------------------------------------------------- | --------------- |
| `eval`                           | invariato (abbreviazione, ambigua per costruzione) | —               |
| `exec`                           | invariato (idem)                                   | —               |
| `kb-review`                      | `kb`                                               | sì, 4 adottanti |
| `commit`                         | invariato (coincide già in inglese)                | —               |
| `method-review` (solo adottanti) | `method`                                           | sì, 4 adottanti |

Dominio, per repo:

| Repo     | Nome attuale                 | Bersaglio                  | Propagazione              |
| -------- | ---------------------------- | -------------------------- | ------------------------- |
| metodo   | `adopters-review`            | `adottanti`                | no, locale (non si forka) |
| nixos    | `manutenzione`               | invariato (già sostantivo) | —                         |
| nixos    | `aggiorna-overlay`           | `overlay`                  | no, locale                |
| bi       | `ordini`                     | invariato                  | —                         |
| bi       | `categorizza`                | `categorizzazione`         | no, locale                |
| bi       | `tassonomia`                 | invariato                  | —                         |
| economia | `eval finanze` (scope)       | invariato                  | —                         |
| economia | `eval posta` (scope)         | invariato                  | —                         |
| economia | `eval registrazioni` (scope) | invariato                  | —                         |
| salute   | `eval trascrizione` (scope)  | invariato                  | —                         |

## Lavoro

1. ✅ **Canone** (`metodo`): cartelle rinominate (`.claude/skills/kb/`,
   `.claude/skills/method/`, wrapper Codex corrispondenti); riferimenti
   aggiornati (`CLAUDE.md`, `README.md`, `commit/SKILL.md`, `eval`/`exec`,
   nodi collegati in `kb/`, register `goal.md`, `o1/plan.md`).
2. ✅ Prescrizione emessa: `o3/skill-nomi-verbo-sostantivo.md`, stesso schema
   di `skill-per-arco`. Resta il recepimento dei quattro adottanti.
3. ✅ **Locale**: `adopters-review`→`adottanti` applicato in `metodo`
   (nessuna propagazione — non forka).
4. ✅ Raccomandazione forte (non obbligo) incisa nella stessa prescrizione
   `o3/skill-nomi-verbo-sostantivo.md`: `aggiorna-overlay`→`overlay` per
   `nixos` — resta una skill autonoma nixos, la rinomina la fa `nixos`
   stesso, ma ora è un item esplicito della prescrizione invece che una nota
   informale.
5. ✅ Stessa prescrizione: raccomandazione a `bi` di verificare sull'`ls`
   reale locale il nome vivo di `categorizza`/`categorizzazione` — la
   ricognizione di `metodo` lo classifica già conforme, ma la fotografia può
   essere stale.

## Criterio di chiusura

Task chiuso quando: le due cartelle canoniche sono rinominate in `metodo`
(fatto), la prescrizione di propagazione è recepita dai quattro adottanti
(marker aggiornati — **in attesa**), e
`adopters-review`→`adottanti` è applicato localmente (fatto). Il punto 4
(`aggiorna-overlay`) non blocca la chiusura: è un suggerimento a `nixos`, non
un obbligo di propagazione da questo repo.

**Nota**: la clausola §3 della prescrizione («il marker non cambia nome») è
superata da [i3/allineamento-marker-stadio.md](../i3/allineamento-marker-stadio.md)
— il marker trasloca a `i3/allineamento-metodo.md`, non resta
`method-review.md` in root. Il lavoro di prescrizione e propagazione per
questo punto vive ora in
[o2/marker-allineamento-i3.md](marker-allineamento-i3.md), non qui.
