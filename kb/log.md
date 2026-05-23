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

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | `log.md` corposo e coerente con cambi strutturali, audit e decisioni tecniche. | Buon esempio di memoria interpretativa sopra git: non sostituisce i diff, spiega perché contano. |
| `bi` | `log.md` corposo, utile per seguire evoluzioni applicative e refactor. | Adeguato al dominio, ma va mantenuta la distinzione tra decisione e output operativo. |
| `economia` | `log.md` più breve, affiancato da `stato.md`, `scadenze.md` e `diario.md`. | Adattamento legittimo: il log non deve diventare stato corrente, perché quello vive in file locali specializzati. |
| `salute` | Il progetto ha `log.md` e anche `diario.md`; il diario è più personale e riflessivo. | Chiarisce una distinzione utile: log = memoria del progetto, diario = materiale personale o filing back potenziale. |

Il confronto suggerisce che il metodo dovrebbe nominare esplicitamente i file locali affini al log. `diario.md`, `stato.md` e `scadenze.md` non violano la ricetta se la loro funzione è distinta e se non sostituiscono il log interpretativo.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [git-history](git-history.md)
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [struttura-progetto](struttura-progetto.md)
