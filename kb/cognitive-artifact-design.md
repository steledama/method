---
stato: maturo
---

# Cognitive artifact design

Il _cognitive artifact design_ è la pratica con cui si progettano e si
mantengono artefatti cognitivi per la cognizione condivisa tra umano e LLM. Non
progetta soltanto una knowledge base: progetta l'intero ciclo che collega Goal,
rappresentazioni persistenti, decisione, azione nel `world`, percezione del
ritorno e revisione. La KB è lo strato riflessivo dell'artefatto, necessario ma
non sufficiente — riflessiva come _livello_ di elaborazione, e nucleo
formalizzato del _system image_, che è invece l'intero artefatto, trasversale ai
tre livelli e canale tra agenti (cfr. `system-image`, `processing-layers`).

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

Il metodo si inscrive nella cornice di augmentation di Engelbart (H-LAM/T), che
contiene i suoi riferimenti: lo Zettelkasten definisce la forma dei nodi atomici
e interconnessi (il means _Language_); Norman fornisce il modello che collega
conoscenza, rappresentazione e azione attraverso il ciclo completo (l'interfaccia
col Mondo); la gamba di manutenzione dell'insieme con l'LLM è il _Methodology/
Training_ engelbartiano, di cui il pattern Karpathy è l'istanza contemporanea.
Il pavimento ontologico — perché il sistema accoppiato sia cognizione — è
Hutchins/Clark. La trattazione vive in `augmentation-system` e `cognitive-system`.

Il principio centrale è che l'artefatto non è una cartella di appunti né un
archivio da interrogare occasionalmente. È cumulativo: ogni ingest, query, lint
o filing back deve lasciarlo più chiaro, più collegato o più verificabile
di prima. La struttura della KB emerge dalle connessioni tra i nodi; la
struttura esplicita appartiene al progetto intero: atrio, cruscotto nelle stanze
`o1/` e `i3/`, cataloghi interni, collezioni-stadio, strati input/output e
membrana `world`.

Il metodo è portabile tra progetti diversi. La sua parte stabile riguarda forma dei nodi, strumenti di manutenzione, memoria interpretativa, indice, task aperti e collaborazione con LLM; la parte locale riguarda dominio, cluster, lessico, fonti, vincoli tecnici e priorità. Il principio generale è neutro: relazionalità, significato emergente dalle connessioni, conoscenza come rete invece che come archivio di elementi isolati.

Lo sviluppo del metodo procede per due movimenti complementari in alternanza, descritti in `method-development`. Dal basso, una modifica metodologica nasce da un'esigenza concreta in un repo adottante: un problema reale di dominio obbliga a inventare o correggere una pratica locale; se la soluzione si dimostra riusabile, viene riportata nel repo `metodo` come generalizzazione portabile; gli altri repo adottanti la ricevono poi leggendo i commit del metodo e applicando solo ciò che è pertinente. Dall'alto, una cornice teorica importata — un gigante, una distinzione — offre la forma per nominare e mettere in ordine ciò che dal basso si avverte ma non si sa inquadrare. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione, non l'unica regola. Esiste anche un movimento top-down sul lato runtime, con pari dignità: `metodo` pianifica il proprio **output di canone** — le prescrizioni (o3-runtime) e le convergenze che disegnano come gli artefatti adottanti dovrebbero diventare — che l'adottante poi recepisce eseguendolo nel proprio `method-review`. Ciò che resta fuori è il **micromanagement della coda interna** degli adottanti: aprire in `metodo` task che ordinano i singoli interventi nei loro repo. La linea di faglia è tra pianificare il proprio canone (legittimo) e gestire la coda altrui (no).

Il repo che ospita il metodo ha anche una funzione di osservatorio. Raccoglie le differenze tra progetti adottanti, confronta componenti, strumenti, skill e salute delle KB, e decide se un segnale debba diventare generalizzazione metodologica, estensione strumentale o restare lavoro locale nel progetto interessato. La diagnosi può sfociare in prescrizione: quando l'osservatorio rileva uno squilibrio generalizzabile, `metodo` emette un o3-runtime che l'adottante recepisce. Ciò che resta escluso non è il prescrivere ma il **sostituirsi alla coda operativa**: `metodo` custodisce le astrazioni emerse e disegna il proprio canone, non micromanagia gli interventi interni dei repo adottanti.

Indice cognitivo del metodo:

- `AGENTS.md`: dove trovo le istruzioni operative condivise tra agenti?
- `CLAUDE.md`: come devo agire in questo repo?
- `README.md`: dove sono e da dove parto?
- `kb/kb.md`: quali nodi esistono e come li trovo?
- `o1/plan.md`: cosa dobbiamo fare adesso?
- `goal.md`: verso quale nord lavora il progetto, misurato da quali segnali?
- `world.md`: com'è fatto il territorio reale del dominio — superfici, entità, fonti — e come si lega ai nodi?
- nodo: che cosa significa questo concetto specifico?
- connessioni: a quali altri concetti è legato?
- `o2/`: quali sono i dettagli operativi e di contesto dei singoli task aperti?
- `i3/`: perché una decisione o una sessione conta?
- git history: che cosa è cambiato davvero?
- `o3/`: quali controlli e prescrizioni sono deterministici?
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
  nucleo formalizzato del system image (che è l'intero artefatto, il canale trasversale tra agenti — cfr. `system-image`). Contiene i nodi di metodo e
  di dominio. Il nucleo portabile comprende `cognitive-artifact-design`,
  `knowledge-base`, `node`, `zettelkasten`, `karpathy-pattern`,
  `project-structure`, `kb-tools`, `connection` e, quando il dominio
  richiede verifica anti-drift, `cognitive-fidelity`. Negli adottanti questi nodi
  possono vivere in `method/` come symlink, mentre `kb/` resta dedicata al
  dominio.
- `README.md`: la **bussola** e il file di bootstrap per umano e LLM. Presenta nome, dominio, scopo e principi locali in sintesi, e punta al resto del cruscotto. È il primo punto di accesso e deve permettere di orientarsi senza leggere tutto il repository: **orienta e punta, non immagazzina** — i task in `o1/plan.md`, il catalogo in `kb/kb.md`, il modello nei nodi e in `i2/`, i poli nei register `goal.md` e `world.md`. Dettaglio nel nodo `readme`.
- `CLAUDE.md`: costituzione operativa del progetto. Contiene regole d'azione, vincoli, workflow consentiti e riferimenti rapidi per agenti; non contiene conoscenza di dominio né descrizioni narrative del sistema. Quando cresce oltre il ruolo operativo, il contenuto va trasferito nei nodi tematici e sostituito da pointer.
- `AGENTS.md`: wrapper agent-agnostico minimale. Non duplica le regole operative; esplicita l'ordine di lettura e rimanda a `README.md` e `CLAUDE.md`, così agenti diversi entrano nello stesso protocollo di lavoro.
- `goal.md` + `world.md`: i **register dei due poli** in root, porte aperte on-demand. `goal.md` declina il nord in obiettivi con segnali e lavoro corrente (custode umano); `world.md` indicizza il territorio — superfici della membrana, entità, fonti di verità con provenienza — e lo lega ai nodi che lo spiegano. Non sono la bussola (quella è il README) né il modello (che vive nei nodi e in `i2/`). Dettaglio nei nodi `goal` e `world`.
- `i3/`: i verdetti attuali, un file per filo/area aperta. Il git log conserva cosa è cambiato; il filo conserva come stanno le cose ora e perché conta, aggiornato in place — la cronologia di un filo è il git history del file stesso. Non è un archivio di output automatici.
- `o1/plan.md` + `o2/`: il Plan supervisiona il lavoro futuro; `o2/` ne tiene i dettagli operativi. `o1/plan.md` è l'indice di `o2/`: ogni task sostanziale ha una riga e, quando serve contesto, un file dedicato. I task completati vengono rimossi; la storia resta in git, nei fili `i3/` e nei nodi aggiornati.
- `o3/`: prescrizioni e strumenti versionati per la parte deterministica della manutenzione (la macchina del ciclo di _sviluppo_, distinta dagli `scripts/` di output del _runtime_ nei repo code-based). `o3/kb_tools.py`, quando presente, gestisce audit, link, backlink, README, migrazione, candidati terminologici e controlli specifici di dominio. Gli strumenti devono produrre segnali verificabili; il giudizio resta umano/LLM.
- `.claude/skills/`: interfacce operative per workflow ricorrenti. Il quartetto operativo ufficiale è `kb-review` (diagnosi), `plan-review` (supervisione del braccio di esecuzione), `verdicts-review` (supervisione del braccio di valutazione) e `commit` (gate di filing back); `method-review` verifica l'allineamento dell'adottante ai commit del metodo. Ogni progetto può aggiungere skill locali per workflow di dominio. Una skill interpreta e orchestra gli strumenti versionati, senza reimplementare parsing fragile in chat.
- `.codex/skills/`: wrapper opzionali quando il progetto deve essere usabile anche da Codex. Devono rimandare alle skill canoniche senza duplicare workflow.
- strato output: traduce la KB in azione possibile (o1 macchina / o2 decisione
  / o3 prescrizione versionata). Lo strato di sintesi-documento ha nome
  uniforme, `i2/`; la stessa superficie è o2 quando viene prodotta
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
- generare `README.md` come bussola concisa che orienta e punta a `o1/plan.md`, `kb/kb.md`, al modello (nodi/`i2/`) e ai register dei poli
- generare `CLAUDE.md` come costituzione operativa, non come documentazione narrativa
- generare `AGENTS.md` come wrapper minimale verso `README.md` e `CLAUDE.md`
- creare `kb/kb.md` come catalogo dei nodi e i register dei poli `goal.md` e `world.md`
- dichiarare la membrana `world/` e gli strati input/output del dominio, senza
  creare riflessi versionati che l'uso non richiede ancora
- creare `i3/verdicts.md` e, se serve, un primo file-filo di fondazione
- creare `o1/plan.md` come Plan e `o2/` per i dettagli operativi, inserendovi solo lavoro futuro, mai storico
- creare almeno i nodi dominio iniziali se il progetto ha già concetti stabili
- aggiungere strumenti in `o3/`, skill e wrapper solo quando esistono workflow reali da rendere ripetibili

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
- o2/: conserva lavoro futuro e contesto transitorio
- i3/: il verdetto attuale per filo/area aperta

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
- ciò che è da fare resta in `o1/plan.md` o, con contesto, in `o2/`
- ciò che è stato fatto sparisce da `o2/` e viene conservato da git, fili `i3/` e nodi aggiornati
- ciò che spiega perché una decisione conta va nei fili `i3/`
- ciò che spiega come lavorare va in CLAUDE.md, skill o strumenti versionati
- ciò che serve solo come appunto temporaneo non entra nel metodo finché non diventa task, nodo o verdict
- la KB permanente descrive il presente; la storia resta in git e nei fili `i3/` salvo che diventi concetto riusabile
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
- cluster del catalogo `kb/kb.md`
- fonti e directory specialistiche
- task aperti e priorità
- lessico specifico del dominio
- eventuali interpretazioni filosofiche locali del metodo

Connessioni:

- [cognitive-artifact](cognitive-artifact.md)
- [cognitive-system](cognitive-system.md)
- [augmentation-system](augmentation-system.md)
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
