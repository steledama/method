---
sintesi: "Il ciclo autonomo gira da un timer systemd dichiarato in un unico modulo nixos, con Claude Code non interattivo: un file di decisioni per repo e un meccanismo generico. Costruito e collaudato al gradino 0 su deck e svezia. Riaperto il 2026-10-21: portare il meccanismo nel metodo, indipendente dal sistema operativo, a tenuta stagna per repo; problema esposto con domande aperte."
ciclo: dev
---

# Dove gira il ciclo autonomo

Il ciclo autonomo è un giro `eval all` → `exec all` che chiude con un commit e il
push, senza custode.

## Scelta

Decisa dal custode il 2026-10-11.

- **Scheduler**: timer systemd sull'host, dichiarato in `nixos`. Versionato e
  riproducibile, sopravvive ai riavvii, vede checkout, `gdrive` e superfici
  ssh. Scartati `/loop` (vive nella sessione, non versionato) e le routine
  cloud (un clone dal remoto non vede checkout locali né superfici private).
- **Harness**: solo Claude Code, `claude -p`. Il confronto con Codex e pi
  nasceva dal timore di dipendere da un solo fornitore; in questa fase
  complicava senza beneficio. Se servirà cambiare, si valuteranno le opzioni
  di quel momento.
- **Prova**: su repo reali con il servizio reale, non su cloni usa e getta.
  La gradualità sta nei gradini del [pilota](pilota-ciclo-autonomo.md), non in un
  ambiente di prova separato.

## Forma del modulo

Un unico modulo in `nixos`, con le decisioni separate dal meccanismo:

- **File delle decisioni**: per ogni repo host, cadenza, orario, tempo
  massimo e stato (`manuale`: unità presente, avvio solo a mano; `timer`:
  schedulato). Il campo `host` ha un solo valore: «un solo host tiene il
  ciclo autonomo di un repo» vale per costruzione. `danea-auto` vi compare come voce
  dichiarata «fuori nixos (Task Scheduler)», così il quadro resta completo.
- **Meccanismo generico**: su ogni host genera le unità dei soli repo
  assegnati a lui. Tiene in un posto l'invocazione, il tempo massimo
  (`RuntimeMaxSec`), il lock contro sessioni sovrapposte sullo stesso
  checkout, il log dei tentativi e la fonte di stato per la home. Il registro
  di cadenza di `/manutenzione` non è un lock fra sessioni: serve un lock
  locale.

Confine: `nixos` decide **dove e quando**, il repo decide **cosa**. Prompt
del giro, permessi del ciclo autonomo e perimetro degli atti (`autonomy.md`) vivono
nel repo; il modulo invoca senza sapere cosa fa il giro (cfr.
`kb/method-development.md`, «dichiara e taci»). La scelta qui non attiva lo
scheduler: l'attivazione vive in `nixos`.

Due recinti, in quest'ordine (ricognizione di `salute`, 2026-10-11):

- **L'unità** è il recinto vero: percorsi in sola lettura o inaccessibili
  (`ReadOnlyPaths`, `InaccessiblePaths`), lock, tempo massimo. Le regole Bash
  dell'harness non coprono redirect e sottoprocessi.
- **I permessi dell'harness** sono il secondo: un file del solo ciclo autonomo,
  versionato nel repo e passato all'unità con `--settings`, non
  `.claude/settings.json`, che vale anche per le sessioni interattive. Con
  `--setting-sources project` l'unità esclude `settings.local.json` e le
  impostazioni utente, che possono concedere atti non voluti nel ciclo autonomo (in
  `salute` su `deck`, cancellazioni su Drive e calendario).

## Invocazione

Verificato sull'help il 2026-10-11 (Claude Code 2.1.295): `claude -p` con
`--permission-mode dontAsk` (ogni permesso non concesso è negato senza
chiedere), `--no-session-persistence`, `--max-budget-usd`,
`--output-format json`. L'ambiente dell'unità evita i blocchi interattivi:
stdin da `/dev/null`, `GIT_TERMINAL_PROMPT=0`,
`GIT_SSH_COMMAND="ssh -o BatchMode=yes"`, `PAGER=cat`.

Verificato ai gradini 0 di `salute` (2026-10-11) e `crm` (2026-10-15),
cfr. [pilota](pilota-ciclo-autonomo.md): le skill del repo si invocano da
`claude -p`, i permessi negati arrivano alla chiusura e ingialliscono il
semaforo, Claude e il push via ssh si autenticano nell'unità senza agent.
Resta da osservare l'arresto per `RuntimeMaxSec` e la sua traccia nel
journal: nessun giro ha ancora toccato il tempo massimo.

## Vincoli comuni

- Sincronizzazione: la skill `cycle` fa `git pull --ff-only` a working tree
  pulito prima di ogni atto e si ferma se fallisce. Un push rifiutato non si
  forza e rende visibile l'arresto (caso reale in `method` il 2026-10-08).
- Dove un push innesca un rilascio (`bi`), il ciclo autonomo eredita la scelta
  locale: in `bi` il push resta su richiesta quando i commit toccano il
  codice eseguito dal ciclo.

## Arresti e fonte di stato

La proposta operativa deve precisare comportamento e arresto per checkout
sporco, conflitto, timeout, sessioni sovrapposte e push rifiutato, senza
chiedere un consenso interattivo che nel ciclo autonomo non può arrivare.

Definire una fonte dello stato dei tentativi leggibile dalla home: partenza,
chiusura, arresto e mancata partenza rispetto alla cadenza attesa; distinguere
commit creato, push e pubblicazione. Il solo `git log` non misura un tentativo
interrotto prima del commit. `o3/view/publish.py` e il suo `status.json`
misurano la pubblicazione, non l'esecuzione di `eval`/`exec`.

## Da ripensare: il meccanismo nel metodo, non nell'host

Riaperto dal custode il 2026-10-21. Per ora il problema si espone e basta,
con le domande aperte, per tornarci con calma. Nessuna scelta è presa: la
Scelta del 2026-10-11 e il modulo in `nixos` restano in vigore finché il
custode non decide.

### Il segnale

Il 2026-10-21 alle 13:00 il giro di `economia` si è fermato per sessione
aperta del custode, un arresto corretto. La riga dell'arresto l'ha scritta
`ciclo-sessioni`, che è un `ExecStartPre` dell'unità e gira prima di
`ciclo-avvio`. Per questo la riga sta in `~/.local/state/ciclo/economia/` e
non in `i1/giri` dichiarato dal repo. La home ha mostrato una «partenza
mancata» senza motivo
([cattura](../i1/arresto-economia-fuori-giri-2026-10-21.md)). Il guasto è
piccolo, ma mostra due cose del disegno attuale che il custode non vuole:

- una parte dell'intelligenza del repo vive in un altro repo: partenza,
  controlli, chiusura e forma del log sono circa 440 righe di bash in
  `nixos` `o3/modules/home/ciclo/`;
- un repo, `nixos`, scrive un log importante per un altro repo.

### L'obiettivo del custode

Uno script del metodo, uguale per tutti i repo, lanciato con parametri. Ogni
repo lo gestisce da sé, a tenuta stagna rispetto agli altri. Il metodo deve
restare indipendente anche dal sistema operativo, oltre che da harness e
modello (cfr. [session-messaging](../kb/session-messaging.md)). NixOS è la
distribuzione preferita del custode, ma non la più diffusa, e `danea-auto`
gira su Windows. Un ciclo autonomo che esiste solo come modulo NixOS lega il
metodo a quel sistema.

### Come fa oggi `danea-auto`

Rilevato da `origin/main` di `danea-auto` il 2026-10-21, `85b27f5`:

- il lanciatore è nel repo: `o3/scheduler/ciclo_autonomo.py`, Python, 582
  righe. Fa su Windows quello che l'unità di `nixos` fa altrove: lock,
  sessioni aperte, tree pulito e divergenza, `claude -p` con tetto di tempo e
  di costo, chiusura scritta sempre;
- lo scheduler è quello del sistema: `crea_task_ciclo.ps1` registra un task
  del Task Scheduler alle 08:10. La password resta nel Task Scheduler, fuori
  dal repo;
- scrive direttamente nel proprio `i1/giri/tentativi.jsonl`, con la stessa
  forma delle righe e gli stessi codici d'uscita dell'unità (15 sessione
  aperta, 75 lock, …). La vista `o3/view/ciclo.py` la legge senza
  differenze;
- il recinto è solo l'harness, per decisione del custode del 2026-10-20:
  Windows non ha l'equivalente della sandbox dell'unità systemd;
- ha controlli propri dell'host: lo slot del run orario, la scadenza del
  login, i percorsi protetti nel pull d'avvio. La regola sulle sessioni è più
  severa: qualunque `claude.exe` sull'host, non solo nel checkout.

Il contratto, cioè la forma dei tentativi e i codici d'arresto, esiste quindi
già due volte, in due linguaggi: bash in `nixos` e Python in `danea-auto`.
Il lato di lettura è invece già canonico: `o3/view/ciclo.py` è identico in
`method`, `nixos` e `danea-auto`. Manca il lato di scrittura.

### Domande aperte

- **Confine a tre.** Cosa va nello script canonico di `method`, cosa nel
  file di parametri del repo e cosa resta all'host? L'orario e il tetto di
  costo sono una decisione del repo o dell'host?
- **Recinto e sistema operativo.** La sandbox systemd esiste solo su Linux.
  Il denominatore comune basta come recinto, cioè i permessi dell'harness,
  come in `danea-auto`? La sandbox dell'host diventerebbe allora un rinforzo
  facoltativo. Oppure così si abbassa la soglia dove oggi c'è di più? E un
  repo che dichiara da solo i propri parametri può allargarsi il recinto?
- **Controllo delle sessioni.** Su Linux leggere la cwd degli altri processi
  richiede di stare fuori dal namespace; su Windows si guarda l'intero host.
  Serve una regola sola, per checkout o per host? Come resta agnostica
  rispetto all'harness, visto che i rollout Codex sono già un caso
  (`nixos` `101e32b`)?
- **Codice privilegiato da un checkout.** Se una parte dello script gira
  fuori dal recinto, eseguirla dal checkout vivo di `method` la espone a
  ogni commit. Fissarla a una versione, per esempio un input del flake o un
  tag, costa un aggiornamento a ogni modifica. Come arriva lo script
  all'adottante: symlink al checkout come i nodi, copia come la vista, o
  versione fissata? E su `danea2` c'è un checkout di `method`?
- **Linguaggio.** Python è già lo strumento di `o3/` e del lanciatore di
  `danea-auto`, ed è multipiattaforma; bash è quello di oggi in `nixos`.
  Quale dipendenza dall'interprete si accetta?
- **Scheduler.** Ogni sistema ha il suo: timer systemd, Task Scheduler,
  launchd, cron. La registrazione del trigger è un adattatore minimo del
  metodo, per esempio uno script che genera unità o task? Oppure resta alla
  configurazione dell'host, come il modulo `nixos` e il `.ps1` di
  `danea-auto`?
- **Controlli locali.** Lo slot di `danea-auto`, `requiresProduction` di
  `bi`, i `fetch` del perceive di `method` e i wrapper `gog` di `economia`
  sono controlli locali. Diventano punti di aggancio del repo? Dove passa la
  linea fra generico e locale?
- **Harness.** Lo script invoca `claude -p`. Lo scope resta quello deciso il
  2026-10-11, cioè solo Claude Code. Resta da capire se l'invocazione vada
  isolata in un punto, per lasciare aperto il cambio senza costruirlo ora.
- **Migrazione.** Si parte da `method` stesso, o da `danea-auto` come prova
  di portabilità? Il modulo `nixos` si riduce ad adattatore mentre le due
  implementazioni attuali continuano a girare? Il guasto del log
  dell'arresto si chiude dentro la migrazione, non con una pezza in `nixos`
  (scelta del custode, 2026-10-21).

## Chiusura

Modulo dichiarato in `nixos` e collaudato al gradino 0 sui due host,
protocollo dei casi di arresto, contratto della fonte per la home e
prescrizione di attivazione locale per gli adottanti.
