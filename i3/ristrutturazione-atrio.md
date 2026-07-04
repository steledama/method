---
ciclo: dev
---

# Ristrutturazione dell'atrio: la root diventa il ciclo

L'atrio è stato ristrutturato (2026-07-04): le collezioni-stadio portano il codice
del loro stadio — `i1/` Perceive, `i2/` Interpret, `i3/` Compare, `o1/` Plan,
`o2/` Specify, `o3/` Perform — e la root smette di _raccontare_ il ciclo per
_esserlo_. Le decisioni ratificate:

- **facet `ciclo: dev|runtime`** sul frontmatter di ogni item di collezione; il
  criterio è il Mondo su cui l'item insiste (artefatto → `dev`, adottanti →
  `runtime`). L'enforcement deterministico è il task
  `estensione-check-facet-cartelle-stadio`;
- **verdetto a fili-file**: `verdict.md` è scisso in un file per filo in `i3/`,
  indice `verdicts.md`; la disciplina (in place, filo chiuso = file rimosso)
  invariata;
- **`o1/` regna `plan.md`**, con la colonna `Ciclo` (l'asse `natura` resta
  parcheggiato, cfr. `home-16-slot.md`);
- **strumenti in `o3/`** come esecutori deterministici del ciclo di sviluppo,
  registrati in `prescriptions.md` («Strumenti»); `tools.md` soppresso;
- **`presentation/`** (ex `views/`) raccoglie l'intera superficie presentativa:
  home `index.html`, deck, viste, `assets/`;
- **catalogo `kb/kb.md`**, indice interno omonimo della collezione: la
  collisione temuta con un nodo non c'era (`index` documenta la funzione,
  `knowledge-base` il concetto).

Stato: il canone locale è tornato eseguibile. I tre file d'ingresso (`README`,
`CLAUDE`, `AGENTS`), gli indici di collezione, `index`, i nodi strutturali più
vicini alla rottura (`project-structure`, `plan`, `tasks`, `verdict`, `view`,
`kb-tools`), gli script in `o3/` e le skill operative sono riallineati ai nuovi
path. `kb_tools.py` riconosce `kb/kb.md`, verifica i task in `o2/` e presidia la
facet `ciclo: dev|runtime` sugli item delle collezioni-stadio; l'audit è tornato
pulito (49 nodi, 0 link rotti, 16 item `ciclo` validi) e le build di home/vista
passano su `presentation/`.

**Cocci ancora a terra**: i nodi meno centrali e il deck `i2/metodo-in-sintesi.md`
contengono ancora riferimenti storici o concettuali alla forma precedente
(`plan.md`, `verdict.md`, `tasks/`, `interpretations/`, `tools/`). Non bloccano gli
strumenti, ma vanno riletti con calma per distinguere riferimenti storici sani da
canone stantio. La **propagazione agli adottanti** resta il punto più delicato:
questa è la prima divergenza strutturale del canone dalla forma che i quattro
adottanti conoscono — path delle collezioni, nome del catalogo, casa degli
strumenti — e va progettata come prescrizione, non lasciata al drift.

Decisioni rinviate, deliberatamente: la sorte delle viste `tasks.html` /
`verdict.html` (candidate al taglio dopo lo split del verdetto); il mini-server
per `presentation/index.html` (rompe l'invariante `file://`, parcheggiato in
`home-16-slot.md`). Il filo si chiude quando il debito testuale residuo è ripulito
o esplicitamente classificato come storico e la propagazione agli adottanti è
almeno pianificata.
