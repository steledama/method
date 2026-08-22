---
stato: maturo
---

# Cognitive artifact design

Il _cognitive artifact design_ è la pratica con cui si progettano e si
mantengono artefatti cognitivi per la cognizione condivisa tra umano e LLM. Non
progetta soltanto una knowledge base: progetta l'intero ciclo che collega Goal,
rappresentazioni persistenti, decisione, azione nel `world`, percezione del
ritorno e revisione. La KB è lo strato riflessivo dell'artefatto, necessario ma
non sufficiente — riflessiva come _livello_ di elaborazione, e nucleo
formalizzato del _system image_, che è invece l'intero artefatto, trasversale ai
tre livelli e canale tra agenti (cfr. `system-image`, `processing-layers`).

L'oggetto progettato è l'**artefatto cognitivo**: il repository portabile con la
sua anatomia, le rappresentazioni e i vincoli. Il risultato nell'uso è il
**sistema cognitivo**: l'accoppiamento dinamico tra artefatto, umano, LLM,
harness e ambiente. Il metodo coltiva il primo perché il secondo possa
funzionare, senza confondere ciò che persiste con agenti e infrastrutture che
cambiano.

Il ciclo completo comprende tre altitudini. In alto, la KB accumula concetti,
assunzioni e verdetti nello strato riflessivo. In mezzo, o2/i2 rende la sintesi
leggibile per specificare e interpretare. In basso, o3 e i1 sono i riflessi
versionati on-demand della membrana `world`: prescrizione dell'atto e cattura
del segnale. L'atto e il grezzo restano nel Mondo non versionato. Progettare
l'artefatto significa rendere attraversabili entrambi i gulf, non soltanto
organizzare bene i nodi.

Il grado di automazione non è uniforme. Le operazioni note e verificabili
possono essere delegate; formazione del Goal, triage dei segnali esogeni e
decisioni ad alta posta richiedono supervisione umana. Il gradiente di autonomia
si progetta per stadio, dominio e rischio, mantenendo espliciti feedback,
vincoli e punti di controllo.

Il metodo si inscrive nella cornice di augmentation di Engelbart (H-LAM/T), che
contiene i suoi riferimenti: lo Zettelkasten definisce la forma dei nodi atomici
e interconnessi (il means _Language_); Norman fornisce il modello che collega
conoscenza, rappresentazione e azione attraverso il ciclo completo
(l'interfaccia col Mondo); la gamba di manutenzione dell'insieme con l'LLM è il
_Methodology/ Training_ engelbartiano, di cui il pattern Karpathy è l'istanza
contemporanea. Il pavimento ontologico — perché il sistema accoppiato sia
cognizione — è Hutchins/Clark. La trattazione vive in `augmentation-system` e
`cognitive-system`.

Il principio centrale è che l'artefatto non è una cartella di appunti né un
archivio da interrogare occasionalmente. È cumulativo: ogni ingest, query, lint
o filing back deve lasciarlo più chiaro, più collegato o più verificabile di
prima. La struttura della KB emerge dalle connessioni tra i nodi; la struttura
esplicita appartiene al progetto intero: root, cruscotto nelle collezioni `o1/`
e `i3/`, cataloghi interni, collezioni-stadio, strati input/output e membrana
`world`.

Il metodo è portabile tra progetti diversi. La sua parte stabile riguarda forma
dei nodi, strumenti di manutenzione, memoria interpretativa, indice, task aperti
e collaborazione con LLM; la parte locale riguarda dominio, cluster, lessico,
fonti, vincoli tecnici e priorità. Il principio generale è neutro:
relazionalità, significato emergente dalle connessioni, conoscenza come rete
invece che come archivio di elementi isolati.

Lo sviluppo del metodo procede per due movimenti complementari in alternanza —
l'esigenza che sale da un dominio reale e la cornice teorica che scende a darle
forma — ai quali si affianca, sul lato runtime e con pari dignità, l'**output di
canone** che `metodo` pianifica e che l'adottante recepisce eseguendolo. La
linea di faglia che li tiene onesti separa il pianificare il proprio canone dal
gestire la coda altrui. La trattazione, con i fallimenti propri di ciascun
movimento e il distinguo tra i due top-down, vive in `method-development`.

Il repo che ospita il metodo ha anche una funzione di osservatorio. Raccoglie le
differenze tra progetti adottanti, confronta componenti, strumenti, skill e
salute delle KB, e decide se un segnale debba diventare generalizzazione
metodologica, estensione strumentale o restare lavoro locale. La diagnosi può
sfociare in prescrizione di canone; non autorizza a gestire la coda interna
degli adottanti.

## Superfici del metodo

Questo nodo è l'hub concettuale stabile, non la ricetta completa né un manuale.
Le responsabilità operative hanno case autonome:

- anatomia e collocazione dei componenti in `project-structure`;
- orientamento e bootstrap in `readme` e `claude`;
- forma e manutenzione della conoscenza in `knowledge-base`, `node`,
  `connection` e `kb-tools`;
- poli e archi del ciclo in `goal`, `world`, `input`, `output` e `action-cycle`;
- lavoro corrente in `plan`, `tasks` e `verdict`;
- sviluppo e propagazione in `method-development` e `method-observatory`;
- verifica semantica e fonti in `cognitive-fidelity` e `source-of-truth`.

Un nuovo progetto adotta queste superfici solo quando hanno una funzione reale
nel dominio. Il nucleo canonico può vivere nel symlink `method/`, mentre la KB
locale conserva i concetti specifici. Nuovi nodi, strumenti e skill entrano
quando migliorano accessibilità o rendono ripetibile un workflow già osservato,
non per completare preventivamente un inventario.

Connessioni:

- [cognitive-artifact](cognitive-artifact.md)
- [cognitive-system](cognitive-system.md)
- [augmentation-system](augmentation-system.md)
- [world](world.md)
- [input](input.md)
- [processing-layers](processing-layers.md)
- [system-image](system-image.md)
- [node](node.md)
- [knowledge-base](knowledge-base.md)
- [karpathy-pattern](karpathy-pattern.md)
- [project-structure](project-structure.md)
- [kb-tools](kb-tools.md)
- [claude](claude.md)
- [readme](readme.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [source-of-truth](source-of-truth.md)
- [method-observatory](method-observatory.md)
- [method-development](method-development.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [design-principles](design-principles.md)
- [zettelkasten](zettelkasten.md)
- [connection](connection.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
