# Indice dei nodi

Catalogo statico della KB — la **porta-collezione** di `kb/` nell'atrio di root: si vede a
colpo d'occhio, si legge on-demand (non al bootstrap). Forma in inglese (`kb`, register vivo),
distinta dal nodo-concetto [indice](kb/indice.md) (italiano, documentazione). I conteggi e i
segnali si rigenerano con `tools/kb_tools.py audit`.

## Metodo generale

- [cognitive-artifact-design](kb/cognitive-artifact-design.md) — Hub del metodo: design dell'artefatto cognitivo completo per la cognizione condivisa umano-LLM
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
- [vincolo](kb/vincolo.md) — La limitazione progettata (guardrail): tipi di Norman, presidio strutturale sotto il check riflessivo, l'errore reso impossibile o rumoroso
- [agente](kb/agente.md) — L'attore che agisce nell'artefatto: dal binomio umano/LLM alla popolazione di agenti; distinto da `agents`, che è il file
- [system-image](kb/system-image.md) — Triangolo di Norman: la KB è il system image che porta il peso della comunicazione tra agenti che non si parlano
- [processing-layers](kb/processing-layers.md) — I tre strati di elaborazione di Norman applicati alle altitudini del ciclo; il viscerale comprende world e i riflessi i1/o3
- [artefatto-cognitivo](kb/artefatto-cognitivo.md) — Strumento cognitivo esterno (Norman/Hutchins): cognizione esperienziale vs riflessiva; naturalezza come criterio dell'output
- [sistema-cognitivo](kb/sistema-cognitivo.md) — Accoppiamento dinamico (Hutchins) tra artefatto, umano e LLM; tripartizione artefatto/sistema/metodo; asimmetria degli agenti
- [goal](kb/goal.md) — Gerarchia motivo/goal/operazione (Leontiev): il goal come confine aperto di Norman; KB informa il goal senza generarlo
- [world](kb/world.md) — Membrana fisica non versionata al fondo del ciclo; i1 e o3 sono i suoi riflessi versionati on-demand
- [matrice-ciclo-azione](kb/matrice-ciclo-azione.md) — Verifica a 40 caselle: i 6 atti + 2 poli applicati ai cinque artefatti, con verdetto solido/debole/forzato contro l'auto-accondiscendenza
- [output](kb/output.md) — Strato output (o1/o2/o3), l'arco di esecuzione: conflitto Zettelkasten/Karpathy, le tre altitudini, la forma dell'o2 segue la domanda, criteri di Norman
- [input](kb/input.md) — Strato input (i1/i2/i3): due tessiture di i1, valenza come confine i1→i2 e formazione-goal
- [deck](kb/deck.md) — Runbook portabile del deck come forma navigabile di `interpretations/`: sorgente markdown unica, build Reveal da CDN, apertura locale e condivisione on-demand
- [connessione](kb/connessione.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta
- [pace-layering](kb/pace-layering.md) — Strati a frequenza di cambiamento diversa (Duffy, Brand): sostituisce «conoscenza stabile» come criterio di collocazione
- [sviluppo-metodo](kb/sviluppo-metodo.md) — I due movimenti (bottom-up e top-down) in alternanza e contraddittorio
- [consenso](kb/consenso.md) — Proporre, attendere consenso esplicito, non scambiare un sì parziale per un sì totale; gemello sul lato verifica

## Componenti della ricetta

- [agents](kb/agents.md) — Wrapper agent-agnostico: ingresso comune verso README e CLAUDE
- [claude](kb/claude.md) — Costituzione operativa per agenti: regole d'azione, vincoli e bootstrap
- [readme](kb/readme.md) — La bussola dell'artefatto: orienta e punta, non immagazzina; ingresso per umano e LLM
- [indice](kb/indice.md) — Catalogo statico dei nodi: recupero rapido distinto dalla mappa; nodo-concetto del register `kb.md`
- [map](kb/map.md) — Indice-di-dominio: il territorio reale (entità, sistemi, fonti) legato ai nodi; register root `map.md`, porta on-demand
- [plan](kb/plan.md) — Supervisione corrente del lavoro futuro: lo stadio Plan del ciclo di sviluppo; istanza root `plan.md`
- [tasks](kb/tasks.md) — Dettagli operativi e contesto dei singoli task aperti: la cartella `tasks/`, stadio Specify
- [verdict](kb/verdict.md) — Il verdetto attuale del progetto, per filo/area aperta: lo stadio Compare (i3) del ciclo di sviluppo; istanza root `verdict.md`, aggiornata in place
- [git-history](kb/git-history.md) — Storia verificabile dei cambiamenti e dei diff
- [skill](kb/skill.md) — Workflow ricorrenti codificati per agenti
- [fonte-di-verita](kb/fonte-di-verita.md) — Fonti contro cui verificare ciò che la KB dice
