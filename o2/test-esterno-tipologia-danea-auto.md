---
sintesi: "Eseguire il test esterno che due verdetti di canone aspettano da giugno — la tipologia-contenuto G/M/A e l'esito «zero forzati» della matrice — su danea-auto, l'unico artefatto disponibile cresciuto senza il metodo. Si legge un solo stato, lo snapshot pre-adozione fb83c0d, in sola lettura; il risultato è indicativo e non conclusivo per il limite di contaminazione dal custode, e in caso di falsificazione il raggio a valle è di cinque artefatti."
ciclo: dev
---

# Test esterno della tipologia su specimen `danea-auto`

Due verdetti di `i3/maturazione-nodi-fondativi.md` sono provvisori da giugno per
la stessa ragione: mancava un artefatto **nato senza il metodo** su cui provarli.

- `kb-content-typology` (`bozza`): la tripletta G/M/A (Goal-ought /
  Mondo-is / Macchina) copre i quattro adottanti «senza forzare», ma i quattro
  li ha plasmati il metodo;
- l'esito «zero forzati» della matrice del ciclo (`kb/action-cycle-matrix.md`).

`danea-auto` è quell'artefatto: 50 commit dal 2026-06-05, automazione AHK di
produzione su Danea/EasyFatt, nessuno stadio `i1`–`o3`, nessun register dei poli,
nodi `kb/` senza frontmatter né `Connessioni:`. Il contesto pieno — cosa ha
inventato per conto suo e cosa no — vive nel filo.

## Lo stato da leggere, e nessun altro

**`fb83c0d`** — l'ultimo commit prima di `d45d4cb`, che il 2026-08-12 ha estratto
la `kb/` da `CLAUDE.md`. Ogni stato successivo porta un'articolazione (split
d'altitudine, regola di non-derivabilità) plausibilmente trasferita dal canone,
quindi non è materiale di test.

```
git -C ~/danea-auto show fb83c0d:CLAUDE.md
git -C ~/danea-auto ls-tree -r --name-only fb83c0d
```

**A `fb83c0d` non esiste nessuna `kb/`**, e questo è il punto: il sapere durevole
sta tutto in un `CLAUDE.md` da **1046 righe**, più `TODO.md` (code e prove da
fare) e `danea-backup.md` (documento satellite su un'area contigua). Non è una
KB da riclassificare — è **conoscenza senza KB**, che è un test più severo di
quello previsto: i quattro adottanti hanno una `kb/` perché il metodo gliel'ha
prescritta, e qui la tipologia deve discriminare su materiale che nessuno ha mai
organizzato in nodi.

Lo snapshot è immutabile: il task **non ha scadenza** e non deve precedere una
eventuale adozione.

## Vincoli

- **Read-only sul repo esterno.** Non si scrive nulla in `~/danea-auto` — né
  nodi, né register, né struttura. `danea-auto` non è un adottante e non ha un
  `method` da attraversare: scrivergli dentro da qui scavalcherebbe la membrana
  («agisci attraverso, ratifica»). Il verdetto si scrive **qui**.
- **Il risultato è indicativo, non conclusivo.** Il caveat anti-complicità non si
  solleva: si sposta dall'artefatto al custode, che è lo stesso che tiene il
  canone. Un baricentro che cade pulito va riportato come corroborazione debole,
  e la dichiarazione del limite è parte del risultato, non una nota a margine.
- **Un baricentro «pulito» non basta come esito.** La domanda utile non è se la
  tripletta _possa_ classificare quei contenuti — con tre categorie larghe si
  classifica quasi tutto — ma se la classificazione **discrimini**: se cambia
  qualcosa nel giudizio sull'artefatto, e se qualche contenuto resista.
- **L'unità di classificazione va scelta e dichiarata prima di guardare i dati.**
  Per i quattro adottanti l'unità era il nodo, data dal catalogo; qui non c'è
  catalogo, quindi bisogna decidere cosa si classifica (le sezioni `##` di
  `CLAUDE.md`? i fatti singoli? i file?) e la scelta può fabbricare il risultato.
  Dichiararla prima è il vincolo che impedisce la forzatura che la matrice esiste
  per intercettare.

## Come si saprà che ha funzionato

Esito atteso: una voce nel filo `maturazione-nodi-fondativi` che sposta i due
verdetti da «provvisorio, manca il materiale» a **corroborato-debole** oppure a
**falsificato**, con l'unità di classificazione dichiarata, la classificazione
stesa per esteso e gli anomali nominati (le «sorgenti fuori posto» della prima
passata sono il precedente: la tipologia le segnalò come anomalia invece di
inventargli una casa, ed era l'esito gradito). Se il materiale non basta a
decidere, anche quello è un esito: si scrive che il test è stato eseguito e non
discrimina.

## Raggio a valle se falsifica

Cinque artefatti dipendono dai due verdetti, e vanno rivisti nell'ordine:

- `kb/kb-content-typology.md` (`bozza`) — il nodo stesso;
- `i2/baricentro-kb-adottanti.md` (`bozza`) — l'osservazione che l'ha generato,
  che porta già la propria condizione di caduta;
- `kb/action-cycle-matrix.md` — il claim «zero forzati» e il conteggio delle
  celle;
- `kb/knowledge-base.md` e `kb/system-image.md` — citano la tipologia.

Il raggio è dichiarato qui perché il test **serve** a poter falsificare: se
l'esito costringesse a toccare cinque file, non è una sorpresa da gestire ma il
prezzo previsto.
