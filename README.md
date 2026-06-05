# Metodo KB

Framework metodologico e osservatorio cross-repo per knowledge base personali e professionali mantenute con LLM.

Questo repository ha due funzioni complementari. La prima è custodire il metodo portabile: forma dei nodi, struttura di progetto, strumenti di manutenzione, principi guida e ciclo di lavoro. La seconda è osservare come il metodo viene applicato nei progetti adottanti, confrontando componenti, strumenti, skill, nodi, task e segnali di salute delle KB.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale — principi, struttura KB, ciclo operativo — mentre le personalizzazioni sono esplicite: ogni progetto estende il metodo con principi, fonti di verità e strumenti propri del dominio. Le differenze tra progetti non sono rumore: sono materiale di analisi per capire cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo del metodo è bottom-up: un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Questo repo non orchestra task sui progetti adottanti; custodisce il metodo emerso dall'uso reale.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (ponte), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro.
- **Strumenti comuni**: `scripts/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura README, migrazione, candidati terminologici e segnali generici sui progetti code-based.
- **Manutenzione propria del metodo**: task in `todo/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Strato output**: [`presentazione/metodo-in-sintesi.md`](presentazione/metodo-in-sintesi.md) è l'L2 del repo — cinque diagrammi che reggono il metodo intero (tre giganti, ciclo dell'azione, anatomia del progetto, sviluppo bottom-up, routing dei contenuti). Il metodo applica il proprio principio `ponte` a sé stesso: la sintesi vive qui, non nei nodi. Il `.md` è la fonte unica; il PDF per stampa/distribuzione (L3) si rigenera con `cd presentazione && md2pdf metodo-in-sintesi.md` e non viene versionato.

## Progetti adottanti

| Progetto                 | Ambito                                                |
| ------------------------ | ----------------------------------------------------- |
| [nixos](../nixos/)       | Configurazione dichiarativa NixOS multi-host          |
| [bi](../bi/)             | Business intelligence e sincronizzazione dati         |
| [economia](../economia/) | Gestione finanziaria, patrimoniale e legale personale |
| [salute](../salute/)     | Benessere, pratica, filosofia e salute personale      |

## Tasks aperti

| Task | Priorità | Note |
| ---- | -------- | ---- |
| [Rifondazione input/output](todo/rifondazione-input-output.md) | alta | Rename ponte→output, L1/L2/L3→o1/o2/o3, introduce strati i1/i2/i3, chiude l'analogia con Norman |
| [Ingest dei libri di Norman](todo/ingest-norman.md) | media | Fonte grezza versionata; primo pilota dello strato input; dipende dalla rifondazione |
| [Scorporo concettuale](todo/artefatto-cognitivo.md) | alta | Artefatto/sistema/metodo, ciclo a due agenti, gerarchia del Goal; cerniera su `ciclo-azione` con la rifondazione |

I task con contesto operativo vivono in `todo/` e vengono rimossi quando
completati.

## Come collegare un nuovo progetto

1. Crea il symlink: `ln -s ../metodo/kb metodo` dalla root del progetto.
2. Aggiungi una riga alla tabella dei progetti adottanti.
3. Nel README del progetto, referenzia `metodo/metodo-kb.md` come nodo centrale del metodo e aggiungi una sezione con i principi specifici del progetto.
4. Aggiorna i path in `CLAUDE.md` del progetto: `kb/metodo-kb.md` → `metodo/metodo-kb.md` (e analogamente per gli altri nodi metodologici).

## Nodi

### Metodo generale

- [metodo-kb](kb/metodo-kb.md) — Hub del metodo: ricetta metodologica, ciclo operativo, tipi documentali, regole di revisione
- [nodo](kb/nodo.md) — Unità atomica della KB: struttura, naming, frontmatter, footer Connessioni
- [knowledge-base](kb/knowledge-base.md) — KB basata su LLM: artefatto cumulativo, divisione del lavoro umano/LLM
- [struttura-progetto](kb/struttura-progetto.md) — Pilastri e componenti operativi: README, CLAUDE.md, AGENTS.md, log.md, todo, skill e strumenti
- [strumenti-kb](kb/strumenti-kb.md) — Script versionati portabili e profili avanzati per audit, backlink, migrazione, copertura e candidati terminologici
- [osservatorio-metodo](kb/osservatorio-metodo.md) — Meta-analisi periodica dei progetti adottanti: componenti, strumenti, skill, nodi, salute e task locali
- [confronto-progetti-adottanti](kb/confronto-progetti-adottanti.md) — Sintesi della situazione attuale dei quattro progetti che adottano il metodo
- [fedelta-cognitiva](kb/fedelta-cognitiva.md) — Verifica della KB oltre il lint: anti-drift, checklist semantica, adattamento al dominio
- [design-principles](kb/design-principles.md) — Principi guida: universali, code-based e specifici di progetto
- [zettelkasten](kb/zettelkasten.md) — Metodo Zettelkasten: nodi atomici interconnessi, struttura emergente
- [pattern-karpathy](kb/pattern-karpathy.md) — Pattern wiki personale mantenuta da LLM: ingest, query, lint e filing back
- [ciclo-azione](kb/ciclo-azione.md) — Modello di Norman come terzo gigante del metodo: sette stadi, due gulf (execution, evaluation), quattro proprietà cardine (visibilità, feedback, mapping, constraint) come criteri di L2
- [affordance-signifier](kb/affordance-signifier.md) — Distinzione di Norman (aggiunta del 2013) tra azione possibile e segnale di dove agire; l'agente «person, animal, or machine» fonda i due strati output (L1 macchina, L2 umano)
- [system-image](kb/system-image.md) — Triangolo di Norman (design model / system image / user's model): la KB è il system image che porta tutto il peso della comunicazione tra i due agenti che non si parlano (umano nel tempo, LLM tra sessioni)
- [visceral-behavioral-reflective](kb/visceral-behavioral-reflective.md) — I tre livelli di Norman (*Emotional Design*): la KB è lo strato riflessivo, che non agisce ma condiziona il behavioral attraverso l'output; emozione e cognizione si intrecciano
- [ponte](kb/ponte.md) — Strato output del metodo: L1 macchina, L2 decisione umana, L3 azione nel mondo; risoluzione del conflitto Zettelkasten/Karpathy (la sintesi vive nello strato output, non nei nodi)
- [connessione](kb/connessione.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta

### Componenti della ricetta

- [agents](kb/agents.md) — Wrapper agent-agnostico: ingresso comune verso README e CLAUDE
- [claude](kb/claude.md) — Costituzione operativa per agenti: regole d'azione, vincoli e bootstrap
- [readme](kb/readme.md) — Bootstrap del progetto: orientamento, task, indice e accessi cognitivi
- [indice](kb/indice.md) — Catalogo statico dei nodi: recupero rapido distinto dalla mappa
- [task-aperti](kb/task-aperti.md) — Supervisione corrente del lavoro futuro nel README
- [mappa](kb/mappa.md) — Modello del dominio: entità, fonti di verità, flussi e nodi
- [todo](kb/todo.md) — Dettagli operativi e contesto dei singoli task aperti
- [log](kb/log.md) — Memoria interpretativa: perché decisioni e sessioni contano
- [git-history](kb/git-history.md) — Storia verificabile dei cambiamenti e dei diff
- [skill](kb/skill.md) — Workflow ricorrenti codificati per agenti
- [fonte-di-verita](kb/fonte-di-verita.md) — Fonti contro cui verificare ciò che la KB dice
