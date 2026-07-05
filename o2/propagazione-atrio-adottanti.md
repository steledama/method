---
sintesi: "La prescrizione della ristrutturazione dell'atrio è scritta e attiva (o3/ristrutturazione-atrio.md): runbook unico con touchpoint per-repo, pilot nixos. Questo task traccia il recepimento — ogni adottante la esegue col proprio method-review come task locale; chiude quando tutti e quattro l'hanno recepita."
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

Pilot `nixos`: i suoi cocci raffinano la prescrizione prima degli altri tre.

- `nixos` — da eseguire (pilot)
- `bi` — in attesa del pilot
- `economia` — in attesa del pilot
- `salute` — in attesa del pilot

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
