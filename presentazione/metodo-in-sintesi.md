# Il metodo in sintesi

Strato output (L2) del repo `metodo`: la vista d'insieme leggibile a colpo d'occhio del metodo KB. Non è un nodo della KB — è la sintesi che, per la disciplina zettelkastiana, vive nel ponte e non nei nodi atomici. I cinque diagrammi reggono il metodo intero; il dettaglio sta nei nodi linkati in fondo.

## 1. I tre giganti

Tre pilastri che si dividono il lavoro in modo nitido: come è fatto il nodo, chi tiene aggiornato il sistema, come il sistema produce azione.

```mermaid
flowchart LR
    L["<b>Luhmann</b> · Zettelkasten<br/><br/>forma del nodo:<br/>atomico, interconnesso<br/>sintesi fuori dal nodo"]
    K["<b>Karpathy</b> · LLM KB<br/><br/>manutenzione dell'insieme:<br/>ingest · query · lint<br/>filing back"]
    N["<b>Norman</b> · ciclo di azione<br/><br/>interfaccia KB ↔ mondo:<br/>visibilità · feedback<br/>mapping · constraint"]
    M(["METODO KB"])
    L --> M
    K --> M
    N --> M
```

Karpathy risolve il "chi mantiene" che Luhmann non affronta; Norman risolve il "come l'utente agisce" che né Luhmann né Karpathy affrontano.

## 2. Il ciclo che si chiude attraverso l'azione

La KB non è il fine: è strumentale all'azione. Lo strato output traduce la conoscenza in azione possibile su tre livelli, e l'azione nel mondo ritorna come nuova fonte.

```mermaid
flowchart LR
    KB[("KB<br/>nodi atomici")]
    L1["<b>L1</b> · macchina<br/>JSON, dati, .nix"]
    L2["<b>L2</b> · decisione<br/>schemi, viste, slide"]
    L3{{"<b>L3</b> · azione nel mondo<br/>email, parole, gesti, transazioni"}}
    F["fonte di ritorno<br/>referto, paper trail, diario"]
    KB --> L1
    KB --> L2
    L2 --> L3
    L1 -.->|continua il lavoro tra sessioni| L2
    L3 --> F
    F -.->|filing back| KB
```

Solo L3 produce effetti reali; L1 e L2 sono strumentali. Senza strato output, la KB accumula conoscenza ma non chiude il ciclo.

## 3. Anatomia di un progetto

La struttura replicabile non è un albero identico: è la presenza esplicita delle funzioni cognitive. Ogni componente risponde a una domanda.

```mermaid
flowchart TB
    A["<b>AGENTS.md</b><br/><i>dove sono le istruzioni?</i>"]
    R["<b>README.md</b><br/><i>dove sono, da dove parto?</i>"]
    C["<b>CLAUDE.md</b><br/><i>come agisco qui?</i>"]
    MAP["<b>mappa</b><br/><i>come si tiene insieme il dominio?</i>"]
    KB["<b>kb/</b><br/><i>cosa significa questo concetto?</i>"]
    TODO["<b>todo/</b><br/><i>cosa devo fare adesso?</i>"]
    LOG["<b>log.md</b><br/><i>perché una decisione conta?</i>"]
    S["<b>scripts/ · skill</b><br/><i>quali controlli e workflow?</i>"]
    OUT["<b>strato output (ponte)</b><br/><i>come traduco la KB in azione?</i>"]

    A --> R
    R --> C
    R --> MAP
    R --> TODO
    MAP --> KB
    C --> S
    KB --> OUT
    OUT --> LOG
    TODO --> LOG
```

## 4. Sviluppo bottom-up del metodo

Il metodo non si decreta dall'alto: emerge dall'uso reale. `metodo` custodisce le generalizzazioni, non orchestra i repo.

```mermaid
flowchart LR
    P["esigenza concreta<br/>in un repo adottante"]
    S["soluzione locale<br/>task · log · nodi"]
    G{"è<br/>generalizzabile?"}
    M["filing back in metodo<br/>nodo · regola · strumento"]
    PR["altri repo leggono i commit<br/>e applicano il pertinente"]
    L["resta lavoro locale"]
    P --> S --> G
    G -->|sì| M --> PR
    G -->|no| L
```

## 5. Dove vive cosa

La regola di routing che tiene puliti i confini tra i componenti.

```mermaid
flowchart TB
    Q{"che tipo di<br/>contenuto?"}
    Q -->|concetto stabile e riusabile| KB["kb/"]
    Q -->|lavoro futuro| TODO["README + todo/"]
    Q -->|perché una decisione conta| LOG["log.md"]
    Q -->|come agire / workflow| OP["CLAUDE.md · skill"]
    Q -->|orientamento e indice| R["README.md"]
    Q -->|sintesi · vista · dashboard| OUT["strato output (ponte)"]
```

## Lo strato output di questo repo

Dichiarazione minima del ponte del repo `metodo`, applicata a sé stesso:

- **L1 macchina**: `kb/` in markdown consumato dagli LLM via symlink; output di `scripts/kb_tools.py` (audit JSON/markdown)
- **L2 decisione**: questo file — i cinque diagrammi del metodo in sintesi
- **L3 azione**: il metodo applicato nei quattro repo adottanti (nodi creati, commit, KB mantenute)
- **Fonte di ritorno**: l'osservatorio rilegge i repo adottanti e aggiorna `kb/confronto-progetti-adottanti.md`
- **Criterio di aggiornamento**: quando un gigante, un livello o un componente cambia nei nodi, qui si aggiorna il diagramma corrispondente

## Approfondimento

I diagrammi comprimono; i nodi spiegano.

- tre giganti → `kb/ciclo-azione.md`, `kb/zettelkasten.md`, `kb/pattern-karpathy.md`
- strato output e L1/L2/L3 → `kb/ponte.md`
- anatomia del progetto → `kb/struttura-progetto.md`
- sviluppo bottom-up e osservatorio → `kb/osservatorio-metodo.md`, `kb/metodo-kb.md`
- dove vive cosa → `kb/metodo-kb.md` (regole sullo stato), `kb/zettelkasten.md` (regola pratica)
