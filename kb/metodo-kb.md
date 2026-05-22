---
data: 2026-05-09
stato: maturo
---

# Metodo KB

Il metodo KB è il modo operativo con cui una knowledge base personale viene costruita, mantenuta e resa navigabile con l'aiuto di un LLM. Nasce dall'incontro tra Zettelkasten e pattern Karpathy: lo Zettelkasten definisce la forma dei nodi atomici e interconnessi; il pattern Karpathy definisce il ciclo di manutenzione dell'insieme, dove fonti, domande e sintesi vengono progressivamente compilate in una rete persistente.

Il principio centrale è che la KB non è una cartella di appunti né un archivio da interrogare occasionalmente. È un artefatto cumulativo: ogni ingest, query, lint o filing back deve lasciare il sistema più chiaro, più collegato o più verificabile di prima. La struttura non viene imposta dall'alto con categorie rigide; emerge dalle connessioni tra i nodi. La struttura esplicita appartiene invece al progetto che ospita la KB: README, istruzioni agent, log, strumenti e task aperti.

Il metodo è portabile tra progetti diversi. La sua parte stabile riguarda forma dei nodi, strumenti di manutenzione, log, indice e collaborazione con LLM; la parte locale riguarda dominio, cluster, lessico, fonti e priorità. Il principio generale è neutro: relazionalità, significato emergente dalle connessioni, conoscenza come rete invece che come archivio di elementi isolati.

Componenti portabili:

- nodi metodo: metodo-kb, nodo, knowledge-base, pattern-karpathy, struttura-progetto, strumenti-kb, zettelkasten, connessione
- README.md: bootstrap iniziale per umano e LLM, con presentazione del progetto, metodo, task aperti e indice statico
- CLAUDE.md: costituzione operativa del progetto, con convenzioni, workflow e regole di manutenzione
- AGENTS.md: wrapper minimo che indirizza ogni agente a README.md e CLAUDE.md
- log.md: memoria interpretativa append-only delle sessioni significative
- todo/: task aperti con contesto operativo, cancellabili quando completati
- scripts/kb_tools.py: backend deterministico per audit, link, backlink, README, migrazione e candidati terminologici
- skill audit-kb: interfaccia LLM che usa gli script versionati e interpreta i risultati
- convenzioni markdown: frontmatter minimale, H1, corpo senza link inline, sezione finale Connessioni

Skeleton minimo:

- kb/: contiene gli otto nodi metodo e i nodi del dominio
- README.md: descrizione breve, principi, sezione Tasks aperti, indice statico della KB
- CLAUDE.md: istruzioni operative per gli agenti, incluso leggere README.md a inizio sessione
- AGENTS.md: wrapper che dice di leggere README.md e poi CLAUDE.md
- log.md: memoria interpretativa delle sessioni significative
- todo/: dettagli dei task aperti, con .gitkeep se non ci sono task
- scripts/: strumenti versionati, incluso kb_tools.py quando il progetto richiede audit deterministico
- .claude/skills/: skill progetto per audit-kb, commit ed eventuali workflow locali
- .codex/skills/: wrapper delle skill Claude quando il progetto deve essere usabile anche da Codex

Prompt di creazione:

- creare la struttura minima del progetto seguendo questi otto nodi metodo
- personalizzare nome, dominio, scopo, cluster iniziali e task aperti
- generare README.md come file di bootstrap e indice statico
- generare CLAUDE.md come costituzione operativa, non come documentazione narrativa
- generare AGENTS.md come wrapper minimale verso README.md e CLAUDE.md
- creare log.md vuoto o con una prima entry di fondazione
- creare todo/ e inserire solo task futuri, mai storico
- creare almeno i nodi dominio iniziali se il progetto ha già concetti stabili

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
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [zettelkasten](zettelkasten.md)
- [connessione](connessione.md)
