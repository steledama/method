---
data: 2026-06-10
stato: bozza
---

# Plan

Il plan risponde alla domanda: cosa dobbiamo fare adesso? È la supervisione corrente del lavoro futuro, ordinata per priorità e collegata ai dettagli operativi quando servono. È lo **stadio Plan del ciclo di sviluppo**: la sua istanza è il file root `plan.md`, sollevato dall'altezza nel ciclo fuori dalla cartella `tasks/` — è la meta-istanza dei task, letta a ogni sessione, quindi sale in root anche se cambia in fretta (l'altezza vince sulla pace).

`plan` è il Plan dello _sviluppo_ (l'azione sull'artefatto), distinto da o1 (il Plan del _runtime_ in ciclo-azione, l'azione sul mondo): tenerli separati evita una contraddizione tra nodi.

Il plan non è storico e non è backlog infinito. Deve rappresentare il lavoro ancora vivo. Quando un task viene completato, la riga sparisce; la storia resta in git, `why.md` e nei nodi aggiornati.

Regole:

- vive in root come `plan.md`, vista sintetica e supervisionabile
- ogni task sostanziale può avere un file in `tasks/`
- ogni file in `tasks/` deve avere una riga corrispondente in `plan.md`
- priorità e dipendenze devono essere esplicite
- i task completati vanno rimossi, non archiviati in `tasks/`
- i task locali restano nel repo locale, non nel repo metodo
- i task del repo `metodo` riguardano solo il metodo stesso: ristrutturazione,
  semplificazione, coerenza dei nodi, strumenti portabili già giustificati o
  generalizzazioni emerse dai repo adottanti
- le verifiche operative su un repo adottante restano nel repo adottante, anche
  quando possono produrre filing back metodologico

I task sono parte strutturale del metodo perché le sessioni LLM pianificano, analizzano e implementano lavoro attraverso task espliciti. Se i task driftano, la sessione parte da una supervisione falsa: priorità, dipendenze e prossimo lavoro non rappresentano più lo stato reale del progetto.

La revisione del plan va fatta come controllo leggero a inizio sessione e come controllo completo quando cambiano fatti, scadenze o dipendenze. Nei progetti adottanti questa funzione è codificata nella skill base `tasks-review`, che deve verificare drift `plan`/`tasks`, task superati, nuovi task emersi dai fatti, priorità aggiornate e task consigliato per la sessione corrente.

## La forma e gli identificatori a vite diverse

La forma del `plan.md` istanza si descrive **una volta sola, qui nel nodo**: il file non ripete le istruzioni. Letto, si auto-spiega — una tabella ordinata per esecuzione e un footer di link sono leggibili a colpo d'occhio — e le convenzioni che la forma non rende evidenti da sé vivono in questo nodo, a cui `CLAUDE.md`/`AGENTS.md` rimandano invece di duplicarle. È la fonte-unica-di-verità applicata al plan, e il vantaggio dei symlink preservato: cambiare la forma è un edit solo, ereditato da tutti gli adottanti — incorporare le istruzioni in ogni `plan.md` lo annullerebbe.

La forma tiene separati **due identificatori con vite diverse**. Il numero `#` è un puntatore locale **effimero**: ordine di esecuzione, vive solo nella tabella, si rinumera lì quando l'ordine cambia, e serve a riferire un task in conversazione e nella colonna «Dipende da» (`#2` invece del titolo intero). Il link al file `tasks/` è invece **stabile**: vive in un footer ordinato per titolo, disaccoppiato dall'ordine. L'identità (il file) sta in un posto, l'ordine (il `#`) in un altro, e non si rincorrono: riordinare le priorità tocca una lista sola, non due.

La tabella resta **stretta e portabile** — `# · Priorità · Task · Dipende da` — con i collegamenti fuori dalle celle. «Priorità» (`alta`/`media`/`bassa`) indica l'importanza, non l'ordine; «Dipende da» usa `#n` per le dipendenze interne e testo libero per quelle esterne, e riflette dipendenze reali, non preferenze d'ordine. Nei commit e nella documentazione i task si citano per titolo, non per numero: il `#` è un puntatore conversazionale, non un'identità. Dove la coda è minima (`nixos`, `metodo`) un elenco basta — sempre senza ripetere qui le istruzioni.

## Sviluppo del metodo e perimetro dei task

Sul perimetro dei task lo sviluppo del metodo segue il movimento dal basso — uno dei due descritti in sviluppo-metodo, e quello che protegge dal costruire per futuri immaginati. Un task nasce dove esiste il problema concreto, con le fonti, le dipendenze e i criteri di chiusura del dominio. Se durante quel lavoro emerge una regola generale, il filing back aggiorna `metodo`; il task però resta locale finché richiede evidenza locale.

Il repo `metodo` non è una backlog board per i progetti adottanti. Non deve contenere task del tipo "controlla X in repo Y". Questi task hanno senso solo nel repo che deve produrre l'evidenza. `metodo` riceve il risultato quando diventa principio, nodo, skill base, strumento comune o criterio di revisione. Nel repo `metodo` i task dovrebbero essere rari.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                    | Confronto con il metodo                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | coda piccola, `plan` compatto.                                                        | Molto aderente: pochi task vivi, legati a cambi tecnici concreti.                                                                                                           |
| `bi`       | coda media; tabella stretta con puntatore `#` e footer per titolo (forma emersa qui). | Adeguato alla complessità del dominio. Le istruzioni d'uso sono ancora incorporate nel file: follow-up locale per snellirle verso il nodo e rimandare da `CLAUDE`/`AGENTS`. |
| `economia` | coda ampia legata a scadenze, adempimenti e situazioni aperte.                        | La numerosità è legittima perché il dominio è operativo e calendariale; serve però revisione frequente per evitare task morti.                                              |
| `salute`   | coda media; può contenere anche task senza file per elaborazione fonti.               | Adattamento accettabile per ingest semplici, ma i task più sostanziali dovrebbero avere contesto in `tasks/`.                                                               |

Il metodo deve ammettere granularità diverse. Nei domini tecnici il task tende a essere un intervento verificabile; in `economia` può essere una pratica aperta; in `salute` può essere ingest o sviluppo concettuale. La regola comune resta la stessa: ciò che è futuro e operativo non deve diventare nodo permanente.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [tasks](tasks.md)
- [why](why.md)
- [git-history](git-history.md)
- [ciclo-azione](ciclo-azione.md)
- [struttura-progetto](struttura-progetto.md)
- [affordance-signifier](affordance-signifier.md)
