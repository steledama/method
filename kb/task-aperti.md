---
data: 2026-05-23
stato: bozza
---

# Task aperti

I task aperti sono la parte del README che risponde alla domanda: cosa dobbiamo fare adesso? Sono la supervisione corrente del lavoro futuro, ordinata per priorità e collegata ai dettagli operativi quando servono.

La tabella dei task aperti non è storico e non è backlog infinito. Deve rappresentare il lavoro ancora vivo. Quando un task viene completato, la riga sparisce; la storia resta in git, log.md e nei nodi aggiornati.

Regole:

- vive nel README come vista sintetica e supervisionabile
- ogni task sostanziale può avere un file in todo/
- ogni file in todo/ deve avere una riga corrispondente nel README
- priorità e dipendenze devono essere esplicite
- i task completati vanno rimossi, non archiviati in todo/
- i task locali restano nel repo locale, non nel repo metodo
- i task del repo `metodo` riguardano solo il metodo stesso: ristrutturazione,
  semplificazione, coerenza dei nodi, strumenti portabili già giustificati o
  generalizzazioni emerse dai repo adottanti
- le verifiche operative su un repo adottante restano nel repo adottante, anche
  quando possono produrre filing back metodologico

I task sono parte strutturale del metodo perché le sessioni LLM pianificano, analizzano e implementano lavoro attraverso task espliciti. Se i task driftano, la sessione parte da una supervisione falsa: priorità, dipendenze e prossimo lavoro non rappresentano più lo stato reale del progetto.

La revisione dei task aperti va fatta come controllo leggero a inizio sessione e come controllo completo quando cambiano fatti, scadenze o dipendenze. Nei progetti adottanti questa funzione è codificata nella skill base `revisione-tasks`, che deve verificare drift README/todo, task superati, nuovi task emersi dai fatti, priorità aggiornate e task consigliato per la sessione corrente.

## Sviluppo bottom-up del metodo

Lo sviluppo del metodo parte dai repo adottanti. Un task nasce dove esiste il problema concreto, con le fonti, le dipendenze e i criteri di chiusura del dominio. Se durante quel lavoro emerge una regola generale, il filing back aggiorna `metodo`; il task però resta locale finché richiede evidenza locale.

Il repo `metodo` non è una backlog board per i progetti adottanti. Non deve contenere task del tipo "controlla X in repo Y" o "applica Y al repo Z". Questi task hanno senso solo nel repo che deve produrre l'evidenza. `metodo` riceve il risultato quando diventa principio, nodo, skill base, strumento comune o criterio di revisione.

Una sessione dentro un repo adottante deve quindi controllare la coda locale e, se necessario, la storia recente di `metodo` per vedere quali generalizzazioni sono state introdotte. La propagazione avviene tramite commit del metodo letti e applicati localmente, non tramite task centrali che dirigono i repo adottanti.

Nel repo `metodo` i task dovrebbero essere rari. Sono legittimi quando riguardano questo repo direttamente: riorganizzare la presentazione, semplificare nodi, formalizzare una regola già emersa, aggiornare strumenti portabili o correggere incoerenze interne. Se un task richiede uso reale di un repo adottante, va spostato lì.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                       | Confronto con il metodo                                                                                                        |
| ---------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `nixos`    | coda piccola, tabella README compatta.                                                  | Molto aderente: pochi task vivi, legati a cambi tecnici concreti.                                                              |
| `bi`       | coda media, tabella README con priorità e dipendenze.                                   | Adeguato alla complessità del dominio; i task sono spesso strutturali e vanno tenuti distinti dai nodi stabili.                |
| `economia` | coda ampia legata a scadenze, adempimenti e situazioni aperte.                          | La numerosità è legittima perché il dominio è operativo e calendariale; serve però revisione frequente per evitare task morti. |
| `salute`   | coda media; il README contiene anche task senza file per elaborazione fonti.            | Adattamento accettabile per ingest semplici, ma i task più sostanziali dovrebbero avere contesto in `todo/`.                   |

Il metodo deve ammettere granularità diverse. Nei domini tecnici il task tende a essere un intervento verificabile; in `economia` può essere una pratica aperta; in `salute` può essere ingest o sviluppo concettuale. La regola comune resta la stessa: ciò che è futuro e operativo non deve diventare nodo permanente.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [todo](todo.md)
- [log](log.md)
- [git-history](git-history.md)
