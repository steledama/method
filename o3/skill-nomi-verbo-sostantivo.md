---
data: 2026-08-01
stato: attiva
ciclo: runtime
target: nixos, salute, economia, bi
---

# Rename sostantivo delle due skill canoniche in `-review`

## Cosa e perché

Il sostantivo vince sull'imperativo verbo per i nomi delle skill (ratifica
2026-08-01, filo `i3/nome-skill-dominio-verbo-o-sostantivo.md`, corollario in
`kb/skill.md`, «La regola dei nomi»): un imperativo ripetuto a ogni
invocazione suona da comando, non da capacità permanente. Dei cinque nomi
decisi, due sono **canonici** — uguali nei cinque repo, forkati dagli
adottanti — e questa prescrizione ne propaga il rename:

- `kb-review` → `kb`
- `method-review` (solo adottanti, `metodo` non la espone) → `method`

`adopters-review` → `adottanti` non è nemmeno un caso di questa prescrizione:
è locale a `metodo`, il cui Mondo sono gli adottanti stessi — non si forka e
non c'è nulla da recepire altrove.

I restanti due casi sono di **dominio** (non canone: nomi diversi da repo a
repo, decisi dall'adottante) ma nascono dalla stessa regola ratificata, e
questa prescrizione li porta come **raccomandazione forte**, non come
propagazione forzata — la decisione e i tempi restano dell'adottante:

- **`nixos`**: `aggiorna-overlay` → `overlay`. Stesso principio del rename
  canonico (sostantivo, non verbo): applicalo quando conviene, non c'è
  obbligo di sincronia con questa prescrizione.
- **`bi`**: verifica il nome vivo di `categorizza`. La ricognizione di
  `metodo` (tabella in `o2/skill-nomi-verbo-sostantivo.md`) l'ha classificato
  già conforme — sostantivo `categorizzazione`, non azione — quindi
  presumibilmente nessun cambio è dovuto; ma la fotografia può essere
  stale (cfr. `cognitive-fidelity`): conferma sull'`ls` reale locale prima di
  chiudere la voce.

`metodo` ha già applicato il rename canonico
(`.claude/skills/kb/`, `.claude/skills/method/`, wrapper Codex
corrispondenti) e aggiornato i propri riferimenti (`CLAUDE.md`, `README.md`,
`commit/SKILL.md`, i nodi `kb/` collegati). Il dettaglio del lavoro e la
tabella verificata sono in `o2/skill-nomi-verbo-sostantivo.md` di `method`.

## La ricetta (nel lessico del metodo)

1. **Rinomina le cartelle** delle due skill forkate: `.claude/skills/kb-review/`
   → `.claude/skills/kb/`, `.claude/skills/method-review/` →
   `.claude/skills/method/` (più i wrapper corrispondenti in
   `.codex/skills/`, se presenti). Il contenuto locale (parametrizzazioni,
   esempi di dominio) migra col rename, non si ricopia dal canone.
2. **Aggiorna i riferimenti locali** al vecchio nome: l'elenco skill in
   `CLAUDE.md`/`README`, eventuali righe `## Scadenze` che citano le skill per
   nome, i nodi `kb/` forkati che le menzionano, e qualunque skill di dominio
   il cui testo le nomini. Fai un grep mirato (`kb-review`, `method-review`)
   e classifica: riferimenti operativi/normativi si migrano al nome nuovo, i
   fili storici che narrano un fatto passato datato conservano il nome che
   descriveva quel fatto in quel momento — non si riscrive la storia.
3. **Il marker non cambia nome**: `method-review.md` nella root dell'adottante
   resta `method-review.md` — è il file del ledger, non il nome della skill
   che lo gestisce. Solo la skill che lo legge/scrive si chiama ora `method`.
4. **Recepimento ordinario**: canale `method` (ex `method-review`), marker
   avanti dopo la classificazione.

Nessun impatto sul contratto plan×`o2/`: il rename tocca solo `.claude/skills/`
e `.codex/skills/`, non le collezioni `o1`/`o2`/`o3`.

## Ordine e chiusura

Si recepisce in qualunque ordine, al prossimo `method` di ciascun adottante.
Resta attiva finché i quattro non hanno rinominato le due cartelle canoniche e
aggiornato i propri riferimenti; recepita da tutti, si rimuove dalla
collezione — la storia resta in git. Le due raccomandazioni di dominio
(`nixos`, `bi`) non bloccano la chiusura: sono lette e decise, non eseguite
per obbligo di questa prescrizione.
