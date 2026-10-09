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
- La strategia di sincronizzazione va scelta esplicitamente: `pull --rebase`
  è un candidato, non un prerequisito già deciso. Un push rifiutato non si
  forza e rende visibile l'arresto (caso reale in `method` il 2026-10-08).
- Dove un push innesca un rilascio (`bi`), il battito eredita la scelta
  locale: in `bi` il push resta su richiesta quando i commit toccano il
  codice eseguito dal ciclo.

## Confronto e risultato richiesti

Le capacità delle opzioni sopra sono ipotesi da verificare sulle fonti
correnti durante la ricerca. Confrontarle sullo stesso bisogno: accesso alle
fonti dichiarate in World, durata e costo, credenziali, ambiente riproducibile,
isolamento del lavoro, concorrenza e recupero. La ricerca può partire subito;
la scelta esecutiva deve rispettare i criteri concordati per il pilota.

Un solo host non impedisce due sessioni sullo stesso checkout. La proposta
operativa deve precisare comportamento e arresto per checkout sporco,
conflitto, timeout, sessioni sovrapposte e push rifiutato, senza chiedere un
consenso interattivo che nel battito non può arrivare.

Definire una fonte dello stato dei tentativi leggibile dalla home: partenza,
chiusura, arresto e mancata partenza rispetto alla cadenza attesa; distinguere
commit creato, push e pubblicazione. Il solo `git log` non misura un tentativo
interrotto prima del commit. `o3/view/publish.py` e il suo `status.json`
misurano la pubblicazione, non l'esecuzione di `eval`/`exec`.

Chiusura: confronto documentato e scelta del custode per il pilota, protocollo
dei casi di arresto, contratto della fonte per la home e prescrizione di
attivazione locale. L'host è governato dal suo repository: la scelta qui non
attiva uno scheduler né modifica gli adottanti.
