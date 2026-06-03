---
data: 2026-05-24
stato: maturo
---

# Metodo KB

Il metodo KB è il modo operativo con cui una knowledge base personale viene costruita, mantenuta e resa navigabile con l'aiuto di un LLM. Si appoggia su tre pilastri: lo Zettelkasten definisce la forma dei nodi atomici e interconnessi; il pattern Karpathy definisce il ciclo di manutenzione dell'insieme, dove fonti, domande e sintesi vengono progressivamente compilate in una rete persistente; Norman fornisce il modello che traduce la KB in azione possibile nel mondo, chiudendo il ciclo tra accumulazione della conoscenza e comportamento reale.

Il principio centrale è che la KB non è una cartella di appunti né un archivio da interrogare occasionalmente. È un artefatto cumulativo: ogni ingest, query, lint o filing back deve lasciare il sistema più chiaro, più collegato o più verificabile di prima. La struttura non viene imposta dall'alto con categorie rigide; emerge dalle connessioni tra i nodi. La struttura esplicita appartiene invece al progetto che ospita la KB: README, istruzioni agent, log, strumenti e task aperti.

Il metodo è portabile tra progetti diversi. La sua parte stabile riguarda forma dei nodi, strumenti di manutenzione, memoria interpretativa, indice, task aperti e collaborazione con LLM; la parte locale riguarda dominio, cluster, lessico, fonti, vincoli tecnici e priorità. Il principio generale è neutro: relazionalità, significato emergente dalle connessioni, conoscenza come rete invece che come archivio di elementi isolati.

Lo sviluppo del metodo è bottom-up. Una modifica metodologica sana nasce da un'esigenza concreta in un repo adottante: un problema reale di dominio obbliga a inventare o correggere una pratica locale; se la soluzione si dimostra riusabile, viene riportata nel repo `metodo` come generalizzazione portabile; gli altri repo adottanti la ricevono poi leggendo i commit del metodo e applicando solo ciò che è pertinente. Il flusso inverso — aprire in `metodo` task che ordinano interventi nei repo adottanti — è da evitare salvo manutenzioni che riguardino davvero il metodo stesso.

Il repo che ospita il metodo ha anche una funzione di osservatorio. Raccoglie le differenze tra progetti adottanti, confronta componenti, strumenti, skill e salute delle KB, e decide se un segnale debba diventare generalizzazione metodologica, estensione strumentale o restare lavoro locale nel progetto interessato. Osservare non significa orchestrare: il repo `metodo` custodisce le astrazioni emerse, non sostituisce le code operative dei repo adottanti.

Indice cognitivo del metodo:

- `AGENTS.md`: dove trovo le istruzioni operative condivise tra agenti?
- `CLAUDE.md`: come devo agire in questo repo?
- `README.md`: dove sono e da dove parto?
- README / indice: quali nodi esistono e come li trovo?
- README / tasks: cosa dobbiamo fare adesso?
- mappa: come si tiene insieme questo dominio?
- nodo: che cosa significa questo concetto specifico?
- connessioni: a quali altri concetti è legato?
- `todo/`: quali sono i dettagli operativi e di contesto dei singoli task aperti?
- `log.md`: perché una decisione o una sessione conta?
- git history: che cosa è cambiato davvero?
- `scripts/`: quali controlli sono deterministici?
- skill: quali workflow ricorrenti sono codificati?
- fonti di verità: contro che cosa verifico ciò che la KB dice?
- fedeltà cognitiva: la KB aderisce ancora al sistema reale?
- osservatorio metodo: che cosa impariamo confrontando i progetti?
- Metodo KB: qual è la ricetta generale?

Ricetta metodologica:

- `kb/`: spazio della conoscenza stabile. Contiene i nodi di metodo e i nodi di dominio. Il nucleo metodologico portabile comprende `metodo-kb`, `knowledge-base`, `nodo`, `zettelkasten`, `pattern-karpathy`, `struttura-progetto`, `strumenti-kb`, `connessione` e, quando il dominio richiede verifica anti-drift, `fedelta-cognitiva`. Nei progetti che usano il metodo come dipendenza, questi nodi possono vivere in `metodo/` come symlink o sottoalbero separato, mentre `kb/` resta dedicata al dominio.
- `README.md`: file di bootstrap per umano e LLM. Presenta nome, dominio, scopo, principi locali, task aperti e indice statico della KB. È il primo punto di accesso e deve permettere di orientarsi senza leggere tutto il repository. Nei progetti grandi può contenere router per intenzione, cataloghi per cluster e pointer alla mappa canonica.
- `CLAUDE.md`: costituzione operativa del progetto. Contiene regole d'azione, vincoli, workflow consentiti e riferimenti rapidi per agenti; non contiene conoscenza di dominio né descrizioni narrative del sistema. Quando cresce oltre il ruolo operativo, il contenuto va trasferito nei nodi tematici e sostituito da pointer.
- `AGENTS.md`: wrapper agent-agnostico minimale. Non duplica le regole operative; esplicita l'ordine di lettura e rimanda a `README.md` e `CLAUDE.md`, così agenti diversi entrano nello stesso protocollo di lavoro.
- `log.md`: memoria interpretativa append-only delle sessioni significative. Il git log conserva cosa è cambiato; `log.md` conserva perché una decisione, un ingest, una revisione o un cambio di approccio contano. Non è un archivio di output automatici.
- `todo/`: spazio dei task futuri con contesto operativo. La tabella Tasks aperti del README ne è l'indice: ogni task sostanziale ha una riga e, quando serve contesto, un file dedicato. I task completati vengono rimossi; la storia resta in git, log e nodi aggiornati.
- `scripts/`: strumenti versionati per la parte deterministica della manutenzione. `scripts/kb_tools.py`, quando presente, gestisce audit, link, backlink, README, migrazione, candidati terminologici e controlli specifici di dominio. Gli script devono produrre segnali verificabili; il giudizio resta umano/LLM.
- `.claude/skills/`: interfacce operative per workflow ricorrenti. La triade base ufficiale del metodo è `audit-kb` (diagnosi), `revisione-tasks` (supervisione del lavoro futuro) e `commit` (gate di filing back). Ogni progetto può aggiungere skill locali per workflow di dominio. Una skill interpreta e orchestra gli strumenti versionati, senza reimplementare parsing fragile in chat.
- `.codex/skills/`: wrapper opzionali quando il progetto deve essere usabile anche da Codex. Devono rimandare alle skill canoniche senza duplicare workflow.
- strato output (ponte): il livello che traduce la KB in azione possibile, separando output macchina (L1), decisione umana (L2) e azione nel mondo (L3). Il nome locale dipende dal dominio (`quadro/`, `presentazione/`, `output/`, configurazione di sistema), non dal metodo. La funzione è universale: senza strato output la KB non chiude il ciclo di azione e la conoscenza non produce comportamento reale. Modello completo e criteri di Norman in `ponte` e `ciclo-azione`.
- convenzioni markdown: frontmatter minimale per nodi e task, nessun frontmatter nei file root, H1, corpo autonomo, link inline solo quando servono alla frase, sezione finale `Connessioni:` come footer di navigazione. Il dettaglio vive nei nodi `nodo` e `todo`.

Creazione di un nuovo progetto:

- partire dalla ricetta metodologica come checklist, non come gerarchia concettuale
- personalizzare nome, dominio, scopo, cluster iniziali, fonti di verità e task aperti
- generare `README.md` come bootstrap e indice statico
- generare `CLAUDE.md` come costituzione operativa, non come documentazione narrativa
- generare `AGENTS.md` come wrapper minimale verso `README.md` e `CLAUDE.md`
- creare `log.md` vuoto o con una prima entry di fondazione
- creare `todo/` e inserirvi solo lavoro futuro, mai storico
- creare almeno i nodi dominio iniziali se il progetto ha già concetti stabili
- aggiungere `scripts/`, skill e wrapper solo quando esistono workflow reali da rendere ripetibili

Ogni componente della ricetta merita un nodo autonomo, anche quando è ancora in stato bozza. Il nodo autonomo rende esplicita la funzione cognitiva del componente, permette confronti cross-repo e segnala quali parti del metodo sono mature e quali sono ancora work in progress. Un componente può essere descritto anche in `struttura-progetto`, ma il suo nodo dedicato resta il punto in cui accumulare regole, esempi reali e criteri di revisione.

Evidenza dai progetti adottanti:

- `nixos` e `bi` usano il metodo come nucleo condiviso linkato da `metodo/`, con README molto forti come router e mappe di progetto specifiche
- `economia` incorpora una variante locale con file aggiuntivi (`stato.md`, `scadenze.md`, `diario.md`) e fonti di verità JSON, mostrando che la ricetta deve ammettere componenti di dominio senza assorbirli nel nucleo portabile
- `salute` conserva una forma più narrativa del metodo nel README, utile come traccia storica ma meno separata tra metodo portabile, filosofia locale e indice della KB
- i progetti tecnici richiedono strumenti anti-drift e fonti di verità verificabili; i progetti riflessivi richiedono soprattutto accessi cognitivi, hub semantici e filing back accurato
- ogni progetto adottante ha già uno strato output, anche senza averlo nominato; dove L2 è forte il progetto serve decisioni condivise con altri (`bi`); dove L2 è debole la KB resta introspettiva e fatica a generare azione coordinata

La fotografia comparativa corrente vive nel nodo `confronto-progetti-adottanti`. I nodi dei singoli componenti contengono invece il dettaglio per progetto, così il confronto non resta una nota generale ma diventa parte della definizione pratica del componente.

Tipi documentali:

- mappa: orienta sull'insieme e collega concetti a fonti di verità
- nodo concettuale: spiega un'idea stabile e riusabile
- reference: rende accessibili dati o convenzioni da consultare rapidamente
- runbook: guida un'azione operativa con sequenza e verifiche
- todo/: conserva lavoro futuro e contesto transitorio
- log.md: conserva motivazioni e decisioni nel tempo

Le categorie non sono gabbie formali, ma aiutano a preservare funzione e
aspettative di lettura. Quando più tipi iniziano a convivere nello stesso file,
la KB diventa meno accessibile anche se il contenuto resta corretto.

Operazioni ricorrenti:

- ingest: una fonte viene trasformata in conoscenza compilata, cioè nodi nuovi o aggiornamenti a nodi esistenti
- query: una domanda attraversa la rete dei nodi e può produrre una risposta temporanea o un nuovo contenuto stabile
- lint: la KB viene controllata per link rotti, orfani, cluster isolati, nodi non indicizzati e problemi di formato
- fidelity: fatti ad alta deriva e copertura documentale vengono confrontati con
  fonti tecniche verificabili, senza confondere segnali automatici e giudizio
  semantico
- filing back: le sintesi nate in chat o nel diario vengono riportate nella KB quando hanno valore durevole
- revisione strutturale: si verifica se i nodi hanno ancora funzione limpida, aderenza al presente e accessi cognitivi adeguati
- commit: le modifiche vengono consolidate in git con messaggi brevi e leggibili

Regole sullo stato:

- ciò che è stabile e riusabile diventa nodo in kb/
- ciò che è da fare resta nella tabella Tasks aperti del README o in todo/
- ciò che è stato fatto sparisce da todo/ e viene conservato da git, log.md e dai nodi aggiornati
- ciò che spiega perché una decisione conta va in log.md
- ciò che spiega come lavorare va in CLAUDE.md, skill o strumenti versionati
- ciò che serve solo come appunto temporaneo non entra nel metodo finché non diventa task, nodo o log
- la KB permanente descrive il presente; la storia resta in git e log.md salvo che diventi concetto riusabile
- una generalizzazione metodologica entra in `metodo` solo dopo evidenza locale sufficiente in almeno un repo adottante, e idealmente con verifica di portabilità su almeno un secondo contesto

Regole di revisione:

- separare per audience o responsabilità quando lettori diversi hanno bisogno di istruzioni diverse
- separare stato corrente, procedura e storia quando iniziano a convivere nello stesso nodo
- distinguere mappa, concetto, reference e runbook prima ancora di chiedersi se il file sia lungo
- creare nuovi nodi solo se migliorano accessibilità e stabilità semantica
- preferire esempi realmente incarnati nel dominio a esempi didattici plausibili ma non verificati
- quando due flussi possono divergere nel tempo, documentarli separatamente anche se oggi sono ancora vicini
- trattare i warning anti-drift come inviti alla revisione, non come errori da
  sopprimere automaticamente
- i file operativi (CLAUDE.md, skill, hook) sono costituzione, non documentazione: le descrizioni di come funziona qualcosa appartengono ai nodi tematici, mai al file operativo, che ne è solo il pointer
- quando un file operativo cresce a contenere descrizioni del sistema, trasferire il contenuto nei nodi tematici prima di rimuoverlo dal file operativo (mappa per sezione: keep / relocate / remove, poi arricchimento dei nodi target, poi rimozione)
- quando un elenco metodologico compare in più punti, mantenerlo una sola volta come ricetta e usare gli altri punti per descrivere funzione, variazioni locali o procedura
- quando un componente del metodo accumula regole proprie, esempi cross-repo e criteri di revisione, promuoverlo a nodo autonomo collegato da questo hub
- quando una tensione metodologica emerge in un repo adottante, risolverla prima lì; aggiornare `metodo` solo dopo aver distinto soluzione locale, criterio portabile e propagazione eventuale agli altri repo

Personalizzazioni locali:

- nome, dominio e scopo del progetto
- cluster dell'indice README
- fonti e directory specialistiche
- task aperti e priorità
- lessico specifico del dominio
- eventuali interpretazioni filosofiche locali del metodo

Connessioni:

- [nodo](nodo.md)
- [knowledge-base](knowledge-base.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [strumenti-kb](strumenti-kb.md)
- [agents](agents.md)
- [claude](claude.md)
- [readme](readme.md)
- [indice](indice.md)
- [task-aperti](task-aperti.md)
- [mappa](mappa.md)
- [todo](todo.md)
- [log](log.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [fonte-di-verita](fonte-di-verita.md)
- [osservatorio-metodo](osservatorio-metodo.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [design-principles](design-principles.md)
- [zettelkasten](zettelkasten.md)
- [connessione](connessione.md)
- [ponte](ponte.md)
- [ciclo-azione](ciclo-azione.md)
