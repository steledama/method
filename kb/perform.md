---
stato: bozza
---

# Perform (o3)

Lo stadio o3 del ciclo d'azione: la prescrizione versionata dell'atto, il riflesso del Perform predisposto sul lato interno della membrana `world`. o3 **non è l'atto**: l'email inviata, l'incontro, la transazione, il deploy e il gesto corporeo accadono nel Mondo. o3 è la loro prescrizione versionata — un canovaccio, un messaggio predisposto, un promemoria, un runbook, un payload pronto. È l'ultimo gradino dell'arco di esecuzione (cfr. `output`), quello che bacia la membrana `world`.

Come i1 (`perceive`), o3 è **on-demand**: serve quando l'esecuzione richiede precisione, revisione o durata; non ogni gesto deve lasciare un artefatto. Dove vive: la collezione `o3/`, indicizzata da `o3/prescriptions.md`, versionata quando precisione o durata lo richiedono.

## Chiusura del ciclo di vita

Una prescrizione è **consumata** quando l'atto che predisponeva è compiuto e
l'esito è risalito dove deve vivere: nel Mondo (l'email inviata, il deploy
fatto), nei fili `i3/`, nei task `o2/` o nei nodi. Come per le catture i1
(cfr. `perceive`) e i task completati (cfr. `tasks`), il file si elimina
insieme alla riga nell'indice — la collezione tiene solo procedure vive,
canovacci riusabili e artefatti ancora pronti all'atto; un o3 che accumula
prescrizioni eseguite è un archivio travestito, e l'archivio è git (cfr.
`git-history`). L'indice può nominare in prosa l'ultima chiusa, come ponte
verso la storia. Nel repo `metodo` la regola è la stessa a scala di
propagazione: una prescrizione resta finché tutti gli adottanti non l'hanno
recepita, poi si rimuove. Il presidio è leggero e vive in `plan-review`, che
rivedendo i task verifica che le prescrizioni collegate a lavoro chiuso non
restino in collezione; una review dedicata dello stadio entra in gioco solo se
l'accumulo ricorre. (Sciolto dal basso da `economia`, 2026-07-10.)

## L'esecuzione può far emergere Goal

Predisporre un atto obbliga a specificare destinatari, vincoli, poste e criteri di successo. Questo lavoro può rendere visibili Goal latenti non ancora formalizzati: il canovaccio non si limita a eseguire un'intenzione, può rivelare che l'intenzione era incompleta. Il triage/formazione-goal non appartiene quindi solo all'input esogeno (cfr. `compare`); può essere innescato anche dall'arco di esecuzione. Il nuovo Goal resta una decisione riflessiva, non un prodotto automatico di o3 (cfr. `goal`).

Connessioni:

- [action-cycle](action-cycle.md)
- [output](output.md)
- [perceive](perceive.md)
- [world](world.md)
- [goal](goal.md)
- [compare](compare.md)
- [processing-layers](processing-layers.md)
- [tasks](tasks.md)
- [git-history](git-history.md)
