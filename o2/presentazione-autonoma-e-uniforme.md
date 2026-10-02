---
sintesi: "Primo passo della ristrutturazione della presentazione chiesta dal custode il 2026-10-02: i builder in un path di canone identico in ogni repo (o3/presentation/), un solo stile canonico (lo stile pulito di nixos al posto di quello a sketch), un colore d'accento per progetto, la sigla del repo nei titoli delle viste e presentation/ chiusa su se stessa, fatta solo di file generati. Sblocca risveglio e server, che partono dalle stesse basi."
ciclo: dev
---

# Presentazione autonoma e uniforme per progetto

Primo task della ristrutturazione chiesta dal custode il 2026-10-02.
Condizioni di risveglio, server LAN e (dopo la revisione dei verdetti)
indice dei Confronti partono da qui. Il canone cambiato si propaga con una sola
prescrizione alla fine
([prescrizione-presentazione-ristrutturata](prescrizione-presentazione-ristrutturata.md)).

## Builder in `o3/presentation/`

Decisione del custode (2026-10-02): il path dei builder è **canone, non
scelta del fork**. Oggi stanno in `o3/` (`metodo`, `danea-auto`) o in
`o3/tools/` (`nixos`, `bi`, `crm`), e chi passa da un repo all'altro, umano
o agente, deve prima scoprire dove. Anche le skill (`commit`, `exec`, `kb`)
citano path diversi a seconda del fork.

- Tutto quello che produce o serve la presentazione vive in
  `o3/presentation/`.
- `o3/presentation/build.sh` è l'**unico entrypoint** di build: fonde
  `build-presentation.sh` e `build-system-image.sh`, così la rigenerazione
  è un gesto solo.
- `o3/presentation/serve.py` è il server (task
  [server-lan-della-presentazione](server-lan-della-presentazione.md)).
- Accanto restano i moduli `build_views.py`, `build_lists.py` e
  `build_system_image.py`. La libreria condivisa `presentation.py` si
  rinomina (per esempio `sources.py`), perché un `presentation.py` dentro
  `presentation/` confonde.
- `o3/` resta la casa dei runbook (`.md`) e degli altri esecutori: la
  sottocartella vale per ora solo per la presentazione. `kb_tools.py` e
  `kb_profile.py` restano dove sono finché non nasce un secondo caso.
- Si aggiornano i riferimenti: skill `commit`, `exec`, `kb`, indice
  `o3/prescriptions.md`, test in `tests/`.
- **Da verificare:** `build.sh` è bash, e su Windows (`danea-auto`) serve
  Git Bash. Lo si controlla nel fork prima di fissarlo nel canone.

## Stile unico

- Oggi `metodo`, `bi`, `crm` e `danea-auto` usano lo stile a sketch (Patrick
  Hand, carta crema), che il custode giudica troppo confidenziale. `nixos`
  usa uno stile pulito, che diventa la base comune. `economia` e `salute`
  tengono un loro renderer.
- Si crea un solo CSS canonico delle viste Reveal (nome da fissare, per
  esempio `presentation/assets/deck.css`), ricavato dalla parte generica del
  CSS di `nixos`: token, titoli con la barra d'accento, cover, slide `hero`,
  tabella del plan.
- Le classi di diagramma del deck di `nixos` (`card`, `frame`, `arrow`,
  `routing`, …) non sono canone: restano in un CSS locale del dominio, come
  già succede per la home (`i3/home-minimalista.md`, contratto minimale).
- A distinguere i progetti è solo il **colore d'accento**, un token
  `--accent` (con la sua variante `--accent-ink` per il testo) in una sede
  per repo. Vale per tutte le superfici, viste Reveal, liste e home:
  - `metodo` #4338ca (indigo);
  - `nixos` #c2410c (arancio, quello attuale);
  - `bi` #0f766e (teal);
  - `economia` #15803d (verde);
  - `salute` #be123c (rosa);
  - `crm` #a16207 (ambra);
  - `danea-auto` #7e22ce (viola).

## Sigla del repo nei titoli

- Le intestazioni delle viste portano la sigla del progetto, nella lingua
  del repo: «Method Plan», «Method Verdicts», «NixOS Plan»; «BI Piano»,
  «BI Confronti», «Economia Piano», «Salute Piano», «CRM Piano», «Danea
  Piano».
- Sigla e lingua si dichiarano **una volta** per repo e le leggono tutti i
  builder (viste Reveal, liste, home). La sede si sceglie all'implementazione
  tra la sezione CONFIG già prevista dai builder e un file dedicato. Il
  vincolo è che i fork la parametrizzino in un punto solo.
- Anche il `<title>` delle pagine porta la sigla, così le schede del browser
  si distinguono tra repo diversi.

## Compartimento stagno

Decisione del custode: `presentation/` si apre e si serve da sola, senza link
che escono dalla cartella. Oggi ne escono 44 (`../goal.md`, `../o1/plan.md`,
`../o2/…`, le fonti di liste e tavole).

- La chiave `Ob.` del plan oggi porta a `goal.md`
  (`obiettivo-del-plan-collegato-al-goal`, recepita dai sei il 2026-10-01).
  Diventa un link interno a una slide di legenda degli obiettivi, con i
  titoli letti da `goal.md` al momento della build: il collegamento
  task→obiettivo resta, ma porta a un punto dentro la vista.
- Le righe «Sorgente: `o2/…`» e il rimando «plan sorgente» spariscono. Il
  secondo lo sostituisce il task
  [condizioni-di-risveglio-nella-vista](condizioni-di-risveglio-nella-vista.md).
- Nelle liste (`build_lists.py`) i link verso i file della collezione
  diventano testo semplice. Restano link solo le ancore interne e gli URL
  assoluti.
- **Tavole delle Interpretazioni** (`i2/*.png`, 17 MB in `metodo`): oggi
  sono sfondi caricati da `../i2/`. Decisione del custode (2026-10-02): la
  fonte resta in `i2/`, dove l'indice `i2/interpretations.md` le elenca
  come sintesi illustrata, e il builder le **copia** in
  `presentation/assets/`. Così la dipendenza resta nel verso giusto (la
  presentazione si ricava dalle collezioni) e `presentation/` resta fatta
  di file generati più gli asset. Il peso nella storia è nullo, perché git
  salva una volta sola i file identici; il checkout cresce di 17 MB. La
  fonte del deck riferisce le tavole col path di destinazione
  (`assets/<nome>.png`), e il builder rompe se una tavola citata non esiste
  in `i2/`.
- **Presidio:** il builder rompe la build se un `href` o una `url(...)`
  emessi escono da `presentation/`. È il «derivata implica verificata» di
  `kb/view.md` applicato al confine della cartella.

## Canone da toccare

- `kb/project-structure.md` o `kb/presentation.md`: `o3/presentation/` come
  path canonico dei builder, con `build.sh` e `serve.py`.

- `kb/presentation.md`: stile unico più accento, compartimento stagno e
  contratto del CSS canonico.
- `kb/view.md`, se il confine della cartella diventa un obbligo della vista.

## Criterio di chiusura

I builder di `metodo` vivono in `o3/presentation/` e `build.sh` rigenera
tutto in un gesto. Le viste sono rigenerate col CSS unico e l'accento indigo, i
titoli portano «Method», `grep` non trova link che escono da `presentation/`
e due build consecutive danno lo stesso output.
