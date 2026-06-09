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

| Livello        | Audience                      | Forma                                            | Dove vive                 |
| -------------- | ----------------------------- | ------------------------------------------------ | ------------------------- |
| o1 — macchina  | LLM, sistema, automazione     | JSON, dati strutturati, `.nix` compilato         | nel repo                  |
| o2 — decisione | umano (utente, collaboratori) | schemi, diagrammi, slides, termometri            | nel repo                  |
| o3 — azione    | mondo                         | email, parole dette, transazioni, gesti corporei | fuori dal repo, nel mondo |

o3 è dove l'output produce effetti reali. Tutto il resto è strumentale. o1 e o2 hanno funzioni diverse e dovrebbero essere distinguibili: un JSON denso è inutile per la decisione umana, un'infografica colorata è inefficiente per l'LLM.

o1 e o2 sono due _altitudini_ dell'arco di output, non lo stesso stadio: o1 il livello-macchina vicino alla KB, o2 la vista di decisione per l'umano. L'agente che li consuma (LLM/umano) è una dimensione ortogonale all'altitudine — cfr. `ciclo-azione`.

## Lo strato input

Il lato simmetrico del ciclo. Il segnale grezzo del mondo ritorna nel sistema e attraversa tre stadi prima di diventare conoscenza stabile:

| Livello           | Natura                         | Forma                                              | Dove vive                         |
| ----------------- | ------------------------------ | -------------------------------------------------- | --------------------------------- |
| i1 — grezzo       | percezione del segnale esterno | referto, log, export, documento, messaggio         | `sources/` (o locale al progetto) |
| i2 — distillato   | interpretazione e sintesi      | nota di lettura, analisi, estratto commentato      | `kb/` in `stato: bozza`           |
| i3 — formalizzato | conoscenza stabile o verdetto  | nodo KB aggiornato, fonte di verità, input al Goal | `kb/` in `stato: maturo`          |

Ogni stadio corrisponde a uno stadio di Norman: i1 = Perceive, i2 = Interpret, i3 = Compare. Il passaggio i2→i3 non è automatico — è il giudizio che decide se un'interpretazione è abbastanza stabile da entrare nella KB. Per questo i2 vive in `kb/` come nodo in `stato: bozza`: la forma è quella del nodo, ma la funzione è ancora di elaborazione. La maturazione `bozza→maturo` è il passaggio i2→i3.

i1 ha due sorgenti: feedback (risposta a o3, chiude un goal esistente) ed esogeno (il mondo agisce da sé — busta paga, normativa, alert — e apre spesso un goal nuovo). Per questo i3 ha due modi: verdetto (Compare contro un goal esistente) e triage/formazione-goal (per l'esogeno). Cfr. `goal`.

## Lo specchio e le due cerniere

I due archi — output (esecuzione) e input (valutazione) — sono speculari, accoppiati per altitudine: **o3 ↔ i1** al Mondo, **o2 ↔ i2** in mezzo, **o1 ↔ i3** alla KB. L'output scende dalla KB al Mondo, l'input risale dal Mondo alla KB. La simmetria è quella di Norman; o1 è il vertice-macchina dell'arco di output — non manca e non appartiene a «un altro ciclo».

La simmetria convive con un'asimmetria _locale ai vertici_:

- **Cerniera Mondo** (o3 → i1): o3 scrive un effetto nel mondo, i1 lo rilegge più tardi come segnale. Il mondo trattiene lo stato nell'intervallo — è scrivi-poi-leggi attraverso un medium, non riflesso immediato.
- **Cerniera KB** (i3 → Goal): i3 _scrive_ l'esito nella KB, il Goal _legge_ l'intenzione — stessa forma, attraverso la memoria persistente. L'asimmetria vera non è tra le cerniere ma tra i medium: il mondo persiste da sé, la KB persiste solo se scritta. Da qui il principio: una decisione non scritta nella KB è una decisione persa.

I _due_ cicli non sono «uno per agente» ma **annidati per Mondo**: il ciclo runtime agisce sulla realtà, il ciclo di sviluppo agisce sull'artefatto stesso (o3 = un commit, i1 = lint/audit/test). o1/o2/o3 e i1/i2/i3 si raddoppiano di conseguenza. L'agente (umano/LLM) e il livello (1/2/3) sono dimensioni _ortogonali_, non la stessa cosa — cfr. `ciclo-azione`.

## Stato dei progetti adottanti

| Progetto   | o1                                                          | o2                                                         | o3                                                                  |
| ---------- | ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| `nixos`    | `.nix` in `home/`, `hosts/`, `modules/` (forte)             | testo descrittivo in `kb/` (debole, no diagrammi)          | sistema in esecuzione, deploy, switch (forte)                       |
| `bi`       | scripts notturni (forte)                                    | `presentation/` Reveal.js (forte)                          | decisioni business, riunioni (forte)                                |
| `economia` | `output/json/` (forte)                                      | `output/report*.md` tabelle (medio)                        | email amministratori, riunioni famigliari (forte)                   |
| `salute`   | implicito sparso (scadenze, cronologia in `storia-clinica`) | `quadro/` con termometro e file per area (pilota in bozza) | yoga, controlli, alimentazione, conversazioni mediche (medio-forte) |

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
