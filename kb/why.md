---
data: 2026-06-06
stato: maturo
---

# Why

`why.md` è la memoria interpretativa delle decisioni significative. Risponde alla domanda: perché una decisione o una sessione conta? Non registra tutto ciò che accade; registra ciò che serve a capire il senso delle evoluzioni del progetto. Sta in root, nel cruscotto del ciclo di sviluppo, come lato valutazione: è il **residuo scritto dello stadio Compare (i3)** — la domanda «va bene?» rispetto agli obiettivi, sedimentata perché il Goal successivo la legga (la cerniera KB: i3 scrive, il Goal legge).

Da qui la linea che separa `why` dal log, e il modo tipico in cui un `why.md` tradisce la sua funzione: un'entry che racconta _cosa_ è stato fatto appartiene a git; un'entry di `why` porta un _verdetto_ — perché conta, se va bene, cosa cambia nella valutazione. Il drift verso la cronaca di azioni è esattamente ciò che la distinzione «git dice cosa, `why` dice perché conta» deve presidiare.

Il git log dice cosa è cambiato. `why.md` dice perché quel cambiamento ha importanza, quale problema risolve, quale decisione stabilizza o quale direzione apre. Questa distinzione evita sia il diario prolisso sia la perdita del contesto decisionale.

La chiave organizzativa è la **motivazione**, non la data. Le entry si raggruppano per la decisione o il filo concettuale che illuminano; la data è un metadato che vive _dentro_ il gruppo. È una scelta di affordance ([[affordance-signifier]]): il signifier «log datato» invita ad accodare note di sessione e compete con git sull'asse che git già possiede — il tempo. Indicizzare per motivazione rende `why` ortogonale e complementare a git, che resta la fonte dell'asse cronologico completo.

Regole:

- registra decisioni, revisioni strutturali, ingest importanti e cambi di approccio
- ogni entry porta un verdetto (perché conta / va bene?), non una cronaca di azioni: la cronaca è di git
- non archivia output automatici completi
- non sostituisce git history
- non contiene task futuri se non come conseguenza interpretativa
- deve essere leggibile come memoria del progetto
- cita commit, nodi o task quando chiariscono il contesto

## Formato canonico

Il file ha un preambolo breve, poi una riga separatrice `---`, poi i **gruppi di motivazione**. Il preambolo contiene titolo, funzione del file e le convenzioni. Ogni gruppo è un heading `##` (la motivazione, con una riga di intro in corsivo); dentro ogni gruppo le entry sono heading `###` con la decisione come titolo-tesi, la **data come metadato** in prefisso `[YYYY-MM-DD]`, e il **commit citabile inline**:

```markdown
# why.md

Memoria interpretativa: il git log dice cosa è cambiato, qui sta perché conta.
La chiave è la motivazione; la data vive dentro il gruppo.

---

## La motivazione / il filo concettuale

_Una riga che inquadra cosa tiene insieme questo gruppo._

### [YYYY-MM-DD] La decisione, scritta come tesi

Perché conta, quale tensione risolve, cosa apre. Il commit `abc1234` è il puntatore.
```

Regole di forma:

- **Per motivazione, non per data.** Si clusterizzano solo i temi già stabilizzati (guardia bottom-up: niente scaffali vuoti per temi futuri). Una entry nuova si aggiunge al gruppo pertinente, o ne fonda uno solo se il filo è davvero emerso.
- **Dentro il gruppo, dalla più recente.** La cronologia di una singola idea è significativa (evoluzione, ritrattazioni); l'ordine intra-gruppo la rende leggibile.
- **Supersessione esplicita.** Un'entry superata resta in posizione e riceve una riga `> ↳ …` verso quella che la corregge — la traccia non si cancella (git la conserva comunque).
- **Multi-tema.** Un'entry che tocca più motivazioni vive nel gruppo più pertinente e rimanda agli altri con `[[…]]` o per titolo.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                               | Confronto con il metodo                                                                               |
| ---------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `nixos`    | 9 gruppi per motivazione; i dump erano già potati.                               | Le entry `[storico]` confermano che la data è asse secondario.                                        |
| `bi`       | 7 gruppi per motivazione; dump audit estratti in uno snapshot operativo.         | Decisioni e output macchina sono nuovamente separati.                                                 |
| `economia` | 4 gruppi per motivazione, affiancati da `stato.md`, `scadenze.md` e `diario.md`. | La memoria resta distinta da stato corrente, prossime azioni e resoconto periodico.                   |
| `salute`   | 4 gruppi per motivazione; `diario.md`, storia clinica e quadro restano separati. | La memoria del progetto resta distinta da esperienza personale, cronologia clinica e stato operativo. |

Il confronto suggerisce che il metodo dovrebbe nominare esplicitamente i file locali affini. `diario.md`, `stato.md` e `scadenze.md` non violano la ricetta se la loro funzione è distinta e se non sostituiscono la memoria interpretativa.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [affordance-signifier](affordance-signifier.md)
- [git-history](git-history.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [struttura-progetto](struttura-progetto.md)
