---
data: 2026-05-09
stato: maturo
---

# Connessione

La connessione è il modo in cui un nodo si apre alla rete della knowledge base. In markdown può essere espressa con due strategie: link inline nel corpo del testo o link raccolti a fondo nodo in una sezione finale dedicata. La scelta non è puramente estetica: cambia il modo in cui si scrive, si legge e si naviga la rete, sia da parte di un umano che di un LLM.

Inline: il link appare nel punto esatto in cui il concetto viene menzionato. Il lettore viene segnalato del collegamento nel contesto in cui è rilevante. Il testo acquista il ritmo di una rete ipertestuale navigabile subito. Il costo è la frammentazione visiva: il corpo del nodo diventa più difficile da leggere come prosa, lo stesso nodo può apparire più volte creando rumore, la lista completa dei vicini non è mai visibile in un colpo d'occhio.

Footer: tutte le connessioni raccolte in una sezione finale dedicata, separata dal corpo del nodo. Il corpo diventa prosa pura, leggibile senza interruzioni; la sezione Connessioni è l'interfaccia esplicita del nodo verso la rete. Il costo è la perdita del contesto immediato: il lettore deve spostarsi in fondo per sapere verso dove può navigare. Questo costo è basso per un LLM (che legge l'intero nodo in una passata) ma più sentito per un umano che legge scorrendo.

La scelta dei footer, in questo progetto, poggia su tre ragioni convergenti. Prima: il testo è più godibile da scrivere e da leggere senza il rumore sintattico dei link inline. Seconda: la manutenzione dei footer — deduplica, ordinamento per occorrenza, aggiornamento dopo rinominamenti — è esattamente il tipo di lavoro in cui un LLM eccelle e un umano è lento; spostare questo peso sull'LLM rende il sistema più sostenibile. Terza: la forma footer rispecchia meglio il modo in cui sia la mente umana che un LLM navigano una rete semantica — prima si comprende il nodo, poi si valutano i vicini.

Inline:

- il contesto del link è nel testo (si sa perché è collegato)
- navigazione immediata durante la lettura
- stesso target può apparire più volte (rumore visivo)
- lista vicini non leggibile a colpo d'occhio
- manutenzione manuale costosa per l'umano

Footer:

- corpo del nodo leggibile come prosa pura
- interfaccia del nodo esplicita e scannable
- manutenzione delegabile all'LLM (deduplica, ordina)
- coerente con la struttura a rete: prima comprendi il nodo, poi valuti i vicini
- il contesto del link non è esplicito nel testo

Regole del progetto:

- i link tra nodi stanno nella sezione finale Connessioni
- i link nel corpo dei nodi sono evitati anche quando sarebbero comodi
- le connessioni sono deduplicate
- le connessioni puntano a filename relativi nello stesso folder quando sono nodi della stessa KB
- i link cross-folder tra kb/ e altre directory sono evitati nei nodi
- README può linkare liberamente ai nodi perché è un indice, non un nodo
- todo/ può linkare a kb/ con percorso esplicito quando serve contesto operativo
- le rinominazioni richiedono aggiornamento dei link e audit

Ordinamento:

- prima i nodi più direttamente necessari alla comprensione
- poi i nodi di contesto o metodo
- evitare elenchi troppo lunghi se il nodo non dialoga davvero con tutti i target
- un nodo senza backlink è un segnale da valutare, non automaticamente un errore

Connessioni:

- [metodo-kb](metodo-kb.md)
- [zettelkasten](zettelkasten.md)
