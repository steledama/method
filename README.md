# Metodo KB

Framework metodologico e osservatorio cross-repo per knowledge base personali e professionali mantenute con LLM.

Questo repository ha due funzioni complementari. La prima è custodire il metodo portabile: forma dei nodi, struttura di progetto, strumenti di manutenzione, principi guida e ciclo di lavoro. La seconda è osservare come il metodo viene applicato nei progetti adottanti, confrontando componenti, strumenti, skill, nodi, task e segnali di salute delle KB.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale — principi, struttura KB, ciclo operativo — mentre le personalizzazioni sono esplicite: ogni progetto estende il metodo con principi, fonti di verità e strumenti propri del dominio. Le differenze tra progetti non sono rumore: sono materiale di analisi per capire cosa generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Lo sviluppo del metodo è bottom-up: un'esigenza nasce in un repo adottante mentre si risolve un problema concreto, viene stabilizzata localmente, poi viene riportata qui solo se diventa una generalizzazione portabile. Questo repo non orchestra task sui progetti adottanti; custodisce il metodo emerso dall'uso reale.

## Orientarsi

La root è il cruscotto del ciclo di sviluppo, letto a ogni sessione:

- **[map.md](map.md)** — il modello del dominio (l'o2 conciso): ontologia, i tre giganti, gli strati, il layout
- **[plan.md](plan.md)** — lo stadio Plan: i task aperti, prioritizzati, con dipendenze
- **[kb/index.md](kb/index.md)** — il catalogo di tutti i nodi, consultato on-demand
- **[why.md](why.md)** — la memoria interpretativa: perché le decisioni contano
- **CLAUDE.md** / **AGENTS.md** — le regole operative

L'ordine di bootstrap è `README → map → CLAUDE → nodo`.

## Funzioni del repo

- **Metodo portabile**: nodi in `kb/` che descrivono ricetta metodologica, i tre giganti del metodo (Zettelkasten, pattern Karpathy, ciclo di azione di Norman), struttura di progetto, strato output (o1/o2/o3) e input (i1/i2/i3), strumenti, fedeltà cognitiva e principi.
- **Osservatorio cross-repo**: confronto periodico tra i progetti adottanti per leggere convergenze, drift, duplicazioni, lacune e specificità locali senza sostituirsi alla loro coda di lavoro.
- **Strumenti comuni**: `scripts/kb_tools.py` come backend portabile per audit strutturale, backlink, copertura del catalogo, migrazione, candidati terminologici e segnali generici sui progetti code-based.
- **Manutenzione propria del metodo**: task in `tasks/` solo quando riguardano questo repo, la sua presentazione, la coerenza dei nodi o una generalizzazione già emersa dai repo adottanti.
- **Strato output**: [`presentation/metodo-in-sintesi.md`](presentation/metodo-in-sintesi.md) è l'o2/o3 del repo — i diagrammi che reggono il metodo intero, dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo dell'azione come specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al processo (anatomia, sviluppo, routing). La sintesi vive qui, non nei nodi. Il `.md` è la fonte unica; il PDF per stampa/distribuzione (o3) si rigenera con `cd presentation && md2pdf metodo-in-sintesi.md` e non viene versionato.

## Progetti adottanti

| Progetto                 | Ambito                                                |
| ------------------------ | ----------------------------------------------------- |
| [nixos](../nixos/)       | Configurazione dichiarativa NixOS multi-host          |
| [bi](../bi/)             | Business intelligence e sincronizzazione dati         |
| [economia](../economia/) | Gestione finanziaria, patrimoniale e legale personale |
| [salute](../salute/)     | Benessere, pratica, filosofia e salute personale      |

## Come collegare un nuovo progetto

1. Crea il symlink: `ln -s ../metodo/kb metodo` dalla root del progetto.
2. Aggiungi una riga alla tabella dei progetti adottanti.
3. Nel README del progetto, referenzia `metodo/metodo-kb.md` come nodo centrale del metodo e aggiungi una sezione con i principi specifici del progetto.
4. Aggiorna i path in `CLAUDE.md` del progetto: `kb/metodo-kb.md` → `metodo/metodo-kb.md` (e analogamente per gli altri nodi metodologici).
