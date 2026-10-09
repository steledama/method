---
ciclo: runtime
obiettivo: 2
---

# Audit runtime-o1: la distanza degli adottanti dal telos

Verdetto aggregato dell'audit mensile `/adottanti`, aggiornato in place a
ogni giro. Ultimo giro d'insieme: **2026-10-01**, quarto battito, puntuale
sulla scadenza; verifiche fuori giro il 2026-10-02 e il 2026-10-03. Le
letture sono fatte su `origin` dopo un `git fetch`: `economia` e `salute` su
`deck`, `nixos`, `bi`, `crm` e `danea-auto` su `svezia`. `baserow`, settimo
adottante, è entrato il 2026-10-05 fuori giro: le letture qui sotto che
contano «i sei» lo precedono, e la sua baseline fondativa è nella fotografia
delle code.

## Verdetto

**Canale del canone: i sette marker su `origin` dichiarano `aligned` a
`f0c9a9b`, revisione del 2026-10-09.** Lettura dopo `git fetch` dai clone
su `deck`, marker e commit di recepimento con `Autonomia: concordato`:
`nixos` `dcf9ad1`, `bi` `a95c4f10` e `a8c849bd`, `economia` `8ed2926`,
`salute` `7d3a448`, `crm` `cc0500b`, `baserow` `305de15`, `danea-auto`
`bf186fb`. Il dato certifica cursori e commit pubblicati, non la semantica
di ogni file né il runtime. L'ultimo audit mensile resta quello del 01/10.

`goal-senza-fotografia` è chiusa il 2026-10-09: i sette marker ne
dichiarano l'esito, con gli adattamenti locali motivati (in `nixos` il solo
fatto senza altra sede è passato in `kb/rclone-gdrive.md`; in `danea-auto`
due fatti restano nel Goal come buchi di misura con provenienza).

`delega-ciclo` è chiusa lo stesso giorno: i sette hanno `autonomy.md` locale
e il presidio dei casi in `eval perceive`; il riesame dei casi e di un
campione di decisioni ordinarie vive nello step 5b di `/adottanti`, la
raccolta nel passo 3 di `eval perceive` canonico. Nessun caso ancora
raccolto, nessun giro delegato reale. Perimetri decisi dal custode nelle
sessioni: sola lettura e atti di `CLAUDE.md` in `nixos`; rilasci e PROD
riservati in `bi`; deploy, produzione e invii riservati in `crm`; invii come
sola bozza in `economia`. Tre atti sul Mondo delegati: eventi Calendar delle
scadenze in `salute`, backup manuale senza restore in `baserow`, ripristino
di LibreOffice incastrato e test dei task fuori slot in `danea-auto`,
recepimento selettivo con effetto dichiarato sull'osservazione
(`i2/presidio-ipotesi-adottanti.md`). In `nixos` il push rifiutato per
divergenza si è fermato fino al via del custode al rebase: confine
rispettato, primo caso riuscito da riesaminare al battito.

`revisione-bootstrap-adottante` è chiusa lo stesso giorno, dopo la lettura
nel merito dei quattro file su `origin` (`i2/bootstrap-adottanti.md`): il
contratto regge in tutti e sette, con residui editoriali di ultimo miglio
che restano dell'adottante. Il più ampio è `CLAUDE.md` di `bi`, che
riporta un inventario di strumenti già indicizzato altrove; lo stato
corrente nel README di `crm` e `baserow` è un segnale aperto
(`i1/stato-nel-readme.md`). Il marker di `danea-auto` a `bf186fb` la dà
rinviata per la formula del prompt selettivo, mentre il precedente la dava
già soddisfatta: il prossimo `/method` locale può ripristinare l'esito.

`ingresso-adottante` esce dalle prescrizioni lo stesso giorno: è una
procedura dell'osservatorio, non una ricetta da recepire, e vive fra le
procedure di `o3/prescriptions.md`, richiamata da `/adottanti`. Il collaudo
con `baserow` è in `i2/ingresso-adottante.md`; la prima verifica nell'uso
resta al battito del 01/11.

`migrazione-viste`, `viste-fuori-da-git` e `push-autonomo` sono chiuse dal
2026-10-08. La verifica pubblicata del push è sui commit `nixos` `3fdec4e`,
`bi` `42ba5dbb`, `economia` `60d52bc`, `salute` `130ddbc`, `crm` `644b70c`,
`danea-auto` `ffb2953`, `baserow` `623f086`. `bi` mantiene il push su richiesta
quando i commit non pubblicati toccano codice eseguito dal ciclo: lì è un
rilascio. La rimozione della forma vecchia dei servizi è registrata nel
codice di `nixos` (`422bb5b`) e in `danea-auto` (`11c0510`); il marker di
`nixos` conserva un task per confermare la generazione attiva sui server.
Chiusura del canone e attivazione locale restano evidenze distinte.

**`aligned` e file coincidono.** Il 2026-10-02 i sei sono stati ricostruiti
da `origin` in una cartella temporanea: nessun `misura:` negli indici `i3/`,
`obiettivo:` in ogni file di `i3/` verificato dalla build, builder identici
al canone salvo la CONFIG della home e un adattamento dichiarato in
`salute`. La revisione contro gli obiettivi ha ridotto i fili da 38 a 19
(marker inclusi): `crm` tiene solo il cursore, perché col dominio fermo
nessuna tensione era viva. Il 2026-10-03 `presentazioni-permanenti` è
risultata recepita nei file di tutti e sei: `serve.py` identico al canonico,
decisione del custode nei `CLAUDE.md` senza eccezioni, esposizione dei dati
registrata dove ogni repo tiene i propri vincoli (`CLAUDE.md` in cinque,
`world.md` in `crm`). Il link `Ob.`→`goal.md` è
verificato nei file: in tutte e sei le `tasks.html` le ancore corrispondono
alle intestazioni del rispettivo `goal.md`.

**Prescrizioni aperte, con provenienza della verifica:**

- `pull-autonomo` — applicata in `method` il 2026-10-09: regola «Pull
  remoto» in `CLAUDE.md` e aggiornamento del checkout nel passo 1 di
  `/method`, che prima lo vietava. Recepita su `origin` da `economia`,
  `salute`, `crm` e `baserow` a `8796425` e da `bi` a `1f0e55a`
  (`b5c3b785`), dove il push del codice è autonomo dopo l'intera suite
  verde perché il checkout è produzione, e da `nixos` a `33b4f2c`
  (`de2ac9c`): su `deck` la path unit ripubblica le viste a ogni
  spostamento di `HEAD`, quindi il pull è un rilascio delle sole viste, e
  `/manutenzione` passa a `--ff-only` per proteggere il suo lock. Manca
  `danea-auto`, dove il pull del repository su `danea2` è un rilascio da
  decidere;
- `esiti-per-stadio-nel-commit` — il trailer `Esiti:` è nei fork di
  `eval`/`exec` di tutti e sette, e sei lo scrivono davvero. Commit con
  `Esiti:` dal 2026-09-25 al 2026-10-07 su `origin`: `danea-auto` 27,
  `economia` 15, `bi` 11, `baserow` 6, `nixos` 4, `salute` 3. In
  `baserow` uno è nascosto a `%(trailers)` (`205c627`, il segnale i1
  `trailer-esiti-ultimo-paragrafo`); nessun altro caso negli altri repo.
  `crm` non ha fatto giri, quindi non ha righe: il `git log` lo conferma,
  non è un buco di registrazione. La prescrizione resta attiva fino al
  conteggio del 2026-11-01;
- `presidio-ipotesi` — recepita nei file di sei repo a `35a08d5`, ciascuno
  con l'esito nel marker. Il seguito sul deck di `nixos` è chiuso: la
  lettura causale vive in `i2/ipotesi-boot-server.md` e il filo
  `affidabilita-boot-server` la raggiunge, col riesame al 2026-12-31.
  `danea-auto` non l'ha ancora revisionata ed è osservato senza
  sollecitazione (`i2/presidio-ipotesi-adottanti.md`, riesame dal
  2026-10-13);

**Il passo «Rileggi le prescrizioni aperte» di `/method` ha girato in tutti
e sei.** `economia`, `salute` e `danea-auto`, che mancavano, l'hanno fatto
col giro fino a `47d8204`. `salute` elenca nel marker l'esito di ognuna
delle cinque prescrizioni aperte. Gli altri due le riportano nei soli
adattamenti dove le hanno toccate. È il terzo giro in cui `aligned` e i
file coincidono: `aligned` copre ora anche le prescrizioni aperte, e il
marker non avanza finché una pertinente resta senza esito.

**Superfici e viste: fresche in tutti e sette, verificate per
rigenerazione dopo la migrazione.** Il 2026-10-05 ogni repo è stato estratto
da `origin` in una cartella temporanea e ricostruito con
`python3 o3/view/build.py`: build riuscita ovunque, e in sei la
rigenerazione è identica a `view/` versionata. In `danea-auto` cambia solo
`view/presentation.html`, il deck reso da pandoc: costruito su Windows con
pandoc 3.12, qui con la 3.7.0.2, che porta un altro CSS di default e il pin
di reveal.js a `5.1.0` invece di `6.0.2`. È toolchain, non contenuto. Il confronto per date, la lente del
giro precedente, segnalava invece viste più vecchie della fonte in
`economia`, `salute`, `bi` e `crm`. Erano tutti falsi rossi: la fonte era
cambiata fuori dalla parte che la vista rende, per esempio `world.md` sotto
la sua intro. Nessuna vista a mano.

Fotografia delle code (`development-goal`, pesata sulla gradualità di
dominio):

- **nixos** — coda dev vuota, 8 task runtime (7 a settembre). Il
  `goal.md` ha un obiettivo nuovo (3, inferenza locale, 2026-09-27) con i
  suoi task. `/manutenzione` ha guadagnato il ramo `home-manager` e gira
  ogni giorno su più host. La riga `(quotidiano)` porta ancora la data
  2026-08-01: è lo stesso falso rosso di settembre, legato al segnale i1
  `registro-perpetuo-vs-cattura-singola`.
- **bi** — 11 task, 7 dev e 4 runtime (9 dev a settembre): la coda dev
  scende mentre il lavoro è intenso (65 commit in una settimana, un giro
  `eval`/`exec` quasi ogni giorno sul cantiere OEM). Timetable dei cinque
  run automatizzati intatto. La semestrale concorrenza del 2026-07-31 è
  ancora annotata come attesa, ora da due mesi.
- **economia** — 16 task runtime, 0 dev, in-the-loop per costituzione.
  `## Scadenze` densa e tutta futura, salvo un termine di oggi. Il link
  `Ob.` è recepito nella sua vista generata.
- **salute** — 4 task runtime, 0 dev, coda stabile dal 2026-09-27. Le
  scadenze sono appuntamenti datati, tutti futuri.
- **crm** — 9 task dev, plan fermo dal **2026-08-21**: 41 giorni. Dopo
  il 24/9 i suoi soli commit sono allineamenti al canone. La tensione di
  settembre si conferma: il canale col canone funziona, il dominio no.
  È coda di dominio, non drift.
- **danea-auto** — il controprofilo di settembre si è ribaltato: dal più
  fermo al più attivo. 32 commit dal 24/9, 21 giri con `Esiti:`, coda
  da 3 a 6 task runtime su guasti veri (Controlp, dialog Danea, run
  fatali). Ha sciolto da solo le due divergenze dichiarate «finché non hanno
  una funzione locale»: ha adottato `/commit` (con `valida_ahk.ps1` come
  controllo sostanziale) e ha generato `presentation/`. Qui l'audit
  continua a non certificare Danea, Task Scheduler né il backup.
- **baserow** — baseline fondativa all'ingresso del 2026-10-05, contata a
  mano sul checkout di `svezia` al commit di adozione `62396a7`, non ancora
  su `origin`. Marker a `f44b6c0`, `aligned`, con le quattro prescrizioni
  aperte esitate. Contenuto: 4 nodi `kb/`, 2 catture `i1/`, nessuna sintesi
  `i2/`, 2 fili `i3/` più il marker, 3 runbook `o3/`. Plan con 4 task, 3
  runtime e 1 dev, quest'ultimo in attesa di `nixos`. Skill: il quartetto
  forkato più `method`, senza `/kb` e senza skill di dominio. Builder
  identici al canone salvo la CONFIG della home; accento `#0369a1`. Il
  bootstrap regge il contratto comune. Dominio a posta alta e fermo sul
  primo fronte: nessun backup automatico, ultimo archivio del 31 luglio.
  Non c'è storia comparabile, quindi niente delta.

**Materiale per la clausola di uscita delle skill per arco**
(`o2/rivalutazione-skill-per-arco.md`). Primo dato con la misura nuova,
da non giudicare prima del 2026-11-01. Gli esiti `vuoto` adesso esistono e
si contano. Il più frequente è `interpret=vuoto` in `bi`, in tutti e cinque
i suoi giri `eval`. Conferma la lettura di settembre: la sua `interpret`
vive negli script, lo stadio esiste ma la skill non lo esercita.

Il segnale sui trailer resta un solo incidente documentato di perdita,
`baserow` `205c627`. Il marker di `danea-auto` documenta il recepimento del
presidio, non un secondo incidente. Il canone di `/commit` prescrive ormai
l'ultimo paragrafo unico: il conteggio di novembre confronterà trailer e
righe nel corpo, senza riscrivere la storia.

## Tensioni aperte

- `aligned` e file: coincidono da tre giri (2026-09-25, 2026-09-30,
  2026-10-01). Finché non è confermato, il battito verifica le prescrizioni
  nei file e non nei marker; se il 2026-11-01 coincidono ancora, la verifica
  d'insieme si alleggerisce;
- `revisione-bootstrap-adottante`: completare il confronto fra gli esiti
  dichiarati e il contratto della revisione coordinata; i marker da soli
  non equivalgono alla rilettura qualitativa dei quartetti. Il task
  `Goal senza fotografia` ha aggiornato il contratto di questa prescrizione;
- ripetibilità: il quarto battito è arrivato in tempo, ma lo ha ricordato
  l'agente leggendo `## Scadenze` dentro una sessione aperta per altro. La
  cella runtime-o1 resta D finché il battito non parte da un innesco;
- `crm`: 41 giorni di plan fermo con 9 task dev. Al prossimo giro: riprende
  il dominio, o la struttura adottata è scaffolding intorno a un lavoro che
  vive altrove? La domanda è per `crm`, non per il canone;
- `nixos`: la data aggregata della riga `(quotidiano)`, da leggere insieme
  al segnale i1 sul registro perpetuo;
- la clausola di uscita delle skill per arco: il battito del 2026-11-01
  conta gli esiti per stadio e per repository;
- `baserow`, prima verifica nell'uso al battito del 2026-11-01: il segnale
  è lo stato del backup raccolto dai suoi `/eval perceive`. Un timer attivo
  con restore provato chiude il primo fronte. Su `origin` al 2026-10-07 il
  restore è provato (`9f69920`) e strumenti e timer sono versionati
  (`7f3b0d9`); l'attivazione del timer su `svezia` non è verificata da qui.

## Limiti

- i quartetti di bootstrap non sono stati riletti nel giro del 09/10;
  il collaudo dell'ingresso di `baserow` è documentato nella sintesi i2,
  ma non certifica da solo la qualità corrente di tutti i bootstrap;
- la rigenerazione dimostra che le viste sono fedeli ai builder del repo,
  non che i builder siano fedeli al canone: quella è materia dei
  `/method` locali;
- un giro `eval`/`exec` vuoto ora lascia un commit con `Esiti:`, ma solo se
  si è chiuso: una sessione interrotta resta invisibile;
- l'attivazione delle presentazioni permanenti: su `deck` il 2026-10-04 le
  quattro unit `presentazione-*` sono attive. Il 2026-10-05 la produzione
  serve `bi`, `crm` e `baserow` sulle 8001-8003 dopo i rebuild di `nixos`
  (`fb8509c`, collaudo LAN in `ec881e8`, da casa in `41453cc`): verificato
  qui dall'indirizzo LAN di `svezia`, 200 coi titoli giusti, 404 su `/.env`.
  Per `danea2` c'è solo il collaudo riportato dall'istanza di `danea-auto`,
  ora pubblicato su `origin` ma non verificato da qui; lo legge il battito
  del 2026-11-01;
- `origin` resta indietro quando un adottante non pubblica i suoi commit.
  Il 2026-10-05 `danea-auto` aveva recepito `migrazione-viste` a `f21594b`
  nel checkout di `danea2` (`1443454`) mentre `origin` era ancora a
  `91cf874`, e lo stesso per `baserow` (`62396a7`); lo scarto si è chiuso
  il giorno stesso con le pubblicazioni. Le letture su `origin` misurano ciò
  che è pubblicato, non ciò che è stato recepito.
