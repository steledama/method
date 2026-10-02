---
ciclo: runtime
obiettivo: 2
---

# Audit runtime-o1: la distanza degli adottanti dal telos

Verdetto aggregato dell'audit mensile `/adottanti`, aggiornato in place a
ogni giro. Ultimo giro: **2026-10-01**, quarto battito, puntuale sulla
scadenza (HEAD `ff064c1`). Le letture sono fatte su `origin` dopo un
`git fetch`: `economia` e `salute` su `deck`, `nixos`, `bi`, `crm` e
`danea-auto` su `svezia`. La copia locale di `danea-auto` su `svezia` è 17
commit dietro origin: è stantia, non in drift.

## Verdetto

**Verifica fuori giro, 2026-10-02.** Dopo la ristrutturazione della
presentazione e la revisione dei verdetti, i sei sono stati riletti su
`origin` e ricostruiti in una cartella temporanea. Tutti i marker sono a
`8c024a1`, `aligned`, e coincidono coi file: nessun `misura:` negli indici
`i3/`, `obiettivo:` in ogni file di `i3/` verificato dalla build, builder
identici al canone salvo la CONFIG della home e un adattamento dichiarato in
`salute`. Le viste sono fresche in cinque; in `danea-auto` cambiano solo le
intestazioni scritte da pandoc (toolchain, cfr.
`toolchain-builder-presentazione`). La revisione ha ridotto i fili da 38 a 19
(marker inclusi): `crm` tiene solo il cursore, perché col dominio fermo
nessuna tensione era viva. `presentazione-e-verdetti-misurati` e
`toolchain-builder-presentazione` hanno un esito in tutti e sei e sono
potate. Non verificati: lo stato dei firewall dopo i rebuild e il server
LAN da Linux. Il battito del 2026-11-01 resta il prossimo giro d'insieme.

**Canale del canone: tutti e sei alla HEAD del canone recepibile.** Ogni
marker è a `47d8204`, `aligned`: l'unico commit successivo, `ff064c1`, è la
potatura della prescrizione che quei marker hanno recepito. Il recepimento
del link `Ob.`→`goal.md` è verificato nei file, non nei marker: in tutte e
sei le `tasks.html` le ancore corrispondono alle intestazioni del rispettivo
`goal.md`.

**Prescrizioni aperte, verificate nei file:**

- `esiti-per-stadio-nel-commit` — il trailer `Esiti:` è nei fork di
  `eval`/`exec` di tutti e sei, e cinque lo scrivono davvero dal
  recepimento del 2026-09-25: `danea-auto` 21 giri, `economia` 9, `bi` 8,
  `nixos` 2, `salute` 2. `crm` non ha fatto giri, quindi non ha righe:
  il `git log` lo conferma, non è un buco di registrazione. La prescrizione
  resta attiva fino al conteggio del 2026-11-01;
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

**Superfici e viste: fresche in tutti e sei, verificate per rigenerazione.**
Ogni repo è stato estratto da `origin` in una cartella temporanea e
ricostruito coi propri builder. In cinque la rigenerazione è identica alle
viste versionate. In `danea-auto` cambia solo il CSS di default di pandoc:
le viste sono state costruite su Windows con pandoc 3.12, `svezia` ha la
3.7.0.2. È toolchain, non contenuto. Il confronto per date, la lente del
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
  conta gli esiti per stadio e per repository.

## Limiti

- `revisione-bootstrap-adottante` e `ingresso-adottante` non verificate nel
  merito: richiedono una lettura qualitativa dei quartetti di bootstrap,
  fuori dalla portata di un giro d'insieme su sei repo;
- la rigenerazione dimostra che le viste sono fedeli ai builder del repo,
  non che i builder siano fedeli al canone: quella è materia dei
  `/method` locali;
- un giro `eval`/`exec` vuoto ora lascia un commit con `Esiti:`, ma solo se
  si è chiuso: una sessione interrotta resta invisibile.
