---
sintesi: "Un confronto con pro e contro delle soluzioni per far girare il battito eval → exec a intervalli, da cui il custode sceglie quella per il pilota."
ciclo: dev
---

# Dove gira il battito

Il battito è un giro `eval all` → `exec all` che chiude con un commit e il
push, senza custode. Dove e come lo si esegue è aperto: il custode vuole
confrontare le soluzioni prima di scegliere.

## Opzioni da approfondire

- **Timer sull'host dichiarato in `nixos`**, che lancia Claude Code in modo
  non interattivo. Versionato e riproducibile, sopravvive ai riavvii, vede
  checkout, `gdrive` e superfici ssh. Da capire: credenziali sull'host,
  permessi in allowlist, log degli esiti.
- **Sessione permanente di Claude Code con `/loop`**. Nessuna
  infrastruttura. Da verificare: quanto vivono i loop di sessione, cosa
  succede a chiusura del terminale o al riavvio, crescita del contesto. Una
  schedulazione che vive solo nella sessione non è versionata.
- **Routine cloud (`/schedule`)**. Nessun host da tenere acceso. Gira su un
  clone dal remoto: non vede i checkout locali né le superfici private.
- **Task Scheduler di Windows** per `danea-auto`, l'unico adottante fuori da
  Linux, che lo usa già per i suoi giri di dominio.

## Vincoli comuni

- Un solo host tiene il battito di un repo.
- Il giro parte con `pull --rebase`; un push rifiutato non si forza e chiude
  il giro come rosso (caso reale in `method` il 2026-10-08).
- Dove un push innesca un rilascio (`bi`), il battito eredita la scelta
  della prescrizione `push-autonomo`.
