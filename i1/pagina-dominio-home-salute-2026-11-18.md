---
ciclo: runtime
---

# Segnale: una pagina di dominio di primo livello non ha posto sulla home canonica

Data: 2026-11-18 · Fonte: inoltro della sessione `salute` su `deck` via
Herdr, su richiesta del custode; `salute` `ba52e68` citato nell'inoltro

## Il segnale

In `salute` il builder di dominio scrive `view/cruscotto.html`, il cruscotto
corpo-mente. Legge solo il registro di i1 e dal 18/11 mette meditazione, sonno
e HRV sulla stessa linea del tempo. Secondo l'inoltro è, con la presentazione,
la pagina più usata della vista.

La home canonica (`o3/view/build_system_image.py`, `render`) linka come voce a
sé solo il deck (`deck-link` → `presentation.html`). L'unico aggancio locale è
`DESCRIZIONI` in `project.py`. Il link al cruscotto finisce quindi nella
descrizione della card i2, anche se il cruscotto non è una lettura i2. Il
custode non lo trovava più: «non mi sembra che ci sia più il collegamento
dalla home page». Il ripiego di `ba52e68` mette il link in grassetto in
apertura della card i2 e nelle slide.

## La proposta della sessione

Un campo facoltativo in `project.py`, per esempio
`PAGINE_HOME: list[tuple[str, str]]`, che la home rende come voci a sé
accanto a «Presentazione», con la stessa classe `deck-link`. Valgono gli
invarianti che il canone ha già. La pagina la scrive il builder di dominio
nella cartella d'uscita. `check_closed` (`o3/view/sources.py`) rompe se la
destinazione manca o esce da `view/`. Se il campo manca, gli altri adottanti
non cambiano.

## Riscontro sugli altri adottanti

Letti `origin/main` di `nixos`, `economia`, `salute` (locali) e `bi`,
`baserow`, `abbinatore` (su `svezia`). `danea-auto` non è stato letto.

- Solo `salute` ha una pagina di dominio di primo livello nella vista, e solo
  `salute` mette un link in `DESCRIZIONI`.
- `economia` scrive più pagine (`o3/view/deck.py`), ma sono sotto-deck dentro
  `presentation/` raggiunti dal deck. Riguardano il secondo candidato
  dell'inoltro (presentazioni annidate, oggi uno scostamento dichiarato in
  `i3/allineamento-metodo.md` di `salute`), non questo.
- `nixos`, `bi`, `baserow` e `abbinatore` non hanno builder di dominio.

## Cosa c'è da valutare

- Se il caso è generale: per ora è un caso solo.
- Il nome e la forma del campo, e se la home debba distinguere il racconto
  (il deck) dalle pagine operative.
- Se un aggancio dichiarato in `project.py` è il punto giusto, o se basta
  che la home elenchi le pagine di primo livello che il builder di dominio
  dichiara di scrivere.

Seguito: giro del 2026-11-19, decisione chiesta al custode nel task
[presentazione oltre il deck](../o2/presentazione-oltre-il-deck.md).
