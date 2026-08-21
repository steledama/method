---
stato: maturo
---

# Project structure

La struttura rende visibili le funzioni dell'artefatto e colloca ogni file nel
luogo in cui viene usato. I nomi standard permettono a umano e agente di
orientarsi allo stesso modo nei diversi progetti; il contenuto resta specifico
del dominio.

## Componenti

- `README.md` — orientamento al dominio e accesso al cruscotto;
- `CLAUDE.md` — regole operative per agenti;
- `AGENTS.md` — wrapper agent-agnostico con ordine di lettura;
- `goal.md` — direzione, obiettivi e segnali;
- `world.md` — territorio, superfici esterne e fonti;
- `kb/` — conoscenza stabile, catalogata in `kb/kb.md`;
- `presentation/` — home, viste generate e asset;
- `i1/`, `i2/`, `i3/` — percezioni, interpretazioni e verdetti;
- `o1/`, `o2/`, `o3/` — piano, specifiche operative e prescrizioni/esecutori.

Le sei collezioni del ciclo hanno un indice interno:

- `i1/perceptions.md`;
- `i2/interpretations.md`;
- `i3/verdicts.md`;
- `o1/plan.md`;
- `o2/tasks.md`;
- `o3/prescriptions.md`.

`goal.md` e `world.md` sono register, non collezioni: sintetizzano i due
confini del ciclo e forniscono alla home le rispettive intro. `method/` espone
negli adottanti i nodi canonici tramite symlink. Le superfici esterne concrete
(`gdrive/`, mount, sync, servizi) sono dichiarate in `world.md`, gitignorate
quando locali e chiamate per ciò che sono.

## Criterio di collocazione

La collocazione segue la funzione:

- conoscenza durevole → `kb/`;
- segnale catturato → `i1/`;
- sintesi → `i2/`;
- verdetto aperto → `i3/`;
- supervisione del lavoro → `o1/plan.md`;
- dettaglio di un task aperto → `o2/`;
- prescrizione, runbook o esecutore → `o3/`;
- rappresentazione derivata → `presentation/`;
- contenuto che conserva significato senza l'artefatto → superficie dichiarata
  in `world.md`.

Il corpo applicativo o dichiarativo di un progetto può vivere in `o3/` quando
è ciò con cui l'artefatto agisce sul proprio Mondo. Le sottocartelle restano una
scelta del dominio.

I file che una toolchain richiede in root (`flake.nix`, `package.json`, lock e
dotfile) sono eccezioni tecniche. Cache, log e intermedi rigenerabili non si
versionano. Ogni altra eccezione deve avere una funzione distinta; se duplica
README, CLAUDE, un register, un indice o un nodo, va rimossa o ricollocata.

## Convenzioni

- file riconosciuti per nome da strumenti o agenti: `README.md`, `CLAUDE.md`,
  `AGENTS.md`;
- nomi strutturali e register in lowercase;
- nodi `kb/` in inglese, lowercase, singolare e con trattini;
- nodi `kb/*.md`: frontmatter `stato` e footer `Connessioni:`;
- item delle collezioni: frontmatter `ciclo: dev|runtime`;
- task `o2/`: frontmatter `sintesi` e `ciclo`;
- README, CLAUDE, AGENTS, register e indici: nessun frontmatter;
- `o1/plan.md` fa eccezione perché è insieme indice e item corrente del Plan.

La forma dettagliata dei singoli componenti vive nei nodi dedicati (`readme`,
`claude`, `agents`, `goal`, `world`, `plan`, `tasks`, `verdict`). Questo nodo
non la replica.

## Bootstrap

Ordine di lettura: `README → CLAUDE → nodo pertinente`. Piano, fili, register e
catalogo si aprono quando il lavoro li richiede. La posizione nella root rende
un file reperibile; non implica che debba essere letto in ogni sessione.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [readme](readme.md)
- [claude](claude.md)
- [agents](agents.md)
- [goal](goal.md)
- [world](world.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [system-image](system-image.md)
