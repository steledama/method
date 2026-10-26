---
sintesi: "Portare il lanciatore del ciclo autonomo nel metodo: uno script canonico uguale per tutti i repo, lanciato con parametri, a tenuta stagna per repo e indipendente dal sistema operativo. Problema esposto con domande aperte, nessuna scelta presa."
ciclo: dev
---

# Lanciatore del ciclo nel metodo

## Origine

Nasce il 2026-10-26 dalla chiusura del task «Dove gira il ciclo autonomo»,
riaperto dal custode il 2026-10-21. Quel task aveva deciso il 2026-10-11 il
meccanismo in uso: un timer systemd dichiarato in un unico modulo `nixos`,
con `claude -p` come solo harness. Scartati `/loop`, che vive nella sessione
e non è versionato, e le routine cloud, che da un clone non vedono checkout
locali né superfici private. Confine: `nixos` decide dove e quando, il repo
decide cosa (prompt, permessi del giro, `autonomy.md`). Due recinti:
l'unità, con percorsi in sola lettura, lock e tempo massimo, e i permessi
dell'harness passati con `--settings` e `--setting-sources project`. Il
meccanismo è collaudato e in esercizio in sei repo
(`i3/ciclo-autonomo.md`); la sua forma vive in `kb/cicli.md` di `nixos` e
nella prescrizione `o3/ciclo-autonomo.md`. La storia della scelta resta in
git.

Il meccanismo resta in vigore finché il custode non decide su questo task.
Per ora il problema si espone e basta, con le domande aperte, per tornarci
con calma.

## Il segnale

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

## L'obiettivo del custode

Uno script del metodo, uguale per tutti i repo, lanciato con parametri. Ogni
repo lo gestisce da sé, a tenuta stagna rispetto agli altri. Il metodo deve
restare indipendente anche dal sistema operativo, oltre che da harness e
modello (cfr. [session-messaging](../kb/session-messaging.md)). NixOS è la
distribuzione preferita del custode, ma non la più diffusa, e `danea-auto`
gira su Windows. Un ciclo autonomo che esiste solo come modulo NixOS lega il
metodo a quel sistema.

## Come fa oggi `danea-auto`

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

## Domande aperte

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
- **Cambio d'orario.** Il 2026-10-21 lo switch che spostava `economia`
  dalle 13:00 alle 14:00 (`nixos` `7c9fd47`) ha riavviato il timer, e il
  giro è partito subito, alle 16:01, nonostante `Persistent=false`.
  L'ultimo avvio era delle 13:00 e le 14:00 erano già passate. Il giro si è
  fermato per sessione aperta. Ogni scheduler ha regole proprie sugli avvii
  dopo un cambio o un riavvio. Il metodo deve garantire che cambiare
  l'orario non lanci un giro fuori tempo, per esempio con un controllo
  dello slot nello script, come fa `danea-auto`? Oppure basta dichiararlo
  come comportamento noto dell'adattatore?
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

## Da osservare intanto

L'arresto per `RuntimeMaxSec` e la sua traccia nel journal: nessun giro ha
ancora toccato il tempo massimo di 45 minuti. Il contratto del lanciatore
dovrà dire come lo registra.

## Criterio di chiusura

Il custode decide le domande aperte. Lo script canonico gira in `method` e
in almeno un adottante su un altro sistema operativo, scrive i tentativi
nel `i1/giri/` del repo, arresti prima del giro compresi, e il modulo
`nixos` si riduce all'adattatore dello scheduler. Riga del plan, voce in
`o2/tasks.md` e questo file si rimuovono nello stesso commit.

Connessioni:

- [pilota-ciclo-autonomo](pilota-ciclo-autonomo.md)
- [home-fatto-da-fare](home-fatto-da-fare.md)
- [session-messaging](../kb/session-messaging.md)
