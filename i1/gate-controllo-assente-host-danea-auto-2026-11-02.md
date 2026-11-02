---
ciclo: runtime
---

# Segnale: un controllo del gate senza il suo strumento sull'host ferma ogni commit

Data: 2026-11-02 · Fonte: inoltro della sessione `danea-auto` su `deck` via
Herdr, su richiesta del custode; `danea-auto` `9839b98` letto su `origin`

## Il segnale

`danea-auto` dichiara in `o3/commit_gate.toml` un controllo PowerShell,
`o3/tools/verifica_commit.ps1`, senza `quando`. Su `deck` PowerShell non c'è,
e `o3/commit_gate.py prima` dà «non disponibile, FALLITO» (righe 96-98): il
gate ferma anche un commit di soli documenti in `i1/`, fuori da ciò che il
controllo verifica. Un formatter assente invece viene saltato (righe 82-83).

Il custode ha scelto di restringere il controllo alle superfici che verifica
(`9839b98`): `*.ahk`, `kb/*` e `o3/*`. Poiché `quando` accetta un solo glob,
il profilo ripete tre volte la stessa voce.

## Cosa c'è da valutare

- Il `FALLITO` per un controllo assente è voluto: un controllo non deve
  passare in silenzio. Resta da capire se basti dichiarare sempre `quando`
  per i controlli legati a uno strumento di piattaforma, o se il gate debba
  distinguere fra «assente ma non dovuto» e «assente e dovuto».
- `quando` con un solo glob costringe a duplicare le voci quando un controllo
  copre più superfici.
- Il messaggio dice anche che il gate legge `git status` e non l'indice. Nella
  skill `/commit` canonica il gate gira prima dello staging, quindi è
  coerente. `danea-auto` dichiara invece che il suo `verifica_commit.ps1` legge
  l'indice e va lanciato dopo lo staging: è un ordine locale da verificare,
  non un difetto del canone.

Per ora è un caso solo, su un host per cui il repository non è pensato.
