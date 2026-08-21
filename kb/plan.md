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
  `world` se la prossima mossa è esterna, `pause` se la tratteniamo noi.

L'ordine delle righe, insieme alle dipendenze, esprime la priorità: non servono
numeri identificativi o una colonna apposita. Un fatto vive in una sola
rappresentazione; eventuali dettagli stanno in `o2/`, non in nuove colonne.

`world` e `pause` possono avere una chiave (`world [a]`) spiegata in una legenda
breve sotto la tabella. La legenda dichiara causa e condizione di risveglio; non
diventa un secondo diario del task.

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
