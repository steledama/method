---
data: 2026-06-06
stato: bozza
---

# Why

`why.md` è la memoria interpretativa append-only delle decisioni significative. Risponde alla domanda: perché una decisione o una sessione conta? Non registra tutto ciò che accade; registra ciò che serve a capire il senso delle evoluzioni del progetto. Sta in root, nel cruscotto del ciclo di sviluppo, come lato valutazione: il residuo scritto delle operazioni di Compare.

Il git log dice cosa è cambiato. `why.md` dice perché quel cambiamento ha importanza, quale problema risolve, quale decisione stabilizza o quale direzione apre. Questa distinzione evita sia il diario prolisso sia la perdita del contesto decisionale.

Regole:

- registra decisioni, revisioni strutturali, ingest importanti e cambi di approccio
- non archivia output automatici completi
- non sostituisce git history
- non contiene task futuri se non come conseguenza interpretativa
- deve essere leggibile come memoria del progetto
- cita commit, nodi o task quando chiariscono il contesto

## Formato canonico

Il file ha un preambolo breve e poi le entry. Il preambolo contiene titolo, funzione del file e formato delle entry. Dopo il preambolo una riga separatrice `---`; la prima entry inizia sotto quel separatore.

Il modello dell'entry mette **la decisione come chiave** — il titolo è ciò che si è stabilito, non un'etichetta di tipo — la **data come metadato** e il **commit citabile inline** come puntatore alla storia verificabile:

```markdown
# why.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta.

---

## [YYYY-MM-DD] La decisione, scritta come tesi

Perché conta, quale tensione risolve, cosa apre. Il commit `abc1234` è il puntatore.
```

La riga `---` non è decorazione: separa le istruzioni stabili del file dalla memoria append-only. Le entry si aggiungono in ordine cronologico inverso (la più recente in cima), senza riordinare entry storiche senza motivo.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                   | Confronto con il metodo                                                                                             |
| ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | `why.md` corposo e coerente con cambi strutturali, audit e decisioni tecniche.       | Buon esempio di memoria interpretativa sopra git: non sostituisce i diff, spiega perché contano.                    |
| `bi`       | `why.md` corposo, utile per seguire evoluzioni applicative e refactor.               | Adeguato al dominio, ma va mantenuta la distinzione tra decisione e output operativo.                               |
| `economia` | `why.md` più breve, affiancato da `stato.md`, `scadenze.md` e `diario.md`.           | Adattamento legittimo: la memoria non deve diventare stato corrente, perché quello vive in file locali specializzati.   |
| `salute`   | Il progetto ha `why.md` e anche `diario.md`; il diario è più personale e riflessivo. | Chiarisce una distinzione utile: why = memoria del progetto, diario = materiale personale o filing back potenziale. |

Il confronto suggerisce che il metodo dovrebbe nominare esplicitamente i file locali affini. `diario.md`, `stato.md` e `scadenze.md` non violano la ricetta se la loro funzione è distinta e se non sostituiscono la memoria interpretativa.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [git-history](git-history.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [struttura-progetto](struttura-progetto.md)
