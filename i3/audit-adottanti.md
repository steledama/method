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

**Canale del canone: tutti e sette `aligned` su `origin`.** Riletti il
2026-10-07 da `deck` dopo un `git fetch`: `nixos`, `bi`, `economia`,
`salute`, `crm` e `baserow` a `35a08d5`; `danea-auto` a `a344f64`
(`c3acb33`). Il 2026-10-08 `danea-auto` è a `6e1d95f` (`e8ad9c9`),
verificato su `origin`: `migrazione-viste` e `viste-fuori-da-git` sono
recepite dai sette e chiuse, con la forma vecchia dei servizi tolta in
`nixos` (`422bb5b`) e in `danea-auto` (`11c0510`).

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
`world.md` in `crm`). Le 8765 residue sono solo di migrazione (firewall
transitorio di `nixos`, rimozione della regola in `danea-auto`); in `crm` la
8765 è il server dei test Playwright. L'attivazione resta nei task locali:
`nixos` `o2/serve-project-presentations.md`, `danea-auto`
`o2/presentazione-permanente-danea2.md`. Il link `Ob.`→`goal.md` è
verificato nei file: in tutte e sei le `tasks.html` le ancore corrispondono
alle intestazioni del rispettivo `goal.md`.

**Prescrizioni aperte, verificate nei file:**

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
- `liste-o3-i1-fedeli-alla-fonte` — ha un esito in tutti e sei, ma non
  sempre è un recepimento. La riscrittura Pandoc è nei file di `nixos`,
  `bi` e `danea-auto`, che ha forkato i builder per la prima volta.
  `economia` e `salute` tengono il proprio renderer Python con una
  divergenza motivata nel marker: i loro indici non hanno gerarchie che il
  renderer appiattisce, e in `economia` Pandoc non è nel `flake.nix`. `crm`
  non ha viste a elenco: non si applica. Potata il 2026-10-01;
- `revisione-bootstrap-adottante` e `ingresso-adottante` — non verificate
  nel merito (cfr. Limiti); `salute` le dichiara una soddisfatta e una non
  pertinente.

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

Classificazione degli scostamenti:

- **segnale i1**: i builder della presentazione assumono il toolchain degli
  host Linux. È la codifica delle chiamate a pandoc, più il pin di reveal.js
  accoppiato a una versione di pandoc non fissata. Viene da `danea-auto`, è
  verificato nel canone ed è valutato nel filo
  `toolchain-builder-presentazione` (propagazione chiusa il 2026-10-02);
- **nessuna prescrizione nuova**: le aperte sono recepite o in attesa del
  loro battito;
- **coda di dominio**: la data aggregata di `nixos`, l'attesa semestrale di
  `bi`, il plan fermo di `crm`;
- **per `exec perform`**: `obiettivo-del-plan-collegato-al-goal` è potata il
  2026-10-01 (`ff064c1`), `liste-o3-i1-fedeli-alla-fonte` lo stesso giorno,
  dopo la verifica nei file.

## Tensioni aperte

- `aligned` e file: coincidono da tre giri (2026-09-25, 2026-09-30,
  2026-10-01). Finché non è confermato, il battito verifica le prescrizioni
  nei file e non nei marker; se il 2026-11-01 coincidono ancora, la verifica
  d'insieme si alleggerisce;
- `revisione-bootstrap-adottante`: la prescrizione resta aperta finché i sei
  registrano nel marker un esito sulla revisione coordinata di README,
  CLAUDE, Goal e World, divergenze motivate incluse. Il merito non si
  verifica in un giro d'insieme (cfr. Limiti);
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

- `revisione-bootstrap-adottante` e `ingresso-adottante` non verificate nel
  merito: richiedono una lettura qualitativa dei quartetti di bootstrap,
  fuori dalla portata di un giro d'insieme su sei repo;
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
