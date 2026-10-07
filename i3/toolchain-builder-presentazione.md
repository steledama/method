---
ciclo: dev
obiettivo: S
---

# I builder della presentazione assumono un toolchain che non dichiarano

## Verdetto

Il segnale viene da `danea-auto` (2026-10-01), il primo adottante che fa
girare i builder di `presentation/` su Windows. Per farli funzionare ha
dovuto cambiare due punti del canone. Tutti e due sono verificati nel
codice di `metodo`, e tutti e due vengono dalla stessa assunzione taciuta: il
toolchain è quello degli host Linux di chi li ha scritti.

**Codifica.** `build_lists.py` (oggi assorbito in `o3/view/`) chiamava pandoc con `text=True` e senza
`encoding`: Python usa la codifica di default della piattaforma, cp1252 su
Windows, e la build fallisce. Il fix di `danea-auto`, `encoding="utf-8"`
nelle due chiamate, entra nel canone così com'è. Non cambia nulla sugli
host Linux, dove la codifica di default è già UTF-8.

**reveal.js accoppiato a pandoc.** Il wrapper della build fissava
`reveal.js@5.1.0`, ma i percorsi dei plugin li scrive pandoc, secondo la
propria versione. Pandoc 3.12 scrive quelli di reveal 6
(`dist/plugin/notes.js`); con la 5.1.0 quei file non esistono e le slide
restano bianche. `deck` e `svezia` hanno pandoc 3.7.0.2, che scrive ancora i
percorsi della 5.x: oggi gli host Linux non vedono il problema. Un
aggiornamento di pandoc negli host basterebbe a svuotare le slide di tutti i
fork senza che cambi un file del repo.

Spostare il pin alla 6.0.2, come ha fatto `danea-auto`, avrebbe spostato il
guasto sugli host con pandoc vecchio. Il rimedio è quello di
`kb/view.md` («Derivata implica verificata»): la build **rompe invece di
degradare**. La soglia è verificata nel changelog di pandoc:
la 3.12 (2026-09-27) corregge i percorsi del template per reveal 6 (#11907),
la 3.11 scrive ancora quelli della 5. La build (oggi
`o3/view/build.py`) legge quindi
la versione di pandoc e sceglie `reveal.js@6.0.2` da 3.12 in su,
`reveal.js@5.1.0` sotto; se non riesce a leggerla si ferma con un errore. Una
slide bianca è una vista che inganna senza che nessuno lo veda.

Entrambi i fix sono nel canone dal 2026-10-01. Con pandoc 3.7.0.2 l'output è
identico; i rami 3.12 e versione illeggibile sono provati con un pandoc
simulato. La propagazione è chiusa il 2026-10-02: i sei hanno recepito i due
fix copiando `build.py`, e la prescrizione è potata. Il primo collaudo reale
su Windows (`danea-auto`, pandoc 3.12) ha confermato reveal.js 6.0.2 e ha
trovato due altre assunzioni da host Linux, corrette nel canone lo stesso
giorno: i link `file:` e `C:\…` passavano il presidio come esterni, e le
viste restavano LF solo grazie a Prettier (ora `newline="\n"` e
`.gitattributes`).

Il gate di freschezza assumeva lo stesso toolchain: con pandoc diversi tra
host la stessa fonte dava HTML diversi, e un commit fatto dall'host
«sbagliato» portava rumore presentato come freschezza. In `metodo` la
tensione si è sciolta con l'uscita di `view/` da git (`9b9597f`): il gate
verifica senza confrontare l'output, e la vista pubblicata dichiara il
toolchain che l'ha resa. Negli adottanti che versionano ancora `view/` resta
finché non recepiscono la prescrizione.

## Tensioni aperte

- la regola regge finché il template di pandoc non cambia di nuovo i
  percorsi. Il controllo ferma solo una versione illeggibile: un cambio
  futuro tornerebbe a dare slide bianche senza errori, finché qualcuno non
  aggiorna la soglia in `build.py`. Una verifica che i percorsi dei plugin
  esistano davvero chiuderebbe il buco, ma chiede la rete durante la build:
  non si fa finché il caso non si ripresenta.
