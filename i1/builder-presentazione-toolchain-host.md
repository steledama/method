---
ciclo: runtime
---

# Segnale: i builder della presentazione assumono il toolchain degli host Linux

Data: 2026-10-01 · Fonte: danea-auto — `i3/allineamento-metodo.md`
(adattamenti del fork dei builder, `078abe8`), verificato da `/adottanti`

## Il segnale

`danea-auto` ha forkato per la prima volta i builder di `presentation/` da
`47d8204` e li fa girare su Windows, da PowerShell via `bash.exe`. Per farli
funzionare ha dovuto cambiarne due punti. Il suo marker dice che entrambi
«valgono per qualunque fork e vanno fatti risalire al canone»:

- **codifica**: `build_lists.py` chiama pandoc con `text=True` e senza
  `encoding`. Su Windows la codifica di default è cp1252 e la build va in
  errore, poi resta appesa. Il fork passa `encoding="utf-8"`
  alle due chiamate;
- **versione di reveal.js**: il canone fissa `reveal.js@5.1.0` in
  `build-presentation.sh`. Pandoc 3.12 scrive i percorsi dei plugin nella
  forma di reveal 6 (`dist/plugin/notes.js`); con la 5.1.0 quei file non
  esistono e le slide restano bianche. Il fork fissa `reveal.js@6.0.2`.

## Cosa è stato verificato

- il canone (`o3/build_lists.py`, `render_markdown`) ha davvero le due
  chiamate senza `encoding`;
- `deck` e `svezia` hanno pandoc 3.7.0.2, che scrive ancora i percorsi della
  5.x (`plugin/notes/notes.js`): oggi gli host Linux non vedono il problema;
- le viste di `danea-auto` rigenerate su `svezia` differiscono da quelle
  versionate solo nel CSS di default di pandoc: lo stesso sorgente dà HTML
  diversi con due versioni del toolchain.

## Perché conta

Il pin di reveal.js è accoppiato alla versione di pandoc, che il canone non
fissa: un aggiornamento di pandoc negli host Linux (nixpkgs) lascerebbe
bianche le slide di tutti i fork senza che nessun file del repo cambi. La
codifica è un'assunzione di piattaforma che finora nessun fork aveva
attraversato. Il primo è un rischio latente per tutti, il secondo un difetto
di portabilità che oggi tocca un solo adottante.
