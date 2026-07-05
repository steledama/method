---
sintesi: "La prescrizione della ristrutturazione dell'atrio è attiva (o3/ristrutturazione-atrio.md). Il pilot nixos ha collaudato la migrazione strutturale e poi forzato la regola piena: ogni contenuto versionato va collocato nello spazio funzionale previsto; ciò che non entra resta eccezione dichiarata e pesa nel verdetto di fit. Il task chiude quando tutti gli adottanti l'hanno recepita per intero."
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
- `economia` — da eseguire
- `salute` — da eseguire

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
