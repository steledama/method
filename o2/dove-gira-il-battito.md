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

## Modo non interattivo dei tre harness

Verificato il 2026-10-11 sull'help delle versioni installate dal profilo
`nixos` su `deck`: Claude Code 2.1.292, Codex CLI 0.161.0, pi 1.0.4.

- **Claude Code**: `claude -p` (`--print`), «non-interactive output».
  Sessione non salvata con `--no-session-persistence`, tetto di spesa con
  `--max-budget-usd`, permessi con `--permission-mode`
  (`dontAsk`, `acceptEdits`, `auto`, `bypassPermissions`…) e
  `--allowedTools`/`--disallowedTools`, esito con `--output-format json`.
- **Codex**: `codex exec`, «Run Codex non-interactively». Sessione non
  salvata con `--ephemeral`, sandbox `read-only`, `workspace-write` o
  `danger-full-access`, approvazioni instradate a una revisione automatica
  con `--approve-for-me`, eventi JSONL con `--json`, ultimo messaggio su
  file con `-o`. Nessun tetto di spesa fra le opzioni.
- **pi**: `pi -p`, «process prompt and exit». Sessione non salvata con
  `--no-session`, allowlist e denylist degli strumenti con `--tools` ed
  `--exclude-tools`, esito JSON con `--mode json`. Nell'help non compare un
  sistema di permessi né un tetto di spesa; `--approve` riguarda la fiducia
  nei file di progetto.

In tutti e tre il processo termina quando l'agente chiude il turno finale:
lo scheduler vede l'uscita e il codice di ritorno. La chiusura non è
garantita se un comando resta appeso (ssh senza risposta, un prompt
interattivo, un pager): serve un tempo massimo imposto dallo scheduler,
per esempio `RuntimeMaxSec` nell'unità systemd, e il tempo scaduto è un
arresto da rendere visibile.

Da provare con un giro reale, non leggibile dall'help:

- che `/eval` e `/exec` si invochino nel modo non interattivo: le skill
  vivono in `.claude/skills/` con wrapper in `.codex/skills/`; pi le carica
  con `--skill` e la scoperta automatica nel progetto non è verificata;
- cosa succede a una richiesta di permesso non coperta: rifiuto e
  prosecuzione, oppure arresto;
- se `workspace-write` di Codex consente la rete, che servono a push e ssh;
- l'autenticazione headless sull'host scelto per ciascun harness.

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
