---
description: Revisione consistenza, priorità e dipendenze dei task aperti del metodo
user-invocable: true
---

Rivedi i task aperti come supervisione corrente del lavoro sul metodo. Usa questa
skill a inizio sessione quando bisogna scegliere cosa affrontare, e a fine
sessione quando decisioni metodologiche, generalizzazioni emerse dagli adottanti o
ristrutturazioni di nodi possono aver cambiato priorità, dipendenze o completezza
dei task. Questa è la copia canonica della skill: gli adottanti la forkano e la
parametrizzano sui propri segnali di dominio.

## Procedura

**1. Raccogli il contesto corrente**

Esegui in parallelo:

```bash
git diff HEAD
git status --short
git log --oneline -5
```

Leggi `o1/plan.md`, `map.md` se esiste, i fili recenti in `i3/` e i file `o2/` necessari per capire
i task aperti. Se l'obiettivo è solo un health check, puoi limitarti ai
titoli/frontmatter dei file `o2/`.

**2. Verifica consistenza o1/plan.md/o2**

Controlla:

- ogni file `o2/*.md` con `stato: aperto` ha una riga corrispondente in `o1/plan.md`
- ogni link `o2/` in `o1/plan.md` esiste
- task chiusi da un commit, una propagazione completata o un nodo creato non
  restano aperti
- `o1/plan.md` resta povero: il `metodo` non è una backlog board per gli adottanti
  (cfr. `kb/plan.md`), i suoi task sono rari e riguardano solo questo repo

**3. Rivaluta stato, dipendenze e priorità**

Individua eventi che possono spostare priorità o creare/rimuovere dipendenze, che
nel `metodo` hanno natura propria:

- una generalizzazione si è stabilizzata in un repo adottante -> può diventare
  nodo, skill base, strumento comune o criterio di revisione qui
- rinomina o spostamento di un nodo -> richiede aggiornare i link nei `CLAUDE.md`
  e `README.md` di tutti gli adottanti collegati
- nuova fonte (`i1`) ingerita o cornice teorica importata -> può aprire nodi bozza
  o ristrutturazioni
- drift tra `i2/` e i nodi -> può aprire un task di riallineamento o2
- scadenza di una fotografia dell'osservatorio cross-repo

**3b. Lettura strategica delle mosse**

L'igiene (passi 2-3) dice se la coda è coerente; non se una mossa **vada fatta**.
Per ogni mossa nostra che la review raccomanderebbe, interroga tre lenti — e se una
si accende, la mossa può **nascere come `pause`** invece che come prossimo task:

- **mandato/canale** — la mossa scavalca un agente o un canale con mandato? Nel
  `metodo`: scrivere diretto nei file di un adottante invece di lasciare che il suo
  `method-review` tiri il canone scavalca la membrana («agisci attraverso,
  ratifica»).
- **sequenza/informazione** — un uso o una conversazione imminente darebbe un
  _read_ prima di muoverci? Nel `metodo`: l'uso reale di un adottante darebbe
  l'evidenza prima di incidere il canone («evidenza prima della struttura»).
- **effetti di secondo ordine** — la mossa rompe un consumatore a valle o cambia
  gli incentivi di una controparte? Nel `metodo`: un rename o un refactor di un
  nodo che rompe un generatore o un link negli adottanti.

È la versione **plan-time** del check i3 che `/commit` fa a commit-time: stesso
invariante, momento diverso. La ricchezza multi-attore (incentivi, canali neutrali,
tempismo di una negoziazione) vive nei fork degli adottanti come adattamento di
dominio; qui resta l'invariante.

**4. Proponi le modifiche e il prossimo task**

Presenta all'utente, come elenco, le modifiche proposte — una voce per task, con
azione (aggiungi/modifica/rimuovi), priorità e motivo:

- **<task>** — <azione>; priorità <…>; <motivo>

Se non ci sono modifiche da proporre, dillo esplicitamente. Chiudi indicando il
task consigliato per la sessione corrente, motivandolo con urgenza, dipendenze e
costo/opportunità.

**5. Applica solo dopo conferma**

Applica modifiche a `o1/plan.md` e `o2/` solo dopo conferma esplicita dell'utente.

## Note operative

- Mantieni i titoli brevi e coerenti con la tabella esistente
- La colonna `Dip.` deve riflettere dipendenze reali, non preferenze d'ordine
- I task completati si rimuovono da `o1/plan.md` e `o2/`; lo storico resta in git,
  nei fili `i3/` e nei nodi aggiornati
- Dopo la revisione, suggerisci `/commit` per chiudere la sessione quando ci sono
  modifiche da fissare
