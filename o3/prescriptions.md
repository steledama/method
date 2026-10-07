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
  la misura che la clausola di uscita della tripartizione non aveva.
  Recepita dai sei e da `baserow` all'ingresso; resta attiva fino al conteggio del 2026-11-01.
- [Le viste escono in `view/`, il deck curato in
  `presentation/`](migrazione-viste.md) — recepita dai sei; restano la
  rimozione della forma vecchia del servizio in `nixos` e `danea-auto`.
- [Presidio delle ipotesi in attesa](presidio-ipotesi.md) — orizzonte,
  riscontro con fonte e raggiungibilità da `eval` dove manca il presidio;
  recepita da sei, seguito sul deck di `nixos` chiuso; resta `danea-auto`.

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
- `view/` — i builder delle viste, con lo stesso path in ogni repo (canone,
  cfr. [view](../kb/view.md)):
  - `build.py` — **unico entrypoint**: `python3 o3/view/build.py` verifica i
    contratti fra le fonti, rigenera pagine, deck, home e asset in `../view/`,
    rimuove ciò che non produce più, formatta con Prettier e chiude col
    presidio del compartimento stagno (nessun URL emesso esce da `../view/`).
    Costruisce in una cartella temporanea e tocca `../view/` solo a esito
    riuscito; `--check` verifica senza scrivere, `--publish DIR` pubblica da
    un commit pulito. È Python per girare anche sugli host Windows;
  - `publish.py` — la pubblicazione da commit pulito chiamata da
    `build.py --publish`: fonti esportate con `git archive`, una cartella
    per versione, puntatore `current` scambiato solo a build riuscita,
    `status.json` con l'ultimo tentativo, lock col PID e richiesta accodata.
    Test: `python3 -m unittest discover -s tests -p 'test_publish.py'`;
  - `project.py` — l'unico file che il fork parametrizza: sigla, lingua,
    colore d'accento (scritto in `view/assets/theme.css`), sorgente del deck,
    CSS di dominio ed esclusioni dal perimetro;
  - `sources.py` — libreria condivisa: parsing di plan, task e register,
    contratti plan × o2 e i3 × goal, Pandoc e resa del deck; non si invoca
    direttamente;
  - `build_pages.py` — le pagine 1:1 di `goal.md`, `world.md` e delle sei
    collezioni, allo stesso path del repo, con la navigazione comune, i link
    riscritti sul perimetro e le immagini copiate accanto. Regressioni:
    `python3 -m unittest discover -s tests -p 'test_build_pages.py'`;
  - `build_system_image.py` — la home statica minimalista: register in
    sintesi, un collegamento primario per stadio, il deck come voce a sé;
  - `serve.py` — serve la sola `../view/` sulle reti private:
    `python3 o3/view/serve.py`, porta 8000, Ctrl-C per chiudere; il servizio
    permanente dell'host privilegiato lancia lo stesso script con `--port`;
    con `--publish-root DIR` serve la versione pubblicata e `/_stato`, e
    senza versione valida esce con 3 (`--check` fa solo il controllo).
    Solo libreria standard, niente dotfile né elenchi di cartella;
  - `assets/` — i CSS canonici, copiati in `../view/assets/`: `page.css`
    per le pagine, `system-image.css` per la home, `deck.css` per il deck.

Ogni file di `../view/` ha una sorgente canonica; il generatore verifica i
contratti fra sorgenti ([view](../kb/view.md)):

- `../view/<path>.html` ← `../<path>.md`, per `../goal.md`, `../world.md` e
  ogni `.md` delle sei collezioni;
- `../view/presentation.html` ← `../presentation/presentation.md`, con le
  tavole copiate da `../presentation/`;
- `../view/index.html` ← titolo di `../README.md`, intro dei register
  `../goal.md` e `../world.md`, configurazione degli slot; le collezioni le
  _collega_, non le rende.

`view/build.py` e `kb_tools.py audit` sono il controllo minimo dopo
modifiche strutturali.
