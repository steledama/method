# Cognizione condivisa

Framework metodologico e osservatorio cross-repo per il _cognitive artifact
design_: la progettazione di artefatti cognitivi che sostengono la cognizione
condivisa tra umano e modelli di intelligenza artificiale lungo l'intero ciclo
d'azione.

Questo repository ha due funzioni complementari. La prima è custodire il metodo
portabile: KB riflessiva, strati input/output, membrana `world`, struttura di
progetto, strumenti, principi guida e ciclo di lavoro. La seconda è osservare
come il metodo viene applicato nei progetti adottanti, confrontando artefatti,
componenti, strumenti, skill, nodi, task e segnali di salute.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale —
principi, anatomia dell'artefatto e ciclo operativo — mentre le
personalizzazioni sono esplicite: ogni progetto estende il metodo con Goal,
Mondo, fonti di verità, rappresentazioni e strumenti propri del dominio. Le
differenze tra progetti non sono rumore: sono materiale di analisi per capire
cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo alterna esigenze emerse dagli adottanti e cornici teoriche che
aiutano a interpretarle. Il canone torna ai progetti come conoscenza e
prescrizioni, mentre ciascun adottante governa la propria coda. Il criterio e i
confini di questi movimenti vivono in
[method-development](kb/method-development.md).

## Il dominio in breve

Il dominio è il metodo stesso. Il suo Mondo runtime comprende i progetti
adottanti e le fonti teoriche dichiarati in [world.md](world.md); il Mondo di
sviluppo è l'artefatto che custodisce il canone, con i nodi `kb/` al centro.

Progettiamo l'artefatto persistente perché sostenga il sistema cognitivo che
nasce nell'uso con umano e agenti. Per questa distinzione e i fondamenti si
parte dall'hub [cognitive-artifact-design](kb/cognitive-artifact-design.md). Il
modello illustrato vive in [i2/metodo-in-sintesi.md](i2/metodo-in-sintesi.md), i
criteri progettuali in [design-principles](kb/design-principles.md).

## Metodo

Questo è il repository **canonico** del metodo: non lo adotta, lo custodisce. I
repo adottanti leggono i nodi canonici via il loro symlink `method/`; qui il
territorio e le superfici sono dichiarati nel register [`world.md`](world.md) e
la superficie Drive delle fonti vive come `gdrive/` gitignorato, non come
`world/`. L'hub d'ingresso è
[`cognitive-artifact-design.md`](kb/cognitive-artifact-design.md), il solo nome
di nodo assunto stabile come punto d'aggancio. Questa è la **sezione README
canonica** ([readme](kb/readme.md)) — comune ai sette repo: dichiara l'adozione
e punta ai due poli, che vivono nei register di root — [`goal.md`](goal.md) (il
nord: obiettivi, segnali, lavoro corrente) e [`world.md`](world.md) (il
territorio: i sei adottanti, le superfici della membrana, le fonti) — da cui la
home ricava i poli Goal e World rendendone l'intro.

## Orientarsi

La root rende visibile la struttura del progetto
([project-structure](kb/project-structure.md)). Le sei collezioni portano il
codice del loro stadio; ogni item dichiara nel frontmatter la facet
`ciclo: dev|runtime`, letta dal Mondo su cui insiste — artefatto → `dev`,
adottanti → `runtime` — dentro la relazione tra runtime cycle e development
meta-cycle ([development-meta-cycle](kb/development-meta-cycle.md)).

**Collezioni del ciclo**, ciascuna col proprio indice:

- **[i1/](i1/perceptions.md)** — Perceive: i segnali catturati valenza-neutri
  (indice `perceptions.md`)
- **[i2/](i2/interpretations.md)** — Interpret: le sintesi sorgente (indice
  `interpretations.md`)
- **[i3/](i3/verdicts.md)** — Compare: un file per filo aperto, aggiornato in
  place (indice `verdicts.md`)
- **[o1/](o1/plan.md)** — Plan: i task aperti, prioritizzati, con dipendenze e
  ciclo (`plan.md`)
- **[o2/](o2/tasks.md)** — Specify: i dettagli e il contesto dei task aperti
  (indice `tasks.md`)
- **[o3/](o3/prescriptions.md)** — Perform: i runbook di propagazione e gli
  **esecutori deterministici**, gli strumenti registrati nell'indice
  (`prescriptions.md`)

**Componenti trasversali**:

- **[kb/](kb/kb.md)** — il nucleo di conoscenza formalizzata della system image;
  il catalogo è l'indice interno omonimo [`kb/kb.md`](kb/kb.md)
- **[presentation/](presentation/)** — la superficie presentativa: `index.html`
  (la home della system image), le viste generate e gli asset condivisi

**Register dei poli** — puntano _fuori_ dall'artefatto, ai due confini del
ciclo:

- **[goal.md](goal.md)** — il polo superiore: il nord declinato in obiettivi,
  ognuno coi segnali che lo misurano e il lavoro corrente che lo serve; custode
  umano ([goal](kb/goal.md))
- **[world.md](world.md)** — il polo inferiore: il territorio (i sei adottanti),
  le superfici della membrana e la provenienza delle fonti-mondo autorevoli,
  base dei `## Riferimenti` (i3) ([world](kb/world.md))

Il cruscotto di lavoro è la coppia [`o1/plan.md`](o1/plan.md) (lato esecuzione:
i task aperti) e [`i3/`](i3/verdicts.md) (lato valutazione: i verdetti aperti).
L'ordine di bootstrap è `README → CLAUDE → nodo`.

## Funzioni del repo

- **Metodo portabile** — il modello e la ricetta vivono nei nodi indicizzati da
  [`kb/kb.md`](kb/kb.md).
- **Osservatorio cross-repo** — il protocollo vive in
  [`method-observatory`](kb/method-observatory.md); il verdetto corrente in
  [`i3/audit-adottanti.md`](i3/audit-adottanti.md).
- **Strumenti comuni** — esecutori e runbook sono registrati in
  [`o3/prescriptions.md`](o3/prescriptions.md); capacità e limiti in
  [`kb-tools`](kb/kb-tools.md) e [`skill`](kb/skill.md).
- **Presentazione** — le viste generate vivono in
  [`presentation/`](presentation/) e la disciplina della derivazione in
  [`view`](kb/view.md).

## Come collegare un nuovo progetto

I progetti adottanti sono il Mondo runtime, indicizzati nel register
[`world.md`](world.md). Il protocollo d'ingresso vive in
[`method-observatory`](kb/method-observatory.md); la forma della sezione Metodo,
dei due register e delle connessioni intenzionali vive in
[`readme`](kb/readme.md), [`goal-register`](kb/goal-register.md),
[`world-register`](kb/world-register.md) e
[`method-development`](kb/method-development.md).
