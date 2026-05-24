---
data: 2026-05-24
stato: aperto
---

# Osservatorio metodo su bi

## Contesto

`bi` e il caso guida per un progetto applicativo complesso: molti flussi,
dipendenze operative tra script, Baserow, WooCommerce, dati e task strutturali.
La fotografia iniziale del 2026-05-23 lo indicava anche come caso principale di
drift di `CLAUDE.md`; la revisione e stata completata nel repo `bi` con il
commit `b195b8ff docs(kb): compatta CLAUDE e chiudi task metodo`.

Questo task resta nel repo `metodo` per monitorare gli aspetti metodologici
cross-repo senza duplicare task nel README di `bi`.

## Verifiche

- verificare nel prossimo confronto che `bi/CLAUDE.md` resti costituzione
  operativa e non torni a essere manuale di dominio
- valutare se il numero e la complessita dei task richiedano una skill locale
  `revisione-tasks` o se basti una checklist forte in `CLAUDE.md`
- confrontare `bi/.claude/skills/audit-kb` e `commit` con gli altri repo per
  capire cosa e portabile e cosa e configurazione locale
- mantenere `graphify` come caso di skill locale realmente domain/tool-specific
- verificare corrispondenza README `Tasks aperti` <-> `todo/` e stati canonici
  dei task
- verificare quali comandi di `scripts/kb_tools.py` sono comuni e quali sono
  specifici del dominio BI

## Soglia locale

Aprire un task in `bi` solo quando l'azione diventa lavoro autonomo sul dominio
BI, per esempio modifica puntuale di `CLAUDE.md`, nodi, script o skill locali.
Le verifiche metodologiche restano qui.

## Output atteso

- esito aggiornato nel confronto cross-repo
- eventuale decisione su checklist vs skill `revisione-tasks`
- eventuali task locali solo se il lavoro non e piu una verifica metodologica
