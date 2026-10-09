---
ciclo: dev
obiettivo: 1
---

# Le skill si tagliano per arco: la tripartizione `eval`/`exec` regge?

Il taglio è canone dal 2026-08-01 (`kb/skill.md`, `stato: maturo`): il
quartetto operativo segue il ciclo di Norman, con `eval` ed `exec` che portano
ciascuna i tre stadi del proprio arco come scope. Motivazione e storia della
decisione stanno nel nodo e in git. Qui resta la tensione aperta: la scommessa
che la rigidità paghi in qualità autocorrettiva più di quanto costi in
scritture e invocazioni, con la sua clausola di uscita e il task `p1`
(`o2/rivalutazione-skill-per-arco.md`).

## Verdetto della rivalutazione (custode, 2026-09-24)

**La tripartizione resta com'è. Si corregge la clausola, non il taglio.** Il
materiale viene dal terzo battito `/adottanti` (eseguito il 2026-09-24,
arretrato dal 1° settembre), misurato
per commit sui sette repository dal 2026-08-01:

- **nessun sintomo del «troppo».** Nessuno stadio è vuoto ovunque: tutti i
  repository hanno commit su `i2/` (da 2 a 32) e su `o3/`. Il repository che
  usa di più l'arco, `bi` (circa 15 giri `eval`/`exec` fra il 14/8 e il 23/9),
  non l'ha abbandonato: l'ha adattato. I suoi giri scrivono quasi solo
  `i3/` e `o2/` (i1 = 2 commit, i2 = 5, i3 = 64) perché `interpret` vive negli
  script, col registry `o3/lib/perception.js`. È l'accorpamento degli scope
  che la clausola prevedeva come primo snellimento, fatto spontaneamente e
  senza smettere di distinguere i passi;
- **il «ha pagato» è documentato solo in `metodo`.** Resta il caso del primo
  giro (`eval compare` che intercetta due fotografie stale di `goal.md`).
  Negli adottanti i giri intercettano problemi reali, come la regressione del
  retry OAuth in `bi`, ma un `eval` monolitico li avrebbe trovati lo stesso:
  sono compatibili con la tripartizione, non la dimostrano;
- **il costo dell'assorbimento non è stato sentito.** Nessuna traccia in
  `salute` ed `economia`; `bi` lo aveva citato solo in anticipo. Nel
  controfattuale le skill autonome di `nixos` si sono ridotte da sole
  (`nix-overlay-update` fusa in `/manutenzione`);
- **la misura principale non esisteva.** Gli esiti nulli per stadio, e con
  loro l'invocazione fatta «solo per disciplina», venivano restituiti in
  conversazione e non lasciavano traccia. Nessuna attesa li avrebbe resi
  contabili: la clausola, così com'era scritta, non poteva scattare in nessuna
  delle due direzioni.

Da qui la correzione: ogni giro si chiude con un commit che porta l'esito per
stadio (trailer `Esiti:`, `materia` o `vuoto`, `--allow-empty` se il giro non
ha cambiato file), inciso in `kb/skill.md`, nelle canoniche `eval`, `exec` e
`/commit`, e propagato coi sei adottanti come prescrizione
`o3/esiti-per-stadio-nel-commit.md`. Il posto è il commit e non il filo o il
marker perché un file aggiornato a ogni giro sarebbe un log, e il log è git.

**Il fallback del 2026-11-01 si riattiva**, con l'evidenza mancante
dichiarata: il conteggio degli esiti per stadio sui giri registrati dopo il
recepimento, e una lettura del profilo ancora muto: `crm`, col plan fermo
dal 2026-08-21. `danea-auto`, muto fino a settembre, dal 2026-09-26 è il
repository con più giri registrati. A novembre il verdetto
si prende su numeri, non su proxy.

## La clausola di uscita, dichiarata prima di partire

Il rischio dichiarato dal custode è il barocco: una divisione che moltiplica
scritture, token ed energie per azioni che verrebbero naturali tutte insieme. La
scommessa è che la rigidità paghi in qualità autocorrettiva, e i tre episodi
danno la misura del prezzo dell'alternativa. Ma la scommessa si rivaluta, e la
condizione si scrive **ora** perché fra tre mesi non dipenda da chi si ricorda di
averla promessa:

- **quando**: il task di rivalutazione `pause` esiste
  (`o2/rivalutazione-skill-per-arco.md`). La data originaria (**2026-11-01**)
  era stata anticipata dal custode al **2026-09-01**; il giudizio di settembre,
  preso il 2026-09-24, ha mantenuto la tripartizione e riattivato novembre con
  l'evidenza mancante dichiarata (sezione sopra);
- **la misura**: il trailer `Esiti:` dei commit che chiudono i giri,
  contato per stadio e per repository con
  `git log --format='%(trailers:key=Esiti,valueonly)'`. Un sintomo che non si
  legge in questa misura va dichiarato insieme alla fonte che lo rende
  contabile;
- **sintomi che direbbero «troppo»**: uno stadio che chiude `vuoto` in _tutti_
  i repo per tre giri; giri tutti `vuoto` (commit `--allow-empty`) che si
  ripetono senza che cambi nulla nel verdetto o nella coda: è l'invocazione
  fatta solo per disciplina;
- **sintomi che direbbero «ha pagato»**: un errore intercettato dallo stadio che
  prima non esisteva (una sintesi i2 corretta perché il claim è caduto, un
  segnale i1 che sarebbe rimasto orfano, una prescrizione o3 consumata potata);
- **cosa si snellisce per primo**, se si snellisce: gli scope, non gli stadi —
  si accorpa l'invocazione, non si smette di distinguere i passi.

## Lettura della misura con un battito programmato

Il risveglio resta il 2026-11-01. Se iniziano giri periodici, il loro
innesco va distinto, quando documentabile, dai giri richiesti da eventi o
dal custode: aumentare la frequenza può aumentare gli esiti vuoti senza
provare che gli stadi siano superflui. Dove la fonte non discrimina,
dichiarare il limite. L'integrità del conteggio si controlla confrontando
trailer riconosciuti e righe nel corpo, recuperando senza duplicazioni il
caso noto di `baserow`. Un tentativo interrotto prima del commit resta fuori
da questa misura e richiede la fonte dell'esecutore del battito.
