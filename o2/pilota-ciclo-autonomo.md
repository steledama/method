---
sintesi: "Un adottante scelto insieme fa girare il ciclo autonomo a intervalli concordati per un periodo di osservazione, e il suo esito decide se e come estenderlo agli altri."
ciclo: dev
---

# Pilota del ciclo autonomo

Un repo fa da apripista per il loop agentico di base, su cui poi si
articolano i loop di dominio.

## Prerequisiti

- Push autonomo recepito nel repo pilota: soddisfatto, recepito dai sette
  il 2026-10-08 (in `bi` con l'eccezione del codice del ciclo).
- Trailer di autonomia e impatto (in `/commit` dal 2026-10-08) e sezione
  «fatto» della home: il custode
  deve vedere i giri prima di toglierne la conferma.
- Criteri per il ciclo autonomo schedulato concordati nel register:
  soddisfatto dal criterio `ciclo-autonomo`, ratificato in `method` e nei sei
  adottanti col timer (`danea-auto` il 2026-10-20). Task chiuso il
  2026-10-25: proposte e register raggiungibili dalla home, collaudo sui casi
  portato nel campione qui sotto.
- La scelta di dove gira il ciclo autonomo: timer systemd dal modulo `cicli` di
  `nixos` (`6a6a7ed`), con Claude Code; collaudato al gradino 0 di `salute`.
- Il ciclo autonomo visibile nella home, con semaforo e pagina del giro
  (`kb/view.md`): va in parallelo al ciclo autonomo, prima del gradino 1.
  Task chiuso il 2026-10-26, verificato dal custode sulla home servita.

## Scelta del pilota e gradini

Decisa dal custode il 2026-10-11: due piloti in parallelo, uno per host,
`salute` su `deck` e `crm` su `svezia`. Il ciclo autonomo di runtime è
direzione costitutiva del metodo (`goal.md`): tutti i repo ci arrivano,
gradualmente, ciascuno con i propri limiti da analizzare.

- **Gradino 0**: l'unità vera avviata a mano dal custode (`systemctl start`).
  È un ciclo avviato dal custode, coperto da `ciclo-delegato`; prova ambiente
  dell'unità, credenziali, permessi, push e tempo massimo.
- **Gradino 1**: timer acceso, cadenza bassa. È il ciclo autonomo schedulato, coperto
  dal criterio `ciclo-autonomo` di ogni repo.
- **Gradini successivi**, un repo alla volta per host: su `deck` poi
  `economia`; su `svezia` poi `baserow`, quindi `nixos`, quando il modulo ha
  retto i primi giri, e `bi` in coda; `method` quando il canone ha visto
  girare il ciclo autonomo negli adottanti; `danea-auto` per ultimo, fuori
  `nixos`, in cantiere dal 2026-10-20 (voce sotto). Il custode, 2026-10-15: `baserow` passa davanti a `nixos`, perché ha
  una manutenzione semplice e il ciclo autonomo di `nixos` toccherebbe il
  proprio scheduler. Su `svezia` un solo timer acceso alla volta: `baserow`
  entra al gradino 1 dopo che `crm` ha retto il suo.

Perché questi due: `salute` ha checkout solo su `deck`, pochi cambi e nessun
rilascio legato al push, ma dati personali da tenere fuori dalle letture
automatiche verso l'esterno. `crm` dà giri con materia e il suo confine
(checkout che è anche pubblicazione) è già deciso in `autonomy.md`. `nixos`
non apre la scala: il ciclo autonomo toccherebbe il proprio scheduler e il repo che
governa gli host, con più sessioni concorrenti. `baserow` farebbe soprattutto
giri vuoti; `bi` ha ogni push come rilascio; in `method` un errore autonomo
arriva agli adottanti via symlink.

## Andamento

- **`salute`, gradino 0, 2026-10-11** (`deck`): primo giro avviato a mano,
  riuscito con commit `2eb8a69` e push, 4,5 minuti, 77 turni, 1,85 USD
  dichiarati. Skill `eval`, `exec` e `commit` invocate dal tool Skill;
  Calendar via `gog` e push via ssh senza agent funzionano nell'unità. Due
  permessi negati su comandi composti, rifatti spezzati. Il giro ha
  corretto da sé un errore di `o3/health_data.py` che annullava una
  decisione del custode, con test: è il primo caso del campione da rileggere
  contro le fonti. Il custode ha deciso di togliere da `deck` il Drive di
  Letizia, gli altri remote non suoi e la chiave GitHub di Letizia invece di
  recintarli (`nixos` `74b1328`).
- **Sonde del recinto, 2026-10-11** (unità `ciclo-<repo>-sonda`, senza
  Claude): sola lettura sui mount FUSE superata. Lo stop per sessione
  concorrente taceva, perché dal namespace dell'unità `/proc/<pid>/cwd` è
  illeggibile: spostato in un `ExecStartPre=+` fuori dal namespace, ora
  ferma con 15. Con `--setting-sources project` i deny di
  `.claude/settings.json` valgono anche nel ciclo autonomo e i suoi allow si
  ereditano nei workspace fidati; senza fonti il giro perde `CLAUDE.md` e
  skill. Regola da prescrivere: gli allow di `settings.json` stanno dentro
  quelli del file del ciclo autonomo, i deny sono liberi.
- **`salute`, secondo giro manuale, 2026-10-11** (`deck`): riuscito con
  commit `1d7fe22` e push, 2,5 minuti, 44 turni, 0,89 USD. La skill `cycle` invocata in modo `autonomo`, riga `Attenzione:` presente, semaforo
  giallo per proposte e dinieghi. Le correzioni dei permessi del primo giro
  tengono (`sort`, lettura di `method/`). Una foto pressoria illeggibile non
  registrata e lasciata come proposta in `o2/`. Due difetti, dichiarati
  dall'agente stesso: tre dinieghi su `git` (il deny intero su `git branch`
  e `git -C`) e un `Co-Authored-By` che ha staccato i trailer, perché il
  ciclo autonomo non legge `attribution` dalle impostazioni utente. Il giro
  resta fuori dal conteggio degli esiti; `1d7fe22` non si riscrive. Il
  custode ha deciso lo stesso giorno: amend concesso dove è concesso il
  commit, solo prima del push, con la rilettura dei trailer nelle skill
  `commit` e `cycle`; base git comune nella prescrizione
  `ciclo-autonomo`, chiusa il 2026-10-28; `attribution` passato
  dall'unità.
- **`salute`, gradino 1, deciso il 2026-10-11** (`deck`): timer ogni giorno
  alle 12:00 dal 2026-10-12 (`nixos` `cd2be2a`), criterio `ciclo-autonomo`
  ratificato con la regola di sospensione (`salute` `308d4ec`): si torna al
  manuale dopo un rosso per atto fuori delega o ricostruzione sbagliata,
  mentre lo stop per sessione aperta, il push rifiutato e il lock occupato
  sono il sistema che funziona. L'orario segue i dati, non il calendario:
  alle 12:00 sono arrivati notte, pratica del mattino e invio manuale del
  custode, perché la sincronizzazione automatica dell'orologio oggi non è
  affidabile. `Persistent=false`: con `deck` spento il giro salta e la home
  lo segna rosso, con `deck` sospeso parte alla ripresa.
- **`crm`, gradino 0, 2026-10-15** (`svezia`): criterio `ciclo-autonomo`
  ratificato dal custode (`crm` `abaf9c7`). Il giro lavora su artefatto e
  proposte, non implementa task dev e non tocca codice applicativo,
  migrazioni, `o3/tools/` (backup in esercizio dal checkout) né `o3/view/`
  (server riavviato al commit). Il push è automatico e i test Django valgono
  solo per un giro che tocca codice: l'unità non ha `uv` né un Postgres di
  test. Allargamenti previsti, uno alla volta: test, poi `o3/view/`.
  - **Primo giro** (`f4fc1af`, 1,7 minuti, 0,87 USD, giallo): ha ricostruito
    dalla storia git la coda ferma dal 2026-08-21, e la ricostruzione è
    verificata. Ha lasciato una proposta A/B/C. La lettura di `~/manager` è
    stata negata e non aggirata: la domanda del prompt presupponeva fonti
    fuori perimetro. Il custode ha chiarito che il lavoro è in design
    condiviso con i colleghi, fuori dai repository.
  - **Secondo giro** (`301463f`, 1,9 minuti, 0,82 USD, 26 turni, giallo):
    bozza della scheda per Alessio, con le otto domande del custode rese
    fedelmente e una nona lasciata in proposta.
  - Dinieghi innocui in entrambi i giri (`hostname`, `echo rc=$?`), corretti
    nel canone (`70a5825`, `94d85b7`). Il deny `git add .*` della
    prescrizione bloccava `.claude/`: corretto in `cb39a4b`.
- **`crm`, gradino 1, deciso il 2026-10-15**: timer ogni giorno alle 05:30,
  modifica di `state` chiesta a `nixos`. Il giro si ferma se trova una
  sessione aperta sul checkout di `svezia`.
- **`crm`, uscito dal ciclo autonomo il 2026-10-19**: decisione del custode,
  `nixos` `1be1e2d` con switch su `svezia`. Unità e timer rimossi, voce tolta
  da `decisioni.json`; la vista resta servita senza ciclo autonomo. Lo storico
  dei tentativi resta in `~/.local/state/ciclo/crm/` su `svezia`. `crm` va
  verso la dismissione; al suo posto è atteso un nuovo adottante,
  `abbinamenti`.
- **`baserow`, `svezia`**: secondo su `svezia`, deciso il 2026-10-15. Prima
  del gradino 0 servono la voce in `nixos` `o3/cicli.nix` e i passi 5–7 della
  prescrizione. Il backup manuale senza restore resta riservato al custode
  nel suo criterio `ciclo-autonomo`.
  - **Gradino 0, 2026-10-16**: criterio ratificato col perimetro del ciclo
    avviato dal custode, compresi sei comandi ssh esatti sullo standby e tre
    query SQL aggregate, meno il backup manuale (`baserow` `bc60b09`); voce
    in `nixos` `ce41bad` con `requiresProduction`. Sonda superata.
  - **Primo giro** (`e779a40`, 17,8 minuti, 1,62 USD, 71 turni, giallo):
    Docker, ssh su `norvegia` e query passano dal recinto. Verdetto di
    `recuperabilita-dati` portato a «sufficiente», con chiusura proposta e
    non applicata; i fatti del backup (7 coppie per lato, `peer_verified`)
    sono verificati contro `latest.json` e i due host. Cinque dinieghi:
    `ls -l backup/` in locale, che il prompt elenca ma il recinto nega, un
    filtro con `awk`, `git fetch`, `python3 -` e `prettier --write`. Punto
    da decidere prima del gradino 1: `ciclo-avvio` fa `pull --ff-only` di un
    checkout indietro, mentre in `baserow` il pull è un rilascio su
    richiesta del custode (`CLAUDE.md`, «Pull remoto»); col timer
    diventerebbe automatico. Casi in
    [`i1/casi-delega-baserow-2026-10-16.md`](../i1/casi-delega-baserow-2026-10-16.md).
  - **Gradino 1, 2026-10-17**: pull d'avvio concesso al giro come eccezione
    al checkout servito e `ls -l backup/` fuori dal prompt (`baserow`
    `1d8b20c`); timer alle 06:30 acceso da `nixos` `e3f463a`. Giri
    schedulati del 18 e 19 partiti sul timer, pull d'avvio senza commit da
    rilasciare (dal task `o2/ciclo-autonomo.md` di `baserow`). Il 2026-10-19
    il prompt dichiara i filtri ammessi in pipe, allineati a mano a
    `ciclo.json` (`e24d585`).
  - **Standby, deciso il 2026-10-19** (`437b11b`): dopo un push riuscito il
    giro porta il checkout di `norvegia` allo stesso commit, con tre comandi
    SSH esatti, guardie su marker di ruolo assente e working tree pulito,
    `pull --ff-only` e verifica dell'hash; guardia fallita, nessun altro
    tentativo e voce in `Attenzione:`. È il primo atto di un giro autonomo
    su un host diverso da quello dell'unità, e anche lì il pull è un
    rilascio (script del controllo di freschezza). Da rileggere ai primi
    esercizi, dal giro del 2026-10-20: guardie eseguite, hash coincidente,
    rilascio dichiarato nel resoconto.

- **`economia`, `nixos` e `method`, gradino 0, deciso il 2026-10-16**
  (`deck`): il custode allarga il ciclo autonomo ai quattro repo gestiti da
  `deck`, dopo i giri di `salute` e `crm`. Anticipa `method`, che la scala
  metteva dopo gli adottanti, e porta `nixos` su `deck`, dove la sua vista è
  già servita (il modulo vuole ciclo e vista sullo stesso host). Unità in
  stato `manuale`, orari predisposti un'ora dopo l'altra: `salute` 12:00,
  `economia` 13:00, `nixos` 14:00, `method` 15:00, l'ultimo perché il suo
  perceive trovi i giri degli adottanti del giorno. Perimetri:
  - `economia`: manutenzione dell'artefatto, Gmail, Calendar e Drive in
    lettura, bozze Gmail senza ok preventivo sul testo, mai l'invio;
  - `nixos`: `/manutenzione` al centro, con bump e switch di `ia` e
    `home-manager` dentro il giro; per lo switch la home dell'unità è
    scrivibile (`homeWritable`) e il recinto resta solo l'harness, scelta
    fatta dal custode sapendolo;
  - `method`: `kb/` modificabile, prescrizioni, strumenti e skill in
    proposta, `/adottanti` e `/method` fuori dal giro, marker letti dai
    checkout locali di `deck`.

  Il timer si accende un repo alla volta, dopo un paio di giri manuali
  puliti. Commit di attivazione: `nixos` `4322077` (voci in `o3/cicli.nix`,
  `homeWritable`, `X-RestartIfChanged=false` su ogni unità `ciclo-*`, perché
  un bump di Claude Code non interrompa un giro in corso), `economia`
  `986ade1`, `method` `118c276`. Sonde superate su `economia` e `nixos`;
  quella di `method` ferma per la sessione del custode aperta su
  `~/method`, cioè il controllo che funziona.
  - **`nixos`, primo giro** (`98e48cf`, 1,4 minuti, 1,20 USD, 39 turni):
    `/manutenzione` senza rami dovuti, quindi né bump né switch: la parte
    rischiosa del perimetro resta da collaudare. Due bonifiche di testo sul
    ramo `home-manager` in plan e prescrizioni. Segnalata la sonda di
    `method` rimasta fallita: da qui `31ef62d`, la sonda usa
    `ExecCondition` e con una sessione aperta viene saltata, non fallita.
  - **`economia`, primo giro** (`368bf9a`, 2,6 minuti, 1,21 USD): risposta
    del notaio e proposta Albatros viste in Gmail ma non catturate, perché
    `posta` era fuori dal giro. Il custode ha deciso lo stesso giorno: il
    giro esegue `posta` dentro `perceive` e salva gli allegati pertinenti in
    `gdrive/<dominio>/` senza sovrascrivere né cancellare; Drive `economia`
    scrivibile nell'unità, il resto in sola lettura (`a05e72e`, `31ef62d`).
  - **`economia`, secondo giro** (`2430f5a`, 8,2 minuti, 2,96 USD, 100
    turni): 14 segnali catturati, proposta Albatros salvata e letta con
    `pandoc`, sollecito a Caprioli in bozza Gmail (verificata, non
    inviata). Un errore dichiarato dall'agente: un conto WindTre di Tigli
    archiviato fra le bollette di via Romana, doppione. Il custode ha
    controllato il codice cliente, confermato la correzione e tolto il
    doppione (cestino di Drive); il prompt ora chiede intestatario e ricerca
    dei doppioni in tutto `gdrive/` prima di salvare (`cda8da0`). Costo più
    che doppio per la posta, sotto il tetto di 5 USD.
  - **Potatura**: il custode concede `git rm` su bozze e canovacci di `o3/`,
    task `o2/` chiusi e catture `i1/` superate; restano negati `rm`,
    `git rm -r`, gli indici e ogni cancellazione su Drive (`660eb7a`). Il
    terzo giro (`882601a`, vuoto) non l'ha usato: senza segnali nuovi
    nessuno stadio tornava sui file consumati. Il prompt ora la chiede come
    controllo fisso di `exec` (`7e55e53`).
  - **`economia`, quarto giro** (`086f13b`, 2 minuti, 0,73 USD): tolte la
    bozza ad Arsini (inviata il 10/10, risposta del 12/10) e quella ad
    Albatros (superata dalla telefonata del 15/10), con riferimenti
    aggiornati; lasciati i file non ancora consumati.
  - **`method`, primo giro** (`0de0157`, 3,1 minuti, 1,34 USD, 47 turni,
    giallo), lanciato da terminale senza sessioni su `~/method`, dopo la
    sonda superata: nessun nodo `kb/` toccato; filo del ciclo autonomo,
    indice, audit e tre task `o2/` riallineati all'andamento. Marker dei
    sette verificati contro i checkout. Il filo ometteva la ratifica di
    `economia` e `nixos`, corretta in sessione. Quattro dinieghi, tre
    dichiarati: il ciclo `for` sui marker (ripiegato su Read), `git log` e
    reflog di `salute`, `tentativi.jsonl` di `salute`. Il perimetro concede
    solo i marker, mentre l'orario delle 15:00 è motivato dai giri degli
    adottanti del giorno: il custode concede la lettura dei soli
    `tentativi.jsonl` dei repo di `deck`, non di `giri/`, che porta i dati
    di `salute` ed `economia` (2026-10-16). Il timer di `method` attende il
    primo giro schedulato di `economia` e un secondo giro manuale pulito.
  - **`economia`, gradino 1, deciso il 2026-10-16**: timer ogni giorno alle
    13:00 dallo stesso giorno (`nixos` `5f127c7`), dopo quattro giri
    manuali, gli ultimi due puliti. È il secondo timer su `deck`, un'ora
    dopo `salute`; il rischio noto è il Drive scrivibile, che con il mount
    irraggiungibile ferma l'unità come `salute` il 2026-10-14, ora
    registrato da `ciclo-namespace`. Primo giro schedulato (`e51265b`,
    13:00, 1,7 minuti, 0,68 USD, vuoto): riuscito, ma il trailer dichiara
    «gradino 0 (avvio manuale del custode)», perché prompt e `autonomy.md`
    di `economia` non sono passati al gradino 1 con il timer. Regola per
    i prossimi: la voce `timer` in `nixos` va insieme al gradino 1 nel
    prompt e nel criterio del repo, sul modello di `salute`.
  - Dinieghi in tutti i giri, innocui: il comando composto d'avvio (in
    `nixos` con `git -C`), una bozza Gmail con quoting `$'…'`, `git rm -q`
    su due file; ogni volta rifatti nella forma ammessa. Il primo comando
    composto ricorre in ogni giro: candidato a una correzione della skill
    `cycle` canonica.
  - **`method`, secondo giro** (`b8b26f5`, 2,1 minuti, 0,82 USD, 38 turni),
    avviato a mano il 2026-10-16 alle 13:35 senza sessioni su `~/method`:
    il primo con la lettura dei `tentativi.jsonl` (`735d7f7`). Nessun nodo
    `kb/` toccato; i giri del 16/10 di `salute` ed `economia` scritti nel
    filo combaciano con `tentativi.jsonl` e journal, riletti in sessione col
    custode il 2026-10-17. Un diniego innocuo, `ls -d` sui checkout degli
    adottanti.
  - **`method`, gradino 1, deciso il 2026-10-17**: timer ogni giorno alle
    15:00, insieme al gradino 1 in `.claude/ciclo-prompt.md` e in
    `autonomy.md`. Timer acceso dallo stesso giorno insieme a quello di
    `nixos` (`nixos` `7fad7d2`, switch su `deck` riuscito): su `deck` girano
    quattro timer, `salute` 12:00, `economia` 13:00, `nixos` 14:00,
    `method` 15:00.
  - **Decisioni del 2026-10-17** del custode, per portare il timer su tutti i
    repo:
    - `nixos`: timer alle 14:00 senza attendere un giro con bump e switch
      veri; la parte rischiosa del perimetro si collauda al primo giro che
      li trova dovuti (gradino 1 in prompt e criterio di `nixos`,
      `7fad7d2`). Primo giro schedulato riuscito il 2026-10-17 alle 14:00
      (`861f7d8`, commit e push, quattro dinieghi, da `tentativi.jsonl`);
      se abbia trovato bump e switch dovuti, e quali comandi siano stati
      negati, il giro di `method` non lo legge. Secondo giro il 2026-10-18
      (`5b19d5c`, commit e push, tre dinieghi), 9,7 minuti e 69 turni
      contro i 2,3 del primo: se la durata venga da un bump o da uno switch
      è il primo punto da rileggere nel trascritto, in sessione;
    - `baserow`: il giro fa il `pull --ff-only` d'avvio, sapendo che lì è
      un rilascio; `ls -l backup/` esce dal prompt. Il timer alle 06:30 segue
      la verifica su `svezia` dei giri schedulati di `crm`, perché su
      `origin` manca il giro del 2026-10-17 alle 05:30 e quello del 16 si
      firma gradino 0: il prompt e il criterio di `crm` non sono passati al
      gradino 1 con il timer, come in `economia`;
    - `bi`: gradino 0 su `svezia` (`nixos` `d55da57`), poi gradino 1 in
      giornata dopo un solo giro manuale riuscito (`bi` `e423e8b1`: commit e
      push, 3,18 USD su 5, scritture Baserow fino a esaurimento delle code).
      Prompt e criterio al gradino 1 in `bi` `86cf2804`, timer alle 07:30
      in `nixos` `d1c4346`, switch su `svezia` riuscito. Il caso del marker
      di ruolo è in `i1/casi-delega-bi-2026-10-17.md`;
    - `economia`: giro schedulato del 2026-10-17 riuscito alle 13:00
      (`53ea575`, commit e push, da `tentativi.jsonl`); resta da verificare
      il gradino 1 nel prompt e nel criterio, che il giro di `method` non
      legge.
  - **Prompt di `method` contro il recinto, deciso: alternativa 3** (giro del
    2026-10-20, `i1/giro-method-2026-10-20.md`). Il fetch dei quattro repo di
    `svezia` fallisce, perché nell'unità i loro checkout sono in sola lettura
    e il fetch scrive in `.git/`. In più il timer di `nixos` parte alle
    04:30 dal 2026-10-19 (`tentativi.jsonl`), e quindi il «un'ora dopo
    `nixos`» del prompt e l'elenco dei quattro orari qui sopra non valgono
    più. Le alternative:
    1. rendere scrivibili nell'unità i soli `.git/` dei quattro checkout
       (`readOnlyPaths` in `nixos` `o3/cicli.nix`), sapendo che il fetch
       tocca checkout dove lavora un'altra sessione;
    2. togliere il fetch dal prompt e leggere `origin` noto, dichiarandone
       l'età, con il fetch lasciato alle sessioni col custode;
    3. far fare il fetch a un passo dell'unità prima del giro, fuori
       dall'harness.

    Motivo: oggi il giro legge marker di `svezia` di età ignota, mentre il
    prompt dice il contrario. Il custode ha scelto la 3 il 2026-10-20: campo
    `fetch` e passo `ciclo-fetch` in `nixos` (`ExecStartPre=+` dopo
    `ciclo-sessioni`, esito in `~/.local/state/ciclo/method/fetch.json`);
    il prompt non tenta più il fetch, legge quell'esito e motiva le 15:00 come
    ultimo giro di `deck`; via da `o3/ciclo/permessi.json` i quattro
    `git fetch`. Provato a mano fuori dall'unità: quattro fetch riusciti,
    tutti con `origin/main` più avanti di quello letto dal giro. Rivisto in
    sessione lo stesso giorno (`nixos` `75011be`): fetch limitato a 15 s per
    checkout e `TimeoutStartSec` di 90 s più 15 per checkout, perché un remote
    appeso non faccia fallire l'avvio; in `fetch.json` il campo
    `ultimo_riuscito`, che il prompt usa come età dell'`origin` a fetch
    fallito. Primo giro schedulato dopo lo switch, 2026-10-20 alle 15:00:
    quattro fetch riusciti, `id` di `fetch.json` uguale a quello della
    partenza, nessun `git fetch` tentato dal giro.

- **`danea-auto`, esecutore su Windows, deciso il 2026-10-20**: il custode
  mette in cantiere il suo ciclo autonomo. Un adottante senza ciclo autonomo
  non è pienamente tale (`goal.md`, «ciclo autonomo di runtime in ogni
  repo»): «per ultimo» resta l'ordine nella scala, non un rinvio senza data.
  Stato al 2026-10-20: `/cycle` recepita solo in sessione (`dcd5deb`);
  `autonomy.md` locale dichiara che nessun giro gira senza custode e la home
  lo mostra. Manca l'esecutore, che il modulo `cicli` di `nixos` dà agli altri
  sei e che qui va costruito fuori `nixos`, col Task Scheduler. Il **cosa**
  vive in un task `o2/` di `danea-auto` (lanciatore, slot, criterio); qui la
  scala. Punti propri di Windows, da risolvere lì:
  - **lanciatore** in `o3/scheduler/`, con i passi dell'unità (sessione
    aperta, lock, branch e tree, prompt e permessi del repo, tempo massimo,
    chiusura) e `i1/giri/tentativi.jsonl` nella stessa forma, perché la home
    canonica dia il semaforo senza modifiche;
  - **recinto più debole**: senza un equivalente semplice della home in sola
    lettura resta l'harness, come in `nixos` con `homeWritable`; da accettare
    sapendolo o da compensare;
  - **slot dell'export**: gli script AHK pilotano la GUI ogni ora, e un giro
    che apre una console durante uno slot ruba il primo piano. Il giro sta
    fra la FINE di un run e lo slot successivo, con tempo massimo più corto e
    comandi senza finestra (`2eeeb5e` lo fa già per la vista);
  - **criterio `ciclo-autonomo`** in `autonomy.md` da ratificare, con Danea,
    Windows e Controlp sempre fuori; poi gradino 0 avviato a mano, timer
    dopo un paio di giri puliti.

  Un giro autonomo quotidiano di `/eval` darebbe da solo la cadenza di guardia
  della rampa di LibreOffice; fino al 27/10 la guardia resta manuale (22 e
  24/10, poi ogni giorno).
  - **Gradino 0 preparato lo stesso giorno** (`danea-auto` `96ae950`,
    `4ace513`, `63d51f0`), senza task registrati. Decisioni del custode: D1
    utente `danea-ciclo` non interattivo con ACL, D2 `pythonw.exe` con
    interprete esplicito, D3 07:05, D4 clone proprio e `--rilascio` del
    checkout servito come `danea`, D5 semaforo subito. Il lanciatore
    `o3/scheduler/ciclo_autonomo.py` segue la sequenza degli script
    dell'unità, riscontrata in sessione da `method`. Le differenze: arresto
    per qualunque `claude.exe` vivo, perché su Windows la cwd di un altro
    processo non si legge; slot letti dal log dell'export (16); timeout
    locale (22). Il rilascio non porta mai diff su produzione o recinto
    (`o3/runtime/`, `o3/scheduler/`, `o3/ciclo/`, `.claude/`,
    `autonomy.md`, `CLAUDE.md`: 17); al gradino 1 gira alle 08:10. Ogni
    arresto lascia un tentativo, lock compreso. Restano gli undici atti del
    custode in fondo al task di `danea-auto`, poi la ratifica del criterio e
    il primo giro.
  - **D1 rivista dal custode lo stesso giorno**: niente utente separato, il
    giro gira come `danea`. Pesa la semplicità: un trasferimento di `danea2`
    non deve dover ricreare utenti, ACL e credenziali. Rischio accettato
    sapendolo: il recinto è solo l'harness, come in `nixos` con
    `homeWritable`, e Danea, Windows e Controlp restano fuori per permessi e
    prompt, non per il sistema. Il task gira «indipendentemente dalla
    connessione dell'utente», con la password salvata: senza desktop, così
    nessuna finestra ruba il primo piano agli slot. Restano il clone proprio
    (D4) e il rilascio protetto. Autenticazione di Claude e push di `danea`
    fuori dal desktop si provano al primo giro.
  - **Gradino 1, deciso dal custode il 2026-10-21** (`danea-auto` `de11b1a`,
    `85b27f5`): basta il giro `6c90701f` (`5fe03bb`, riuscito, 2,2 minuti,
    48 turni, 1,13 USD) al posto di due giri puliti, e le correzioni si
    fanno in campo. Il primo giro (`490fa4a`) si era fermato su un diniego
    sul comando dei CSV, corretto in `b8ee551`. Task registrato dal custode:
    ogni giorno alle 08:10, `ExecutionTimeLimit` 50 minuti, tetto del giro
    40 minuti o le :50; primo giro schedulato il 22/10. Correzioni del giro
    del 21: il diniego del `Grep` sul gate di `method` si è tolto dal
    prompt invece di concedere la lettura del checkout; il trailer
    `Prossimo:` rifiutato nasceva dal fork locale di `exec` e `commit`, che
    scriveva il riesame nel trailer. Da qui in `method` il gate che accetta
    `nessuno (<motivo>)`, prima rifiutato pur ammesso da `exec`, e il
    guardiano delle skill che prova gli esempi di `Prossimo:` contro il
    gate. Il login claude.ai del giro scade il 24/10 (`refreshTokenExpiresAt`):
    il lanciatore lo segnala giallo entro tre giorni e rosso (arresto 18)
    entro il tetto; il custode rinnova a mano, e `claude setup-token` resta
    da riprendere. Da verificare se la stessa scadenza tocca gli adottanti
    di `nixos` col login claude.ai. Alle 08:10 nessuna sessione Claude
    aperta su `danea2`, altrimenti arresto 15. Il primo giro schedulato,
    il 22/10, è riuscito con commit e push su `origin` (`1a6b33f`, 08:11,
    trailer `ciclo-autonomo`, gradino 1, timer delle 08:10). Il commit
    concordato `8af2b9e` dello stesso giorno dice nell'oggetto che il login
    è stato rinnovato il 21/10 e che la scadenza la legge solo il
    lanciatore. Il giro di `method` non ha letto la nuova data di scadenza.
    I giri schedulati del 23 e del 24 sono riusciti con commit e push
    (`e9b89c4`, `c628acb`), quindi il 24 il login era valido.

I tempi fra i gradini si decidono sull'andamento delle prove. Si avanza senza
atti fuori delega, senza arresti invisibili e con un campione di giri riletto
contro le fonti; si torna al gradino precedente, per quel repo, alle
condizioni di sospensione sotto.

## Da fissare alla partenza

Fissare prima dell'avvio intervallo, durata, perimetro degli atti delegati,
criteri di riuscita e condizioni di arresto. I prerequisiti dipendono dai
risultati dei task della home e dell'esecutore, chiusi il 2026-10-26; i
criteri sono in `autonomy.md`.

- Concordare un campione di decisioni e ricostruzioni da rileggere contro le
  fonti, includendo i verdetti modificati: motivo comprensibile e trailer
  corretti non bastano a provarne la qualità. Il campione include i casi del
  filo [ricostruzione delegabile](../i3/verdetto-piu-sicuro-del-materiale.md),
  tenendo distinte leggibilità del motivo e fedeltà alle fonti (dal task dei
  criteri, chiuso il 2026-10-25).
- Misurare interventi necessari del custode e tempo di ricostruzione degli
  esiti, con un confronto assistito concordato prima della partenza. Il
  beneficio atteso è meno lavoro di supervisione a qualità conservata;
  frequenza dei giri e quantità dei commit non lo dimostrano.
- Osservare i tentativi anche quando non producono commit: mancata partenza,
  arresto e fallimento devono essere visibili al custode.
- Concordare quando sospendere il pilota e come tornare alla modalità
  assistita, almeno per un atto fuori delega, un impatto alto applicato,
  un arresto invisibile o una ricostruzione errata che altera una decisione.

La delega sulla manutenzione dell'artefatto resta distinta dalle azioni di
dominio. L'esperienza di `/manutenzione` in `nixos` non dimostra da sola la
delegabilità di `eval compare`; negli altri candidati vale lo stesso esame
contro il Goal locale.

## Criterio di chiusura

A fine osservazione, verdetto nel filo [ciclo autonomo](../i3/ciclo-autonomo.md)
su fedeltà delle ricostruzioni, rispetto della delega, visibilità degli
arresti e costo per il custode. Dichiarare copertura e limiti del campione;
un pilota privo di casi informativi non certifica l'autonomia. Il custode
decide se estendere, correggere o tornare alla modalità assistita.
