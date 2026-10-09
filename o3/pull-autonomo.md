---
data: 2026-10-09
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Il pull non attende il custode

## Cosa e perché

Il custode ha deciso il 2026-10-09: **l'agente fa il pull del branch
corrente da `origin` senza richiesta**, a inizio sessione, prima di un giro e
quando un confronto trova il checkout indietro. Si usa `git pull --ff-only`, e
solo a working tree pulito; con modifiche locali o un branch divergente non si
fa merge né rebase da soli, ci si ferma e si riferisce. In `method` la regola
vive in `CLAUDE.md` («Pull remoto») e nel passo 1 della
[skill canonica `/method`](../.claude/skills/method/SKILL.md), che prima
vietava fetch e pull automatici.

È il gemello del push autonomo dell'08/10: senza il pull, un giro parte da un
checkout indietro e confronta col canone una fotografia vecchia, e ogni
riallineamento resta un gesto del custode. Il pull del checkout di `method`
porta canone e prescrizioni ma non applica nulla: il recepimento resta
soggetto al gate di `/method`.

L'autorizzazione vale per il repository in cui l'agente lavora e per il
checkout di `method` che legge. Non vale per i checkout di altri repository,
dove può lavorare un'altra sessione: lì bastano `fetch` e la lettura di
`origin`.

## Ricetta per il /method locale

1. Nel passo 1 del fork di `/method`, sostituire il divieto di fetch e pull
   con l'aggiornamento del checkout di `method` (`pull --ff-only` se pulito,
   altrimenti dichiarare il limite), come nel canone. Rimuovere dal marker i
   limiti che dipendevano dal divieto, per esempio «`/method` non fa fetch».
2. Aggiungere la regola del pull del repository locale alle autorizzazioni
   della bussola (`CLAUDE.md`, `AGENTS.md`), accanto a quella del push.
3. **Residui di dominio**: verificare se il working tree del repository è
   esso stesso produzione, cioè se un processo esegue direttamente i file del
   checkout (Task Scheduler, servizi, `docker compose` che legge la
   configurazione dal checkout). Dove succede, il pull è un rilascio. Due vie:
   lasciare su richiesta il pull di quel checkout, conservando autonomo
   quello di `method`, oppure dichiarare che il rilascio segue il pull. La
   scelta spetta al custode; finché non decide, quel pull resta su richiesta e
   il motivo si scrive nella bussola.
4. Registrare nel marker locale il recepimento o l'adattamento motivato.

## Indizi da verificare sul posto

Lettura del 2026-10-09 dai marker e dai `CLAUDE.md` su `origin`:

- **danea-auto**: le Action del Task Scheduler puntano al working tree, quindi
  un `.ahk` modificato è in produzione allo slot successivo. Il pull del
  repository su `danea2` è un rilascio (passo 3); il pull del checkout Windows
  di `method` resta neutro. Il marker dichiara che il clone di `method` su
  Windows può restare indietro e che `/method` non fa fetch.
- **bi**: `o3/scripts-auto.sh` e `o3/scripts-auto-morning.sh` fanno già
  `git pull` prima di girare, quindi ciò che è su `origin` è già rilasciato
  per costruzione; il pull dell'agente sull'host di produzione anticipa il
  cron. Verificare che non esistano altri esecutori dal working tree.
- **baserow**: la versione dell'immagine è bloccata in `docker-compose.yml`
  nel checkout; un pull non riavvia nulla, ma il successivo avvio dello
  stack (`docker compose up`) userebbe la configurazione nuova. Verificare
  se è un rilascio da dichiarare.
- **crm**: il deploy passa da `o3/tools/deploy.sh` su richiesta esplicita;
  verificare che il servizio non legga file dal checkout.
- **nixos**: `CLAUDE.md` dice che nessun host fa `pull` da solo e che la
  pubblicazione delle viste costruisce l'`HEAD` del checkout locale; un pull
  dell'agente aggiorna le viste servite, non il sistema, che richiede
  `nixos-rebuild`. Riformulare la frase in modo che resti vera.
- **economia**, **salute**: repository di dati e conoscenza; il pull può
  portare catture prodotte da un altro host. Nessun esecutore noto dal
  working tree.
