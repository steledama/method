---
data: 2026-06-17
stato: bozza
---

# Nested cycles

Il ciclo d'azione che il metodo eredita da Norman non è uno solo: sono due, e il
secondo è annidato nel primo. Ciascuno è lo specchio simmetrico a sei atti e due
poli descritto in `action-cycle`; i due si distinguono unicamente per _cosa sia
il loro Mondo_ in fondo. Norman descrive un utente che agisce su un artefatto e
ne valuta la risposta, ma tace su una cosa: quando l'artefatto è esso stesso
costruito, è il prodotto di un ciclo d'azione precedente. Il metodo apre quella
scatola nera, e l'apertura è questo nodo.

L'annidamento ha un antenato preciso, del 1962: il **bootstrap** di Engelbart —
«Tools Developed vs Tools Used» (§IV-E di _Augmenting Human Intellect_) — il
sistema di augmentation che applica i propri means a migliorare sé stesso, e si
solleva «by its own bootstraps» (cfr. `augmentation-system`). La distinzione
engelbartiana tra ciò che il sistema _sviluppa_ e ciò che _usa_ è la stessa che
qui separa il ciclo di sviluppo dal runtime, e porta con sé lo stesso
avvertimento sulla confusione dei due termini, guardia contro l'affiancamento.

Il ciclo **runtime** ha per Mondo la realtà: o3 prescrive un'email, una
transazione, una pubblicazione o un gesto, l'atto accade nella membrana `world`,
i1 ne cattura il segnale quando serve. Il ciclo di **sviluppo** ha per Mondo
l'artefatto stesso: o3 prescrive la modifica, il commit agisce sull'artefatto,
i1 cattura lint, audit, test o errore. Per questo gli atti si _raddoppiano_: ogni
ciclo possiede le proprie prescrizioni e catture attorno al proprio Mondo, e un
elemento del metodo non è collocato finché non se ne dichiara anche
l'annidamento — è la seconda delle quattro dimensioni ortogonali di
`action-cycle`, quella la cui omissione aveva fatto «sparire» o1.

## La cucitura, non l'affiancamento

I due cicli non sono paralleli, sono annidati, e confonderli è l'errore da cui
questo nodo guarda. La giunzione è precisa: **il Mondo del ciclo di sviluppo è
la macchina che esegue il ciclo runtime**. Il commit non _è_ la macchina: è
l'atto o3-sviluppo che modifica l'artefatto; la macchina è l'artefatto
risultante, cioè il Mondo-dev su cui quel ciclo agisce. I due cicli condividono
dunque una sutura reale, non un bordo adiacente: il fondo dell'uno è il motore
dell'altro.

Ne segue una conseguenza per ogni rappresentazione, testuale o visiva: mostrare
i due cicli come due stati alla pari — due colonne, due schede commutabili —
appiattisce l'annidamento in parallelismo e perde proprio ciò che il metodo
aggiunge a Norman. Una rappresentazione fedele deve rendere visibile la
cucitura: il Mondo-dev/artefatto che, una volta costruito, diventa macchina del
runtime.

## I due versi della stessa sutura

La stessa cucitura si legge da due capi, ed entrambe le letture sono vere; il
nodo le tiene esplicite perché chi confronta la prosa con il disegno non le
scambi per una contraddizione.

Il **verso di provenienza** è quello con cui l'annidamento si scopre, ed è la
mossa di Norman estesa: si parte dall'artefatto _in opera_ — il ciclo runtime che
agisce sul dominio — si apre la scatola nera, e dentro si trova il ciclo di
sviluppo che quell'artefatto l'ha prodotto. Il dev è «dentro» come origine e
storia. Risalire da un output runtime al task che l'ha generato — output, codice,
commit, task, goal — non è debug ma attraversamento della sutura in questo verso.

Il **verso operativo** è quello con cui l'annidamento si rappresenta, ed è il
verso del diagramma. Il ciclo di sviluppo è il loop _esterno_ che costruisce
l'artefatto; l'artefatto, una volta costruito e messo in opera, è la macchina che
_contiene_ ed esegue il ciclo runtime. Il dev è «fuori e sopra» come costruzione
che racchiude; il runtime è «dentro» l'artefatto.

Non sono due modelli in competizione, ma la stessa sutura vista dai due capi: il
fondo del ciclo di sviluppo (l'artefatto = World-dev) è il motore del ciclo
runtime. La prosa di questo nodo narra spesso il verso di provenienza — è come il
metodo è arrivato all'annidamento; il diagramma rende il verso operativo — è come
l'annidamento opera.

## Annidamento per contenimento: quattro poli e un gradiente di portabilità

Poiché i due cicli hanno Mondi distinti, hanno poli distinti: non un Goal e un
Mondo soli, ma **quattro poli** — Goal-dev, Artefatto, Goal-runtime,
World-runtime — disposti non come due colonne alla pari ma per **contenimento**.

In cima sta il **Goal-dev**, ed è universale: non contenuto di dominio, ma la
posizione auspicata dell'artefatto lungo dimensioni comuni a tutti gli artefatti
— attrito, autonomia, temporalità — calibrate per dominio e non ridefinite
(`development-goal`). Poiché il Mondo-dev è la macchina del runtime, quelle
dimensioni sono desiderata sulla forma del runtime.

Sotto il Goal-dev corre il ciclo di sviluppo a sei stadi (esecuzione ‖
valutazione), il cui fondo è l'**Artefatto = World-dev**: il polo che è insieme il
Mondo su cui il dev agisce e il **contenitore** del ciclo runtime. È la cucitura
resa polo. Dentro l'artefatto vive il ciclo runtime, anch'esso a sei stadi, con il
proprio **Goal-runtime**, lo scopo di dominio — forma e scopo restano distinti dal
Goal-dev, il contenimento li mette su altitudini diverse senza fonderli
(`development-goal`).

Il quarto polo, il **World-runtime**, non sta chiuso nell'artefatto: **sporge**.
Il dominio — le mail, le transazioni, il patrimonio, il corpo — non è contenuto
dall'artefatto; l'artefatto ci _agisce sopra_. Nel disegno il World-runtime esce
dal fondo della scatola: l'artefatto è la macchina, il dominio è la realtà fuori
su cui la macchina opera attraverso la membrana `world`.

Questa disposizione fa emergere un **gradiente di portabilità verticale**: in cima
il Goal-dev è la parte comune a tutti i domini; scendendo verso il World-runtime
si diventa progressivamente domain-specifici. È ciò che la rappresentazione a due
colonne alla pari nascondeva.

Per un artefatto come `method`, il cui dominio è il metodo stesso, i due Mondi
sono leggibili a colpo d'occhio nelle collezioni dell'atrio. Il ciclo di sviluppo
abita i file-ciclo e le collezioni interne — il piano, i task, il verdetto, le
interpretazioni — perché il suo Mondo sono i nodi e la loro coerenza. Il ciclo
runtime abita invece le collezioni rivolte fuori — i segnali che emergono dagli
adottanti (i1) e i runbook di adozione del canone (o3) — perché il suo Mondo sono
i progetti adottanti. Le due collezioni rivolte fuori non sono un'eccezione
tassonomica: sono il ciclo runtime, separato fisicamente ma non ancora etichettato
come tale.

## L'agente è un asse ortogonale all'annidamento

Una tentazione ricorrente è leggere i due cicli come «uno umano, uno IA»: l'umano
sviluppa, l'IA esegue. È falso e va respinto. **Entrambi** i cicli sono percorsi
da umano + LLM insieme — il ciclo di sviluppo lo percorriamo in due proprio
adesso. Ciò che cambia tra i due non è _quale_ agente, ma il **mix**: il peso
umano è alto nel dev e scivola verso l'LLM nel runtime, con l'umano che passa da
_in-the-loop_ (interviene a ogni stadio) a _on-the-loop_ (sorveglia e interviene
per eccezione). È un gradiente, non un interruttore.

Quella posizione — quanto in alto tenere l'umano nel loop — non è una proprietà
dell'annidamento: è essa stessa una **dimensione del Goal-dev**, l'autonomia
auspicata dell'artefatto (`development-goal`). Agente e annidamento stanno dunque
su **assi ortogonali**: il diagramma può suggerire il mix — una velatura,
un'etichetta — ma non deve collassarlo nell'annidamento. Collassarli è lo stesso
errore che aveva fatto «sparire» o1, proiettare due dimensioni indipendenti su una
sola (cfr. `action-cycle`, le quattro dimensioni ortogonali; e in `verdict.md` il
filo di de-cablaggio del binomio «due agenti»).

## I sei stadi sono punti di controllo e di rientro

Ogni ciclo è lo specchio a sei atti di `action-cycle`, e i sei stadi vanno resi
**visibili e osservabili in entrambi** i cicli — non per completezza estetica, ma
perché ogni stadio reso esplicito è due cose insieme: il punto in cui l'**umano
ispeziona e interviene**, e il punto in cui l'**LLM rientra nel loop senza
ricostruirlo** (`action-cycle`, §«Saltare uno stadio»). Un ciclo mostrato come un
solo arco — o3 più il ritorno i1 — perde questi punti: collassa gli stadi e con
essi il controllo, per entrambi gli agenti e con frustrazione di tutti. È questa
la ragione anti-collasso che vieta sia la riduzione a un atto solo sia
l'affiancamento a due colonne mozzate.

## Perché non è solo di method

L'annidamento non è una peculiarità del meta-artefatto. Ogni progetto adottante
ha entrambi i cicli: uno sviluppo che costruisce la propria macchina — codice,
configurazione, KB — e un runtime in cui quella macchina agisce sul proprio
Mondo, sia esso un sistema da configurare, dati da sincronizzare, un patrimonio
da governare o una pratica da sostenere. La popolazione dei due cicli cambia da
dominio a dominio, e proprio quella differenza è materiale di confronto tra
adottanti: dove un ciclo è solido e dove è assente perché non serve. La verifica
sul campo dell'annidamento, artefatto per artefatto, è il compito di
`action-cycle-matrix`.

Connessioni:

- [action-cycle](action-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [augmentation-system](augmentation-system.md)
- [world](world.md)
- [goal](goal.md)
- [development-goal](development-goal.md)
- [perform](perform.md)
- [perceive](perceive.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [adopter-comparison](adopter-comparison.md)
