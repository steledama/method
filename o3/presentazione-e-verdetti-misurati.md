---
data: 2026-10-02
stato: attiva
ciclo: dev
target: nixos, bi, economia, salute, crm, danea-auto
---

# Verdetti misurati contro un obiettivo e presentazione uniforme

## Cosa e perché

Il 2026-10-02 il custode ha ristrutturato la presentazione di `metodo`. Il
lavoro si è allargato a una revisione del modello, perché mettere la colonna
`Ob.` nell'indice dei Confronti ha costretto a chiedersi, filo per filo, se
ogni verdetto confronta davvero qualcosa con uno scopo. In `metodo` i fili
sono passati da 16 a 5. Questa prescrizione porta tutti e due i cambi, in
quest'ordine, perché la vista rende quello che la revisione decide:

1. **Verdetti misurati** (`kb/verdict.md`, «Che cosa è un filo»). Un file
   resta in `i3/` solo se ha una tensione aperta, un obiettivo di `goal.md`
   dichiarato nel frontmatter (`obiettivo: 1`, `S`, …) e una condizione di
   chiusura che il ciclo può vedere arrivare. Il resto va dove vive il suo
   genere: motivazione stabile nel nodo, ipotesi in attesa nello `stato` del
   nodo, seguito di una prescrizione nell'audit, decisione da prendere in un
   task. La provenienza del segnale non è l'obiettivo misurato: in `metodo`
   sei fili «misuravano» il canale delle percezioni solo perché ne erano
   nati. La `misura:` testuale nell'indice sparisce.
2. **Presentazione uniforme e chiusa** (`kb/presentation.md`):
   - builder in `o3/presentation/`, **stesso path in ogni repo**, con un
     solo entrypoint Python, `python3 o3/presentation/build.py`, che gira
     anche su Windows;
   - un solo stile canonico (`presentation/assets/deck.css`, base pulita al
     posto dello sketch); a distinguere i progetti restano solo sigla e
     colore d'accento, dichiarati in `o3/presentation/project.py`, l'unico
     file che il fork parametrizza;
   - `presentation/` **chiusa su se stessa**: nessun URL emesso esce dalla
     cartella. I link alle fonti diventano etichetta, la chiave `Ob.` apre
     una slide di legenda degli obiettivi, le tavole restano in `i2/` e la
     build le copia in `presentation/assets/`. La build si ferma se qualcosa
     esce o manca;
   - la vista del plan rende, in una slide, tutto ciò che segue la tabella
     (legenda, risvegli, scadenze); le chiavi `p<n>`/`w<n>` vi puntano;
   - la vista dei Confronti apre con l'indice Ciclo · Ob. · Filo, e la build
     verifica `i3/` contro l'indice e contro `goal.md`;
   - `python3 o3/presentation/serve.py` serve la sola `presentation/` sulla
     LAN, su richiesta (porta 8765, Ctrl-C per chiudere).

Recepire il punto 2 soddisfa anche la prescrizione
`toolchain-builder-presentazione`: `build.py` porta già la codifica UTF-8 e
la scelta di reveal.js dalla versione di pandoc. Registra l'esito di
entrambe.

## Ricetta di recepimento

### 1. Rivedi i fili `i3/` contro il tuo `goal.md`

È la parte che pesa di più, e il giudizio è tuo. Per ogni file di `i3/`:

- **c'è una tensione aperta?** Se il filo ratifica una decisione già incisa
  nel canone o nei nodi locali, verifica che la sostanza stia lì, poi
  chiudilo (file e voce d'indice; la storia resta in git). Se una parte della
  sostanza manca, spostala nel nodo prima di chiudere;
- **contro quale obiettivo?** Scrivi `obiettivo:` nel frontmatter con la
  chiave del tuo `goal.md`, al livello dell'obiettivo e non del suo
  indicatore. Se un filo vero non trova un obiettivo, forse manca
  l'obiettivo: proponilo al custode, non scriverlo nel register;
- **quale chiusura?** Un filo che aspetta «il primo caso reale» senza data
  né raccolta è un'ipotesi: il suo posto è lo `stato` del nodo;
- **cursori** come `i3/allineamento-metodo.md`: restano, dichiarano anche
  loro `obiettivo:` (di solito quello di sviluppo, che era già la loro
  `misura:`) e stanno nell'indice;
- snellisci ciò che resta alla tensione viva: la cronaca va in git;
- togli `misura:` dalle voci di `i3/verdicts.md`. Nell'introduzione
  dell'indice può restare il rimando a `kb/verdict.md`.

Se l'indice di `o3/` o di `i1/` porta cronaca di prescrizioni o catture
chiuse, potala: con la vista chiusa su se stessa la cronaca finisce per
intero nella pagina, e il canone dice già che la storia resta in git.

### 2. Sposta i builder in `o3/presentation/`

Copia da `$method_repo/o3/presentation/` i file canonici `build.py`,
`sources.py`, `build_views.py`, `build_lists.py`, `serve.py`, più
`build_system_image.py` riportandoci la **tua** sezione CONFIG (titoli e slot
della home). Copia `presentation/assets/deck.css`. Poi:

- scrivi `o3/presentation/project.py` con `SIGLA`, `LINGUA`, `ACCENTO`,
  `DECK` e, se il tuo deck ha classi di dominio, `CSS_LOCALI`;
- rimuovi i vecchi builder (`build-presentation.sh`, `build-system-image.sh`,
  `presentation.py`, `build_*.py` in `o3/` o `o3/tools/`) e il vecchio
  `interpretations.css`, dopo averne salvato le classi di dominio in un CSS
  locale;
- nella fonte del deck cita le tavole come `assets/<nome>` invece di
  `../i2/<nome>`;
- se hai `test_build_lists.py`, riallinealo a quello canonico in
  `$method_repo/tests/`;
- riallinea ogni riferimento ai vecchi path: skill `commit`, `exec`, `kb`,
  `CLAUDE.md`, `README.md`, indice `o3/`, runbook.

### 3. Verifica

- `python3 o3/presentation/build.py` esce senza errori. Se si ferma, legge i
  contratti: plan × `o2/`, `i3/` × `goal.md`, chiavi della legenda, link
  che escono da `presentation/`. Correggi le fonti, non il builder;
- una seconda build consecutiva lascia `git status` vuoto;
- `python3 o3/presentation/serve.py --bind 127.0.0.1` e apri
  `http://localhost:8765/`: titoli con la sigla, accento giusto, legenda
  degli obiettivi, indice dei Confronti, tavole visibili.

### 4. Indizi per repo, da verificare sul posto

- **`nixos`**: sigla «NixOS», `LINGUA = "en"`, accento `#c2410c`. I builder
  stanno in `o3/tools/`. Il deck (`i2/nixos-in-sintesi.md`) è la fonte dello
  stile pulito: le sue classi di diagramma vanno in un CSS locale dichiarato
  in `CSS_LOCALI`. L'iniezione di Mermaid e l'estensione `raw_html` sono
  adattamenti locali di `build.py`, da dichiarare nel marker. **Firewall**:
  su `svezia` e `deck` il firewall degli `home-clients` è attivo e la porta
  8765 non è ammessa. Dichiarala aperta solo verso la rete locale: finché
  `serve.py` non gira, sulla porta non ascolta nessuno.
- **`bi`**: sigla «BI», `LINGUA = "it"`, accento `#0f766e`. I builder stanno
  in `o3/tools/`, con `test_build_lists.py` accanto. Passa dallo sketch al
  CSS unico. Nella prova a secco del 2026-10-02 il cursore
  `i3/allineamento-metodo.md` risultava fuori da `i3/verdicts.md`.
- **`crm`**: sigla «CRM», `LINGUA = "it"`, accento `#a16207`. I builder
  stanno in `o3/tools/`. Non ha `build_lists.py`, e genera
  `interpretations` da `build_views.py` invece che da un deck in `i2/`: o
  porti la sorgente a un deck (`DECK`), o dichiari l'adattamento.
- **`danea-auto`**: sigla «Danea», `LINGUA = "it"`, accento `#7e22ce`. I
  builder stanno in `o3/`. `build.py` sostituisce la build lanciata da
  PowerShell via `bash.exe`. Collauda build e server su `danea2`: alla prima
  esecuzione di `serve.py` Windows chiede il permesso del firewall.
- **`economia`**, **`salute`**: hanno un renderer proprio. Il punto 1 vale
  per intero, perché è canone del verdetto e non della resa. Del punto 2
  valgono le parti che la loro superficie ha: sigla («Economia»,
  «Salute»), accento (`#15803d`, `#be123c`) su home e viste, nessun link
  che esce da `presentation/`, path `o3/presentation/` e `serve.py`. Il
  resto può essere una divergenza motivata.

## Chiusura

La prescrizione resta attiva finché i sei adottanti non hanno un esito nel
marker `i3/allineamento-metodo.md`: recepita, non applicabile o divergenza
motivata, distinguendo i due punti. Il battito `/adottanti` la verifica nei
file: build che passa coi contratti, nessun `misura:` negli indici `i3/`,
`obiettivo:` in ogni file di `i3/`.
