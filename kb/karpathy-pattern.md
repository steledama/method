---
stato: maturo
---

# Karpathy pattern

Il pattern Karpathy per le knowledge base con LLM descrive un modo di usare l'LLM non come motore di recupero occasionale, ma come manutentore di un artefatto persistente. La differenza rispetto al RAG classico è decisiva: nel RAG la conoscenza viene recuperata e ricomposta a ogni domanda; nel pattern Karpathy viene compilata una volta in una rete di file markdown, poi mantenuta, corretta e arricchita nel tempo.

**Istanza, non pilastro.** Lo _slot funzionale_ che questo pattern occupa è reale — il _chi mantiene_ la KB, la gamba di manutenzione e rigenerazione — ma non è un gigante al pari di Luhmann e Norman: accostarlo a loro era un'asimmetria di pedigree, perché il suo contributo sulla questione è un post, un pattern influente del presente, non una tradizione di pensiero. Quello slot ha un gigante che precede Karpathy di sessant'anni: è il _Methodology/Training_ della cornice H-LAM/T di Engelbart, la gamba di manutenzione di un sistema di augmentation co-evolvente (cfr. `augmentation-system`). Il pattern Karpathy ne è l'**istanza contemporanea per l'era LLM** — il _come si tiene aggiornato_ il sistema oggi — non il pilastro. Il pavimento _ontologico_ della stessa gamba — perché un artefatto esterno conti come cognizione — è invece di Hutchins/Clark (cfr. `cognitive-system`), un peso teorico altrui di cui Karpathy era stato sovraccaricato.

La knowledge base diventa così uno strato intermedio tra le fonti grezze e le domande future. Quando entra una nuova fonte, l'LLM non si limita a indicizzarla: la legge, ne estrae i concetti, aggiorna i nodi esistenti, crea quelli mancanti, segnala tensioni o contraddizioni, rafforza le connessioni. La conoscenza non resta dispersa nella chat o nei documenti originali, ma si accumula in un corpo navigabile e versionato.

In questa KB il pattern Karpathy è adattato in forma più autoriale: l'LLM non scrive tutto in autonomia, ma assiste l'utente nella manutenzione. L'umano mantiene la responsabilità del senso, della direzione e dello stile; l'LLM prende in carico il lavoro ripetitivo e strutturale: cross-reference, footer Connessioni, audit, aggiornamento dell'indice, filing back delle sintesi utili.

Il pattern originale di Karpathy include summary pages e viste d'insieme dentro il wiki, mantenute dall'LLM. Nel metodo questa scelta diverge deliberatamente: le sintesi escono da `kb/` e vanno nello strato output, così i nodi restano atomici secondo la disciplina zettelkastiana. Questa tensione tra Zettelkasten (sintesi fuori dai nodi) e Karpathy (sintesi dentro il wiki), e la sua risoluzione strutturale, sono trattate in `output`. Dentro la stessa cornice di sistema, Norman descrive come l'utente attraversa il ciclo di azione dal Goal al mondo e ritorno come nuova fonte (cfr. `action-cycle`).

Karpathy aggiunge un secondo principio sull'output, che il metodo adotta: la forma della risposta segue la domanda. «Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas». L'output non è monolitico: pagina, tabella, deck di slide, grafico, canvas sono forme alternative, scelte secondo cosa la risposta deve far capire o decidere. Nel metodo questo dà il repertorio dello strato o2 — il deck di slide ne è la forma-default per la sintesi che si scorre, non l'unica (cfr. `output`, `deck`).

Architettura:

- fonti: materiali grezzi o elaborati che alimentano la KB, conservati separatamente dai nodi atomici
- nodi: unità concettuali compilate a partire dalle fonti, dalle riflessioni e dalle sessioni di lavoro
- schema operativo: istruzioni, convenzioni e skill che insegnano all'LLM come mantenere il progetto
- indice: catalogo statico in `kb/kb.md` che orienta umano e LLM nella rete dei nodi
- verdict: il verdetto attuale per filo/area aperta, aggiornato in place nei file `i3/` — la cronologia è il git history del file
- strumenti: script versionati che rendono deterministici i controlli meccanici
- task: lavoro futuro tracciato in `o1/plan.md` e dettagliato in `o2/`, separato dalla conoscenza stabile
- wrapper agent: AGENTS.md e .codex/skills quando servono più agenti sullo stesso progetto

Operazioni:

- ingest: una fonte entra nel sistema, viene sintetizzata, trasformata in nodi o usata per aggiornare nodi esistenti
- query: una domanda attraversa la KB e può produrre una risposta temporanea o un nuovo nodo stabile
- lint: la KB viene controllata periodicamente per link rotti, orfani, concetti mancanti, cluster isolati e incoerenze
- filing back: le sintesi nate in chat non restano effimere ma vengono riportate nella KB quando hanno valore durevole

Ciclo di bootstrap:

- l'agente legge README.md per orientamento; il catalogo in `kb/kb.md`, i task in `o1/plan.md`
- l'agente legge CLAUDE.md per regole operative e comandi sicuri
- l'agente apre solo i nodi necessari alla domanda o al task corrente
- l'agente usa `o3/kb_tools.py` per controlli strutturali invece di improvvisare parser
- l'agente propone filing back quando una conversazione produce conoscenza durevole
- l'agente aggiorna README, fili `i3/`, `o1/plan.md`/`o2/` e nodi solo secondo il ruolo di ciascun file

Differenze rispetto al RAG:

- il RAG recupera frammenti al momento della domanda; il pattern Karpathy consolida conoscenza prima della domanda futura
- il RAG non accumula necessariamente comprensione; la KB cresce e si modifica a ogni ingest, query e lint
- il RAG tratta le fonti come deposito; la KB le trasforma in una rete di concetti già collegati
- il RAG privilegia la risposta; il pattern Karpathy privilegia la costruzione progressiva dell'artefatto

Rischi:

- accumulo meccanico di nodi senza reale comprensione
- eccessiva delega all'LLM con perdita dell'authorship umana
- struttura operativa troppo pesante rispetto al valore dei contenuti
- falsa precisione dei controlli automatici: gli script trovano problemi strutturali, non decidono il significato

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [augmentation-system](augmentation-system.md)
- [knowledge-base](knowledge-base.md)
- [zettelkasten](zettelkasten.md)
- [node](node.md)
- [project-structure](project-structure.md)
- [kb-tools](kb-tools.md)
- [connection](connection.md)
- [output](output.md)
- [view](view.md)
- [action-cycle](action-cycle.md)
