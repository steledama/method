---
sintesi: "Portare il lanciatore del ciclo autonomo nel metodo: uno script canonico uguale per tutti i repo, lanciato con parametri, a tenuta stagna per repo e indipendente dal sistema operativo. Adottato dal custode il 2026-11-08 il disegno minimale, in Python, dal checkout vivo, con la sandbox accesa dove esiste; da implementare, prima in method."
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
nella prescrizione `ciclo-autonomo`, recepita da tutti e chiusa il
2026-10-28. La storia della scelta e della prescrizione resta in git.

Il meccanismo resta in vigore finché lo script canonico non lo sostituisce.

## Decisioni del custode (2026-11-08)

Adottato il disegno minimale della proposta del 2026-10-29, con queste scelte:

- **Recinto:** i permessi dell'harness, versionati nel repo. La sandbox
  systemd resta accesa dove esiste: «facoltativa» vale per i sistemi che non
  ce l'hanno, come Windows, e non abbassa la soglia su `deck`.
- **Come arriva lo script:** dal checkout vivo di `method`, come il gate, con il
  `pull --ff-only` del checkout all'avvio e la rete in chiusura. Niente versione
  fissata.
- **Linguaggio:** Python.
- **Ordine:** prima `method`, poi `danea-auto` come prova su un altro sistema
  operativo; il modulo `nixos` si riduce dopo.

Le altre domande qui sotto si decidono quando il lavoro le raggiunge.

## Stato

`o3/lanciatore.py` esiste con i test (`tests/test_lanciatore.py`, agente finto su
repository veri) e il timer non lo usa ancora. Stessi codici d'arresto e stessa
forma delle righe dell'unità di `nixos`; `lock` e `settings.json` stanno in
`.git/lanciatore/`, così non serve una cartella di stato fuori dal repo e ogni
arresto finisce in `i1/giri/`, che chiude il guasto dell'origine. Provato il
2026-11-08 con Claude Code 2.1.318 in un repo usa e getta: giro riuscito, tracce
lette dalla vista, 0,06 USD. In `method` i controlli hanno trovato la sessione
aperta (15).

Scelte prese scrivendolo, da rivedere col custode se non tornano:

- tetto di tempo e di costo sono del repo (`o3/ciclo/lanciatore.toml`), l'orario
  resta all'host;
- un giro che tocca un percorso protetto ferma i successivi con
  `.git/lanciatore/fermo`, che toglie una persona: è il «torna al manuale»;
- il lanciatore sta fuori dalla sandbox e `--recinto`, opzione dell'host, mette
  dentro il solo agente. Dentro il namespace `/proc` degli altri processi è
  negato e il pull sui percorsi in sola lettura si romperebbe a metà;
- l'avviso di `attenzione` è copiato nella chiusura, come fa già `danea-auto`.

Confermate dal custode il 2026-11-08, insieme a ciò che ha portato il confronto
con `danea-auto`:

- il profilo `o3/ciclo/lanciatore.toml` è il posto dei parametri del repo:
  `branch`, `minuti`, `budget_usd`, `protetti`, `prima`;
- `prima` è l'unico aggancio locale, uno script Python in `o3/ciclo/` che gira
  prima dell'agente e può fermare (16-19), accorciare il tetto, avvisare o saltare;
- `pull_fermo` ferma con 17 il pull che tocca i percorsi elencati, dove il
  checkout è anche la produzione e il pull è un rilascio. Vuota per default. In
  `danea-auto` elenca i soli `o3/runtime/*` e `o3/scheduler/*`, e la decisione D4
  del 20/10 resta in vigore per la produzione; il recinto lo coprono i protetti
  e la rete in chiusura;
- il lanciatore aggiorna il proprio checkout del canone, salvo
  `--senza-pull-canone`, opzione dell'host. Su `danea2` resta spento: lì il
  canone lo aggiorna il custode in sessione.

Prossimi passi, `danea-auto` per prima:

1. `danea-auto` su `danea2`: profilo e `prima.py` scritti il 2026-11-08, provati in
   un repo di prova con un agente finto. Su Windows reggono `pythonw`, il lock con
   `msvcrt`, la chiusura dell'albero al tetto e i codici 17, 23 e 24
   (`i1/lanciatore-canonico-prova-windows.md` di quel repo). Primo giro vero il
   2026-11-08 alle 16:13, avviato a mano dal Task Scheduler: riuscito in 2 minuti
   e 42 secondi, 1,02 USD, commit `0624d2f` pubblicato, nessun diniego. Il task
   punta ora al lanciatore canonico. Tolti poi `ciclo_autonomo.py` (`22c7aa0`) e lo
   stato in `C:\ciclo\stato` (`9352d4a`); `host-settings.json`, che era `{}`, non
   si fonde più ed è tolto. Il campo `giro` della chiusura fa leggere a
   `commit_gate.py stadi` il giro delle 16:13. Dal resoconto inoltrato il
   2026-11-08: i controlli che si fermavano al primo arresto e il tetto alle :50
   sforato da fetch e pull li chiude `bbe06b4`; l'attesa dello slot anche sotto
   `--controlli` la chiude `LANCIATORE_MODO` (`a063923`), letta da `prima.py` di
   `danea-auto` in `ef7273a`. Provato dal vivo alle 16:39: `--controlli` riporta
   tutti gli arresti. Primo giro dal timer col canone il 2026-11-09 alle 08:10. Il pull che non ferma un cambio del recinto è il disegno
   (rete in chiusura); `exit_status` stringa come `$EXIT_STATUS` di systemd,
   `push` vero senza commit perché vuol dire «niente da pubblicare» e la vista lo
   legge solo con `commit`;
2. collaudo in `method`: l'unità `ciclo-method` lancia lo script, con `--recinto`
   costruito su `systemd-run` e `RuntimeMaxSec` come tetto di riserva. È un atto
   sul modulo `nixos`, nella sua sessione, su messaggio Herdr del custode. Le prove
   della sessione `nixos` dell'host di casa (resoconto inoltrato il 2026-11-08, prove in
   `/tmp` di quell'host): `systemd-run` regge come recinto con `BindsTo`/`After`
   verso l'unità esterna e `--expand-environment=no`; senza, al tetto unità e
   agente restano vivi. Codici, recinto, `fetch.json` e commit con push locale
   tornano; il giro col Claude vero si è fermato sul limite delle 5 ore (20) ed è
   da ripetere. Due rischi portati al canone e chiusi qui:
   - **chiusura al tetto con l'agente vivo.** Il lanciatore uccideva
     `systemd-run` e scriveva la chiusura prima che l'unità interna morisse.
     Nuova opzione dell'host `--recinto-ferma`, il comando che ferma la sandbox e
     ne attende la fine, lanciato prima della chiusura. Per `ciclo-method`:
     `systemctl --user stop ciclo-method-agente`. Trovato rileggendo: la rete in
     chiusura girava solo sul giro riuscito, e un commit protetto seguito da tetto,
     errore o interruzione sfuggiva. Ora vale per ogni fine dopo l'avvio
     dell'agente, con 23 e il `fermo`;
   - **git del lanciatore su un checkout scritto dall'agente.** Criterio per
     tutti: il giro non scrive ciò che git esegue dal lanciatore, cioè
     `o3/lanciatore.py` nel canone, `.git/config`, `.git/hooks`, `.git/lanciatore`
     e la cartella di `core.hooksPath`, se versionata. Lo dicono i permessi e la
     sandbox dove c'è; la cartella degli hook versionati entra da sé fra i
     protetti della rete. In `method` `o3/**` era già negato (il resoconto parlava
     del solo `o3/ciclo/**`); aggiunto il divieto su `.git/**`. `bi` è già
     allineata. Entra nella prescrizione del passo 3;

   Il modulo è pronto in `nixos-casa` (`d375d55b`, `82240929`): esterna con
   `TimeoutStopSec=90s`, perché al tetto di `RuntimeMaxSec` il lanciatore
   riceve il SIGTERM subito e deve sopravvivere ai 30 secondi dell'agente.
   Provato su `svezia` con agente sordo: 143, o 23 col commit protetto, e la
   chiusura arriva sempre dopo la morte dell'agente. Resta al custode la
   sequenza in `kb/cicli.md` di quel repo: pull di `~/method` su deck,
   switch, sonda, un giro a mano col Claude vero. Dopo, la riga del tetto in
   `autonomy.md` passa dall'unità al lanciatore;

3. prescrizione agli altri adottanti e riduzione del modulo `nixos`
   all'adattatore. I moduli sono due, in due repo distinti: `nixos-casa`
   (`steledama/nixos`, host di casa, `ciclo-method`) e `nixos` di lavoro
   (`svezia`, `ciclo-bi` e `ciclo-baserow`), ciascuno con la sua copia. Da
   decidere col custode prima di questo passo: l'adattatore collaudato a casa
   si copia nel `nixos` di lavoro o diventa un pezzo comune ai due repo? Fino
   ad allora i giri di `svezia` restano sul vecchio modulo, dove git gira
   dentro il namespace e i due rischi del collaudo non si presentano in
   quella forma.

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

Decisione del custode, 2026-10-21: nessuna pezza in `nixos`. La sola fonte
dichiarata resta l'obiettivo e la si ottiene portando nel metodo la
scrittura dei tentativi. Fino ad allora un arresto prima del giro può stare
nella cartella dell'unità, e la vista lo rende come partenza mancata: rosso
lo stesso, col motivo sbagliato. Scartate la vista che unisce le due
cartelle per `id`, perché aggiunge un secondo lettore, e la scrittura nella
cartella `giri` dentro `nixos`, perché è la pezza.

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
- **Freschezza del checkout del canone.** Il gate e il guardiano che il giro
  dell'adottante legge dal checkout di `method` possono essere indietro: il
  giro `baserow` del 2026-10-22 su `svezia` ha letto il gate da `c224d3e`,
  prima di `73717f4`, e il rifiuto di `nessuno (…)` ha prodotto un finto
  task (`767236c`). Il lanciatore fa il `pull --ff-only` del checkout di
  `method` all'avvio, già concesso da `CLAUDE.md` («Pull remoto»), o il giro
  dichiara l'hash del canone letto? La domanda tocca la versione fissata
  del punto precedente.
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

## Proposta del 2026-10-29: lanciatore minimale

Nasce dall'arresto del giro di `method` del 2026-10-29 alle 15:00
(`pull-in-sola-lettura`, voce nel
[task pilota](pilota-ciclo-autonomo.md)). Il custode chiede se basti un
lanciatore generico e minimale che fa il pull d'avvio e lancia l'agente,
con l'intero ciclo dentro l'artefatto e all'host il solo trigger.

Il recinto non può stare solo in una regola di `autonomy.md`. Una norma
si può saltare, per un'istruzione dentro un dato letto (una mail, una
pagina), per un errore o per un comando concesso che scrive un file; un
vincolo rende l'atto impossibile (`kb/constraint.md`). Il vincolo però sta
già nel repo e non dipende dal sistema operativo: sono i permessi
dell'harness, `o3/ciclo/permessi.json`, passati con `--settings`, l'unico
recinto di `danea-auto`. Fino al 2026-10-29 quei permessi non negavano la
scrittura su `o3/ciclo/**`, coperta solo dalla sandbox dell'unità; il
divieto è stato aggiunto lo stesso giorno.

Il disegno proposto:

- **lanciatore canonico** con le sole cose che l'agente non può fare da sé:
  lock, controllo della sessione aperta, `pull --ff-only` a working tree
  pulito anche sui percorsi protetti, avvio di `claude -p` coi permessi del
  repo, tetto di tempo e di costo, righe di partenza e chiusura in
  `i1/giri/`, scritte anche quando l'agente si pianta;
- **recinto nei permessi dell'harness**, versionati nel repo: scrittura
  negata su prompt e permessi del giro, `autonomy.md`, `CLAUDE.md`,
  `.claude/` e lanciatore. In `autonomy.md` resta il perché;
- **rete in chiusura**: se i commit del giro, da `head_prima` a
  `head_dopo`, toccano i percorsi protetti, la chiusura è rossa e il giro
  torna al manuale. Così una modifica protetta che arriva da `origin` è
  passata da una sessione col custode, e il pull d'avvio non ha bisogno di
  fermarsi;
- **sandbox dell'host** (systemd su Linux) come rinforzo facoltativo, non
  più come recinto;
- fuori dal lanciatore i controlli locali: fetch degli adottanti, slot di
  `danea-auto`, scadenza del login, nel prompt del repo o in agganci locali.

Resta la domanda «Codice privilegiato da un checkout»: il lanciatore vive
nel checkout, il suo pull lo aggiorna dal giro successivo e i permessi ne
vietano la scrittura al giro. Le modifiche a `nixos` che ne seguiranno
passano dalla sessione su `nixos`, su messaggio Herdr del custode.

## Da osservare intanto

L'arresto per `RuntimeMaxSec` e la sua traccia nel journal: nessun giro ha
ancora toccato il tempo massimo di 45 minuti. Il contratto del lanciatore
dovrà dire come lo registra.

## Criterio di chiusura

Lo script canonico gira in `method` e
in almeno un adottante su un altro sistema operativo, scrive i tentativi
nel `i1/giri/` del repo, arresti prima del giro compresi, e il modulo
`nixos` si riduce all'adattatore dello scheduler. Riga del plan, voce in
`o2/tasks.md` e questo file si rimuovono nello stesso commit.

Connessioni:

- [pilota-ciclo-autonomo](pilota-ciclo-autonomo.md)
- [view](../kb/view.md)
- [session-messaging](../kb/session-messaging.md)
