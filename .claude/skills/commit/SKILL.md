---
description: Crea un git commit seguendo le convenzioni del repo metodo
user-invocable: true
---

Crea un git commit seguendo le convenzioni del progetto. Questa è la copia
canonica della skill: gli adottanti la forkano e la parametrizzano sui propri
formatter e fonti di verità.

## Pre-commit: domande da fare prima di procedere

**1. Audit KB** — Valuta se le modifiche toccano un numero significativo di nodi in `kb/` (aggiunte, rinominamenti, ristrutturazioni di link). Se sì, chiedi all'utente: _"Vuoi eseguire /audit-kb prima del commit?"_. Se l'utente risponde sì, esegui la skill `audit-kb` e includi eventuali fix nel commit. Se le modifiche sono minori (un file, fix puntuale), salta la domanda.

**1b. Formato nodo** — Per ogni nodo nuovo o pesantemente modificato in `kb/`: verifica che abbia (a) frontmatter con `data:` e `stato:` in cima e (b) sezione `Connessioni:` in fondo. Se mancano entrambi, segnalalo prima di committare.

**1c. Portabilità del nodo** — Per ogni nodo nuovo in `kb/`: verifica che sia metodologico e applicabile ad almeno due progetti diversi. Un concetto specifico di un singolo dominio non appartiene alla `kb/` del `metodo`.

**1d. Propagazione** — Se un nodo è stato rinominato o spostato, ricorda che i link nei `CLAUDE.md` e `README.md` degli adottanti collegati vanno aggiornati a mano (i nodi arrivano via symlink, ma nome/path no).

**2. Entry in why.md** — Valuta se la sessione ha prodotto qualcosa di significativo: nuovi nodi, cluster nuovi, decisioni strutturali o metodologiche, ingest di fonti, cambiamenti di approccio. Se sì, chiedi all'utente: _"Vuoi aggiungere un'entry in why.md per questa sessione?"_. Se sì, proponi un'entry nel formato canonico di `why.md` (raggruppata per motivazione, `### [YYYY-MM-DD] titolo-tesi` con 1-3 righe sul perché conta — non un elenco di file ma il significato del cambiamento). Se le modifiche sono di manutenzione (formatting, fix link, task completati), salta la domanda.

Dopo aver risolto le pre-check (o averle saltate), procedi con il commit:

1. Esegui in parallelo per capire lo stato attuale:
   - `git status` per vedere i file modificati/non tracciati
   - `git diff` per vedere le modifiche non in staging
   - `git diff --cached` per vedere le modifiche in staging
   - `git log --oneline -5` per vedere lo stile dei commit recenti

2. Formatta i file modificati con gli strumenti disponibili:
   - Markdown: `prettier --write "**/*.md"`
   - Python: `ruff format tools/*.py` se ci sono script Python modificati

   Se un formatter non è disponibile, segnalalo e continua senza inventare alternative.

3. Fai lo staging dei file: usa `git add -u` per i file tracciati. Per i file non tracciati che appartengono chiaramente alla modifica, aggiungili individualmente per nome. Non usare `git add -A`.

4. Scrivi un messaggio di commit conciso:
   - Usa conventional commits: `type(scope): description`
   - Tipi comuni: `feat`, `fix`, `refactor`, `docs`, `chore`
   - Scope: area o nodo, es. `docs(kb)`, `docs(tasks)`, `refactor(root)`
   - Una riga, sotto i 72 caratteri
   - Focalizzato sul perché operativo della modifica

5. Crea il commit con HEREDOC:

   ```
   git commit -m "$(cat <<'EOF'
   descrizione del commit

   Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
   EOF
   )"
   ```

6. Esegui `git status` per confermare che il commit sia andato a buon fine.

IMPORTANTE:

- NON usare `--no-verify`
- NON fare amend di commit esistenti salvo richiesta esplicita
- NON fare push salvo richiesta esplicita
- NON committare file con segreti (`.env`)
