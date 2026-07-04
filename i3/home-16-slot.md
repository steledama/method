---
ciclo: dev
---

# La home a 16 slot: tensione con `action-cycle-matrix` e propagazione aperta

Il cluster di presentazione è esaurito (deck→`view`, `presentation/assets/`+viste in `presentation/`
materializzati, home rifatta 2026-06-30 come matrice annidata a 16 slot con switch
dev/runtime; motore condiviso in `o3/build_system_image.py`, gli adottanti forkano
la sola CONFIG). Il deck è stato ri-fondato (2026-07-04) su cinque tavole sketchnote
più poche slide d'appoggio a elenchi: la sintesi ricca è uscita dalla sorgente (vive
nei nodi), l'o2 raggiunge finalmente il viscerale — ma le tavole sono **asset raster
statici**, non più diagrammi derivati dalla sorgente: se un nodo cambia il senso di
una tavola, la rigenerazione è un atto manuale/creativo, non di build. Nuovo punto di
possibile stale, presidiato solo dal check i2 di `/commit`. Due code aperte:

- **Tensione col nodo `action-cycle-matrix`**: il nodo tiene il frame a 16 celle come
  dogfooding di solo `metodo` (adottanti al ciclo singolo) e una scala a cinque valori
  col «vuoto legittimamente assente»; la home adotta invece il frame a 16 per tutti e
  una regola **binaria** acceso/dimesso che non rende la scala analitica. Da
  riconciliare: o la home è solo affordance di navigazione (la scala resta lo
  strumento del nodo, distinto), oppure la scelta «16 per tutti» risale nel nodo.
- **Propagazione agli adottanti** (forkare motore + CONFIG): canale o3-runtime, non
  ancora pianificato.

Fili parcheggiati dello stesso fronte: dei due assi ortogonali di `plan` — ciclo
(sviluppo/runtime) × natura (metodologico/merito) — la colonna `Ciclo` è incisa
(2026-07-04, con la facet `ciclo:` sugli item di collezione); resta parcheggiata
`natura`. L'omologia tools=o3-sviluppo / scripts=o3-runtime / skill=prescrizioni
narrative è promulgata in `o3/prescriptions.md` («Strumenti»);
l'eventuale uniformità totale degli indici col suo costo (rinomina del nodo `index`,
split del catalogo `tools`). Fuori orizzonte, deliberatamente: i task come slide
navigabili, la finestra-terminale per dialogare col modello e il mini-server che
serva `presentation/index.html` (entrambi rompono l'invariante `file://`, saranno
classe e nodo a sé). Il gap **runtime-o1** — il protocollo d'audit
periodico top-down — è un task in `o1/plan.md`, non più un TODO di questo filo.
