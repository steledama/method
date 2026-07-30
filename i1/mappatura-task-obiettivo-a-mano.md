---
ciclo: runtime
---

# Segnale: la mappatura task→obiettivo vive solo nel register, a mano

Data: 2026-07-30 · Fonte: custode, su esperienza `economia` (ristrutturazione
di `goal.md` e introduzione di una colonna `Ob.` in `o1/plan.md`)

## Il segnale

In `economia` ogni obiettivo di `goal.md` portava una voce **«Lavoro
corrente»** con l'elenco dei titoli dei task che lo servono. È l'unico posto in
cui esisteva la direzione task→obiettivo: la tabella di `o1/plan.md` ha le
colonne `Ciclo`, `Task` e `Dip.`, e non nomina obiettivi.

Il 30/07, durante una `plan-review`, l'elenco è risultato **derivato**: mancava
del tutto un task che stava in **posizione 2** nella tabella, marcato `—`
(nessun blocco), con file `o2/` e voce nell'indice `o2/tasks.md`. Non era un
task marginale né appena nato: era lavoro prioritario e sbloccato, invisibile
al register. Nella stessa sessione ne è nato un secondo, che senza l'intervento
manuale sarebbe rimasto ugualmente fuori.

Osservazioni raccolte facendo la correzione:

- **è lo stesso modo di fallire che l'invariante nomina già**. `kb/plan.md` (da
  `6133ace`) stabilisce che un fatto viva in una sola rappresentazione, o che la
  seconda sia derivata dalla prima e ancorata da una chiave. Qui la seconda
  rappresentazione non era derivata da nulla: era una trascrizione;
- **la duplicazione era invisibile perché asimmetrica nei tempi di lettura**.
  `o1/plan.md` si rilegge a ogni sessione (bootstrap), `goal.md` si apre
  on-demand. La copia che deriva è quella che si guarda di rado, e nulla
  segnala la divergenza;
- **le due review si passavano il controllo a vuoto**. `plan-review` verifica
  «ogni task serve un obiettivo del register» e `verdicts-review` la direzione
  opposta; entrambe leggevano la stessa lista scritta a mano, quindi il
  controllo confermava la copia invece della realtà;
- **il criterio non era ambiguo, mancava il supporto**. Nessuno aveva sbagliato
  un giudizio: mancava il posto dove scrivere il dato una volta sola.

Risoluzione locale adottata (fatto, non prescrizione): una colonna **`Ob.`**
nella tabella di `o1/plan.md`, col numero dell'obiettivo servito (più d'uno
separato da virgola quando il task ne serve davvero due); `goal.md` rimanda
alla colonna invece di elencare i titoli. Divergenza dal canone registrata in
`method-review.md`.

Effetto collaterale non previsto, e forse il vero guadagno: con la mappatura in
colonna la **distribuzione** diventa leggibile a colpo d'occhio. In `economia`
è risultata 11 task su un obiettivo, 1 su un altro, e quell'1 era il traguardo
dichiarato. Il register appiattiva l'informazione spalmandola su liste
separate; la colonna l'ha resa un fatto visibile, ed è diventata materia di
decisione strategica nella stessa sessione.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- la direzione task→obiettivo va nel plan, nel register, o è indifferente
  purché stia in un posto solo? Il caso suggerisce il plan (si rilegge sempre,
  ed è dove il task esiste), ma il canone finora la colloca implicitamente nel
  register;
- una colonna in più nella tabella è ammissibile nel canone, o la terna
  `Ciclo` / `Task` / `Dip.` è forma chiusa? Se ammissibile, con quale criterio
  si accettano colonne nuove senza che la tabella diventi un database;
- il caso «task che serve due obiettivi» va ammesso (`1,4`) o è il sintomo di
  un task da scomporre? In `economia` una riga su diciassette è doppia e sembra
  legittima;
- esiste una regola generale del tipo **«un elenco scritto a mano che
  ripete item esistenti altrove è un difetto strutturale»**, applicabile oltre
  questo caso? Gli indici di collezione (`o2/tasks.md`, `o3/prescriptions.md`,
  `i3/verdicts.md`) sono elenchi analoghi: sono legittimi perché è l'indice
  della collezione stessa, o corrono lo stesso rischio;
- quando una copia derivata sta in un artefatto che si legge **meno spesso**
  dell'originale, serve un controllo esplicito nella review che legge
  l'originale? Qui il difetto è sopravvissuto perché nessuna delle due review
  confrontava le due superfici, si limitavano a leggere quella comoda;
- la **distribuzione** dei task fra gli obiettivi è un'informazione che il
  metodo vuole rendere visibile? Se sì, è una proprietà da chiedere alla forma
  (come qui, per effetto collaterale) o un controllo da mettere in
  `plan-review`.
