---
data: 2026-05-24
stato: aperto
---

# Osservatorio metodo su salute

## Contesto

`salute` e il caso guida per KB ampie, riflessive e semantiche: molti nodi,
fonti testuali, diario, pratica, filing back e scadenze personali. La fotografia
cross-repo ha evidenziato task locali gia aperti per mappa autonoma e principi
specifici del dominio; quei task restano in `salute` perche producono contenuto
locale.

Qui resta la verifica metodologica: cosa generalizzare per KB non tecniche e
come evitare duplicazione tra task centrali e task locali.

## Verifiche

- chiarire il criterio tra righe README-only per ingest semplice e task
  sostanziali con file `todo/`
- valutare se la revisione task debba restare checklist in `CLAUDE.md` o
  diventare skill locale, eventualmente collegata a ingest e filing back
- seguire l'esito dei task locali `mappa-progetto.md` e
  `principi-specifici-dominio.md` solo per estrarre generalizzazioni di metodo
- valutare se il loop teoria -> pratica -> verifica richieda un nodo metodo,
  una skill locale o resti specifico di `salute`
- confrontare `elabora-trascrizione` con le altre skill per distinguere skill
  locale sana da possibile pattern portabile
- verificare come una KB riflessiva debba fare fedelta cognitiva senza
  ridursi a fact check tecnico

## Soglia locale

Restano in `salute` i task che producono nodi, mappa, principi, ingest o
pratiche del dominio. Restano in `metodo` le regole generali su README-only vs
`todo/`, filing back, skill e fedelta qualitativa.

## Output atteso

- criterio metodologico per task README-only vs file `todo/`
- eventuale aggiornamento dei nodi `task-aperti`, `todo`, `skill` e
  `fedelta-cognitiva`
- nessuna duplicazione dei task locali di `salute` nel repo metodo
