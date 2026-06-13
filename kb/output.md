---
data: 2026-06-13
stato: bozza
---

# Output

Lo strato output del metodo: il livello che traduce la conoscenza accumulata nella KB in azione possibile nel mondo — l'**arco di esecuzione** del ciclo d'azione, che scende dalla KB al Mondo. È il simmetrico dello strato `input` (l'arco di valutazione, che risale dal Mondo alla KB e chiude il ciclo); la geometria che li accoppia — specchio per altitudine, le due cerniere, i cicli annidati — vive in `action-cycle`. È distinto dalla KB perché ospita sintesi, viste, dashboard — tutto ciò che il purismo zettelkastiano vieta dentro ai nodi atomici e che il pattern Karpathy chiede di produrre.

Lo strato output esiste perché la KB possa restare pura. È la sua condizione di possibilità, non un'aggiunta opzionale. Senza, la pressione di sintesi finisce dentro ai nodi (caso paradigmatico: `salute/kb/storia-clinica.md`, diventato di fatto un mini-dashboard improprio), violando l'atomicità che è il principio fondante dello Zettelkasten.

## La risoluzione del conflitto Zettelkasten/Karpathy

Il metodo si appoggia su due pilastri con una tensione mai nominata. Lo Zettelkasten non nega l'output, ma lo colloca fuori dall'archivio: le carte di Luhmann sono atomiche, nessuna sintesi dentro. Karpathy mette invece la sintesi dentro al wiki — summary pages, entity pages, comparisons, mantenute dall'LLM. Le due posizioni collidono se si pretende di averle nello stesso spazio. La risoluzione del metodo è strutturale: la KB resta zettelkastiana pura, lo strato output ospita le sintesi karpathiane. La sintesi acquista un posto legittimo senza violare l'atomicità dei nodi.

## I tre livelli dell'output

- **o1 — macchina** — audience: LLM, sistema, automazione; forma: JSON, dati strutturati, `.nix` compilato; dove vive: nel repo se è parte dell'artefatto, in `data/` locale se è stato operativo o sensibile
- **o2 — decisione** — audience: umano (utente, collaboratori); forma: schemi, diagrammi, slides, termometri; dove vive: nel repo
- **o3 — prescrizione** — audience: chi compie l'atto; forma: canovaccio,
  messaggio predisposto, promemoria, runbook o payload pronto; dove vive:
  versionato nel repo quando precisione o durata lo richiedono

o3 non è l'atto: è la sua prescrizione versionata, il riflesso dell'azione
predisposto sul lato interno della membrana `world`. L'email inviata,
l'incontro, la transazione, il deploy e il gesto corporeo accadono nel Mondo.
Come i1, o3 è **on-demand**: serve quando l'esecuzione richiede precisione,
revisione o durata; non ogni gesto deve lasciare un artefatto.

o1 e o2 hanno funzioni diverse e dovrebbero essere distinguibili: un JSON denso
è inutile per la decisione umana, un'infografica colorata è inefficiente per
l'LLM.

o1 e o2 sono due _altitudini_ dell'arco di output, non lo stesso stadio: o1 il livello-macchina vicino alla KB, o2 la vista di decisione per l'umano. L'agente che li consuma (LLM/umano) è una dimensione ortogonale all'altitudine — cfr. `action-cycle`.

## Dati operativi e presentazione

La fonte di verità non coincide necessariamente con ciò che Git deve
versionare. Nei domini con dati personali, voluminosi o rigenerabili, la
separazione di default è:

- `data/` — workspace locale ignorato da Git: fonti grezze, dati compilati,
  cache, intermedi e report strutturati destinati alle macchine
- `interpretations/` — superfici curate per lettura, decisione e interpretazione:
  HTML, CSS, SVG, markdown editoriale e altri artefatti i2/o2 intenzionalmente
  versionati (cfr. `action-cycle`, sezione i2 micro/macro)
- `scripts/`, `config/`, schemi e fixture anonime — trasformazione
  riproducibile, versionata

La distinzione non è «generato contro scritto a mano». Anche una presentazione
generata si versiona quando è un risultato editoriale che deve aprirsi
direttamente, essere revisionabile nel tempo e incorporare affinamenti di
design. Anche un JSON può essere versionato quando è configurazione, schema,
fixture o parte costitutiva dell'artefatto. I dati operativi, invece, non
entrano nella storia Git soltanto perché alimentano la presentazione.

Questa separazione riduce esposizione di dati sensibili, rumore nei diff e peso
della storia. La riproducibilità è affidata alla trasformazione versionata e
alla provenienza dichiarata delle fonti; il backup dei dati resta una
responsabilità distinta da Git.

## La forma dell'o2 segue la domanda

L'o2 non è una sola forma. Karpathy: la forma della risposta segue la domanda — pagina markdown, tabella di confronto, deck di slide, grafico, canvas (cfr. `karpathy-pattern`). Il deck è la forma-default per la sintesi che si scorre, ma per un'altra domanda l'o2 giusto può essere una tabella o un grafico. Lo strumento del deck resta uniforme tra i repo (cfr. `deck`); il repertorio delle forme no: si sceglie per funzione, non per uniformità.

## Stato dei progetti adottanti

- **`nixos`** — o1: `.nix` in `home/`, `hosts/`, `modules/`; o2: testo
  descrittivo in `kb/` (debole); o3: configurazione e procedure pronte al
  deploy; `world`: switch applicato e sistema in esecuzione
- **`bi`** — o1: script notturni; o2: `interpretations/index.html`; o3:
  payload, runbook e canovacci per decisioni business; `world`: pubblicazione e
  riunioni realizzate
- **`economia`** — o1: `data/json/` locale; o2/i2: fotografia finanziaria in
  `interpretations/index.html`; o3: email predisposte e canovacci degli
  incontri; `world`: invii, telefonate, riunioni e transazioni
- **`salute`** — o1: scadenze e stato strutturato; o2: deck in
  `interpretations/index.html`; o3: promemoria e canovacci; `world`: pratiche,
  controlli, alimentazione e conversazioni mediche

## L'esecuzione può far emergere Goal

Predisporre un atto obbliga a specificare destinatari, vincoli, poste e criteri
di successo. Questo lavoro può rendere visibili Goal latenti non ancora
formalizzati nella KB: il canovaccio non si limita a eseguire un'intenzione,
può rivelare che l'intenzione era incompleta. Il triage/formazione-goal non
appartiene quindi solo all'input esogeno; può essere innescato anche dall'arco
di esecuzione. Il nuovo Goal resta una decisione riflessiva, non un prodotto
automatico di o3.

Pattern emergente: dove o2 è forte, il progetto serve decisioni condivise con altri (`bi`); dove o2 è debole, la KB resta personale e fatica a generare azione coordinata.

## Dichiarazione minima

Ogni progetto adottante dovrebbe dichiarare esplicitamente il proprio strato output nella mappa o nel README locale:

```markdown
## Strato output

- o1 macchina:
- o2 decisione:
- o3 azione:
- Strato input (i1/i2/i3):
- Fonte di ritorno:
- Criterio di aggiornamento:
```

## Nome uniforme, carattere nel contenuto

Lo strato di sintesi-documento ha nome **uniforme** tra i progetti:
`interpretations/`. Il carattere del dominio vive nel contenuto, non nel nome
della cartella (cfr. project-structure, «struttura uniforme, carattere nel
contenuto»): anche una fotografia finanziaria seleziona, aggrega e rappresenta i
numeri secondo i goal, dunque interpreta. La stessa superficie è o2 quando viene
prodotta come vista di decisione e substrato i2 quando viene letta per attribuire
significato ai dati. Resta distinto ciò che è output di altra natura ontologica:
in `nixos` l'output _è_ la configurazione che gira (`home/`, `hosts/`,
`modules/`), o1/runtime, non la porta `interpretations/`. La funzione è la stessa
ovunque: tradurre conoscenza in azione possibile.

## Criteri di qualità

Lo strato output va valutato sui criteri di Norman: visibilità, feedback, mapping, constraint (cfr. `action-cycle`). La bellezza dei nodi della KB non basta. Se l'utente non agisce, l'output è mal progettato, non l'utente è pigro.

Connessioni:

- [input](input.md)
- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [world](world.md)
- [deck](deck.md)
- [cognitive-artifact](cognitive-artifact.md)
- [karpathy-pattern](karpathy-pattern.md)
- [zettelkasten](zettelkasten.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [adopter-comparison](adopter-comparison.md)
- [project-structure](project-structure.md)
- [processing-layers](processing-layers.md)
