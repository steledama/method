---
data: 2026-06-05
stato: bozza
---

# Goal

Altitudine intermedia nella gerarchia dell'azione. L'activity theory (Leontiev) articola il comportamento su tre livelli: *attività* (orientata al motivo — il perché profondo, il bisogno che muove), *azione* (diretta dal goal — l'obiettivo cosciente e formulato), *operazione* (condizionata dal contesto — la tecnica adattata alle condizioni correnti). Il goal è il livello medio: più concreto del motivo, più intenzionale dell'operazione. La stessa azione può servire motivi diversi; la stessa operazione può realizzare goal diversi.

In Norman il goal è l'apice del ciclo di azione: il punto da cui parte l'esecuzione (Goal → Plan → Specify → Perform) e a cui torna la valutazione (Perceive → Interpret → Compare → *nuovo Goal*). Norman lo presuppone come dato — il ciclo descrive come raggiungere un goal, non come formarlo. È il confine aperto del modello: tutto ciò che precede l'intenzione resta fuori.

## Il goal nel metodo

`goal`, `task` e `todo` sono tre altitudini, non sinonimi. Nel metodo:
- *goal* = l'obiettivo che orienta un arco di lavoro (livello azione, Leontiev)
- *task* = il compito operativo che lo realizza (livello operazione)
- `todo/` = la coda di operazioni concrete, eseguibili

Rinominare `todo/`→`goals/` sarebbe sbagliato: mescolarebbe altitudini e descriverebbe il contenuto in modo falso. Il nodo sul Goal esiste per tenere distinte le quote, non per cambiare la nomenclatura dei file.

## La KB informa il Goal, non lo genera

Il Goal non viene dalla KB — nasce all'incrocio tra motivo (che viene da sopra, dalla vita, dal committente) e KB (che informa, raffina, vincola). Quando la valutazione di un ciclo produce un esito, l'i3 lo scrive nella KB; il ciclo successivo *legge* da quella KB e forma il goal del nuovo ciclo. La KB è la memoria persistente dove il ciclo si chiude — ma non è la sorgente del motivo.

Questa distinzione ha una conseguenza di progetto: la KB e lo strato output devono essere *goal-guidati sulla rilevanza, neutri sulla valenza*. I goal determinano legittimamente cosa mostrare e a quale granularità (rilevanza); il verdetto buono/cattivo appartiene all'i3, non all'i2. Un i2 già carico di valenza riflette il bias di chi lo ha prodotto e annulla la funzione di sicurezza dell'arco di valutazione — l'artefatto non riesce più a portare cattive notizie.

## I due modi di i3

L'i3 — il Compare di Norman — ha due modalità che il modello originale non distingue esplicitamente:

- *Verdetto*: confronta l'esito di o3 con un goal esistente; chiude un loop noto. È il Norman puro.
- *Triage/formazione-goal*: elabora input esogeni (il mondo ha agito da solo — busta paga, normativa, alert) che aprono loop nuovi. Il goal non preesiste: si forma nell'i3.

Il secondo modo è l'estensione del metodo oltre Norman. Conseguenza per il design dell'autonomia: si può delegare la chiusura di loop noti (verdetto), ma la formazione del goal — decidere cosa conta — è la cosa meno esternalizzabile nell'artefatto. È il criterio che differenzia i domini: `nixos` (motivo codificabile, autonomia alta) da `salute` (motivo non esternalizzabile, supervisione permanente).

## Riferimenti

- Alexei Leontiev, _Activity, Consciousness, and Personality_ (1978) — gerarchia attività/azione/operazione; fonte primaria non disponibile in `sources/`.
- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition (2013), Cap. 2 — il Goal come apice del ciclo a sette stadi; cfr. `ciclo-azione`.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [sistema-cognitivo](sistema-cognitivo.md)
- [artefatto-cognitivo](artefatto-cognitivo.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [metodo-kb](metodo-kb.md)
