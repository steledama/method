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

Stato: i tre file d'ingresso (`README`, `CLAUDE`, `AGENTS`), gli indici di
collezione e il nodo `index` sono riallineati. **Cocci ancora a terra**, in
ordine: i nodi strutturali di `kb/` (`project-structure` racconta ancora il
gradiente di cardinalità con plan/verdict in root; `plan` non conosce la colonna
`Ciclo`; `verdict` descrive il file monolitico; `view` e `kb-tools` hanno path
vecchi); i path interni degli strumenti in `o3/` (cercano `tools/`, `views/`,
`plan.md` in root) con la rigenerazione di home e viste; le skill in
`.claude/skills/` che invocano `tools/kb_tools.py`. Fino alla riparazione degli
strumenti, `/kb-review` e i build non sono affidabili.

Decisioni rinviate, deliberatamente: la sorte delle viste `tasks.html` /
`verdict.html` (candidate al taglio dopo lo split del verdetto); il mini-server
per `presentation/index.html` (rompe l'invariante `file://`, parcheggiato in
`home-16-slot.md`). La **propagazione agli adottanti** è il punto più delicato:
questa è la prima divergenza strutturale del canone dalla forma che i quattro
adottanti conoscono — path delle collezioni, nome del catalogo, casa degli
strumenti — e va progettata come prescrizione, non lasciata al drift. Il filo si
chiude quando nodi, strumenti e skill sono riallineati e la propagazione è
almeno pianificata.
