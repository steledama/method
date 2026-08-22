---
stato: bozza
---

# Source of truth

Una fonte di verità è ciò contro cui si verifica ciò che la KB dice. Risponde
alla domanda: contro che cosa verifico ciò che la KB dice? Può essere codice,
configurazione, JSON, documento autoritativo, database, output strutturato o
mappa mantenuta manualmente.

La fonte di verità impedisce alla KB di diventare una descrizione plausibile ma
disancorata. Nei progetti code-based può coincidere con file tecnici; nei
progetti finanziari con documenti e JSON compilati; nei progetti riflessivi con
fonti testuali, corpus elaborati o scelte interpretative dichiarate.

Regole:

- deve essere esplicita quando un fatto ha alta deriva
- deve essere distinta dalla sintesi interpretativa della KB
- può essere tecnica, documentale o umana a seconda del dominio
- non deve essere versionata per forza: autorevolezza, persistenza, backup e
  controllo versione sono proprietà distinte
- la **provenienza** delle fonti-mondo autorevoli (quale edizione regge quale
  nodo) si versiona nella sezione fonti del register `world.md` (che assorbe il
  vecchio `sources.md`) e alimenta i `## Riferimenti` dei nodi
- va collegata dal register `world.md` e dai nodi ad alta responsabilità
- alimenta i controlli di fedeltà cognitiva
- non tutti i nodi richiedono la stessa intensità di verifica

## Casi osservati negli adottanti

Quattro configurazioni ricorrenti, non l'inventario del territorio (che vive nel
register `world.md`):

- **configurazione dichiarativa** — la fonte è il codice stesso: flake, moduli,
  profili, filesystem. È il caso più verificabile, perché le fonti sono
  leggibili direttamente dagli script.
- **integrazione di sistemi esterni** — accanto a script e configurazioni locali
  vivono gestionali, e-commerce e fogli remoti. La difficoltà è distinguere le
  fonti tecniche locali dai sistemi esterni, non sempre esportabili né
  interrogabili a piacere.
- **dominio non-code ad alta responsabilità** — la fonte autoritativa per
  l'analisi può essere un dato compilato da parser e **non versionato**, mentre
  Git conserva parser, regole e presentazioni ma non lo stato granulare. Qui la
  provenienza e la temporalità pesano più della verificabilità automatica.
- **dominio riflessivo** — fonti testuali elaborate, materiale grezzo e pratica
  personale: la fonte è meno meccanica e conta la tracciabilità interpretativa
  più del fact check automatico.

Il confronto impedisce una generalizzazione troppo tecnica. "Fonte di verità"
non significa sempre codice: può essere un JSON prodotto da parser, una tabella
esterna, un documento legale, una fonte testuale o una scelta interpretativa
dichiarata. La regola comune è esplicitare il livello di fiducia e non
verificare documentazione contro altra documentazione.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [world](world.md)
- [kb-tools](kb-tools.md)
- [knowledge-base](knowledge-base.md)
