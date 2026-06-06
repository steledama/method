---
title: "Metodo KB"
subtitle: "Framework metodologico e osservatorio cross-repo per KB personali e professionali con LLM"
author: "Stefano Pompa · stefano.pompa@gmail.com · github.com/steledama/metodo"
date: "2026.06.05"
---

Questa è la vista d'insieme del **metodo KB**: il metodo per costruire e mantenere *knowledge base* — basi di conoscenza personali e professionali, da qui in poi «KB» — insieme a un modello linguistico (LLM).

I diagrammi comprimono il metodo intero e si leggono dall'alto in basso: *cosa è* l'oggetto che si coltiva, *come* funziona (i tre giganti, il ciclo dell'azione, il goal), *come cresce* nel tempo. Ognuno è una porta: il dettaglio vive nei nodi della KB linkati in fondo.

Questo documento non è un nodo della KB ma una sua sintesi — e per la disciplina zettelkastiana le sintesi vivono fuori dai nodi atomici, in uno strato dedicato. Cosa sia quello strato, e perché questa pagina ne sia un esempio, si chiarisce più avanti.

## Cosa è: artefatto, sistema, metodo

La knowledge base non è il metodo: il metodo è più generale e la contiene. Tre parole per tre cose distinte, a lungo confuse nella sineddoche "KB = metodo".

```mermaid
flowchart TB
    MET["<b>METODO</b> · la pratica portabile<br/>più generale della KB: la contiene e la coltiva"]
    subgraph SIS["SISTEMA COGNITIVO"]
        direction LR
        H(["umano"])
        ART["<b>ARTEFATTO COGNITIVO</b> · portabile<br/>la rappresentazione che persiste<br/>KB + strato output + input + struttura"]
        AG(["<b>LLM</b> Claude · ChatGPT · DeepSeek…<br/>+<br/><b>harness</b> Claude Code · Codex…"])
        H --- ART
        ART --- AG
    end
    MET -->|coltiva| ART
```

- L'**artefatto cognitivo** è la rappresentazione esterna che persiste e si progetta — KB + strato output + input + struttura. È *portabile*: sopravvive al cambio di modello o di harness. È ciò che si coltiva.
- Il **sistema cognitivo** è dove la cognizione accade davvero: l'artefatto accoppiato all'umano e all'LLM (col suo harness), in opera. Non si progetta come oggetto: emerge dall'uso, e non è portabile.
- Il **metodo** è la pratica con cui si coltiva l'artefatto perché il sistema performi.

LLM e harness sono cose diverse: l'**LLM** è il modello (Claude, ChatGPT, DeepSeek…), l'**harness** è lo strumento che lo mette al lavoro (Claude Code, Codex…). La tesi del progetto — *artefatto portabile, vendor-neutro* — è dicibile solo perché l'artefatto è la rappresentazione, non il sistema d'interazione: cambi modello e harness, l'artefatto resta.

## I tre giganti

Sotto l'ontologia, tre pilastri si dividono il lavoro in modo nitido: come è fatto il nodo, chi tiene aggiornato il sistema, come il sistema produce azione. Luhmann *è* la KB — Karpathy la *governa* — Norman la *connette al mondo*.

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

## Il ciclo dell'azione

La KB non è il fine: è strumentale all'azione. Il ciclo è quello di Norman, nella sua forma originale: il **Goal** in cima (la KB è la memoria all'apice), il **Mondo** in fondo, l'esecuzione che scende a sinistra (Plan → Specify → Perform) e la valutazione che risale a destra (Perceive → Interpret → Compare).

```mermaid
flowchart TB
    KB[("KB")]
    GOAL(["<b>GOAL</b>"])
    o1["<b>o1</b> · Plan<br/>macchina"]
    o2["<b>o2</b> · Specify<br/>decisione"]
    o3["<b>o3</b> · Perform<br/>azione"]
    i3["<b>i3</b> · Compare<br/>formalizzato"]
    i2["<b>i2</b> · Interpret<br/>distillato"]
    i1["<b>i1</b> · Perceive<br/>segnale grezzo"]
    MONDO[/"<b>MONDO</b>"/]

    KB --> GOAL
    GOAL --> o1
    o1 --> o2
    o2 --> o3
    o3 -->|cerniera Mondo| MONDO
    GOAL --> i3
    i3 --> i2
    i2 --> i1
    i1 --> MONDO
    i3 -.->|cerniera KB| KB
```

Le due cerniere non sono uguali. Al **Mondo** è simmetrica — o3 agisce, i1 percepisce, stesso luogo due versi. Alla **KB** è *scrivi-poi-leggi*: i3 scrive l'esito nella memoria persistente, il Goal vi legge l'intenzione. È l'unica asimmetria, e non si vede dalla forma — per questo va detta. È qui che il metodo estende Norman ai suoi due estremi: apre il confine-Mondo (il mondo agisce, non solo risponde) e il confine-Goal (il goal si forma, non è dato).

## Cicli annidati: due Mondi

Il ciclo non è uno solo: sono due, annidati, ciascuno lo specchio appena visto. Si distinguono per *cosa è il loro Mondo* in fondo.

```mermaid
flowchart LR
    subgraph DEV["ciclo di SVILUPPO · Mondo = l'artefatto"]
        direction TB
        dG["Goal"]
        dO["<b>o3</b> · un commit<br/>agisce sull'artefatto"]
        dI["<b>i1</b> · lint, audit, test, errore"]
        dG --> dO --> dI --> dG
    end
    ART[("ARTEFATTO<br/>il codice · la KB")]
    subgraph RUN["ciclo RUNTIME · Mondo = la realtà"]
        direction TB
        rG["Goal"]
        rO["<b>o3</b> · email, transazione, gesto<br/>agisce sul mondo"]
        rI["<b>i1</b> · referto, payload, alert"]
        rG --> rO --> rI --> rG
    end
    DEV ==>|produce| ART
    ART ==>|è la macchina di| RUN
```

Per questo o1/o2/o3 e i1/i2/i3 si **raddoppiano**: c'è un o3 che agisce sul mondo e uno che agisce sull'artefatto, un i1 che viene dal mondo e uno che viene dall'artefatto. L'incastro è che l'**o3 del ciclo di sviluppo è la macchina del ciclo runtime** — il commit produce il codice che gira. Risalire da un output al task che l'ha generato — `output → codice → commit → tasks → goal` — è attraversare l'annidamento; `git-history`, `why` e `tasks` ne registrano la traccia. È il senso in cui il metodo apre la scatola nera che Norman lasciava chiusa: ogni sistema è l'o3 di un ciclo che lo precede.

## Le quattro dimensioni

«Dividere gli stadi per agente» sarebbe un taglio rigido: nasconde che agente e livello sono cose diverse — l'errore che aveva fatto «sparire» o1. Ogni elemento del metodo si colloca invece su quattro dimensioni *ortogonali*.

| dimensione          | valori                                                      |
| ------------------- | ---------------------------------------------------------- |
| **agente**          | umano · LLM                                                |
| **annidamento**     | runtime (→ mondo) · sviluppo (→ artefatto)                 |
| **livello**         | 1 macchina · 2 decisione · 3 azione                        |
| **lato del cappio** | output (esecuzione) · input (valutazione)                  |

La matrice è la lente per confrontare i domini. Qualche elemento collocato: il `.nix` di `nixos` è {LLM, sviluppo, livello 1, output}; un referto in `salute` è {umano, runtime, livello 1, input}; il termometro del `quadro` è {umano, runtime, livello 2, output}; un test che fallisce è {LLM, sviluppo, livello 1, input}. Letta per dominio dice cosa è sviluppato, cosa manca perché non serve (`nixos` ha pochissimo input esogeno dal mondo), e cosa manca ma servirebbe.

## Il goal: tre altitudini, un confine aperto

Norman dà il Goal per scontato. Il metodo lo disciplina con la gerarchia dell'activity theory (Leontiev): `goal` / `task` / `tasks/` non sono sinonimi, sono tre altitudini.

```mermaid
flowchart TB
    M["<b>motivo</b> · attività<br/><i>il perché di fondo — la cosa meno esternalizzabile</i>"]
    G["<b>goal</b> · azione<br/><i>cosa ottenere — informato dalla KB, non generato da essa</i>"]
    O["<b>operazione</b> · task<br/><i>tasks/ — il come, nel contesto</i>"]
    M --> G --> O
```

La KB *informa e raffina* il Goal, non lo *genera*: il Goal nasce all'incrocio tra motivo (da sopra) e KB. Da qui i due modi di i3: **verdetto** (Compare contro un goal esistente — loop noto, delegabile) e **formazione del goal** (triage dell'esogeno, decidere cosa conta — la cosa meno esternalizzabile, eco delle ironie dell'automazione di Bainbridge).

## Anatomia di un progetto

La struttura replicabile non è un albero identico: è la presenza esplicita delle funzioni cognitive. La **root è il cruscotto del ciclo di sviluppo** — i pochi artefatti letti a ogni sessione per capire il tutto. La collocazione segue altezza nel ciclo + pace, non profondità: `plan` e `why` stanno in root pur cambiando in fretta perché la loro altezza lo impone. Ogni componente risponde a una domanda. (`AGENTS.md` non è una funzione a sé: è il wrapper sottile, agnostico rispetto all'agente, che instrada verso README e CLAUDE.)

```mermaid
flowchart TB
    R["<b>README.md</b><br/><i>Goal: dove sono, da dove parto?</i>"]
    MAP["<b>map.md</b><br/><i>come si tiene insieme il dominio?</i>"]
    PLAN["<b>plan.md</b><br/><i>Plan: cosa devo fare adesso?</i>"]
    C["<b>CLAUDE.md</b> · <small>via AGENTS.md</small><br/><i>come agisco qui?</i>"]
    WHY["<b>why.md</b><br/><i>perché una decisione conta?</i>"]
    KB["<b>kb/</b> <small>+ index.md</small><br/><i>cosa significa questo concetto?</i>"]
    TASKS["<b>tasks/</b><br/><i>i dettagli operativi del task</i>"]
    S["<b>scripts/ · skill</b><br/><i>quali controlli e workflow?</i>"]
    OUT["<b>strato output</b><br/><i>come traduco la KB in azione?</i>"]

    R --> MAP
    R --> PLAN
    R --> C
    MAP --> KB
    PLAN --> TASKS
    C --> S
    KB --> OUT
    OUT --> WHY
    TASKS --> WHY
```

## Sviluppo bottom-up del metodo

Il metodo non si decreta dall'alto: emerge dall'uso reale. `metodo` custodisce le generalizzazioni, non orchestra i repo.

```mermaid
flowchart LR
    P["esigenza concreta<br/>in un repo adottante"]
    S["soluzione locale<br/>task · why · nodi"]
    G{"è<br/>generalizzabile?"}
    M["filing back in metodo<br/>nodo · regola · strumento"]
    PR["altri repo leggono i commit<br/>e applicano il pertinente"]
    L["resta lavoro locale"]
    P --> S --> G
    G -->|sì| M --> PR
    G -->|no| L
```

## Dove vive cosa

La regola di routing che tiene puliti i confini tra i componenti.

```mermaid
flowchart TB
    Q{"che tipo di<br/>contenuto?"}
    Q -->|concetto stabile e riusabile| KB["kb/ + index.md"]
    Q -->|lavoro futuro| TODO["plan.md + tasks/"]
    Q -->|perché una decisione conta| LOG["why.md"]
    Q -->|come agire / workflow| OP["CLAUDE.md · skill"]
    Q -->|modello del dominio| MAP["map.md"]
    Q -->|orientamento / ingresso| R["README.md"]
    Q -->|sintesi · vista · dashboard| OUT["strato output"]
```

## Lo strato output di questo repo

Dichiarazione minima dello strato output del repo `metodo`, applicata a sé stesso:

- **o1 macchina**: `kb/` in markdown consumato dagli LLM via symlink; output di `scripts/kb_tools.py` (audit JSON/markdown)
- **o2 decisione**: questo file — i diagrammi del metodo in sintesi
- **o3 azione**: il metodo applicato nei quattro repo adottanti (nodi creati, commit, KB mantenute)
- **i1 grezzo**: osservazioni dai repo adottanti (commit, task, why) e fonti in `sources/` (i libri di Norman, Hutchins, Leontiev)
- **i3 di ritorno**: l'osservatorio rilegge i repo adottanti e aggiorna `kb/confronto-progetti-adottanti.md`
- **Criterio di aggiornamento**: quando un gigante, un livello, un componente o un concetto fondativo cambia nei nodi, qui si aggiorna il diagramma corrispondente

## Approfondimento

I diagrammi comprimono; i nodi spiegano.

- cosa è (artefatto / sistema / metodo) → `kb/artefatto-cognitivo.md`, `kb/sistema-cognitivo.md`
- tre giganti → `kb/ciclo-azione.md`, `kb/zettelkasten.md`, `kb/pattern-karpathy.md`
- il ciclo · specchio simmetrico · cicli annidati · quattro dimensioni → `kb/ciclo-azione.md`, `kb/output.md`
- i due agenti · system image condivisa → `kb/system-image.md`, `kb/affordance-signifier.md`, `kb/visceral-behavioral-reflective.md`
- il goal · tre altitudini → `kb/goal.md`
- anatomia del progetto → `kb/struttura-progetto.md`
- sviluppo bottom-up e osservatorio → `kb/osservatorio-metodo.md`, `kb/metodo-kb.md`
- dove vive cosa → `kb/metodo-kb.md` (regole sullo stato), `kb/zettelkasten.md` (regola pratica)
