---
ciclo: dev
---

# Una rappresentazione per fatto: gli stadi output tengono solo il vivo, e il register non trascrive il plan

Ratificato (2026-07-11), dalla valutazione i2→i3 di due percezioni di
`economia` (catturate il 2026-07-10: «indice o2/tasks.md sottoutilizzato» e
«potatura delle prescriptions o3 consumate», consumate da questo filo);
esteso il 2026-07-28 dalla terza percezione dello stesso adottante («la
sezione cause del plan diventa una seconda fonte di verità», 2026-07-28,
anch'essa consumata qui) e il 2026-07-31 dalla quarta («la mappatura
task→obiettivo vive solo nel register, a mano», 2026-07-30), che porta
l'invariante fuori dagli stadi output, sul confine col register del Goal.

**Un solo indice per collezione, anche per i task.** Il footer `## Dettagli
task` di `o1/plan.md` era un secondo indice dei file `o2/` — la stessa
patologia del `#` abolito: due rappresentazioni da tenere in sincronia. E
infatti in `metodo` l'indice vero (`o2/tasks.md`) era rimasto indietro mentre
il footer faceva il suo lavoro: la duplicazione non era teorica. Ratificata la
forma di `economia`: `o2/tasks.md` è l'unico indice dei dettagli (una voce per
task aperto, ordinata per titolo), il plan chiude col solo rimando. Canone in
`kb/plan.md` e `kb/tasks.md`; `metodo` materializzato.

**Le prescrizioni consumate si potano.** o3 tiene solo il vivo — procedure,
canovacci riusabili, artefatti pronti all'atto; l'eseguito è archivio
travestito, e l'archivio è git. Canone in `kb/perform.md` («Chiusura del ciclo
di vita», il parallelo di `perceive` che mancava); `metodo` la praticava già —
la prescrizione strutturale è stata rimossa al recepimento pieno (2026-07-11) —
ora la regola è incisa. Presidio leggero in `plan-review` (le prescrizioni
collegate a lavoro chiuso non restano in collezione); una review dedicata
dello stadio Perform resta deliberatamente fuori finché l'accumulo non ricorre
in più adottanti.

**Non mancava una soglia, mancava una forma.** La sezione «cause delle attese e
delle pause» di `economia`, cresciuta al 44% del plan, non era una legenda
troppo lunga: era una legenda degenerata in **sezione parallela** alla tabella.
Tre dei cinque sintomi misurati (bullet su task `—`, ordine divergente, `Dip.`
che contraddice il proprio bullet) erano già impossibili nella forma canonica,
dove la chiosa pende da una chiave letta dalla tabella. Ciò che davvero mancava:
delle tre parti del plan solo due avevano una forma sottile — la tabella e `##
Scadenze` (`data → una riga → un rimando`); la chiosa di legenda diceva _cosa_
scrivere, mai _quanto_. Incisa in `kb/plan.md`: `chiave → causa → risveglio →
rimando a o2/`, in ordine di tabella, una voce per chiave e nessuna voce senza
chiave. Il numero di righe è la conseguenza degli slot, non il meccanismo: è la
forma che rende lo sforamento visibile senza leggere il contenuto (`constraint`,
il presidio strutturale sotto il check riflessivo che era saltato per mesi).

**Terza incarnazione, un solo vincolo.** `#` come secondo identificatore, footer
`## Dettagli task` come secondo indice, sezione cause come seconda fonte sullo
stato dei task: tre istanze bastano a nominare l'invariante nel nodo invece di
ri-diagnosticarlo caso per caso — un fatto o vive in una sola rappresentazione,
o la seconda è derivata dalla prima e ancorata da una chiave. La coerenza tra
struttura e prosa non si controlla: si rende impossibile da rompere.

**Quarta incarnazione: la copia stava fuori dagli stadi output, nel register.**
La direzione task→obiettivo viveva solo nell'elenco «Lavoro corrente» di
`goal.md`, trascritto a mano dai titoli del plan (`economia`, 2026-07-30). Non
era derivato da nulla, e infatti mancava un task in **posizione 2**, `—`, con
file `o2/` e voce d'indice: lavoro prioritario e sbloccato, invisibile al
register. Ratificata la forma di `economia` (2026-07-31): una colonna `Ob.` in
`o1/plan.md` con la chiave dell'obiettivo — numero per gli obiettivi runtime,
`S` per il Goal di sviluppo — e il register che rimanda alla colonna invece di
elencare titoli. Canone in `kb/plan.md` e `kb/goal.md`; `metodo` materializzato,
gli altri tre recepiscono col normale `method-review`.

Tre reperti che l'istanza aggiunge all'invariante, e che le prime tre non
avevano:

- **la duplicazione era asimmetrica nei tempi di lettura**, ed è per questo che
  non si è fatta notare: `o1/plan.md` si rilegge a ogni bootstrap, `goal.md`
  on-demand. La copia che deriva era quella che si guarda di rado. La tentazione
  è aggiungere un controllo alla review che legge l'originale; la risposta giusta
  è togliere la copia, ed è quella incisa nel nodo;
- **le due review si passavano il controllo a vuoto**: `plan-review` verificava
  task→obiettivo e `verdicts-review` obiettivo→segnale, ma entrambe leggevano lo
  stesso elenco scritto a mano — confermavano la copia, non la realtà. Un
  controllo riflessivo che legge la rappresentazione sbagliata non fallisce mai:
  è la stessa lezione di `constraint`, dal versante della supervisione;
- **gli indici di collezione non sono la stessa patologia**, e va detto perché
  la somiglianza inganna: `o2/tasks.md`, `i3/verdicts.md`, `o3/prescriptions.md`
  sono elenchi scritti a mano che ripetono item esistenti altrove, ma sono
  l'**unica** rappresentazione della collezione come collezione — non la seconda
  di un fatto che vive già in tabella. Il difetto non è «un elenco a mano», è «un
  elenco a mano di un fatto già rappresentato».

La colonna è arrivata con un **presidio, non con una regola**: il generatore
delle viste legge `Ob.` come contratto — chiave assente dal register o cella
vuota rompono la build (`o3/presentation.py`), e una riga di tabella di forma
non riconosciuta non si salta più in silenzio. Senza quest'ultimo tratto la
quarta incarnazione avrebbe riprodotto il difetto di `vista-derivata-e-verificata`:
tabella a quattro colonne, parser fermo a tre, vista dei task vuota senza che
nulla rompesse.

**Potare è fondere, non cancellare.** Reperto emerso _facendo_ la potatura, e il
più portabile perché indipendente dal plan: ogni istruzione di consolidamento
del metodo assume implicitamente che la copia da rimuovere sia quella stale. In
due casi su otto era il plan a portare il fatto più recente. Riga aggiunta al
passo 4 di `verdicts-review` (dove l'atto vive), non a un nodo: con una sola
istanza resta operativa. Se ricorre sui fili `i3/` o sulle prescrizioni `o3/`,
sale a canone.

Il ritardo di sedici giorni perché il protocollo post-evento — nato in
`economia` — rientrasse nel suo fork non è un segnale a sé: sta sotto la cadenza
dell'audit mensile, che già lo misura (`audit-adottanti`), ed è strutturale per
l'adottante che è origine di buona parte del canone.

Watchpoint aperti sulla colonna `Ob.`: la chiave `S` per il Goal di sviluppo è
nata materializzando la colonna in `metodo` — dove l'unico task non bloccato
serve il goal di sviluppo, che nel register non è numerato — e va collaudata sui
tre adottanti che devono ancora recepirla; il caso «un task serve due obiettivi»
(`1,4`) è ammesso ma deve restare **raro** (in `economia` una riga su diciassette),
e se cresce il sospetto si sposta sui task da scomporre o sugli obiettivi da
riformulare. La distribuzione dei task per obiettivo, ora leggibile a colpo
d'occhio, resta una proprietà della forma: non se ne fa un controllo di
`plan-review` finché la forma la mostra da sé.

Watchpoint: la forma nuova del plan viaggia col normale `method-review` degli
adottanti (nessuna prescrizione dedicata: modifica puntuale, non strutturale);
se un adottante accumula o3 consumate nonostante il check di `plan-review`, il
filo si riapre verso la review dedicata. Da sciogliere al prossimo
`method-review` di `economia`: la regola del budget copiata nel suo `CLAUDE.md`
contraddice `kb/plan.md` («la forma si descrive una volta sola nel nodo») — la
premessa era vera (la skill gira solo se invocata), ma la risposta è che il plan
si legge a ogni bootstrap e la forma si auto-spiega, non che la regola si
duplichi. Se il ramo «potare fondendo» cresce oltre la riga di skill, si splitta
in filo proprio.
