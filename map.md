# Map

Il modello del dominio di questo repo: come si tiene insieme il metodo. È la vista
o2 in root — letta a bootstrap dopo il README, prima di aprire un nodo — tenuta
concisa apposta. La sintesi ricca e illustrata (o3, per stampa e distribuzione) vive
in [`presentations/metodo-in-sintesi.md`](presentations/metodo-in-sintesi.md); qui sta
solo il modello, non lo spiegamento.

## Il dominio è il metodo stesso

Questo repo ha due funzioni: **custodire** il metodo portabile e **osservare** come
viene applicato nei progetti adottanti. Il «mondo» su cui agisce il ciclo non è
codice o dati, ma i nodi `kb/` e la loro coerenza.

## Ontologia — tre piani

- **Artefatto**: la KB come strumento cognitivo esterno che amplifica la mente.
- **Sistema**: l'accoppiamento dinamico artefatto + umano + LLM (Hutchins).
- **Metodo**: la ricetta portabile che tiene insieme i due — forma dei nodi,
  struttura di progetto, ciclo operativo.

## Fonti di verità — i tre giganti

Il metodo non è inventato: poggia su tre fonti contro cui si verificano le scelte.

- **Zettelkasten** — nodi atomici interconnessi, struttura emergente.
- **Pattern Karpathy** — wiki personale mantenuta da LLM: ingest, query, lint, filing back.
- **Ciclo dell'azione di Norman** — sette stadi, due gulf, le quattro proprietà cardine.

## Meccanica — gli strati e il ciclo

- **kb/** è il system image (lo strato riflessivo): porta il peso della comunicazione
  tra agenti che non si parlano. È la fonte di verità; le contraddizioni si risolvono qui.
- **strato output (o1/o2/o3) e input (i1/i2/i3)**: il cappio con due cerniere (Mondo
  e KB). In questo repo l'o2 è la presentazione; il Compare del ciclo di sviluppo si
  cristallizza lì come termometro.
- **il ciclo ritorna alla KB**: ogni azione valutata rientra come nuova fonte. Senza
  questo ritorno la mappa descriverebbe solo l'accumulo, non il ciclo completo.

## Layout — la root come atrio

La root è l'atrio dell'artefatto: l'`ls` ne dichiara l'inventario completo. Due specie di file ([struttura-progetto](kb/struttura-progetto.md)):

- **file-ciclo** (letti ogni sessione): `README.md` (Goal) · `map.md` (modello) · `plan.md` (Plan) · `CLAUDE.md`/`AGENTS.md` (regole) · `why.md` (memoria di valutazione)
- **porte-collezione** (viste sempre, aperte on-demand): `kb.md` (catalogo nodi) · `tools.md` (strumenti e skill) · `presentations.md` (o2/o3) · `sources.md` (manifest fonti i1)
- **collezioni**: `kb/` nodi · `tools/` strumenti · `presentations/` o2/o3 · `sources/` fonti grezze (i1) · `tasks/` dettagli dei task

## Accessi cognitivi

- per **capire il metodo**: [metodo-kb](kb/metodo-kb.md) → [struttura-progetto](kb/struttura-progetto.md) → [output](kb/output.md)
- per **i fondamenti**: [zettelkasten](kb/zettelkasten.md), [pattern-karpathy](kb/pattern-karpathy.md), [ciclo-azione](kb/ciclo-azione.md)
- per **i nodi tutti**: il catalogo in [kb.md](kb.md)
- per **lo stato del lavoro**: [plan.md](plan.md)
