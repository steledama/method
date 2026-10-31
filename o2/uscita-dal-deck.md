---
sintesi: "Il deck non ha un'uscita: Reveal intercetta Alt+frecce e nella pagina nulla riporta alle viste. Rimedio canonico in due parti, Alt+frecce lasciate al browser e un link fisso «← viste», da far arrivare anche ai deck di dominio. Proposta da nixos il 2026-10-31, verificata sul sorgente di Reveal."
ciclo: dev
decidere: "Adottare il rimedio in due parti (keyboardCondition che ignora Alt e link fisso alle viste) come canone, con un frammento comune che anche i DECK_BUILDER includono?"
---

# Uscita dal deck

## Origine

Proposta della sessione `nixos` su `deck`, inoltrata via Herdr su richiesta
del custode il 2026-10-31, discussa col custode in quella sessione. Il
messaggio non porta autorizzazioni nuove.

## Il difetto, verificato

Rilevato il 2026-10-31 sul sorgente pubblicato di Reveal e sul template di
pandoc 3.7.0.2 di `deck`:

- `revealjs_url()` in `o3/view/build.py` sceglie Reveal 5.1.0 fino a pandoc
  3.11 e 6.0.2 dalla 3.12. In 5.1.0 (`js/controllers/keyboard.js`) Alt
  con le frecce significa «avanti/indietro saltando i frammenti» (righe
  262-343) e l'evento chiude con `preventDefault` (383, 391): Alt+← non
  arriva al browser. La 6.0.2 ha lo stesso comportamento
  (`skipFragments: e.altKey`, 14 occorrenze in `dist/reveal.mjs`);
- il template canonico ha `hash: true` e `history: false`: un solo
  «indietro» del browser riporta alla home delle viste, ed è oggi l'unica
  uscita. Nella pagina niente la indica;
- `keyboardCondition`, se è una funzione che rende `false`, fa ignorare
  l'evento a Reveal prima di ogni altra gestione (riga 146 della 5.1.0;
  presente anche nella 6.0.2). Il template di pandoc non lo espone come
  variabile, perché è una funzione: si passa con uno script dopo
  `Reveal.initialize`, per esempio
  `Reveal.configure({keyboardCondition: e => !e.altKey})` nell'`include-after`
  (riga 317 del template, dopo l'inizializzazione alla 95).

## Il rimedio proposto

- **Alt+frecce al browser**: si perde solo il salto dei frammenti, che i
  deck del metodo non usano;
- **link fisso «← viste»** verso `index.html`, discreto, sull'accento del
  progetto, in ogni deck. Il deck è `view/presentation.html`, accanto alla
  home, quindi il link è relativo e resta nel compartimento stagno.
  Etichetta da `LINGUA`; posizione lontana da numero di slide e controlli
  (in basso a destra), nascosto in stampa.

## Il punto che la proposta non copre

`sources.reveal_page` serve solo i deck da Markdown (`method`, `bi`,
`danea-auto`, `nixos`). `economia` (`deck.py`) e `salute` (`build_deck.py`)
hanno un `DECK_BUILDER` con un proprio `Reveal.initialize`: una modifica al
solo `reveal_page` non li raggiunge e il canone divergerebbe per deck.
Servono:

- un frammento canonico in `sources.py` (script e link), che
  `reveal_page` usa e che il contratto di `DECK_BUILDER` chiede di
  includere;
- un controllo nella build: `presentation.html` senza il link alle viste
  rompe, così un builder di dominio non recepito si vede invece di restare
  muto;
- le regole in `deck.css`, accanto agli stili canonici.

## Propagazione

Strumento in `o3/view/` e stile in `deck.css`: canone copiato, non
symlink. Arriva agli adottanti con una prescrizione; `nixos` non tocca la
propria copia per non creare drift. La prescrizione nomina `economia` e
`salute` per l'inclusione del frammento nei loro builder.

## Criterio di chiusura

Il custode decide. Il frammento e il controllo girano in `method`, test
compresi; la prescrizione è aperta. Riga del plan, voce in `o2/tasks.md` e
questo file si rimuovono nello stesso commit.

Connessioni:

- [view](../kb/view.md)
- [presentation](../kb/presentation.md)
- [pubblicazione-decisa-dal-repo](pubblicazione-decisa-dal-repo.md)
