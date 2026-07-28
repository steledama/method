---
ciclo: runtime
---

# Segnale: il recepimento di un vincolo fa emergere il drift che era già lì

Data: 2026-07-29 · Fonte: `nixos`, esito del proprio `method-review`
(intervallo `6133ace..b42164c`, marker portato a `b42164c`, `aligned`).

## Il segnale

Dei tre commit dell'intervallo `nixos` ne ha recepito uno solo in modo diretto:
il contratto «derivata implica verificata» nel generatore delle viste (tabella
del plan × file `o2/`). Gli altri due erano già soddisfatti dal symlink verso
`kb/` o non pertinenti. Il recepimento non è stato un adeguamento formale:
nell'atto di applicare il contratto sono emersi due difetti **già presenti** nel
repo, che nessun controllo locale vedeva.

**Un difetto latente.** La potatura del footer `## Dettagli task` da
`o1/plan.md` aveva rimosso l'unica chiave con cui una riga risolveva al proprio
file `o2/`, e il generatore locale faceva `continue` in silenzio su ogni riga
senza sorgente. `presentation/tasks.html` era fermo al 2026-07-10 e non
conteneva il task aperto il 20 luglio: **diciannove giorni**, mentre audit,
inventory, facts, coverage, fidelity e `check.sh` restavano verdi.

**Divergenze vive.** Applicato il contratto, tre righe del plan non portavano il
titolo-identità del proprio file `o2/` (`plan`: «un solo identificatore, lo
stesso ovunque»); per una di esse l'indice `o2/tasks.md` portava una **terza**
variante. Il generatore esce con errore: senza allinearle il recepimento non
chiude.

Osservazioni:

- **è il secondo repo su due a pagare al primo contatto.** Il `method-review` di
  `bi`, lo stesso giorno, aveva trovato col medesimo port undici righe non
  risolte da tre settimane e una divergenza di titolo. Il recepimento non ha
  creato lavoro nuovo: ha reso esigibile lavoro dovuto;
- **le due classi trovate hanno età diverse.** Il difetto latente era in essere
  da diciannove giorni e non produceva alcun segnale; le divergenze di titolo
  erano nate con le righe stesse. Un vincolo che arriva in un repo con storia le
  incontra insieme, al primo giro;
- **nessuna delle due sarebbe stata trovata dal presidio previsto.**
  L'inventario delle viste è la quinta lente di `/adopters-review`, in calendario
  l'11 agosto; il canale del canone, a cadenza propria dell'adottante, è arrivato
  prima. `nixos` era uno dei due repo che quella lente doveva ancora guardare;
- **il costo del recepimento non è stato il costo della modifica.** Il commit di
  canone era piccolo; il lavoro reale è stato riparare ciò che il vincolo ha
  scoperto — generatore, plan, indice `o2/`, vista rigenerata (5 task su 5);
- **due esiti collaterali non toccano il canone**: l'adottante ha registrato come
  adattamento durevole che il motore delle viste vive in `o3/tools/` e non in
  `o3/` (conseguenza di una sua regola locale sugli strumenti dev), e la
  riesecuzione della skill sullo stesso target ha dato intervallo vuoto,
  provandone l'idempotenza.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- che un vincolo recepito paghi **retroattivamente** è canone da incidere?
  `constraint` oggi parla solo in avanti — rendere impossibile o rumorosa
  l'azione sbagliata — e tace su cosa succede quando il vincolo arriva in un
  artefatto che ha già storia;
- se il recepimento è un atto diagnostico e non solo di allineamento, l'ordine
  con cui un vincolo viene portato negli adottanti diventa una scelta (prima
  dove il drift costa di più) o resta indifferente?
- resta `economia` come unico dei quattro non esaminato su questo asse:
  aspettare il battito dell'11 agosto, o anticipare come si è fatto per la sua
  home?
