# CLAUDE.md

Regole operative per agenti che lavorano su questo repository.

## Bootstrap di sessione

Ordine: `README → map → CLAUDE → nodo`.

1. `README.md` — scopo del repo, progetti adottanti, puntatori al cruscotto
2. `map.md` — il modello del dominio; `plan.md` per lo stato del lavoro, `kb/index.md` per il catalogo dei nodi
3. nodo pertinente alla modifica richiesta

## Operazioni consentite senza autorizzazione

- modifica ai nodi in `kb/`
- aggiornamento di `README.md`, `map.md`, `plan.md` e `why.md`
- commit e operazioni git locali

## Memoria

Non usare il sistema di memoria dell'harness (lo store in `~/.claude/`): è
host-locale, opaco e non versionato — l'anti-pattern dell'artefatto portabile.
La memoria del progetto vive versionata nel repo: `why.md` (perché una decisione
conta), nodi `kb/` (conoscenza stabile), `tasks/` (lavoro futuro e contesto).

## Quando aggiungere un nodo

Un nodo entra in `kb/` solo se il concetto è metodologico e applicabile ad almeno due progetti diversi. I concetti specifici di un singolo progetto restano nella `kb/` locale del progetto.

Procedura: creare il file in `kb/` seguendo la struttura in `kb/nodo.md`, aggiungere riga al catalogo in `README.md`.

## Quando aggiornare un nodo esistente

Aggiornare quando una modifica del metodo in un progetto è generalizzabile. Verificare che la modifica non rompa il senso per gli altri progetti adottanti. Se la modifica è domain-specific, inserirla nella sezione "Adattamento al dominio" del nodo (come in fedelta-cognitiva) invece di modificare il corpo principale.

## Come propagare modifiche ai progetti collegati

I progetti leggono i nodi via symlink — vedono automaticamente le modifiche. Non serve aggiornamento manuale salvo che cambi nome o path di un nodo: in quel caso aggiornare i link nei `CLAUDE.md` e `README.md` di tutti i progetti collegati.

## Push remoto

Mai automatico, sempre su richiesta esplicita.
