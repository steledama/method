---
sintesi: "Direzione approvata il 2026-10-06: view/ esce da git, con verifica nel gate e pubblicazione da un commit pulito dopo la build. Passi 1-3 fatti il 2026-10-07: pubblicazione da commit con ultima vista buona, servizio di deck collaudato in nixos (pull manuale), view/ fuori da git in metodo e canone inciso con una transizione per gli adottanti. Passo 4 prescritto lo stesso giorno (o3/viste-fuori-da-git.md); resta il recepimento dei sette, danea-auto compreso."
ciclo: dev
---

# Viste fuori da git

Direzione approvata dal custode il **2026-10-06**, con le correzioni emerse
dalla revisione. La revisione della specifica è autorizzata; l'implementazione
resta lavoro futuro, a partire dalla prova su `metodo`. Si riconsidera la
decisione di versionare `view/` presa con la migrazione delle viste (`216ec6f`).

## La proposta

`view/` è interamente derivata dalle fonti, dai builder e dagli asset
versionati. Togliere l'output da git rende i diff più leggibili ed elimina
il rumore di toolchain dalla storia. Si rinuncia all'HTML disponibile subito
dopo il clone: chi lavora su un altro checkout genera le viste in locale.
Il debito di freschezza passa alla pubblicazione, non scompare.

Ogni repo ha già un **host privilegiato** che serve le viste sulle reti
private. Il flusso previsto è: verifica locale → commit → push su richiesta
→ aggiornamento del checkout sull'host → build e pubblicazione automatica.
Su `deck` l'aggiornamento del checkout resta manuale, come deciso dal
custode (sezione «Decisione» sotto). Dove si sviluppa e si
serve sullo stesso host (`danea2`), la pubblicazione segue il commit locale.
Il gate pre-commit resta una verifica, distinta dalla pubblicazione.

## Fatti verificati il 2026-10-06

- `view/` in `metodo`: 41 file, tutti prodotti da `python3 o3/view/build.py`
  (Pandoc e Prettier). La rigenerazione sul checkout pulito non cambia nulla:
  la build è deterministica e le viste erano fresche.
- I 17 MB di `view/` sono quasi tutti i sette PNG copiati da
  `presentation/`: blob identici, git li conserva una volta. Il peso non è un
  argomento.
- 24 dei 75 commit dell'ultimo mese toccano `view/`: un terzo della storia
  porta HTML rigenerato.
- L'output dipende dalla versione di Pandoc dell'host: il 2026-10-05 il deck
  di `danea-auto` differiva solo per quella (`goal.md`, obiettivo 2).
- Le ragioni del versionamento in `kb/view.md` sono due: aprire le viste dal
  checkout senza build, e il servizio permanente che «lancia lo stesso
  `serve.py` del checkout; un pull aggiorna le viste senza riavvii». L'hook
  di rigenerazione era scartato perché installazione host-locale non
  versionata.
- In `nixos` (`o3/modules/home/presentations.nix`, `o3/presentations.nix`)
  il pull sugli host privilegiati è **manuale**: oggi le viste servite
  cambiano solo dopo push e pull. Host privilegiati: `deck` per `method`,
  `nixos`, `salute`, `economia`; il ruolo `production` della coppia server
  per `bi`, `crm`, `baserow`; `danea2` per `danea-auto`.

- Fino al 2026-10-07 `build.py` scriveva e potava nella cartella servita
  prima di Prettier e del controllo finale, e `build_pages.py` leggeva dal
  working tree anche i Markdown non tracciati: il solo hash di `HEAD` non
  identificava le fonti. Il passo 1 ha chiuso entrambi i punti.
- La unit `-vista` attuale in `nixos` è una migrazione una tantum, con
  `RemainAfterExit=true`. Non è già un modello di ricostruzione ricorrente.
  `PathChanged=` non recupera le modifiche precedenti all'attivazione solo
  perché il file esiste: cfr. [documentazione systemd.path](https://github.com/systemd/systemd/blob/main/man/systemd.path.xml).
- La revisione ha letto la configurazione locale dei servizi, non collaudato
  gli host remoti o la raggiungibilità delle loro porte.

## Contratto della pubblicazione

Questi requisiti entrano nel canone senza dipendere da NixOS o da un host
particolare. La configurazione dei servizi ne è un'implementazione.

- **Ultima vista buona**: costruire in una destinazione temporanea, eseguire
  contratti, rendering, formattazione e controllo del compartimento stagno,
  poi pubblicare soltanto l'esito riuscito. Un errore, anche tardivo, lascia
  intatta la versione precedente. Specificare e provare il passaggio fra le
  versioni, senza esporre una cartella parzialmente aggiornata; la soluzione
  deve funzionare anche su Windows.
- **Anteprima e pubblicazione**: la build locale può rendere il lavoro in
  corso, dichiarandolo come anteprima. La vista pubblicata deriva da un
  commit pulito: escludere modifiche e file non tracciati che entrerebbero
  nell'output. Il gate verifica senza sostituire la vista pubblicata, anche
  quando sviluppo e servizio condividono lo stesso host.
- **Provenienza**: la home pubblicata espone l'hash del commit realmente
  costruito, scritto insieme all'output valido. Registrare anche le versioni
  del toolchain per diagnosticare differenze. Costruire da fonti stabili:
  serializzare o isolare la lettura rispetto a pull, edit e build concorrenti;
  non attribuire un hash a contenuti letti da revisioni diverse.
- **Recupero**: verificare all'avvio se l'output manca o è arretrato, oltre a
  ricostruire dopo un aggiornamento delle fonti. Definire recupero dopo un
  errore e gestione di un nuovo aggiornamento durante la build. Se manca
  qualunque versione valida, il servizio resta fermo con diagnosi leggibile;
  se ne esiste una, continua a servirla e rende consultabile l'errore.
- **Verifica distinta dalla freschezza**: `/adottanti` controlla separatamente
  build e contratti sulle fonti, revisione servita rispetto al riferimento
  remoto aggiornato, raggiungibilità della porta. La corrispondenza degli hash
  non prova la correttezza del rendering. Una porta irraggiungibile è «non
  verificata», non fresca per presunzione.

## Sequenza e risorse

1. **Preparare e provare su `metodo`**, mantenendo inizialmente `view/`
   versionata. Modificare `o3/view/build.py` e, se necessario, `serve.py` per
   rispettare il contratto; definire le modalità di verifica, anteprima e
   pubblicazione senza duplicare le regole di derivazione. Superare le prove
   sotto prima di generalizzare la soluzione.

   **Stato al 2026-10-07: lato build e server fatto e provato in locale.**
   `build.py` rende sempre in una cartella temporanea e copia in `view/` solo
   a esito riuscito; `--check` verifica senza scrivere. `build.py --publish
DIR` delega a `publish.py`: esporta il commit con `git archive` (niente
   modifiche locali né file non tracciati, fonti stabili durante pull ed
   edit), costruisce coi builder di quel commit in `releases/<data>-<hash>`
   e scambia il puntatore `current` con `os.replace`. Tiene la versione
   corrente e la precedente, scrive `status.json`, serializza con un lock e
   ripubblica la revisione più recente se un'altra richiesta arriva durante
   la build. La home pubblicata espone commit e toolchain, che
   `provenance.json` registra. `serve.py --publish-root DIR` rilegge il
   puntatore a ogni richiesta, rende `/_stato` e senza versioni valide non
   parte e dice perché.

   Provato su un clone di `metodo`, con la porta solo su `127.0.0.1`:
   output pubblicato identico alla build del working tree, salvo il piè di
   pagina; working tree sporco e file non tracciati esclusi; contratto
   violato ed errore tardivo di Prettier senza effetti sulla versione
   servita, con l'errore in `/_stato`; 300 richieste HTTP durante tre
   scambi, tutte 200; richiesta accodata durante una build pubblicata alla
   fine; avvio senza versioni con diagnosi. Test in `tests/test_publish.py`.

   Restano fuori dal passo: il marcatore di anteprima sulla build locale,
   che cambierebbe la `view/` ancora versionata e si aggiunge al passo 3;
   la prova su
   Windows, dove `tarfile` non estrae i symlink senza privilegi; i fork in
   cui il perimetro attraversa un symlink come `method/`, che `git archive`
   esporta come link e la build già non segue.

2. **Preparare il servizio dell'host di `metodo` attraverso `nixos`**.
   `o3/modules/home/presentations.nix` e `o3/presentations.nix` governano
   toolchain e servizi. Fornire gli eseguibili con versioni controllate e
   percorsi espliciti. Una path unit su `.git/logs/HEAD` è un candidato al
   trigger, da validare insieme al controllo all'avvio e al recupero; non
   ereditare il comportamento una tantum di `-vista`. La condizione sulla
   presenza dell'HTML non deve impedire la prima build. Collaudare la porta
   dell'host prima della rimozione delle viste da git.

   **Stato al 2026-10-07: fatto in `nixos` e collaudato su `deck`**, secondo
   l'esito riportato dall'istanza di `nixos` (task locale
   `o2/publish-views-from-clean-commit.md`, KB in
   `kb/network-architecture.md`); qui non è stato riverificato. Per il solo
   `method`: una oneshot `presentazione-method-pubblicazione` lancia
   `build.py --publish ~/.local/state/view/method` con toolchain dal flake
   (pandoc 3.7.0.2, prettier 3.9.6) e parte al login; una path unit su
   `~/method/.git/logs/HEAD` la innesca a ogni spostamento di `HEAD`
   (commit, checkout, pull, non fetch); `presentazione-method` serve sulla
   8001 dopo la pubblicazione, anche se questa fallisce, e senza versione
   valida resta ferma senza riavvii. Prove superate: primo avvio senza
   output, commit su un ramo di prova, build fallita con versione servita
   identica byte per byte, nessuna versione valida, output arretrato al
   login, due commit a un secondo in un solo giro con 30 richieste HTTP
   tutte 200, porta da `neve` e `norvegia` (200, 404 su `/.git/config`).
   Non verificati: login o reboot veri (simulati con `default.target`), la
   porta da `game` e da `svezia`.

   Le due debolezze segnalate da `nixos` sono corrette in `metodo` lo stesso
   giorno: `serve.py` esce con 3 quando manca una versione valida e ha
   `--check` per un `ExecCondition`, così il controllo non si duplica nella
   unit; il lock di `publish.py` porta il PID e si riprende subito se il
   processo è morto, un SIGTERM chiude il giro dal `finally` (provato:
   uscita 143, nessun lock o `.partial` residuo, versione servita intatta).
   Una build fallita non chiude più il giro se nel frattempo è arrivato un
   commit nuovo, che copre anche la corsa fra scrittura del reflog e
   spostamento del ref. Il seguito in `nixos` è fatto (`7eb6811`, riportato
   dall'istanza di `nixos`): `ExecCondition` con `serve.py --check`,
   `RestartPreventExitStatus=3`, timeout della pubblicazione a 5 minuti.
   Provati il salto della unit senza versione valida (0 riavvii, diagnosi
   nel journal) e lo stop durante una pubblicazione (nessun lock,
   `.partial` o sorgente temporanea residui, versione servita intatta). Non
   collaudata l'uscita 3 a server avviato, una corsa difficile da
   riprodurre. Da quel collaudo viene una correzione in `metodo`: una
   pubblicazione interrotta ora si registra in `status.json`.

3. **Migrare `metodo` e incidere il canone**, dopo la preparazione dell'host:
   - `.gitignore` con `/view/` e rimozione dall'indice. `git rm --cached`
     conserva l'output sul checkout che lo esegue, ma il pull del commit di
     rimozione può eliminare i file tracciati negli altri checkout: predisporre
     e provare il passaggio mantenendo disponibile l'ultima vista buona;
   - `kb/view.md`: riscrivere Freschezza, Perimetro, HTML e Servizio con il
     contratto portabile; ammettere lo spazio temporaneo e la versione valida
     necessaria alla pubblicazione, senza fonti mantenute a mano;
   - `goal.md`: proporre «viste facilmente consultabili, riproducibili dalle
     fonti» al posto di «viste che si aprono dal checkout»;
   - gate di `/commit`: la build **resta come verifica**, il suo output non
     entra più nel commit e non viene pubblicato. Resta il giudizio sugli
     artefatti di sintesi `i2/`;
   - `/adottanti`: separare i tre controlli del contratto; aggiornare i
     riferimenti alla versione delle viste nelle skill e nei nodi
     (`project-structure`, `presentation`, `karpathy-pattern`, `zettelkasten`),
     nelle bussole e nelle istruzioni dei builder.

   **Stato al 2026-10-07: fatto in `metodo`.** `view/` è in `.gitignore` e
   fuori dall'indice; la build locale si dichiara anteprima nella home.
   `kb/view.md` ha Freschezza, HTML e Servizio riscritti, la nuova sezione
   «Pubblicazione» col contratto e una Transizione per gli adottanti che
   versionano ancora `view/`. `/commit` ed `exec plan` usano
   `build.py --check`, `/adottanti` separa i tre controlli; `goal.md` ha la
   formulazione approvata dal custode. `presentation`, `karpathy-pattern` e
   `zettelkasten` nominano `view/` senza presupporne il versionamento e non
   sono cambiati. Provato su una copia dei soli file tracciati: audit senza
   link rotti, `--check` e build riusciti, `view/` ignorata. Resta da
   osservare su `deck` il commit che rimuove `view/`: la pubblicazione non
   dipende dal checkout, ma è la prova di accettazione ancora aperta.

4. **Prescrivere il recepimento ai sette adottanti** dopo il collaudo su
   `metodo`. Ogni `method` locale ratifica builder e modalità di pubblicazione,
   prepara il proprio host, prova, poi rimuove `view/` da git e verifica la
   porta. La preparazione dei servizi in `nixos` è una dipendenza esplicita
   per i repo che serve, non un passo successivo alla rimozione dell'output.

   **Stato al 2026-10-07: prescritto** in
   [`o3/viste-fuori-da-git.md`](../o3/viste-fuori-da-git.md), con l'ordine
   builder → host → git per ogni repo. La ricetta, provata in un clone di
   `nixos` e uno di `salute`, ha fatto emergere un difetto del canone:
   l'interfaccia dei builder di deck di dominio non riceveva la cartella di
   uscita, e `nixos_deck.py` chiudeva i link su `root / "view"`. Ora è
   `render(root, reveal_url, folder)`, e la firma vecchia ferma la build.
   Il task resta aperto sul recepimento dei sette. `nixos` ha recepito per
   primo lo stesso giorno, fino a `view/` fuori da git e la sua porta 8002
   nella forma pubblicata; lo stato per repo vive nella prescrizione.

5. **Adattare a `danea-auto`** tramite il suo `method`: su `danea2` la verifica
   precede il commit, la pubblicazione lo segue su fonti pulite. Definire il
   comando o meccanismo locale che esegue questo secondo passo e il recupero
   all'avvio; la sola build del gate non basta. Il seguito coinvolge anche
   `o3/scheduler/serve_presentazione.pyw`. Collaudare il passaggio fra versioni
   con il server Windows in funzione prima di rimuovere l'output da git.

## Prove di accettazione

La prova su `metodo` deve produrre evidenza dei seguenti esiti; la prescrizione
richiede il collaudo del servizio locale e delle differenze di piattaforma.

- Build riuscita: contratti e controllo finale passano; con le stesse fonti
  e toolchain l'output è identico. Dopo pubblicazione la porta rende le nuove
  pagine e l'hash del commit costruito.
- Errore tardivo simulato, anche dopo il rendering: nessun file della versione
  pubblicata cambia, la porta continua a servire quella versione e l'errore
  è leggibile. Una nuova build riuscita ripristina l'aggiornamento.
- Primo avvio senza output e riavvio con output arretrato: il servizio
  costruisce e pubblica senza attendere un altro pull. Senza build valida
  l'assenza è diagnosticata, senza ciclo di riavvio incontrollato.
- Modifiche locali o fonti non tracciate: l'anteprima resta possibile, ma
  la pubblicazione non le attribuisce a `HEAD`. Dopo il commit il nuovo hash
  corrisponde alle fonti rese, anche nel flusso locale di `danea2`.
- Aggiornamento durante una build e richieste HTTP durante la pubblicazione:
  nessuna resa parziale o di fonti mescolate; l'ultimo commit richiesto viene
  infine pubblicato. Definire il comportamento delle richieste già in corso.
- Pull del commit che elimina le viste tracciate: l'host già predisposto
  conserva la disponibilità della versione valida e pubblica la nuova.
- Audit: distinguere build fallita, versione servita arretrata e porta non
  raggiungibile, senza confondere l'uguaglianza degli hash con la correttezza
  del generatore.

## Decisione: pull manuale su deck

Il custode ha deciso il **2026-10-07**: per ora `deck` si aggiorna con un
pull manuale. Dopo un commit e un push da `game` le pagine su `deck` restano
vecchie finché il custode non aggiorna il checkout; da quel momento build e
pubblicazione sono automatiche. Resta un gesto distinto per aggiornare il
sito, che si può dimenticare dopo il push.

L'aggiornamento automatico non è escluso per il futuro. Se si riapre, va
definito il checkout dedicato alla pubblicazione, il ramo seguito, la
gestione degli errori e il comportamento con modifiche locali o divergenze,
senza sovrascritture né risoluzioni automatiche dei conflitti; il collaudo
copre l'intero flusso `game → remoto → deck`, compreso il recupero dopo
indisponibilità del remoto. La scelta per `deck` non implica che ogni host
adottante debba usare lo stesso meccanismo.

## Confini e verifiche sul Mondo

- Verificare le porte dai luoghi dell'audit, in particolare `danea2` da casa
  e la coppia server dal lavoro. Una verifica mancante resta dichiarata.
- Il push resta su richiesta e il pull resta manuale (decisione sopra).
  Fino all'aggiornamento del checkout sull'host, la vista remota può
  restare indietro.
- Il deck in `presentation/` resta versionato come sorgente; solo la resa
  in `view/` esce da git.
- La rimozione dei cloni di `danea-auto` dagli altri host è una decisione
  separata, non un requisito per pubblicare correttamente su `danea2`.
- Il canone prescrive; gli adottanti ratificano. Preparazione e deploy degli
  host passano dai rispettivi repository e mandati.

## Bilancio e momento

Il guadagno ricorrente è la leggibilità dei diff e l'assenza di output stale
nella storia; il costo comprende builder, pubblicazione affidabile, collaudo
su Linux e Windows e recepimento nei sette adottanti. La prima prova su
`metodo` rende questo costo osservabile prima della propagazione.

Coordinare con `migrazione-viste`, che tocca gli stessi servizi, senza rendere
la pulizia del ramo vecchio dipendente dall'intera nuova architettura. La sua
chiusura richiede le verifiche già dichiarate nella prescrizione, non la sola
approvazione di questo task.

La pulizia della storia è scartata: nessun commit tocca solo `view/` (0 su
25), lo spazio non cala perché i PNG sono gli stessi blob di
`presentation/`, e la riscrittura degli hash romperebbe i marker degli
adottanti e i riferimenti nei `.md`. Basta `git rm --cached` da qui in
avanti.

## Criterio di chiusura

Il task si chiude dopo il collaudo e la migrazione effettiva di `metodo`, il
canone rivisto e la prescrizione pubblicata con ordine di recepimento e prove.
L'approvazione della direzione o la sola modifica documentale non bastano.
Le evidenze della prova e gli eventuali limiti residui devono essere leggibili
prima della chiusura. Il seguito negli adottanti vive nella prescrizione;
quello dei servizi vive nel plan di `nixos`, senza dichiararlo compiuto per
il solo handoff.
