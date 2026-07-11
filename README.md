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

Lo sviluppo del metodo procede per due movimenti in alternanza ([method-development](kb/method-development.md)). Dal basso, un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Dall'alto, una cornice teorica importata — un gigante, una distinzione — dà forma a ciò che dal basso si avverte come disagio ma non si sa ancora inquadrare. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione, non l'unica regola. Il dall'alto ha pari dignità su due fronti: importa le cornici teoriche che danno forma al metodo, e — sul lato runtime — pianifica il proprio output di canone, le prescrizioni e le convergenze che disegnano come gli artefatti adottanti dovrebbero diventare, che l'adottante poi recepisce eseguendole. Ciò che questo repo non fa è micromanagiare la coda interna degli adottanti: custodisce il metodo emerso dall'uso reale e le cornici che lo reggono, e prescrive il proprio canone senza sostituirsi alle loro code operative.

## Il dominio in breve

Il dominio di questo repo è il metodo stesso. Come meta-artefatto ha due facce del [world](kb/world.md): il Mondo runtime sono i quattro progetti adottanti più le fonti teoriche su `gdrive/` — da lì emergono esigenza dal basso e pavimento concettuale, e lì torna la propagazione — mentre il Mondo di sviluppo sono i nodi `kb/` e la loro coerenza, non codice o dati. Il metodo si inscrive in una cornice di augmentation ([augmentation-system](kb/augmentation-system.md), l'H-LAM/T di Engelbart) che _contiene_ i suoi riferimenti — [zettelkasten](kb/zettelkasten.md) (l'unità atomica), [action-cycle](kb/action-cycle.md) (l'interfaccia col Mondo), e [karpathy-pattern](kb/karpathy-pattern.md) come istanza contemporanea della gamba di manutenzione — e poggia su un'ontologia a tre piani: artefatto, sistema, metodo ([cognitive-artifact](kb/cognitive-artifact.md), [cognitive-system](kb/cognitive-system.md), col pavimento Hutchins/Clark). I principi guida vivono in [design-principles](kb/design-principles.md). Il modello completo e illustrato vive in [i2/metodo-in-sintesi.md](i2/metodo-in-sintesi.md); il dettaglio concettuale nei nodi. Questo README **orienta e punta**: non ripete né il modello né il catalogo.

## Metodo

Questo è il repository **canonico** del metodo: non lo adotta, lo custodisce. I
repo adottanti leggono i nodi canonici via il loro symlink `method/`; qui il
territorio e le superfici sono dichiarati nel register [`world.md`](world.md)
e la superficie Drive delle fonti vive come `gdrive/` gitignorato, non come
`world/`. L'hub d'ingresso è
[`cognitive-artifact-design.md`](kb/cognitive-artifact-design.md), il solo nome
di nodo assunto stabile come punto d'aggancio. Questa è la **sezione README
canonica** ([readme](kb/readme.md)) — comune ai cinque repo: dichiara l'adozione
e punta ai due poli, che vivono nei register di root — [`goal.md`](goal.md) (il
nord: obiettivi, segnali, lavoro corrente) e [`world.md`](world.md) (il
territorio: i quattro adottanti, le superfici della membrana, le fonti) — da
cui la home ricava i poli Goal e World rendendone l'intro.

## Orientarsi

La root è l'atrio dell'artefatto: un `ls` ne dichiara l'anatomia, e l'anatomia **è il ciclo stesso**. Le sei collezioni-stadio portano il codice del loro stadio ([project-structure](kb/project-structure.md)); ogni item dichiara nel frontmatter la facet `ciclo: dev|runtime`, letta dal Mondo su cui l'item insiste — artefatto → `dev`, adottanti → `runtime` — dentro la relazione tra runtime cycle e development meta-cycle ([development-meta-cycle](kb/development-meta-cycle.md)).

**Collezioni-stadio** — le sei stanze del ciclo, ciascuna col proprio indice interno:

- **[i1/](i1/perceptions.md)** — Perceive: i segnali catturati valenza-neutri (indice `perceptions.md`)
- **[i2/](i2/interpretations.md)** — Interpret: le sintesi sorgente (indice `interpretations.md`)
- **[i3/](i3/verdicts.md)** — Compare: un file per filo aperto, aggiornato in place (indice `verdicts.md`)
- **[o1/](o1/plan.md)** — Plan: i task aperti, prioritizzati, con dipendenze e ciclo (`plan.md`)
- **[o2/](o2/tasks.md)** — Specify: i dettagli e il contesto dei task aperti (indice `tasks.md`)
- **[o3/](o3/prescriptions.md)** — Perform: i runbook di propagazione e gli **esecutori deterministici**, gli strumenti registrati nell'indice (`prescriptions.md`)

**Le due ali fuori dal ciclo** — trasversali agli stadi:

- **[kb/](kb/kb.md)** — il nucleo di conoscenza formalizzata della system image; il catalogo è l'indice interno omonimo [`kb/kb.md`](kb/kb.md)
- **[presentation/](presentation/)** — la superficie presentativa: `index.html` (la home della system image), le viste generate e gli asset condivisi

**Register dei poli** — puntano _fuori_ dall'artefatto, ai due confini del ciclo:

- **[goal.md](goal.md)** — il polo superiore: il nord declinato in obiettivi, ognuno coi segnali che lo misurano e il lavoro corrente che lo serve; custode umano ([goal](kb/goal.md))
- **[world.md](world.md)** — il polo inferiore: il territorio (i quattro adottanti), le superfici della membrana e la provenienza delle fonti-mondo autorevoli, base dei `## Riferimenti` (i3) ([world](kb/world.md))

Il cruscotto di lavoro è la coppia [`o1/plan.md`](o1/plan.md) (lato esecuzione: i task aperti) e [`i3/`](i3/verdicts.md) (lato valutazione: i verdetti aperti). L'ordine di bootstrap è `README → CLAUDE → nodo`.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (o1/o2/o3) e input (i1/i2/i3), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro; il battito è l'audit mensile `/adopters-review` (runtime-o1), col verdetto aggregato in [`i3/audit-adottanti.md`](i3/audit-adottanti.md).
- **Strumenti comuni**: `o3/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura del catalogo, migrazione, candidati terminologici e segnali generici sui progetti code-based. Il quartetto operativo — `/kb-review`, `/plan-review`, `/verdicts-review`, `/commit` — e la skill di allineamento `/method-review` vivono in `.claude/skills/` (con wrapper Codex in `.codex/skills/`): `metodo` fa dogfooding ed è la copia canonica che gli adottanti forkano.
- **Manutenzione propria del metodo**: task in `o2/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Presentazione**: [`presentation/`](presentation/) raccoglie l'intera superficie presentativa. [`presentation/index.html`](presentation/index.html) è la home statica della system image, generata da `README.md`, dai register `goal.md`/`world.md` (l'intro di ciascuno è il polo) e da `o1/plan.md` con `o3/build-system-image.sh`; apre il ciclo Goal/Plan/Specify/Compare/Interpret/World e punta alle viste. [`i2/`](i2/interpretations.md) è la collezione sorgente dello stadio i2; [`i2/metodo-in-sintesi.md`](i2/metodo-in-sintesi.md) ne è la sintesi principale — i diagrammi che reggono il metodo intero. Il `.md` è la fonte unica; `o3/build-presentation.sh` genera `presentation/interpretations.html`, la vista navigabile a slide della collezione, apribile direttamente dal checkout. Lo stesso script genera `presentation/tasks.html` e `presentation/verdict.html`; gli asset comuni stanno in `presentation/assets/`. Il PDF per stampa/distribuzione (o3) esce dall'export della vista a slide e non viene versionato.

## Come collegare un nuovo progetto

I progetti adottanti sono il Mondo runtime, indicizzati nel register
[`world.md`](world.md). Per collegarne uno nuovo:

1. Crea il symlink `method/` verso i nodi canonici: `ln -s ../method/kb method`
   dalla root del progetto, e aggiungilo al register `world.md` di `metodo`.
2. Scrivi la **sezione README canonica** ([readme](kb/readme.md)): `## Metodo`
   con la dichiarazione di adozione, il symlink `method/` e i puntatori ai due
   register dei poli — poi crea `goal.md` e `world.md` del dominio ([goal](kb/goal.md),
   [world](kb/world.md)): l'intro di ciascuno è il polo in sintesi che la home
   rende. È la dichiarazione _una-volta_ della dipendenza generale dal metodo.
3. Aggancia il metodo all'hub
   [`cognitive-artifact-design.md`](kb/cognitive-artifact-design.md), unico nome
   di nodo assunto stabile, e aggiungi la sezione con i principi specifici del
   progetto. **Non** replicare in `CLAUDE.md` un inventario di path interni del
   metodo: collega un nodo solo dove una regola o uno strumento locale dipende
   davvero da quella specifica — dipendenza intenzionale, non accidentale (cfr.
   [method-development](kb/method-development.md), «Il confine canone↔adottante:
   dichiara e taci»).
4. Dichiara gli strati input/output e le superfici della membrana del dominio
   in `world.md`; crea symlink o mount host-local solo quando il progetto viene
   messo in uso, con nomi fisici descrittivi.
