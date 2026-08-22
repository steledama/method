---
stato: maturo
---

# Plan

Il plan è la supervisione corrente del lavoro futuro: risponde a «cosa facciamo
adesso?». La sua istanza è `o1/plan.md`; i dettagli sostanziali vivono nei file
`o2/`, indicizzati una sola volta da `o2/tasks.md`.

È una coda, non uno storico né un backlog degli adottanti. Contiene solo lavoro
vivo del repository, ordinato per esecuzione. Un task concluso scompare dal plan
e da `o2/`; Git e i fili conservano ciò che merita storia.

## Forma

La tabella canonica usa `Ciclo · Ob. · Task · Dip.`:

- `Ciclo`: `dev` o `runtime`, secondo il mondo su cui insiste il task;
- `Ob.`: numero dell'obiettivo servito in `goal.md`, oppure `S` per il Goal di
  sviluppo; non può essere vuoto;
- `Task`: titolo unico usato anche nei riferimenti e nell'indice `o2/tasks.md`;
- `Dip.`: `—` se pronto, `↳ <titolo>` se sequenziato dopo un altro task,
  `w<n>` se la prossima mossa è esterna, `p<n>` se la tratteniamo noi.

L'ordine delle righe, insieme alle dipendenze, esprime la priorità: non servono
numeri identificativi o una colonna apposita. Un fatto vive in una sola
rappresentazione; eventuali dettagli stanno in `o2/`, non in nuove colonne.

Attese e pause portano un indice (`w1`, `p2`) che le lega a una legenda breve
sotto la tabella: la lettera dice chi tiene il tempo — il mondo o noi — e il
numero è l'indirizzo della chiosa. Gli indici si riassegnano in ordine di tabella
a ogni revisione: sono indirizzi, non identificatori stabili del task. La legenda
dichiara causa e condizione di risveglio; non diventa un secondo diario.

## Attese a finestra

`Dip.` dice da cosa dipende un task, non come si comporta il costo del ritardo, e
sono tre comportamenti diversi. L'attesa **piatta** non costa: l'opzione resta
identica. L'attesa **onerosa** costa in modo crescente ma resta aperta e si
recupera pagando — interessi, sanzioni, ravvedimenti. L'attesa **a finestra** non
rende la cosa più cara: può renderla impossibile.

Le prime due sono già governate, perché `## Scadenze` regge tutto ciò che ha una
data. La terza è invisibile per costruzione: la sua caratteristica è precisamente
di non averne una — una capacità di agire che può venir meno, una controparte che
può uscire di scena, un fatto altrui non databile. Nessun controllo che ragioni
per distanza temporale la troverà.

Per questo l'indice può portare un `!` appeso (`w2!`): l'opzione può chiudersi e
non riaprire. Significa **deperibile, non urgente**, e la distinzione va tenuta
ferma perché inverte la lettura normale della coda: una finestra può avere mesi
davanti e meritare comunque presidio, mentre una scadenza già passata può
legittimamente restare in attesa.

Si marca ciò la cui chiusura **non ha una data calcolabile** e su cui non c'è
ancora una mossa in agenda. Se una data esiste — una prescrizione, un termine di
decadenza — il posto è `## Scadenze`, e marcarla qui diluirebbe il segnale: la
rarità è ciò che lo fa funzionare.

Vale anche il verso opposto, ed è l'esito che il marcatore deve provocare:
appena si mette in agenda l'azione che presidia la finestra, **la data sostituisce
il marcatore**, che si toglie. Il `!` serve finché si aspetta, e smettere di
aspettare è il modo giusto di farlo sparire. Un piano in cui non compare perché
ogni finestra è stata messa in agenda è un piano sano, non un piano che ha
dimenticato il meccanismo.

La chiosa di un `!` dichiara due cose oltre a causa e risveglio: **cosa chiude la
finestra** e **cosa resta se si chiude**. Il secondo campo è quello che conta.
Scrivere il ripiego col suo costo trasforma un'ansia in una decisione: si può
scegliere di rischiare una finestra, non si può sceglierlo senza sapere cosa c'è
dopo.

Il controllo delle scadenze dell'adottante stampa le righe marcate a ogni
esecuzione, senza condizione di distanza, e non le conta come scadute: non lo
sono.

## Tempo e fonti

`## Scadenze` contiene solo date esogene o battiti che possono cambiare l'ordine
della coda. Se l'orologio è nostro, la data appartiene alla condizione di un
`pause`; se è di uno scheduler, la riga indica cadenza e configurazione senza
replicare ogni prossima data. Calendari che non muovono la coda restano nel
dominio.

Un ingest semplice può restare una riga del plan; `## Fonti da elaborare` tiene
eventuali path lunghi. Quando servono decisioni, vincoli o più passaggi, nasce un
file `o2/`.

La skill `exec plan` controlla coerenza, priorità e rapporto task→obiettivo; il
generatore verifica il contratto tra tabella, indice e file `o2/`.

Connessioni:

- [tasks](tasks.md)
- [goal](goal.md)
- [verdict](verdict.md)
- [action-cycle](action-cycle.md)
- [constraint](constraint.md)
- [view](view.md)
