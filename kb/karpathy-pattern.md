---
stato: maturo
---

# Karpathy pattern

Il pattern Karpathy è il nome operativo con cui il metodo indica la manutenzione
di una KB persistente assistita dall'LLM: le fonti vengono interpretate e
integrate in nodi che si correggono e si collegano nel tempo. La provenienza
originaria del nome non ha ancora una fonte primaria identificata nel register
`world.md`. Questo nodo descrive quindi una formalizzazione locale, non
attribuisce a Karpathy le singole regole.

La funzione del pattern è mantenere il sistema di conoscenza. Il metodo la legge
nella cornice di augmentation di Engelbart (`augmentation-system`), come
applicazione contemporanea di metodologia e apprendimento nell'uso. La cornice
teorica e questa pratica locale hanno responsabilità distinte.

Quando entra una fonte, l'LLM ne estrae i concetti, aggiorna i nodi pertinenti,
segnala tensioni e propone nuove unità soltanto quando hanno una funzione
autonoma. L'umano custodisce senso, direzione e stile; l'agente opera entro
l'autorità concessa. La conoscenza utile non resta dispersa nella chat.

La collocazione segue la funzione: le sintesi interpretative vivono in `i2/`, le
specifiche che preparano una decisione in `o2/`, le rappresentazioni derivate in
`presentation/`. Nella KB risale la conoscenza riusabile, anche quando nasce da
una sintesi. L'atomicità limita le responsabilità del nodo, non vieta di
integrare più fonti sullo stesso concetto.

La forma segue la domanda: testo, tabella, grafico, slide o canvas si scelgono
per ciò che devono rendere comprensibile. Una vista a slide è adatta a una
sintesi da scorrere, senza essere il default di ogni specifica (`view`).

Operazioni:

- ingest: una fonte entra nel sistema, viene sintetizzata, trasformata in nodi o
  usata per aggiornare nodi esistenti
- query: una domanda attraversa la KB e può produrre una risposta temporanea o
  un nuovo nodo stabile
- lint: la KB viene controllata periodicamente per link rotti, orfani, concetti
  mancanti, cluster isolati e incoerenze
- filing back: le sintesi nate in chat non restano effimere ma vengono riportate
  nella KB quando hanno valore durevole

Rapporto con il recupero delle fonti:

- il recupero al momento della domanda e la manutenzione di conoscenza
  persistente sono funzioni complementari;
- una KB interpretata non sostituisce le fonti: le affermazioni ad alta deriva
  devono restare verificabili;
- la risposta di sessione diventa conoscenza condivisa solo dopo averne valutato
  durata, collocazione e affidabilità.

Rischi:

- accumulo meccanico di nodi senza reale comprensione
- eccessiva delega all'LLM con perdita dell'authorship umana
- struttura operativa troppo pesante rispetto al valore dei contenuti
- falsa precisione dei controlli automatici: gli script trovano problemi
  strutturali, non decidono il significato

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
