---
stato: maturo
---

# Tasks

`o2/` è la directory dei dettagli operativi e di contesto dei singoli task aperti. Risponde alla domanda: quali sono i dettagli operativi e di contesto dei singoli task aperti? Contiene lavoro futuro, non conoscenza permanente. È lo stadio Specify: il file in `o2/` spiega cosa, perché, con quali vincoli e dipendenze, mentre `o1/plan.md` ne tiene solo la riga di supervisione.

La separazione tra `o1/plan.md` e `o2/` serve a mantenere il cruscotto leggero senza perdere contesto. `plan` supervisiona cosa fare; il file in `o2/` spiega perché, con quali vincoli, con quali dipendenze e con quale stato operativo.

Regole:

- contiene solo task futuri o in corso
- non conserva storico dei task completati
- ogni file deve corrispondere a una riga in `o1/plan.md`
- ogni riga sostanziale di `o1/plan.md` deve avere un file quando serve contesto
- può linkare nodi KB per contesto stabile
- va ripulita quando il task viene completato
- nel repo `metodo`, contiene solo task propri del metodo, non verifiche operative
  sui repo adottanti

Nel repo `metodo`, `o2/` non è una coda di governance cross-repo. È una coda di manutenzione del metodo: ristrutturazioni, semplificazioni, coerenza dei nodi, formalizzazioni già maturate e strumenti comuni già giustificati dall'uso reale.

Le verifiche operative su un repo adottante vanno nello stadio Specify (`o2/`) di quel repo, anche quando possono produrre una generalizzazione metodologica. Il filing back verso `metodo` avviene dopo, quando il caso locale ha prodotto un criterio portabile. Questo evita che `metodo/o2/` diventi backlog dei progetti adottanti.

## Frontmatter dei task

```yaml
---
stato: aperto
sintesi: "Risultato atteso del task in una frase breve."
---
```

Il frontmatter dei task è obbligatorio perché permette agli strumenti cross-repo di distinguere i task operativi dai nodi stabili e di costruire report comparativi senza interpretare testo libero.

`stato` resta minimale: per ora il valore canonico è solo `aperto`. La data di apertura, come ogni data, vive in git e non nel frontmatter. `sintesi` è una frase autoriale e autosufficiente sul risultato atteso: non replica il titolo, non registra priorità, non contiene dipendenze e non sostituisce il corpo del task. Priorità e dipendenze vivono in `o1/plan.md`, perché `plan` è il punto di supervisione corrente.

Quando un task viene completato, il file viene eliminato insieme alla riga in `o1/plan.md`. Non serve uno stato `chiuso`: lo storico resta in git, nei fili di `i3/` e nei nodi aggiornati.

## Applicazione nei progetti adottanti

- **`nixos`** — situazione attuale: `o2/` piccolo, con task tecnici puntuali. Confronto con il metodo: buon uso come spazio temporaneo — il contesto stabile resta nei nodi e nel codice.
- **`bi`** — situazione attuale: `o2/` più ampio, con task legati a refactor, dati, fornitori e metodo. Confronto con il metodo: utile per non trasformare README e CLAUDE in backlog; richiede disciplina nel chiudere o spostare le decisioni in `kb/`/`i3/`.
- **`economia`** — situazione attuale: `o2/` molto operativo, legato a scadenze, pratiche, immobili, tasse e investimenti. Confronto con il metodo: caso che chiarisce l'adattamento — `o2/` può contenere pratiche reali e non solo refactor, ma deve restare lavoro futuro.
- **`salute`** — situazione attuale: `o2/` contiene task concettuali e operativi sostanziali, mentre ingest semplici possono restare solo righe in `plan`. Confronto con il metodo: conferma la soglia — ingest semplice può stare in `plan`, ma serie di nodi, loop pratica-verifica o interventi strutturali richiedono file dedicato finché non diventano nodi stabili.

La pratica conferma che `o2/` è parte del metodo ma non della KB stabile. Quando un file contiene principi riusabili, il contenuto va promosso a nodo; quando contiene solo stato storico, va chiuso e lasciato a git/fili `i3/`. Nel repo `metodo`, la condizione di apertura di un task è ancora più stretta: deve riguardare la custodia del metodo, non l'applicazione puntuale del metodo altrove.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [plan](plan.md)
- [readme](readme.md)
- [verdict](verdict.md)
- [connection](connection.md)
