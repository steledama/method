---
stato: maturo
---

# System image

Concetto di Donald Norman per spiegare come la comprensione di un sistema si
forma a distanza, senza che chi l'ha progettato e chi lo usa possano parlarsi.
Il _system image_ comprende tutta l'informazione che la struttura costruita
lascia percepire: forma, comportamento, documentazione, signifier. È il vertice
che porta l'intero peso della comunicazione tra due menti che non si incontrano.
Per il metodo è il concetto cardine dello strato condiviso: l'**artefatto** _è_
il system image attraverso cui due agenti — l'umano nel tempo e l'LLM tra le
sessioni — formano la propria comprensione del lavoro, perché è il loro canale
persistente condiviso; la KB ne è il nucleo di conoscenza formalizzata, non il
sinonimo.

Norman costruisce il concetto su due strati. Un _conceptual model_ è una
spiegazione semplificata di come qualcosa funziona, utile senza doverne
riprodurre tutta la struttura — le cartelle e le icone sullo schermo sono un
modello efficace, anche se dentro il computer non esiste nessuna cartella. Un
_mental model_ è il modello concettuale nella mente di chi usa. Persone diverse
tengono modelli diversi dello stesso oggetto, e una stessa persona può tenerne
più d'uno, anche in conflitto.

## Il triangolo: design model, system image, user's model

Norman dispone tre vertici. Il _design model_ è la concezione che il progettista
ha del prodotto. Il prodotto, una volta costruito, è isolato da lui — sta sul
bancone della cucina dell'utente. Il _system image_ è ciò che si può percepire
dalla struttura fisica costruita, documentazione e signifier inclusi. Lo _user's
model_ nasce dal system image, attraverso l'interazione con il prodotto.

Il progettista vorrebbe che il modello dell'utente coincidesse col proprio, ma
non può comunicarglielo direttamente: l'intero peso della comunicazione cade sul
system image. Tutto ciò che voleva dire deve essere leggibile nell'artefatto.
Quando il system image è incoerente, incompleto o contraddittorio, l'utente non
riesce a usare il sistema. Buoni modelli concettuali dipendono quindi da una
buona comunicazione incorporata nel prodotto.

## Modelli semplificati e assunzioni

Un modello concettuale è utile proprio perché semplifica, ma soltanto finché
reggono le assunzioni che lo sostengono. L'esempio di Norman è il cloud — il
modello "il documento è sul mio schermo" funziona finché la connessione regge;
quando cade, il modello non sa più spiegare nulla. Un buon modello concettuale
serve soprattutto a capire cosa fare quando le cose non vanno come previsto:
senza, si opera a memoria, alla cieca, e quando arriva la situazione nuova non
si sa reagire.

Una regola di classificazione può smettere di valere quando cambiano i dati. Il
presidio consiste nel rendere esplicita l'assunzione che la sostiene e la
condizione che richiede di rivederla (`cognitive-fidelity`). Il lettore può così
capire se la regola sia ancora applicabile anche senza chi l'ha scritta.

## Perché conta per il metodo

Nel metodo il system image comprende l'intero artefatto: README, register,
collezioni del ciclo, KB e viste. La KB ne è il nucleo di conoscenza
formalizzata; non coincide con l'intero medium. I livelli di elaborazione di
`processing-layers` sono una lente sull'uso delle superfici, non una partizione
che confina il system image a una quota del ciclo.

Umano e LLM possono comunicare durante la sessione, ma la continuità del lavoro
non deve dipendere da quella conversazione. L'artefatto rende ricostruibili
assunzioni, contesto e ragioni delle decisioni. Git conserva anche messaggi e
razionali: non è estraneo al sistema, ma un motivo necessario al lavoro corrente
va esposto nei nodi o nei fili aperti, senza obbligare il lettore a ricostruirne
la storia.

La distinzione fra system image e modello del lettore vale per entrambi gli
agenti. L'LLM usa l'artefatto come principale contesto persistente del progetto,
integrandolo con richiesta, strumenti e segnali; l'umano vi aggiunge esperienza
e memoria personale (`cognitive-system`). Progettare rese adatte ai diversi
lettori significa rendere accessibile lo stesso contenuto senza presumere
identità dei modelli mentali o dei percorsi di comprensione.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition
  (Basic Books, 2013), Cap. 1 "The Psychopathology of Everyday Things", sezioni
  _Conceptual Models_ e _The System Image_ (Figura 1.11, il triangolo design
  model / system image / user's model).
- Provenienza nel register `world.md` (sezione fonti). L'EPUB usato per la
  distillazione non è osservabile nella superficie locale corrente: prima di
  usare le formulazioni verbatim va ripristinata una copia primaria leggibile.

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [cognitive-system](cognitive-system.md)
- [action-cycle](action-cycle.md)
- [processing-layers](processing-layers.md)
- [knowledge-base](knowledge-base.md)
- [kb-content-typology](kb-content-typology.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [agent](agent.md)
