---
data: 2026-06-05
stato: bozza
---

# Output

Lo strato output del metodo: il livello che traduce la conoscenza accumulata nella KB in azione possibile nel mondo, e che riceve il segnale del mondo di ritorno per chiudere il ciclo. È distinto dalla KB perché ospita sintesi, viste, dashboard — tutto ciò che il purismo zettelkastiano vieta dentro ai nodi atomici e che il pattern Karpathy chiede di produrre.

Lo strato output esiste perché la KB possa restare pura. È la sua condizione di possibilità, non un'aggiunta opzionale. Senza, la pressione di sintesi finisce dentro ai nodi (caso paradigmatico: `salute/kb/storia-clinica.md`, diventato di fatto un mini-dashboard improprio), violando l'atomicità che è il principio fondante dello Zettelkasten.

## La risoluzione del conflitto Zettelkasten/Karpathy

Il metodo si appoggia su due pilastri con una tensione mai nominata. Lo Zettelkasten non nega l'output, ma lo colloca fuori dall'archivio: le carte di Luhmann sono atomiche, nessuna sintesi dentro. Karpathy mette invece la sintesi dentro al wiki — summary pages, entity pages, comparisons, mantenute dall'LLM. Le due posizioni collidono se si pretende di averle nello stesso spazio. La risoluzione del metodo è strutturale: la KB resta zettelkastiana pura, lo strato output ospita le sintesi karpathiane. La sintesi acquista un posto legittimo senza violare l'atomicità dei nodi.

## I tre livelli dell'output

- **o1 — macchina** — audience: LLM, sistema, automazione; forma: JSON, dati strutturati, `.nix` compilato; dove vive: nel repo se è parte dell'artefatto, in `data/` locale se è stato operativo o sensibile
- **o2 — decisione** — audience: umano (utente, collaboratori); forma: schemi, diagrammi, slides, termometri; dove vive: nel repo
- **o3 — azione** — audience: mondo; forma: email, parole dette, transazioni, gesti corporei; dove vive: fuori dal repo, nel mondo

o3 è dove l'output produce effetti reali. Tutto il resto è strumentale. o1 e o2 hanno funzioni diverse e dovrebbero essere distinguibili: un JSON denso è inutile per la decisione umana, un'infografica colorata è inefficiente per l'LLM.

o1 e o2 sono due _altitudini_ dell'arco di output, non lo stesso stadio: o1 il livello-macchina vicino alla KB, o2 la vista di decisione per l'umano. L'agente che li consuma (LLM/umano) è una dimensione ortogonale all'altitudine — cfr. `ciclo-azione`.

## Dati operativi e presentazione

La fonte di verità non coincide necessariamente con ciò che Git deve
versionare. Nei domini con dati personali, voluminosi o rigenerabili, la
separazione di default è:

- `data/` — workspace locale ignorato da Git: fonti grezze, dati compilati,
  cache, intermedi e report strutturati destinati alle macchine
- `presentations/` — superfici curate per lettura e decisione: HTML, CSS, SVG,
  markdown editoriale e altri artefatti o2 intenzionalmente versionati
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

L'o2 non è una sola forma. Karpathy: la forma della risposta segue la domanda — pagina markdown, tabella di confronto, deck di slide, grafico, canvas (cfr. `pattern-karpathy`). Il deck è la forma-default per la sintesi che si scorre, ma per un'altra domanda l'o2 giusto può essere una tabella o un grafico. Lo strumento del deck resta uniforme tra i repo (cfr. `presentazione`); il repertorio delle forme no: si sceglie per funzione, non per uniformità.

## Lo strato input

Il lato simmetrico del ciclo. Il segnale grezzo del mondo ritorna nel sistema e attraversa tre stadi prima di diventare conoscenza stabile:

- **i1 — grezzo** — natura: percezione del segnale esterno; forma: referto, log, export, documento, messaggio; dove vive: `sources/` (o locale al progetto)
- **i2 — distillato** — natura: interpretazione e sintesi; forma: nota di lettura, analisi, estratto commentato; dove vive: `kb/` in `stato: bozza`
- **i3 — formalizzato** — natura: conoscenza stabile o verdetto; forma: nodo KB aggiornato, fonte di verità, input al Goal; dove vive: `kb/` in `stato: maturo`

Ogni stadio corrisponde a uno stadio di Norman: i1 = Perceive, i2 = Interpret, i3 = Compare. Il passaggio i2→i3 non è automatico — è il giudizio che decide se un'interpretazione è abbastanza stabile da entrare nella KB. Per questo i2 vive in `kb/` come nodo in `stato: bozza`: la forma è quella del nodo, ma la funzione è ancora di elaborazione. La maturazione `bozza→maturo` è il passaggio i2→i3.

i1 ha due sorgenti: feedback (risposta a o3, chiude un goal esistente) ed esogeno (il mondo agisce da sé — busta paga, normativa, alert — e apre spesso un goal nuovo). Per questo i3 ha due modi: verdetto (Compare contro un goal esistente) e triage/formazione-goal (per l'esogeno). Cfr. `goal`.

## L'i2 ha bisogno di un substrato

L'i2 (Interpret) non lavora sul grezzo: da centinaia di segnali (i1) non si interpreta nulla. È la **sintesi** — la torta delle spese, il trend, il termometro — il luogo dove l'interpretazione accade. Per questo i2 e o2 sono lo stesso artefatto visto dai due archi (lo specchio o2↔i2): la sintesi è o2 quando la si produce (feedforward, scende), è substrato dell'i2 quando la si legge per interpretare (feedback, risale). La forma segue il dominio: grafica dove i dati sono molti (`economia`, `bi`), testuale dove il dominio è concettuale (`salute`). Vincolo di sicurezza: la sintesi che interpreta dev'essere goal-guidata sulla rilevanza ma neutra sulla valenza, o l'i2 diventa ragionamento motivato e la stessa superficie che dovrebbe far capire finisce per persuadere (cfr. `goal`).

## Lo specchio e le due cerniere

I due archi — output (esecuzione) e input (valutazione) — sono speculari, accoppiati per altitudine: **o3 ↔ i1** al Mondo, **o2 ↔ i2** in mezzo, **o1 ↔ i3** alla KB. L'output scende dalla KB al Mondo, l'input risale dal Mondo alla KB. La simmetria è quella di Norman; o1 è il vertice-macchina dell'arco di output — non manca e non appartiene a «un altro ciclo».

La simmetria convive con un'asimmetria _locale ai vertici_:

- **Cerniera Mondo** (o3 → i1): o3 scrive un effetto nel mondo, i1 lo rilegge più tardi come segnale. Il mondo trattiene lo stato nell'intervallo — è scrivi-poi-leggi attraverso un medium, non riflesso immediato.
- **Cerniera KB** (i3 → Goal): i3 _scrive_ l'esito nella KB, il Goal _legge_ l'intenzione — stessa forma, attraverso la memoria persistente. L'asimmetria vera non è tra le cerniere ma tra i medium: il mondo persiste da sé, la KB persiste solo se scritta. Da qui il principio: una decisione non scritta nella KB è una decisione persa.

I _due_ cicli non sono «uno per agente» ma **annidati per Mondo**: il ciclo runtime agisce sulla realtà, il ciclo di sviluppo agisce sull'artefatto stesso (o3 = un commit, i1 = lint/audit/test). o1/o2/o3 e i1/i2/i3 si raddoppiano di conseguenza. L'agente (umano/LLM) e il livello (1/2/3) sono dimensioni _ortogonali_, non la stessa cosa — cfr. `ciclo-azione`.

## Stato dei progetti adottanti

- **`nixos`** — o1: `.nix` in `home/`, `hosts/`, `modules/` (forte); o2: testo descrittivo in `kb/` (debole, no diagrammi); o3: sistema in esecuzione, deploy, switch (forte)
- **`bi`** — o1: scripts notturni (forte); o2: `presentations/index.html` Reveal.js autonomo (forte); o3: decisioni business, riunioni (forte)
- **`economia`** — o1: `data/json/` locale e non versionato (forte); o2: fotografia finanziaria versionata in `presentations/index.html`, derivata dai dati (forte); o3: email amministratori, riunioni famigliari (forte)
- **`salute`** — o1: implicito sparso (scadenze, cronologia in `storia-clinica`); o2: deck Reveal in `presentations/index.html` con file di dettaglio per area (forte); o3: yoga, controlli, alimentazione, conversazioni mediche (medio-forte)

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

Lo strato di sintesi-documento ha nome **uniforme** tra i progetti: `presentations/`. Il carattere del dominio vive nel contenuto, non nel nome della cartella (cfr. struttura-progetto, «struttura uniforme, carattere nel contenuto»): `salute` migra `quadro/`→`presentations/`, perché il nome clinico contraddiceva l'essenza non-dualista corpo/mente della KB. Resta distinto ciò che è output di altra natura ontologica: in `nixos` l'output _è_ la configurazione che gira (`home/`, `hosts/`, `modules/`), o1/runtime, non la porta `presentations/`. La funzione è la stessa ovunque: tradurre conoscenza in azione possibile.

## Criteri di qualità

Lo strato output va valutato sui criteri di Norman: visibilità, feedback, mapping, constraint (cfr. `ciclo-azione`). La bellezza dei nodi della KB non basta. Se l'utente non agisce, l'output è mal progettato, non l'utente è pigro.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [goal](goal.md)
- [mondo](mondo.md)
- [presentazione](presentazione.md)
- [artefatto-cognitivo](artefatto-cognitivo.md)
- [pattern-karpathy](pattern-karpathy.md)
- [zettelkasten](zettelkasten.md)
- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [struttura-progetto](struttura-progetto.md)
