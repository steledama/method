---
title: "Cognizione condivisa"
subtitle: "Framework metodologico e osservatorio cross-repo per la progettazione di artefatti di supporto alla cognizione condivisa tra uomo e modelli di intelligenza artificiale tramite knowledge base (KB)"
author: "Stefano Pompa · stefano.pompa@gmail.com · github.com/steledama/method"
date: "2026.06.09"
---

## Progettare la mente che condividiamo con la macchina {.hero data-background-color="#161d29"}

Non un prompt, non un mucchio di note: un **artefatto** che persiste, sopravvive al cambio di modello, e regge la cognizione condivisa lungo tutto il ciclo d'azione.

## Cosa è: artefatto, sistema, metodo

La KB non è il metodo: il metodo la contiene. Tre parole per tre cose, a lungo confuse nella sineddoche «KB = metodo».

<div class="diagram ontology">
  <div class="card accent"><strong>METODO</strong><span>la pratica portabile più generale della KB: la contiene e la coltiva</span></div>
  <div class="arrow down"><span>coltiva</span></div>
  <div class="frame">
    <div class="frame-title">SISTEMA COGNITIVO</div>
    <div class="diagram-row">
      <div class="card pill">umano</div>
      <div class="line"></div>
      <div class="card primary"><strong>ARTEFATTO COGNITIVO</strong><span>portabile · la rappresentazione che persiste</span><small>KB + strato output + input + struttura</small></div>
      <div class="line"></div>
      <div class="card pill"><strong>LLM</strong><span>Claude · ChatGPT · DeepSeek…</span><small>+ harness · Claude Code · Codex…</small></div>
    </div>
  </div>
</div>

- **Artefatto** — la rappresentazione che persiste e si progetta; _portabile_, sopravvive al cambio di modello o harness.
- **Sistema** — l'artefatto in opera, accoppiato a umano e LLM: dove la cognizione accade. Emerge dall'uso, non è portabile.
- **Metodo** — la pratica con cui si coltiva l'artefatto perché il sistema performi.

L'artefatto resta vendor-neutro perché è la _rappresentazione_, non il sistema d'interazione (LLM e harness sono diversi e sostituibili).

## I tre giganti

Luhmann _è_ la KB (forma del nodo), Karpathy la _governa_ (manutenzione), Norman la _connette al mondo_ (azione).

<div class="diagram giants">
  <div class="diagram-row cards-3">
    <div class="card"><strong>Luhmann · Zettelkasten</strong><span>forma del nodo</span><small>atomico · interconnesso<br>sintesi fuori dal nodo</small></div>
    <div class="card"><strong>Karpathy · LLM KB</strong><span>manutenzione dell'insieme</span><small>ingest · query · lint<br>filing back</small></div>
    <div class="card"><strong>Norman · ciclo di azione</strong><span>interfaccia KB ↔ mondo</span><small>visibilità · feedback<br>mapping · constraint</small></div>
  </div>
  <div class="merge-arrows"><i></i><i></i><i></i></div>
  <div class="card pill accent">METODO KB</div>
</div>

Karpathy risolve il «chi mantiene» assente in Luhmann; Norman il «come l'utente agisce» assente in entrambi.

## Il ciclo dell'azione: 6 atti + 2 poli

La KB non è il fine: è strumentale all'azione. Il ciclo di Norman, riletto: ai vertici due **poli** — il **Goal** (apice, il motivo) e il **Mondo** (fondo) — e fra loro sei **atti**, l'esecuzione che scende e la valutazione che risale.

<div class="diagram action-cycle">
  <div class="card pole">GOAL</div>
  <div class="cycle-columns">
    <div class="cycle-side execution">
      <div class="side-title">esecuzione ↓</div>
      <div class="card"><strong>o1 · Plan</strong><span>macchina</span></div>
      <div class="arrow down"></div>
      <div class="card"><strong>o2 · Specify</strong><span>decisione</span></div>
      <div class="arrow down"></div>
      <div class="card"><strong>o3 · Perform</strong><span>prescrizione</span></div>
    </div>
    <div class="cycle-side evaluation">
      <div class="side-title">↑ valutazione</div>
      <div class="card"><strong>i3 · Compare</strong><span>formalizzato</span></div>
      <div class="arrow up"></div>
      <div class="card"><strong>i2 · Interpret</strong><span>distillato</span></div>
      <div class="arrow up"></div>
      <div class="card"><strong>i1 · Perceive</strong><span>cattura</span></div>
    </div>
  </div>
  <div class="card pole world">WORLD · atto / grezzo</div>
</div>

I poli non si eseguono: si _costituiscono_ ai bordi. Il Mondo non preesiste — lo ritaglia l'artefatto, dall'infinito, per rilevanza guidata dai goal. `world` è la membrana non versionata; o3 e i1 sono i riflessi versionati on-demand che la toccano dai due versi.

## I tre livelli: perché un o2 solo riflessivo non muove

I tre livelli di Norman stratificano il ciclo per altezza: **riflessivo** in alto (la KB — pensa, non agisce direttamente), **behavioral** in mezzo (o2/i2 — l'operare), **viscerale** alla membrana (atto/grezzo in `world`, prescrizione/cattura in o3/i1).

Conseguenza per il design: il riflessivo può solo _condizionare_ l'azione, attraverso l'output. Per muovere davvero, l'o2 deve raggiungere il **viscerale** — apparenza, impatto immediato, affetto. Un o2 solo riflessivo (testo, schemi) sa ma non muove: è la stasi.

## Attractive things work better {.hero data-background-color="#161d29"}

Non è estetica. È la condizione perché il sapere attraversi i tre livelli — riflessivo, behavioral, viscerale — **fino al gesto**.

## Cicli annidati: due Mondi

Due cicli annidati, distinti da _cosa è il loro Mondo_ in fondo.

<div class="diagram nested-cycles">
  <div class="frame vertical-cycle">
    <div class="frame-title">CICLO DI SVILUPPO</div>
    <div class="card pill">Goal di sviluppo</div>
    <div class="arrow down"></div>
    <div class="card">o3 · commit</div>
    <div class="arrow down"></div>
    <div class="card pole world"><strong>Mondo di sviluppo</strong><span>ARTEFATTO</span></div>
    <div class="return-step">↻ i1 · lint · audit · test · errore</div>
  </div>
  <div class="handoff"><span>l'artefatto è la macchina del runtime</span><b>↓</b></div>
  <div class="frame vertical-cycle">
    <div class="frame-title">CICLO RUNTIME</div>
    <div class="card pill">Goal runtime</div>
    <div class="arrow down"></div>
    <div class="card">o3 · email · transazione · gesto</div>
    <div class="arrow down"></div>
    <div class="card pole world"><strong>Mondo runtime</strong><span>realtà del dominio</span></div>
    <div class="return-step">↻ i1 · referto · payload · alert</div>
  </div>
</div>

L'o3 di sviluppo è la macchina del runtime — il commit produce il codice che gira. Per questo il metodo apre la scatola nera di Norman: ogni sistema è l'o3 di un ciclo che lo precede.

## Le quattro dimensioni

Agente e livello sono cose diverse — confonderli aveva fatto «sparire» o1. Ogni elemento sta su quattro dimensioni _ortogonali_.

- **agente** — umano · LLM _(caso saliente di una popolazione)_
- **annidamento** — runtime (→ mondo) · sviluppo (→ artefatto)
- **livello** — 1 macchina · 2 decisione · 3 azione
- **lato del cappio** — output (esecuzione) · input (valutazione)

La matrice è la lente per confrontare i domini: cosa è sviluppato, cosa manca perché non serve, cosa manca ma servirebbe.

## Il goal: tre altitudini, un confine aperto

Norman dà il Goal per scontato; il metodo lo disciplina con Leontiev: `goal` / `task` / `tasks/` sono tre altitudini.

<div class="diagram altitude">
  <div class="card"><strong>motivo · attività</strong><span>il perché di fondo · la cosa meno esternalizzabile</span></div>
  <div class="arrow down"></div>
  <div class="card primary"><strong>goal · azione</strong><span>cosa ottenere · informato dalla KB, non generato da essa</span></div>
  <div class="arrow down"></div>
  <div class="card"><strong>operazione · task</strong><span><code>tasks/</code> · il come, nel contesto</span></div>
</div>

La KB _informa_ il Goal, non lo _genera_: nasce all'incrocio motivo × KB. Da qui i due modi di i3 — **verdetto** (Compare su goal noto, delegabile) e **formazione del goal** (triage dell'esogeno, la cosa meno esternalizzabile).

## La matrice di verifica: contro l'auto-accondiscendenza

La simmetria a 8 elementi non si dà per scontata: si mette alla prova. Gli 8 elementi × 5 artefatti, verdetto **solido / debole / forzato**.

Il rischio è la complicità con sé stessi — [chi cerca simmetria la trova]{.punch}. Primo passaggio onesto: i venti S di bordo sono quasi tautologici (li definiamo noi), l'interno è debole o da verificare, e lo zero-forzati è sospetto perché le caselle dure (i2/i3) sono ancora vuote.

[Lo strumento serve a _falsificare_ la teoria, non a incoronarla.]{.punch}

## Anatomia di un progetto

La struttura replicabile non è un albero identico: è la presenza esplicita delle funzioni cognitive. La root è l'**atrio** — l'`ls` ne dichiara l'inventario. Due specie: _file-ciclo_ (letti ogni sessione) e _porte-collezione_ (viste, aperte on-demand). La collocazione segue funzione + pace, non profondità.

<div class="diagram project-anatomy">
  <div class="card accent"><strong>README.md</strong><span>Goal · dove sono, da dove parto?</span></div>
  <div class="branch-arrows"><i></i><i></i><i></i></div>
  <div class="diagram-row cards-3">
    <div class="track"><div class="card"><strong>map.md</strong><span>come si tiene insieme il dominio?</span></div><div class="arrow down"></div><div class="card"><strong>kb.md → kb/</strong><span>cosa significa questo concetto?</span></div><div class="arrow down"></div><div class="card"><strong>strato output</strong><span>come traduco la KB in azione?</span></div></div>
    <div class="track"><div class="card"><strong>plan.md</strong><span>Plan · cosa devo fare adesso?</span></div><div class="arrow down"></div><div class="card"><strong>tasks/</strong><span>i dettagli operativi del task</span></div><div class="arrow down"></div><div class="card destination"><strong>verdict.md</strong><span>perché una decisione conta?</span></div></div>
    <div class="track"><div class="card"><strong>CLAUDE.md</strong><small>via AGENTS.md</small><span>come agisco qui?</span></div><div class="arrow down"></div><div class="card"><strong>tools.md → tools/ · skill</strong><span>quali controlli e workflow?</span></div></div>
  </div>
</div>

## Sviluppo del metodo: dal basso e dall'alto

<div class="diagram method-development">
  <div class="frame adopters">
    <div class="frame-title">PROGETTI ADOTTANTI</div>
    <div class="diagram-row">
      <div class="card">esigenza concreta</div><div class="arrow right"></div><div class="card">soluzione locale</div>
    </div>
  </div>
  <div class="movement bottom-up"><b>↓</b><span>bottom-up · filing back</span></div>
  <div class="diagram-row decision-row">
    <div class="card theory">cornice teorica<br><small>gigante · distinzione</small></div>
    <div class="arrow right"><span>inquadramento</span></div>
    <div class="card diamond">generalizzabile?</div>
    <div class="split"><span>no → resta locale</span><b>↓ sì</b></div>
  </div>
  <div class="card primary">METODO · nodo · regola · strumento</div>
  <div class="movement top-down"><b>↓</b><span>top-down · propagazione</span></div>
  <div class="card accent">adozione e verifica nei domini</div>
  <div class="feedback">↻ feedback · nuove esigenze</div>
</div>

Due movimenti in alternanza. Dal basso, un'esigenza concreta risale a `metodo`
solo se generalizzabile. Dall'alto, il metodo restituisce la generalizzazione
agli adottanti, dove viene adattata e verificata; una cornice teorica può inoltre
dare forma a ciò che dal basso si avverte ma non si sa nominare. `metodo`
custodisce e propaga il canone, senza trasformarsi nel backlog operativo dei
repo.

## Dove vive cosa

La regola di routing che tiene puliti i confini tra i componenti.

<div class="diagram routing">
  <div class="card diamond accent">che tipo di contenuto?</div>
  <div class="routing-list">
    <div><span>concetto stabile e riusabile</span><strong>kb.md → kb/</strong></div>
    <div><span>lavoro futuro</span><strong>plan.md + tasks/</strong></div>
    <div><span>perché una decisione conta</span><strong>verdict.md</strong></div>
    <div><span>come agire · workflow</span><strong>CLAUDE.md · skill</strong></div>
    <div><span>modello del dominio</span><strong>map.md</strong></div>
    <div><span>orientamento · ingresso</span><strong>README.md</strong></div>
    <div><span>sintesi · vista · dashboard</span><strong>strato output</strong></div>
  </div>
</div>

## Le interpretazioni di questo repo

Dichiarazione minima, applicata a sé stessa:

- **o1 macchina**: `kb/` in markdown via symlink; output di `tools/kb_tools.py`
- **i2-macro**: _questo deck_ (Reveal sulla sorgente `metodo-in-sintesi.md`, in `interpretations/`) — rivela tensioni non-locali tra nodi. In ogni dominio la stessa superficie è o2 quando viene prodotta come vista di decisione e substrato i2 quando viene letta per attribuire significato alla sintesi — cfr. `kb/action-cycle.md`, sezione i2 micro/macro. La forma segue la domanda: deck per la sintesi che si scorre, ma il repertorio o2/i2 è più largo (pagina, tabella, grafico, canvas)
- **o3 azione**: il metodo applicato nei repo adottanti (nodi, commit, KB mantenute)
- **i1/i3 di ritorno**: osservazioni dai repo → `adopter-comparison`

La pubblicazione (o3) si serve dalla sorgente, per un percorso versionato, dietro confine di rete (cfr. `deck`).

## Ogni sezione è un'interpretazione: l'i2-macro del metodo su sé stesso

Ecco perché questa pagina è un esempio dello strato che descrive. Il deck non è solo un prodotto: è l'**organo di interpretazione** — ogni sezione è un'interpretazione i2-macro che rende co-presenti le tensioni tra nodi altrimenti invisibili da dentro ciascuno (Luhmann: i nodi sono atomici e _localmente_ coerenti). Il _verdetto_ (i3) che ne segue si chiude nei nodi e in `verdict.md` — il termometro del ciclo di sviluppo, simmetrico a `plan.md` (lo stadio Plan), per la simmetria o1 ↔ i3.

Comprimere il metodo in poche interpretazioni forza la co-presenza e fa affiorare le tensioni _non-locali_. Disciplina: il deck rivela, i nodi risolvono — ogni tensione si chiude giù nei nodi (la fonte di verità), poi il deck si _ri-deriva_. Aggiornare questa pagina è far girare l'i2-macro del metodo su sé stesso — come questa stessa revisione.

## Il deck rivela, i nodi risolvono {.hero data-background-color="#161d29"}

Comprimere il metodo in poche interpretazioni fa **affiorare** le tensioni non-locali. Ma ogni tensione si chiude giù nei nodi — la fonte di verità — e poi il deck si _ri-deriva_.

## Approfondimento

I diagrammi comprimono; i nodi spiegano.

- cosa è (artefatto / sistema / metodo) → `kb/cognitive-artifact.md`, `kb/cognitive-system.md`
- tre giganti → `kb/action-cycle.md`, `kb/zettelkasten.md`, `kb/karpathy-pattern.md`
- ciclo (6 atti + 2 poli) · cicli annidati · quattro dimensioni → `kb/action-cycle.md`, `kb/world.md`, `kb/output.md`
- i tre livelli · system image · agente come popolazione → `kb/processing-layers.md`, `kb/system-image.md`, `kb/affordance-signifier.md`, `kb/agent.md`
- il goal · tre altitudini → `kb/goal.md`
- la matrice di verifica → `kb/action-cycle-matrix.md`
- strato output · repertorio o2 · pubblicazione → `kb/output.md`, `kb/deck.md`
- anatomia del progetto → `kb/project-structure.md`
- sviluppo del metodo e osservatorio → `kb/method-development.md`, `kb/method-observatory.md`, `kb/cognitive-artifact-design.md`
- dove vive cosa → `kb/cognitive-artifact-design.md`, `kb/zettelkasten.md`
