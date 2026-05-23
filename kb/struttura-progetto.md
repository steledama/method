---
data: 2026-05-09
stato: maturo
---

# Struttura progetto

Schema a quattro pilastri che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

I pilastri sono indipendenti nel ruolo ma si completano: insieme danno al LLM tutto il contesto necessario per lavorare in modo coerente e continuativo tra sessioni diverse.

Il primo pilastro è README.md: descrive brevemente il progetto, enuncia i principi costitutivi, mostra lo stato corrente dei task aperti e contiene l'indice statico di tutti i nodi organizzati per cluster tematici. È il file di bootstrap di ogni sessione — leggere README è sufficiente per orientarsi.

Il secondo pilastro è CLAUDE.md, con AGENTS.md come wrapper agent-agnostico: contiene le regole d'azione per gli agenti — cosa è consentito eseguire autonomamente, vincoli operativi non documentati altrove, bootstrap di sessione, pointer alla knowledge base. È la "costituzione operativa" del progetto, distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README.md e CLAUDE.md esplicitando l'ordine di lettura.

Il terzo pilastro è log.md: registro append-only delle sessioni significative. Il git log dice cosa è cambiato; log.md dice perché conta. Non registra ogni commit ma le sessioni in cui è emerso qualcosa di rilevante — una decisione strutturale, un cambio di approccio, un ingest importante. È lo strato interpretativo sopra quello analitico del git log.

Il quarto pilastro è la skill audit-kb: health check periodico della KB. Controlla link rotti, nodi orfani, connessioni tra cluster, stato della migrazione ai footer link, convenzioni di naming. L'output esteso è un report strutturato ricostruibile dagli strumenti versionati; in log.md entra solo una sintesi interpretativa quando l'audit produce una decisione o una revisione significativa. La skill è versionata nel progetto, non globale, perché ogni KB ha check specifici diversi. La parte meccanica dell'audit è delegata agli strumenti KB versionati in `scripts/`, così parsing e conteggi restano deterministici.

Caratteristiche:

- README come bootstrap: unico file da leggere per orientarsi a inizio sessione; contiene anche i task aperti
- README come artefatto a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara — sezioni distinte per cluster tematici riducono lo scanning per entrambi gli attori
- CLAUDE.md come costituzione operativa: procedure per l'LLM, co-evoluta nel tempo con l'utente
- AGENTS.md come wrapper agent-agnostico: rimanda a README.md e CLAUDE.md senza duplicare contenuto
- log.md come strato interpretativo: il perché delle decisioni, non il catalogo dei cambiamenti
- audit-kb come strumento di salute: check periodici, report ricostruibile e sintesi interpretativa in log.md quando serve, versionata nel progetto
- strumenti KB come backend deterministico: script versionati per link, backlink, README e formato dei nodi
- struttura di progetto replicabile: ogni nuova KB parte da questo schema operativo e lo personalizza al proprio dominio
- todo/ come spazio operativo: dettagli dei task aperti, non conoscenza permanente; la tabella Tasks aperti nel README è l'indice di todo/ — ogni file ha una riga, ogni riga ha un file
- .claude/skills come interfaccia operativa: skill versionate, preferite ai vecchi comandi
- .codex/skills come wrapper opzionale: rimanda alle skill Claude senza duplicare workflow
- revisione-tasks come chiusura sessione: rivedere priorità e dipendenze dei task aperti quando eventi significativi cambiano la KB

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

Sezioni README:

- titolo e descrizione del progetto
- principi o approccio
- Tasks aperti con tabella Priorità, Task, Dipende da
- documentazione o metodi di accesso, se utili
- indice statico della knowledge base come ultima sezione quando il progetto è principalmente una KB

Regole todo/:

- il README contiene una tabella Tasks aperti con priorità, titolo linkato al file di dettaglio e dipendenze
- esiste una corrispondenza uno a uno tra le righe della tabella e i file in `todo/`: ogni riga ha un file, ogni file ha una riga
- un file senza riga nella tabella è invisibile agli agenti e agli utenti futuri; una riga senza file è un link rotto
- task completato = riga rimossa dalla tabella + file eliminato da `todo/`

Regole AGENTS:

- deve essere breve
- deve indicare che le istruzioni sono in README.md e CLAUDE.md
- deve esplicitare l'ordine di lettura a inizio sessione (README → mappa del progetto → CLAUDE → nodo tematico)
- non deve contenere regole operative divergenti

Regole CLAUDE:

- contiene solo regole d'azione per gli agenti, mai contenuto di dominio
- il contenuto di dominio (architettura, servizi, pattern, comandi, descrizioni di come funziona qualcosa) vive nei nodi kb/; CLAUDE.md ne è solo il pointer
- apre con il bootstrap di sessione esplicito: ordine di lettura README → mappa del progetto → nodo tematico → CLAUDE.md
- contiene i vincoli operativi non documentati altrove: cosa l'agente può eseguire autonomamente, comportamenti proibiti, regole di sicurezza
- può elencare i comandi quotidiani ad alta frequenza (formatter, validazione locale, entry point KB) ma rimanda alla KB per la reference completa
- chiude con una tabella "Riferimenti rapidi" che mappa intenti operativi ai nodi KB
- la dimensione è un segnale: oltre ~100 righe è probabile sovrapposizione con la KB
- mai usata come fonte di fatti per gli audit: il filesystem o i nodi tematici sono le fonti di verità (vedi fedelta-cognitiva)

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | Ricetta molto coerente: README, CLAUDE, AGENTS, log, `todo/`, `scripts/`, skill e mappa canonica sono presenti e distinti. | È il riferimento operativo per un progetto code-based: pochi componenti locali, fonti dichiarative forti e strumenti anti-drift maturi. |
| `bi` | Struttura completa e ricca: README, CLAUDE, AGENTS, log, `todo/`, `scripts/`, skill, presentazione, client e mappa. | Il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale. |
| `economia` | Struttura completa con componenti locali aggiuntivi: `stato.md`, `scadenze.md`, `diario.md`, config, dati e output JSON. | Mostra che la ricetta deve ammettere file di dominio specializzati senza renderli universali. |
| `salute` | Struttura completa con KB molto ampia, fonti, diario, scadenze e skill ingest; README e CLAUDE restano narrativi. | È il caso storico/riflessivo: il metodo è presente, ma la separazione tra bootstrap, mappa, filosofia e istruzioni può migliorare. |

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni cognitive: ingresso, regole operative, memoria, task, conoscenza stabile, strumenti e fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, log o nodi.

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
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [log](log.md)
- [skill](skill.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
