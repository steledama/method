---
ciclo: runtime
stato: aperto
sintesi: Scrivere la prescrizione o3 dei poli-register (goal.md/world.md, quartetto di review) e seguirne il recepimento nei quattro adottanti, pilota economia
---

# Propagazione poli-register e quartetto di review

Il canone è ratificato (filo
[poli-register-goal-world](../i3/poli-register-goal-world.md)): i register
dell'atrio sono i due poli — `goal.md` gemello di `world.md` (che assorbe
`map.md` e `sources.md`) — e il quartetto di review sostituisce la triade
(`plan-review` rinomina di `tasks-review`, `verdicts-review` nuova). `metodo` è
già materializzato. Resta la propagazione: una prescrizione o3 per repo,
recepita dal `method-review` di ciascun adottante.

## Contenuto della prescrizione (da scrivere in `o3/`)

Per ogni adottante:

1. **`goal.md`** — creare il register del polo Goal: intro = il motivo in
   sintesi (la home lo rende), obiettivi di livello azione con segnali e lavoro
   corrente, sezione «Goal di sviluppo» (posizione sulle dimensioni comuni),
   disciplina col custode umano dichiarato. Il contenuto lo porta il custode:
   la prescrizione dà la forma, non il nord.
2. **`map.md` → `world.md`** — rinominare e riorganizzare: intro = la visione
   del Mondo (ex `### World` del README), sezioni superfici della membrana
   (incluse quelle multiple, es. Drive foto in `bi`), territorio (l'ex mappa),
   fonti (l'ex `sources.md` dove esiste; `salute` ne era priva per divergenza
   dichiarata).
3. **README** — asciugare la sezione canonica: `## Metodo` con dichiarazione e
   puntatori ai register; via `### Goal` e `### World`.
4. **Builder della home** — fork di `register_intro` (H1 → primo H2) al posto
   di `canonical_readme_section`; i poli si leggono dai register.
5. **Skill** — rinomina `tasks-review`→`plan-review` (con lente
   task→obiettivo), fork di `verdicts-review`, wrapper Codex; aggiornare
   CLAUDE/README locali.
6. **Link al canone** — i riferimenti a `method/map.md` e `method/sources.md`
   non esistono più: puntare a `method/world.md`/`method/goal.md` (nodi
   `kb/world.md`, `kb/goal.md`).

## Sequenza

- **`economia` pilota** — il banco più severo: register assente e sintomo
  avanzato (46 righe di narrativa di stato nel plan da bonificare col primo
  giro di `verdicts-review`).
- **`bi`** — a metà strada: `goal.md`, `plan-review` e `verdicts-review` già
  nati lì (`52b2b600`); restano fusione `map.md`→`world.md`, README, builder.
- **`salute`**, **`nixos`** — recepimento pieno; in `nixos` la mappa
  host/moduli diventa la sezione territorio di `world.md`.

I cocci del pilota si incidono nel runbook prima degli altri recepimenti, come
per la prescrizione dell'atrio.
