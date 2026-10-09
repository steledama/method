---
description: Crea un git commit seguendo le convenzioni del repo metodo
user-invocable: true
---

Crea un git commit seguendo le convenzioni del progetto. Questa è la copia
canonica della skill: gli adottanti la forkano e la parametrizzano sui propri
formatter e fonti di verità.

## Pre-commit: controlli e confini della delega

Leggi `autonomy.md`, richiesta corrente e autorizzazioni operative. I controlli
necessari e gli aggiornamenti pertinenti già delegati si eseguono senza una
nuova conferma. Chiedi solo per cambi di scopi, territorio o delega, atti non
autorizzati o incertezze decisive non risolvibili dalle fonti. Un punto
sospeso non blocca modifiche indipendenti e verificabili.

**1. Audit KB** — Se le modifiche toccano un numero significativo di nodi
(aggiunte, rinominamenti, ristrutturazioni), esegui `python3 o3/kb_tools.py audit`
e risolvi i problemi pertinenti entro il mandato. Per modifiche minori scegli
i controlli appropriati. Non avviare implicitamente `kb review`, revisione
semantica profonda separata dal gate ordinario.

**1b. Formato nodo** — Per ogni nodo nuovo o pesantemente modificato in `kb/`: verifica che abbia (a) frontmatter con `stato:` in cima e (b) sezione `Connessioni:` in fondo. Se mancano entrambi, segnalalo prima di committare.

**1c. Portabilità del nodo** — Per ogni nodo nuovo in `kb/`: verifica che sia metodologico e applicabile ad almeno due progetti diversi. Un concetto specifico di un singolo dominio non appartiene alla `kb/` del `metodo`.

**1d. Propagazione** — Se un nodo è stato rinominato o spostato, verifica le connessioni intenzionali effettivamente coinvolte, senza ricostruire inventari dei path canonici. Il recepimento avviene nel repository adottante con il suo `/method`; qui si rende leggibile il cambiamento di canone (`kb/method-development.md`).

**2. Filo in i3/** — Se la modifica cambia un verdetto, aggiorna in place
il filo pertinente entro la delega vigente: stato corrente e motivo, non log.
Crea un filo solo per una tensione viva contro un obiettivo. Se si chiude,
rimuovi file e voce d'indice dopo aver conservato eventuali presidi di ipotesi;
i cursori e i contratti correnti restano. Chiedi al custode solo quando la
modifica supera il confine della delega. La semplice manutenzione non richiede
un aggiornamento rituale del filo.

**3. I due check del ciclo di valutazione (i2/i3)** — Verifiche da eseguire; eventuali decisioni seguono il confine della delega.

- **i2 — le viste sono ancora vere?** Non è una domanda di giudizio: esegui la verifica della build, uguale in ogni repo (`python3 o3/view/build.py --check`). Contratti fra le fonti e presidio del compartimento stagno devono passare; un errore si corregge nelle fonti prima del commit. L'output non entra nel commit: `view/` è ignorata da git e la vista pubblicata la ricostruisce l'host dal commit (cfr. `kb/view.md`, «Freschezza»). Il giudizio resta solo su ciò che la build non copre: un artefatto di sintesi (`i2/`) il cui _significato_ è cambiato va ripensato, non solo ri-derivato — è il presidio della fedeltà cognitiva (un'assunzione che cambia significato senza essere ri-valutata esplode più tardi).
- **i3 — il verdetto cambia?** Ciò che è cambiato altera il verdetto su un filo aperto rispetto agli obiettivi, o poggia su un'assunzione che merita di essere scritta? Se sì, è il momento di aggiornare il file-filo in `i3/` (punto 2). Il caso-tipo: un rename o un refactor che rompe un consumatore a valle — la domanda «va bene?» lo intercetta prima del commit. Se il verdetto cambia, verifica anche: _si propaga a `o1/plan.md`/`o2/` (priorità, dipendenze, nuovi task — `/exec plan`), ai puntatori ai segnali di `goal.md` (copertura da mantenere, senza ricopiare lo stato) o al Goal stesso (filo di formazione-goal, non di verdetto su un goal noto)?_

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

   Eccezione: se il commit chiude un giro di `eval` o `exec`, aggiungi dopo
   la riga il trailer `Esiti:` con una parola per stadio invocato (`materia` o
   `vuoto`). Un giro senza file cambiati si committa comunque, con
   `--allow-empty` (cfr. `kb/skill.md`).

   Ogni commit dichiara chi l'ha deciso (cfr. `kb/consent.md`, consenso
   differito):

   - `Autonomia: concordato` se il custode ha deciso o ratificato la modifica
     concreta, anche lasciandone esplicitamente il modo all'agente;
     `Autonomia: agente` se l'ha decisa l'agente entro una delega,
     anche col custode presente in chat. L'avvio del ciclo non ratifica in
     anticipo le sue decisioni. Nei commit misti separa le decisioni quando
     possibile; altrimenti usa `agente` e dichiara i motivi pertinenti. Un commit senza
     il trailer, come quelli storici, si legge `concordato`;
   - solo con `Autonomia: agente`, `Impatto: basso|medio|alto` e almeno un
     `Impatto-motivo:` che dice cosa ha determinato il livello: il criterio
     del register e il file o la sezione che l'ha fatto scattare, oppure
     `giudizio:` seguito dalla ragione quando l'agente ha alzato il livello.
     Il giudizio alza, non abbassa. Con più motivi si ripete il trailer e
     vale il livello più alto. Un commit `alto` porta la proposta, non
     l'atto: il messaggio nomina il file dove vive.

   Tutti i trailer stanno nell'**ultimo paragrafo** del messaggio, insieme:
   una riga vuota fra loro li nasconde a `%(trailers)`.

5. Crea il commit con il messaggio preparato:

   ```
   git commit -m "descrizione del commit" -m "Autonomia: concordato"
   git commit -m "descrizione del giro" -m "Esiti: perceive=vuoto interpret=materia compare=materia
   Autonomia: agente
   Impatto: medio
   Impatto-motivo: ciclo-delegato (autonomy.md, verdetto corretto su fonte verificata)"
   ```

6. Esegui `git status` per confermare che il commit sia andato a buon fine.

7. Esegui `git push` del branch corrente su `origin` (autorizzato dal custode
   il 2026-10-08, `CLAUDE.md` «Push remoto») e riporta SHA ed esito. Se il
   push è rifiutato non forzarlo: fermati e riferisci.

IMPORTANTE:

- NON usare `--no-verify`
- NON fare amend di commit esistenti salvo richiesta esplicita
- NON fare `push --force` né push di altri branch salvo richiesta esplicita
- NON committare file con segreti (`.env`)
- NON aggiungere automaticamente trailer di attribuzione o coautoria riferiti a
  modelli, vendor o harness. Aggiungerli solo su richiesta esplicita dell'utente.
