---
ciclo: runtime
---

# Segnale: presentazioni annidate, oltre il «solo deck» di `kb/presentation.md`

Data: 2026-11-18 · Fonte: inoltro della sessione `salute` su `deck` via
Herdr, su richiesta del custode; `salute` `ba52e68` ed `economia` `0c0ebff`
letti su `origin`

## Il segnale

[presentation](../kb/presentation.md) definisce il racconto curato come «un
solo deck», reso in `view/presentation.html`. Due adottanti sono arrivati
allo stesso bisogno con due soluzioni locali diverse: un deck principale da
cui si scende in sotto-deck orizzontali, con ↓ per scendere e ↑ per risalire
alla slide madre, senza limite di profondità. Tutti e due passano dal
`DECK_BUILDER` di `project.py` e girano attorno allo stesso vincolo: Reveal ha
due soli assi e una colonna verticale non contiene una sequenza orizzontale.

- **`salute`** (`o3/view/build_presentazioni.py`, scelta del custode del
  18/11, scostamento dichiarato in `i3/allineamento-metodo.md`). Usa più
  pagine. Il deck principale è `presentation/salute.md`, la teoria del
  progetto. I sotto-deck sono `presentation/tradizioni.md`,
  `presentation/mente.md` e il corpo, generato da `build_deck.py`. Ogni
  sotto-deck è una pagina `view/presentation-<nome>.html`. La slide madre
  dichiara in coda `Approfondimento: presentation/<nome>.md`. Una briciola di
  percorso in alto dice il livello. Il builder rompe su cicli e duplicati,
  e `check_closed` tiene i link dentro `view/`. Il motivo: il deck unico
  copriva solo il corpo e non rappresentava il progetto.
- **`economia`** (`o3/view/deck.py`). Usa una sola pagina. I livelli
  (`principale`, `finanze`, `immobili`, `tigli`) stanno in
  `presentation.html` come `<template>`, e uno script li monta al posto delle
  slide visibili (`Reveal.sync()`). Una slide con `data-sub="<livello>"` apre
  il livello omonimo. La pila dei livelli aperti sta nell'indirizzo
  (`#/principale.7/immobili.1/tigli.0`), con l'hash di Reveal spento. Le
  sorgenti sono HTML in `presentation/`, tranne `finanze`, generato dai JSON
  di `i1/`. Un `data-sub` verso un livello inesistente, o un livello che
  nessuna slide apre, rompe la build.

Le due soluzioni divergono sul punto che un contratto dovrebbe fissare:

- la pagina: una sola con livelli montati, contro una pagina per sotto-deck;
- la sintassi del collegamento: riga `Approfondimento:` nel Markdown, contro
  attributo `data-sub` nell'HTML;
- lo stato della navigazione: pila nell'hash, contro briciola e link fra
  pagine;
- in comune hanno la profondità libera, le sorgenti curate o generate per
  livello e la rottura della build sui collegamenti orfani.

## Cosa c'è da valutare

- Se `kb/presentation.md` debba ammettere un deck principale con sotto-deck
  senza che sia uno scostamento, e con quale contratto: sintassi del
  collegamento, nomi delle pagine, navigazione ↓/↑.
- Se la navigazione (script e briciola) debba diventare canonica, o restare
  locale con solo il contratto nel canone.
- Quale delle due forme regge meglio i presidi del canone: link chiusi in
  `view/`, una sola voce in home, indirizzo condivisibile di una slide
  profonda.
- Il nesso con [la pagina di dominio in
  home](pagina-dominio-home-salute-2026-11-18.md): tutti e due i segnali
  chiedono cosa, oltre al deck, la home e la presentazione possano ospitare.

Sono due casi, in due adottanti.

Seguito: giro del 2026-11-19, decisione chiesta al custode nel task
[presentazione oltre il deck](../o2/presentazione-oltre-il-deck.md).
