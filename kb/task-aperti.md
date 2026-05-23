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
