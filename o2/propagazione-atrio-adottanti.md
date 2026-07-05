---
sintesi: "La prescrizione della ristrutturazione dell'atrio è attiva (o3/ristrutturazione-atrio.md) e il pilot nixos l'ha recepita (2026-07-05, marker a 0f74186, idempotenza provata): il runbook è collaudato, i cocci del pilot sono incisi. Restano bi, economia e salute; il task chiude quando tutti e quattro l'hanno recepita."
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

- `nixos` — **recepito** (pilot, 2026-07-05): migrazione completa via
  `/method-review`, marker avanzato a `0f74186`, `status: aligned`,
  ri-esecuzione idempotente. I due cocci del pilot (risync `kb_tools.py` con
  esclusione del catalogo omonimo; facet su item, non su indici) sono incisi
  nel runbook (`9033223`); oltre quelli, la ricetta è passata senza attriti.
- `bi` — pronto a eseguire (runbook collaudato)
- `economia` — pronto a eseguire
- `salute` — pronto a eseguire

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
