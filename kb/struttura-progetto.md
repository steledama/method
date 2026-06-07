---
data: 2026-06-07
stato: maturo
---

# Struttura progetto

Schema che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

La root non si decide per profondità («più in alto = più stabile», criterio demolito da pace-layering). Si decide perché sia **atrio**: il *system image* dell'artefatto. Un `ls` della root deve mostrare l'anatomia completa — quali classi di componente esistono — senza aprire nulla. È applicazione diretta di affordance-signifier e system-image: la struttura di directory porta essa stessa il peso della comunicazione, invece di delegarlo a un documento che la spiega (il cartello «tirare» su una porta mal progettata). Il principio è a sua volta applicazione di sviluppo-metodo: una cornice posata dall'alto (Norman) e verificata dal basso (le root reali dei progetti adottanti).

## Le due specie di file root

La root contiene due tipi di file, distinti per **funzione**, non per profondità.

**1. File-ciclo** — letti a *ogni* sessione per capire e agire. Sono il cruscotto del ciclo di sviluppo (quello che agisce sull'artefatto, non sul mondo):

- `README.md` — il Goal: identità, principi, motivazioni; punta a `map`, `plan`, `kb`
- `map.md` — il modello del dominio (vista o2, separata dal README per pace)
- `plan.md` — il Plan: i task aperti prioritizzati con dipendenze
- `CLAUDE.md` + `AGENTS.md` — le regole d'azione (AGENTS come wrapper agent-agnostico)
- `why.md` — la memoria del perché, append-only

**2. Porte-collezione** — *visibili* sempre nell'atrio, *lette* on-demand. Una per ogni collezione, così che la root dichiari l'inventario completo dell'artefatto:

- `kb.md` — il catalogo dei nodi (porta di `kb/`)
- `tools.md` — strumenti e skill (porta di `tools/`)
- `presentations.md` — lo strato output o2/o3 (porta di `presentations/`)
- `sources.md` — il manifest delle fonti i1 (porta di `sources/`)

## Visibilità ≠ caricamento

«In root» non significa «letto al bootstrap». I file-ciclo si leggono ogni sessione; le porte-collezione si *vedono* sempre ma si *aprono* solo quando servono. Il signifier che dice *cosa* leggere e *quando* è l'ordine di bootstrap dichiarato in `CLAUDE`/`AGENTS`, non la posizione del file. Questa scissione è ciò che permette all'atrio di essere completo senza gonfiare il contesto: l'esistenza di `kb.md` è informazione gratuita (un nome nell'`ls`), la sua lettura è un costo che si paga solo on-demand.

Questo **supera** la vecchia regola «un file-meta vive dentro la cartella se on-demand, sale in root solo se letto a ogni sessione»: un catalogo on-demand può vivere in root *come porta*, perché la root è inventario visibile, e l'ordine di bootstrap distingue cosa caricare. La pace resta criterio di compagnia: decide cosa non fondere (per questo `map` è in root ma distinto dal README, che cambia a passo più lento).

## Root estensibile dal basso

Il set universale (i file-ciclo + le porte-collezione) è un *pavimento, non un soffitto*: un dominio aggiunge i propri file bootstrap-essenziali — `economia` con `stato.md`/`scadenze.md`, `salute` con `scadenze.md`/`diario.md` — con lo stesso criterio di funzione.

## Il cruscotto è il ciclo di sviluppo, non simmetrico a sette caselle

Il cruscotto agisce sull'artefatto (la KB), non sul mondo del dominio. Per questo `plan` è il Plan dello sviluppo, **non** o1 (il Plan del runtime in ciclo-azione): tenere distinte le due cose evita una contraddizione `plan`/o1 tra nodi. `plan` resta `plan.md` e non diventa `tasks.md`: è uno stadio del ciclo, non l'indice di `tasks/` — eccezione semantica per altezza, prova che l'atrio contiene il vecchio criterio di altezza come caso speciale.

Il cruscotto ha due lati. Il lato esecuzione sono *intenzioni scritte* — Goal e Plan diventano file a root (`README`, `plan`). Il lato valutazione sono *operazioni* — l'audit, la fedelta-cognitiva — il cui residuo rientra in `why` e nei nodi. Il Compare (i3 in ciclo-azione) non vuole un `compare.md`: quando si cristallizza è l'**o2/termometro** (la presentazione, una `stato.md`) nello strato output — vista generata, non intenzione.

## Le regole d'azione e la memoria

`CLAUDE.md`, con `AGENTS.md` come wrapper agent-agnostico, è la "costituzione operativa": contiene cosa è consentito eseguire, vincoli operativi, bootstrap di sessione, pointer alla KB. È distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README e CLAUDE esplicitando l'ordine di lettura.

`why.md` è il registro append-only delle decisioni significative. Il git log dice cosa è cambiato; `why` dice perché conta — la decisione come chiave, la data come metadato, il commit citabile inline come puntatore. È lo strato interpretativo sopra quello analitico del git log.

## La triade di skill base

`audit-kb`, `tasks-review` e `commit`. `audit-kb` è l'health check periodico: link rotti, nodi orfani, connessioni tra cluster, naming, escludendo il file-meta `kb.md` dal conteggio dei nodi. `tasks-review` mantiene vera la supervisione: coerenza `plan`/`tasks`, priorità, dipendenze, task superati. `commit` è il gate di filing back. Le skill sono versionate nel progetto, non globali, perché ogni KB ha check, fonti e segnali locali diversi; quando possibile delegano la parte meccanica agli strumenti in `tools/`, così parsing e conteggi restano deterministici.

## Struttura uniforme, carattere nel contenuto

I nomi delle collezioni standard sono **uniformi** tra i progetti (`kb/`, `tools/`, `presentations/`, `sources/` e le rispettive porte): la familiarità della cornice rende l'artefatto leggibile e confortante a chi passa da un repo all'altro, umano o LLM. Il «colore» del dominio non vive nel nome della cartella ma nel **contenuto** dei file. Questo **supera** il vecchio principio «il nome dello strato output è una scelta di dominio»: un nome di dominio che contraddice il contenuto è un signifier che mente (es. `quadro/` in `salute`, che evoca il quadro *clinico* in una KB che rifiuta la separazione corpo/mente). La guardia che il vecchio principio proteggeva — non forzare la struttura sul dominio — resta valida solo come divieto di nomi fuorvianti, non come licenza di nomi idiosincratici.

Resta distinto ciò che non è una collezione di sintesi-documento ma output di altra natura ontologica: la configurazione che gira in `nixos` (`home/`, `hosts/`, `modules/`) è o1/runtime, non la porta `presentations/`. L'uniformità riguarda le collezioni standard dell'artefatto, non costringe a ribattezzare un output che *è* un'altra cosa.

## Caratteristiche

- root come atrio: l'`ls` dichiara l'inventario completo dei componenti; i file-ciclo si leggono, le porte-collezione si aprono on-demand
- README a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara
- la collocazione segue la funzione (file-ciclo vs porta-collezione) + pace, non la profondità
- le porte-collezione sono **generate dai tool** dove possibile (`kb.md` dall'audit), così non mentono sullo stato della collezione
- `tasks/` come spazio operativo: dettagli dei task aperti (stadio Specify), non conoscenza permanente; `plan.md` ne è l'indice — ogni file ha una riga, ogni riga ha un file
- `.claude/skills` come interfaccia operativa; `.codex/skills` come wrapper opzionale

## Skeleton directory

- file-ciclo: `README.md` · `map.md` · `plan.md` · `CLAUDE.md` · `AGENTS.md` · `why.md`
- porte-collezione: `kb.md` · `tools.md` · `presentations.md` · `sources.md`
- collezioni: `kb/` · `tools/` · `presentations/` · `sources/` · `tasks/`
- `.claude/skills/` · `.codex/skills/`

## Naming dei file

- file UPPERCASE — riconosciuti e caricati per nome da tool o LLM: `README.md`, `CLAUDE.md`, `AGENTS.md` (solo `CLAUDE.md` è auto-caricato dall'harness Claude Code; gli altri seguono l'ordine di bootstrap)
- file-ciclo lowercase in root (`map.md`, `plan.md`, `why.md`): letti seguendo l'ordine di bootstrap, tenuti concisi perché entrano in contesto presto
- porte-collezione lowercase in root (`kb.md`, `tools.md`, `presentations.md`, `sources.md`): il nome della porta è il nome della collezione (`kb.md` ↔ `kb/`), così l'atrio è auto-descrittivo
- forma inglese per gli artefatti strutturali vivi (`map`, `plan`, `why`, `kb`), italiano per i nodi-concetto e la prosa di dominio: l'inglese marca l'artefatto vivo, l'italiano la documentazione concettuale
- nodi `kb/` — lowercase con trattini, singolare come forma canonica (regola dettagliata in nodo)

## Frontmatter per tipo di file

- `kb/*.md`: frontmatter obbligatorio `data` + `stato`, secondo il nodo nodo
- `tasks/*.md`: frontmatter obbligatorio `data` + `stato: aperto`, secondo il nodo tasks
- file-ciclo (`README.md`, `CLAUDE.md`, `AGENTS.md`, `map.md`, `plan.md`, `why.md` e varianti locali come `stato.md`, `scadenze.md`, `diario.md`) e porte-collezione (`kb.md`, `tools.md`, `presentations.md`, `sources.md`): nessun frontmatter

La ragione è funzionale. I nodi e i task sono unità analizzabili dagli strumenti; i file-ciclo e le porte-collezione sono ingressi operativi o cataloghi leggibili direttamente. Aggiungere frontmatter crea metadati editoriali difficili da mantenere e senza funzione metodologica stabile.

## Bootstrap di sessione

- `README.md` è il primo file letto: orientamento, principi, puntatori al cruscotto
- `map.md` viene letto prima di toccare codice o dati, per legare concetti a file reali
- `CLAUDE.md` è già in contesto: contiene i vincoli operativi, non i contenuti di dominio
- le porte-collezione e il nodo tematico pertinente vengono letti solo quando servono
- l'ordine esplicito (`README → map → CLAUDE → nodo`) abbassa il costo di ricostruzione del modello del dominio in ogni nuova sessione LLM

## Regole dettagliate per componente

Questo nodo tiene l'overview; le regole proprie e i criteri di revisione di ciascun componente vivono nel nodo dedicato.

- README: funzione, doppia audience e sezioni tipiche in readme; il catalogo dei nodi sta nella porta `kb.md`, nodo-concetto indice
- map e plan: modello del dominio in map, supervisione del lavoro in plan
- CLAUDE e AGENTS: regole d'azione, bootstrap esplicito, confini con il dominio in claude e agents
- tasks/: corrispondenza uno a uno `plan` ↔ file, frontmatter e ciclo di vita del task in tasks
- why: formato canonico e distinzione da diario/stato in why

## Applicazione nei progetti adottanti

Lo stato sotto fotografa i progetti *prima* della migrazione all'atrio: ognuno la recepisce con un task locale (`kb/index.md`→`kb.md`, `scripts/`→`tools/`, output→`presentations/` dove è sintesi-documento), letto dal canone via symlink.

| Progetto   | Situazione attuale                                                                                                         | Confronto con il metodo                                                                                                                 |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | Ricetta molto coerente: README, CLAUDE, AGENTS, `why`, `tasks/`, `scripts/`, skill e mappa canonica sono presenti e distinti. | È il riferimento operativo per un progetto code-based: pochi componenti locali, fonti dichiarative forti e strumenti anti-drift maturi. |
| `bi`       | Struttura completa e ricca: README, CLAUDE, AGENTS, `why`, `tasks/`, `scripts/`, skill, presentazione, client e mappa.        | Il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale.                   |
| `economia` | Struttura completa con file di dominio in root: `stato.md`, `scadenze.md`, `diario.md`, config, dati e output JSON.        | Conferma la root estensibile dal basso: la root ammette file bootstrap di dominio senza renderli universali.                            |
| `salute`   | Struttura completa con KB molto ampia, fonti, diario, scadenze e skill ingest; README e CLAUDE restano narrativi.          | È il caso storico/riflessivo: il metodo è presente, ma la separazione tra bootstrap, mappa, filosofia e istruzioni può migliorare.      |

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni dell'atrio: ingresso, modello, piano, regole operative, memoria, più le porte verso la collezione dei nodi, gli strumenti, le presentazioni e le fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, why o nodi.

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
- [why](why.md)
- [skill](skill.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
