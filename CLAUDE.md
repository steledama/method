# CLAUDE.md

Regole operative per agenti che lavorano su questo repository.

## Bootstrap di sessione

La root è l'**atrio** dell'artefatto: l'`ls` dichiara l'inventario. I _file-ciclo_ si leggono a ogni sessione; le _porte-collezione_ (`kb.md`, `tools.md`, `perceptions.md`, `interpretations.md`, `prescriptions.md`, `sources.md`) si vedono ma si aprono on-demand. Ordine: `README → CLAUDE → nodo`.

1. `README.md` — la bussola: scopo, dominio in breve, orientamento operativo; punta a `plan.md` (lavoro), `kb.md` (catalogo), `interpretations/` e nodi (modello)
2. nodo pertinente alla modifica richiesta

## Operazioni consentite senza autorizzazione

- modifica ai nodi in `kb/`
- aggiornamento di `README.md`, `plan.md` e `verdict.md`
- commit e operazioni git locali

## Skill

La triade operativa del metodo e la skill di allineamento vivono versionate anche
qui (`metodo` fa dogfooding ed è la copia canonica di riferimento):
`.claude/skills/` con wrapper Codex in `.codex/skills/`.

- `/kb-review` — health check della KB via `tools/kb_tools.py` (diagnosi, non corregge)
- `/tasks-review` — supervisione di `plan.md`/`tasks/`: drift, priorità, dipendenze, prossimo task
- `/commit` — gate di filing back prima di fissare le modifiche nella storia
- `/method-review` — revisione del drift tra un adottante e i commit di `method`

Le skill sono interfacce sugli strumenti versionati, non documentazione: cfr.
[skill](kb/skill.md). Gli adottanti le forkano e le parametrizzano.

## Memoria

Non usare il sistema di memoria dell'harness (`auto-memory`, store in
`~/.claude/projects/.../memory/`): il contenuto è host-locale, opaco e non versionato
— l'anti-pattern dell'artefatto portabile. La memoria del progetto vive versionata nel
repo: `verdict.md` (perché una decisione conta), nodi `kb/` (conoscenza stabile), `tasks/`
(lavoro futuro e contesto).

L'enforcement (spegnere la feature) è invece versionabile: vive in `nixos` — env var
`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `modules/home/claude-code.nix`, specchio di
`DISABLE_AUTOUPDATER`. Su harness che non leggono questi settings (Codex) vale solo
questa regola.

## Tabelle vs elenchi

Le tabelle markdown sono illeggibili su schermi stretti (mobile): preferire elenchi puntati per confronti e liste di voci. Eccezione: `plan.md` (forma tabellare canonica, cfr. `kb/plan.md`).

## Quando aggiungere un nodo

Un nodo entra in `kb/` solo se il concetto è metodologico e applicabile ad almeno due progetti diversi. I concetti specifici di un singolo progetto restano nella `kb/` locale del progetto.

Procedura: creare il file in `kb/` seguendo la struttura in `kb/node.md`, aggiungere riga al catalogo in `README.md`.

## Quando aggiornare un nodo esistente

Aggiornare quando una modifica del metodo in un progetto è generalizzabile. Verificare che la modifica non rompa il senso per gli altri progetti adottanti. Se la modifica è domain-specific, inserirla nella sezione "Adattamento al dominio" del nodo (come in cognitive-fidelity) invece di modificare il corpo principale.

## Come propagare modifiche ai progetti collegati

I progetti leggono i nodi via symlink — vedono automaticamente le modifiche. Non serve aggiornamento manuale salvo che cambi nome o path di un nodo: in quel caso aggiornare i link nei `CLAUDE.md` e `README.md` di tutti i progetti collegati.

## Push remoto

Mai automatico, sempre su richiesta esplicita.
