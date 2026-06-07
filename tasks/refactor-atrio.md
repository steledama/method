---
data: 2026-06-07
stato: aperto
---

# Refactor: la root come atrio (system image)

Runbook e **stato d'arrivo canonico** del ridisegno della root. Questo file è il modello che
i task locali dei repo adottanti citeranno; il modello vero, però, vive nei nodi aggiornati
(soprattutto [[struttura-progetto]]) e nell'entry `why.md` — condivisi per symlink. Qui sta la
procedura e la mappa d'impatto, non la teoria.

## Stato

- **`metodo` ✅ fatto** (commit `c66cf82`): rename, tooling, nodi, file-ciclo, why, audit pulito.
- **Propagazione ai figli — da fare**: aprire i task locali autonomi (sezione finale).

## Decisione (Filosofia B, con una condizione)

La root passa da **cruscotto del ciclo** (solo ciò che si legge ogni sessione) a **atrio /
system image**: ogni classe di componente ha la sua porta in root, così che un `ls` mostri
l'anatomia completa dell'artefatto senza leggere nulla. Fondamento Norman: la struttura di
directory *è* system image e deve portare il peso della comunicazione (`affordance-signifier`,
`system-image`) — non un documento che la spiega (il cartello «tirare»).

**Condizione irrinunciabile — visibilità ≠ caricamento.** "In root" non significa più "letto
al bootstrap". La root ha **due specie di file**:
- *file-ciclo* (letti ogni sessione): `README.md`, `map.md`, `plan.md`, `why.md`, `CLAUDE.md`,
  `AGENTS.md`;
- *porte-collezione* (visibili sempre, lette on-demand): `kb.md`, `tools.md`,
  `presentations.md`, `sources.md`.
L'ordine di bootstrap in `CLAUDE`/`AGENTS` è il signifier che dice *quali* porte aprire e
quando. Senza questa scissione, l'atrio gonfia silenziosamente il contesto.

`map.md` **resta separato** (qui e nei figli): niente fusione in README — vince la pace
(README = ingresso stabile, map = modello che evolve con la teoria).

## Stato d'arrivo della root

```
README.md  map.md  plan.md  why.md  CLAUDE.md  AGENTS.md   ← file-ciclo
kb.md  tools.md  presentations.md  sources.md              ← porte-collezione
kb/  tools/  presentations/  sources/  tasks/              ← collezioni
```

`plan.md` resta `plan` (non `tasks.md`): è lo stadio Plan del ciclo, non l'indice di `tasks/` —
eccezione semantica per altezza. È la prova che B *contiene* A come caso speciale.

## Operazioni ordinate

Ogni `git mv` va seguito dall'aggiornamento dei riferimenti (mappa sotto). Attenzione alla
**trappola del grep**: ispezionare, non sostituire alla cieca.

**1. `kb/index.md` → `kb.md` (catalogo in root).**
- `git mv kb/index.md kb.md`.
- Riferimenti da rivedere (distinguere catalogo `index` da nodo-concetto `indice`):
  CLAUDE.md, map.md, README.md, why.md, e i nodi kb/indice.md, kb/knowledge-base.md,
  kb/map.md, kb/metodo-kb.md, kb/pattern-karpathy.md, kb/readme.md, kb/strumenti-kb.md,
  kb/struttura-progetto.md, kb/zettelkasten.md, presentations/metodo-in-sintesi.md.
- I link *dentro* `kb/` verso il catalogo diventano `../kb.md`; il nodo-concetto resta
  `[indice](indice.md)`.

**2. `scripts/` → `tools/` + nuovo `tools.md`.**
- `git mv scripts tools` (porta `kb_tools.py`; `repo_root()=parents[1]` regge).
- Creare `tools.md`: indice di strumenti e skill dell'artefatto (oggi `kb_tools.py`; i comandi
  audit/backlinks/orphans/readme/migration/terms/inventory/coverage).
- Riferimenti: README.md, map.md, why.md, tasks/sostanza-why.md, e i nodi
  kb/confronto-progetti-adottanti.md, kb/metodo-kb.md, kb/pattern-karpathy.md, kb/skill.md,
  kb/strumenti-kb.md, kb/struttura-progetto.md.

**3. `presentation/` → `presentations/` + nuovo `presentations.md`.**
- `git mv presentation presentations`.
- Creare `presentations.md`: indice delle presentazioni (oggi `metodo-in-sintesi.md`).
  Niente atomizzazione delle slide ora: è scelta di tooling di authoring, rinviata.
- Riferimenti: README.md, map.md, why.md, sources/README.md (→ sources.md), e i nodi
  kb/artefatto-cognitivo.md, kb/confronto-progetti-adottanti.md, kb/metodo-kb.md,
  kb/output.md, kb/struttura-progetto.md.

**4. `sources/README.md` → `sources.md` (manifest in root).**
- `git mv sources/README.md sources.md`; la cartella `sources/` resta per i binari i1.
- `.gitignore`: `sources/*` resta; rimuovere l'eccezione `!sources/README.md` (non serve più).
- Correggere i **link rotti** del manifest (`../todo/ingest-norman.md`,
  `../todo/rifondazione-input-output.md` non esistono — `todo/` è ora `tasks/` e quei task
  sono stati eliminati): toglierli o ripuntarli a `why.md`.
- I riferimenti dei nodi a `sources/` (la cartella) **restano validi** — solo il manifest si
  sposta.

## Tooling — `tools/kb_tools.py`

- `CATALOG_NAME`/`catalog_path`: il catalogo ora è `root/kb.md`, fuori da `kb/`. Aggiornare la
  ricerca del catalogo (root come prima sede) mantenendo l'esclusione dal conteggio nodi.
- `markdown_report`: stringhe `kb/index.md` → `kb.md`.
- `FILE_META = {"index.md"}`: `kb.md` è in root, non in `DOC_DIRS`, quindi già fuori dal
  conteggio nodi; verificare che `doc_files` non lo raccolga.
- **Indici generati, non a mano** (così non mentono): aggiungere un comando che rigenera
  `kb.md` (e, se semplice, `tools.md`/`presentations.md` da `tools/` e `presentations/`).
  Priorità: la generazione di `kb.md`; gli altri due possono restare a mano in prima battuta.

## Nodi e regole

- **[[struttura-progetto]] — riscrittura canonica** (è il modello che i figli ereditano):
  - le **due specie di file root** (file-ciclo vs porte-collezione) sostituiscono la triade
    «file-meta dentro la cartella se on-demand»;
  - **visibilità ≠ caricamento**, con l'ordine di bootstrap come signifier;
  - indici come **porte generate dai tool**;
  - **`presentations` nome uniforme** + principio nuovo **«struttura uniforme, carattere nel
    contenuto»** (supera «il nome dello strato output è locale», riga 54, con `> ↳`);
  - skeleton aggiornato: `kb.md`, `tools/`+`tools.md`, `presentations/`+`presentations.md`,
    `sources.md`; sezione naming aggiornata.
- **[[indice]]** (nodo-concetto): il register è ora `root/kb.md`, il nodo resta in `kb/`.
- **[[strumenti-kb]]**, **[[skill]]**: `scripts/` → `tools/`.
- ritocchi di link in: knowledge-base, map, metodo-kb, pattern-karpathy, readme, zettelkasten
  (catalogo), confronto-progetti-adottanti, output, artefatto-cognitivo (presentations).

## why.md

- **Supera** l'entry [2026-06-06] «Il root è il cruscotto…» con `> ↳`: il catalogo torna in
  root come porta visibile; la regola «file-meta dentro la cartella se on-demand» è raffinata
  (i cataloghi on-demand possono stare in root come porte, con l'ordine di bootstrap a dire
  cosa leggere).
- **Nuova entry** (in cima al gruppo «Il cruscotto del ciclo di sviluppo»): l'atrio (B), il
  fondamento Norman (affordance/system-image vs economia di lettura), la scissione
  visibilità/caricamento, l'uniformità («carattere nel contenuto»), map separato, il modello
  di propagazione, il filone Clark come pavimento (rimando a [[fonti-mente-estesa]]), e la nota
  top-down→arricchimento di dominio (slide olistiche di salute).

## Verifica

- `python tools/kb_tools.py audit` → 0 link rotti, 0 orfani, catalogo a copertura piena.
- grep di residui stantii: `kb/index\.md`, `scripts/`, `presentation\b` (singolare),
  `sources/README`.
- commit del refactor separato dal commit di questo runbook.

## Propagazione ai figli (dopo il commit di metodo)

Da qui, stessa sessione: aprire in **ciascun** repo adottante un task locale **committato e
autonomo** (`tasks/adotta-atrio.md`) che (i) punta al commit canonico di `metodo` e al nodo
`struttura-progetto`, (ii) elenca i rename specifici di quel repo, (iii) si apre e si chiude
**lì**. Nessun write-back verso `metodo`; il task di `metodo` si chiude qui. I figli leggono il
canone via symlink, non riscrivono il canone.

Differenze locali note da versare nei task figli:
- **salute**: `quadro/` → `presentations/` — rimuove una contraddizione (il nome clinico
  contraddice l'essenza non-dualista corpo/mente della KB), non solo uniforma. Sezione di
  dominio da preservare nel task di salute (riconciliare con eventuale task esistente):
  > La presentazione non è il quadro *clinico* ma la sintesi olistica del vivere meglio. Ogni
  > slide tiene insieme dimensione corporea e mentale/esistenziale — mai una senza l'altra.
  > Mira a istruzioni pratiche e concrete per vivere meglio, non a una fotografia diagnostica.
  > Arricchimento: disegni personalizzati uno per slide (strato visceral/affettivo, cfr.
  > `visceral-behavioral-reflective`) per tenere l'umano nel loop.
- **bi**: attenzione — lì `scripts/` è output del runtime (o3), *non* strumenti. Il rename
  `scripts→tools` di `metodo` riguarda gli strumenti dell'artefatto; in `bi` `scripts/` resta
  com'è e semmai si introduce `tools/` separato se servono strumenti di manutenzione.
- **fonti**: dove un repo ha `fonti/`, valutare `sources/` + `sources.md` per uniformità.
