---
sintesi: "Aggiungere a tasks.html una tabella di apertura — ordine, ciclo, obiettivo, dipendenza — con link agli slide dei singoli task, così la vista di o2 copre anche la supervisione d'insieme del plan senza sdoppiare la materializzazione di o1."
ciclo: dev
---

# Vista sinottica del plan in tasks.html

## Origine

Segnalato dall'adottante `bi` (2026-09-08): la coda di `o1/plan.md`, letta
grezza in un editor a schermo stretto, wrappa male quando una cella `Dip.`
composta (`↳ <titolo1> + <titolo2>`) allunga tutta la colonna. La vista
generata `tasks.html` non soffre il problema — uno slide per task, con
`overflow-x: auto` — ma non offre la supervisione d'insieme che la tabella
grezza dà: l'ordine di tutta la coda in un colpo d'occhio.

## Vincolo di design da rispettare

`kb/plan.md` è netto: o1 non ha una seconda materializzazione — «il piano è
la coda, e sdoppiarlo produrrebbe un nodo-atomo senza contenuto proprio». La
proposta non la viola: non introduce un nuovo file né una seconda fonte di
verità, arricchisce la vista che già esiste per o2 con un rendering derivato
dagli stessi dati che `task_view()` già legge via `parse_plan()`.

## Proposta tecnica

In `o3/build_views.py`, `task_view()`: prima degli slide per task, emettere
uno slide di apertura con una tabella HTML nativa (`Ciclo · Ob. · Task ·
Dip.`, stesse colonne del plan), `overflow-x: auto` per schermi stretti.
Ogni cella `Task` è un link `#<slug>` allo slide del task corrispondente più
sotto nello stesso file: pandoc assegna già `id="<slug-del-titolo>"` a ogni
`<section>` generata dall'H2, quindi basta calcolare lo stesso slug (ASCII,
minuscolo, spazi/punteggiatura → trattino) lato Python, senza introdurre un
secondo schema di identificatori.

## Criterio di chiusura

`tasks.html` apre su una tabella cliccabile equivalente al plan grezzo (stesso
ordine, stesse colonne), ogni riga porta al proprio slide di dettaglio; il
contratto generatore (`check_plan_contract`) resta l'unica fonte di verità
sulla corrispondenza plan↔o2. Verificare su almeno un adottante con
dipendenze `w<n>`/`p<n>` popolate (`bi`) che la tabella resti leggibile senza
scroll orizzontale eccessivo prima di chiudere.

Connessioni:

- [plan](../kb/plan.md)
- [tasks](../kb/tasks.md)
- [view](../kb/view.md)
