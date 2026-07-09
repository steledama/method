---
stato: bozza
---

# Processing layers

Modello di Donald Norman (con Andrew Ortony e William Revelle) che distingue tre livelli di elaborazione del cervello, ciascuno con un ruolo diverso e — per il design — un proprio stile. È il contributo di _Emotional Design_, dove Norman corregge la tesi di _The Design of Everyday Things_: l'usabilità non basta, perché «the emotional side of design may be more critical to a product's success than its practical elements». Per il metodo il livello che conta è il _reflective_: la KB è un artefatto riflessivo, il luogo dove l'esperienza diventa generalizzazione, e i tre livelli danno il vocabolario per capire perché il sapere riflessivo non agisce da solo e ha bisogno dello strato output per raggiungere l'azione. «La KB è riflessiva» vale però _in questo frame_ (i tre livelli di elaborazione); il system image è invece l'intero artefatto, trasversale ai livelli e non uno stadio, di cui la KB è il nucleo formalizzato — cfr. `system-image` e, sotto, «I tre livelli e l'altezza del ciclo».

I tre livelli non nascono dal nulla in _Emotional Design_: **articolano i due modi** che Norman aveva tracciato in _Things That Make Us Smart_ (1993) — la cognizione esperienziale e quella riflessiva (cfr. `cognitive-artifact`). Il riflessivo resta; l'esperienziale, il modo percettivo-diretto, si sdoppia nel _visceral_ (giudizio affettivo immediato) e nel _behavioral_ (operazione esperta di routine). Riconoscere la genealogia tiene coerenti i due nodi: lo stesso Norman, undici anni dopo, raffina due modi in tre livelli.

Il nome del nodo usa _layers_ per restare vicino alla stratificazione di Norman
e risuonare con gli strati input/output del metodo, evitando l'omonimia con i
_levels of processing_ di Craik e Lockhart.

I tre livelli, nelle parole di Norman: «the automatic, prewired layer, called the visceral level; the part that contains the brain processes that control everyday behavior, known as the behavioral level; and the contemplative part of the brain, or the reflective level». Si intrecciano in ogni design — «It is not possible to have design without all three» — e, cosa importante, «these three components interweave both emotions and cognition»: emozione e cognizione non sono opposte, sono inseparabili.

## I tre livelli

Il _visceral_ è veloce e biologico: «it makes rapid judgments of what is good or bad, safe or dangerous», invia segnali ai muscoli, è l'inizio dell'elaborazione affettiva. È il livello delle reazioni immediate — la lucertola opera quasi solo qui.

Il _behavioral_ è la sede della maggior parte del comportamento umano. Non è conscio — «you can successfully drive your automobile subconsciously at the behavioral level while consciously thinking of something else at the reflective level» — ed è dove eccelle l'esperto in operazioni ben apprese e di routine. Può essere potenziato o inibito dal riflessivo, e a sua volta potenzia o inibisce il viscerale.

Il _reflective_ è il più alto: «the home of reflection, of conscious thought, of the learning of new concepts and generalizations about the world». Il dettaglio decisivo per il metodo: «it does not have direct access either to sensory input or to the control of behavior. Instead it watches over, reflects upon, and tries to bias the behavioral level». Il livello riflessivo non sente e non agisce direttamente: osserva e cerca di condizionare l'azione altrui.

## I tre tipi di design

A ogni livello corrisponde uno stile di design. Il _visceral design_ «concerns itself with appearances». Il _behavioral design_ «has to do with the pleasure and effectiveness of use». Il _reflective design_ «considers the rationalization and intellectualization of a product. Can I tell a story about it? Does it appeal to my self-image, to my pride?». L'esempio dei livelli in azione: il roller coaster oppone «one level of affect—the visceral sense of fear—against another level—the reflective pride of accomplishment».

## Perché conta per il metodo

La KB è la materializzazione del livello riflessivo — _in quanto livello di elaborazione_. Il riflessivo, in Norman, è «the learning of new concepts and generalizations about the world»: è la definizione di ciò che la KB accumula. Il _system image_, però, è l'intero artefatto, trasversale ai tre livelli — il substrato che l'intero ciclo legge e scrive, non uno stadio (cfr. `system-image`); la KB ne è il nucleo formalizzato, e le due letture convivono. E il suo esempio canonico è il filing back del metodo, parola per parola. Camminiamo attorno a una staccionata per raggiungere il cibo (esecuzione, behavioral); poi «we can then think back about the experience—reflect upon it—and decide to move the fence or the food, so we don't have to walk around the next time. We can also tell other people about the problem, so they will know what to do even before they get there». Riflettere sull'esito, cambiare il sistema, comunicarlo a chi verrà: è il ciclo che si chiude nella KB, e il "tell other people" è la KB che serve gli altri agenti — l'umano nel tempo e l'LLM tra le sessioni.

Il limite del riflessivo spiega perché lo strato output esiste. Il riflessivo «does not have direct access to the control of behavior»: il sapere nella KB non può agire nel mondo, può solo _condizionare_ l'azione che avviene al livello behavioral. È il gulf of execution detto in termini neuropsicologici — la distanza tra il livello che sa e il livello che fa. I signifier dello strato output sono ciò che permette al livello riflessivo di raggiungere quello behavioral; senza, il sapere resta contemplazione che non muove nulla, ed è di nuovo la provocazione del ciclo di azione (se l'utente non agisce, la KB è mal progettata). Specularmente, delegare il livello behavioral all'agente macchina — l'LLM che esegue operazioni di routine "subconsciamente", come si guida mentre si pensa ad altro — mentre l'umano trattiene il livello riflessivo di supervisione è la forma cognitiva del gradiente di autonomia.

C'è infine il contributo proprio di questa fonte, che le altre due non danno: la dimensione _affettiva_. Norman insiste che emozione e cognizione si intrecciano. Il rapporto dell'umano con la propria KB non è solo strumentale — c'è orgoglio, possesso, la storia che il repo racconta (reflective design: «Can I tell a story about it? Does it appeal to my self-image, to my pride?»). Non è decorazione: è parte di ciò che tiene l'umano dentro il loop quando il livello behavioral è ormai delegato alla macchina.

## I tre livelli e l'altezza del ciclo

I tre livelli stratificano il ciclo di azione per altezza, e la corrispondenza
non è forzata: viene dalla definizione stessa di Norman. Il _visceral_ «makes
rapid judgments of what is good or bad… and sends signals to the muscles» —
giudizio sensoriale rapido più output motorio — è la cerniera bassa nel suo
insieme. `world` contiene il segnale grezzo e l'atto; `i1/` e `o3/` ne sono i riflessi
versionati, rispettivamente cattura del Perceive e prescrizione del Perform. o3
non è dunque il gesto motorio: lo prepara dal lato dell'artefatto. Il
_reflective_ «watches over, reflects upon, and tries to bias the behavioral
level», senza accesso diretto a senso e azione: è la triade alta — Compare,
Goal, Plan. La KB **non coincide** con questa triade: la triade sono gli _stadi_
riflessivi, la KB è la loro regione formalizzata. Il _substrato_ che tutti gli
stadi leggono e scrivono — i1 lo alimenta, o2 ne attinge — è invece il system
image, cioè l'intero artefatto. La KB materializza il riflessivo come livello ed è
il nucleo formalizzato del system image, che è trasversale (cfr. `system-image`). Il _behavioral_, sede dell'operazione esperta e di
routine, è la vita del ciclo: Specify (o2) e Interpret (i2). La stratificazione
si appoggia al «6 atti + 2 poli» di `action-cycle`.

Resta il monito di Norman: «it is not possible to have design without all three», i livelli si intrecciano. È una stratificazione di _enfasi_, non una partizione: nessun atto è puramente un livello.

La conseguenza di progetto è netta e spiega le stasi. Il riflessivo non agisce: può solo _condizionare_ il behavioral, e solo attraverso l'output. Ma per muovere davvero il behavioral, l'o2 deve raggiungere anche il _visceral_ — l'apparenza, l'impatto immediato, l'affetto. Un o2 solo riflessivo (testo, schemi analitici) parla alla parte che già sa e non muove la parte che fa: è la diagnosi della stasi di `salute`, una KB riflessiva ricca la cui rappresentazione non scende al viscerale e quindi non genera azione. «Attractive things work better» non è estetica: è la condizione perché il sapere attraversi i tre livelli fino al gesto. Da qui un criterio per lo strato output: ogni o2 va valutato su tutti e tre i registri, e quello sistematicamente mancante negli artefatti è il viscerale (cfr. `matrice-action-cycle`, dove la colonna o2 è debole in quattro artefatti su cinque).

## I tre specchi sono i tre livelli

I due archi del ciclo sono speculari e accoppiati per altitudine (cfr. `action-cycle`, `input`, `output`): ogni coppia output↔input cade su uno dei tre livelli. **o3↔i1** (`perform`↔`perceive`) è la coppia _viscerale_, alla membrana `world`: prescrizione dell'atto e cattura del segnale, i due riflessi versionati del gesto e della percezione. **o2↔i2** (`specify`↔`interpret`) è la coppia _behavioral_, la vita del ciclo: una superficie di decisione prodotta come o2 e riletta come substrato d'interpretazione in `i2/`. **o1↔i3** (`plan`↔`compare`) è la coppia _riflessiva_, alla KB: piano strutturato e conoscenza formalizzata. Dei tre specchi solo **o2↔i2** ha oggi una materializzazione attiva — la vista Interpretazioni, l'unica superficie che il metodo produce e rilegge nello stesso artefatto (cfr. `view`); gli altri due restano specchi concettuali finché un artefatto non li rende letterali.

La specularità si legge anche per **funzione**, non solo per altitudine — è la formula emersa nella sintesi i2: l'atto di input **rivela**, l'atto di output **risolve**. Al behavioral le interpretazioni (i2) rivelano le tensioni e i compiti (o2) le risolvono; al riflessivo i confronti (i3) rivelano tensioni, priorità e drift e i piani (o1) risolvono orientando il lavoro futuro. Alla coppia viscerale la formula si attenua in cattura e preparazione — i1 cattura il segnale, o3 prepara l'atto — perché alla membrana non c'è ancora significato da rivelare né soluzione da scegliere.

## Riferimenti

- Donald Norman, _Emotional Design: Why We Love (or Hate) Everyday Things_ (Basic Books, 2004), Prologo "Three Teapots" e Cap. 1 "Attractive Things Work Better". Il modello dei tre livelli è di Norman con Andrew Ortony e William Revelle (cfr. Figura 1.1, "Three levels of processing").
- Donald Norman, _Things That Make Us Smart_ (Addison-Wesley, 1993), Cap. 2 «Experiential and Reflective Cognition» — i due modi da cui i tre livelli del 2004 derivano (cfr. `cognitive-artifact`).
- Fonte grezza (`gdrive/`, su Drive): PDF, provenienza nel register `world.md` (sezione fonti).

Connessioni:

- [action-cycle](action-cycle.md)
- [system-image](system-image.md)
- [affordance-signifier](affordance-signifier.md)
- [knowledge-base](knowledge-base.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [world](world.md)
- [input](input.md)
- [output](output.md)
