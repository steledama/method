---
ciclo: runtime
---

# Il bootstrap nei sette adottanti

Sintesi qualitativa del 2026-10-09 sui file di `origin` dei sette adottanti,
letti dopo `git fetch` dai clone su `deck` al recepimento di `f0c9a9b`. Il
materiale per ogni repo è `README.md`, `CLAUDE.md`, `goal.md`, `world.md` e
il nuovo `autonomy.md`. Le lunghezze sono misurate con `wc -l`; i giudizi
derivano dalla lettura, non da una soglia quantitativa. La sintesi precedente,
del 2026-08-21 su sei repo, è nella storia Git del file.

## La relazione da verificare

I quattro file formano un solo bootstrap distribuito:

- `README.md` orienta nel dominio e apre i percorsi;
- `CLAUDE.md` istruisce l'agente su azioni, vincoli e pericoli;
- `goal.md` rende il nord nell'intro e lo articola on-demand;
- `world.md` rende il territorio nell'intro e ne registra superfici e fonti.

`autonomy.md` si aggiunge come register dell'autorità: in tutti e sette è
raggiungibile da README o CLAUDE e il Goal di sviluppo vi rimanda. Il
criterio resta la **coerenza del quartetto**, non la qualità isolata di un
file (`kb/readme.md`, `kb/claude.md`).

## Fotografia per adottante

### `nixos`

README, Goal e World concordano su host, coppia production/standby e i due
goal in tensione; il terzo obiettivo, l'inferenza su `game`, è dichiarato
come capacità e non come polo. `CLAUDE.md` (157 righe) resta costituzione
operativa: rilevamento host, confini di rebuild e guardrail di reboot
giustificano la specificità. Residuo editoriale: la seconda metà del README
conserva elenco hardware, porte della presentazione e catalogo, in parte
ripetuti in World e CLAUDE.

### `bi`

Il caso di agosto si è in gran parte risolto: il README apre con «Il dominio
in breve» e l'intro di `goal.md` rende i tre risultati di business invece
del contratto del polo. Resta aperto `CLAUDE.md`, cresciuto da 340 a 417
righe: la sezione «Strumenti» (circa cento righe) dichiara di avere la
reference completa altrove ma la riporta, e «Task management» e
«Documentazione e KB» ripetono regole già nei nodi canonici. I guardrail ad
alta posta, come il push che è un rilascio, giustificano parte della
lunghezza, non l'inventario. Il marker dichiara il quartetto coerente: la
lettura nel merito lo conferma per tre file su quattro.

### `economia`

La contraddizione di agosto è sciolta: README, Goal e World nominano gli
stessi due assi ereditari, con Ilaria e Sodini. L'intro del Goal è un nord
autentico in tre paragrafi. `CLAUDE.md` (313 righe) è lungo soprattutto per
guardrail sugli invii, la privacy e la verifica dei destinatari, che devono
precedere l'atto; residuo minore il template del nodo, già in
`method/node.md`.

### `salute`

`CLAUDE.md` è sceso da 308 a 183 righe: il manuale residuo di agosto si è
ridotto a responsabilità, dati personali, intento → strumento e
convenzioni. README, Goal e World concordano sul corpo-mente vissuto e sulle
tre direzioni. `world.md` è lungo (402 righe) per le fonti, che sono il suo
contenuto on-demand.

### `crm`

Goal e World restano compatti e coerenti. Il README conserva una sezione
«Stato» con l'avanzamento corrente e il prossimo incremento, e una sezione
«Sviluppo locale» procedurale: la prima ripete ciò che vive nel plan, la
seconda compete con la bussola. Il Goal di sviluppo dichiara la delega ma
non segnali propri oltre al marker.

### `danea-auto`

Resta il caso più compresso e nitido: README su automazioni, esecuzione e
diagnosi, Goal con quattro obiettivi e segnali, World breve. `CLAUDE.md`
(201 righe) porta guardrail inderogabili su GUI, Controlp e Task Scheduler.
Il marker di `bf186fb` registra la revisione come rinviata, per effetto
della formula del prompt del recepimento selettivo; il marker precedente la
dava già soddisfatta, e la lettura lo conferma.

### `baserow`

Scritto all'adozione contro il contratto: percorsi per intenzione, Goal con
quattro obiettivi e un buco di misura dichiarato, World centrato
sull'istanza. Come `crm`, il README ha una sezione «Stato» con versione,
date e avanzamento del task di backup.

## Generalizzazione

Le quattro domande di agosto discriminano ancora:

- il dominio arriva prima della sua impalcatura metodologica?
- ogni fatto vive nel file letto nel momento in cui serve?
- le intro di Goal e World rendono i poli, non il contratto dei register?
- il quartetto concorda su identità, direzione, territorio e stato corrente?

In ottobre le prime e le terze reggono ovunque. I residui cadono sulla
seconda: inventari di strumenti in `CLAUDE.md` (`bi`) e stato corrente nel
README (`crm`, `baserow`). Quest'ultimo è lo stesso movimento che
`goal-senza-fotografia` ha tolto dal Goal, spostato nella bussola: è un
segnale aperto in `i1/stato-nel-readme.md`. L'ultimo miglio resta
dell'adottante.
