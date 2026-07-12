---
description: Revisione consistenza, priorità, dipendenze e direzione task→obiettivo dei task aperti del metodo
user-invocable: true
---

Rivedi i task aperti come supervisione corrente del lavoro sul metodo. È la
skill simmetrica di `verdicts-review`: questa tiene onesto il piano (braccio di
esecuzione), quella tiene onesto il confronto (braccio di valutazione); il
register `goal.md` è la cerniera che entrambe controllano da versanti opposti.
Usa questa skill a inizio sessione quando bisogna scegliere cosa affrontare, e a
fine sessione quando decisioni metodologiche, generalizzazioni emerse dagli
adottanti o ristrutturazioni di nodi possono aver cambiato priorità, dipendenze
o completezza dei task. Dopo eventi del mondo gira per **ultima** nel
protocollo post-evento (percezione i1 → `verdicts-review` → `plan-review`):
le priorità si rivalutano su verdetti freschi, non stantii. Questa è la copia
canonica della skill: gli adottanti la forkano e la parametrizzano sui propri
segnali di dominio.

## Procedura

**1. Raccogli il contesto corrente**

Esegui in parallelo:

```bash
git diff HEAD
git status --short
git log --oneline -5
```

Leggi `o1/plan.md`, il register `goal.md`, i fili recenti in `i3/` e i file `o2/` necessari per capire
i task aperti. Se l'obiettivo è solo un health check, puoi limitarti ai
titoli/frontmatter dei file `o2/`.

Cerca gli **handoff pendenti**: gli «impatti sul piano» di un
`verdicts-review` appena girato e le catture i1 con impatti o1 non ancora
consumate. Sono input, non comandi: consumali con giudizio e dichiara le
divergenze (es. una dipendenza che resta `world` anche se l'attesa puntuale è
sciolta).

**2. Verifica consistenza o1/plan.md/o2**

Controlla:

- ogni file `o2/*.md` ha una riga corrispondente in `o1/plan.md` e la sua voce
  nell'indice `o2/tasks.md` — l'unico indice dei dettagli: il plan porta solo
  il rimando, non un secondo elenco di link (cfr. `kb/plan.md`)
- ogni voce dell'indice `o2/tasks.md` punta a un file esistente
- le prescrizioni `o3/` collegate a lavoro chiuso non restano in collezione:
  una prescrizione consumata (atto compiuto, o recepita da tutti gli adottanti)
  si pota insieme alla sua riga in `o3/prescriptions.md` (cfr. `kb/perform.md`,
  «Chiusura del ciclo di vita»)
- task chiusi da un commit, una propagazione completata o un nodo creato non
  restano aperti
- `o1/plan.md` resta povero: il `metodo` non è una backlog board per gli adottanti
  (cfr. `kb/plan.md`), i suoi task sono rari e riguardano solo questo repo
- **direzione task→obiettivo**: ogni task serve un obiettivo dichiarato nel
  register `goal.md` (un task senza obiettivo è un candidato al taglio); il
  «lavoro corrente» citato nel register corrisponde a righe vive del plan. La
  direzione opposta (obiettivo→segnale/filo) è di `verdicts-review`

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

**6. Chiudi con l'handoff inverso «verdetti da rivalutare»**

Task i cui fatti, visti dal versante esecuzione, smentiscono o incrinano un
filo `i3/`. Se il protocollo post-evento è stato rispettato l'elenco è
normalmente **vuoto** — il vuoto è il segnale che la verità è passata per
prima, non un fallimento. Se non è vuoto, segnalalo al custode: il movimento
di ritorno è l'eccezione che va giustificata, non un secondo giro automatico.

## Note operative

- Mantieni i titoli brevi e coerenti con la tabella esistente
- La colonna `Dip.` deve riflettere dipendenze reali, non preferenze d'ordine
- I task completati si rimuovono da `o1/plan.md` e `o2/`; lo storico resta in git,
  nei fili `i3/` e nei nodi aggiornati
- Dopo la revisione, suggerisci `/commit` per chiudere la sessione quando ci sono
  modifiche da fissare
