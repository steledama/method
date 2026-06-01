---
data: 2026-05-23
stato: bozza
---

# Todo

todo/ è la directory dei dettagli operativi e di contesto dei singoli task aperti. Risponde alla domanda: quali sono i dettagli operativi e di contesto dei singoli task aperti? Contiene lavoro futuro, non conoscenza permanente.

La separazione tra README e todo/ serve a mantenere il bootstrap leggero senza perdere contesto. Il README supervisiona cosa fare; il file in todo/ spiega perché, con quali vincoli, con quali dipendenze e con quale stato operativo.

Regole:

- contiene solo task futuri o in corso
- non conserva storico dei task completati
- ogni file deve corrispondere a una riga nella tabella Tasks aperti del README
- ogni riga sostanziale del README deve avere un file quando serve contesto
- può linkare nodi KB per contesto stabile
- va ripulita quando il task viene completato
- nel repo `metodo`, contiene solo task propri del metodo, non verifiche operative
  sui repo adottanti

Nel repo `metodo`, `todo/` non è una coda di governance cross-repo. È una coda di manutenzione del metodo: ristrutturazioni, semplificazioni, coerenza dei nodi, formalizzazioni già maturate e strumenti comuni già giustificati dall'uso reale.

Le verifiche operative su un repo adottante vanno nel `todo/` di quel repo, anche quando possono produrre una generalizzazione metodologica. Il filing back verso `metodo` avviene dopo, quando il caso locale ha prodotto un criterio portabile. Questo evita che `metodo/todo/` diventi backlog dei progetti adottanti.

## Frontmatter dei task

```yaml
---
data: YYYY-MM-DD
stato: aperto
---
```

Il frontmatter dei task è obbligatorio perché permette agli strumenti cross-repo di distinguere i task operativi dai nodi stabili e di costruire report comparativi senza interpretare testo libero.

`data` è la data di apertura del task, non l'ultima modifica. `stato` resta minimale: per ora il valore canonico è solo `aperto`. Priorità e dipendenze vivono nella tabella del README, non nel frontmatter, perché il README è il punto di supervisione corrente.

Quando un task viene completato, il file viene eliminato insieme alla riga README. Non serve uno stato `chiuso`: lo storico resta in git, `log.md` e nei nodi aggiornati.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                   | Confronto con il metodo                                                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | `todo/` piccolo, con task tecnici puntuali.                                                                          | Buon uso come spazio temporaneo: il contesto stabile resta nei nodi e nel codice.                                                                                                      |
| `bi`       | `todo/` più ampio, con task legati a refactor, dati, fornitori e metodo.                                             | Utile per non trasformare README e CLAUDE in backlog; richiede disciplina nel chiudere o spostare le decisioni in KB/log.                                                              |
| `economia` | `todo/` molto operativo, legato a scadenze, pratiche, immobili, tasse e investimenti.                                | Caso che chiarisce l'adattamento: `todo/` può contenere pratiche reali e non solo refactor, ma deve restare lavoro futuro.                                                             |
| `salute`   | `todo/` contiene task concettuali e operativi sostanziali, mentre ingest semplici possono restare solo righe README. | Conferma la soglia: ingest semplice può stare nel README, ma serie di nodi, loop pratica-verifica o interventi strutturali richiedono file dedicato finché non diventano nodi stabili. |

La pratica conferma che `todo/` è parte del metodo ma non della KB stabile. Quando un file in `todo/` contiene principi riusabili, il contenuto va promosso a nodo; quando contiene solo stato storico, va chiuso e lasciato a git/log. Nel repo `metodo`, la condizione di apertura di un task è ancora più stretta: deve riguardare la custodia del metodo, non l'applicazione puntuale del metodo altrove.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [task-aperti](task-aperti.md)
- [readme](readme.md)
- [log](log.md)
- [connessione](connessione.md)
