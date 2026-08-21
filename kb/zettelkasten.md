---
stato: maturo
---

# Zettelkasten

Metodo di gestione della conoscenza basato su unità interconnesse, associato al
lavoro del sociologo Niklas Luhmann. Il nome significa letteralmente "scatola
di appunti". Luhmann descrive lo schedario come un partner di comunicazione:
ogni unità acquista valore attraverso riferimenti e percorsi che permettono
combinazioni non previste in anticipo. Nel metodo questa idea viene tradotta
nella disciplina dei nodi atomici e della struttura emergente.

Robert Pirsig descrive in _Lila_ una pratica affine di schede riorganizzabili.
È un esempio letterario della manipolazione materiale delle idee, non la fonte
del modello né la prova di una discendenza diretta da Luhmann.

Un precursore meno noto vive nella cornice di sistema di Douglas Engelbart: il sistema di schede _edge-notched_ descritto in _Augmenting Human Intellect_ (1962, §III-A-3) è uno **Zettelkasten ante litteram** — nodi atomici con link tipizzati e provenienza, manipolabili meccanicamente con ferri da calza che selezionano le carte tagliate sul bordo. Engelbart lo accompagna alla mossa di ingest che il metodo riconosce come propria — «type the article in, tear it apart... it sits in the archives like an orange rind», l'articolo grezzo digerito in note collegate — segno che la disciplina dell'unità atomica era già parte di un sistema di augmentation co-evolvente (cfr. `augmentation-system`).

Caratteristiche:

- principio di atomicità: ogni nodo contiene un'unica idea, espressa in modo autonomo
- interconnessione: i nodi si collegano tra loro creando una rete di relazioni
- struttura emergente: l'organizzazione nasce dal basso, dalle connessioni, non da categorie predefinite
- crescita organica: il sistema si sviluppa gradualmente con l'aggiunta di nuovi nodi e nuovi collegamenti
- separazione tra raccolta e organizzazione: le idee vengono prima catturate, poi integrate nella rete
- dialogo con il sistema: rileggere e attraversare i collegamenti stimola connessioni inattese
- strumento di creatività: la giustapposizione di idee diverse genera nuove possibilità
- supporto al pensiero critico: riformulare le idee con parole proprie obbliga a comprenderle in profondita
- apprendimento attivo: scrivere e collegare è un modo di pensare, non solo di archiviare

Adattamento operativo:

- i nodi non sono categorie, ma unità interrogabili
- il catalogo `kb/kb.md` è una mappa di accesso, non una gerarchia rigida
- i cluster dell'indice possono cambiare senza rinominare i nodi
- i task aperti non sono nodi: vivono in `o1/plan.md` e `o2/`
- le fonti non sono nodi: alimentano la creazione o revisione dei nodi
- i fili `i3/` non sono nodi: registrano il verdetto attuale per filo aperto, non un concetto stabile

Regola pratica:

- se il contenuto serve a capire un concetto, va in kb/
- se serve a fare una cosa futura, va in `o1/plan.md` o in `o2/`
- se spiega una decisione già presa, va in un filo `i3/`
- se istruisce un agente, va in CLAUDE.md o in una skill
- se orienta il lettore, va in README.md
- se è una sintesi, una vista d'insieme o un dashboard, va nello strato output del progetto, non in kb/

Nel metodo, lo Zettelkasten sta dentro la cornice di augmentation di Engelbart, dove occupa il means _Language_ (cfr. `augmentation-system`): fornisce la disciplina che regola la forma dei nodi — ogni nodo è atomico, le sintesi non stanno nel nodo. Lo strato output è il corollario diretto di questa disciplina: ospita le sintesi karpathiane, le viste e i dashboard che non possono entrare in kb/ senza violare l'atomicità. Senza lo strato output, la pressione di sintesi finisce dentro i nodi e corrompe il principio fondante.

## Riferimenti

- Niklas Luhmann, «Kommunikation mit Zettelkästen» (1981), fonte della
  descrizione dello schedario come partner di comunicazione.
- Robert M. Pirsig, _Lila: An Inquiry into Morals_ (1991), descrizione della
  pratica delle schede.
- Douglas C. Engelbart, _Augmenting Human Intellect_ (1962), §III-A-3, per il
  sistema edge-notched e l'ingest in unità collegate; provenienza nel register
  `world.md`.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [karpathy-pattern](karpathy-pattern.md)
- [augmentation-system](augmentation-system.md)
- [node](node.md)
- [connection](connection.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
