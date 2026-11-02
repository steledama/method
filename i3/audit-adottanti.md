---
ciclo: runtime
obiettivo: 2
---

# Audit runtime-o1: la distanza degli adottanti dal telos

Verdetto aggregato dell'audit mensile `/adottanti`, aggiornato in place a
ogni giro. Ultimo giro d'insieme: **2026-11-02**, quinto audit, un giorno
dopo la scadenza: il ciclo autonomo non lancia `/adottanti` e il giro di
`method` del 01/11 era fallito per un errore di rete. Le letture sono fatte su
`origin` dopo un `git fetch` da `deck`, con le estrazioni in una cartella
temporanea. Sono i sei adottanti di `world.md`: `crm` è dismesso dal
2026-10-22 e `abbinamenti`, atteso al suo posto, non è ancora entrato, quindi
non c'è una baseline fondativa da dare.

## Verdetto

**Canale del canone: i sei marker su `origin` dichiarano `aligned`, revisione
del 2026-10-29.** Le posizioni: `economia`, `salute` e `danea-auto` a
`a1814f7`, 4 commit dietro HEAD (`f2a9163`); `bi` e `baserow` a `ad1e4ae`,
5 commit; `nixos` a `321e096`, 11 commit. Il ritardo di `nixos` comprende il
canone del 29/10 sul giro che pianifica i task e non li esegue (`22ead2d`,
`96314f5`, `369d5ea`, `48fff8d`): nel suo `autonomy.md` quella regola
manca ancora, mentre i nodi `kb/` gli arrivano via symlink. Sono commit su
nodi e skill canoniche, non una prescrizione, e hanno due giorni: il ritardo
è fisiologico e il prossimo `/method` locale lo assorbe. Nessuno `status:
action-required`.

**`aligned` e file coincidono, quarto giro di fila (09/25, 09/30, 10/01,
11/02).** Le prescrizioni aperte sono state verificate nei file, non solo
nei marker:

- `esiti-per-stadio-nel-commit`: tutti e sei scrivono il trailer, da 22 a 32
  giri ciascuno dall'08/10 (conteggio sotto);
- `prossimo-task-e-ipotesi-del-giro`: `Prossimo:` c'è in ogni giro dal 22/10
  che ha invocato `plan`. Le cinque eccezioni (`nixos` 1, `economia` 3,
  `salute` 1) sono giri senza lo stadio `plan`, quindi conformi;
- `comunicazione-fra-sessioni`: il rimando a `session-messaging` è nel
  `CLAUDE.md` di tutti e sei;
- `progettazione-skill`: aperta come dichiarano i marker. I punti 4-6 sono in
  task locali in `bi`, `economia` e `danea-auto`, e in corso in `nixos` per
  decisione del custode del 27/10. `salute` e `baserow` dichiarano il
  recepimento completo.

Le prime tre risultano recepite da tutti nei file, ma `o3/prescrizioni.py
verifica` ne dà recepita una sola per adottante su sei. Lo strumento cerca
una riga che nomini la prescrizione fra backtick insieme a «recepit», e due
forme legittime non passano: «già soddisfatta» (`economia` e `danea-auto` su
`esiti-per-stadio`) e l'elenco in prosa senza nomi di `salute` («Esiti per
stadio, momento del commit, prossimo task…»). La chiusura è sospesa: decide
il custode se chiudere sull'evidenza dei file o chiedere ai marker la forma
che lo strumento riconosce (vedi «Tensioni aperte»). Anche l'indice
`o3/prescriptions.md` è indietro: dà `comunicazione-fra-sessioni` recepita
dai soli `nixos`, `bi` e `baserow`.

Con quattro coincidenze, la verifica d'insieme si alleggerisce come
previsto: dal prossimo audit le prescrizioni si leggono nei marker, con il
controllo nei file di una sola prescrizione a campione. Si torna alla
verifica completa al primo scarto.

**Superfici e viste: fresche e verificate in tutte e sette, `danea2`
compreso.** La lettura distingue tre controlli:

- **build e contratti sulle fonti di `origin`**: `python3 o3/view/build.py
--check` termina con codice 0 in tutte e sei le estrazioni;
- **revisione servita**: `/_stato` dà `ok: true` e un `served_commit` uguale a
  `origin/main` per `method`, `nixos`, `salute` ed `economia` su `deck`
  (8001-8004), `bi` e `baserow` su `svezia` (8001, 8003) e `danea-auto` su
  `danea2` (8001). È la prima verifica di `danea2` fatta da qui;
- **porta**: raggiunta dall'indirizzo LAN di `deck` in tutti e sette i casi.

Gli hash uguali non provano che il rendering sia corretto. Gli accenti di
`o3/view/project.py` coincidono con la copia in `world.md` e restano distinti
fra loro e da `#4338ca` di `metodo`.

**Skill: niente residui.** I sei hanno il quartetto, `/cycle` e `/method`,
con i wrapper Codex speculari. `baserow` non ha `/kb`, come dalla baseline.
Le skill di dominio sono `/manutenzione` in `nixos` e
`categorizzazione`, `corrispondenze`, `ordini` e `tassonomia` in `bi`.

Fotografia delle code (`development-goal`, pesata sulla gradualità di
dominio). **La firma del telos è nuova: tutti e sei girano da soli ogni
giorno.** Dall'08/10, i giri con `Impatto-motivo: ciclo-autonomo` sono 21 in
`nixos`, 20 in `bi`, 25 in `economia` e in `salute`, 20 in `danea-auto` e 18
in `baserow`; in `metodo` sono 17.

- **nixos**: 1 dev e 6 runtime (0 e 8 il 01/10). L'unico dev è la
  ristrutturazione di `/manutenzione`, in attesa dei rami `lavoro` e
  `docker`. Due runtime sono in pausa sulla decisione del custode di separare
  il repo in casa e lavoro. `## Scadenze` dichiara il timer `ciclo-nixos`
  senza data, con rimando alla config: la falsa data aggregata
  `(quotidiano)` di settembre non c'è più.
- **bi**: 9 dev e 5 runtime (7 e 4). La coda dev cresce col lavoro su ordini
  e stato condiviso, non per abbandono: 152 commit dall'08/10. La verifica
  inventari mensile del **2026-10-31** è passata senza traccia nei commit,
  quindi l'orologio è fermo da due giorni. La semestrale della concorrenza ir
  è ancora in attesa del Mondo dal 2026-07-31, da tre mesi. È coda di
  dominio.
- **economia**: 1 dev e 20 runtime (0 e 16), in-the-loop per costituzione.
  `## Scadenze` è densa e tutta futura, con i termini di oggi e domani
  presidiati.
- **salute**: 0 dev e 4 runtime, coda stabile. Le scadenze sono appuntamenti
  datati e tutti futuri.
- **danea-auto**: 3 dev e 4 runtime. Fra i dev ci sono il lanciatore del
  ciclo su `danea2`, con riesame alla scadenza del login il 18/11, e
  l'import degli ordini fornitore da `bi`. Manca `## Scadenze`: i run
  automatizzati stanno nell'elenco del Task Scheduler in `world.md`.
- **baserow**: 0 dev e 2 runtime (1 e 3). **Il primo fronte è chiuso**:
  backup quotidiano riuscito sui due lati, controlli delle 06:00 a 0 nei
  giri del 31/10, 01/11 e 02/11 e restore provato a ottobre. Anche qui manca
  `## Scadenze`: il timer vive in `o3/systemd`. Aperti il fronte deadlock (tre
  notti su cinque) e la crescita di audit log e row history a circa 37 MB al
  giorno.

**Conteggio degli esiti per stadio, il risveglio di `p1`**
(`o2/rivalutazione-skill-per-arco.md`). La fonte è
`%(trailers:key=Esiti)` su `origin/main` dall'08/10. Totali sui sei adottanti,
come materia/vuoto:

- perceive 112/21;
- interpret 75/53;
- compare 69/57;
- plan 50/81;
- specify 58/65;
- perform 42/79.

Per repository, in giri con `Esiti:`: `economia` 32, `salute` 27, `nixos`
26, `danea-auto` 23, `baserow` 22, `bi` 21, `metodo` 21. Fra l'80 e il 95
per cento di questi giri è schedulato. Integrità: le righe `Esiti:` nel corpo
coincidono coi trailer riconosciuti, tranne `salute` `1d7fe22` (11/10), dove
`Co-Authored-By` in un paragrafo a parte lascia `Esiti:` fuori dal blocco dei
trailer. Il caso è contato una volta, e il recupero è dichiarato. È lo
stesso incidente di `baserow` `205c627`, prima della regola dell'ultimo
paragrafo unico in `/commit`.

Contro i sintomi della clausola nel filo
[skill per arco](skill-per-arco-tripartito.md):

- **nessuno stadio è vuoto in tutti i repository**: ogni stadio ha almeno un
  giro con materia in ognuno dei sei. Le serie vuote lunghe sono locali e hanno una lettura di dominio:
  `interpret` in `nixos` (11 di fila), `plan` in `bi` (16), cioè la conferma
  ripetuta con runtime sano che il canone del 29/10 chiama equilibrio, e
  `perform` in `danea-auto`, `baserow`, `salute` e `metodo` (da 13 a 18).
  Dal 29/10 il giro non esegue i task per regola, quindi un `perform=vuoto`
  nel giro schedulato è atteso e non è un indizio di invocazione superflua;
- **giri tutti vuoti**: da 0 a 5 per repository (`danea-auto` 5, `economia`
  4), senza ripetizioni a verdetto e coda fermi;
- **«ha pagato»**: nessun caso nuovo documentato come tale. In `bi`,
  `interpret` è materia in 9 giri su 20, contro lo zero di settembre: lo
  stadio è esercitato dove prima viveva solo negli script.

È materiale per il verdetto del custode, non il verdetto: la misura dice che
la tripartizione non mostra il sintomo del «troppo». Il giro schedulato
gonfia gli esiti vuoti, e un trailer non distingue un giro schedulato vuoto
da un'invocazione di sola disciplina.

**Casi della delega (5b).** In `metodo/i1/` non sono arrivati casi nuovi dal
19/10. In `danea-auto`, due catture locali sono ancora «da inoltrare»:
`i1/delega-diniego-csv-primo-giro.md` (20/10) e
`i1/delega-trailer-prossimo-secondo-giro.md` (21/10). Le loro questioni
sono già nel canone: `73717f4` ammette `Prossimo: nessuno (…)` al gate e fa
provare a `skill_tools.py audit` gli esempi delle skill. La prescrizione
`ciclo-autonomo`, chiusa il 28/10, chiede i comandi del prompt alla lettera
nei permessi e un giro senza dinieghi prima del gradino 1. Le catture sono
consumate senza bisogno di essere acquisite qui: la segnatura «acquisita da
method» tocca al prossimo giro di `danea-auto`. Campione di decisioni
ordinarie fuori dal giro schedulato, uno per adottante, letto contro il
diff:

- negli altri cinque il motivo è coerente col soggetto e coi file toccati;
  li ho letti nel log, senza aprire il diff;
- in `bi`, `15921275` corregge il gancio `deploy-client`, che aveva
  distribuito `menu.bat` ai PC da un commit su un branch. Dichiara `Impatto:
basso` su codice che gira in produzione e ha appena toccato i client, e
  arriva senza test. La correzione di tre righe è giusta. L'impatto
  dichiarato è sotto la lettura della fonte: è una domanda locale per `bi`,
  non un criterio comune.

Il campione è piccolo, e l'assenza di altri scarti non prova l'assenza di
attrito.

## Tensioni aperte

- **chiusura delle tre prescrizioni recepite da tutti nei file**
  (`esiti-per-stadio-nel-commit`, `prossimo-task-e-ipotesi-del-giro`,
  `comunicazione-fra-sessioni`): `prescrizioni.py` non le riconosce per la
  forma dei marker. Al custode la scelta fra chiudere a mano sull'evidenza
  di questo audit e lasciare che i marker si adeguino. Nel secondo caso
  resta aperta anche la domanda se lo strumento debba accettare «già
  soddisfatta»;
- la clausola di uscita delle skill per arco: il materiale è raccolto e il
  verdetto spetta al custode, nel filo;
- `nixos`: il recepimento del canone del 29/10 sul giro che pianifica e non
  esegue, al prossimo `/method` locale;
- ripetibilità: il quinto audit è arrivato con un giorno di ritardo, perché
  nessun innesco lo lancia. La cella runtime-o1 resta D;
- `baserow`, verifica nell'uso: il fronte backup è chiuso, restano deadlock e
  crescita dello storico, che sono coda di dominio.

## Limiti

- le letture su `origin` misurano ciò che è pubblicato, non ciò che è
  recepito in un checkout non ancora pushato;
- la rigenerazione e `--check` dimostrano la fedeltà delle viste ai builder
  del repo, non quella dei builder al canone: quella è materia dei `/method`
  locali;
- i `tentativi.jsonl` di `svezia` e di `danea2` non sono leggibili da `deck`:
  gli arresti prima del commit lì restano invisibili a questo audit;
- l'innesco dei giri si legge da `Impatto-motivo:`. I commit di sessione
  senza quella riga finiscono in «altro» e non sono separabili da un giro
  avviato a mano con la riga mancante.
