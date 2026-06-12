# Artefatti di cognizione condivisa tra uomo e modelli di intelligenza artificiale

Framework metodologico e osservatorio cross-repo per knowledge base personali e professionali mantenute con LLM.

Questo repository ha due funzioni complementari. La prima è custodire il metodo portabile: forma dei nodi, struttura di progetto, strumenti di manutenzione, principi guida e ciclo di lavoro. La seconda è osservare come il metodo viene applicato nei progetti adottanti, confrontando componenti, strumenti, skill, nodi, task e segnali di salute delle KB.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale — principi, struttura KB, ciclo operativo — mentre le personalizzazioni sono esplicite: ogni progetto estende il metodo con principi, fonti di verità e strumenti propri del dominio. Le differenze tra progetti non sono rumore: sono materiale di analisi per capire cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo del metodo procede per due movimenti in alternanza ([sviluppo-metodo](kb/sviluppo-metodo.md)). Dal basso, un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Dall'alto, una cornice teorica importata — un gigante, una distinzione — dà forma a ciò che dal basso si avverte come disagio ma non si sa ancora inquadrare. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione, non l'unica regola. Questo repo non orchestra task sui progetti adottanti; custodisce il metodo emerso dall'uso reale e le cornici che lo reggono.

## Il dominio in breve

Il dominio di questo repo è il metodo stesso. Come meta-artefatto ha due [mondi](kb/mondo.md): il Mondo runtime sono i progetti adottanti — da lì emerge dal basso l'esigenza e lì ritorna la propagazione — mentre il Mondo di sviluppo sono i nodi `kb/` e la loro coerenza, non codice o dati. Il metodo poggia su tre giganti — [zettelkasten](kb/zettelkasten.md), [pattern-karpathy](kb/pattern-karpathy.md), [ciclo-azione](kb/ciclo-azione.md) — e su un'ontologia a tre piani: artefatto, sistema, metodo ([artefatto-cognitivo](kb/artefatto-cognitivo.md), [sistema-cognitivo](kb/sistema-cognitivo.md)). I principi guida vivono in [design-principles](kb/design-principles.md). Il modello completo e illustrato vive in [presentations/metodo-in-sintesi.md](presentations/metodo-in-sintesi.md); il dettaglio concettuale nei nodi. Questo README **orienta e punta**: non ripete né il modello né il catalogo.

## Orientarsi

La root è l'atrio dell'artefatto: un `ls` ne dichiara l'anatomia. Due specie di file ([struttura-progetto](kb/struttura-progetto.md)).

**File-ciclo** — il cruscotto del lavoro:

- **[plan.md](plan.md)** — lo stadio Plan: i task aperti, prioritizzati, con dipendenze
- **[why.md](why.md)** — la memoria interpretativa: perché le decisioni contano
- **CLAUDE.md** / **AGENTS.md** — le regole operative

**Porte-collezione** — viste nell'atrio, aperte on-demand:

- **[kb.md](kb.md)** — il catalogo di tutti i nodi
- **[tools.md](tools.md)** — strumenti e skill dell'artefatto
- **[presentations.md](presentations.md)** — lo strato output o2/o3
- **[sources.md](sources.md)** — il manifest delle fonti i1

Dove un dominio ha un territorio da indicizzare (host, entità, sistemi), una porta `map.md` lo mappa sui nodi; in `metodo` il dominio è astratto e non la richiede — il suo modello vive nei nodi e in `presentations/`.

L'ordine di bootstrap è `README → CLAUDE → nodo`.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (o1/o2/o3) e input (i1/i2/i3), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro.
- **Strumenti comuni**: `tools/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura del catalogo, migrazione, candidati terminologici e segnali generici sui progetti code-based. La triade base di skill — `/audit-kb`, `/tasks-review`, `/commit` — vive in `.claude/skills/` (con wrapper Codex in `.codex/skills/`): `metodo` fa dogfooding ed è la copia canonica che gli adottanti forkano.
- **Manutenzione propria del metodo**: task in `tasks/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Strato output**: [`presentations.md`](presentations.md) è la porta verso lo strato o2/o3; [`presentations/metodo-in-sintesi.md`](presentations/metodo-in-sintesi.md) ne è la sintesi — i diagrammi che reggono il metodo intero, dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo dell'azione come specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al processo (anatomia, sviluppo, routing). La sintesi vive qui, non nei nodi. Il `.md` è la fonte unica; `presentations/index.html` lo rende come deck Reveal.js (da CDN, diagrammi Mermaid inclusi) servendo la cartella, e il PDF per stampa/distribuzione (o3) esce dall'export del deck — non più da `md2pdf` — e non viene versionato.

## Progetti adottanti

- **[nixos](../nixos/)** — Configurazione dichiarativa NixOS multi-host
- **[bi](../bi/)** — Business intelligence e sincronizzazione dati
- **[economia](../economia/)** — Gestione finanziaria, patrimoniale e legale personale
- **[salute](../salute/)** — Benessere, pratica, filosofia e salute personale

## Come collegare un nuovo progetto

1. Crea il symlink: `ln -s ../metodo/kb metodo` dalla root del progetto.
2. Aggiungi una voce all'elenco dei progetti adottanti.
3. Nel README del progetto, referenzia `metodo/metodo-kb.md` come nodo centrale del metodo e aggiungi una sezione con i principi specifici del progetto.
4. Aggiorna i path in `CLAUDE.md` del progetto: `kb/metodo-kb.md` → `metodo/metodo-kb.md` (e analogamente per gli altri nodi metodologici).
