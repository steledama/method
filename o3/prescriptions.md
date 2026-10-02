# Prescriptions

Indice della collezione `o3/`: lo **stadio o3** del ciclo, l'atto versionato e predisposto sul Mondo runtime. Il significato dello stadio vive nell'atomo [perform](../kb/perform.md). Il Mondo runtime di `method` sono gli adottanti: l'o3 di `method` è il **runbook di propagazione** — la ricetta, per repo, che porta un adottante al canone nuovo. Lo esegue il `method` dell'adottante: o3 prescrive, method compie l'atto ([action-cycle](../kb/action-cycle.md)). Una prescrizione nasce quando un segnale i1 ([perceptions](../i1/perceptions.md)) è stato valutato e ha prodotto un cambio di canone; resta finché tutti gli adottanti non l'hanno recepita. La fetta di skill che mantiene lo stadio è lo scope `perform` di [exec](../.claude/skills/exec/SKILL.md).

## Divisione del lavoro

`method` prescrive il canone **fino ai propri concetti**; l'adottante personalizza l'**ultimo miglio** contro il suo stato reale.

- qui vivono il _cosa_/_perché_ e la ricetta nel lessico del metodo, più i touchpoint per-repo che `method` già conosce — come **indizi da verificare in loco**, non ordini alla lettera;
- la mappatura sui file veri (path, nomi, struttura) la fa il `method` dell'adottante, che legge il repo aggiornato: è il checkpoint di [cognitive-fidelity](../kb/cognitive-fidelity.md) — il modello che `method` ha di un repo è una fotografia dell'osservatorio e può derivare, quindi non va pre-cotto dove il rappresentato cambia;
- una prescrizione si **personalizza per repo** (un file dedicato) solo quando l'applicazione diverge davvero tra adottanti; finché la differenza è solo _quali_ file esistono, un runbook unico con note per-repo basta.

## Contenuti

- [Ingresso di un adottante nell'osservatorio](ingresso-adottante.md) —
  verificare l'adozione locale, fissare una baseline con provenienza,
  aggiornare le rappresentazioni correnti e predisporre il primo giro senza
  governare la coda del nuovo repository.
- [Revisione coordinata del bootstrap di un
  adottante](revisione-bootstrap-adottante.md) — rileggere insieme README,
  CLAUDE, Goal e World; il canone fornisce criteri e indizi, il `/method`
  locale applica o motiva l'ultimo miglio di dominio.
- [Ogni giro di `eval` ed `exec` lascia l'esito per stadio nel
  commit](esiti-per-stadio-nel-commit.md) — trailer `Esiti:` con `materia` o
  `vuoto` per ogni stadio invocato, `--allow-empty` per i giri tutti vuoti; è
  la misura che la clausola di uscita della tripartizione non aveva. Da
  recepire prima del battito del 2026-11-01.
- [I builder della presentazione dichiarano il toolchain che
  assumono](toolchain-builder-presentazione.md) — `encoding="utf-8"` nelle
  chiamate a pandoc e URL di reveal.js derivato dalla versione di pandoc
  (6.0.2 da 3.12 in su, 5.1.0 sotto), con errore esplicito se non si legge;
  da `danea-auto`, che può tornare dal pin fisso alla regola.

Le prescrizioni recepite da tutti gli adottanti escono dall'indice: la
loro storia è in git.

## Strumenti

Gli **esecutori deterministici** del ciclo di sviluppo (`ciclo: dev`): agiscono
sull'artefatto, non sul Mondo runtime — l'omologo runtime negli adottanti
code-based sono gli `scripts/` di dominio. Vivono qui in `o3/` perché il Perform
è il loro stadio: prescrizioni eseguibili invece che narrative.

- `kb_tools.py` — backend portabile per l'audit della KB. Comandi: `audit`,
  `backlinks <nodo>`, `orphans`, `readme`, `migration`, `terms`, `facets`,
  `tasks`, `inventory` / `coverage`. Il report di `audit` è una diagnosi i1 su
  stdout.
- `kb_profile.py --root .` — profilo quantitativo comune e manifest di
  `kb/`: dimensioni, maturità, esclusioni e impronte dei nodi; esce con codice
  1 per stati/frontmatter invalidi, 2 per corpus non leggibile. Non verifica
  fatti o fonti. Test: `python3 -m unittest discover -s tests -p 'test_kb_profile.py'`.
- `presentation/` — i builder della presentazione, con lo stesso path in ogni
  repo (canone, cfr. [presentation](../kb/presentation.md)):
  - `build.py` — **unico entrypoint**: `python3 o3/presentation/build.py`
    rigenera viste Reveal, liste, home e asset, formatta con Prettier e
    chiude col presidio del compartimento stagno (nessun URL emesso esce da
    `../presentation/`). È Python per girare anche sugli host Windows;
  - `project.py` — l'unico file che il fork parametrizza: sigla e lingua dei
    titoli, colore d'accento (scritto in `assets/theme.css`), sorgente del
    deck delle Interpretazioni;
  - `sources.py` — libreria condivisa: parsing di plan, task e register,
    titoli con sigla, chiusura dei link sull'AST di Pandoc; non si invoca
    direttamente;
  - `build_views.py` — le sorgenti Markdown delle viste Reveal `tasks` (con
    la legenda interna degli obiettivi e, in una slide, tutto ciò che nel plan
    segue la tabella: legenda delle dipendenze, risvegli, scadenze; le chiavi
    `p<n>`/`w<n>` della colonna Dip. vi puntano e senza voce rompono) e
    `verdict` (indice Ciclo · Ob. · Filo nell'ordine di `../i3/verdicts.md`,
    poi un filo per slide; contratto i3 × goal: ogni file indicizzato, ogni
    voce col suo file, `obiettivo:` verificato contro `../goal.md`);
  - `build_lists.py` — le due viste a elenco `prescriptions.html` e
    `perceptions.html`: l'intero indice reso con Pandoc, nell'ordine e con la
    struttura della fonte; i link alle fonti restano etichetta. Regressioni:
    `python3 -m unittest discover -s tests -p 'test_build_lists.py'`;
  - `serve.py` — serve la sola `../presentation/` sulla LAN, su richiesta:
    `python3 o3/presentation/serve.py`, porta 8765, Ctrl-C per chiudere;
    solo libreria standard, niente dotfile né elenchi di cartella;
  - `build_system_image.py` — la home statica minimalista: ciclo singolo,
    un collegamento primario per slot; il CSS condiviso della home resta
    potato alle classi che il builder emette.

Ogni sezione delle viste generate ha una sorgente canonica; i generatori
verificano i contratti fra sorgenti ([view](../kb/view.md)):

- `../presentation/interpretations.html` ← `../i2/metodo-in-sintesi.md`, con le tavole copiate da `../i2/`;
- `../presentation/tasks.html` ← `../o1/plan.md` e i file in `../o2/`;
- `../presentation/verdict.html` ← i fili in `../i3/`;
- `../presentation/prescriptions.html` ← l'intero indice
  `prescriptions.md` (questo file);
- `../presentation/perceptions.html` ← l'intero indice
  `../i1/perceptions.md`;
- `../presentation/index.html` ← titolo di `../README.md`, intro dei register
  `../goal.md` e `../world.md`, configurazione degli slot; le collezioni-stadio
  le _collega_, non le rende.

I path interni sono riallineati alla struttura `o3/` + `presentation/` +
`o1/plan.md`; `presentation/build.py` e
`kb_tools.py audit` sono il controllo minimo dopo modifiche strutturali.
