---
data: 2026-06-13
stato: maturo
---

# Verdict

`verdict.md` è il verdetto attuale del progetto, per filo/area aperta. Sta in root,
nel cruscotto del ciclo di sviluppo, come lato valutazione: è il **residuo scritto
dello stadio Compare (i3)** — la domanda «va bene?» rispetto agli obiettivi,
sedimentata perché il Goal successivo la legga (la cerniera KB: i3 scrive, il Goal
legge). Specchio di `plan`: `plan.md` fotografa i task aperti (o1, lato output),
`verdict.md` fotografa i verdetti aperti (i3, lato input).

**Nome: sostantivo, non un log.** Doveva chiamarsi `compare.md`? No: i3 (Compare) è
più largo del solo confronto puntuale — copre anche la formazione del goal quando il
segnale è esogeno (cfr. `goal`, i due modi di i3: verdetto su goal noto / triage che
apre un goal nuovo). «Verdetto» è il sostantivo che copre entrambi: è il _risultato_
che i3 deposita, non l'atto. Resta valida la ragione che aveva escluso `compare.md`
— ma non esclude `verdict`, che è l'esito, non il verbo.

**Stato corrente, non cronaca.** Il git log dice _cosa_ è cambiato; `verdict.md` dice
_come stanno le cose ora_ su ciascun filo concettuale aperto, e _perché conta_. A ogni
commit, il check i3 del gate `/commit` si domanda: ciò che è cambiato in questa
sessione cambia il verdetto su un filo aperto? Se sì, il filo si aggiorna **in place**.
La cronologia delle revisioni di un filo è il git history di questo file stesso — non
un accumulo di entry datate. Quando un filo si chiude (verdetto stabile, nessuna
tensione aperta), il gruppo si rimuove: la storia resta in git, non qui.

**La cascata.** Un cambio di verdetto non finisce in sé stesso: può propagarsi a
`plan.md`/`tasks/` (priorità, dipendenze, nuovi task — `/tasks-review`) o persino al
Goal stesso, quando il filo che cambia è di formazione-goal e non di verdetto su un
goal noto. Rendere esplicita questa domanda ad ogni commit è ciò che tiene scorrevole
il ciclo dell'azione e riduce il drift (cfr. `ciclo-azione`).

Regole:

- ogni gruppo `##` è un filo/area aperta; il corpo è lo **stato attuale**, non una
  sequenza di entry datate
- non archivia output automatici completi (rigenerabili, vivono fuori di qui)
- non sostituisce git history
- non contiene task futuri se non come conseguenza interpretativa (→ `plan`/`tasks`)
- cita commit, nodi o task quando chiariscono il contesto

## Formato canonico

Il file ha un preambolo breve (funzione, convenzioni), poi una riga separatrice `---`,
poi i **gruppi per filo**. Ogni gruppo è un heading `##` con il nome del filo; il
corpo è il verdetto attuale, scritto in prosa, aggiornato in place quando il filo
evolve:

```markdown
# verdict.md

Il verdetto attuale del progetto, per filo/area aperta — non un log.

---

## Il filo / l'area aperta

Stato attuale: cosa è deciso, cosa resta in tensione, cosa dipende da cosa.
Il commit `abc1234` è il puntatore alla storia verificabile, se serve.
```

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [ciclo-azione](ciclo-azione.md)
- [goal](goal.md)
- [affordance-signifier](affordance-signifier.md)
- [git-history](git-history.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [struttura-progetto](struttura-progetto.md)
