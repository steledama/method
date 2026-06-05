# Metodo KB

Framework metodologico e osservatorio cross-repo per knowledge base personali e professionali mantenute con LLM.

Questo repository ha due funzioni complementari. La prima è custodire il metodo portabile: forma dei nodi, struttura di progetto, strumenti di manutenzione, principi guida e ciclo di lavoro. La seconda è osservare come il metodo viene applicato nei progetti adottanti, confrontando componenti, strumenti, skill, nodi, task e segnali di salute delle KB.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale — principi, struttura KB, ciclo operativo — mentre le personalizzazioni sono esplicite: ogni progetto estende il metodo con principi, fonti di verità e strumenti propri del dominio. Le differenze tra progetti non sono rumore: sono materiale di analisi per capire cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo del metodo è bottom-up: un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Questo repo non orchestra task sui progetti adottanti; custodisce il metodo emerso dall'uso reale.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (o1/o2/o3) e input (i1/i2/i3), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro.
- **Strumenti comuni**: `scripts/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura README, migrazione, candidati terminologici e segnali generici sui progetti code-based.
- **Manutenzione propria del metodo**: task in `todo/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Strato output**: [`presentazione/metodo-in-sintesi.md`](presentazione/metodo-in-sintesi.md) è l'o2 del repo — i diagrammi che reggono il metodo intero, dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo dell'azione come specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al processo (anatomia, sviluppo bottom-up, routing). La sintesi vive qui, non nei nodi. Il `.md` è la fonte unica; il PDF per stampa/distribuzione (o3) si rigenera con `cd presentazione && md2pdf metodo-in-sintesi.md` e non viene versionato.

## Progetti adottanti

| Progetto                 | Ambito                                                |
| ------------------------ | ----------------------------------------------------- |
| [nixos](../nixos/)       | Configurazione dichiarativa NixOS multi-host          |
| [bi](../bi/)             | Business intelligence e sincronizzazione dati         |
| [economia](../economia/) | Gestione finanziaria, patrimoniale e legale personale |
| [salute](../salute/)     | Benessere, pratica, filosofia e salute personale      |

## Tasks aperti

- [affinamento-o2](todo/affinamento-o2.md) — rilettura ravvicinata della presentazione (`metodo-in-sintesi.md`) e l'o2 come strumento diagnostico condiviso tra umano e LLM

I task con contesto operativo vivono in `todo/` e vengono rimossi quando completati.

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
- [artefatto-cognitivo](kb/artefatto-cognitivo.md) — Strumento cognitivo esterno (Norman/Hutchins): la KB come artefatto che amplifica la mente; cognizione esperienziale vs riflessiva; principio di naturalezza come criterio di progetto dello strato output
- [sistema-cognitivo](kb/sistema-cognitivo.md) — Accoppiamento dinamico (Hutchins) tra artefatto, umano e LLM; tripartizione artefatto/sistema/metodo; asimmetria dei due agenti (per l'LLM la KB è il modello mentale completo)
- [goal](kb/goal.md) — Gerarchia motivo/goal/operazione (Leontiev): il goal come confine aperto di Norman; KB informa il goal senza generarlo; due modi di i3 (verdetto vs formazione-goal)
- [output](kb/output.md) — Strato output (o1/o2/o3) e input (i1/i2/i3) del metodo: risoluzione del conflitto Zettelkasten/Karpathy; il cappio con due cerniere (Mondo e KB); criteri di Norman per o2
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
