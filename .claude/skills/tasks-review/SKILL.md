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

Leggi `plan.md`, `map.md`, `verdict.md` recente e i file `tasks/` necessari per capire
i task aperti. Se l'obiettivo è solo un health check, puoi limitarti ai
titoli/frontmatter dei file `tasks/`.

**2. Verifica consistenza plan.md/tasks**

Controlla:

- ogni file `tasks/*.md` con `stato: aperto` ha una riga corrispondente in `plan.md`
- ogni link `tasks/` in `plan.md` esiste
- task chiusi da un commit, una propagazione completata o un nodo creato non
  restano aperti
- `plan.md` resta povero: il `metodo` non è una backlog board per gli adottanti
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
- drift tra `interpretations/` e i nodi -> può aprire un task di riallineamento o2
- scadenza di una fotografia dell'osservatorio cross-repo

**4. Proponi le modifiche e il prossimo task**

Presenta all'utente una tabella:

| Task | Azione proposta           | Priorità | Motivo |
| ---- | ------------------------- | -------- | ------ |
| ...  | aggiungi/modifica/rimuovi | ...      | ...    |

Se non ci sono modifiche da proporre, dillo esplicitamente. Chiudi indicando il
task consigliato per la sessione corrente, motivandolo con urgenza, dipendenze e
costo/opportunità.

**5. Applica solo dopo conferma**

Applica modifiche a `plan.md` e `tasks/` solo dopo conferma esplicita dell'utente.

## Note operative

- Mantieni i titoli brevi e coerenti con la tabella esistente
- La colonna "Dipende da" deve riflettere dipendenze reali, non preferenze d'ordine
- I task completati si rimuovono da `plan.md` e `tasks/`; lo storico resta in git,
  `verdict.md` e nodi aggiornati
- Dopo la revisione, suggerisci `/commit` per chiudere la sessione quando ci sono
  modifiche da fissare
