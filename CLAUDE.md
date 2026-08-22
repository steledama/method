# CLAUDE.md

Regole operative per agenti che lavorano su questo repository.

## Bootstrap di sessione

La root contiene le collezioni `i1/`–`i3/` e `o1/`–`o3/`, ciascuna col
proprio indice, più `kb/`, `presentation/` e i register `goal.md` e
`world.md`. Il cruscotto è `o1/plan.md` con i fili pertinenti in `i3/`;
catalogo, register e altre collezioni si aprono quando servono. Gli item delle
collezioni dichiarano `ciclo: dev|runtime`. Ordine di lettura:
`README → CLAUDE → nodo pertinente`.

1. `README.md` — la bussola: scopo, dominio in breve, orientamento operativo; punta a `o1/plan.md` (lavoro), `kb/kb.md` (catalogo), `i2/` e nodi (modello)
2. nodo pertinente alla modifica richiesta

## Operazioni consentite senza autorizzazione

- modifica ai nodi in `kb/`
- aggiornamento di `README.md`, `o1/plan.md` e dei fili in `i3/`
- commit e operazioni git locali

## Skill

Il quartetto operativo del metodo e la skill di allineamento vivono versionati anche
qui (`metodo` fa dogfooding ed è la copia canonica di riferimento):
`.claude/skills/` con wrapper Codex in `.codex/skills/`.

- `/eval [perceive|interpret|compare|all]` — il braccio di valutazione: raccolta del grezzo (i1), sintesi con provenienza e cascata (i2), verdetto dei fili contro `goal.md` e bonifica del plan (i3)
- `/exec [plan|specify|perform|all]` — il braccio di esecuzione: coda e priorità (o1), qualità interna dei task (o2), supervisione della collezione e atti autorizzati (o3)
- `/kb [audit|review]` — audit deterministico o revisione semantica profonda
  della KB (diagnosi, non corregge; capacità trasversale ai due archi)
- `/commit` — gate di filing back prima di fissare le modifiche nella storia
- `/method` — revisione del drift tra un adottante e i commit di `method`

Skill di dominio (il Mondo runtime di `metodo` sono gli adottanti; non si forka):

- `/adottanti` — audit runtime-o1 mensile dei sei adottanti: canale del canone e distanza dal telos, esiti nel filo `i3/audit-adottanti.md`

Le skill sono interfacce sugli strumenti versionati, non documentazione: cfr.
[skill](kb/skill.md). Gli adottanti le forkano e le parametrizzano.

## Memoria

Non usare il sistema di memoria dell'harness (`auto-memory`, store in
`~/.claude/projects/.../memory/`): il contenuto è host-locale, opaco e non versionato
— l'anti-pattern dell'artefatto portabile. La memoria del progetto vive versionata nel
repo: i fili in `i3/` (perché una decisione conta), nodi `kb/` (conoscenza stabile), `o2/`
(lavoro futuro e contesto).

L'enforcement (spegnere la feature) è invece versionabile: vive in `nixos` — env var
`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `modules/home/claude-code.nix`, specchio di
`DISABLE_AUTOUPDATER`. Su harness che non leggono questi settings (Codex) vale solo
questa regola.

## Tabelle vs elenchi

Le tabelle markdown sono illeggibili su schermi stretti (mobile): preferire elenchi puntati per confronti e liste di voci. Eccezione: `o1/plan.md` (forma tabellare canonica, cfr. `kb/plan.md`).

## Quando aggiungere un nodo

Un nodo entra in `kb/` solo se il concetto è metodologico e applicabile ad almeno due progetti diversi. I concetti specifici di un singolo progetto restano nella `kb/` locale del progetto.

Procedura: creare il file in `kb/` seguendo la struttura in `kb/node.md`, aggiungere riga al catalogo `kb/kb.md`.

## Quando aggiornare un nodo esistente

Aggiornare quando una modifica del metodo in un progetto è generalizzabile. Verificare che la modifica non rompa il senso per gli altri progetti adottanti. Se la modifica è domain-specific, inserirla nella sezione "Adattamento al dominio" del nodo (come in cognitive-fidelity) invece di modificare il corpo principale.

## Come propagare modifiche ai progetti collegati

I progetti leggono i nodi via symlink — vedono automaticamente le modifiche. Non serve aggiornamento manuale. Se cambia nome o path di un nodo, l'adottante aggiorna solo le **connessioni intenzionali** che ha dichiarato: la sezione README canonica (che aggancia il solo hub `cognitive-artifact-design.md`) e i punti in cui una regola o uno strumento locale dipende davvero da quella specifica. Non esiste un inventario dei path del metodo da bonificare a ogni rinomina: replicarlo è coupling alla struttura interna del canone invece che alla sua interfaccia (cfr. `kb/method-development.md`, «Il confine canone↔adottante: dichiara e taci»).

## Push remoto

Mai automatico, sempre su richiesta esplicita.
