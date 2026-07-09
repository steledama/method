---
stato: maturo
---

# Project structure

Schema che definisce l'infrastruttura operativa del progetto. La knowledge base, in senso stretto, non ha una struttura gerarchica predefinita: la sua forma emerge dalle connessioni tra i nodi. Il progetto che la ospita, invece, ha bisogno di una struttura esplicita per rendere leggibili le convenzioni, lo stato dei lavori, la memoria delle decisioni e gli strumenti di manutenzione.

La root non si decide per profondità («più in alto = più stabile», criterio demolito da pace-layering). Si decide perché sia **atrio**: il _system image_ dell'artefatto. Un `ls` della root deve mostrare l'anatomia completa — quali classi di componente esistono — senza aprire nulla. È applicazione diretta di affordance-signifier e system-image: la struttura di directory porta essa stessa il peso della comunicazione, invece di delegarlo a un documento che la spiega (il cartello «tirare» su una porta mal progettata). Il principio è a sua volta applicazione di method-development: una cornice posata dall'alto (Norman) e verificata dal basso (le root reali dei progetti adottanti).

## Il gradiente di cardinalità

La collocazione segue un razionale, non l'abitudine: il **gradiente di cardinalità** del ciclo. Il ciclo è un funnel tra due poli — il Goal è il punto di convergenza (singolare), il Mondo la molteplicità grezza ritagliata per rilevanza (cfr. `action-cycle`, `goal`, `world`). L'arco di valutazione distilla il molteplice verso l'uno, l'arco di esecuzione dispiega l'uno verso il molteplice.

Dalla ristrutturazione dell'atrio (2026-07-04) le sei collezioni-stadio portano il **codice del loro stadio** — `i1/` Perceive, `i2/` Interpret, `i3/` Compare, `o1/` Plan, `o2/` Specify, `o3/` Perform — e l'atrio non _racconta_ il ciclo: lo _è_. Il gradiente non decide più «file in root vs cartella»: decide la **popolazione interna** di ogni stanza. Vicino al Goal l'unità: in `o1/` regna un solo `plan.md`; `i3/` tiene un file per filo aperto, aggiornato in place. Verso il Mondo la molteplicità: `i1/` accumula segnali, `o2/` dettagli di task, `o3/` prescrizioni e strumenti. File-unici in cima, collezioni piene in fondo: combacia coi due poli e coi tre livelli di elaborazione (cfr. `processing-layers`).

Ogni collezione porta il suo **indice dentro la cartella**, e la coppia dei nomi si divide il lavoro: la cartella porta il _codice_ dello stadio, l'indice il suo _nome_ — `i1/perceptions.md`, `i2/interpretations.md`, `i3/verdicts.md`, `o2/tasks.md`, `o3/prescriptions.md`. In `o1/` l'indice è `plan.md` stesso (Specify è la coda del Plan: `plan.md` tiene una riga per ogni file di `o2/`). Il _significato_ dello stadio vive nell'atomo (`perceive`, `interpret`, `compare`, `plan`, `specify`, `perform`); l'indice dichiara ed elenca. Ogni item di collezione dichiara nel frontmatter la facet `ciclo: dev|runtime`, letta dal Mondo su cui insiste — artefatto → `dev`, adottanti/dominio → `runtime` (cfr. `development-meta-cycle`).

Questo **supera** la regola della «triade alta in root» (README, `plan.md`, `verdict.md` come file-ciclo di root): Plan e Compare restano la quota alta del ciclo — un'unica istanza corrente, aggiornata in place — ma vivono nella propria stanza (`o1/plan.md`, i fili di `i3/`). La root non ospita più _istanze_ di stadio: ospita gli stadi. In root restano la bussola e le regole (README, CLAUDE, AGENTS), che non sono stadi ma l'ingresso e la costituzione, e i register dei due poli (`goal.md`, `world.md`), che non sono stadi ma i confini del ciclo.

## Le specie di file root

Sciolta la collocazione, la root contiene due specie di file, distinte per
**funzione** non per profondità. Nessuna ospita artefatti del **runtime del
dominio**: quelli si collocano per stadio nelle collezioni (vedi «Collocazione
per funzione», sotto). Nei repo di dominio a queste due specie si aggiunge la
disciplina dell'inventario: contenuti versionati ricollocati nello stadio
funzionale previsto, eccezioni di toolchain e traffico runtime dichiarati (vedi
«L'inventario dell'atrio», sotto).

**1. Bussola e regole** — letti a _ogni_ sessione per capire e agire:

- `README.md` — la **bussola**: identità, principi e dominio in sintesi; orienta e _punta_ a `o1/plan.md`, `kb/kb.md`, al modello (nodi/`i2/`) e ai register dei poli
- `CLAUDE.md` + `AGENTS.md` — le regole d'azione (AGENTS come wrapper agent-agnostico)

Il **cruscotto** — `o1/plan.md` (i task aperti prioritizzati, con dipendenze, ciclo e i vincoli che ne ordinano l'esecuzione, le `scadenze` del dominio in una sezione propria) e i fili di `i3/` — si legge anch'esso a ogni sessione, ma vive nelle stanze del ciclo, non in root.

**2. Register** — porte verso ciò che sta _fuori_ dall'artefatto, non verso una collezione interna; visibili nell'atrio e letti on-demand. I register sono **i due poli del ciclo**: come le sei stanze materializzano gli stadi, i due register materializzano i confini che il ciclo non controlla — l'atrio non _racconta_ il ciclo, lo _è_, poli compresi:

- `goal.md` — il polo superiore: il nord del dominio, gli obiettivi declinati con i segnali che li misurano e il lavoro corrente che li serve; custode umano dichiarato (forma e disciplina in `goal`)
- `world.md` — il polo inferiore: il territorio che l'artefatto ritiene rilevante — superfici della membrana, entità, sistemi e attori legati ai nodi, provenienza delle fonti-mondo autorevoli (forma in `world`)

I due register condividono il contratto machine-readable: l'intro (H1 → primo H2) è il polo in sintesi, resa fedelmente dalla home; le sezioni sono la profondità. Questo **supera** la vecchia coppia `map.md`/`sources.md`: l'indice-di-dominio e il registro di provenienza erano entrambi indici del Mondo e confluiscono in `world.md` (la dimensione interna di `map` — «dove vivono o1, o2, o3» — è superata dall'atrio, che si auto-dichiara); il polo Goal, che prima viveva in una sezione del README, guadagna la porta simmetrica.

I cataloghi non salgono più in root. `kb.md` è l'indice interno omonimo di `kb/` (`kb/kb.md`): la KB resta il **nucleo di conoscenza formalizzata** del system image, trasversale agli stadi (cfr. `system-image`, `knowledge-base`), ma la trasversalità non richiede la root — l'atrio mostra la porta `kb/`, l'ordine di bootstrap dice quando aprirla. `tools.md` è **soppresso**: gli strumenti sono gli **esecutori deterministici** del ciclo di sviluppo e hanno nel Perform il loro stadio — vivono in `o3/`, registrati nella sezione «Strumenti» dell'indice `prescriptions.md` (prescrizioni eseguibili accanto a quelle narrative; l'omologo runtime nei repo code-based sono gli `scripts/` di dominio). Questo **supera** la specie «cataloghi trasversali in root». Anche la vecchia «collisione» tra catalogo e nodo-concetto `kb/index.md` si è sciolta da sé: il catalogo è `kb/kb.md`, omonimo della collezione, e `index` ne documenta la funzione.

**Strato di presentazione** — `presentation/` raccoglie l'infrastruttura derivata, non nuove sorgenti: `index.html` (la home statica della system image), `assets/` (token grafici, primitivi e adattatori CSS condivisi) e le viste HTML generate e versionate, apribili via `file://`, che leggono le sorgenti del ciclo (`README.md`, `i2/`, `o1/plan.md`, `o2/`, `i3/`) senza sostituirle. La disciplina vive nel nodo `view`: vista derivata, mai seconda fonte.

## Visibilità ≠ caricamento

«Visibile nell'atrio» non significa «letto al bootstrap». Bussola, regole e cruscotto si leggono ogni sessione; catalogo, register e collezioni si _vedono_ sempre (un nome nell'`ls`) ma si _aprono_ solo quando servono. Il signifier che dice _cosa_ leggere e _quando_ è l'ordine di bootstrap dichiarato in `CLAUDE`/`AGENTS`, non la posizione del file. Questa scissione è ciò che permette all'atrio di essere completo senza gonfiare il contesto: l'esistenza di `kb/` è informazione gratuita, la lettura di `kb/kb.md` è un costo che si paga solo on-demand.

Questo **supera**, in due tempi, la vecchia regola «un file-meta vive dentro la cartella se on-demand, sale in root solo se letto a ogni sessione»: prima ammettendo cataloghi trasversali on-demand in root (`kb.md`, `tools.md`), poi — con la ristrutturazione dell'atrio — riportando anche quelli dentro le collezioni. La posizione non codifica mai il caricamento: lo codifica il bootstrap. Perfino il cruscotto (`o1/plan.md`, `i3/`), letto sempre, vive in cartella.

Questo **supera** anche la regola del 2026-06-06 «`map` resta in root come file-ciclo, distinto dal README per pace». Quella regola trattava "map" come una cosa sola — il modello che evolve. La scomposizione lo scioglie meglio: la **bussola** (orientamento d'ingresso, stabile) è il README; il **modello** (la teoria che evolve) vive nei nodi e in `i2/`; l'**indice del territorio** è il register del polo World (`world.md`, porta on-demand). Così lo strato veloce resta fuori dal README — la pace è rispettata meglio del compromesso del 06-06. Il README **orienta e punta, non immagazzina** (regola in readme).

## Collocazione per funzione, non estensione della root

Il set universale (bussola e regole + register + le sei stanze) è un _pavimento, non un soffitto_, ma un dominio **non** si estende aggiungendo file in root: si estende con ciò che mette nelle collezioni. Gli artefatti del **runtime del dominio** si collocano per stadio cognitivo, distinti da quelli di sviluppo dalla facet `ciclo: runtime`:

- cattura cronologica valenza-neutra (`diario`) → `i1/`, tenuta neutra: l'interpretazione valenzata risale a `stato`, non scinde il file;
- sintesi corrente (`stato`) → `i2/`, come i2 _testuale_ accanto alle view generate; le due forme dell'i2 convivono (cfr. input, «la forma segue il dominio»). Non si fonde nella view — perderebbe leggibilità — ma le sta accanto;
- prescrizione o promemoria predisposto → `o3/`;
- vincolo di pianificazione (`scadenze`: le date che ordinano i task) → una sezione di `o1/plan.md`. È parte del **Plan**, non un artefatto i/o: determina l'ordine d'esecuzione, quindi vive col cruscotto, non tra gli item.

Questo **supera** la regola «root estensibile dal basso» (2026-06-07, che nominava `stato`/`diario`/`scadenze` come file root): contraddiceva il principio «il cruscotto è il ciclo di sviluppo, non il runtime». La sua giustificazione era «letti a ogni sessione», ma **posizione ≠ bootstrap**: l'ordine di bootstrap in `CLAUDE` può puntare a `i2/stato.md` come prima lettura senza che il file viva in root. L'ergonomia è salva; con la facet `ciclo:` runtime e dev convivono nelle stesse stanze senza mescolarsi.

## L'inventario dell'atrio: collocazione, eccezioni, verdetto di fit

Nei repo code-based il corpo di dominio è la superficie del Mondo di sviluppo
che vive dentro il repo: i sorgenti su cui il commit agisce e da cui build e
deploy percepiscono la risposta (cfr. `world`: per `metodo` quel Mondo coincide
con l'ala `kb/`; per un adottante code-based sono moduli, host, client, script,
dichiarazioni). Il corpo di dominio non è un'eccezione al metodo e non ottiene
una dispensa dalla struttura: aderire al metodo significa collocarlo negli
spazi versionati previsti secondo la funzione che svolge. Se prepara o compie
l'atto sul Mondo, vive in `o3/` come o3-runtime; se cattura segnali vive in
`i1/`; se sintetizza vive in `i2/`; se specifica lavoro futuro vive in `o2/`.
La root mostra le porte dell'atrio, non conserva il dominio per inerzia.

La disciplina è l'**inventario**: ogni voce dell'`ls` della root appartiene a una classe dichiarata —

- bussola e regole (README, CLAUDE, AGENTS);
- collezioni-stadio (`i1/`–`o3/`) e ali (`kb/`, `presentation/`);
- register dei poli (`goal.md`, `world.md`);
- contenuto versionato ricollocato nello stadio funzionale previsto;
- **eccezioni di toolchain** — file che lo strumento inchioda alla root (`flake.nix`/`flake.lock`, `package.json`, dotfile): vincoli, non scelte; dichiarate una volta;
- **traffico runtime** — cache, log, output intermedi: membrana `world/` o gitignore, mai voci versionate senza classe.

Ciò che non si lascia collocare si conta come eccezione, e il conteggio è il
**verdetto di fit** del metodo sul dominio: poche eccezioni motivate = il
metodo si applica e il dominio caratterizza la struttura; molte eccezioni o
voci inclassificabili = il metodo lì non si applica adeguatamente. Prenderne
atto è un esito legittimo: la negazione onesta della tesi è un verdetto, il
non-averci-provato no. Il verdetto risale all'osservatorio con l'esito del
`method-review`.

## L'i1 e l'o3 di `method`: il canale con gli adottanti

`method` è un meta-artefatto e materializza anch'esso i due riflessi che baciano la membrana `world`, dove il Mondo runtime sono gli adottanti (cfr. `world`, `input`, `output`).

- **i1 → `i1/`** — il segnale metodologico che un adottante solleva mentre risolve un problema concreto («nel repo X la regola Z è scomoda»). Si cattura qui, **valenza-neutro**: il confine i1→i2 è l'ingresso della valenza, quindi la valutazione (generalizza? come?) è i2→i3 e avviene in `method` (fili di `i3/`, nodi), non nel repo che segnala. Un adottante perciò **non pianifica** un cambio di canone nel proprio `plan.md` — non è suo lavoro, non può sequenziarlo né dargli dipendenze: emette il segnale. Pianificare il canone è di `method`.
- **o3 → `o3/`** — il runbook di adozione di un cambio di canone, preparato per repo ed eseguito dal `method-review` dell'adottante: o3 prescrive, method-review compie l'atto. È la forma concreta della propagazione.

Così `method` ha l'atrio completo del ciclo (i1/i2/i3 e o2/o3) e fa da modello agli adottanti dogfoodando anche il proprio arco di input/output, non solo la KB.

## Il cruscotto è il ciclo di sviluppo, non simmetrico a sette caselle

Il cruscotto agisce sull'artefatto, non sul mondo del dominio. Per questo `plan` è **o1-sviluppo**: il Plan del ciclo di sviluppo (che agisce sull'artefatto), distinto da **o1-runtime** (il Plan del runtime in action-cycle, che agisce sul mondo). Non è la negazione dell'omologia Plan=o1 — `action-cycle` mappa Plan=o1 — ma il suo **qualificatore di ciclo**: stesso stadio, runtime o meta-ciclo di sviluppo, distinti dalla facet `ciclo:`. `plan` resta `plan.md` e non diventa `tasks.md` perché il suo nome è lo **stadio** (Plan, la quota alta), non la cartella che indicizza; è l'altezza nel ciclo a farne il file unico che regna in `o1/` mentre `o2/` accumula (cfr. «Il gradiente di cardinalità»).

Il cruscotto ha due lati. Il lato esecuzione sono _intenzioni scritte_ — il Goal in root (`README`), il Plan nella sua stanza (`o1/plan.md`). Il lato valutazione sono _operazioni_ — l'audit, la cognitive-fidelity — il cui residuo rientra nei fili di `i3/` e nei nodi. Il Compare deposita lì il suo esito come **sostantivo** (il verdetto, un file per filo aperto), non come log di atti; quando si cristallizza in view generata (`presentation/verdict.html`) è o2/i2-macro — vista derivata, non intenzione.

## Le regole d'azione e la memoria

`CLAUDE.md`, con `AGENTS.md` come wrapper agent-agnostico, è la "costituzione operativa": contiene cosa è consentito eseguire, vincoli operativi, bootstrap di sessione, pointer alla KB. È distinta dal contenuto di dominio che vive nei nodi `kb/`: ogni descrizione di come funziona qualcosa appartiene a un nodo, CLAUDE.md ne è solo l'indirizzo. AGENTS.md non duplica le regole: indirizza ogni agente verso README e CLAUDE esplicitando l'ordine di lettura.

I fili di `i3/` sono il verdetto attuale, per filo/area aperta — non un log. Il git log dice cosa è cambiato; il filo dice come stanno le cose ora e perché conta, aggiornato in place; la cronologia di un filo è il git history del suo file. È lo strato interpretativo sopra quello analitico del git log.

## Skill base

`kb-review`, `plan-review`, `verdicts-review` e `commit`. `kb-review` è l'health check periodico: link rotti, nodi orfani, connessioni tra cluster, naming, escludendo il catalogo `kb/kb.md` dal conteggio dei nodi. `plan-review` e `verdicts-review` sono la coppia simmetrica di supervisione — una per braccio del ciclo, col register `goal.md` come cerniera: la prima tiene onesto il piano (coerenza `o1/plan.md`↔`o2/`, priorità, dipendenze, lente task→obiettivo), la seconda tiene onesto il confronto (i fili `i3/` contro i segnali reali, copertura obiettivo→filo, bonifica del plan dalla narrativa di stato). `commit` è il gate di filing back. Le skill sono versionate nel progetto, non globali, perché ogni KB ha check, fonti e segnali locali diversi; quando possibile delegano la parte meccanica agli esecutori in `o3/`, così parsing e conteggi restano deterministici.

`method-review` completa questa base sul confine tra repository: legge i commit
del metodo successivi al marker versionato dell'adottante, classifica ciò che è
diretto, adattato, non pertinente o già soddisfatto e lascia l'eventuale lavoro
futuro in `o1/plan.md`/`o2/` locale. Non sostituisce la triade: controlla la
relazione adottante-metodo, non la salute o la coda interna del progetto.

## Struttura uniforme, carattere nel contenuto

I nomi delle collezioni standard sono **uniformi** tra i progetti (le sei stanze `i1/`–`o3/` coi loro indici, `kb/`, `presentation/`): la familiarità della cornice rende l'artefatto leggibile e confortante a chi passa da un repo all'altro, umano o LLM. Il «colore» del dominio non vive nel nome della cartella ma nel **contenuto** dei file. Questo **supera** il vecchio principio «il nome dello strato output è una scelta di dominio»: un nome di dominio che contraddice il contenuto è un signifier che mente (es. `quadro/` in `salute`, che evoca il quadro _clinico_ in una KB che rifiuta la separazione corpo/mente). La guardia che il vecchio principio proteggeva — non forzare la struttura sul dominio — resta valida solo come divieto di nomi fuorvianti, non come licenza di nomi idiosincratici.

Resta distinto ciò che non è una collezione di sintesi-documento ma output di
altra natura ontologica: la configurazione che gira in `nixos` è o3-runtime,
non la porta `interpretations/`. L'uniformità riguarda le collezioni standard
dell'artefatto e vincola la collocazione funzionale; non costringe a
ribattezzare il contenuto di dominio oltre le sottocartelle necessarie dentro
lo stadio corretto.

Anche `world/` ha nome uniforme, ma non è una collezione dell'artefatto. È un
symlink host-local verso la cartella di progetto non versionata, tipicamente su
Drive: la membrana fisica attraversata da atti e segnali grezzi, sempre
gitignorata e senza manifest. La porta versionata del polo è il register
`world.md`, che dichiara le superfici della membrana senza versionarne il
contenuto. Nel repo `method`, `world/` contiene symlink ai repository adottanti
e le fonti autorevoli, e materializza il suo Mondo runtime senza versionarne i
path.

## Caratteristiche

- root come atrio: l'`ls` dichiara l'inventario completo dei componenti; bussola, regole e cruscotto si leggono, catalogo, register e collezioni si aprono on-demand
- README a doppia audience: umano e LLM condividono l'interesse per una struttura semantica chiara
- la collocazione segue la funzione e il gradiente di cardinalità interno alle stanze, non la profondità
- `kb/kb.md` è l'indice interno della KB; `o3/` contiene gli esecutori deterministici
- `o2/` come spazio operativo: dettagli dei task aperti (stadio Specify), non conoscenza permanente; `o1/plan.md` ne è l'indice — ogni file ha una riga, ogni riga ha un file
- `.claude/skills` come interfaccia operativa; `.codex/skills` come wrapper opzionale

## Skeleton directory

- bussola e regole: `README.md` · `CLAUDE.md` · `AGENTS.md`
- collezioni-stadio: `i1/` · `i2/` · `i3/` · `o1/` · `o2/` · `o3/`
- indici di collezione, dentro la cartella: `i1/perceptions.md` · `i2/interpretations.md` · `i3/verdicts.md` · `o1/plan.md` · `o2/tasks.md` · `o3/prescriptions.md`
- ali trasversali: `kb/` con catalogo `kb/kb.md`; `presentation/` con `index.html`, viste generate e `assets/`
- register dei poli (verso i confini del ciclo, non collezioni dell'artefatto): `goal.md` (il nord) · `world.md` (territorio, superfici della membrana, fonti autorevoli)
- membrana locale: `world/`, symlink gitignorato alla cartella di progetto non
  versionata, senza manifest
- workspace locale opzionale: `data/`, ignorato da Git, per fonti, dati
  compilati e intermedi che non appartengono alla storia dell'artefatto
- `.claude/skills/` · `.codex/skills/`

## Naming dei file

- file UPPERCASE — riconosciuti e caricati per nome da tool o LLM: `README.md`, `CLAUDE.md`, `AGENTS.md` (solo `CLAUDE.md` è auto-caricato dall'harness Claude Code; gli altri seguono l'ordine di bootstrap)
- cartelle-stadio con codice del ciclo (`i1/`-`o3/`); indici con nome leggibile dello stadio (`perceptions.md`, `interpretations.md`, `verdicts.md`, `plan.md`, `tasks.md`, `prescriptions.md`)
- catalogo KB dentro la collezione (`kb/kb.md`), omonimo alla cartella
- register lowercase in root (`goal.md`, `world.md`): stesso stile, ma puntano _fuori_ dall'artefatto (i due poli del ciclo), non a una collezione interna; singolare come i poli che nominano
- forma inglese per filename, H1 e artefatti strutturali vivi (`map`, `plan`, `verdicts`, `kb`); prosa italiana per la documentazione concettuale
- nodi `kb/` — lowercase inglese con trattini, singolare come forma canonica (regola dettagliata in node)

## Frontmatter per tipo di file

- `kb/*.md`: frontmatter obbligatorio `stato`, secondo il nodo node
- item di collezione-stadio: frontmatter obbligatorio `ciclo: dev|runtime`
- task in `o2/`: frontmatter obbligatorio `sintesi` + `ciclo: dev|runtime`, secondo il nodo tasks (il campo `stato:` è soppresso dal canone 2026-07-04)
- bussola/regole (`README.md`, `CLAUDE.md`, `AGENTS.md`), register (`goal.md`, `world.md`) e indici ordinari di collezione (`i1/perceptions.md`, `kb/kb.md`, …): nessun frontmatter; `o1/plan.md` fa eccezione perché è anche l'istanza corrente del Plan

La ragione è funzionale. I nodi, i task e gli item di collezione sono unità analizzabili dagli strumenti; bussola, regole, register e indici di collezione sono ingressi operativi o cataloghi leggibili direttamente. Aggiungere frontmatter lì crea metadati editoriali difficili da mantenere e senza funzione metodologica stabile.

## Bootstrap di sessione

- `README.md` è il primo file letto: la bussola — orientamento, principi in sintesi, puntatori al cruscotto
- `CLAUDE.md` è già in contesto: contiene i vincoli operativi, non i contenuti di dominio
- il cruscotto `o1/plan.md` e i fili pertinenti in `i3/` si leggono a inizio lavoro; catalogo, register e collezioni si aprono quando servono
- il nodo tematico pertinente viene letto prima della modifica richiesta
- l'ordine esplicito (`README → CLAUDE → nodo`) abbassa il costo di ricostruzione del dominio in ogni nuova sessione LLM

## Regole dettagliate per componente

Questo nodo tiene l'overview; le regole proprie e i criteri di revisione di ciascun componente vivono nel nodo dedicato.

- README: funzione, doppia audience e sezioni tipiche in readme; il catalogo dei nodi sta in `kb/kb.md`, nodo-concetto indice
- register dei poli: forma e disciplina di `goal.md` in goal, di `world.md` in world; supervisione del lavoro in plan
- CLAUDE e AGENTS: regole d'azione, bootstrap esplicito, confini con il dominio in claude e agents
- o2/: corrispondenza uno a uno `plan` ↔ file, frontmatter e ciclo di vita del task in tasks
- i3/: formato canonico dei fili e distinzione da diario/stato in verdict

## Applicazione nei progetti adottanti

Lo stato sotto fotografa i progetti _prima_ della migrazione all'atrio: ognuno
la recepisce con un task locale (catalogo→`kb/kb.md`; collezioni-stadio
`i1/`–`o3/` coi loro indici: cattura cronologica→`i1/`, sintesi-documento→`i2/`,
verdetto a fili→`i3/`, `plan`→`o1/plan.md`, dettagli task→`o2/`, strumenti di
sviluppo e corpo performativo→`o3/`, viste→`presentation/`; `scadenze`→sezione
di `o1/plan.md`), letto dal canone via symlink. Il cuore della migrazione è
l'**inventario dell'atrio** (sezione sopra): decidere voce per voce dove vive il
contenuto di dominio, spostarlo nello spazio funzionale previsto e dichiarare
le eccezioni residue. La prescrizione di propagazione è attiva
(`o3/ristrutturazione-atrio.md`, pilot `nixos`); il recepimento è tracciato in
`o2/propagazione-atrio-adottanti.md`.

- **`nixos`** — situazione attuale: pilot recepito fino in fondo: il corpo
  dichiarativo versionato (`home/`, `hosts/`, `modules/`, `identity/`,
  `patches/`, `scripts/`) è stato spostato in `o3/` come o3-runtime; in root
  restano solo atrio, register ed eccezioni di toolchain. Confronto con il
  metodo: è il riferimento operativo per un progetto code-based — pochi
  componenti locali, fonti dichiarative forti e strumenti anti-drift maturi.
- **`bi`** — situazione attuale: struttura completa e ricca: README, CLAUDE, AGENTS, `verdict`, `tasks/`, `scripts/`, skill, presentazione, client e mappa. Confronto con il metodo: il metodo è adottato, ma la complessità operativa ha fatto crescere `CLAUDE.md` oltre la sua funzione costituzionale.
- **`economia`** — situazione attuale: atrio recepito per intero (`a0538f5`,
  2026-07-05): strumenti, script, libreria, config e test in `o3/`, viste in
  `presentation/`, i3 a file-per-filo, legenda dell'atrio estesa all'`ls -A`,
  verdetto di fit 0 eccezioni; membrana `world` verso i dati non versionati.
  Confronto con il metodo: secondo giro del pilot — i suoi quattro cocci
  (file-per-filo, indice unico, dotfile in legenda, chiusura col commit) sono
  incisi nel runbook; conferma la separazione tra stato operativo e risultato
  editoriale.
- **`salute`** — situazione attuale: atrio recepito per intero (`9f997c8`,
  2026-07-06): collezioni-stadio coi loro indici, `diario`→`i1/`, verdetto
  scisso a file-per-filo, catalogo `kb/kb.md` con 197 nodi tutti indicizzati,
  `tools.md` soppresso in `prescriptions.md`, legenda dell'atrio su `ls -A`,
  verdetto di fit 0 eccezioni; sette divergenze intenzionali registrate (KB
  runtime-heavy, diario valenzato, assenza di `sources.md`). Confronto con il
  metodo: è il caso doc-based/riflessivo, e il suo coccio — il link checker
  che contava rotti i cross-link validi al canone via symlink — ha corretto
  `kb_tools.py` per tutti.

La struttura replicabile non coincide con un albero identico. Coincide con la presenza esplicita delle funzioni dell'atrio: ingresso/bussola (README), piano, regole operative, memoria, più le porte verso la collezione dei nodi, l'indice-di-dominio (dove esiste), gli strumenti, le interpretazioni e le fonti. I file locali sono sani quando dichiarano una funzione distinta; diventano drift quando duplicano README, CLAUDE, verdict o nodi.

Gli strumenti vanno esposti su tre livelli — README orienta, CLAUDE istruisce, nodi approfondiscono — secondo la regola dettagliata in kb-tools.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [karpathy-pattern](karpathy-pattern.md)
- [node](node.md)
- [zettelkasten](zettelkasten.md)
- [pace-layering](pace-layering.md)
- [method-development](method-development.md)
- [affordance-signifier](affordance-signifier.md)
- [system-image](system-image.md)
- [processing-layers](processing-layers.md)
- [goal](goal.md)
- [world](world.md)
- [perceive](perceive.md)
- [interpret](interpret.md)
- [perform](perform.md)
- [kb-tools](kb-tools.md)
- [agents](agents.md)
- [claude](claude.md)
- [readme](readme.md)
- [index](index.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [skill](skill.md)
- [adopter-comparison](adopter-comparison.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
