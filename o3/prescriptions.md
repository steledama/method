# Prescriptions

Indice della collezione `o3/`: lo **stadio o3** del ciclo, l'atto versionato e predisposto sul Mondo runtime. Il significato dello stadio vive nell'atomo [perform](../kb/perform.md). Il Mondo runtime di `method` sono gli adottanti: l'o3 di `method` è il **runbook di propagazione** — la ricetta, per repo, che porta un adottante al canone nuovo. Lo esegue il `method` dell'adottante: o3 prescrive, method compie l'atto ([action-cycle](../kb/action-cycle.md)). Una prescrizione nasce quando un segnale i1 ([perceptions](../i1/perceptions.md)) è stato valutato e ha prodotto un cambio di canone; resta finché tutti gli adottanti non l'hanno recepita. La fetta di skill che mantiene lo stadio è lo scope `perform` di [exec](../.claude/skills/exec/SKILL.md).

## Divisione del lavoro

`method` prescrive il canone **fino ai propri concetti**; l'adottante personalizza l'**ultimo miglio** contro il suo stato reale.

- qui vivono il _cosa_/_perché_ e la ricetta nel lessico del metodo, più i touchpoint per-repo che `method` già conosce — come **indizi da verificare in loco**, non ordini alla lettera;
- la mappatura sui file veri (path, nomi, struttura) la fa il `method` dell'adottante, che legge il repo aggiornato: è il checkpoint di [cognitive-fidelity](../kb/cognitive-fidelity.md) — il modello che `method` ha di un repo è una fotografia dell'osservatorio e può derivare, quindi non va pre-cotto dove il rappresentato cambia;
- una prescrizione si **personalizza per repo** (un file dedicato) solo quando l'applicazione diverge davvero tra adottanti; finché la differenza è solo _quali_ file esistono, un runbook unico con note per-repo basta.

## Contenuti

- [Il motore del ciclo lo sceglie il repo](motori-del-ciclo.md) — `motori` nel
  profilo del lanciatore, fallback nei due versi, esecutore Codex canonico;
  all'host solo binari, recinto, arresto e trigger, e nessun nixos tiene la
  politica degli altri repo. Prescritta ai sette il 2026-11-11.
- [L'ultimo giro senza `git log` da quotare](ultimo-giro.md) —
  `o3/ultimo_giro.py` al posto dei `git log` con parentesi che aprono il
  giro, negati in 13 giri di quattro repo; le skill lo usano, i permessi lo
  concedono. Prescritta ai sette il 2026-11-12.

Le prescrizioni recepite da tutti gli adottanti escono dall'indice: la
loro storia è in git.

## Procedure

Runbook permanenti che `method` esegue su se stesso come osservatorio, non
ricette da far recepire agli adottanti: restano finché servono.

- [Ingresso di un adottante nell'osservatorio](ingresso-adottante.md) —
  verificare l'adozione locale, fissare una baseline con provenienza,
  aggiornare le rappresentazioni correnti e predisporre il primo giro senza
  governare la coda del nuovo repository. Si esegue da `/adottanti` quando
  un progetto entra nel territorio.

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
- `traduzioni.py check` — allineamento delle copie gemelle `nome.<lingua>.md`
  al sorgente (cfr. [translation](../kb/translation.md)): esce con errore per
  copia senza sorgente o senza `fonte:`, segnala senza fermare quelle
  indietro; `fonte <file>` stampa la riga da scrivere nella copia. Lo lancia
  il gate di `/commit`. Test: `python3 -m unittest discover -s tests -p 'test_traduzioni.py'`.
- `lanciatore.py` — il lanciatore canonico del ciclo autonomo: controlli, pull,
  avvio dell'agente coi tetti, righe di `partenza` e `chiusura` in `i1/giri/`;
  `--controlli` è in sola lettura. Osservabilità e contratto di fallback:
  [engine fallback](ciclo/fallback.md). In uso dal timer di method dal 09/11
  e in `danea-auto` su Windows. Test: `python3 -m unittest discover -s tests -p 'test_lanciatore.py'`.
- `esecutore_codex.py` — l'esecutore canonico di Codex per il lanciatore:
  traduce permessi e hook del giro in un hook `PreToolUse` di Codex e
  normalizza i suoi eventi. Test: `python3 -m unittest discover -s tests -p 'test_esecutore_codex.py'`.
- `scadenze.py` — il controllo di scadenze e ricorrenze del plan
  ([plan](../kb/plan.md), «Ricorrenze»). Test: `python3 -m unittest discover -s tests -p 'test_scadenze.py'`.
- `dinieghi.py` — la ricorrenza dei dinieghi nei giri autonomi: classi di
  grafia in almeno due giri fra gli ultimi dieci dei repo leggibili, con
  l'esito sul segnale canonico ([agent-as-user](../kb/agent-as-user.md)). Lo
  lancia il giro di `method`. Test: `python3 -m unittest discover -s tests -p 'test_dinieghi.py'`.
- `ultimo_giro.py` — l'ultimo giro e l'ultimo `Prossimo:` del repo corrente,
  senza grafie da quotare ([ultimo giro](ultimo-giro.md)). Test nello stesso file.
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
