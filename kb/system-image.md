---
stato: bozza
---

# System image

Concetto di Donald Norman per spiegare come la comprensione di un sistema si forma a distanza, senza che chi l'ha progettato e chi lo usa possano parlarsi. Il _system image_ è «the combined information available to us» — tutto ciò che la struttura costruita lascia percepire: forma, comportamento, documentazione, signifier. È il vertice che porta l'intero peso della comunicazione tra due menti che non si incontrano. Per il metodo è il concetto cardine dello strato condiviso: l'**artefatto** _è_ il system image attraverso cui due agenti — l'umano nel tempo e l'LLM tra le sessioni — formano la propria comprensione del lavoro, perché non hanno altro canale; la KB ne è il nucleo di conoscenza formalizzata, non il sinonimo.

Norman costruisce il concetto su due strati. Un _conceptual model_ è «an explanation, usually highly simplified, of how something works. It doesn't have to be complete or even accurate as long as it is useful» — le cartelle e le icone sullo schermo sono un modello concettuale efficace, anche se dentro il computer non esiste nessuna cartella. Un _mental model_ è il modello concettuale nella mente di chi usa: «the conceptual models in people's minds that represent their understanding of how things work». Persone diverse tengono modelli diversi dello stesso oggetto, e una stessa persona può tenerne più d'uno, anche in conflitto.

## Il triangolo: design model, system image, user's model

Norman dispone tre vertici. Il _design model_ è la concezione che il progettista ha del prodotto. Il prodotto, una volta costruito, è isolato da lui — sta sul bancone della cucina dell'utente. Il _system image_ è ciò che si può percepire dalla struttura fisica costruita, documentazione e signifier inclusi. Lo _user's model_ nasce dal system image, attraverso l'interazione con il prodotto.

La frase che regge tutto: «The designer expects the user's model to be identical to the design model, but because designers cannot communicate directly with users, the entire burden of communication is on the system image». Il progettista non può parlare all'utente; tutto ciò che voleva dire deve essere leggibile nell'artefatto. Quando il system image è incoerente, incompleto o contraddittorio, l'utente non riesce a usare il sistema. Da qui la conclusione di Norman: «Good conceptual models are the key to understandable, enjoyable products: good communication is the key to good conceptual models».

## Modelli semplificati e assunzioni

Un modello concettuale è utile proprio perché semplifica, ma la semplificazione ha una condizione di validità: «Simplified models are valuable only as long as the assumptions that support them hold true». L'esempio di Norman è il cloud — il modello "il documento è sul mio schermo" funziona finché la connessione regge; quando cade, il modello non sa più spiegare nulla. Un buon modello concettuale serve soprattutto «in figuring out what to do when things do not go as planned»: senza, si opera a memoria, alla cieca, e quando arriva la situazione nuova non si sa reagire.

È lo stesso meccanismo del guasto registrato nel ciclo di azione: un'assunzione che reggeva un comportamento ("presente nei backorders ⇒ fornitore esterno") smette di valere quando il modello dati cambia, ma niente costringe a riaprirla. Il presidio è formalizzare l'assunzione, non il solo comportamento — il check di fedeltà cognitiva. Il system image cattura _perché_ la formalizzazione va scritta nell'artefatto e non lasciata nella testa di chi decide: è l'unico canale che sopravvive a chi se ne va.

## Perché conta per il metodo

Nel metodo il system image è l'**intero artefatto** — README, `o1/plan.md`, `o2/`, `kb/`, le collezioni-stadio: tutto ciò che il repo presenta e che l'agente legge per costruirsi il modello. La KB ne è il nucleo di conoscenza formalizzata, non il sinonimo — appiattirlo sulla sola `kb/` spinge il system image verso il polo Goal (dove la KB sta) e perde il resto del medium. I due agenti che lo usano non possono comunicare direttamente: l'umano dimentica e cambia nel tempo, l'LLM riparte da zero a ogni sessione. Esattamente come tra progettista e utente di Norman, l'intero peso della comunicazione cade sull'artefatto — il repo. È la ragione testuale per cui l'artefatto deve essere autosufficiente nel bootstrap, per cui i fili `i3/` esistono (un'assunzione che vive solo in un messaggio di commit è fuori dal system image), e per cui una decisione non scritta è una decisione persa.

Da non confondere i due referenti. La **KB** è un _livello di elaborazione_ (cfr.
`processing-layers`): materializza il riflessivo — concetti e generalizzazioni —
e vive vicino al polo Goal, dove i2/i3 depositano. Il **system image** è invece
l'**intero artefatto**, **trasversale** ai tre livelli: non uno stadio del ciclo
ma il substrato che l'intero ciclo legge e scrive — i1 lo alimenta dal basso (in
`i1/`), o2 vi attinge per scendere fino al viscerale (in `o2/`), ogni
atto vi deposita o vi attinge un prodotto, sparso per l'atrio e non nella sola
`kb/`. La KB ne è il nucleo formalizzato, non il medium intero: chi le due cose le
collassa perde il canale che porta il peso della comunicazione a ogni altezza.

Da qui un'asimmetria che il metodo deve tenere esplicita. Il binomio umano + LLM è il caso saliente di una popolazione di agenti più ampia (cfr. `agent`): l'asimmetria che segue resta vera per questo caso, non come struttura unica. Norman dice che persone diverse formano mental model diversi dallo stesso oggetto: i due agenti lo fanno in modo radicalmente diverso. Per l'umano l'artefatto è impalcatura esterna a un modello che possiede già — un promemoria. Per l'LLM l'artefatto _è_ il mental model, non ne ha un altro: il system image e lo user's model coincidono. Questo cambia il criterio di progetto dello strato output: L1 (macchina) e L2 (umano) sono lo stesso system image reso ai due agenti, ma il primo deve essere completo perché è l'unica mente che il suo lettore avrà, il secondo può appoggiarsi a ciò che l'umano già sa. Il system image si costruisce dai signifier, dalle affordance, dai constraint e dai mapping: lo strato output è il lavoro di rendere quel system image leggibile a entrambi.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition (Basic Books, 2013), Cap. 1 "The Psychopathology of Everyday Things", sezioni _Conceptual Models_ e _The System Image_ (Figura 1.11, il triangolo design model / system image / user's model).
- Fonte grezza (`world`, su Drive): EPUB dell'edizione 2013; provenienza nel
  register `world.md` (sezione fonti).

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [action-cycle](action-cycle.md)
- [processing-layers](processing-layers.md)
- [knowledge-base](knowledge-base.md)
- [kb-content-typology](kb-content-typology.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [agent](agent.md)
