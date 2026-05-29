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
- i task metodologici cross-repo restano nel repo metodo, anche quando
  richiedono verifiche o interventi puntuali in un repo adottante

I task sono parte strutturale del metodo perché le sessioni LLM pianificano, analizzano e implementano lavoro attraverso task espliciti. Se i task driftano, la sessione parte da una supervisione falsa: priorità, dipendenze e prossimo lavoro non rappresentano più lo stato reale del progetto.

La revisione dei task aperti va fatta come controllo leggero a inizio sessione e come controllo completo quando cambiano fatti, scadenze o dipendenze. Nei progetti con una skill dedicata, la skill deve verificare drift README/todo, task superati, nuovi task emersi dai fatti, priorità aggiornate e task consigliato per la sessione corrente.

## Governance cross-repo

I task metodologici vivono nel repo `metodo` e di norma hanno precedenza sui task di progetto. La regola vale anche quando l'implementazione e puntuale su un singolo repository: se il motivo del lavoro e metodologico, la fonte di verita del task resta in `metodo/todo/`.

Quando una sessione parte dentro un repo adottante, il bootstrap deve controllare due code: i task locali del repo e i task metodologici centrali che targettano quel repo. La priorita finale nasce dal confronto tra urgenza metodologica e urgenza di dominio, ma il task metodologico non va copiato nel README locale solo per renderlo visibile.

Un repo adottante riceve un task locale solo quando il lavoro e diventato un intervento autonomo di progetto, con esecuzione e priorita proprie del dominio. La soglia pratica e: metodologico per origine e criterio -> `metodo`; locale per esecuzione autonoma e dominio -> repo specifico.

I task metodologici che riguardano piu progetti devono essere scritti come task centrali con sezioni o tabelle per repository target. Questo mantiene una vista globale delle priorita senza duplicare lo stesso task nei README locali.

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | 4 task in `todo/`, tabella README compatta. | Molto aderente: pochi task vivi, legati a cambi tecnici concreti. |
| `bi` | 11 task in `todo/`, tabella README con priorità e dipendenze. | Adeguato alla complessità del dominio; i task sono spesso strutturali e vanno tenuti distinti dai nodi stabili. |
| `economia` | 16 file in `todo/` e task README legati a scadenze, adempimenti e situazioni aperte. | La numerosità è legittima perché il dominio è operativo e calendariale; serve però revisione frequente per evitare task morti. |
| `salute` | 4 file in `todo/`, ma il README contiene anche task senza file per elaborazione fonti. | Adattamento accettabile per ingest semplici, ma i task più sostanziali dovrebbero avere contesto in `todo/`. |

Il metodo deve ammettere granularità diverse. Nei domini tecnici il task tende a essere un intervento verificabile; in `economia` può essere una pratica aperta; in `salute` può essere ingest o sviluppo concettuale. La regola comune resta la stessa: ciò che è futuro e operativo non deve diventare nodo permanente.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [todo](todo.md)
- [log](log.md)
- [git-history](git-history.md)
