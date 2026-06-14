---
data: 2026-06-13
stato: maturo
---

# Cognitive artifact design

Il _cognitive artifact design_ è la pratica con cui si progettano e si
mantengono artefatti cognitivi per la cognizione condivisa tra umano e LLM. Non
progetta soltanto una knowledge base: progetta l'intero ciclo che collega Goal,
rappresentazioni persistenti, decisione, azione nel `world`, percezione del
ritorno e revisione. La KB è lo strato riflessivo dell'artefatto, necessario ma
non sufficiente — riflessiva come _livello_ di elaborazione, ma _system image_
trasversale ai tre livelli come canale tra agenti (cfr. `system-image`,
`processing-layers`).

L'oggetto progettato è l'**artefatto cognitivo**: il repository portabile con la
sua anatomia, le rappresentazioni e i vincoli. Il risultato nell'uso è il
**sistema cognitivo**: l'accoppiamento dinamico tra artefatto, umano, LLM,
harness e ambiente. Il metodo coltiva il primo perché il secondo possa
funzionare, senza confondere ciò che persiste con agenti e infrastrutture che
cambiano.

Il ciclo completo comprende tre altitudini. In alto, la KB accumula concetti,
assunzioni e verdetti nello strato riflessivo. In mezzo, o2/i2 rende la sintesi
leggibile per specificare e interpretare. In basso, o3 e i1 sono i riflessi
versionati on-demand della membrana `world`: prescrizione dell'atto e cattura
del segnale. L'atto e il grezzo restano nel Mondo non versionato. Progettare
l'artefatto significa rendere attraversabili entrambi i gulf, non soltanto
organizzare bene i nodi.

Il grado di automazione non è uniforme. Le operazioni note e verificabili
possono essere delegate; formazione del Goal, triage dei segnali esogeni e
decisioni ad alta posta richiedono supervisione umana. Il gradiente di autonomia
si progetta per stadio, dominio e rischio, mantenendo espliciti feedback,
vincoli e punti di controllo.

Il metodo si appoggia su tre pilastri: lo Zettelkasten definisce la forma dei
nodi atomici e interconnessi; il pattern Karpathy definisce il ciclo di
manutenzione dell'insieme con l'LLM; Norman fornisce il modello che collega
conoscenza, rappresentazione e azione attraverso il ciclo completo.

Il principio centrale è che l'artefatto non è una cartella di appunti né un
archivio da interrogare occasionalmente. È cumulativo: ogni ingest, query, lint
o filing back deve lasciarlo più chiaro, più collegato o più verificabile
di prima. La struttura della KB emerge dalle connessioni tra i nodi; la
struttura esplicita appartiene al progetto intero: cruscotto in root,
cataloghi e collezioni-stadio, strati input/output e membrana `world`.

Il metodo è portabile tra progetti diversi. La sua parte stabile riguarda forma dei nodi, strumenti di manutenzione, memoria interpretativa, indice, task aperti e collaborazione con LLM; la parte locale riguarda dominio, cluster, lessico, fonti, vincoli tecnici e priorità. Il principio generale è neutro: relazionalità, significato emergente dalle connessioni, conoscenza come rete invece che come archivio di elementi isolati.

Lo sviluppo del metodo procede per due movimenti complementari in alternanza, descritti in `method-development`. Dal basso, una modifica metodologica nasce da un'esigenza concreta in un repo adottante: un problema reale di dominio obbliga a inventare o correggere una pratica locale; se la soluzione si dimostra riusabile, viene riportata nel repo `metodo` come generalizzazione portabile; gli altri repo adottanti la ricevono poi leggendo i commit del metodo e applicando solo ciò che è pertinente. Dall'alto, una cornice teorica importata — un gigante, una distinzione — offre la forma per nominare e mettere in ordine ciò che dal basso si avverte ma non si sa inquadrare. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione, non l'unica regola. Il flusso inverso — aprire in `metodo` task che ordinano interventi nei repo adottanti — è da evitare salvo manutenzioni che riguardino davvero il metodo stesso.

Il repo che ospita il metodo ha anche una funzione di osservatorio. Raccoglie le differenze tra progetti adottanti, confronta componenti, strumenti, skill e salute delle KB, e decide se un segnale debba diventare generalizzazione metodologica, estensione strumentale o restare lavoro locale nel progetto interessato. Osservare non significa orchestrare: il repo `metodo` custodisce le astrazioni emerse, non sostituisce le code operative dei repo adottanti.

Indice cognitivo del metodo:

- `AGENTS.md`: dove trovo le istruzioni operative condivise tra agenti?
- `CLAUDE.md`: come devo agire in questo repo?
- `README.md`: dove sono e da dove parto?
- `kb.md`: quali nodi esistono e come li trovo?
- `plan.md`: cosa dobbiamo fare adesso?
- `map.md`: com'è fatto il territorio reale del dominio, e come si lega ai nodi? (dove esiste)
- nodo: che cosa significa questo concetto specifico?
- connessioni: a quali altri concetti è legato?
- `tasks/`: quali sono i dettagli operativi e di contesto dei singoli task aperti?
- `verdict.md`: perché una decisione o una sessione conta?
- git history: che cosa è cambiato davvero?
- `tools/`: quali controlli sono deterministici?
- skill: quali workflow ricorrenti sono codificati?
- fonti di verità: contro che cosa verifico ciò che la KB dice?
- fedeltà cognitiva: la KB aderisce ancora al sistema reale?
- osservatorio metodo: che cosa impariamo confrontando i progetti?
- cognitive artifact design: come si progetta l'artefatto cognitivo completo?

Ricetta metodologica:

- artefatto completo: cruscotto, KB, rappresentazioni input/output, strumenti e
  membrana `world` formano un solo sistema progettato; nessuna parte è il metodo
  per intero
- `kb/`: la conoscenza stabile dell'artefatto — strato riflessivo come livello,
  system image trasversale come canale tra agenti (cfr. `system-image`). Contiene i nodi di metodo e
  di dominio. Il nucleo portabile comprende `cognitive-artifact-design`,
  `knowledge-base`, `node`, `zettelkasten`, `karpathy-pattern`,
  `project-structure`, `kb-tools`, `connection` e, quando il dominio
  richiede verifica anti-drift, `cognitive-fidelity`. Negli adottanti questi nodi
  possono vivere in `method/` come symlink, mentre `kb/` resta dedicata al
  dominio.
- `README.md`: la **bussola** e il file di bootstrap per umano e LLM. Presenta nome, dominio, scopo e principi locali in sintesi, e punta al resto del cruscotto. È il primo punto di accesso e deve permettere di orientarsi senza leggere tutto il repository: **orienta e punta, non immagazzina** — i task in `plan`, il catalogo in `kb`, il modello nei nodi e in `interpretations/` (e nell'indice-di-dominio `map` dove esiste). Dettaglio nel nodo `readme`.
- `CLAUDE.md`: costituzione operativa del progetto. Contiene regole d'azione, vincoli, workflow consentiti e riferimenti rapidi per agenti; non contiene conoscenza di dominio né descrizioni narrative del sistema. Quando cresce oltre il ruolo operativo, il contenuto va trasferito nei nodi tematici e sostituito da pointer.
- `AGENTS.md`: wrapper agent-agnostico minimale. Non duplica le regole operative; esplicita l'ordine di lettura e rimanda a `README.md` e `CLAUDE.md`, così agenti diversi entrano nello stesso protocollo di lavoro.
- `map.md`: l'**indice-di-dominio** in root, una porta aperta on-demand (come `kb.md`). Collega il territorio reale — entità, fonti di verità, flussi — ai nodi che lo spiegano. Presente dove il dominio ha un territorio da indicizzare; assente dove è astratto (in `metodo` non c'è). Non è la bussola (quella è il README) né il modello (che vive nei nodi e in `interpretations/`). Dettaglio nel nodo `map`.
- `verdict.md`: il verdetto attuale, per filo/area aperta. Il git log conserva cosa è cambiato; `verdict.md` conserva come stanno le cose ora su ciascun filo e perché conta, aggiornato in place — la cronologia di un filo è il git history del file stesso. Non è un archivio di output automatici.
- `plan.md` + `tasks/`: il Plan in root supervisiona il lavoro futuro; `tasks/` ne tiene i dettagli operativi. `plan.md` è l'indice di `tasks/`: ogni task sostanziale ha una riga e, quando serve contesto, un file dedicato. I task completati vengono rimossi; la storia resta in git, verdict e nodi aggiornati.
- `tools/`: strumenti versionati per la parte deterministica della manutenzione (la macchina del ciclo di _sviluppo_, distinta dagli `scripts/` di output del _runtime_ nei repo code-based). `tools/kb_tools.py`, quando presente, gestisce audit, link, backlink, README, migrazione, candidati terminologici e controlli specifici di dominio. Gli strumenti devono produrre segnali verificabili; il giudizio resta umano/LLM.
- `.claude/skills/`: interfacce operative per workflow ricorrenti. La triade operativa ufficiale è `kb-review` (diagnosi), `tasks-review` (supervisione del lavoro futuro) e `commit` (gate di filing back); `method-review` verifica l'allineamento dell'adottante ai commit del metodo. Ogni progetto può aggiungere skill locali per workflow di dominio. Una skill interpreta e orchestra gli strumenti versionati, senza reimplementare parsing fragile in chat.
- `.codex/skills/`: wrapper opzionali quando il progetto deve essere usabile anche da Codex. Devono rimandare alle skill canoniche senza duplicare workflow.
- strato output: traduce la KB in azione possibile (o1 macchina / o2 decisione
  / o3 prescrizione versionata). Lo strato di sintesi-documento ha nome
  uniforme, `interpretations/`; la stessa superficie è o2 quando viene prodotta
  e substrato i2 quando viene letta.
- strato input: cattura il ritorno (i1 valenza-neutro → i2 interpretazione → i3
  formalizzazione) e permette all'artefatto di ascoltare ciò che lo smentisce.
- `world/`: membrana host-local non versionata verso il Mondo runtime. L'atto e
  il grezzo vivono qui; o3/i1 ne sono i riflessi versionati quando precisione o
  durata lo richiedono. Non ha manifest.
- convenzioni markdown: frontmatter minimale per nodi e task, nessun frontmatter nei file root, H1, corpo autonomo, link inline solo quando servono alla frase, sezione finale `Connessioni:` come footer di navigazione. Il dettaglio vive nei nodi `node` e `tasks`.

Creazione di un nuovo progetto:

- partire dalla ricetta metodologica come checklist, non come gerarchia concettuale
- personalizzare nome, dominio, scopo, cluster iniziali, fonti di verità e task aperti
- generare `README.md` come bussola concisa che orienta e punta a `plan.md`, `kb.md` e al modello (nodi/`interpretations`, e `map.md` dove esiste)
- generare `CLAUDE.md` come costituzione operativa, non come documentazione narrativa
- generare `AGENTS.md` come wrapper minimale verso `README.md` e `CLAUDE.md`
- creare `kb.md` come catalogo dei nodi e, dove il dominio ha un territorio da indicizzare, `map.md` come indice-di-dominio
- dichiarare la membrana `world/` e gli strati input/output del dominio, senza
  creare riflessi versionati che l'uso non richiede ancora
- creare `verdict.md` vuoto o con un primo filo di fondazione
- creare `plan.md` come Plan e `tasks/` per i dettagli operativi, inserendovi solo lavoro futuro, mai storico
- creare almeno i nodi dominio iniziali se il progetto ha già concetti stabili
- aggiungere `tools/`, skill e wrapper solo quando esistono workflow reali da rendere ripetibili

Ogni componente della ricetta merita un nodo autonomo, anche quando è ancora in stato bozza. Il nodo autonomo rende esplicita la funzione cognitiva del componente, permette confronti cross-repo e segnala quali parti del metodo sono mature e quali sono ancora work in progress. Un componente può essere descritto anche in `project-structure`, ma il suo nodo dedicato resta il punto in cui accumulare regole, esempi reali e criteri di revisione.

Evidenza dai progetti adottanti:

- `nixos` e `bi` usano il metodo come nucleo condiviso linkato da `method/`, con README molto forti come router e mappe di progetto specifiche
- `economia` incorpora una variante locale con file aggiuntivi (`stato.md`, `scadenze.md`, `diario.md`) e fonti di verità JSON, mostrando che la ricetta deve ammettere componenti di dominio senza assorbirli nel nucleo portabile
- `salute` conserva una forma più narrativa del metodo nel README, utile come traccia storica ma meno separata tra metodo portabile, filosofia locale e indice della KB
- i progetti tecnici richiedono strumenti anti-drift e fonti di verità verificabili; i progetti riflessivi richiedono soprattutto accessi cognitivi, hub semantici e filing back accurato
- ogni progetto adottante attraversa già `world` e ha strati input/output, anche
  senza averli nominati; dove o2 è forte il progetto serve decisioni condivise
  con altri (`bi`), mentre un artefatto solo riflessivo fatica a generare azione
  coordinata

La fotografia comparativa corrente vive nel nodo `adopter-comparison`. I nodi dei singoli componenti contengono invece il dettaglio per progetto, così il confronto non resta una nota generale ma diventa parte della definizione pratica del componente.

Tipi documentali:

- map: indice-di-dominio — collega il territorio reale a fonti di verità e nodi (dove esiste)
- nodo concettuale: spiega un'idea stabile e riusabile
- reference: rende accessibili dati o convenzioni da consultare rapidamente
- runbook: guida un'azione operativa con sequenza e verifiche
- tasks/: conserva lavoro futuro e contesto transitorio
- verdict.md: il verdetto attuale per filo/area aperta

Le categorie non sono gabbie formali, ma aiutano a preservare funzione e
aspettative di lettura. Quando più tipi iniziano a convivere nello stesso file,
la KB diventa meno accessibile anche se il contenuto resta corretto.

Operazioni ricorrenti:

- ingest: una fonte viene trasformata in conoscenza compilata, cioè nodi nuovi o aggiornamenti a nodi esistenti
- query: una domanda attraversa la rete dei nodi e può produrre una risposta temporanea o un nuovo contenuto stabile
- lint: la KB viene controllata per link rotti, orfani, cluster isolati, nodi non indicizzati e problemi di formato
- fidelity: fatti ad alta deriva e copertura documentale vengono confrontati con
  fonti tecniche verificabili, senza confondere segnali automatici e giudizio
  semantico
- filing back: le sintesi nate in chat o nel diario vengono riportate nella KB quando hanno valore durevole
- revisione strutturale: si verifica se i nodi hanno ancora funzione limpida, aderenza al presente e accessi cognitivi adeguati
- commit: le modifiche vengono consolidate in git con messaggi brevi e leggibili

Regole sullo stato:

- ciò che è stabile e riusabile diventa nodo in kb/
- ciò che è da fare resta in `plan.md` o, con contesto, in tasks/
- ciò che è stato fatto sparisce da tasks/ e viene conservato da git, verdict.md e dai nodi aggiornati
- ciò che spiega perché una decisione conta va in verdict.md
- ciò che spiega come lavorare va in CLAUDE.md, skill o strumenti versionati
- ciò che serve solo come appunto temporaneo non entra nel metodo finché non diventa task, nodo o verdict
- la KB permanente descrive il presente; la storia resta in git e verdict.md salvo che diventi concetto riusabile
- una generalizzazione metodologica entra in `metodo` solo dopo evidenza locale sufficiente in almeno un repo adottante, e idealmente con verifica di portabilità su almeno un secondo contesto

Regole di revisione:

- separare per audience o responsabilità quando lettori diversi hanno bisogno di istruzioni diverse
- separare stato corrente, procedura e storia quando iniziano a convivere nello stesso nodo
- distinguere mappa, concetto, reference e runbook prima ancora di chiedersi se il file sia lungo
- creare nuovi nodi solo se migliorano accessibilità e stabilità semantica
- preferire esempi realmente incarnati nel dominio a esempi didattici plausibili ma non verificati
- quando due flussi possono divergere nel tempo, documentarli separatamente anche se oggi sono ancora vicini
- trattare i warning anti-drift come inviti alla revisione, non come errori da
  sopprimere automaticamente
- i file operativi (CLAUDE.md, skill, hook) sono costituzione, non documentazione: le descrizioni di come funziona qualcosa appartengono ai nodi tematici, mai al file operativo, che ne è solo il pointer
- quando un file operativo cresce a contenere descrizioni del sistema, trasferire il contenuto nei nodi tematici prima di rimuoverlo dal file operativo (mappa per sezione: keep / relocate / remove, poi arricchimento dei nodi target, poi rimozione)
- quando un elenco metodologico compare in più punti, mantenerlo una sola volta come ricetta e usare gli altri punti per descrivere funzione, variazioni locali o procedura
- quando un componente del metodo accumula regole proprie, esempi cross-repo e criteri di revisione, promuoverlo a nodo autonomo collegato da questo hub
- quando una tensione metodologica emerge in un repo adottante, risolverla prima lì; aggiornare `metodo` solo dopo aver distinto soluzione locale, criterio portabile e propagazione eventuale agli altri repo

Personalizzazioni locali:

- nome, dominio e scopo del progetto
- cluster del catalogo `kb.md`
- fonti e directory specialistiche
- task aperti e priorità
- lessico specifico del dominio
- eventuali interpretazioni filosofiche locali del metodo

Connessioni:

- [cognitive-artifact](cognitive-artifact.md)
- [cognitive-system](cognitive-system.md)
- [world](world.md)
- [input](input.md)
- [processing-layers](processing-layers.md)
- [system-image](system-image.md)
- [node](node.md)
- [knowledge-base](knowledge-base.md)
- [karpathy-pattern](karpathy-pattern.md)
- [project-structure](project-structure.md)
- [kb-tools](kb-tools.md)
- [agents](agents.md)
- [claude](claude.md)
- [readme](readme.md)
- [index](index.md)
- [plan](plan.md)
- [map](map.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [source-of-truth](source-of-truth.md)
- [method-observatory](method-observatory.md)
- [method-development](method-development.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [design-principles](design-principles.md)
- [zettelkasten](zettelkasten.md)
- [connection](connection.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
