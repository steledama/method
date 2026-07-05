---
sintesi: "La prescrizione della ristrutturazione dell'atrio è attiva (o3/ristrutturazione-atrio.md). Nixos recepito (rebuild reale su deck incluso); economia eseguita nel working tree con quattro cocci incisi nel runbook — manca il commit locale che la fissa. Restano bi e salute. Il task chiude quando tutti gli adottanti l'hanno recepita per intero."
ciclo: runtime
---

# Recepimento della prescrizione dell'atrio

## Stato

La ristrutturazione dell'atrio (2026-07-04) è la prima divergenza strutturale
del canone dalla forma che i quattro adottanti conoscono. La prescrizione che la
propaga è scritta e attiva: [`o3/ristrutturazione-atrio.md`](../o3/ristrutturazione-atrio.md)
— runbook unico nel lessico del metodo con touchpoint per-repo (la ricetta è
identica in forma per tutti; divergono solo _quali_ file esistono, cfr.
`o3/prescriptions.md`, «Divisione del lavoro»). Include il risync del fork del
cluster presentazione alla home semplificata (cfr. filo `i3/home-minimalista.md`).

Ogni adottante la recepisce col proprio `/method-review` come task locale: il
canone dichiara, la coda resta dell'adottante (`method-development`, «dichiara e
taci»).

## Recepimento

- `nixos` — **recepito** (pilot, 2026-07-05): migrazione strutturale completa
  via `/method-review` (marker a `0f74186`, `status: aligned`, ri-esecuzione
  idempotente); i due cocci del pilot (risync `kb_tools.py`; facet su item, non
  su indici) sono incisi nel runbook (`9033223`). Il passo 1 ha poi corretto il
  canone: non basta dichiarare il corpo di dominio in root; bisogna spostare il
  contenuto versionato negli spazi funzionali. Nixos lo ha eseguito spostando
  `home/`, `hosts/`, `modules/`, `identity/`, `patches/` e `scripts/` sotto
  `o3/` come o3-runtime; `flake.nix`/`flake.lock` restano eccezioni di
  toolchain; `secrets/` resta eccezione non versionata/materia del Mondo;
  `result*`, `world` e cache sono traffico runtime gitignored.
- `bi` — da eseguire; è il caso più costoso dell'inventario e il suo verdetto
  di fit il più informativo per l'osservatorio: i contenuti versionati vanno
  ricollocati, non solo classificati
- `economia` — **eseguita nel working tree, commit mancante** (2026-07-05,
  marker a `77d8225`, `status: aligned`): ricollocazione completa (strumenti,
  script, libreria, config e test → `o3/`; viste → `presentation/`; legenda
  dell'atrio voce-per-voce; verdetto di fit 0 eccezioni), audit/facet/tasks
  puliti e viste rigenerate. Quattro cocci del secondo giro, incisi nel runbook:
  i3 a file-per-filo (non indice-wrapper sul monolite, riferimento
  `method/i3/…` rotto per costruzione); un solo indice per collezione
  (`o3/tools.md` orfano accanto a `prescriptions.md`); la legenda copre
  l'`ls -A`, dotfile inclusi; la migrazione chiude solo col commit via gate
  `/commit` — marker avanzato su working tree sporco è stato incoerente. In
  loco resta anche il symlink `memory` (store harness vuoto): anti-pattern da
  rimuovere, non da classificare come membrana.
- `salute` — da eseguire

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
