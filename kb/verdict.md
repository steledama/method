---
stato: maturo
---

# Verdict

I fili in `i3/` sono il verdetto attuale del progetto, per filo/area aperta. Stanno
nel cruscotto del ciclo di sviluppo, come lato valutazione: sono il **residuo scritto
dello stadio Compare (i3)** — la domanda «va bene?» rispetto agli obiettivi,
sedimentata perché il Goal successivo la legga (la cerniera KB: i3 scrive, il Goal
legge). Specchio di `plan`: `o1/plan.md` fotografa i task aperti (o1-sviluppo, lato output),
`i3/verdicts.md` indicizza i verdetti aperti (i3-sviluppo, lato input).

**Nome: sostantivo, non un log.** Doveva chiamarsi `compare.md`? No: i3 (Compare) è
più largo del solo confronto puntuale — copre anche la formazione del goal quando il
segnale è esogeno (cfr. `goal`, i due modi di i3: verdetto su goal noto / triage che
apre un goal nuovo). «Verdetto» è il sostantivo che copre entrambi: è il _risultato_
che i3 deposita, non l'atto. Resta valida la ragione che aveva escluso `compare.md`
— ma non esclude `verdict`, che è l'esito, non il verbo.

**Stato corrente, non cronaca.** Il git log dice _cosa_ è cambiato; ogni file-filo in
`i3/` dice _come stanno le cose ora_ su quel filo concettuale aperto, e _perché conta_. A ogni
commit, il check i3 del gate `/commit` si domanda: ciò che è cambiato in questa
sessione cambia il verdetto su un filo aperto? Se sì, il filo si aggiorna **in place**.
La cronologia delle revisioni di un filo è il git history del suo file — non
un accumulo di entry datate. Quando un filo si chiude (verdetto stabile, nessuna
tensione aperta), il file si rimuove: la storia resta in git, non qui.

**La cascata.** Un cambio di verdetto non finisce in sé stesso: può propagarsi a
`o1/plan.md`/`o2/` (priorità, dipendenze, nuovi task — `/plan-review`) o persino al
Goal stesso, quando il filo che cambia è di formazione-goal e non di verdetto su un
goal noto. Rendere esplicita questa domanda ad ogni commit è ciò che tiene scorrevole
il ciclo dell'azione e riduce il drift (cfr. `action-cycle`).

**I due presìdi.** Le regole dei fili hanno un guardiano capillare e uno
periodico: il gate `/commit` guarda una modifica alla volta («il verdetto
cambia?»); la skill `/verdicts-review` rivede periodicamente l'insieme dei fili
contro i segnali reali e il register `goal.md` — è la simmetrica di
`/plan-review` sul braccio di valutazione (cfr. `skill`). Ogni voce
dell'indice `verdicts.md` può portare l'annotazione `misura:` verso
l'obiettivo del register che il filo misura.

## Il verdetto non può essere più sicuro del materiale

L'i3 è lo stadio dove il progetto si racconta cosa è vero, ed è per questo il
punto in cui una deriva ha una **direzione**: verso la lettura più raccontabile.
Non è un rischio simmetrico da bilanciare con l'attenzione — la storia più
elegante è esattamente quella che disattiva l'attenzione mentre la merita di più
(tre episodi indipendenti in una sessione di `economia`, 2026-07-30: un filo più
ottimista del proprio task, una tesi costruita su una coincidenza, una cifra
diventata architrave senza essere mai stata una misura). L'elemento comune non
era l'accesso alle fonti: in tutti e tre i casi **il progetto aveva già in casa
ciò che smentiva**. Mancava ciò che obbliga a guardarlo.

Da qui due obblighi di forma, non di diligenza — la diligenza è precisamente ciò
che manca nel momento in cui la storia convince (cfr. `constraint`):

- **una quantità porta la propria provenienza**. Un numero che entra in un
  verdetto dichiara se è _misurato_, _dichiarato da un terzo_ o _derivato da
  dichiarazioni_, e con quale fiducia nella fonte. Senza marcatura una cifra
  derivata acquisisce col tempo lo stesso peso di una misurata, e la
  propagazione fra artefatti la consolida invece di eroderla: è il livello di
  fiducia che `source-of-truth` chiede di esplicitare, applicato al punto in cui
  il numero comincia a reggere una conclusione. Una quantità derivata non fa da
  architrave a un verdetto: se la tesi cade quando la cifra cade, la cifra va
  misurata prima, non dopo.
- **il materiale di casa si guarda prima**. La regola «non verificare
  documentazione contro altra documentazione» (`source-of-truth`) ha un angolo
  cieco: ciò che il progetto ha **prodotto di suo** — il file `o2/` che alimenta
  il filo, la propria corrispondenza in uscita, la valutazione di credibilità
  già scritta nella KB — è fonte primaria a tutti gli effetti, la più facile da
  consultare e la più dimenticata. Il file `o2/` in particolare è spesso la
  registrazione più fresca e più cauta di un filo, e il confronto filo↔`o2/` è il
  primo passo di `verdicts-review`, non un extra.

Regole:

- ogni file in `i3/`, escluso l'indice `verdicts.md`, è un filo/area aperta; il
  corpo è lo **stato attuale**, non una sequenza di entry datate
- non archivia output automatici completi (rigenerabili, vivono fuori di qui)
- non sostituisce git history
- non contiene task futuri se non come conseguenza interpretativa (→ `plan`/`o2`)
- cita commit, nodi o task quando chiariscono il contesto

## Formato canonico

La collezione ha un indice `i3/verdicts.md` con un preambolo breve (funzione,
convenzioni) e l'elenco dei fili aperti. Ogni filo vive in un file dedicato con
frontmatter `ciclo: dev|runtime`, H1 del filo e corpo in prosa. Il corpo è il
verdetto attuale, aggiornato in place quando il filo evolve:

```markdown
# Il filo / l'area aperta

Stato attuale: cosa è deciso, cosa resta in tensione, cosa dipende da cosa.
Il commit `abc1234` è il puntatore alla storia verificabile, se serve.
```

Un file-filo include anche il frontmatter:

```yaml
---
ciclo: dev
---
```

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [affordance-signifier](affordance-signifier.md)
- [git-history](git-history.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [project-structure](project-structure.md)
- [source-of-truth](source-of-truth.md)
- [constraint](constraint.md)
