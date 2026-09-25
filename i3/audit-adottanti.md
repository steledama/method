---
ciclo: runtime
---

# Audit runtime-o1: la distanza degli adottanti dal telos

**Misura**: «Propagare il canone e chiudere il loop con gli adottanti»
(`goal.md`, obiettivo 2).

Verdetto aggregato dell'audit mensile `/adottanti`, aggiornato in place a
ogni giro. Ultimo giro: **2026-09-24**, terzo battito, eseguito con 23 giorni
di ritardo sulla scadenza del 2026-09-01 (HEAD `435a1e2`). È il primo giro
sui **sei** adottanti. Le letture sono fatte sulle superfici per host: `deck`
per `economia` e `salute`, `ssh svezia` per `nixos`, `bi`, `crm` e
`danea-auto`. Le copie su `deck` dei repo di `svezia` possono essere stantie:
quella di `crm` era ferma al 2026-08-21, mentre `svezia` è al 2026-09-08.

Il **2026-09-25** una rilettura parziale, non un battito, ha riaperto due
sole lenti: il canale del canone (marker su entrambi gli host) e il lessico
della struttura cercato nei file, fuori dai nodi in symlink. Il resto del
verdetto resta quello del 2026-09-24.

## Verdetto

**Canale del canone: tutti e sei alla HEAD.** Il 2026-09-25 ogni adottante
ha girato `/method` e porta il marker a `eb3f400`, `aligned`. Si chiudono
così anche i due ritardi del 2026-09-24: `crm` era a `5b5e344`, 8 commit
indietro, e `danea-auto` ad `ab7003b`, 21 commit indietro con canone
strutturale in mezzo. Il salto di `danea-auto` è stato assorbito in un
solo giro (`4cea53b`). La copia di `danea-auto` su `svezia` è un commit
indietro rispetto a origin e mostra ancora il marker vecchio: è stantia,
non in drift.

**Prescrizioni aperte, verificate nei file invece che dichiarate dai marker:**

- `chiusura-task-controlla-world` — **recepita da tutti e sei**: l'`exec`
  di ognuno enumera le materializzazioni nel Mondo. Consumata e potata il
  2026-09-25;
- `liste-o3-i1-fedeli-alla-fonte` — la versione del 2026-09-09 (walker
  strutturale) è recepita dove esiste un generatore: `bi` e `nixos` col fork,
  `salute` che la soddisfaceva già col proprio. La versione Pandoc del
  2026-09-21 non è in nessun fork, ma è proprio il commit non ancora
  recepito. `crm` e `danea-auto` non hanno `build_lists.py`, quindi la
  prescrizione non si applica;
- `semplificazione-lessico-struttura` — il 2026-09-24 era **non recepita**
  in `bi`, `crm` ed `economia`, tutti `aligned`. Il 2026-09-25 `crm`
  (`2034b26`) ed `economia` (`d9ecd89`) la recepiscono e lo dicono nel
  soggetto del commit. `salute` dichiara nel marker di aver riletto le
  prescrizioni aperte nei file e non solo nel delta. **`bi` no**: il lessico
  è ancora vivo in `README.md` («La legenda dell'atrio», «ali
  trasversali»), in `CLAUDE.md` («bootstrap (atrio)») e in
  `i2/bi-in-sintesi.md`, che dice «la root è l'atrio». Il suo marker è
  passato `aligned` a `eb3f400` (`afa4702d`) senza nominare la prescrizione
  né una divergenza: è il terzo `/method` che non la vede. Restano residui
  di una frase negli indici `o3/prescriptions.md` di `nixos` («questa
  stanza») e di `crm` («inventario dell'atrio»);
- `revisione-bootstrap-adottante` e `ingresso-adottante` — non verificate in
  questo giro: richiedono una lettura qualitativa del quartetto
  README/CLAUDE/Goal/World che l'audit d'insieme non ha fatto (cfr. Limiti).

**Il watchpoint sul valore del marker ha il suo secondo segnale.** Il
2026-08-22 `aligned` aveva certificato un gap documentale una volta sola, in
`bi` e `crm`. Oggi lo stesso gap è vivo in tre repo: `bi` lo porta dopo due
`/method` successivi alla segnalazione, `economia` è un repo nuovo nel conto,
e `crm` lo mette nel titolo di una sezione del marker. La guardia dal-basso è
soddisfatta: la domanda passa a `i1/` come segnale
(`marker-aligned-non-verifica-prescrizioni.md`). Chiede se `/method` debba
verificare le prescrizioni aperte anteriori al proprio cursore.

Fotografia delle code (`development-goal`, pesata sulla gradualità di
dominio):

- **nixos** — coda dev vuota, 7 task runtime (3 in `world`), da 5 ad
  agosto: composizione da telos. Le due skill di manutenzione autonome si
  sono **fuse** in `/manutenzione` (`4236918`, 2026-08-02), che è diventata
  il battito unico e ha girato in 35 giorni distinti dal 1° agosto, di fatto
  ogni giorno. La riga `(quotidiano)` in `## Scadenze` porta però ancora la
  data **2026-08-01**. Non è un orologio fermo: le cadenze sono passate alla
  config per entità di `i1/manutenzione.json` e la data aggregata ha smesso
  di significare qualcosa. La lente delle scadenze ne fa un falso rosso. È
  coda di dominio, ma tocca il segnale i1 aperto
  `registro-perpetuo-vs-cattura-singola`: dove l'orologio vive nel registro
  perpetuo, il plan non sa più che data scrivere.
- **bi** — fase di cantiere: 12 task, 9 dev e 3 runtime (13 con 8 dev ad
  agosto). È l'adottante con l'uso più intenso delle skill nuove: circa 15
  giri `eval`/`exec` fra il 14/8 e il 23/9, su segnali di produzione veri,
  come la regressione del retry OAuth intercettata il 2026-09-08
  (`1f9b1a0a`). Timetable dei cinque run automatizzati intatto; la
  semestrale concorrenza del 2026-07-31 è annotata come attesa, non stantia.
  Tre skill di dominio sempre autonome.
- **economia** — 17 task runtime, 0 dev, in-the-loop per costituzione come
  ad agosto. Tre date passate in `## Scadenze` (24/8, 1/9, 8–10/9) sono tutte
  annotate con l'esito da riconciliare: orologio manuale seguito, non fermo.
  Coda di dominio.
- **salute** — 4 task runtime, 0 dev; ad agosto erano 7 attivi (2 dev) più
  7 sospesi in holding. La sezione holding non c'è più: la coda si è
  **svuotata**, non spostata. `## Scadenze` porta solo appuntamenti datati,
  tutti futuri tranne quello di oggi.
- **crm** — prima baseline, contata a mano (niente `kb_tools.py`, per scelta
  dichiarata) su `fae4824`: 6 nodi KB, 2 sintesi i2, 2 fili i3, 9 task tutti
  dev, nessuna `## Scadenze`. La struttura ha retto al primo lavoro vero:
  contratto `policies.v1`, semantica dei movimenti Danea e 4 viste generate
  e fresche. Il plan però è fermo dal 2026-08-21: da allora solo
  allineamento e manutenzione Docker. `/kb` non è ancora forkata
  (divergenza dichiarata: arriverà coi primi strumenti deterministici).
- **danea-auto** — controprofilo in produzione, fermo dal 2026-08-22: 4 nodi
  KB, 2 sintesi i2, 1 filo i3, 3 task runtime (1 `world`), invariato dalla
  baseline di agosto. Niente `presentation/` e niente `/commit`, divergenza
  dichiarata («finché non hanno una funzione locale»). Qui l'audit non
  certifica Danea, Task Scheduler né il backup: il marker lo esclude.

Superfici e viste: `nixos`, `bi`, `economia`, `salute` e `crm` hanno le viste
alla stessa data dell'ultima modifica delle fonti. `crm` è l'unico con la
vista del plan (2026-09-08) più recente del plan stesso (2026-08-21): è una
rigenerazione, non un drift. Nessuna vista a mano trovata. Il segnale del
2026-08-01 su `economia` («cablaggio plan×`o2/` non esercitato») non si
rilegge qui: resta una tensione, cfr. Limiti.

**Materiale per la clausola di uscita delle skill per arco**
(`o2/rivalutazione-skill-per-arco.md`). Il conteggio è per commit, quindi un
proxy, non il contenuto delle sessioni:

- dal 2026-08-01 nessuno stadio è vuoto ovunque: tutti e sei gli adottanti,
  più `metodo`, hanno commit che toccano `i2/` (da 2 a 32) e `o3/`;
- in `bi` i giri `eval` scrivono quasi solo `i3/` e `o2/` (i1 = 2 commit,
  i2 = 5, i3 = 64). La sua `interpret` è delegata agli script, col registry
  `o3/lib/perception.js`: lo stadio esiste ma vive nel codice. È
  l'accorpamento degli scope previsto dalla clausola, fatto spontaneamente;
- il costo dell'assorbimento non risulta sentito in `salute` né in
  `economia`: nessuna traccia nei fili o nei marker. `bi` lo cita solo in
  anticipo, come motivo per non assorbire. Nel controfattuale, le skill
  autonome di `nixos` si sono ridotte da sole;
- gli **esiti nulli** per stadio, il criterio principale del «troppo», non
  lasciano traccia versionata in nessun repo: con la misura attuale non si
  possono contare.

Classificazione degli scostamenti:

- **segnale i1**: marker `aligned` che non verifica le prescrizioni aperte
  (nuovo);
- **nessuna prescrizione nuova**: il lessico ha già la sua prescrizione
  aperta, manca il recepimento;
- **coda di dominio**: la data aggregata di `nixos`, le date annotate di
  `economia`, il plan fermo di `crm`, `danea-auto` fermo;
- **per `exec perform`**: fatto il 2026-09-25. `chiusura-task-controlla-world`
  è potata, e la nota stantia su `aggiorna-overlay`→`overlay` in
  `o3/prescriptions.md` è corretta.

## Tensioni aperte

- ripetibilità: tre battiti eseguiti, ma il terzo è arrivato con 23 giorni
  di ritardo sulla scadenza. La cella runtime-o1 della matrice resta D: il
  ritmo è dimostrato solo quando il battito arriva senza essere ricordato a
  mano;
- `crm`: il plan è fermo dal 2026-08-21 con 9 task dev. Al prossimo giro va
  visto se riprende, o se la struttura adottata è rimasta scaffolding
  intorno a un lavoro spostato altrove;
- `danea-auto`: il ritardo di canone è chiuso (2026-09-25) e il repo è
  ripartito anche nel dominio (`75b8685`, diagnostica dei run fatali). Il
  prossimo giro verifica che il salto di 21 commit assorbito in una volta
  abbia retto nei file e non solo nel marker;
- il lessico `atrio`/`ali` in `bi`: da verificare nei file al prossimo giro,
  qualunque cosa dichiari il marker. È il caso che tiene aperto il segnale
  `marker-aligned-non-verifica-prescrizioni`;
- `nixos`: la data aggregata della riga `(quotidiano)`, da leggere insieme
  al segnale i1 sul registro perpetuo;
- `salute`: resta nella sua coda la domanda se la home basti a esercitare il
  contratto plan×`o2/`;
- la clausola di uscita delle skill per arco: decisa il 2026-09-24 sul
  materiale di questo giro (la tripartizione resta, gli esiti per stadio vanno
  nel trailer `Esiti:`). Il battito del 2026-11-01 verifica il recepimento
  di `esiti-per-stadio-nel-commit` e conta i trailer.

## Limiti

- `revisione-bootstrap-adottante` e `ingresso-adottante` non verificate:
  richiedono una lettura qualitativa dei quartetti di bootstrap, fuori
  dalla portata di un giro d'insieme su sei repo;
- l'uso delle skill per arco è misurato per commit e messaggi, non per
  sessioni: un giro concluso vuoto non lascia commit e resta invisibile;
- Superfici remote verificate per struttura e marker, non col test di
  freschezza sul contenuto (ultima modifica fonte vs vista): resta per un
  giro con accesso pieno o per i `method-review` locali.
