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

| Livello            | Audience                      | Forma                                            | Dove vive                 |
| ------------------ | ----------------------------- | ------------------------------------------------ | ------------------------- |
| o1 — macchina      | LLM, sistema, automazione     | JSON, dati strutturati, `.nix` compilato         | nel repo                  |
| o2 — decisione     | umano (utente, collaboratori) | schemi, diagrammi, slides, termometri            | nel repo                  |
| o3 — azione        | mondo                         | email, parole dette, transazioni, gesti corporei | fuori dal repo, nel mondo |

o3 è dove l'output produce effetti reali. Tutto il resto è strumentale. o1 e o2 hanno funzioni diverse e dovrebbero essere distinguibili: un JSON denso è inutile per la decisione umana, un'infografica colorata è inefficiente per l'LLM.

o1 e o2 non sono due stadi del ciclo di Norman — sono lo stesso stadio Plan/Specify rivolto ai due agenti che lo portano avanti (cfr. `ciclo-azione`).

## Lo strato input

Il lato simmetrico del ciclo. Il segnale grezzo del mondo ritorna nel sistema e attraversa tre stadi prima di diventare conoscenza stabile:

| Livello        | Natura                          | Forma                                              | Dove vive          |
| -------------- | ------------------------------- | -------------------------------------------------- | ------------------ |
| i1 — grezzo    | percezione del segnale esterno  | referto, log, export, documento, messaggio         | `sources/` (o locale al progetto) |
| i2 — distillato | interpretazione e sintesi       | nota di lettura, analisi, estratto commentato      | `kb/` in `stato: bozza` |
| i3 — formalizzato | conoscenza stabile o verdetto | nodo KB aggiornato, fonte di verità, input al Goal | `kb/` in `stato: maturo` |

Ogni stadio corrisponde a uno stadio di Norman: i1 = Perceive, i2 = Interpret, i3 = Compare. Il passaggio i2→i3 non è automatico — è il giudizio che decide se un'interpretazione è abbastanza stabile da entrare nella KB. Per questo i2 vive in `kb/` come nodo in `stato: bozza`: la forma è quella del nodo, ma la funzione è ancora di elaborazione. La maturazione `bozza→maturo` è il passaggio i2→i3.

i1 ha due sorgenti: feedback (risposta a o3, chiude un goal esistente) ed esogeno (il mondo agisce da sé — busta paga, normativa, alert — e apre spesso un goal nuovo). Per questo i3 ha due modi: verdetto (Compare contro un goal esistente) e triage/formazione-goal (per l'esogeno). Cfr. `goal`.

## Il cappio con due cerniere

La struttura del ciclo non è uno specchio (i3 ↔ o1) ma un cappio con due cerniere asimmetriche.

- **Cerniera Mondo** (o3 → i1): o3 agisce, i1 percepisce — stesso luogo, due versi. Simmetrica: il mondo risponde all'azione. La cerniera è una porta bidirezionale.
- **Cerniera KB** (i3 → Goal): i3 *scrive* l'esito nella KB; il Goal *legge* l'intenzione dalla KB. Scrivi-poi-leggi, non riflesso — l'asimmetria è una feature. La KB è la memoria persistente dove il ciclo si chiude. Da qui il principio: una decisione non scritta nella KB è una decisione persa.

o1 non sta sull'arco principale — vive sul ciclo del secondo agente (l'LLM che legge la KB per agire), che ha un proprio lato-input (audit, lint, errori). Due cicli, uno per agente, stessa KB all'apice.

## Stato dei progetti adottanti

| Progetto   | o1                                                          | o2                                                         | o3                                                                  |
| ---------- | ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| `nixos`    | `.nix` in `home/`, `hosts/`, `modules/` (forte)             | testo descrittivo in `kb/` (debole, no diagrammi)          | sistema in esecuzione, deploy, switch (forte)                       |
| `bi`       | scripts notturni (forte)                                    | `presentazione/` Reveal.js (forte)                         | decisioni business, riunioni (forte)                                |
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

## Forma locale, funzione universale

Il nome dello strato resta locale e segue il dominio: `salute` lo chiama `quadro/`, `bi` ha già `presentazione/`, `economia` ha `output/`, `nixos` ha `home/hosts/modules/` (l'output *è* la configurazione che gira). La funzione è la stessa: tradurre conoscenza in azione possibile. Il nome locale è scelta di dominio, non drift dal metodo.

## Criteri di qualità

Lo strato output va valutato sui criteri di Norman: visibilità, feedback, mapping, constraint (cfr. `ciclo-azione`). La bellezza dei nodi della KB non basta. Se l'utente non agisce, l'output è mal progettato, non l'utente è pigro.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [goal](goal.md)
- [artefatto-cognitivo](artefatto-cognitivo.md)
- [pattern-karpathy](pattern-karpathy.md)
- [zettelkasten](zettelkasten.md)
- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [struttura-progetto](struttura-progetto.md)
