---
stato: bozza
---

# README

README.md è la **bussola** dell'artefatto e il bootstrap principale del progetto. Risponde alla domanda: dove sono e da dove parto? Deve permettere a un umano o a un LLM di capire rapidamente scopo, dominio in breve, obiettivi e principi (in sintesi) e di raggiungere il resto del cruscotto — modello, piano, catalogo, strumenti — senza leggere l'intero repository.

README.md ha una doppia audience. Per l'umano è la porta d'ingresso leggibile; per l'LLM è il primo compressore del contesto. Per questo deve essere sintetico ma semantico: non solo elenco di file, ma orientamento al dominio e puntatori al cruscotto.

## La regola: orienta e punta, non immagazzina

Il README **orienta e punta, non immagazzina**. È il signifier d'ingresso: dice cosa c'è e dove sta, non lo contiene.

- **contiene**: sintesi del dominio e dello scopo, obiettivi, principi guida in sintesi, e l'orientamento operativo — _dove_ vivono modello, lavoro, catalogo, strumenti, output, fonti, ragioni — così che umano e LLM abbiano la visione d'insieme e sappiano dove trovare viste di portata minore o info puntuali
- **non contiene**: il modello del dominio, il catalogo dei nodi, i principi _estesi_, procedure/flag/troubleshooting, la teoria del metodo. Tutto questo vive nei nodi `kb/` (es. `design-principles`), nei register (`kb/kb.md`, `map.md`) e in `i2/`: il README ci _punta_
- principi guida ed obiettivi, quando diventano estesi, sono un **nodo** `kb/`: il README li sintetizza e rimanda

Conseguenza: **non esiste un `map.md` separato come "modello in root"** — la bussola è il README. Il modello del dominio vive nei nodi e in `i2/`; dove il dominio ha un territorio da indicizzare, un register `map.md` lo mappa sui nodi (porta on-demand), ma è l'indice del territorio, non la bussola.

Quando il README inizia a contenere spiegazioni di dominio, il catalogo completo o teoria del metodo, il contenuto va spostato nei nodi (o nel register pertinente) e il README torna a essere un router. È il primo livello della tripartizione **README orienta · CLAUDE istruisce · KB approfondisce**, dettagliata in `kb-tools`.

## Funzioni

- descrivere nome, dominio e scopo del progetto
- dichiarare in sintesi obiettivi e principi, puntando ai nodi quando sono estesi (es. `design-principles`)
- puntare a `o1/plan.md` per i task aperti e le priorità correnti
- puntare al modello del dominio dove vive: nodi `kb/` e `i2/` (e al register `map.md` dove esiste)
- puntare al catalogo dei nodi `kb/kb.md`, senza incorporarlo
- elencare molto brevemente gli strumenti disponibili, rimandando a CLAUDE per l'uso operativo e ai nodi per il dettaglio
- distinguere metodo portabile e specificità locali

Nei progetti adottanti, il README deve dichiarare il metodo condiviso come dipendenza trans-repo quando i nodi metodologici arrivano via symlink (`method/ -> ../method/kb`). Non deve indicizzare quei nodi uno per uno come se fossero conoscenza locale del dominio: il lettore deve capire cosa appartiene al metodo portabile e cosa al progetto.

## La sezione README canonica

C'è una porzione del README **comune ai cinque repo** — i quattro adottanti e `metodo` stesso: la sezione che dichiara l'adozione del metodo e i due poli del ciclo del dominio. È il veicolo concreto del principio «dichiara e taci» (`method-development`): l'adottante dichiara qui, una volta, la dipendenza generale dal metodo, così che altrove resti libero di collegare solo ciò da cui dipende davvero. La forma è fissa; il contenuto è del dominio.

La sezione ha **heading fissi e machine-readable**, perché è anche la sorgente da cui la home (task «System image visiva») ricava i poli Goal e World senza euristiche. La struttura è:

- **`## Metodo`** — la dichiarazione di adozione: una o due frasi che nominano il metodo come insieme con brevissima descrizione, il symlink `method/` in root come membrana verso i nodi canonici, e l'hub `cognitive-artifact-design.md` come unico nome di nodo assunto stabile (il punto d'aggancio per chi vuole entrare nel metodo). Niente inventari di path interni.
- **`### Goal`** — il polo superiore del ciclo del dominio: il motivo che muove l'artefatto, in sintesi (cfr. `goal`). Per `metodo`, che ha il Goal sdoppiato dev/runtime, qui sta la forma compatta che `development-goal` articola.
- **`### World`** — il polo inferiore: la **visione del Mondo che l'artefatto tiene** — di che cosa è fatto il Mondo runtime su cui agisce e da cui legge (cfr. `world` e il register `sources.md`). È testo del dominio nella forma che il dominio richiede: prosa, elenco puntato o misto, senza forma imposta. Anche quando il Mondo sembra una lista purissima, una **puntualizzazione sulla visione** — emersa sviluppando l'artefatto — sta qui. Ciò che **non** sta qui è la membrana e la pipeline (`world/`, gli strati `i1/i2/o*`, i register): sono orientamento operativo e vivono nelle sezioni pertinenti del README o nei nodi, non nel polo World — se ci finiscono, la home li amplifica. Espliciti per repo, **mai derivati per euristica** dall'organizzazione del remote — che differisce tra adottanti (es. `bi` su `tt-sviluppo`, gli altri su `steledama`) e non è una guida affidabile.

Tre vincoli sulla sezione:

- gli heading sono **letterali e stabili**: la home li parsa per nome, quindi non vanno rinominati né tradotti per repo;
- la sezione **dichiara, non immagazzina**: resta dentro la regola «orienta e punta» — Goal e World in sintesi, col rimando ai nodi, non il modello del dominio;
- è il **solo luogo** della dipendenza generale: gli altri link al metodo nel README sono ammessi solo se intenzionali (semantici o operativi), come ovunque;
- il **corpo** di `### World` — e di `### Goal` quando la home lo deriva dal README — è reso come **markdown fedele → HTML**: una bullet list resta bullet list, la prosa resta prosa. Niente card, niente resa strutturata, nessuna euristica per repo — la libertà di forma è dell'adottante, il builder resta stupido e fedele.

## Applicazione nei progetti adottanti

- **`nixos`** — situazione attuale: README sintetico e molto orientativo: host, principi, task, documentazione, router "capire il progetto in 5 minuti" e catalogo completo. Confronto con il metodo: è il caso più vicino alla funzione di bussola — orienta senza diventare manuale completo e rimanda al register-territorio `map.md`.
- **`bi`** — situazione attuale: README ampio ma funzionale: struttura, comandi, repo collegati, skill, task e indice per cluster applicativi. Confronto con il metodo: funziona come router operativo; il rischio è la crescita con la complessità del dominio — il contenuto di dettaglio va spinto nei nodi.
- **`economia`** — situazione attuale: README combina orientamento, task urgenti, pointer agli strumenti; la sezione metodo dichiara il repo trans-repo invece di indicizzare i singoli nodi. Confronto con il metodo: buon adattamento ad alta responsabilità — il bootstrap include stato e scadenze, purché conoscenza stabile e metodo restino nei luoghi canonici.
- **`salute`** — situazione attuale: README lungo e narrativo, con pointer espliciti a register-territorio, `principi-salute` e `verifica-nel-vivere`. Confronto con il metodo: efficace come ingresso umano; i pointer espliciti riducono il rischio che il README debba spiegare anche il modello.

Il confronto chiarisce che il README non deve avere una lunghezza unica. Deve però preservare la funzione di bussola: ingresso, orientamento e puntatori al cruscotto. Quando inizia a immagazzinare invece di puntare, il contenuto va spostato nei nodi (o nel register pertinente) e il README deve restare un router.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [index](index.md)
- [plan](plan.md)
- [map](map.md)
- [claude](claude.md)
- [project-structure](project-structure.md)
- [kb-tools](kb-tools.md)
- [method-development](method-development.md)
- [goal](goal.md)
- [world](world.md)
- [design-principles](design-principles.md)
