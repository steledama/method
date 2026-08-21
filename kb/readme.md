---
stato: bozza
---

# README

README.md è la **bussola** dell'artefatto e il bootstrap principale del progetto. Risponde alla domanda: dove sono e da dove parto? Deve permettere a un umano o a un LLM di capire rapidamente scopo, dominio in breve, obiettivi e principi (in sintesi) e di raggiungere il resto del cruscotto — modello, piano, catalogo, strumenti — senza leggere l'intero repository.

README.md ha una doppia audience. Per l'umano è la porta d'ingresso leggibile; per l'LLM è il primo compressore del contesto. Per questo deve essere sintetico ma semantico: non solo elenco di file, ma orientamento al dominio e puntatori al cruscotto.

Il dominio ha il primato editoriale. Dopo l'identità, il primo contenuto
sostanziale di un README adottante è il **dominio in breve**: di quale Mondo si
occupa l'artefatto, quali poste o tensioni lo rendono rilevante e attraverso
quali percorsi il lettore può entrarvi. La struttura del metodo serve a navigare
quel dominio e non deve diventare il soggetto principale del README.

## La regola: orienta e punta, non immagazzina

Il README **orienta e punta, non immagazzina**. È il signifier d'ingresso: dice cosa c'è e dove sta, non lo contiene.

- **contiene**: l'identità e lo scopo in sintesi, i principi guida in sintesi, e l'orientamento operativo — _dove_ vivono modello, lavoro, catalogo, strumenti, output, fonti, ragioni — così che umano e LLM abbiano la visione d'insieme e sappiano dove trovare viste di portata minore o info puntuali
- **non contiene**: il modello del dominio, il catalogo dei nodi, i principi _estesi_, l'articolazione dei poli, procedure/flag/troubleshooting, la teoria del metodo. Tutto questo vive nei nodi `kb/` (es. `design-principles`), nei register dei poli (`goal.md`, `world.md`), nel catalogo `kb/kb.md` e in `i2/`: il README ci _punta_
- principi guida ed obiettivi, quando diventano estesi, sono un **nodo** `kb/` o il register `goal.md`: il README li sintetizza e rimanda

Conseguenza: la bussola è il README, e i **poli non vi abitano** — il nord articolato vive nel register `goal.md`, il territorio nel register `world.md` (porte on-demand); il modello del dominio vive nei nodi e in `i2/`. Il README conserva l'identità in una riga: chi entra capisce perché il repo esiste senza aprire nulla, e apre i register per l'articolazione.

Il README deve descrivere il dominio abbastanza da renderne visibili identità,
assi, poste e percorsi. Quando comincia invece a incorporarne il modello
dettagliato, le fonti o il catalogo completo, quel contenuto va spostato nei
nodi, nei register o in `i2/`. Anche la teoria del metodo resta nei nodi
canonici: il README torna a essere un router. È il primo livello della
tripartizione **README orienta · CLAUDE istruisce · KB approfondisce**,
dettagliata in `kb-tools`.

## Due mappe, una priorità

Il README può offrire due mappe, che non vanno confuse:

- la **mappa semantica** mostra regioni, entità, poste e percorsi del dominio;
- la **mappa strutturale** mostra dove vivono i componenti dell'artefatto.

La prima ha priorità editoriale. La seconda resta compressa alle porte utili
per orientarsi: KB, cruscotto, register, collezioni, presentazione e regole
operative. La disciplina dell'atrio richiede che ogni voce root appartenga a
una classe dichiarata, non che ogni dotfile, cache o eccezione di toolchain sia
spiegata nel bootstrap. L'inventario completo deve essere verificabile, ma può
vivere in un report deterministico o in una reference operativa on-demand.

## Funzioni

- descrivere nome, dominio e scopo del progetto
- dichiarare in sintesi i principi, puntando ai nodi quando sono estesi (es. `design-principles`), e puntare ai register dei poli (`goal.md`, `world.md`) per obiettivi e territorio
- puntare a `o1/plan.md` per i task aperti e le priorità correnti
- puntare al modello del dominio dove vive: nodi `kb/` e `i2/`
- puntare al catalogo dei nodi `kb/kb.md`, senza incorporarlo
- elencare molto brevemente gli strumenti disponibili, rimandando a CLAUDE per l'uso operativo e ai nodi per il dettaglio
- distinguere metodo portabile e specificità locali

Una sequenza editoriale consigliata, non un template rigido, è:

1. identità e scopo;
2. dominio in breve;
3. percorsi per intenzione;
4. stato e cruscotto;
5. sezione Metodo canonica;
6. struttura essenziale;
7. eventuali cautele di dominio, responsabilità o privacy.

Nei progetti adottanti, il README deve dichiarare il metodo condiviso come dipendenza trans-repo quando i nodi metodologici arrivano via symlink (`method/ -> ../method/kb`). Non deve indicizzare quei nodi uno per uno come se fossero conoscenza locale del dominio: il lettore deve capire cosa appartiene al metodo portabile e cosa al progetto.

## La sezione README canonica

C'è una porzione del README **comune ai sette repo** — i sei adottanti e `metodo` stesso: la sezione **`## Metodo`**, che dichiara l'adozione. È il veicolo concreto del principio «dichiara e taci» (`method-development`): l'adottante dichiara qui, una volta, la dipendenza generale dal metodo, così che altrove resti libero di collegare solo ciò da cui dipende davvero. Contiene una o due frasi che nominano il metodo come insieme con brevissima descrizione, il symlink `method/` in root come membrana verso i nodi canonici, l'hub `cognitive-artifact-design.md` come unico nome di nodo assunto stabile, e i puntatori ai due register dei poli. Niente inventari di path interni.

Questo **supera** i vecchi sottoheading `### Goal` e `### World`: i poli non vivono più nel README ma nei register `goal.md` e `world.md` (cfr. `goal`, `world`), e la home ricava i poli **dall'intro dei register** (dall'H1 al primo H2), non più dal README. Il contratto di resa resta quello ratificato: il **builder è stupido e fedele** — l'intro è reso come markdown fedele → HTML, una bullet list resta bullet list, la prosa resta prosa, niente card né euristiche per repo; la libertà di forma è dell'adottante. E resta il vincolo di contenuto: l'intro del register è la **visione del polo che l'artefatto tiene**, non la membrana né la pipeline (superfici fisiche, strati, indici) — quelle vivono nelle sezioni on-demand del register o nei nodi; se finiscono nell'intro, la home le amplifica.

Due vincoli sulla sezione:

- la sezione **dichiara, non immagazzina**: resta dentro la regola «orienta e punta» — l'adozione e i puntatori, non il modello del dominio;
- è il **solo luogo** della dipendenza generale: gli altri link al metodo nel README sono ammessi solo se intenzionali (semantici o operativi), come ovunque.

## Criteri di revisione

Una review qualitativa del README deve chiedere:

- dopo i primi due minuti è chiaro quale Mondo rappresenta il repository?
- sono visibili gli obiettivi o le poste che rendono rilevante quel Mondo?
- i percorsi di approfondimento sono espressi nel linguaggio del dominio, non
  soltanto in quello del metodo?
- inventari, comandi e teoria estesa stanno sottraendo spazio alla funzione di
  bussola?

La lunghezza non è un criterio autonomo: un dominio ricco può richiedere più
orientamento. È il rapporto fra segnale semantico e dettaglio immagazzinato a
determinare se il README resta una bussola.

## Evidenza dagli adottanti

Le fotografie dei README reali non vivono in questo nodo: cambiano alla
velocità dei progetti e diventerebbero una seconda fonte stale dentro il
canone. La comparazione periodica vive nell'osservatorio, in particolare nella
sintesi `i2/bootstrap-adottanti.md` e nel filo
`i3/bootstrap-adottanti.md`.

L'evidenza dei sei adottanti chiarisce due invarianti. Il README non ha una
lunghezza unica: conta il rapporto fra segnale semantico e dettaglio
immagazzinato. Inoltre non si revisiona da solo: forma con `CLAUDE.md`,
`goal.md` e `world.md` un bootstrap distribuito, la cui coerenza va verificata
insieme. La ricetta operativa è la prescrizione
`o3/revisione-bootstrap-adottante.md`.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [index](index.md)
- [plan](plan.md)
- [claude](claude.md)
- [project-structure](project-structure.md)
- [kb-tools](kb-tools.md)
- [method-development](method-development.md)
- [goal](goal.md)
- [world](world.md)
- [design-principles](design-principles.md)
