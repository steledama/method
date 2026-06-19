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
runtime. Risalire da un output runtime al task che l'ha generato — output,
codice, commit, task, goal — non è debug ma attraversamento di questa sutura.

## Due Mondi, due poli

Poiché i due cicli hanno Mondi distinti, hanno poli distinti: non un Goal e un
Mondo soli, ma una coppia per ciclo. Per un artefatto come `method`, il cui
dominio è il metodo stesso, i due Mondi sono leggibili a colpo d'occhio nelle
collezioni dell'atrio. Il ciclo di sviluppo abita i file-ciclo e le collezioni
interne — il piano, i task, il verdetto, le interpretazioni — perché il suo
Mondo sono i nodi e la loro coerenza. Il ciclo runtime abita invece le collezioni
rivolte fuori — i segnali che emergono dagli adottanti (i1) e i runbook di
adozione del canone (o3) — perché il suo Mondo sono i progetti adottanti. Le due
collezioni rivolte fuori non sono un'eccezione tassonomica: sono il ciclo
runtime, separato fisicamente ma non ancora etichettato come tale.

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
- [world](world.md)
- [goal](goal.md)
- [perform](perform.md)
- [perceive](perceive.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [adopter-comparison](adopter-comparison.md)
