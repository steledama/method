---
stato: bozza
---

# Output

Nota-struttura dello strato output del metodo: l'**arco di esecuzione** del ciclo d'azione, che scende dal Goal al Mondo. Non descrive i singoli stadi — `specify` (o2) e `perform` (o3) vivono come atomi — ma indicizza l'arco, tiene le tensioni tra gli stadi e ospita o1, l'unica altitudine senza atomo proprio. È il simmetrico dello strato `input` (l'arco di valutazione); la geometria che li accoppia vive in `action-cycle`. È distinto dalla KB perché ospita sintesi, viste, dashboard — tutto ciò che il purismo zettelkastiano vieta dentro ai nodi atomici e che il pattern Karpathy chiede di produrre.

## Perché lo strato esiste: il conflitto Zettelkasten/Karpathy

Il metodo si appoggia su due pilastri con una tensione mai nominata. Lo Zettelkasten non nega l'output, ma lo colloca fuori dall'archivio: le carte di Luhmann sono atomiche, nessuna sintesi dentro. Karpathy mette invece la sintesi dentro al wiki — summary pages, entity pages, comparisons mantenute dall'LLM. Le due posizioni collidono se si pretende di averle nello stesso spazio. La risoluzione del metodo è strutturale: la KB resta zettelkastiana pura, lo strato output ospita le sintesi karpathiane. Senza, la pressione di sintesi finisce dentro ai nodi (caso paradigmatico: `salute/kb/storia-clinica.md`, diventato un mini-dashboard improprio), violando l'atomicità che è il principio fondante. Lo strato output è la condizione di possibilità della KB pura, non un'aggiunta opzionale.

## Le tre altitudini

- **o1 — macchina** — audience: LLM, sistema, automazione; forma: JSON, dati strutturati, `.nix` compilato; dove vive: nel repo se è parte dell'artefatto, in `data/` locale se è stato operativo o sensibile. Riduce il gulf of execution per l'LLM che continua il lavoro tra sessioni: trova subito scadenze, stato e fatti strutturati senza ricostruire il modello. o1 non ha atomo proprio: è l'altitudine più sottile, e si sdoppia per annidamento — gli output-macchina del runtime (JSON, `.nix`) sono **o1-runtime**, mentre nel ciclo di sviluppo il Plan operativo (`plan`) è **o1-sviluppo** (cfr. `action-cycle`, `project-structure`).
- **o2 — decisione** (atomo `specify`) — vista per l'umano: schemi, diagrammi, slides, termometri; la forma segue la domanda.
- **o3 — prescrizione** (atomo `perform`) — l'atto predisposto e versionato sul lato interno della membrana `world`.

o1 e o2 sono due _altitudini_ dell'arco, non lo stesso stadio rivolto a due agenti: l'agente che consuma (LLM/umano) è ortogonale all'altitudine (cfr. `action-cycle`, `specify`). Un JSON denso è inutile per la decisione umana, un'infografica è inefficiente per l'LLM.

## Dati operativi e presentazione

La fonte di verità non coincide necessariamente con ciò che Git deve versionare. Nei domini con dati personali, voluminosi o rigenerabili la separazione di default è: `data/` (workspace locale ignorato da Git: grezzi, compilati, cache, intermedi, report per le macchine); `i2/` (superfici curate per lettura e decisione, artefatti i2/o2 intenzionalmente versionati); `scripts/`, `config/`, schemi e fixture anonime (trasformazione riproducibile e versionata). La distinzione non è «generato contro scritto a mano»: anche una presentazione generata si versiona quando è un risultato editoriale che deve aprirsi direttamente ed essere revisionabile; anche un JSON si versiona quando è configurazione, schema, fixture o parte costitutiva dell'artefatto. I dati operativi non entrano nella storia Git solo perché alimentano la presentazione. La riproducibilità è affidata alla trasformazione versionata e alla provenienza dichiarata; il backup dei dati resta distinto da Git.

## Nome uniforme, carattere nel contenuto

Lo strato di sintesi-documento ha nome **uniforme** tra i progetti: `i2/`, con indice leggibile `interpretations.md`. Il carattere del dominio vive nel contenuto, non nel nome della cartella (cfr. `project-structure`). La porta è i2 per identità; la stessa superficie si legge specularmente come o2 (cfr. `interpret`, `specify`). Resta distinto ciò che è output di altra natura ontologica: in `nixos` l'output _è_ la configurazione che gira (`home/`, `hosts/`, `modules/`), o1/runtime, non la porta `i2/`.

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

## Stato dei progetti adottanti

- **`nixos`** — o1: `.nix` in `home/`, `hosts/`, `modules/`; o2: testo descrittivo in `kb/` (debole); o3: configurazione e procedure pronte al deploy; `world`: switch applicato.
- **`bi`** — o1: script notturni; o2: vista HTML in `views/` o equivalente locale; o3: payload, runbook e canovacci; `world`: pubblicazione e riunioni.
- **`economia`** — o1: `data/json/` locale; o2/i2: fotografia finanziaria in vista HTML locale; o3: email predisposte e canovacci; `world`: invii, telefonate, transazioni.
- **`salute`** — o1: scadenze e stato strutturato; o2: deck/vista HTML locale; o3: promemoria e canovacci; `world`: pratiche, controlli, conversazioni mediche.

Pattern emergente: dove o2 è forte il progetto serve decisioni condivise con altri (`bi`); dove o2 è debole la KB resta personale e fatica a generare azione coordinata.

## Criteri di qualità

Lo strato output va valutato sui criteri di Norman: visibilità, feedback, mapping, constraint (cfr. `action-cycle`, `specify`). La bellezza dei nodi della KB non basta: se l'utente non agisce, l'output è mal progettato, non l'utente è pigro.

Connessioni:

- [input](input.md)
- [specify](specify.md)
- [perform](perform.md)
- [plan](plan.md)
- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [world](world.md)
- [view](view.md)
- [karpathy-pattern](karpathy-pattern.md)
- [zettelkasten](zettelkasten.md)
- [knowledge-base](knowledge-base.md)
- [processing-layers](processing-layers.md)
- [project-structure](project-structure.md)
- [adopter-comparison](adopter-comparison.md)
