---
stato: bozza
---

# Plan

Il plan risponde alla domanda: cosa dobbiamo fare adesso? È la supervisione corrente del lavoro futuro, ordinata per priorità e collegata ai dettagli operativi quando servono. È lo **stadio Plan del ciclo di sviluppo**: la sua istanza è `o1/plan.md`, il file unico che regna nella stanza `o1/` e indicizza i dettagli in `o2/`.

`plan` è **o1-sviluppo**: il Plan del ciclo di sviluppo (l'azione sull'artefatto), distinto da **o1-runtime** (il Plan del runtime in action-cycle, l'azione sul mondo). Non nega l'omologia Plan=o1 — `action-cycle` la mappa — la **qualifica per ciclo**: stesso stadio, due annidamenti.

Il plan non è storico e non è backlog infinito. Deve rappresentare il lavoro ancora vivo. Quando un task viene completato, la riga sparisce; la storia resta in git, nei fili di `i3/` e nei nodi aggiornati.

Regole:

- vive in `o1/plan.md`, vista sintetica e supervisionabile
- ogni task sostanziale può avere un file in `o2/`
- ogni file in `o2/` deve avere una riga corrispondente in `o1/plan.md`
- ordine e dipendenze devono rendere esplicita la priorità
- i task completati vanno rimossi, non archiviati in `o2/`
- i task locali restano nel repo locale, non nel repo metodo
- i task del repo `metodo` riguardano solo il metodo stesso: ristrutturazione,
  semplificazione, coerenza dei nodi, strumenti portabili già giustificati o
  generalizzazioni emerse dai repo adottanti
- le verifiche operative su un repo adottante restano nel repo adottante, anche
  quando possono produrre filing back metodologico

I task sono parte strutturale del metodo perché le sessioni LLM pianificano, analizzano e implementano lavoro attraverso task espliciti. Se i task driftano, la sessione parte da una supervisione falsa: priorità, dipendenze e prossimo lavoro non rappresentano più lo stato reale del progetto.

La revisione del plan va fatta come controllo leggero a inizio sessione e come controllo completo quando cambiano fatti, scadenze o dipendenze. Nei progetti adottanti questa funzione è codificata nella skill base `tasks-review`, che deve verificare drift `plan`/`tasks`, task superati, nuovi task emersi dai fatti, priorità aggiornate e task consigliato per la sessione corrente.

## La forma e l'identità unica dei task

La forma dell'istanza `o1/plan.md` si descrive **una volta sola, qui nel nodo**: il file non ripete le istruzioni. Letto, si auto-spiega — una tabella ordinata per esecuzione e un footer di link sono leggibili a colpo d'occhio — e le convenzioni che la forma non rende evidenti da sé vivono in questo nodo, a cui `CLAUDE.md`/`AGENTS.md` rimandano invece di duplicarle. È la fonte-unica-di-verità applicata al plan, e il vantaggio dei symlink preservato: cambiare la forma è un edit solo, ereditato da tutti gli adottanti — incorporare le istruzioni in ogni `plan.md` lo annullerebbe.

Un task ha **un solo identificatore: il suo titolo**. È lo stesso ovunque — nella
tabella, in `Dip.` (`↳ <titolo>`), in conversazione e nei commit — e ancora al
file `o2/` tramite un footer ordinato per titolo, disaccoppiato dall'ordine di
esecuzione. L'ordine non è un identificatore: è la **sequenza delle righe**, che
esprime la priorità (l'imminenza della prossima mossa) e si riordina spostando
righe, senza rinumerare nulla. Un numero `#` di riga sarebbe un **secondo**
identificatore da tenere in sincronia — riordinare toccherebbe la tabella _e_
ogni riferimento `#n` in `Dip.` — e veniva letto come ID stabile pur essendo
effimero: per questo non c'è. (La doppia vita del `#` è l'attrito che gli
adottanti `economia` e `bi` hanno sciolto dal basso togliendolo.)

La tabella resta **stretta e portabile** — `Ciclo · Task · Dip.` — con i
collegamenti fuori dalle celle. `Ciclo` apre la riga: è la colonna a valori
brevi e ricorrenti, e in testa raggruppa a colpo d'occhio i due annidamenti
prima ancora di leggere i titoli; distingue `dev` e `runtime`, letti dal
Mondo su cui il task insiste. Il titolo-identità segue; l'ordine di esecuzione
esprime la priorità tra i task non bloccati; `Dip.` chiude spiegando perché un
task importante non può ancora salire. Una colonna `Priorità` separata sarebbe quindi ridondante: **ordine +
dipendenze codificano la priorità**.

`Dip.` risponde a una domanda sola: il task è pronto, e se no, _di chi è la
mossa_ che lo sblocca? Pensare le dipendenze solo come task↔task è troppo povero:
appiattisce su «dipende / non dipende» situazioni che chiedono risposte opposte.
La colonna ha quattro significanti, dal più libero al più trattenuto:

- `—` — nessun blocco: il task è eseguibile ora.
- `↳ <titolo>` — la mossa è nostra ma **sequenziata**: il task attende il
  completamento di un altro task, citato per titolo (dipendenza interna).
- `world` — la mossa è di un **altro**: il task attende dal mondo una conferma,
  una risposta, un'email, un preventivo, un atto altrui; il prossimo passo non è
  nostro. È una sospensione da **sorvegliare**, non un abbandono: se il silenzio
  supera il tattico, si sollecita e il task torna `—`.
- `pause` — la mossa è nostra, ma la **tratteniamo deliberatamente**. Il task
  sarebbe eseguibile e nessuno fuori ci blocca; scegliamo di non agire — per
  attendere il muoversi degli altri attori di una negoziazione, o per darci tempo
  (approfondimento, ripensamento, valutazione a freddo o su più dati). Il blocco
  è autoimposto: `pause` è un muro che alziamo noi, mentre con `world` il muro è
  fuori. La parola per esteso al posto del vecchio `|`, che collideva con il
  delimitatore di colonna delle tabelle markdown (andava escapato `\|`).

`world` e `pause` possono portare una chiave di legenda — `world [a]`, `pause [b]` —
quando una condizione specifica in una riga aggiunge qualcosa oltre al titolo del
task: una breve `Legenda dipendenze esterne` sotto la tabella la chiosa (per
`world`, l'evento atteso; per `pause`, la ragione della pausa e la sua condizione di
risveglio). La chiave è **facoltativa**: un `world` o `pause` nudo basta quando il
titolo già dice tutto, e il testo libero non gonfia mai le celle. Tre livelli:
significante in tabella, chiosa in legenda, dettaglio pieno nel file in `o2/`.

Un **batch** di task trattenuti per la stessa ragione non chiede un significante
nuovo: condividono una sola chiave di legenda (`pause [a]` su più righe), chiosata
una volta. E quando il fronte parcheggiato è grande abbastanza da fare rumore
nella coda attiva, può raccogliersi in una **sezione di holding** propria (la sua
ragione e il suo risveglio dichiarati una volta in testa) — adattamento di
dominio legittimo, non una variante del canone.

I task di **monitoraggio** sono il caso che il modello task↔task non copre: non
dipendono da un altro task ma dal trascorrere del tempo e dall'evolversi di una
condizione. Si collocano su `world` quando sorvegliano un evento o un
comportamento esterno (un server da osservare nei reboot, un esito atteso) o su
`pause` quando aspettano la nostra esperienza accumulata per una valutazione a freddo
(sessioni di meditazione da pesare dopo mesi, per continuità ed effetti).
Restano aperti per **vigilanza attiva**, e il significante più la sua riga di
legenda dicono cosa si sorveglia e fino a quando.

Le dipendenze devono essere reali, non preferenze d'ordine. Nei commit e nella
documentazione i task si citano sempre per titolo — la stessa identità che porta
la tabella: non c'è un puntatore numerico parallelo da disambiguare.

La larghezza di circa 80 caratteri per riga resta una guida, non una regola. Il
titolo usa lo spazio che rimane dopo le colonne necessarie al dominio.

La forma è **uniforme su tutti i repo adottanti**: la granularità del dominio
vive nel contenuto — quanti task, di che natura — non nella forma. È la regola
dell'atrio applicata al plan (struttura uniforme, carattere nel contenuto): un
nodo in `kb/` contiene solo l'invariante generale, e ciò che è qui si applica
ovunque — nessuna coda è tanto piccola da giustificare una forma propria.

## Scadenze e fonti da elaborare

`o1/plan.md` può contenere una sezione `## Scadenze` dopo `## Dettagli task`, ma
solo quando una data **esogena** interagisce con la priorità dei task. La scadenza
è input dal mondo: avvicinandosi può far salire il lavoro collegato. Non è solo un
_termine ultimo_ ("non oltre X"): può essere una **finestra tattica** ("non prima
del 30/06 — è quando l'atto altrui matura — ed entro Y") quando i suoi bordi li
fissa il mondo; in tal caso la riga esplicita finestra e razionale, e il task non
va raccomandato finché la finestra non si apre. Quando invece l'orologio è il
**nostro** — una data di risveglio che ci diamo per una pausa deliberata — non è
una scadenza ma parte della pausa stessa: il task porta `pause` e la condizione di
risveglio (una data o un trigger) vive nella riga di legenda, non qui. La regola è
**chi possiede l'orologio**: mondo → `## Scadenze`, noi → legenda del `pause`. Un
calendario di adempimenti che non modifica la coda resta invece nel file di
dominio dedicato, per esempio `scadenze.md`.

Dentro `## Scadenze` ogni voce è sottile — `data → una riga → un rimando` al task
o al nodo — e la disciplina dei tre livelli vale anche qui: protocolli, importi e
cronache stanno nel task/nodo, non nella sezione. Una scadenza **ricorrente** che
muove la coda non chiede una sezione propria: vive in `## Scadenze` con la cadenza
tra parentesi — `(mensile)`, `(annuale)`, `(biennale)` — e la **prossima
occorrenza** come data. Una ricorrente che non muove la coda resta nel file di
dominio, come sopra.

Le righe di ingest semplici possono non avere un file in `o2/`. Quando i path
delle fonti renderebbero la tabella illeggibile, il titolo breve resta nella
tabella e i path completi vivono in `## Fonti da elaborare`, dopo `## Dettagli
task`. Se l'ingest richiede contesto, decisioni o più passaggi, resta un task
sostanziale e deve avere il proprio file in `o2/`.

## Sviluppo del metodo e perimetro dei task

Sul perimetro dei task lo sviluppo del metodo segue il movimento dal basso — uno dei due descritti in method-development, e quello che protegge dal costruire per futuri immaginati. Un task nasce dove esiste il problema concreto, con le fonti, le dipendenze e i criteri di chiusura del dominio. Se durante quel lavoro emerge una regola generale, il filing back aggiorna `metodo`; il task però resta locale finché richiede evidenza locale.

Il repo `metodo` non è una backlog board per i progetti adottanti. Non deve contenere task del tipo "controlla X in repo Y". Questi task hanno senso solo nel repo che deve produrre l'evidenza. `metodo` riceve il risultato quando diventa principio, nodo, skill base, strumento comune o criterio di revisione. Nel repo `metodo` i task dovrebbero essere rari.

## Applicazione nei progetti adottanti

I quattro adottanti sono allineati alla forma corrente (identità per titolo,
`↳`/`world`/`pause`, niente colonna `#`) dopo la propagazione del 2026-06-25. Ciò
che varia è il **carattere del dominio**, non la forma:

- **`economia`** — coda ampia legata a scadenze, adempimenti e situazioni aperte.
  È l'**origine** di `pause`, dell'identità per solo nome e del passo `3b` di
  lettura strategica. Mantiene `scadenze.md` separato perché il calendario è una
  funzione di dominio più ampia della priorità dei task.
- **`bi`** — coda media; ha co-segnalato la rimozione del `#` e `|`→`pause`.
  Tiene un guardrail operativo (uso di un tool su PROD) nelle Note invece che
  come significante di dipendenza.
- **`salute`** — coda media con una sezione di **holding** `## Sospesi` (forma a
  batch della pausa, adattamento di dominio ammesso) e un `## Scadenze` di
  appuntamenti medici datati, una-tantum; affianca `## Fonti da elaborare` per
  l'ingest semplice. I task sostanziali conservano contesto in `tasks/`.
- **`nixos`** — coda piccola e compatta, dominio di configurazione; usa
  `world`/`pause` con legenda a chiavi per monitoraggi e pause tattiche.

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
