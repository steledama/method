---
description: Crea un git commit seguendo le convenzioni del repo metodo
user-invocable: true
---

Crea un git commit seguendo le convenzioni del progetto. Questa è la copia
canonica della skill: gli adottanti la forkano e la parametrizzano sui propri
formatter e fonti di verità.

## Pre-commit: domande da fare prima di procedere

**1. Audit KB** — Valuta se le modifiche toccano un numero significativo di nodi in `kb/` (aggiunte, rinominamenti, ristrutturazioni di link). Se sì, chiedi all'utente: _"Vuoi eseguire /kb-review prima del commit?"_. Se l'utente risponde sì, esegui la skill `kb-review` e includi eventuali fix nel commit. Se le modifiche sono minori (un file, fix puntuale), salta la domanda.

**1b. Formato nodo** — Per ogni nodo nuovo o pesantemente modificato in `kb/`: verifica che abbia (a) frontmatter con `stato:` in cima e (b) sezione `Connessioni:` in fondo. Se mancano entrambi, segnalalo prima di committare.

**1c. Portabilità del nodo** — Per ogni nodo nuovo in `kb/`: verifica che sia metodologico e applicabile ad almeno due progetti diversi. Un concetto specifico di un singolo dominio non appartiene alla `kb/` del `metodo`.

**1d. Propagazione** — Se un nodo è stato rinominato o spostato, ricorda che i link nei `CLAUDE.md` e `README.md` degli adottanti collegati vanno aggiornati a mano (i nodi arrivano via symlink, ma nome/path no).

**2. Filo in i3/** — Valuta se la sessione ha cambiato il verdetto su un filo/area aperta: nuovi nodi, cluster nuovi, decisioni strutturali o metodologiche, ingest di fonti, cambiamenti di approccio. Se sì, chiedi all'utente: _"Vuoi aggiornare il filo pertinente in `i3/` per questa sessione?"_. Se sì, aggiorna **in place** il file del filo pertinente (o crea un nuovo file se il filo è nuovo) con lo stato attuale — non un'entry datata, non un elenco di file: il git history del file è già il log. Se il filo si è chiuso (verdetto stabile, nessuna tensione aperta), rimuovi il file e l'indice in `i3/verdicts.md`. Se le modifiche sono di manutenzione (formatting, fix link, task completati), salta la domanda.

**3. I due check del ciclo di valutazione (i2/i3)** — Prompt leggeri, non burocrazia: se la risposta è no, si procede.

- **i2 — è cambiato il significato delle interpretazioni?** Questo commit cambia il senso di un artefatto di sintesi (`i2/`, `presentation/`) rispetto a nuovi input o a goal appena emersi? Se sì, il deck va _ri-derivato_ (`o3/build-presentation.sh`), non lasciato stale: è il presidio della fedeltà cognitiva (un'assunzione che cambia significato senza essere ri-valutata esplode più tardi).
- **i3 — il verdetto cambia?** Ciò che è cambiato altera il verdetto su un filo aperto rispetto agli obiettivi, o poggia su un'assunzione che merita di essere scritta? Se sì, è il momento di aggiornare il file-filo in `i3/` (punto 2). Il caso-tipo: un rename o un refactor che rompe un consumatore a valle — la domanda «va bene?» lo intercetta prima del commit. Se il verdetto cambia, chiedi anche: _si propaga a `o1/plan.md`/`o2/` (priorità, dipendenze, nuovi task — `/plan-review`), al register `goal.md` (fotografia da aggiornare) o al Goal stesso (filo di formazione-goal, non di verdetto su un goal noto)?_

Dopo aver risolto le pre-check (o averle saltate), procedi con il commit:

1. Esegui in parallelo per capire lo stato attuale:
   - `git status` per vedere i file modificati/non tracciati
   - `git diff` per vedere le modifiche non in staging
   - `git diff --cached` per vedere le modifiche in staging
   - `git log --oneline -5` per vedere lo stile dei commit recenti

2. Formatta i file modificati con gli strumenti disponibili:
   - Markdown: `prettier --write "**/*.md"`
   - Python: `ruff format o3/*.py` se ci sono script Python modificati

   Se un formatter non è disponibile, segnalalo e continua senza inventare alternative.

3. Fai lo staging dei file: usa `git add -u` per i file tracciati. Per i file non tracciati che appartengono chiaramente alla modifica, aggiungili individualmente per nome. Non usare `git add -A`.

4. Scrivi un messaggio di commit conciso:
   - Usa conventional commits: `type(scope): description`
   - Tipi comuni: `feat`, `fix`, `refactor`, `docs`, `chore`
   - Scope: area o nodo, es. `docs(kb)`, `docs(tasks)`, `refactor(root)`
   - Una riga, sotto i 72 caratteri
   - Focalizzato sul perché operativo della modifica

5. Crea il commit con il messaggio preparato:

   ```
   git commit -m "descrizione del commit"
   ```

6. Esegui `git status` per confermare che il commit sia andato a buon fine.

IMPORTANTE:

- NON usare `--no-verify`
- NON fare amend di commit esistenti salvo richiesta esplicita
- NON fare push salvo richiesta esplicita
- NON committare file con segreti (`.env`)
- NON aggiungere automaticamente trailer di attribuzione o coautoria riferiti a
  modelli, vendor o harness. Aggiungerli solo su richiesta esplicita dell'utente.
