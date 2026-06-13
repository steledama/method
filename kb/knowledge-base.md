---
data: 2026-05-24
stato: maturo
---

# Knowledge base

Una knowledge base (KB) basata su LLM è un artefatto persistente e cumulativo: non un sistema di recupero delle informazioni (RAG), ma una rete di nodi interconnessi che cresce e si consolida nel tempo. Quando si aggiunge una nuova fonte, l'LLM non si limita a indicizzarla per il recupero futuro — la legge, ne estrae la conoscenza rilevante e la integra nella rete esistente, aggiornando i nodi correlati, segnalando le contraddizioni, rafforzando le connessioni. La conoscenza è compilata una volta e mantenuta aggiornata, non ri-derivata a ogni interrogazione.

Per essere davvero utile a un LLM, però, la KB non deve solo contenere conoscenza corretta: deve offrirla attraverso una buona interfaccia cognitiva. Servono punti di ingresso, mappe, router per intenzione, fonti di verità riconoscibili e nodi con funzioni distinguibili. Una rete formalmente sana ma priva di accessi leggibili costringe l'LLM a ricostruire ogni volta il modello del dominio; una KB ben progettata rende esplicito quel modello e abbassa il costo di comprensione.

Il sistema poggia su tre pilastri metodologici — Zettelkasten (forma del nodo atomico), pattern Karpathy (manutenzione dell'insieme con l'LLM), Norman (ciclo di azione tra utente e sistema). La trattazione completa dei tre giganti vive in `ciclo-azione`: qui basta sapere che insieme coprono come pensare i nodi, come mantenerli nel tempo e come chiudere il ciclo producendo azione nel mondo.

La KB non è il fine: è lo strato riflessivo dell'artefatto. Lo strato output
traduce la conoscenza in azione possibile (o1/o2/o3); lo strato input cattura e
interpreta il ritorno (i1/i2/i3); l'atto e il grezzo attraversano la membrana
`world`. Senza questi strati, la KB accumula conoscenza ma non chiude il ciclo
tra comprensione e comportamento.

La divisione del lavoro tra umano e LLM è asimmetrica per design. L'umano cura le fonti, dirige l'analisi, pone le domande giuste, scrive e corregge nel dettaglio — l'authorship resta sempre umana. L'LLM gestisce la manutenzione: cross-referencing, deduplica dei link, aggiornamento dei footer Connessioni, health check periodico. Questa asimmetria è sostenibile perché il costo di manutenzione per l'LLM è quasi nullo, mentre per un umano crescerebbe fino ad abbandonare il sistema. Umano e LLM sono qui il caso saliente di una popolazione di agenti più ampia (cfr. `agente`): la stessa divisione del lavoro può ripartirsi tra livelli di agente — per capacità e per stadio del ciclo — quando l'uso multi-agente diventa reale.

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
- tasks/ contiene lavoro futuro e contesto operativo temporaneo
- verdict.md contiene il perché delle sessioni significative, non una lista di commit
- README.md contiene l'orientamento e punta al catalogo `kb.md`, non tutta la conoscenza
- CLAUDE.md contiene regole operative per agenti, non contenuto di dominio
- fonti o data contengono materiali grezzi o elaborati, non nodi atomici

Portabilità:

- un nuovo progetto può partire dai nodi del nucleo portabile
- ogni progetto deve poi aggiungere nodi specifici del dominio
- i nodi del nucleo portabile non devono dipendere da dettagli di un singolo repository
- le parti locali vanno in README.md, CLAUDE.md, skill e nodi dominio
- quando il metodo cambia in un progetto, valutare se la modifica è portabile agli altri

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [nodo](nodo.md)
- [zettelkasten](zettelkasten.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [strumenti-kb](strumenti-kb.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [connessione](connessione.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [agente](agente.md)
