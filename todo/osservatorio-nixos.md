---
data: 2026-05-24
stato: aperto
---

# Osservatorio metodo su nixos

## Contesto

`nixos` e il riferimento per progetti code-based dichiarativi: README compatto,
mappa forte, strumenti anti-drift maturi e fonte di verita tecnica verificabile.
La sua implementazione di `kb_tools.py` include comandi avanzati come
`inventory`, `facts`, `coverage` e `fidelity`.

Questo task centralizza nel repo `metodo` le verifiche metodologiche su `nixos`
senza aprire task locali quando il lavoro non e ancora autonomo di dominio.

## Verifiche

- controllare corrispondenza README `Tasks aperti` <-> `todo/`, inclusi task
  completati residui e stati non canonici
- verificare se una checklist leggera in `CLAUDE.md` e sufficiente per la
  revisione task, dato il numero ridotto di task tecnici
- confrontare i sottocomandi avanzati di `scripts/kb_tools.py` con la superficie
  portabile del repo metodo
- capire quali parti di `facts` e `fidelity` sono generalizzabili ai progetti
  code-based e quali restano NixOS-specifiche
- mantenere `nixos` come riferimento per installazione o runbook di strumenti
  runtime, senza spostarli in `metodo` prima di una decisione cross-repo
- valutare l'impatto del symlink `metodo/ -> ../metodo/kb` se in futuro il
  metodo avra anche `tools/` o `skills/`

## Soglia locale

Aprire task in `nixos` solo per interventi concreti sul sistema, sui moduli Nix,
sugli script o sulla documentazione locale. Le valutazioni di portabilita
restano in `metodo`.

## Output atteso

- decisione su quali controlli anti-drift code-based possono diventare
  portabili
- eventuali aggiornamenti a `strumenti-kb` e `fedelta-cognitiva`
- conferma o correzione del bootstrap task in `CLAUDE.md`
