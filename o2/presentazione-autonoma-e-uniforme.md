---
sintesi: "Primo passo della ristrutturazione della presentazione chiesta dal custode il 2026-10-02: un solo stile canonico (lo stile pulito di nixos al posto di quello a sketch), un colore d'accento per progetto, la sigla del repo nei titoli delle viste e presentation/ chiusa su se stessa, senza link alle fonti fuori dalla cartella. Sblocca gli altri tre task, che partono dalle stesse basi."
ciclo: dev
---

# Presentazione autonoma e uniforme per progetto

Primo dei quattro task della ristrutturazione chiesta dal custode il
2026-10-02. Gli altri tre (indice dei Confronti, condizioni di risveglio,
server LAN) partono da qui. Il canone cambiato si propaga con una sola
prescrizione alla fine
([prescrizione-presentazione-ristrutturata](prescrizione-presentazione-ristrutturata.md)).

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
- **Da decidere all'implementazione:** le tavole raster delle
  Interpretazioni (`i2/*.png`, 17 MB in `metodo`) oggi sono sfondi caricati da
  `../i2/`. Le alternative sono tre: copiarle in `presentation/assets/` alla
  build (raddoppia il peso versionato), spostarne la sede canonica in
  `presentation/assets/`, oppure toglierle dal deck. Va scelta col custode,
  misurando il peso negli adottanti.
- **Presidio:** il builder rompe la build se un `href` o una `url(...)`
  emessi escono da `presentation/`. È il «derivata implica verificata» di
  `kb/view.md` applicato al confine della cartella.

## Canone da toccare

- `kb/presentation.md`: stile unico più accento, compartimento stagno e
  contratto del CSS canonico.
- `kb/view.md`, se il confine della cartella diventa un obbligo della vista.

## Criterio di chiusura

Le viste di `metodo` sono rigenerate col CSS unico e l'accento indigo, i
titoli portano «Method», `grep` non trova link che escono da `presentation/`
e due build consecutive danno lo stesso output.
