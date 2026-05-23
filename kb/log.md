---
data: 2026-05-23
stato: bozza
---

# Log

log.md è la memoria interpretativa append-only delle sessioni significative. Risponde alla domanda: perché una decisione o una sessione conta? Non registra tutto ciò che accade; registra ciò che serve a capire il senso delle evoluzioni del progetto.

Il git log dice cosa è cambiato. log.md dice perché quel cambiamento ha importanza, quale problema risolve, quale decisione stabilizza o quale direzione apre. Questa distinzione evita sia il diario prolisso sia la perdita del contesto decisionale.

Regole:

- registra decisioni, revisioni strutturali, ingest importanti e cambi di approccio
- non archivia output automatici completi
- non sostituisce git history
- non contiene task futuri se non come conseguenza interpretativa
- deve essere leggibile come memoria del progetto
- può citare commit, nodi o task quando chiariscono il contesto

Connessioni:

- [metodo-kb](metodo-kb.md)
- [git-history](git-history.md)
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [struttura-progetto](struttura-progetto.md)
