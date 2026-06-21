# Indice dei nodi

Catalogo statico della KB — il **catalogo trasversale** di `kb/` nell'atrio di root: si vede a
colpo d'occhio, si legge on-demand (non al bootstrap). Forma in inglese (`kb`, register vivo),
distinta dal nodo-concetto [index](kb/index.md) (italiano, documentazione). I conteggi e i
segnali si rigenerano con `tools/kb_tools.py audit`.

## Metodo generale

- [cognitive-artifact-design](kb/cognitive-artifact-design.md) — Hub del metodo: design dell'artefatto cognitivo completo per la cognizione condivisa umano-LLM
- [node](kb/node.md) — Unità atomica della KB: struttura, naming, frontmatter, footer Connessioni
- [knowledge-base](kb/knowledge-base.md) — KB basata su LLM: artefatto cumulativo, divisione del lavoro umano/LLM
- [kb-content-typology](kb/kb-content-typology.md) — Di cosa parla la KB (≠ a cosa serve): il contenuto denota i poli del ciclo — ought/is/macchina — e il baricentro per repo è una diagnosi
- [project-structure](kb/project-structure.md) — La root come atrio/system image: tre specie di file-root e collezioni-stadio, gradiente di cardinalità
- [kb-tools](kb/kb-tools.md) — Strumenti versionati portabili e profili avanzati per audit, backlink, copertura e candidati terminologici
- [method-observatory](kb/method-observatory.md) — Meta-analisi periodica dei progetti adottanti: componenti, strumenti, skill, nodi, salute e task locali
- [adopter-comparison](kb/adopter-comparison.md) — Sintesi della situazione attuale dei quattro progetti che adottano il metodo
- [cognitive-fidelity](kb/cognitive-fidelity.md) — Verifica della KB oltre il lint: anti-drift, checklist semantica, adattamento al dominio
- [design-principles](kb/design-principles.md) — Principi guida: universali, code-based e specifici di progetto
- [augmentation-system](kb/augmentation-system.md) — La cornice di sistema di Engelbart (H-LAM/T) che contiene i giganti: synergism, i quattro means, il bootstrap come antenato di dogfooding e cicli annidati
- [zettelkasten](kb/zettelkasten.md) — Metodo Zettelkasten: nodi atomici interconnessi, struttura emergente; le schede edge-notched di Engelbart come precursore
- [karpathy-pattern](kb/karpathy-pattern.md) — Istanza contemporanea (era LLM) della gamba di manutenzione, non pilastro: ingest, query, lint e filing back
- [action-cycle](kb/action-cycle.md) — Modello di Norman, l'interfaccia col Mondo dentro la cornice di augmentation: sei atti due poli, due gulf, quattro proprietà cardine come criteri di o2
- [affordance-signifier](kb/affordance-signifier.md) — Distinzione di Norman tra azione possibile e segnale di dove agire; l'agente «person, animal, or machine» fonda i due strati output
- [constraint](kb/constraint.md) — La limitazione progettata (guardrail): tipi di Norman, presidio strutturale sotto il check riflessivo, l'errore reso impossibile o rumoroso
- [agent](kb/agent.md) — L'attore che agisce nell'artefatto: dal binomio umano/LLM alla popolazione di agenti; distinto da `agents`, che è il file
- [system-image](kb/system-image.md) — Triangolo di Norman: la KB è il system image che porta il peso della comunicazione tra agenti che non si parlano
- [processing-layers](kb/processing-layers.md) — I tre strati di elaborazione di Norman applicati alle altitudini del ciclo; il viscerale comprende world e i riflessi i1/o3
- [cognitive-artifact](kb/cognitive-artifact.md) — Strumento cognitivo esterno (Norman/Hutchins): cognizione esperienziale vs riflessiva; naturalezza come criterio dell'output
- [cognitive-system](kb/cognitive-system.md) — Accoppiamento dinamico (Hutchins) tra artefatto, umano e LLM; tripartizione artefatto/sistema/metodo; asimmetria degli agenti
- [goal](kb/goal.md) — Gerarchia motivo/goal/operazione (Leontiev): il goal come confine aperto di Norman; KB informa il goal senza generarlo
- [development-goal](kb/development-goal.md) — Il polo Goal del ciclo di sviluppo: dimensioni comuni (attrito, autonomia, temporalità) e posizione auspicata; il dominio sceglie la gradualità, non le dimensioni
- [world](kb/world.md) — Membrana fisica non versionata al fondo del ciclo; i1 e o3 sono i suoi riflessi versionati on-demand
- [nested-cycles](kb/nested-cycles.md) — I due cicli annidati (sviluppo e runtime) e i loro due Mondi; la cucitura per cui il Mondo di sviluppo diventa macchina del runtime, contro l'appiattimento in parallelismo
- [action-cycle-matrix](kb/action-cycle-matrix.md) — Verifica a 40 caselle (6 atti + 2 poli × 5 artefatti) più l'asse annidamento dev/runtime aperto in dogfooding sulle 16 celle di `metodo`, con verdetto solido/debole/forzato/vuoto contro l'auto-accondiscendenza
- [output](kb/output.md) — Nota-struttura dell'arco di esecuzione: conflitto Zettelkasten/Karpathy, le tre altitudini, o1 senza atomo, dati vs presentazione
- [input](kb/input.md) — Nota-struttura dell'arco di valutazione: i tre atomi, le due sorgenti di i1 e i due modi di i3, lo specchio con l'output
- [perceive](kb/perceive.md) — Stadio i1: cattura versionata e valenza-neutra; due tessiture; il confine i1→i2 è la valenza; on-demand
- [interpret](kb/interpret.md) — Stadio i2: il distillato dove l'interpretazione accade; serve un substrato; i2 micro/macro; `interpretations/` = i2
- [specify](kb/specify.md) — Stadio o2: la vista di decisione; la forma segue la domanda; o1/o2 due altitudini; le quattro proprietà cardine
- [perform](kb/perform.md) — Stadio o3: la prescrizione versionata dell'atto (o3 ≠ atto); on-demand; può far emergere Goal
- [compare](kb/compare.md) — Stadio i3: conoscenza formalizzata o verdetto; i due modi (verdetto/triage); chiude il ciclo verso il Goal
- [deck](kb/deck.md) — Runbook portabile del deck come forma navigabile di `interpretations/`: sorgente markdown unica, build Reveal da CDN, apertura locale e condivisione on-demand
- [connection](kb/connection.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta
- [pace-layering](kb/pace-layering.md) — Strati a frequenza di cambiamento diversa (Duffy, Brand): sostituisce «conoscenza stabile» come criterio di collocazione
- [method-development](kb/method-development.md) — I due movimenti (bottom-up e top-down) in alternanza e contraddittorio
- [consent](kb/consent.md) — Proporre, attendere consenso esplicito, non scambiare un sì parziale per un sì totale; gemello sul lato verifica

## Componenti della ricetta

- [agents](kb/agents.md) — Wrapper agent-agnostico: ingresso comune verso README e CLAUDE
- [claude](kb/claude.md) — Costituzione operativa per agenti: regole d'azione, vincoli e bootstrap
- [readme](kb/readme.md) — La bussola dell'artefatto: orienta e punta, non immagazzina; ingresso per umano e LLM
- [index](kb/index.md) — Catalogo statico dei nodi: recupero rapido distinto dalla mappa; nodo-concetto del register `kb.md`
- [map](kb/map.md) — Indice-di-dominio: il territorio reale (entità, sistemi, fonti) legato ai nodi; register root `map.md`, porta on-demand
- [plan](kb/plan.md) — Supervisione corrente del lavoro futuro: lo stadio Plan del ciclo di sviluppo; istanza root `plan.md`
- [tasks](kb/tasks.md) — Dettagli operativi e contesto dei singoli task aperti: la cartella `tasks/`, stadio Specify
- [verdict](kb/verdict.md) — Il verdetto attuale del progetto, per filo/area aperta: lo stadio Compare (i3) del ciclo di sviluppo; istanza root `verdict.md`, aggiornata in place
- [git-history](kb/git-history.md) — Storia verificabile dei cambiamenti e dei diff
- [skill](kb/skill.md) — Workflow ricorrenti codificati per agenti
- [source-of-truth](kb/source-of-truth.md) — Fonti contro cui verificare ciò che la KB dice
