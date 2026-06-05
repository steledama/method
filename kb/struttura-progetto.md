---
data: 2026-05-24
stato: maturo
---

# Struttura progetto

Schema a quattro pilastri che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

I pilastri sono indipendenti nel ruolo ma si completano: insieme danno al LLM tutto il contesto necessario per lavorare in modo coerente e continuativo tra sessioni diverse.

Il primo pilastro è README.md: descrive brevemente il progetto, enuncia i principi costitutivi, mostra lo stato corrente dei task aperti e contiene l'indice statico di tutti i nodi organizzati per cluster tematici. È il file di bootstrap di ogni sessione — leggere README è sufficiente per orientarsi.

Il secondo pilastro è CLAUDE.md, con AGENTS.md come wrapper agent-agnostico: contiene le regole d'azione per gli agenti — cosa è consentito eseguire autonomamente, vincoli operativi non documentati altrove, bootstrap di sessione, pointer alla knowledge base. È la "costituzione operativa" del progetto, distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README.md e CLAUDE.md esplicitando l'ordine di lettura.

Il terzo pilastro è log.md: registro append-only delle sessioni significative. Il git log dice cosa è cambiato; log.md dice perché conta. Non registra ogni commit ma le sessioni in cui è emerso qualcosa di rilevante — una decisione strutturale, un cambio di approccio, un ingest importante. È lo strato interpretativo sopra quello analitico del git log.

Il quarto pilastro è la triade di skill base: `audit-kb`, `revisione-tasks` e `commit`. `audit-kb` è l'health check periodico della KB: controlla link rotti, nodi orfani, connessioni tra cluster, stato della migrazione ai footer link e convenzioni di naming. `revisione-tasks` mantiene vera la supervisione del lavoro futuro: controlla coerenza README/todo, priorità, dipendenze e task superati. `commit` è il gate di filing back prima di fissare una modifica nella storia. Le skill sono versionate nel progetto, non globali, perché ogni KB ha check, fonti e segnali locali diversi; quando possibile delegano la parte meccanica agli strumenti versionati in `scripts/`, così parsing e conteggi restano deterministici.

Caratteristiche:

- README come bootstrap: unico file da leggere per orientarsi a inizio sessione; contiene anche i task aperti
- README come artefatto a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara — sezioni distinte per cluster tematici riducono lo scanning per entrambi gli attori
- CLAUDE.md come costituzione operativa: procedure per l'LLM, co-evoluta nel tempo con l'utente
- AGENTS.md come wrapper agent-agnostico: rimanda a README.md e CLAUDE.md senza duplicare contenuto
- log.md come strato interpretativo: il perché delle decisioni, non il catalogo dei cambiamenti
- triade skill base come interfaccia operativa: `audit-kb` per diagnosi, `revisione-tasks` per supervisione dei task, `commit` per filing back e commit
- strumenti KB come backend deterministico: script versionati per link, backlink, README e formato dei nodi
- struttura di progetto replicabile: ogni nuova KB parte da questo schema operativo e lo personalizza al proprio dominio
- todo/ come spazio operativo: dettagli dei task aperti, non conoscenza permanente; la tabella Tasks aperti nel README è l'indice di todo/ — ogni file ha una riga, ogni riga ha un file
- .claude/skills come interfaccia operativa: triade base ufficiale più skill locali versionate, preferite ai vecchi comandi
- .codex/skills come wrapper opzionale: rimanda alle skill Claude senza duplicare workflow
- revisione task come funzione strutturale della sessione: controllo leggero a inizio sessione e revisione completa quando eventi significativi cambiano priorità, dipendenze o stato reale del progetto
- strato output come ponte tra KB e azione: ospita sintesi, viste e dashboard che non possono stare in kb/ senza violare l'atomicità zettelkastiana; il nome è locale e dipende dal dominio (quadro/, presentazione/, output/, configurazione); non compare nel skeleton perché non ha forma fissa, ma ogni progetto deve dichiarare esplicitamente come sono implementati o1, o2, o3 (output) e i1, i2, i3 (input)

Skeleton directory:

- README.md
- CLAUDE.md
- AGENTS.md
- log.md
- kb/
- todo/
- scripts/
- .claude/skills/
- .codex/skills/

Naming dei file pilastro:

- file UPPERCASE — caricati per nome da tool o LLM all'inizio di ogni sessione: README.md, CLAUDE.md, AGENTS.md
- file lowercase — referenziati su richiesta, non auto-caricati: log.md e tutti i nodi in kb/
- nodi kb/ — sempre lowercase con trattini, singolare come forma canonica (regola dettagliata in nodo)
- la distinzione segnala il costo di caricamento: ciò che è UPPERCASE entra in contesto a ogni sessione e deve restare conciso, ciò che è lowercase viene letto solo quando serve

Frontmatter per tipo di file:

- `kb/*.md`: frontmatter obbligatorio `data` + `stato`, secondo il nodo `nodo`
- `todo/*.md`: frontmatter obbligatorio `data` + `stato: aperto`, secondo il nodo `todo`
- file root (`README.md`, `CLAUDE.md`, `AGENTS.md`, `log.md` e varianti locali come `stato.md`, `scadenze.md`, `diario.md`): nessun frontmatter

La ragione è funzionale. I nodi e i task sono unità analizzabili dagli strumenti; i file root sono ingressi operativi o registri leggibili direttamente. Aggiungere frontmatter ai file root crea metadati editoriali difficili da mantenere e non aggiunge una funzione metodologica stabile.

Bootstrap di sessione:

- README.md è il primo file letto a inizio sessione: orientamento, principi, task aperti, indice della KB
- la mappa canonica del progetto viene letta prima di toccare codice o dati, per legare concetti a file reali
- il nodo tematico pertinente al cambiamento viene letto solo quando serve
- CLAUDE.md è già in contesto a inizio sessione: contiene i vincoli operativi, non i contenuti di dominio
- AGENTS.md indirizza ogni agente verso questo flow senza duplicare le regole
- l'ordine esplicito (README → mappa → CLAUDE → nodo) abbassa il costo di ricostruzione del modello del dominio in ogni nuova sessione LLM

Regole dettagliate per pilastro:

Questo nodo tiene l'overview dei quattro pilastri; le regole proprie e i criteri di revisione di ciascun componente vivono nel nodo dedicato.

- README: funzione, doppia audience e sezioni tipiche in `readme`; catalogo e supervisione del lavoro hanno nodi propri (`indice`, `task-aperti`)
- CLAUDE e AGENTS: regole d'azione, bootstrap esplicito, confini con il dominio e segnale di dimensione in `claude` e `agents`
- todo/: corrispondenza uno a uno README ↔ file, frontmatter e ciclo di vita del task in `todo`
- log: formato canonico e distinzione da diario/stato in `log`

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                         | Confronto con il metodo                                                                                                                 |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | Ricetta molto coerente: README, CLAUDE, AGENTS, log, `todo/`, `scripts/`, skill e mappa canonica sono presenti e distinti. | È il riferimento operativo per un progetto code-based: pochi componenti locali, fonti dichiarative forti e strumenti anti-drift maturi. |
| `bi`       | Struttura completa e ricca: README, CLAUDE, AGENTS, log, `todo/`, `scripts/`, skill, presentazione, client e mappa.        | Il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale.                   |
| `economia` | Struttura completa con componenti locali aggiuntivi: `stato.md`, `scadenze.md`, `diario.md`, config, dati e output JSON.   | Mostra che la ricetta deve ammettere file di dominio specializzati senza renderli universali.                                           |
| `salute`   | Struttura completa con KB molto ampia, fonti, diario, scadenze e skill ingest; README e CLAUDE restano narrativi.          | È il caso storico/riflessivo: il metodo è presente, ma la separazione tra bootstrap, mappa, filosofia e istruzioni può migliorare.      |

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni cognitive: ingresso, regole operative, memoria, task, conoscenza stabile, strumenti e fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, log o nodi.

Gli strumenti vanno esposti su tre livelli — README orienta, CLAUDE istruisce, nodi approfondiscono — secondo la regola dettagliata in `strumenti-kb`.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [nodo](nodo.md)
- [zettelkasten](zettelkasten.md)
- [strumenti-kb](strumenti-kb.md)
- [agents](agents.md)
- [claude](claude.md)
- [readme](readme.md)
- [indice](indice.md)
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [log](log.md)
- [skill](skill.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
