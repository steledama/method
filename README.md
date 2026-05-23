# Metodo

Framework metodologico per knowledge base personali e professionali mantenute con LLM. Definisce forma dei nodi, struttura del progetto, strumenti di manutenzione, principi guida e ciclo di lavoro.

Il metodo è portabile tra progetti di natura diversa. Il nucleo è universale — principi, struttura KB, ciclo operativo — mentre le personalizzazioni sono esplicite: ogni progetto estende il metodo con principi e strumenti propri del dominio.

## Progetti adottanti

| Progetto                 | Dominio                                       | Note metodologiche                                                                                                                                                                 |
| ------------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [nixos](../nixos/)       | Configurazione sistemi NixOS multi-host       | principi code-based specifici (Explicit Unfree, Hardware-Specific, Home Manager standalone); audit scripts con sottocomandi nixos-specifici (inventory, facts, coverage, fidelity) |
| [bi](../bi/)             | Business intelligence e sincronizzazione dati | principi operativi specifici (Graceful degradation, Eventual consistency, Tracciabilità operativa); kb_tools.py con facts adattato alla mappa di progetto                          |
| [economia](../economia/) | Gestione finanziaria e legale personale       | fedelta-cognitiva adattata al dominio legale/finanziario: fonte di verità = output strutturati e documenti autoritativi                                                            |
| [salute](../salute/)     | Monitoraggio salute e benessere               | adattamento fedelta-cognitiva e design-principles in corso                                                                                                                         |

## Tasks aperti

| Priorità | Task                                                                                         | Dipende da                                     |
| -------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Bassa    | [Valutazione strumenti, skills e KB cross-repo](todo/valutazione-strumenti-kb-cross-repo.md) | Evoluzione reale dei progetti e dei loro tools |

I task con contesto operativo vivono in `todo/` e vengono rimossi quando
completati.

## Come collegare un nuovo progetto

1. Crea il symlink: `ln -s ../metodo/kb metodo` dalla root del progetto.
2. Aggiungi una riga alla tabella dei progetti adottanti.
3. Nel README del progetto, referenzia `metodo/metodo-kb.md` come nodo centrale del metodo e aggiungi una sezione con i principi specifici del progetto.
4. Aggiorna i path in `CLAUDE.md` del progetto: `kb/metodo-kb.md` → `metodo/metodo-kb.md` (e analogamente per gli altri nodi metodologici).

## Nodi

- [metodo-kb](kb/metodo-kb.md) — Il metodo: ciclo operativo, tipi documentali, regole di revisione
- [nodo](kb/nodo.md) — Unità atomica della KB: struttura, naming, frontmatter, footer Connessioni
- [knowledge-base](kb/knowledge-base.md) — KB basata su LLM: artefatto cumulativo, divisione del lavoro umano/LLM
- [struttura-progetto](kb/struttura-progetto.md) — Quattro pilastri operativi: README, CLAUDE.md, log.md, audit-kb
- [strumenti-kb](kb/strumenti-kb.md) — Script versionati per audit, backlink, migrazione e candidati terminologici
- [fedelta-cognitiva](kb/fedelta-cognitiva.md) — Verifica della KB oltre il lint: anti-drift, checklist semantica, adattamento al dominio
- [design-principles](kb/design-principles.md) — Principi guida: universali, code-based e specifici di progetto
- [zettelkasten](kb/zettelkasten.md) — Metodo Zettelkasten: nodi atomici interconnessi, struttura emergente
- [pattern-karpathy](kb/pattern-karpathy.md) — Pattern wiki personale mantenuta da LLM: ingest, query, lint e filing back
- [connessione](kb/connessione.md) — Strategie di collegamento tra nodi: inline vs footer, motivazioni della scelta
