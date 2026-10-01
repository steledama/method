---
ciclo: dev
---

# I builder della presentazione assumono un toolchain che non dichiarano

**Misura**: «Custodire un canone coerente e fedele alle fonti» (`goal.md`,
obiettivo 1).

## Verdetto

Il segnale viene da `danea-auto` (2026-10-01), il primo adottante che fa
girare i builder di `presentation/` su Windows. Per farli funzionare ha
dovuto cambiare due punti del canone. Tutti e due sono verificati nel
codice di `metodo`, e tutti e due vengono dalla stessa assunzione taciuta: il
toolchain è quello degli host Linux di chi li ha scritti.

**Codifica.** `o3/build_lists.py` chiama pandoc con `text=True` e senza
`encoding`: Python usa la codifica di default della piattaforma, cp1252 su
Windows, e la build fallisce. Il fix di `danea-auto`, `encoding="utf-8"`
nelle due chiamate, entra nel canone così com'è. Non cambia nulla sugli
host Linux, dove la codifica di default è già UTF-8.

**reveal.js accoppiato a pandoc.** `o3/build-presentation.sh` fissa
`reveal.js@5.1.0`, ma i percorsi dei plugin li scrive pandoc, secondo la
propria versione. Pandoc 3.12 scrive quelli di reveal 6
(`dist/plugin/notes.js`); con la 5.1.0 quei file non esistono e le slide
restano bianche. `deck` e `svezia` hanno pandoc 3.7.0.2, che scrive ancora i
percorsi della 5.x: oggi gli host Linux non vedono il problema. Un
aggiornamento di pandoc negli host basterebbe a svuotare le slide di tutti i
fork senza che cambi un file del repo.

Spostare il pin alla 6.0.2, come ha fatto `danea-auto`, avrebbe spostato il
guasto sugli host con pandoc vecchio. Il rimedio è quello di
[vista-derivata-e-verificata](vista-derivata-e-verificata.md): la build
**rompe invece di degradare**. La soglia è verificata nel changelog di pandoc:
la 3.12 (2026-09-27) corregge i percorsi del template per reveal 6 (#11907),
la 3.11 scrive ancora quelli della 5. `o3/build-presentation.sh` legge quindi
la versione di pandoc e sceglie `reveal.js@6.0.2` da 3.12 in su,
`reveal.js@5.1.0` sotto; se non riesce a leggerla si ferma con un errore. Una
slide bianca è una vista che inganna senza che nessuno lo veda.

Entrambi i fix sono nel canone dal 2026-10-01. Con pandoc 3.7.0.2 l'output è
identico; i rami 3.12 e versione illeggibile sono provati con un pandoc
simulato. La propagazione vive in `o3/toolchain-builder-presentazione.md`.

## Tensioni aperte

- **Il gate di freschezza assume lo stesso toolchain.** Il check i2 di
  `/commit` legge come stale tutto ciò che cambia rigenerando. Con pandoc
  diversi tra host, la stessa fonte dà HTML diversi: le viste di
  `danea-auto` rigenerate su `svezia` cambiano nel CSS di default di pandoc,
  non nel contenuto. Un commit fatto dall'host «sbagliato» porterebbe rumore
  di toolchain presentato come freschezza. Per ora è un solo adottante su
  un host diverso: si dichiara, non si risolve. Se un secondo caso lo
  mostra, la domanda è se il canone debba dichiarare una versione di
  pandoc;
- la regola regge finché il template di pandoc non cambia di nuovo i
  percorsi. Il controllo ferma solo una versione illeggibile: un cambio
  futuro tornerebbe a dare slide bianche senza errori, finché qualcuno non
  aggiorna la soglia nel wrapper. Una verifica che i percorsi dei plugin
  esistano davvero chiuderebbe il buco, ma chiede la rete durante la build:
  non si fa finché il caso non si ripresenta.
