---
data: 2026-06-06
stato: bozza
---

# Tasks

`tasks/` è la directory dei dettagli operativi e di contesto dei singoli task aperti. Risponde alla domanda: quali sono i dettagli operativi e di contesto dei singoli task aperti? Contiene lavoro futuro, non conoscenza permanente. È lo stadio Specify: il file in `tasks/` spiega cosa, perché, con quali vincoli e dipendenze, mentre `plan.md` ne tiene solo la riga di supervisione.

La separazione tra `plan` e `tasks/` serve a mantenere il cruscotto leggero senza perdere contesto. `plan` supervisiona cosa fare; il file in `tasks/` spiega perché, con quali vincoli, con quali dipendenze e con quale stato operativo.

Regole:

- contiene solo task futuri o in corso
- non conserva storico dei task completati
- ogni file deve corrispondere a una riga in `plan.md`
- ogni riga sostanziale di `plan.md` deve avere un file quando serve contesto
- può linkare nodi KB per contesto stabile
- va ripulita quando il task viene completato
- nel repo `metodo`, contiene solo task propri del metodo, non verifiche operative
  sui repo adottanti

Nel repo `metodo`, `tasks/` non è una coda di governance cross-repo. È una coda di manutenzione del metodo: ristrutturazioni, semplificazioni, coerenza dei nodi, formalizzazioni già maturate e strumenti comuni già giustificati dall'uso reale.

Le verifiche operative su un repo adottante vanno nel `tasks/` di quel repo, anche quando possono produrre una generalizzazione metodologica. Il filing back verso `metodo` avviene dopo, quando il caso locale ha prodotto un criterio portabile. Questo evita che `metodo/tasks/` diventi backlog dei progetti adottanti.

## Frontmatter dei task

```yaml
---
data: YYYY-MM-DD
stato: aperto
---
```

Il frontmatter dei task è obbligatorio perché permette agli strumenti cross-repo di distinguere i task operativi dai nodi stabili e di costruire report comparativi senza interpretare testo libero.

`data` è la data di apertura del task, non l'ultima modifica. `stato` resta minimale: per ora il valore canonico è solo `aperto`. Priorità e dipendenze vivono in `plan.md`, non nel frontmatter, perché `plan` è il punto di supervisione corrente.

Quando un task viene completato, il file viene eliminato insieme alla riga in `plan.md`. Non serve uno stato `chiuso`: lo storico resta in git, `why.md` e nei nodi aggiornati.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                   | Confronto con il metodo                                                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | `tasks/` piccolo, con task tecnici puntuali.                                                                          | Buon uso come spazio temporaneo: il contesto stabile resta nei nodi e nel codice.                                                                                                      |
| `bi`       | `tasks/` più ampio, con task legati a refactor, dati, fornitori e metodo.                                             | Utile per non trasformare README e CLAUDE in backlog; richiede disciplina nel chiudere o spostare le decisioni in KB/why.                                                              |
| `economia` | `tasks/` molto operativo, legato a scadenze, pratiche, immobili, tasse e investimenti.                                | Caso che chiarisce l'adattamento: `tasks/` può contenere pratiche reali e non solo refactor, ma deve restare lavoro futuro.                                                             |
| `salute`   | `tasks/` contiene task concettuali e operativi sostanziali, mentre ingest semplici possono restare solo righe in `plan`. | Conferma la soglia: ingest semplice può stare in `plan`, ma serie di nodi, loop pratica-verifica o interventi strutturali richiedono file dedicato finché non diventano nodi stabili. |

La pratica conferma che `tasks/` è parte del metodo ma non della KB stabile. Quando un file contiene principi riusabili, il contenuto va promosso a nodo; quando contiene solo stato storico, va chiuso e lasciato a git/why. Nel repo `metodo`, la condizione di apertura di un task è ancora più stretta: deve riguardare la custodia del metodo, non l'applicazione puntuale del metodo altrove.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [plan](plan.md)
- [readme](readme.md)
- [why](why.md)
- [connessione](connessione.md)
