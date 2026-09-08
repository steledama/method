---
stato: maturo
---

# Constraint

Una limitazione progettata che riduce le azioni possibili a quelle valide.
Norman lo elenca tra i meccanismi con cui il design risponde alle domande
dell'utente — accanto a mapping, significanti, modelli concettuali, feedback e
visibilità — ed è ciò che nei progetti si chiama spesso _guardrail_. La sua
forza sta nel livello a cui opera: dove un check riflessivo (ricordarsi di fare
X) può saltare, il vincolo rende l'azione sbagliata impossibile, oppure
rumorosa. Un vincolo automatico riduce la dipendenza dall'attenzione; una
convenzione culturale o semantica richiede invece di essere compresa e seguita.

Norman distingue quattro tipi. I vincoli _fisici_ limitano per geometria (un
pezzo entra in un solo verso). I _culturali_ poggiano su convenzioni condivise.
I _semantici_ derivano dal significato della situazione. I _logici_ escludono
per deduzione le alternative impossibili. Le _forcing function_ sono il caso
forte: impediscono di proseguire finché un passo necessario non è compiuto.

Nel metodo il vincolo è un componente che si _progetta e si costruisce_; la sua
efficacia è anche un criterio di revisione della superficie. Le sue incarnazioni
ricorrono cross-progetto: i guardrail sulla freschezza degli input; la
configurazione dichiarativa che rende irrappresentabili gli stati invalidi; gli
schemi e i test che rifiutano dati malformati; il generatore di una vista che
rompe la build quando le fonti da cui deriva si contraddicono (`view`). Un audit
che emette un report segnala il problema, ma non impedisce da solo di
committare. Il gate operativo deve far usare quel segnale; la revisione
semantica richiede inoltre un giudizio che lo script non può sostituire.

Un vincolo installato in un artefatto che ha già storia paga anche all'indietro:
al primo giro non previene, **rivela** — fa emergere in un colpo il drift
accumulato nel tempo in cui non c'era. Il costo evitato resta una valutazione
delle conseguenze, non si deduce dall'età del difetto. Portare un vincolo in un
progetto esistente è quindi un atto diagnostico oltre che di allineamento, e il
lavoro che ne esce non è lavoro nuovo creato dal vincolo: è lavoro dovuto che
diventa esigibile.

Un vincolo automatico presidia l'errore anche quando manca l'attenzione. Nel
metodo, trasformare un «ricordarsi di» in una condizione controllata dalla
macchina riduce la dipendenza dal ricordo; questa forza non va attribuita
indistintamente a ogni convenzione o revisione umana. Se una sorgente rinominata
può lasciare una copia servita divergente, il rapporto va reso meccanico con un
unico path, un test che fallisce o uno schema. Dove un errore conta, non
affidarsi alla memoria di un agente: costruire il vincolo che lo rende
impossibile o rumoroso.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition
  (2013), Cap. 4 «Knowing What to Do: Constraints, Discoverability, and
  Feedback» — tipi di vincolo e forcing function. Provenienza e limite della
  copia locale nel register `world.md`; l'indice pubblicato dall'autore conferma
  l'articolazione del capitolo, non sostituisce il testo completo.
- Donald Norman, «Affordance, Conventions and Design (Part 2)», JND.org, 2008 —
  testo d'autore che distingue vincoli fisici da vincoli logici e culturali, che
  possono essere ignorati o violati.

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [action-cycle](action-cycle.md)
- [processing-layers](processing-layers.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [system-image](system-image.md)
- [view](view.md)
