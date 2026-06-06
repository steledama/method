# Indice dei nodi

Catalogo statico della KB, consultato on-demand. Vive dentro `kb/` perché è il
registro della collezione, non un file di bootstrap: il README punta qui, non lo
incorpora. Forma in inglese (`index`, register vivo), distinta dal nodo-concetto
[indice](indice.md) (italiano, documentazione). I conteggi e i segnali si
rigenerano con `scripts/kb_tools.py audit`.

## Metodo generale

- [metodo-kb](metodo-kb.md) — Hub del metodo: ricetta metodologica, ciclo operativo, tipi documentali, regole di revisione
- [nodo](nodo.md) — Unità atomica della KB: struttura, naming, frontmatter, footer Connessioni
- [knowledge-base](knowledge-base.md) — KB basata su LLM: artefatto cumulativo, divisione del lavoro umano/LLM
- [struttura-progetto](struttura-progetto.md) — La triade del layout: root come cruscotto del ciclo di sviluppo, cartelle come collezioni atomiche, pace come criterio di compagnia
- [strumenti-kb](strumenti-kb.md) — Script versionati portabili e profili avanzati per audit, backlink, copertura e candidati terminologici
- [osservatorio-metodo](osservatorio-metodo.md) — Meta-analisi periodica dei progetti adottanti: componenti, strumenti, skill, nodi, salute e task locali
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md) — Sintesi della situazione attuale dei quattro progetti che adottano il metodo
- [fedelta-cognitiva](fedelta-cognitiva.md) — Verifica della KB oltre il lint: anti-drift, checklist semantica, adattamento al dominio
- [design-principles](design-principles.md) — Principi guida: universali, code-based e specifici di progetto
- [zettelkasten](zettelkasten.md) — Metodo Zettelkasten: nodi atomici interconnessi, struttura emergente
- [pattern-karpathy](pattern-karpathy.md) — Pattern wiki personale mantenuta da LLM: ingest, query, lint e filing back
- [ciclo-azione](ciclo-azione.md) — Modello di Norman come terzo gigante del metodo: sette stadi, due gulf, quattro proprietà cardine come criteri di L2
- [affordance-signifier](affordance-signifier.md) — Distinzione di Norman tra azione possibile e segnale di dove agire; l'agente «person, animal, or machine» fonda i due strati output
- [agente](agente.md) — L'attore che agisce nell'artefatto: dal binomio umano/LLM alla popolazione di agenti; distinto da `agents`, che è il file
- [system-image](system-image.md) — Triangolo di Norman: la KB è il system image che porta il peso della comunicazione tra agenti che non si parlano
- [visceral-behavioral-reflective](visceral-behavioral-reflective.md) — I tre livelli di Norman: la KB è lo strato riflessivo, che condiziona il behavioral attraverso l'output
- [artefatto-cognitivo](artefatto-cognitivo.md) — Strumento cognitivo esterno (Norman/Hutchins): cognizione esperienziale vs riflessiva; naturalezza come criterio dell'output
- [sistema-cognitivo](sistema-cognitivo.md) — Accoppiamento dinamico (Hutchins) tra artefatto, umano e LLM; tripartizione artefatto/sistema/metodo; asimmetria degli agenti
- [goal](goal.md) — Gerarchia motivo/goal/operazione (Leontiev): il goal come confine aperto di Norman; KB informa il goal senza generarlo
- [output](output.md) — Strato output (o1/o2/o3) e input (i1/i2/i3): conflitto Zettelkasten/Karpathy, il cappio con due cerniere, criteri di Norman per o2
- [connessione](connessione.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta
- [pace-layering](pace-layering.md) — Strati a frequenza di cambiamento diversa (Duffy, Brand): sostituisce «conoscenza stabile» come criterio di collocazione
- [sviluppo-metodo](sviluppo-metodo.md) — I due movimenti (bottom-up e top-down) in alternanza e contraddittorio

## Componenti della ricetta

- [agents](agents.md) — Wrapper agent-agnostico: ingresso comune verso README e CLAUDE
- [claude](claude.md) — Costituzione operativa per agenti: regole d'azione, vincoli e bootstrap
- [readme](readme.md) — Bootstrap del progetto: orientamento, accessi cognitivi, puntatori a map/plan/index
- [indice](indice.md) — Catalogo statico dei nodi: recupero rapido distinto dalla mappa; nodo-concetto del register `index.md`
- [map](map.md) — Modello del dominio: entità, fonti di verità, flussi e nodi; istanza root `map.md` (vista o2)
- [plan](plan.md) — Supervisione corrente del lavoro futuro: lo stadio Plan del ciclo di sviluppo; istanza root `plan.md`
- [tasks](tasks.md) — Dettagli operativi e contesto dei singoli task aperti: la cartella `tasks/`, stadio Specify
- [why](why.md) — Memoria interpretativa: perché decisioni e sessioni contano; istanza root `why.md`, append-only
- [git-history](git-history.md) — Storia verificabile dei cambiamenti e dei diff
- [skill](skill.md) — Workflow ricorrenti codificati per agenti
- [fonte-di-verita](fonte-di-verita.md) — Fonti contro cui verificare ciò che la KB dice
