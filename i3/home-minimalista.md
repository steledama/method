---
ciclo: dev
---

# Home minimalista: la lente dev/runtime rimandata a filtri nelle viste

La home è stata semplificata (74df440, 2026-07-05): ciclo singolo, un solo
collegamento primario per slot, niente switch dev/runtime. Decisione ratificata:
in questa fase la home resta **minimalista**, pura affordance di navigazione; la
lente dev/runtime, quando servirà, entrerà **a valle come filtro nelle singole
viste** (es. tasks o plan: mostra solo il ciclo filtrato oppure tutti) — non
pianificata, deliberatamente rimandata all'uso reale.

Code chiuse dal giro di semplificazione:

- **Tensione con `action-cycle-matrix`**: risolta nella prima delle due vie che
  questo filo poneva — la home è solo affordance di navigazione; la matrice a
  16 celle e la scala a cinque valori restano lo strumento analitico del nodo
  (il suo paragrafo presentativo è aggiornato di conseguenza).
- **Sorte delle viste `tasks.html`/`verdict.html`** (ereditata dal filo
  ristrutturazione-atrio): tenute, uniformate a deck (74df440); saranno la sede
  naturale del futuro filtro dev/runtime.
- **Propagazione del motore della home**: col motore ridotto a ciclo singolo e
  CONFIG minimale il fork è banale; viaggia nella prescrizione dell'atrio
  (`o2/propagazione-atrio-adottanti.md`).

Watchpoint: le tavole della vista Interpretazioni sono **asset raster statici**,
non diagrammi derivati dalla sorgente — se un nodo cambia il senso di una tavola,
la rigenerazione è un atto manuale/creativo, non di build; presidiato solo dal
check i2 di `/commit` (i residui cosmetici stanno in
`o2/redraw-tavole-interpretazioni.md`).

Fili parcheggiati dello stesso fronte: dei due assi ortogonali di `plan` — ciclo
(sviluppo/runtime) × natura (metodologico/merito) — la colonna `Ciclo` è incisa
(2026-07-04, con la facet `ciclo:` sugli item di collezione); resta parcheggiata
`natura`. L'omologia tools=o3-sviluppo / scripts=o3-runtime / skill=prescrizioni
narrative è promulgata in `o3/prescriptions.md` («Strumenti»); l'eventuale
uniformità totale degli indici col suo costo (rinomina del nodo `index`, split
del catalogo `tools`). Fuori orizzonte, deliberatamente: i task come slide
navigabili, la finestra-terminale per dialogare col modello e il mini-server che
serva `presentation/index.html` (entrambi rompono l'invariante `file://`,
saranno classe e nodo a sé).
