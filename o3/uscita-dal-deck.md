---
data: 2026-11-08
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto
---

# Il deck ha un'uscita alle viste

## Cosa e perché

Reveal intercetta Alt+frecce per saltare i frammenti e toglie l'evento al
browser, e nella pagina niente riporta alle viste: un solo «indietro» basterebbe,
ma nessuno lo sa. Proposta da `nixos` il 2026-10-31, adottata dal custode il
2026-11-08 (`kb/presentation.md`, «Forma»).

Il rimedio è un frammento comune, `sources.deck_exit()`: Alt+frecce restano al
browser e un link fisso «← viste» sta in ogni deck, in basso a sinistra. La build
rompe se il deck non lo contiene, così un builder di dominio non recepito si vede
invece di restare muto.

## Ricetta di recepimento

1. Riporta dal canone le modifiche a `o3/view/sources.py`, `o3/view/build.py` e
   `o3/view/assets/deck.css`, preservando le parametrizzazioni locali.
2. Se il repo ha un `DECK_BUILDER`, includi `sources.deck_exit()` nella pagina,
   dopo `Reveal.initialize`, tale e quale: il controllo cerca il frammento esatto.
3. Verifica con `python3 o3/view/build.py --check`, poi apri il deck: il link
   riporta alla home e Alt+← esce dal deck.
4. Registra il recepimento nel marker `i3/allineamento-metodo.md`, in una riga
   che nomina `uscita-dal-deck` come recepita.

## Note per repo

Indizi dal confronto del 2026-11-08, da verificare in loco.

- `economia` (`deck.py`) e `salute` (`build_deck.py`): hanno un `DECK_BUILDER`
  con un proprio `Reveal.initialize`; è il caso per cui esiste il controllo. Va
  aggiornato nello stesso commit della copia canonica, altrimenti la build rompe.
- `nixos`, `nixos-lavoro`, `bi`, `danea-auto`: deck da Markdown, basta la copia
  canonica.
- `baserow`: nessun deck dichiarato; basta la copia canonica, che tiene la vista
  allineata.

## Verifica

`python3 o3/prescrizioni.py verifica uscita-dal-deck` dà la prescrizione recepita
in ogni adottante, e `build.py --check` passa in ciascuno. Provato in Chromium
con Reveal 5.1.0, il caso di pandoc fino alla 3.11. Con la 6.0.2, usata da pandoc
3.12, il comportamento è dedotto dal sorgente: il primo adottante con quella
versione lo verifichi aprendo il deck.
