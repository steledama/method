---
data: 2026-06-07
stato: maturo
---

# Struttura progetto

Schema che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

La root non si decide per profondità («più in alto = più stabile», criterio demolito da pace-layering). Si decide perché sia **atrio**: il _system image_ dell'artefatto. Un `ls` della root deve mostrare l'anatomia completa — quali classi di componente esistono — senza aprire nulla. È applicazione diretta di affordance-signifier e system-image: la struttura di directory porta essa stessa il peso della comunicazione, invece di delegarlo a un documento che la spiega (il cartello «tirare» su una porta mal progettata). Il principio è a sua volta applicazione di sviluppo-metodo: una cornice posata dall'alto (Norman) e verificata dal basso (le root reali dei progetti adottanti).

## Le due specie di file root

La root contiene due tipi di file, distinti per **funzione**, non per profondità.

**1. File-ciclo** — letti a _ogni_ sessione per capire e agire. Sono il cruscotto del ciclo di sviluppo (quello che agisce sull'artefatto, non sul mondo):

- `README.md` — la **bussola** e il Goal: identità, principi e dominio in sintesi; orienta e _punta_ a `plan`, `kb` e al modello (nodi/`interpretations`, register `map` dove esiste)
- `plan.md` — il Plan: i task aperti prioritizzati con dipendenze
- `CLAUDE.md` + `AGENTS.md` — le regole d'azione (AGENTS come wrapper agent-agnostico)
- `verdict.md` — il verdetto attuale, per filo aperto

**2. Porte-collezione** — _visibili_ sempre nell'atrio, _lette_ on-demand. Una per ogni collezione, così che la root dichiari l'inventario completo dell'artefatto:

- `kb.md` — il catalogo dei nodi (porta di `kb/`)
- `map.md` — l'indice-di-dominio: il territorio reale (host, entità, sistemi) legato ai nodi. Register on-demand, presente **dove il dominio ha un territorio da indicizzare**; assente dove è astratto (in `metodo` non c'è)
- `tools.md` — strumenti e skill (porta di `tools/`)
- `interpretations.md` — lo stadio i2 (porta di `interpretations/`); per gli adottanti il deck legge anche come o2 (cfr. `ciclo-azione`, i2 micro/macro)
- `sources.md` — il manifest delle fonti i1 (porta di `sources/`)

## Visibilità ≠ caricamento

«In root» non significa «letto al bootstrap». I file-ciclo si leggono ogni sessione; le porte-collezione si _vedono_ sempre ma si _aprono_ solo quando servono. Il signifier che dice _cosa_ leggere e _quando_ è l'ordine di bootstrap dichiarato in `CLAUDE`/`AGENTS`, non la posizione del file. Questa scissione è ciò che permette all'atrio di essere completo senza gonfiare il contesto: l'esistenza di `kb.md` è informazione gratuita (un nome nell'`ls`), la sua lettura è un costo che si paga solo on-demand.

Questo **supera** la vecchia regola «un file-meta vive dentro la cartella se on-demand, sale in root solo se letto a ogni sessione»: un catalogo on-demand può vivere in root _come porta_, perché la root è inventario visibile, e l'ordine di bootstrap distingue cosa caricare.

Questo **supera** anche la regola del 2026-06-06 «`map` resta in root come file-ciclo, distinto dal README per pace». Quella regola trattava "map" come una cosa sola — il modello che evolve. La scomposizione lo scioglie meglio: la **bussola** (orientamento d'ingresso, stabile) è il README; il **modello** (la teoria che evolve) vive nei nodi e in `interpretations/`; l'**indice-di-dominio** (il territorio reale) è il register `map.md`, una porta on-demand. Così lo strato veloce resta fuori dal README — la pace è rispettata meglio del compromesso del 06-06 — e non serve più un `map.md`-bussola separato. Il README **orienta e punta, non immagazzina** (regola in readme).

## Root estensibile dal basso

Il set universale (i file-ciclo + le porte-collezione) è un _pavimento, non un soffitto_: un dominio aggiunge i propri file bootstrap-essenziali — `economia` con `stato.md`/`scadenze.md`, `salute` con `scadenze.md`/`diario.md` — con lo stesso criterio di funzione.

## Il cruscotto è il ciclo di sviluppo, non simmetrico a sette caselle

Il cruscotto agisce sull'artefatto (la KB), non sul mondo del dominio. Per questo `plan` è il Plan dello sviluppo, **non** o1 (il Plan del runtime in ciclo-azione): tenere distinte le due cose evita una contraddizione `plan`/o1 tra nodi. `plan` resta `plan.md` e non diventa `tasks.md`: è uno stadio del ciclo, non l'indice di `tasks/` — eccezione semantica per altezza, prova che l'atrio contiene il vecchio criterio di altezza come caso speciale.

Il cruscotto ha due lati. Il lato esecuzione sono _intenzioni scritte_ — Goal e Plan diventano file a root (`README`, `plan`). Il lato valutazione sono _operazioni_ — l'audit, la fedelta-cognitiva — il cui residuo rientra in `verdict.md` e nei nodi. Il Compare (i3 in ciclo-azione) deposita qui il suo esito come **sostantivo** (il verdetto, per filo aperto), non come log di atti; quando si cristallizza in vista generata è l'**o2/i2-macro** (il deck in `interpretations/`) — vista derivata, non intenzione.

## Le regole d'azione e la memoria

`CLAUDE.md`, con `AGENTS.md` come wrapper agent-agnostico, è la "costituzione operativa": contiene cosa è consentito eseguire, vincoli operativi, bootstrap di sessione, pointer alla KB. È distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README e CLAUDE esplicitando l'ordine di lettura.

`verdict.md` è il verdetto attuale, per filo/area aperta — non un log. Il git log dice cosa è cambiato; `verdict.md` dice come stanno le cose ora e perché conta, aggiornato in place; la cronologia di un filo è il git history del file stesso. È lo strato interpretativo sopra quello analitico del git log.

## Skill base

`kb-review`, `tasks-review` e `commit`. `kb-review` è l'health check periodico: link rotti, nodi orfani, connessioni tra cluster, naming, escludendo il file-meta `kb.md` dal conteggio dei nodi. `tasks-review` mantiene vera la supervisione: coerenza `plan`/`tasks`, priorità, dipendenze, task superati. `commit` è il gate di filing back. Le skill sono versionate nel progetto, non globali, perché ogni KB ha check, fonti e segnali locali diversi; quando possibile delegano la parte meccanica agli strumenti in `tools/`, così parsing e conteggi restano deterministici.

`method-review` completa questa base sul confine tra repository: legge i commit
del metodo successivi al marker versionato dell'adottante, classifica ciò che è
diretto, adattato, non pertinente o già soddisfatto e lascia l'eventuale lavoro
futuro nel `plan.md`/`tasks/` locale. Non sostituisce la triade: controlla la
relazione adottante-metodo, non la salute o la coda interna del progetto.

## Struttura uniforme, carattere nel contenuto

I nomi delle collezioni standard sono **uniformi** tra i progetti (`kb/`, `tools/`, `interpretations/`, `sources/` e le rispettive porte): la familiarità della cornice rende l'artefatto leggibile e confortante a chi passa da un repo all'altro, umano o LLM. Il «colore» del dominio non vive nel nome della cartella ma nel **contenuto** dei file. Questo **supera** il vecchio principio «il nome dello strato output è una scelta di dominio»: un nome di dominio che contraddice il contenuto è un signifier che mente (es. `quadro/` in `salute`, che evoca il quadro _clinico_ in una KB che rifiuta la separazione corpo/mente). La guardia che il vecchio principio proteggeva — non forzare la struttura sul dominio — resta valida solo come divieto di nomi fuorvianti, non come licenza di nomi idiosincratici.

Resta distinto ciò che non è una collezione di sintesi-documento ma output di altra natura ontologica: la configurazione che gira in `nixos` (`home/`, `hosts/`, `modules/`) è o1/runtime, non la porta `interpretations/`. L'uniformità riguarda le collezioni standard dell'artefatto, non costringe a ribattezzare un output che _è_ un'altra cosa.

Anche `world/` ha nome uniforme, ma non è una collezione dell'artefatto. È un
symlink host-local verso la cartella di progetto non versionata, tipicamente su
Drive: la membrana fisica attraversata da atti e segnali grezzi. Non ha una
porta `world.md` né un manifest, a differenza di `sources.md`; il symlink è
sempre gitignorato. Nel repo `method`, `world/` contiene symlink ai repository
adottanti e materializza il suo Mondo runtime senza versionarne i path.

## Caratteristiche

- root come atrio: l'`ls` dichiara l'inventario completo dei componenti; i file-ciclo si leggono, le porte-collezione si aprono on-demand
- README a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara
- la collocazione segue la funzione (file-ciclo vs porta-collezione) + pace, non la profondità
- le porte-collezione sono **generate dai tool** dove possibile (`kb.md` dall'audit), così non mentono sullo stato della collezione
- `tasks/` come spazio operativo: dettagli dei task aperti (stadio Specify), non conoscenza permanente; `plan.md` ne è l'indice — ogni file ha una riga, ogni riga ha un file
- `.claude/skills` come interfaccia operativa; `.codex/skills` come wrapper opzionale

## Skeleton directory

- file-ciclo: `README.md` · `plan.md` · `CLAUDE.md` · `AGENTS.md` · `verdict.md`
- porte-collezione: `kb.md` · `map.md` (dove il dominio ha un territorio) · `tools.md` · `interpretations.md` · `sources.md`
- collezioni: `kb/` · `tools/` · `interpretations/` · `sources/` · `tasks/`
- membrana locale: `world/`, symlink gitignorato alla cartella di progetto non
  versionata, senza manifest
- workspace locale opzionale: `data/`, ignorato da Git, per fonti, dati
  compilati e intermedi che non appartengono alla storia dell'artefatto
- `.claude/skills/` · `.codex/skills/`

## Naming dei file

- file UPPERCASE — riconosciuti e caricati per nome da tool o LLM: `README.md`, `CLAUDE.md`, `AGENTS.md` (solo `CLAUDE.md` è auto-caricato dall'harness Claude Code; gli altri seguono l'ordine di bootstrap)
- file-ciclo lowercase in root (`plan.md`, `verdict.md`): letti seguendo l'ordine di bootstrap, tenuti concisi perché entrano in contesto presto
- porte-collezione lowercase in root (`kb.md`, `map.md`, `tools.md`, `interpretations.md`, `sources.md`): il nome della porta è il nome della collezione (`kb.md` ↔ `kb/`), così l'atrio è auto-descrittivo
- forma inglese per gli artefatti strutturali vivi (`map`, `plan`, `verdict`, `kb`), italiano per i nodi-concetto e la prosa di dominio: l'inglese marca l'artefatto vivo, l'italiano la documentazione concettuale
- nodi `kb/` — lowercase con trattini, singolare come forma canonica (regola dettagliata in nodo)

## Frontmatter per tipo di file

- `kb/*.md`: frontmatter obbligatorio `data` + `stato`, secondo il nodo nodo
- `tasks/*.md`: frontmatter obbligatorio `data` + `stato: aperto`, secondo il nodo tasks
- file-ciclo (`README.md`, `CLAUDE.md`, `AGENTS.md`, `plan.md`, `verdict.md` e varianti locali come `stato.md`, `scadenze.md`, `diario.md`) e porte-collezione (`kb.md`, `map.md`, `tools.md`, `interpretations.md`, `sources.md`): nessun frontmatter

La ragione è funzionale. I nodi e i task sono unità analizzabili dagli strumenti; i file-ciclo e le porte-collezione sono ingressi operativi o cataloghi leggibili direttamente. Aggiungere frontmatter crea metadati editoriali difficili da mantenere e senza funzione metodologica stabile.

## Bootstrap di sessione

- `README.md` è il primo file letto: la bussola — orientamento, principi in sintesi, puntatori al cruscotto
- `CLAUDE.md` è già in contesto: contiene i vincoli operativi, non i contenuti di dominio
- le porte-collezione (incluso `map.md` dove esiste, da aprire prima di toccare codice o dati per legare concetti a file reali) e il nodo tematico pertinente vengono letti solo quando servono
- l'ordine esplicito (`README → CLAUDE → nodo`) abbassa il costo di ricostruzione del dominio in ogni nuova sessione LLM

## Regole dettagliate per componente

Questo nodo tiene l'overview; le regole proprie e i criteri di revisione di ciascun componente vivono nel nodo dedicato.

- README: funzione, doppia audience e sezioni tipiche in readme; il catalogo dei nodi sta nella porta `kb.md`, nodo-concetto indice
- map e plan: indice-di-dominio (il territorio) in map dove esiste, supervisione del lavoro in plan
- CLAUDE e AGENTS: regole d'azione, bootstrap esplicito, confini con il dominio in claude e agents
- tasks/: corrispondenza uno a uno `plan` ↔ file, frontmatter e ciclo di vita del task in tasks
- verdict: formato canonico e distinzione da diario/stato in verdict

## Applicazione nei progetti adottanti

Lo stato sotto fotografa i progetti _prima_ della migrazione all'atrio: ognuno la recepisce con un task locale (`kb/index.md`→`kb.md`, `scripts/`→`tools/`, output→`interpretations/` dove è sintesi-documento), letto dal canone via symlink.

- **`nixos`** — situazione attuale: ricetta molto coerente: README, CLAUDE, AGENTS, `verdict`, `tasks/`, `scripts/`, skill e mappa canonica sono presenti e distinti. Confronto con il metodo: è il riferimento operativo per un progetto code-based — pochi componenti locali, fonti dichiarative forti e strumenti anti-drift maturi.
- **`bi`** — situazione attuale: struttura completa e ricca: README, CLAUDE, AGENTS, `verdict`, `tasks/`, `scripts/`, skill, presentazione, client e mappa. Confronto con il metodo: il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale.
- **`economia`** — situazione attuale: struttura completa con file di dominio
  in root, `data/` locale non versionato per fonti e JSON, e `interpretations/`
  versionata per le viste decisionali. Confronto con il metodo: conferma sia la
  root estensibile dal basso sia la separazione tra stato operativo e risultato
  editoriale.
- **`salute`** — situazione attuale: struttura completa con KB molto ampia, fonti, diario, scadenze e skill ingest; README e CLAUDE restano narrativi. Confronto con il metodo: è il caso storico/riflessivo — il metodo è presente, ma la separazione tra bootstrap, mappa, filosofia e istruzioni può migliorare.

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni dell'atrio: ingresso/bussola (README), piano, regole operative, memoria, più le porte verso la collezione dei nodi, l'indice-di-dominio (dove esiste), gli strumenti, le interpretazioni e le fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, verdict o nodi.

Gli strumenti vanno esposti su tre livelli — README orienta, CLAUDE istruisce, nodi approfondiscono — secondo la regola dettagliata in strumenti-kb.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [nodo](nodo.md)
- [zettelkasten](zettelkasten.md)
- [pace-layering](pace-layering.md)
- [sviluppo-metodo](sviluppo-metodo.md)
- [affordance-signifier](affordance-signifier.md)
- [system-image](system-image.md)
- [strumenti-kb](strumenti-kb.md)
- [agents](agents.md)
- [claude](claude.md)
- [readme](readme.md)
- [indice](indice.md)
- [map](map.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [skill](skill.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
