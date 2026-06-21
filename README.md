# Cognizione condivisa

Framework metodologico e osservatorio cross-repo per il _cognitive artifact
design_: la progettazione di artefatti cognitivi che sostengono la cognizione
condivisa tra umano e modelli di intelligenza artificiale lungo l'intero ciclo
d'azione.

Questo repository ha due funzioni complementari. La prima è custodire il metodo
portabile: KB riflessiva, strati input/output, membrana `world`, struttura di
progetto, strumenti, principi guida e ciclo di lavoro. La seconda è osservare
come il metodo viene applicato nei progetti adottanti, confrontando artefatti,
componenti, strumenti, skill, nodi, task e segnali di salute.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale —
principi, anatomia dell'artefatto e ciclo operativo — mentre le
personalizzazioni sono esplicite: ogni progetto estende il metodo con Goal,
Mondo, fonti di verità, rappresentazioni e strumenti propri del dominio. Le
differenze tra progetti non sono rumore: sono materiale di analisi per capire
cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo del metodo procede per due movimenti in alternanza ([method-development](kb/method-development.md)). Dal basso, un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Dall'alto, una cornice teorica importata — un gigante, una distinzione — dà forma a ciò che dal basso si avverte come disagio ma non si sa ancora inquadrare. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione, non l'unica regola. Il dall'alto ha pari dignità su due fronti: importa le cornici teoriche che danno forma al metodo, e — sul lato runtime — pianifica il proprio output di canone, le prescrizioni e le convergenze che disegnano come gli artefatti adottanti dovrebbero diventare, che l'adottante poi recepisce eseguendole. Ciò che questo repo non fa è micromanagiare la coda interna degli adottanti: custodisce il metodo emerso dall'uso reale e le cornici che lo reggono, e prescrive il proprio canone senza sostituirsi alle loro code operative.

## Il dominio in breve

Il dominio di questo repo è il metodo stesso. Come meta-artefatto ha due facce del [world](kb/world.md): il Mondo runtime sono i progetti adottanti — da lì emerge dal basso l'esigenza e lì ritorna la propagazione — mentre il Mondo di sviluppo sono i nodi `kb/` e la loro coerenza, non codice o dati. Il metodo si inscrive in una cornice di augmentation ([augmentation-system](kb/augmentation-system.md), l'H-LAM/T di Engelbart) che _contiene_ i suoi riferimenti — [zettelkasten](kb/zettelkasten.md) (l'unità atomica), [action-cycle](kb/action-cycle.md) (l'interfaccia col Mondo), e [karpathy-pattern](kb/karpathy-pattern.md) come istanza contemporanea della gamba di manutenzione — e poggia su un'ontologia a tre piani: artefatto, sistema, metodo ([cognitive-artifact](kb/cognitive-artifact.md), [cognitive-system](kb/cognitive-system.md), col pavimento Hutchins/Clark). I principi guida vivono in [design-principles](kb/design-principles.md). Il modello completo e illustrato vive in [interpretations/metodo-in-sintesi.md](interpretations/metodo-in-sintesi.md); il dettaglio concettuale nei nodi. Questo README **orienta e punta**: non ripete né il modello né il catalogo.

## Metodo

Questo è il repository **canonico** del metodo: non lo adotta, lo custodisce. Il symlink `world/` (gitignorato) punta agli adottanti, duale del `method/` con cui ogni adottante legge i nodi qui; l'hub d'ingresso è [`cognitive-artifact-design.md`](kb/cognitive-artifact-design.md), il solo nome di nodo assunto stabile come punto d'aggancio. Questa è la **sezione README canonica** ([readme](kb/readme.md)) — comune ai cinque repo, con heading fissi e machine-readable da cui la home ricava i poli Goal e World.

### Goal

Il Goal di `metodo` è sdoppiato (cfr. [development-goal](kb/development-goal.md), [goal](kb/goal.md)): il Goal **runtime** è custodire il metodo portabile e propagarne il canone agli adottanti senza micromanagiarne la coda; il Goal di **sviluppo** è la posizione auspicata dell'artefatto-metodo lungo le dimensioni comuni — basso attrito di lettura, KB riflessiva coerente, loop di propagazione che si chiude.

### World

`metodo` ha due Mondi ([world](kb/world.md)). Il Mondo **runtime** sono i quattro adottanti, espliciti — da lì emerge l'esigenza dal basso e lì torna la propagazione:

- **[nixos](../nixos/)** — Configurazione dichiarativa NixOS multi-host
- **[bi](../bi/)** — Business intelligence e sincronizzazione dati
- **[economia](../economia/)** — Gestione finanziaria, patrimoniale e legale personale
- **[salute](../salute/)** — Benessere, pratica, filosofia e salute personale

Il Mondo di **sviluppo** sono i nodi `kb/` e la loro coerenza: un commit agisce sui nodi, lint e audit ne percepiscono la risposta. Le fonti autorevoli stanno fuori dall'artefatto, registrate in [`sources.md`](sources.md).

## Orientarsi

La root è l'atrio dell'artefatto: un `ls` ne dichiara l'anatomia. Tre specie di file più le collezioni, collocate per **gradiente di cardinalità** — unità al polo Goal (file in root), molteplicità al polo Mondo (cartelle) ([project-structure](kb/project-structure.md)).

**File-ciclo** — la triade alta del cruscotto, un'unica istanza aggiornata in place:

- **[README.md](README.md)** — il Goal: la bussola
- **[plan.md](plan.md)** — lo stadio Plan (o1-sviluppo): i task aperti, prioritizzati, con dipendenze
- **[verdict.md](verdict.md)** — lo stadio Compare (i3-sviluppo): il verdetto attuale e perché conta
- **CLAUDE.md** / **AGENTS.md** — le regole operative

**Cataloghi trasversali** — indicizzano una collezione che attraversa tutto il ciclo, perciò salgono in root:

- **[kb.md](kb.md)** — il catalogo di tutti i nodi (`kb/`, la system image)
- **[tools.md](tools.md)** — strumenti e skill dell'artefatto

**Register** — puntano _fuori_ dall'artefatto:

- **[sources.md](sources.md)** — registro di provenienza delle fonti-mondo autorevoli (`source-of-truth`), base dei `## Riferimenti` (i3); punta a `world`, non a una collezione interna

**Collezioni-stadio** — cartelle che accumulano, ciascuna con un indice interno omonimo:

- **[perceptions/](perceptions/perceptions.md)** — lo stadio i1 (Perceive): i segnali metodologici che emergono dagli adottanti
- **[interpretations/](interpretations/interpretations.md)** — lo stadio i2 (Interpret): le sintesi e il deck
- **[prescriptions/](prescriptions/prescriptions.md)** — lo stadio o3 (Prescrivi): i runbook di adozione del canone
- **tasks/** — lo stadio Specify: i dettagli dei task aperti, indicizzati da `plan.md`

Dove un dominio ha un territorio da indicizzare (host, entità, sistemi), una porta `map.md` lo mappa sui nodi; in `metodo` il dominio è astratto e non la richiede — il suo modello vive nei nodi e in `interpretations/`.

L'ordine di bootstrap è `README → CLAUDE → nodo`.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (o1/o2/o3) e input (i1/i2/i3), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro.
- **Strumenti comuni**: `tools/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura del catalogo, migrazione, candidati terminologici e segnali generici sui progetti code-based. La triade operativa — `/kb-review`, `/tasks-review`, `/commit` — e la skill di allineamento `/method-review` vivono in `.claude/skills/` (con wrapper Codex in `.codex/skills/`): `metodo` fa dogfooding ed è la copia canonica che gli adottanti forkano.
- **Manutenzione propria del metodo**: task in `tasks/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Interpretazioni**: [`interpretations/`](interpretations/interpretations.md) è la collezione dello stadio i2; [`interpretations/metodo-in-sintesi.md`](interpretations/metodo-in-sintesi.md) ne è la sintesi principale — i diagrammi che reggono il metodo intero, dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo dell'azione come specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al processo (anatomia, sviluppo, routing). Ogni sezione è un'interpretazione: rivela una tensione tra nodi altrimenti invisibile da dentro ciascuno. La sintesi vive qui, non nei nodi. Il `.md` è la fonte unica; `tools/build-presentation.sh` genera `interpretations/index.html`, l'indice navigabile della collezione, come deck Reveal.js standalone apribile direttamente dal checkout. Il PDF per stampa/distribuzione (o3) esce dall'export del deck e non viene versionato.

## Come collegare un nuovo progetto

I progetti adottanti sono il Mondo runtime, elencati sopra in **Metodo → World**.
Per collegarne uno nuovo:

1. Crea il symlink `method/` verso i nodi canonici: `ln -s ../method/kb method`
   dalla root del progetto, e aggiungilo al Mondo runtime (sezione **World**) e,
   se condiviso, al `world/` di `metodo`.
2. Scrivi la **sezione README canonica** ([readme](kb/readme.md)): `## Metodo`
   con la dichiarazione di adozione e il symlink `method/`, più `### Goal` e
   `### World` del dominio sotto heading fissi. È la dichiarazione _una-volta_
   della dipendenza generale dal metodo.
3. Aggancia il metodo all'hub
   [`cognitive-artifact-design.md`](kb/cognitive-artifact-design.md), unico nome
   di nodo assunto stabile, e aggiungi la sezione con i principi specifici del
   progetto. **Non** replicare in `CLAUDE.md` un inventario di path interni del
   metodo: collega un nodo solo dove una regola o uno strumento locale dipende
   davvero da quella specifica — dipendenza intenzionale, non accidentale (cfr.
   [method-development](kb/method-development.md), «Il confine canone↔adottante:
   dichiara e taci»).
4. Dichiara gli strati input/output e la membrana `world/` del dominio; crea il
   symlink host-local solo quando il progetto viene messo in uso.
