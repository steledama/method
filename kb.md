# Indice dei nodi

Catalogo statico della KB — la **porta-collezione** di `kb/` nell'atrio di root: si vede a
colpo d'occhio, si legge on-demand (non al bootstrap). Forma in inglese (`kb`, register vivo),
distinta dal nodo-concetto [indice](kb/indice.md) (italiano, documentazione). I conteggi e i
segnali si rigenerano con `tools/kb_tools.py audit`.

## Metodo generale

- [metodo-kb](kb/metodo-kb.md) — Hub del metodo: ricetta metodologica, ciclo operativo, tipi documentali, regole di revisione
- [nodo](kb/nodo.md) — Unità atomica della KB: struttura, naming, frontmatter, footer Connessioni
- [knowledge-base](kb/knowledge-base.md) — KB basata su LLM: artefatto cumulativo, divisione del lavoro umano/LLM
- [struttura-progetto](kb/struttura-progetto.md) — La root come atrio/system image: file-ciclo e porte-collezione, pace come criterio di compagnia
- [strumenti-kb](kb/strumenti-kb.md) — Strumenti versionati portabili e profili avanzati per audit, backlink, copertura e candidati terminologici
- [osservatorio-metodo](kb/osservatorio-metodo.md) — Meta-analisi periodica dei progetti adottanti: componenti, strumenti, skill, nodi, salute e task locali
- [confronto-progetti-adottanti](kb/confronto-progetti-adottanti.md) — Sintesi della situazione attuale dei quattro progetti che adottano il metodo
- [fedelta-cognitiva](kb/fedelta-cognitiva.md) — Verifica della KB oltre il lint: anti-drift, checklist semantica, adattamento al dominio
- [design-principles](kb/design-principles.md) — Principi guida: universali, code-based e specifici di progetto
- [zettelkasten](kb/zettelkasten.md) — Metodo Zettelkasten: nodi atomici interconnessi, struttura emergente
- [pattern-karpathy](kb/pattern-karpathy.md) — Pattern wiki personale mantenuta da LLM: ingest, query, lint e filing back
- [ciclo-azione](kb/ciclo-azione.md) — Modello di Norman come terzo gigante del metodo: sette stadi, due gulf, quattro proprietà cardine come criteri di o2
- [affordance-signifier](kb/affordance-signifier.md) — Distinzione di Norman tra azione possibile e segnale di dove agire; l'agente «person, animal, or machine» fonda i due strati output
- [agente](kb/agente.md) — L'attore che agisce nell'artefatto: dal binomio umano/LLM alla popolazione di agenti; distinto da `agents`, che è il file
- [system-image](kb/system-image.md) — Triangolo di Norman: la KB è il system image che porta il peso della comunicazione tra agenti che non si parlano
- [visceral-behavioral-reflective](kb/visceral-behavioral-reflective.md) — I tre livelli di Norman: la KB è lo strato riflessivo, che condiziona il behavioral attraverso l'output
- [artefatto-cognitivo](kb/artefatto-cognitivo.md) — Strumento cognitivo esterno (Norman/Hutchins): cognizione esperienziale vs riflessiva; naturalezza come criterio dell'output
- [sistema-cognitivo](kb/sistema-cognitivo.md) — Accoppiamento dinamico (Hutchins) tra artefatto, umano e LLM; tripartizione artefatto/sistema/metodo; asimmetria degli agenti
- [goal](kb/goal.md) — Gerarchia motivo/goal/operazione (Leontiev): il goal come confine aperto di Norman; KB informa il goal senza generarlo
- [mondo](kb/mondo.md) — Il fondo del ciclo d'azione opposto al Goal: cerniera o3↔i1, Mondo runtime vs di sviluppo, di cosa è fatto in ogni artefatto
- [matrice-ciclo-azione](kb/matrice-ciclo-azione.md) — Verifica a 40 caselle: i 6 atti + 2 poli applicati ai cinque artefatti, con verdetto solido/debole/forzato contro l'auto-accondiscendenza
- [output](kb/output.md) — Strato output (o1/o2/o3) e input (i1/i2/i3): conflitto Zettelkasten/Karpathy, il cappio con due cerniere, criteri di Norman per o2
- [connessione](kb/connessione.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta
- [pace-layering](kb/pace-layering.md) — Strati a frequenza di cambiamento diversa (Duffy, Brand): sostituisce «conoscenza stabile» come criterio di collocazione
- [sviluppo-metodo](kb/sviluppo-metodo.md) — I due movimenti (bottom-up e top-down) in alternanza e contraddittorio

## Componenti della ricetta

- [agents](kb/agents.md) — Wrapper agent-agnostico: ingresso comune verso README e CLAUDE
- [claude](kb/claude.md) — Costituzione operativa per agenti: regole d'azione, vincoli e bootstrap
- [readme](kb/readme.md) — La bussola dell'artefatto: orienta e punta, non immagazzina; ingresso per umano e LLM
- [indice](kb/indice.md) — Catalogo statico dei nodi: recupero rapido distinto dalla mappa; nodo-concetto del register `kb.md`
- [map](kb/map.md) — Indice-di-dominio: il territorio reale (entità, sistemi, fonti) legato ai nodi; register root `map.md`, porta on-demand
- [plan](kb/plan.md) — Supervisione corrente del lavoro futuro: lo stadio Plan del ciclo di sviluppo; istanza root `plan.md`
- [tasks](kb/tasks.md) — Dettagli operativi e contesto dei singoli task aperti: la cartella `tasks/`, stadio Specify
- [why](kb/why.md) — Memoria interpretativa: perché decisioni e sessioni contano; istanza root `why.md`, append-only
- [git-history](kb/git-history.md) — Storia verificabile dei cambiamenti e dei diff
- [skill](kb/skill.md) — Workflow ricorrenti codificati per agenti
- [fonte-di-verita](kb/fonte-di-verita.md) — Fonti contro cui verificare ciò che la KB dice
