---
data: 2026-05-24
stato: aperto
---

# Osservatorio metodo su economia

## Contesto

`economia` e il caso guida per task operativi legati a scadenze, pratiche,
fonti autoritative, dati JSON e stato corrente. E gia il riferimento positivo
per la skill `revisione-tasks`: controllo iniziale in `CLAUDE.md`, revisione a
fine sessione quando cambiano fatti, scadenze o dipendenze, e scelta del task
consigliato.

Il task locale `economia/todo/correzione-audit-kb.md` resta nel repo
`economia`, perche corregge direttamente la KB del progetto. Qui resta invece
la lettura metodologica del caso.

## Verifiche

- usare `economia` come baseline per valutare quando una skill
  `revisione-tasks` diventa necessaria negli altri repo
- osservare come `stato.md`, `scadenze.md`, `diario.md`, output JSON e mappa
  interagiscono con README e `todo/`
- verificare se i controlli `facts` e audit locali suggeriscono una superficie
  portabile oppure restano necessariamente domain-specific
- monitorare la chiusura locale di `correzione-audit-kb.md` e registrare nel
  metodo solo le generalizzazioni emerse
- confrontare skill `audit-kb`, `commit` e `revisione-tasks` con gli altri repo
- verificare se l'uso di Google Workspace CLI produce pattern cross-repo o resta
  documentazione locale/nixos-specifica

## Soglia locale

Restano in `economia` i task su pratiche, scadenze, documenti, audit della KB
locale e dati del progetto. Restano in `metodo` le decisioni sulla portabilita
di skill, strumenti, fonti di verita e governance task.

## Output atteso

- criteri piu chiari per adottare `revisione-tasks` negli altri repo
- eventuali aggiornamenti ai nodi `task-aperti`, `skill`, `fonte-di-verita` o
  `fedelta-cognitiva`
- nessuna duplicazione dei task operativi di `economia` nel repo metodo
