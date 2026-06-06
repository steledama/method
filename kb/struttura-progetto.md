---
data: 2026-06-06
stato: maturo
---

# Struttura progetto

Schema che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

La struttura non si decide per profondità («più in alto = più stabile», criterio demolito da pace-layering). Si decide per una triade: cosa è cruscotto del ciclo, cosa è collezione di unità atomiche, e quando la pace impone di non fondere. Il principio stesso è applicazione di sviluppo-metodo: una cornice posata dall'alto (il ciclo dell'azione di Norman) e verificata dal basso (le root reali dei progetti adottanti).

## La triade

**1. Root = artefatti bootstrap-essenziali di livello-progetto**, letti per capire *il tutto* a prescindere dalla pace. La root è il **cruscotto del ciclo di sviluppo** — quello che agisce sull'artefatto, non sul mondo:

- `README.md` — il Goal: identità, principi, motivazioni; punta a `map`, `plan`, `kb/index`
- `map.md` — il modello del dominio (vista o2, separata dal README per tenerlo conciso)
- `plan.md` — il Plan: i task aperti prioritizzati con dipendenze
- `CLAUDE.md` + `AGENTS.md` — le regole d'azione (AGENTS come wrapper agent-agnostico)
- `why.md` — la memoria del perché, append-only

`plan` e `why` stanno in root pur essendo veloci: la loro **altezza nel ciclo vince sulla pace**.

**2. Cartelle = collezioni di unità atomiche.** Una cartella ha un file-meta *dentro di sé* solo se il suo catalogo si consulta on-demand: è il caso di `kb/index.md`, il register dei nodi. Se invece il meta si legge a ogni sessione, sale in root — è il caso di `plan.md`, meta-istanza dei task, sollevato dall'altezza fuori da `tasks/`.

**3. Pace = criterio di compagnia, non di profondità.** Decide cosa non fondere in un solo file. Quando altezza e pace confliggono, l'altezza decide la collocazione, la pace decide che resti un file separato (così `map` e `plan` sono in root ma distinti dal README, che cambia a passo più lento).

**4. Root estensibile dal basso.** Il set universale (README/map/plan/CLAUDE/AGENTS/why) è un *pavimento, non un soffitto*: un dominio aggiunge i propri file bootstrap-essenziali — `economia` con `stato.md`/`scadenze.md`, `salute` con `scadenze.md`/`diario.md` — con lo stesso criterio di altezza.

## Il cruscotto è il ciclo di sviluppo, non simmetrico a sette caselle

Il cruscotto agisce sull'artefatto (la KB), non sul mondo del dominio. Per questo `plan` è il Plan dello sviluppo, **non** o1 (il Plan del runtime in ciclo-azione): tenere distinte le due cose evita una contraddizione `plan`/o1 tra nodi.

Il cruscotto ha due lati. Il lato esecuzione sono *intenzioni scritte* — Goal e Plan diventano file a root (`README`, `plan`). Il lato valutazione sono *operazioni* — l'audit, la fedelta-cognitiva — il cui residuo rientra in `why` e nei nodi. Il Compare (i3 in ciclo-azione) non vuole un `compare.md`: quando si cristallizza è l'**o2/termometro** (la presentazione, una `stato.md`) nello strato output — vista generata, non intenzione.

## Le regole d'azione e la memoria

`CLAUDE.md`, con `AGENTS.md` come wrapper agent-agnostico, è la "costituzione operativa": contiene cosa è consentito eseguire, vincoli operativi, bootstrap di sessione, pointer alla KB. È distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README e CLAUDE esplicitando l'ordine di lettura.

`why.md` è il registro append-only delle decisioni significative. Il git log dice cosa è cambiato; `why` dice perché conta — la decisione come chiave, la data come metadato, il commit citabile inline come puntatore. È lo strato interpretativo sopra quello analitico del git log.

## La triade di skill base

`audit-kb`, `revisione-tasks` e `commit`. `audit-kb` è l'health check periodico: link rotti, nodi orfani, connessioni tra cluster, naming, escludendo il file-meta `kb/index.md` dal conteggio dei nodi. `revisione-tasks` mantiene vera la supervisione: coerenza `plan`/`tasks`, priorità, dipendenze, task superati. `commit` è il gate di filing back. Le skill sono versionate nel progetto, non globali, perché ogni KB ha check, fonti e segnali locali diversi; quando possibile delegano la parte meccanica agli strumenti in `scripts/`, così parsing e conteggi restano deterministici.

## Caratteristiche

- root come cruscotto: i file letti a ogni sessione per capire il tutto, a prescindere dalla pace
- README a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara
- la collocazione segue altezza + pace, non profondità: l'altezza decide dove, la pace decide che resti separato
- file-meta dentro la cartella solo se on-demand (`kb/index.md`); se letto a ogni sessione sale in root (`plan.md`)
- `tasks/` come spazio operativo: dettagli dei task aperti (stadio Specify), non conoscenza permanente; `plan.md` ne è l'indice — ogni file ha una riga, ogni riga ha un file
- `.claude/skills` come interfaccia operativa; `.codex/skills` come wrapper opzionale
- strato output come ponte tra KB e azione: ospita sintesi, viste e dashboard che non possono stare in `kb/` senza violare l'atomicità zettelkastiana; il nome è locale (quadro/, presentation/, output/); ogni progetto dichiara come implementa o1/o2/o3 e i1/i2/i3

## Skeleton directory

- `README.md` · `map.md` · `plan.md` · `CLAUDE.md` · `AGENTS.md` · `why.md`
- `kb/` (+ `index.md`)
- `tasks/`
- `scripts/`
- `.claude/skills/` · `.codex/skills/`

## Naming dei file

- file UPPERCASE — riconosciuti e caricati per nome da tool o LLM: `README.md`, `CLAUDE.md`, `AGENTS.md`
- file lowercase in root — il resto del cruscotto (`map.md`, `plan.md`, `why.md`): letti seguendo l'ordine di bootstrap, tenuti concisi perché entrano in contesto presto
- forma inglese per gli artefatti strutturali vivi (`map`, `plan`, `why`, `index`), italiano per i nodi-concetto e la prosa di dominio: l'inglese marca l'artefatto vivo, l'italiano la documentazione concettuale
- nodi `kb/` — lowercase con trattini, singolare come forma canonica (regola dettagliata in nodo)

## Frontmatter per tipo di file

- `kb/*.md`: frontmatter obbligatorio `data` + `stato`, secondo il nodo nodo
- `tasks/*.md`: frontmatter obbligatorio `data` + `stato: aperto`, secondo il nodo tasks
- file root (`README.md`, `CLAUDE.md`, `AGENTS.md`, `map.md`, `plan.md`, `why.md` e varianti locali come `stato.md`, `scadenze.md`, `diario.md`) e il file-meta `kb/index.md`: nessun frontmatter

La ragione è funzionale. I nodi e i task sono unità analizzabili dagli strumenti; i file root e i register sono ingressi operativi o cataloghi leggibili direttamente. Aggiungere frontmatter crea metadati editoriali difficili da mantenere e senza funzione metodologica stabile.

## Bootstrap di sessione

- `README.md` è il primo file letto: orientamento, principi, puntatori al cruscotto
- `map.md` viene letto prima di toccare codice o dati, per legare concetti a file reali
- `CLAUDE.md` è già in contesto: contiene i vincoli operativi, non i contenuti di dominio
- il nodo tematico pertinente viene letto solo quando serve
- l'ordine esplicito (`README → map → CLAUDE → nodo`) abbassa il costo di ricostruzione del modello del dominio in ogni nuova sessione LLM

## Regole dettagliate per componente

Questo nodo tiene l'overview; le regole proprie e i criteri di revisione di ciascun componente vivono nel nodo dedicato.

- README: funzione, doppia audience e sezioni tipiche in readme; il catalogo dei nodi sta nel register `kb/index.md`, nodo-concetto indice
- map e plan: modello del dominio in map, supervisione del lavoro in plan
- CLAUDE e AGENTS: regole d'azione, bootstrap esplicito, confini con il dominio in claude e agents
- tasks/: corrispondenza uno a uno `plan` ↔ file, frontmatter e ciclo di vita del task in tasks
- why: formato canonico e distinzione da diario/stato in why

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                         | Confronto con il metodo                                                                                                                 |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | Ricetta molto coerente: README, CLAUDE, AGENTS, `why`, `tasks/`, `scripts/`, skill e mappa canonica sono presenti e distinti. | È il riferimento operativo per un progetto code-based: pochi componenti locali, fonti dichiarative forti e strumenti anti-drift maturi. |
| `bi`       | Struttura completa e ricca: README, CLAUDE, AGENTS, `why`, `tasks/`, `scripts/`, skill, presentazione, client e mappa.        | Il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale.                   |
| `economia` | Struttura completa con file di dominio in root: `stato.md`, `scadenze.md`, `diario.md`, config, dati e output JSON.        | Conferma il punto 4 della triade: la root ammette file bootstrap di dominio senza renderli universali.                                  |
| `salute`   | Struttura completa con KB molto ampia, fonti, diario, scadenze e skill ingest; README e CLAUDE restano narrativi.          | È il caso storico/riflessivo: il metodo è presente, ma la separazione tra bootstrap, mappa, filosofia e istruzioni può migliorare.      |

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni del cruscotto: ingresso, modello, piano, regole operative, memoria, più la collezione dei nodi, gli strumenti e le fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, why o nodi.

Gli strumenti vanno esposti su tre livelli — README orienta, CLAUDE istruisce, nodi approfondiscono — secondo la regola dettagliata in strumenti-kb.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [nodo](nodo.md)
- [zettelkasten](zettelkasten.md)
- [pace-layering](pace-layering.md)
- [sviluppo-metodo](sviluppo-metodo.md)
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
