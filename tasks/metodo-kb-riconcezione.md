---
data: 2026-06-13
stato: aperto
---

# Rinominare e riconcepire l'hub `metodo-kb`

`kb/metodo-kb.md` è l'hub maturo (la ricetta generale, «qual è la ricetta
generale?»), ma nome e incipit sono **riduttivi**. La KB è solo lo strato
**riflessivo** — una delle tre altitudini. Il metodo che si delinea è il _design
di artefatti cognitivi per la cognizione condivisa umano-LLM_, esteso a tutto il
ciclo d'azione (archi input/output, membrana `world`, gradiente di autonomia).
Chiamarlo "knowledge base" nomina la parte per il tutto.

Non è un rename, è **rename + riconcezione**: l'incipit del nodo (_«il modo
operativo con cui una knowledge base personale viene costruita, mantenuta e resa
navigabile…»_) è esattamente la cornice riduttiva da riallineare all'identità
matura.

## Nome

Nome scelto: **`cognitive-artifact-design`** — nomina l'attività (progettare
artefatti cognitivi); calza con la funzione-ricetta dell'hub e con la linea
Norman. Cautela in esecuzione: tenerlo distinto dal nodo-concetto
`artefatto-cognitivo` (uno è "cos'è", l'hub è "come si progetta").

Scartati: `shared-cognition` (legge come concetto, si sovrappone a
`sistema-cognitivo`), `artifact-design` (generico), `cognitive-artifact-method`
(ridondante: un nodo "method" dentro il repo "method").

## Deliverable

- **rename** `kb/metodo-kb.md` → `kb/cognitive-artifact-design.md`; aggiornare
  **tutti** i backlink
  (è l'hub: la quasi totalità dei nodi lo cita, più i `CLAUDE.md`/`README.md`
  degli adottanti — cfr. regola di propagazione rename in `CLAUDE.md`).
- **riconcepire l'incipit**: dal "modo di costruire una KB" al "design di
  artefatti cognitivi per la cognizione condivisa umano-LLM", con la KB come
  strato riflessivo dentro il ciclo d'azione completo (archi, membrana `world`,
  gradiente di autonomia). Il resto della ricetta resta valido; cambia la
  cornice che la introduce.
- aggiornare il catalogo `README.md`/`kb.md` e l'eventuale auto-citazione
  nell'indice cognitivo del nodo («Metodo KB: qual è la ricetta generale?»).

## Dipendenza

Dipende da `tasks/world-membrana.md` (#1): l'hub deve **riflettere** il modello
del ciclo già consolidato (world, o3, processing-layers), non anticiparlo.

Connessioni:

- [metodo-kb](../kb/metodo-kb.md)
- [artefatto-cognitivo](../kb/artefatto-cognitivo.md)
- [sistema-cognitivo](../kb/sistema-cognitivo.md)
- [knowledge-base](../kb/knowledge-base.md)
- [ciclo-azione](../kb/ciclo-azione.md)
