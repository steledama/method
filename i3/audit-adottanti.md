---
ciclo: runtime
---

# Audit runtime-o1: la distanza degli adottanti dal telos

**Misura**: «Propagare il canone e chiudere il loop con gli adottanti»
(`goal.md`, obiettivo 2).

Verdetto aggregato dell'audit mensile `/adottanti`, aggiornato in place a
ogni giro. Ultimo giro: **2026-08-01** (secondo battito, anticipato
dall'11; HEAD `dbed337`, letture via le superfici per host dichiarate in
`world.md`). Il verdetto sotto fotografa i **quattro** allora in territorio.
`crm` e `danea-auto` sono entrati il 2026-08-12, dopo il giro, e sono materia
del prossimo.

## Verdetto

Il canale del canone ha fatto il giro completo in un giorno: **tutti e
quattro hanno recepito** la rifilatura `eval`/`exec` e la quinta domanda, con
i rispettivi piloti del montaggio decisi — `nixos` e `salute` (marker a
`0128891`; `salute` col commit `e6d6f28`), `economia` (marker a `d2607f6`,
commit `1844978`) e `bi` per ultimo (marker a `3940c8b`, commit `20cf5b7d`).
Le due prescrizioni sono consumate e potate dalla collezione. Tutti
`aligned`, nessun `action-required`.

Fotografia delle code — la metrica del telos, pesata sulla gradualità di
ciascun dominio (`development-goal`, fotografie per artefatto):

- **nixos** — coda dev vuota, 5 task runtime (2 in `world` su upstream):
  composizione da telos, come a luglio. Ma **due date stantie** in
  `## Scadenze`: quotidiano e settimanale fermi al 2026-07-19 (il mensile
  scade oggi) — orologio fermo o riga non avanzata, il segnale che la lente
  scadenze esiste per cogliere. Coda di dominio (materia del suo
  `exec plan`, dal recepimento), da verificare sciolta al prossimo giro.
  `nix-overlay-update` confermata skill autonoma dal pilota del montaggio
  (signifier onesto, catalogata nel suo o3).
- **bi** — fase di cantiere: 13 task di cui 8 dev (tassonomia, motore
  riordini, modello sito), da 1 su 7 a luglio — legittimo per un progetto in
  costruzione. La **terza specie è maturata in timetable canonico**: cinque
  run automatizzati con gli orari che vivono solo nel plan e le config
  scheduler che li implementano e rimandano — la tensione del primo giro («va
  vista reggere alla lettura») è sciolta. Due orologi manuali sforati di un
  giorno: fisiologico. Rifilatura recepita per ultima (`20cf5b7d`): tre skill
  di dominio autonome per esito del pilota, colonna `Ob.` portata nel
  generatore e provata su entrambi i modi di rottura — che ha subito rilevato
  una voce del register non corrispondente a nessuna riga del plan (quarta
  incarnazione del «vincolo che arriva tardi rivela»).
- **economia** — 17 task runtime, 0 dev, in-the-loop come da costituzione;
  colonna `Ob.` viva (ne è l'origine, e la divergenza è rientrata a canone in
  quattro giorni), ordinamento dichiarato «per imminenza della prossima
  mossa», chiose per titolo (divergenza registrata). Rifilatura recepita in
  serata (`1844978`, marker a `d2607f6`): tre skill assorbite come scope di
  `eval`, entrambe le prescrizioni chiuse.
- **salute** — 7 task attivi (2 dev) più 7 sospesi ought in holding,
  `## Scadenze` di soli appuntamenti sanitari datati (imminente il 7/8):
  coerente col riequilibrio prescritto. Il suo gap contiene il **ritorno
  della sua stessa percezione**: «vista a mano inverte l'effetto» (f8e8a73) è
  diventata il contratto derivata-implica-verificata (a7fa93e) e il canone
  della freschezza — il loop dal basso ha inciso, e la gamba di ritorno è
  arrivata in giornata col recepimento (`e6d6f28`): il giro
  percezione→canone→ritorno chiuso in quattro giorni.

Superfici e viste: `nixos`, `bi` e `salute` hanno il contratto plan×`o2/`
cablato ed esercitato — ciascuno ha rotto la build al primo contatto su una
divergenza reale (`salute` col recepimento di oggi); `economia` ha il canone
ma il cablaggio nel suo fork non è ancora stato esercitato, mentre la
freschezza sì (tre entrypoint nel gate, viste già fresche). Nessun segnale
rosso rilevato, col limite dichiarato sotto.

Nota fuori giro — spazzata dei marker del **2026-08-12** durante un `eval`, non
un battito, quindi il cursore del filo resta al 2026-08-01: `nixos`, `bi` ed
`economia` sono a `2bc3cd4`, `salute` a `9e9e3be`, `crm` e `danea-auto` a
`c6939d6`, tutti `aligned`. `bi` ed `economia` portano ancora `ciclo: runtime`
nel marker, che `b39c8a7` ha
corretto in `dev`: **non è drift** — la correzione è successiva al loro cursore e
il loro prossimo `method` la recepisce. `nixos` ha già `dev` come adattamento
dichiarato, che `b39c8a7` ha canonizzato: al suo prossimo giro la dichiarazione
di divergenza si cancella (`method/SKILL.md`, «una divergenza riassorbita si
cancella dal ledger»). Questo è lo stato da cui parte il battito di settembre.

Seconda nota fuori giro, verificata il **2026-08-16**: `bi` ha ormai usato
`eval` e `exec` ripetutamente su eventi reali dal 5 al 14 agosto, quindi il
collaudo d'uso non è più vuoto. Il marker di `danea-auto`, rivisto il 14 agosto,
registra inoltre quattro task passati dal vivo sui nuovi entrypoint e il backup
Drive verificato; resta non esercitato il percorso diagnostico, mentre sessione
desktop, Danea, LibreOffice e sito e-commerce restano non certificati. Il
cursore mensile resta al 2026-08-01: questi sono segnali per la baseline di
settembre, non un terzo battito anticipato.

Terza nota fuori giro, verificata il **2026-08-22** durante un `eval compare`,
non un battito: le **tre prescrizioni aperte** in `o3/` sono tutte anteriori a
`ab7003b`, il commit a cui i quattro marker raggiungibili si dichiarano
`aligned` il 2026-08-21 — quindi il loro mancato recepimento non è ritardo
event-driven fra un battito e l'altro. `chiusura-task-controlla-world` risulta
recepita da tutti e quattro; `semplificazione-lessico-struttura` **no**: `bi`
porta ancora `ali` e `atrio` in `README.md` e `ali` in `CLAUDE.md`, `crm` porta
`atrio` in `README.md` e intitola `## Bootstrap e atrio` la sezione del proprio
marker, mentre dichiara «nessuna eccezione oltre alla toolchain». Non è una
divergenza motivata: è un vuoto non visto. `economia` e `salute` stanno su
`deck`, non letti in questo giro. Il cursore mensile resta al 2026-08-01:
questo è materiale pre-raccolto per il battito di settembre, che parte dalla
verifica invece che dalla scoperta.

Ne segue un **watchpoint** sul valore probatorio del marker: `aligned` ha qui
certificato più di quanto avesse verificato, e su un gap **documentale** —
esattamente ciò che `aligned` copre, non il runtime esterno che
`method-observatory` già esclude. Resta watchpoint e non filo autonomo: è una
istanza sola, e la guardia dal-basso di `method-development` chiede il secondo
segnale prima di generalizzare. Se il battito di settembre ne trova un secondo,
la domanda diventa se `/method` debba verificare il recepimento delle
prescrizioni aperte invece di dichiararlo.

Classificazione degli scostamenti: **nessuna prescrizione nuova** (le due in
canna — quinta domanda attiva, rifilatura pianificata — coprono tutto il
drift osservato), **nessun segnale i1 nuovo** (la maturazione della terza
specie in `bi` corrobora `ricorrenza-per-battito`, non apre un filo), date
stantie e orologi sforati = **code di dominio**.

## Tensioni aperte

- ripetibilità: due battiti eseguiti (il secondo anticipato di dieci giorni):
  la cella runtime-o1 della matrice resta D finché il ritmo non è dimostrato
  su più giri regolari;
- **`crm` quinto adottante** (entrato il 2026-08-12, allineato al canone
  corrente): il territorio passa da quattro a cinque e il battito del
  2026-09-01 è il suo primo audit. Non ha storia da confrontare — la lente da
  usare è la **baseline fondativa**, non la distanza dal giro precedente: un
  codebase ancora vuoto rende la composizione della coda un dato debole, e il
  segnale utile è se la struttura adottata regge al primo lavoro reale invece
  di restare scaffolding. Vincolo concreto da non ignorare: `crm` non ha
  `o3/kb_tools.py` (scelta dichiarata — struttura prima delle automazioni),
  quindi i numeri strutturali che le altre righe portano **per lui non
  esistono** e la lente non deve andarli a cercare: il suo dato si conta a
  mano. Da qui esce anche il primo dato per `adopter-comparison`, che oggi lo
  tiene fuori dai conteggi comparativi;
- **`danea-auto` sesto adottante** (entrato il 2026-08-12, marker a
  `c6939d6`, commit locale `57ef8a6`): è il controprofilo di `crm`, un artefatto
  già in produzione che conserva intenzionalmente entrypoint AHK/PowerShell in
  root e segnali runtime nei path correnti finché le migrazioni i1/o3 non
  saranno validate dal vivo. Il primo audit deve leggere questa gradualità e
  non scambiare i limiti documentali dell'adozione per certificazione di Danea,
  Task Scheduler, backup o sessione Windows. Baseline contata a mano: 4 nodi
  KB, 1 sintesi i2, 1 filo i3, 5 task e 3 skill locali; quantità misurate sul
  checkout `57ef8a6`, non confrontabili con la fotografia del 2026-06-03;
- il collaudo d'**uso** delle skill nuove: `bi` ha iniziato i giri reali di
  `eval`/`exec`; restano da osservare gli altri profili, gli esiti nulli per
  stadio e il costo dell'assorbimento fino alla clausola di uscita
  (risveglio anticipato al 2026-09-01; 2026-11-01 solo fallback motivato);
- `nixos`: le due date stantie del quotidiano/settimanale — verificare
  sciolte al giro di settembre;
- `salute`: la gamba di ritorno della sua percezione è arrivata col
  recepimento (`e6d6f28`: contratto plan×`o2/` cablato nel generatore della
  home, che ha subito rotto su una divergenza reale) — resta nella sua coda
  la domanda se la home basti a esercitare il contratto;
- `economia`: il cablaggio del contratto plan×`o2/` nel suo fork non è ancora
  stato esercitato — unico dei quattro, materia della lente 5 a settembre;
- il **costo dell'assorbimento** sollevato da `economia`: con gli scope di
  dominio montati sulle canoniche, l'`ls` di `.claude/skills/` non è più
  l'inventario completo delle capacità — da misurare all'uso nei due repo che
  hanno assorbito (`salute`, `economia`), mentre `nixos` e `bi` restano il
  controfattuale a inventario intatto.

## Limiti

- Superfici remote verificate per struttura e marker, non col test di
  freschezza sul contenuto (ultima modifica fonte vs vista): resta per un
  giro con accesso pieno o per i `method-review` locali.
