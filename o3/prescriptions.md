# Prescriptions

Indice della collezione `o3/`: lo **stadio o3** del ciclo, l'atto versionato e predisposto sul Mondo runtime. Il significato dello stadio vive nell'atomo [perform](../kb/perform.md). Il Mondo runtime di `method` sono gli adottanti: l'o3 di `method` è il **runbook di propagazione** — la ricetta, per repo, che porta un adottante al canone nuovo. Lo esegue il `method-review` dell'adottante: o3 prescrive, method-review compie l'atto ([action-cycle](../kb/action-cycle.md)). Una prescrizione nasce quando un segnale i1 ([perceptions](../i1/perceptions.md)) è stato valutato e ha prodotto un cambio di canone; resta finché tutti gli adottanti non l'hanno recepita.

## Divisione del lavoro

`method` prescrive il canone **fino ai propri concetti**; l'adottante personalizza l'**ultimo miglio** contro il suo stato reale.

- qui vivono il _cosa_/_perché_ e la ricetta nel lessico del metodo, più i touchpoint per-repo che `method` già conosce — come **indizi da verificare in loco**, non ordini alla lettera;
- la mappatura sui file veri (path, nomi, struttura) la fa il `method-review` dell'adottante, che legge il repo aggiornato: è il checkpoint di [cognitive-fidelity](../kb/cognitive-fidelity.md) — il modello che `method` ha di un repo è una fotografia dell'osservatorio e può derivare, quindi non va pre-cotto dove il rappresentato cambia;
- una prescrizione si **personalizza per repo** (un file dedicato) solo quando l'applicazione diverge davvero tra adottanti; finché la differenza è solo _quali_ file esistono, un runbook unico con note per-repo basta.

## Contenuti

- [poli-register.md](poli-register.md) — porta gli adottanti ai **poli-register**
  (`goal.md` gemello di `world.md`, che assorbe `map.md` e `sources.md`), al
  README-bussola con la sezione canonica asciugata, alla home che rende l'intro
  dei register e al **quartetto di review** (`plan-review`, `verdicts-review`);
  passo-cuore il register `goal.md` col custode umano. Pilot `economia` (il
  banco più severo: la bonifica del plan è il collaudo della coppia) —
  recepimento tracciato in `o2/propagazione-poli-register.md`.

L'ultima chiusa è `ristrutturazione-atrio` (collezioni-stadio `i1/`–`o3/`,
catalogo `kb/kb.md`, verdetto a fili, `presentation/`, facet `ciclo`, col
passo-cuore dell'**inventario dell'atrio**; pilot `nixos` 2026-07-05, recepita
dai quattro il 2026-07-11 con la chiusura di `bi`, validata dal suo run
notturno di produzione). Prima di lei `disaccoppiamento-adottanti`
(2026-06-21). La storia resta in Git.

## Strumenti

Gli **esecutori deterministici** del ciclo di sviluppo (`ciclo: dev`): agiscono
sull'artefatto, non sul Mondo runtime — l'omologo runtime negli adottanti
code-based sono gli `scripts/` di dominio. Vivono qui in `o3/` perché il Perform
è il loro stadio: prescrizioni eseguibili invece che narrative.

- `kb_tools.py` — backend portabile per l'audit della KB. Comandi: `audit`,
  `backlinks <nodo>`, `orphans`, `readme`, `migration`, `terms`, `facets`,
  `inventory` / `coverage`. Il report di `audit` è una diagnosi i1 su stdout.
- `presentation.py` — libreria di parsing condivisa (frontmatter, plan, task);
  importata dai due generatori, non si invoca direttamente.
- `build_views.py` — genera le sorgenti markdown derivate per le viste Reveal.
- `build-presentation.sh` — orchestra Pandoc + `build_views.py`: produce le
  viste in `../presentation/`.
- `build_system_image.py` — genera la home statica minimalista: ciclo singolo,
  un collegamento primario per slot; il CSS condiviso della home resta potato
  alle classi che il builder emette.
- `build-system-image.sh` — wrapper: genera e formatta la home.

I path interni sono riallineati alla struttura `o3/` + `presentation/` +
`o1/plan.md`; `build-presentation.sh`, `build-system-image.sh` e
`kb_tools.py audit` sono il controllo minimo dopo modifiche strutturali.
