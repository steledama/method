---
ciclo: runtime
---

# Il bootstrap nei sei adottanti

Sintesi qualitativa del 2026-08-21 sui checkout correnti dei sei adottanti
dichiarati in `world.md`. Il materiale letto per ogni repo è `README.md`,
`CLAUDE.md`, `goal.md` e `world.md`; il nodo `kb/world.md` non è duplicato
localmente ed è correttamente consumato come `method/world.md` attraverso il
symlink canonico. Le lunghezze citate sono **misurate** con `wc -l` sui checkout
locali; i giudizi editoriali derivano dalla lettura dei file, non da una soglia
quantitativa.

## La relazione da verificare

I quattro file formano un solo bootstrap distribuito:

- `README.md` orienta nel dominio e apre i percorsi;
- `CLAUDE.md` istruisce l'agente su azioni, vincoli e pericoli;
- `goal.md` rende il nord nell'intro e lo articola on-demand;
- `world.md` rende il territorio nell'intro e ne registra superfici e fonti.

Una revisione del solo README può spostare, invece di risolvere, l'accumulo:
teoria, inventari e manuali rimossi dalla bussola possono riversarsi in
`CLAUDE.md`; un README domain-first può inoltre contraddire un Goal o un World
rimasti a una fotografia precedente. Il criterio è perciò la **coerenza del
quartetto**, non la qualità isolata di un file.

## Fotografia per adottante

### `nixos`

Il README apre con sistema, host e tensione production/standby; Goal e World
sono intro brevi, semantiche e coerenti. Il router «Capire il progetto in 5
minuti» è il percorso per intenzione più efficace del gruppo. La seconda metà
del README conserva però strumenti, legenda completa dell'atrio e inventario
tecnico: orientamento forte con sovraccarico strutturale. `CLAUDE.md` (144 righe
misurate) resta prevalentemente costituzione operativa; rilevamento host,
confini rebuild e guardrail giustificano la sua specificità.

### `bi`

`world.md` descrive con chiarezza sistemi vivi, relazioni commerciali e flussi.
L'intro di `goal.md`, invece, spiega che cos'è un register e come il ciclo lo
usa: rende il **contratto del polo**, non il nord commerciale, che compare solo
nelle sezioni successive. README (136 righe) e `CLAUDE.md` (340 righe) sono i
più structure-first: inventario dettagliato, comandi, strumenti e manuale di
produzione precedono o competono con i percorsi del dominio. È il caso che
richiede la revisione coordinata più ampia.

### `economia`

Il README presenta subito i due assi finanziari e la fonte operativa, ma poi
duplica la root in elenco, tabella completa e albero. L'intro di `goal.md` rende
un nord autentico e ricco, ma incorpora modello, casi, razionale e dettagli in
una porzione molto più lunga delle altre home. `CLAUDE.md` (269 righe) contiene
molta reference di strumenti. C'è inoltre una contraddizione semantica: il Goal
distingue l'asse con Ilaria e quello Sodini, mentre l'intro di World presenta
come due assi quello personale e quello con Ilaria, senza rendere il secondo
intreccio ereditario. È un giudizio di dominio da risolvere localmente, non un
testo da correggere dal canone.

### `salute`

Il commit `513b6ac` ha trasformato il README ereditato dalla genesi del metodo
in una bussola domain-first: corpo-mente vissuto, tre direzioni del Goal,
percorsi semantici e responsabilità sanitaria precedono la mappa strutturale.
Le intro di Goal e World sono coerenti con questa lettura. Il residuo maggiore
è `CLAUDE.md` (308 righe): filosofia, inventario della struttura, convenzioni
dei nodi e operazioni formano ancora un manuale esteso. La riscrittura del
README è quindi un buon pilot, non la chiusura della revisione del bootstrap.

### `crm`

Goal e World sono compatti, domain-first e coerenti; `CLAUDE.md` (105 righe)
separa bene scope, invarianti del workflow, ownership con `manager` e sicurezza.
Il README mette la struttura subito dopo l'identità e contiene una lunga
sezione di sviluppo locale, ma stato e contratti validati restano leggibili.
Serve una rifinitura editoriale, non una rifondazione.

### `danea-auto`

È il caso più compresso: il README parte da automazioni, vincoli della GUI,
esecuzione e diagnosi; Goal e World sono nitidi. `CLAUDE.md` (131 righe) è più
lungo del README perché conserva guardrail ad alta posta su credenziali, invii
non annullabili, GUI e Task Scheduler. Qui comprimere per quantità sarebbe un
errore: una regola resta nel bootstrap quando deve essere presente prima
dell'atto per impedirne uno dannoso.

## Generalizzazione

La lunghezza non discrimina. Discriminano invece quattro domande:

- il dominio arriva prima della sua impalcatura metodologica?
- ogni fatto vive nel file letto nel momento in cui serve?
- le intro di Goal e World rendono i poli, non il contratto dei register?
- il quartetto concorda su identità, direzione, territorio e stato corrente?

La comparazione appartiene all'osservatorio di `metodo`; l'ultimo miglio
appartiene all'adottante. Il canone può prescrivere criteri e indicare tensioni
da verificare, ma soltanto il repo locale può decidere quali dettagli siano
necessari al proprio dominio e applicare le modifiche tramite `/method`.
