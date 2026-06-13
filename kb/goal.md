---
data: 2026-06-05
stato: bozza
---

# Goal

Altitudine intermedia nella gerarchia dell'azione. L'activity theory (Leontiev) articola il comportamento su tre livelli: _attività_ (orientata al motivo — il perché profondo, il bisogno che muove), _azione_ (diretta dal goal — l'obiettivo cosciente e formulato), _operazione_ (condizionata dal contesto — la tecnica adattata alle condizioni correnti). Il goal è il livello medio: più concreto del motivo, più intenzionale dell'operazione. La stessa azione può servire motivi diversi; la stessa operazione può realizzare goal diversi.

In Norman il goal è l'apice del ciclo di azione: il punto da cui parte l'esecuzione (Goal → Plan → Specify → Perform) e a cui torna la valutazione (Perceive → Interpret → Compare → _nuovo Goal_). Norman lo presuppone come dato — il ciclo descrive come raggiungere un goal, non come formarlo. È il confine aperto del modello: tutto ciò che precede l'intenzione resta fuori.

## Il goal nel metodo

`goal`, `task` e `tasks/` sono tre altitudini, non sinonimi. Nel metodo:

- _goal_ = l'obiettivo che orienta un arco di lavoro (livello azione, Leontiev)
- _task_ = il compito operativo che lo realizza (livello operazione)
- `tasks/` = la coda di operazioni concrete, eseguibili

Rinominare `tasks/`→`goals/` sarebbe sbagliato: mescolarebbe altitudini e descriverebbe il contenuto in modo falso. Il nodo sul Goal esiste per tenere distinte le quote, non per cambiare la nomenclatura dei file.

## La KB informa il Goal, non lo genera

Il Goal non viene dalla KB — nasce all'incrocio tra motivo (che viene da sopra, dalla vita, dal committente) e KB (che informa, raffina, vincola). Quando la valutazione di un ciclo produce un esito, l'i3 lo scrive nella KB; il ciclo successivo _legge_ da quella KB e forma il goal del nuovo ciclo. La KB è la memoria persistente dove il ciclo si chiude — ma non è la sorgente del motivo.

Questa distinzione ha una conseguenza di progetto: la KB e lo strato output devono essere _goal-guidati sulla rilevanza, neutri sulla valenza_. I goal determinano legittimamente cosa mostrare e a quale granularità (rilevanza); il verdetto buono/cattivo appartiene all'i3, non all'i2. Un i2 già carico di valenza riflette il bias di chi lo ha prodotto e annulla la funzione di sicurezza dell'arco di valutazione — l'artefatto non riesce più a portare cattive notizie.

## Formazione del Goal dai due archi

L'i3 — il Compare di Norman — ha due modalità che il modello originale non distingue esplicitamente:

- _Verdetto_: confronta l'esito di o3 con un goal esistente; chiude un loop noto. È il Norman puro.
- _Triage/formazione-goal_: elabora input esogeni (il mondo ha agito da solo — busta paga, normativa, alert) che aprono loop nuovi. Il goal non preesiste: si forma nell'i3.

Il secondo modo è l'estensione del metodo oltre Norman. Ma il goal-surfacing
può partire anche dall'arco di esecuzione: predisporre un o3, per esempio un
canovaccio, rende espliciti vincoli e poste e può rivelare Goal latenti. In
entrambi i casi il segnale arriva da un arco, mentre la formazione del Goal
resta un atto riflessivo. Conseguenza per il design dell'autonomia: si può
delegare la chiusura di loop noti (verdetto), ma decidere cosa conta è la cosa
meno esternalizzabile nell'artefatto. È il criterio che differenzia i domini:
`nixos` (motivo codificabile, autonomia alta) da `salute` (motivo non
esternalizzabile, supervisione permanente).

## Esempi per artefatto

Il goal è il polo opposto al Mondo: l'apice contro cui gli input percepiti dal fondo del ciclo vengono confrontati. Per ciascun artefatto adottante il goal sintetizza il motivo che lo muove (di cosa è fatto il Mondo è in `world`).

- `salute`: stare bene, declinato come equilibrio corpo-mente.
- `economia`: la graduale indipendenza dalla gestione condivisa con la sorella, l'acquisto della casa al mare, la semplificazione degli interessi e l'equilibrio tra entrate e uscite.
- `nixos`: due goal in tensione — un sistema snello, semplice e minimalista, e insieme un'alta affidabilità (host Svezia e Norvegia intercambiabili, replicabilità) che richiede ridondanza. L'artefatto bilancia il «meno» del minimalismo col «di più» della resilienza.
- `bi`: propagare ai plugin degli e-commerce gli aggiornamenti di disponibilità e prezzo dell'intero catalogo, e facilitare la gestione del catalogo prodotti.

I quattro mostrano lo spettro di delegabilità: `bi` e `nixos` hanno goal in larga parte codificabili (autonomia alta), `salute` ed `economia` hanno goal radicati in motivi personali non esternalizzabili (supervisione permanente).

## Il Goal come polo simmetrico al Mondo

Il Goal e il Mondo sono i due confini del ciclo. Se il Mondo è il confine inferiore — la realtà esterna che l'artefatto non controlla e che gli risponde da sé — il Goal è il confine superiore: il motivo che viene da sopra, dalla vita o dal committente, e che l'artefatto non genera. I due poli sono simmetrici nell'essere entrambi fuori dal controllo dell'artefatto, che si limita a mediare tra un motivo che riceve e un mondo che gli risponde. Per questo, come al Mondo si toccano i due versi della cerniera inferiore — o3 esce verso il mondo, i1 entra dal mondo — al Goal si toccano i due versi di quella superiore: il piano (o1) scende dal goal declinandosi in task, e il verdetto (i3) risale confrontando l'esito con il goal e formando il goal successivo.

La simmetria è più piena di quanto sembri: entrambe le cerniere sono scrivi-poi-leggi attraverso un medium persistente. Al Mondo o3 scrive un effetto e i1 lo rilegge più tardi — il mondo trattiene lo stato; al Goal i3 scrive l'esito nella KB e il goal successivo lo legge. L'unica vera asimmetria non è tra le due cerniere ma tra i due medium: il mondo persiste da solo, la KB persiste solo se qualcuno la scrive (cfr. `ciclo-azione`, `system-image`). Da qui il principio gemello di quello del Mondo — un confronto che non si scrive nella KB è un task perso — e la ragione per cui la KB ha bisogno di un custode.

Qui il ciclo si chiude e si riapre. Il goal si declina in task — la coda operativa che lo realizza — ma i task non vivono in questo nodo né in `metodo`: vivono in `plan.md` e `tasks/` di ciascun artefatto, perché sono operativi e volatili. Ciò che è stabile, e quindi metodologico, è dove avviene il confronto da cui i task nascono: la sintesi dello stato corrente che l'i3 mette a paragone con il goal. Per artefatto:

- `economia`: la fotografia dello stato (`stato.md`, scadenze) confrontata con gli obiettivi fa emergere gli scostamenti, e da lì i nuovi task.
- `salute`: il quadro corporeo con i suoi semafori rende visibili i disequilibri rispetto all'equilibrio corpo-mente; ogni banda gialla o rossa pianifica i task di riequilibrio.
- `bi`: lo scostamento tra il catalogo pubblicato e i dati di fornitori e Danea genera i task di riallineamento.
- `nixos`: lo stato del sistema — lentezze, appesantimenti, deriva dal minimalismo — confrontato col goal di snellezza genera i task di pulizia.

Lo stesso lavoro può nascere anche dall'altro polo: al Mondo un i1 esogeno apre un goal nuovo per triage, senza un confronto che lo precede (cfr. «Formazione del Goal dai due archi» e `world`). I due poli sono dunque le due sorgenti del lavoro: il Goal lo rigenera chiudendo loop noti, il Mondo lo apre con segnali inattesi.

## Riferimenti

- Alexei Leontiev, _Activity, Consciousness, and Personality_ (1978) — gerarchia attività/azione/operazione; fonte primaria non disponibile in `sources/`.
- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition (2013), Cap. 2 — il Goal come apice del ciclo a sette stadi; cfr. `ciclo-azione`.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [input](input.md)
- [world](world.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [sistema-cognitivo](sistema-cognitivo.md)
- [artefatto-cognitivo](artefatto-cognitivo.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [metodo-kb](metodo-kb.md)
