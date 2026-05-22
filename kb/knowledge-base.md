---
data: 2026-05-09
stato: maturo
---

# Knowledge base

Una knowledge base (KB) basata su LLM è un artefatto persistente e cumulativo: non un sistema di recupero delle informazioni (RAG), ma una rete di nodi interconnessi che cresce e si consolida nel tempo. Quando si aggiunge una nuova fonte, l'LLM non si limita a indicizzarla per il recupero futuro — la legge, ne estrae la conoscenza rilevante e la integra nella rete esistente, aggiornando i nodi correlati, segnalando le contraddizioni, rafforzando le connessioni. La conoscenza è compilata una volta e mantenuta aggiornata, non ri-derivata a ogni interrogazione.

Per essere davvero utile a un LLM, però, la KB non deve solo contenere conoscenza corretta: deve offrirla attraverso una buona interfaccia cognitiva. Servono punti di ingresso, mappe, router per intenzione, fonti di verità riconoscibili e nodi con funzioni distinguibili. Una rete formalmente sana ma priva di accessi leggibili costringe l'LLM a ricostruire ogni volta il modello del dominio; una KB ben progettata rende esplicito quel modello e abbassa il costo di comprensione.

Il sistema poggia su due pilastri metodologici: lo Zettelkasten, che fornisce la filosofia dei singoli nodi (atomicità, interconnessione, struttura emergente dal basso), e il pattern Karpathy, che fornisce la metodologia di manutenzione dell'insieme (ingest, query, lint, filing back). I due si completano: lo Zettelkasten dice come pensare i nodi, il pattern Karpathy dice come gestire il sistema nel tempo con l'aiuto dell'LLM.

La divisione del lavoro tra umano e LLM è asimmetrica per design. L'umano cura le fonti, dirige l'analisi, pone le domande giuste, scrive e corregge nel dettaglio — l'authorship resta sempre umana. L'LLM gestisce la manutenzione: cross-referencing, deduplica dei link, aggiornamento dei footer Connessioni, health check periodico. Questa asimmetria è sostenibile perché il costo di manutenzione per l'LLM è quasi nullo, mentre per un umano crescerebbe fino ad abbandonare il sistema.

Caratteristiche:

- artefatto cumulativo: ogni ingest arricchisce la KB; le connessioni già tracciate non vanno ri-derivate
- formato portabile: markdown puro, leggibile ovunque, senza dipendenze da strumenti proprietari
- tre operazioni ricorrenti: ingest (nuova fonte → nodi), lint (audit periodico della rete), filing back (le sintesi di sessione non vanno perse nella chat)
- authorship umana: il LLM assiste, non sostituisce; scrivere e correggere è parte dell'obiettivo
- strumenti versionati: i controlli ripetitivi della KB vivono in script stabili, mentre il LLM interpreta e decide
- replicabile: lo schema si trasferisce tra progetti con minima personalizzazione; ogni progetto è autonomo
- interfaccia cognitiva: README, mappe e router rendono il dominio accessibile prima ancora della ricerca puntuale
- fedeltà cognitiva: la KB viene valutata anche per aderenza al sistema reale,
  non solo per link validi e formato corretto

Confini:

- kb/ contiene conoscenza stabile, non task aperti
- todo/ contiene lavoro futuro e contesto operativo temporaneo
- log.md contiene il perché delle sessioni significative, non una lista di commit
- README.md contiene l'orientamento e l'indice statico, non tutta la conoscenza
- CLAUDE.md contiene regole operative per agenti, non contenuto di dominio
- fonti o data contengono materiali grezzi o elaborati, non nodi atomici

Portabilità:

- un nuovo progetto può partire dagli otto nodi metodo come nucleo iniziale
- ogni progetto deve poi aggiungere nodi specifici del dominio
- gli otto nodi metodo non devono dipendere da dettagli di un singolo repository
- le parti locali vanno in README.md, CLAUDE.md, skill e nodi dominio
- quando il metodo cambia in un progetto, valutare se la modifica è portabile agli altri

Connessioni:

- [metodo-kb](metodo-kb.md)
- [nodo](nodo.md)
- [zettelkasten](zettelkasten.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [strumenti-kb](strumenti-kb.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [connessione](connessione.md)
