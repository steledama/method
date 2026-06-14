---
data: 2026-06-13
stato: bozza
---

# Plan

Il plan risponde alla domanda: cosa dobbiamo fare adesso? È la supervisione corrente del lavoro futuro, ordinata per priorità e collegata ai dettagli operativi quando servono. È lo **stadio Plan del ciclo di sviluppo**: la sua istanza è il file root `plan.md`, sollevato dall'altezza nel ciclo fuori dalla cartella `tasks/` — è la meta-istanza dei task, letta a ogni sessione, quindi sale in root anche se cambia in fretta (l'altezza vince sulla pace).

`plan` è **o1-sviluppo**: il Plan del ciclo di sviluppo (l'azione sull'artefatto), distinto da **o1-runtime** (il Plan del runtime in action-cycle, l'azione sul mondo). Non nega l'omologia Plan=o1 — `action-cycle` la mappa — la **qualifica per ciclo**: stesso stadio, due annidamenti.

Il plan non è storico e non è backlog infinito. Deve rappresentare il lavoro ancora vivo. Quando un task viene completato, la riga sparisce; la storia resta in git, `verdict.md` e nei nodi aggiornati.

Regole:

- vive in root come `plan.md`, vista sintetica e supervisionabile
- ogni task sostanziale può avere un file in `tasks/`
- ogni file in `tasks/` deve avere una riga corrispondente in `plan.md`
- ordine e dipendenze devono rendere esplicita la priorità
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

La forma tiene separati **due identificatori con vite diverse**. Il numero `#` è un puntatore locale **effimero**: ordine di esecuzione, vive solo nella tabella, si rinumera lì quando l'ordine cambia, e serve a riferire un task in conversazione e nella colonna `Dip.` (`#2` invece del titolo intero). Il link al file `tasks/` è invece **stabile**: vive in un footer ordinato per titolo, disaccoppiato dall'ordine. L'identità (il file) sta in un posto, l'ordine (il `#`) in un altro, e non si rincorrono: riordinare le priorità tocca una lista sola, non due.

La tabella resta **stretta e portabile** — `# · Task · Dip.` — con i
collegamenti fuori dalle celle. L'ordine di esecuzione esprime la priorità tra i
task non bloccati; `Dip.` spiega perché un task importante non può ancora
salire. Una colonna `Priorità` separata sarebbe quindi ridondante: **ordine +
dipendenze codificano la priorità**.

`Dip.` usa `#n` per le dipendenze interne e marcatori `[a]`, `[b]`, ... per
condizioni esterne. I marcatori vengono spiegati subito sotto la tabella in una
breve sezione `Legenda dipendenze esterne`; il testo libero non gonfia le celle.
Le dipendenze devono essere reali, non preferenze d'ordine. Nei commit e nella
documentazione i task si citano per titolo, non per numero: il `#` è un
puntatore conversazionale, non un'identità.

La larghezza di circa 80 caratteri per riga resta una guida, non una regola. Il
titolo usa lo spazio che rimane dopo le colonne necessarie al dominio.

La forma è **uniforme su tutti i repo adottanti**: la granularità del dominio
vive nel contenuto — quanti task, di che natura — non nella forma. È la regola
dell'atrio applicata al plan (struttura uniforme, carattere nel contenuto): un
nodo in `kb/` contiene solo l'invariante generale, e ciò che è qui si applica
ovunque — nessuna coda è tanto piccola da giustificare una forma propria.

## Scadenze e fonti da elaborare

`plan.md` può contenere una sezione `## Scadenze` dopo `## Dettagli task`, ma
solo quando una data esterna interagisce con la priorità dei task. La scadenza è
input esogeno: avvicinandosi può far salire il lavoro collegato. Un calendario
di adempimenti che non modifica la coda resta invece nel file di dominio
dedicato, per esempio `scadenze.md`.

Le righe di ingest semplici possono non avere un file in `tasks/`. Quando i path
delle fonti renderebbero la tabella illeggibile, il titolo breve resta nella
tabella e i path completi vivono in `## Fonti da elaborare`, dopo `## Dettagli
task`. Se l'ingest richiede contesto, decisioni o più passaggi, resta un task
sostanziale e deve avere il proprio file.

## Sviluppo del metodo e perimetro dei task

Sul perimetro dei task lo sviluppo del metodo segue il movimento dal basso — uno dei due descritti in method-development, e quello che protegge dal costruire per futuri immaginati. Un task nasce dove esiste il problema concreto, con le fonti, le dipendenze e i criteri di chiusura del dominio. Se durante quel lavoro emerge una regola generale, il filing back aggiorna `metodo`; il task però resta locale finché richiede evidenza locale.

Il repo `metodo` non è una backlog board per i progetti adottanti. Non deve contenere task del tipo "controlla X in repo Y". Questi task hanno senso solo nel repo che deve produrre l'evidenza. `metodo` riceve il risultato quando diventa principio, nodo, skill base, strumento comune o criterio di revisione. Nel repo `metodo` i task dovrebbero essere rari.

## Applicazione nei progetti adottanti

- **`nixos`** — situazione attuale: coda piccola e compatta, ancora sulla
  tabella precedente con `Priorità` e dipendenze testuali. Confronto con il
  metodo: contenuto aderente; la nuova forma va recepita localmente.
- **`bi`** — situazione attuale: coda media, ancora sulla tabella precedente
  con `Priorità` e dipendenze testuali. Confronto con il metodo: contenuto
  adeguato alla complessità del dominio; la nuova forma e lo snellimento delle
  istruzioni incorporate vanno recepiti localmente.
- **`economia`** — situazione attuale: coda ampia legata a scadenze,
  adempimenti e situazioni aperte. Confronto con il metodo: mantiene
  `scadenze.md` separato perché il calendario è una funzione di dominio più
  ampia della priorità dei task.
- **`salute`** — situazione attuale: coda media; usa la forma canonica e può
  affiancare `## Scadenze` quando le date cambiano la priorità e `## Fonti da
elaborare` per ingest semplici senza file dedicato. I task sostanziali
  conservano contesto in `tasks/`.

Il metodo deve ammettere granularità diverse. Nei domini tecnici il task tende a essere un intervento verificabile; in `economia` può essere una pratica aperta; in `salute` può essere ingest o sviluppo concettuale. La regola comune resta la stessa: ciò che è futuro e operativo non deve diventare nodo permanente.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [readme](readme.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [git-history](git-history.md)
- [action-cycle](action-cycle.md)
- [project-structure](project-structure.md)
- [affordance-signifier](affordance-signifier.md)
