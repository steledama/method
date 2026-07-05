---
sintesi: "La prescrizione della ristrutturazione dell'atrio è attiva (o3/ristrutturazione-atrio.md). Il pilot nixos ha collaudato la migrazione strutturale (2026-07-05, idempotenza provata), ma il runbook è cresciuto dopo il pilot: il passo 1 — l'inventario dell'atrio, corpo di dominio ed eccezioni dichiarate — è ora il cuore della migrazione e resta da eseguire su tutti e quattro. Il task chiude quando tutti l'hanno recepita per intero."
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

- `nixos` — **recepito parzialmente** (pilot, 2026-07-05): migrazione
  strutturale completa via `/method-review` (marker a `0f74186`,
  `status: aligned`, ri-esecuzione idempotente); i due cocci del pilot (risync
  `kb_tools.py`; facet su item, non su indici) sono incisi nel runbook
  (`9033223`). Resta il **passo 1 — inventario dell'atrio**, introdotto nel
  runbook dopo il pilot: corpo di dominio da dichiarare nella legenda del
  README, `secrets/` e `result` da classificare.
- `bi` — da eseguire; è il caso più costoso dell'inventario e il suo verdetto
  di fit il più informativo per l'osservatorio
- `economia` — da eseguire
- `salute` — da eseguire

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
