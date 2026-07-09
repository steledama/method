---
ciclo: runtime
---

# Segnale: la coppia di review simmetriche piano/verdetti, nata in bi

Data: 2026-07-09 · Fonte: `bi`, subito dopo la materializzazione del register
`goal.md` (cfr. percezione `goal-register-materializzato-in-bi`)

## Il segnale

Con il register `goal.md` in mano è emersa un'asimmetria architetturale nella
supervisione del ciclo. Il braccio di **esecuzione** aveva due cure: quella
alla scrittura (il filing back della skill `commit`) e quella periodica (la
skill `tasks-review`: igiene, dipendenze, priorità). Il braccio di
**valutazione** aveva solo la prima: lo step «il verdetto cambia?» di `commit`
è un hook per-commit che guarda una modifica alla volta; nessuno rivedeva mai
l'insieme dei fili `i3/` — se ogni filo è ancora vero rispetto ai segnali, se
dovrebbe chiudersi, se è degenerato in log, se esistono tensioni aperte senza
filo.

`bi` ha chiuso l'asimmetria con una coppia nominata:

- **`plan-review`** (rinomina di `tasks-review`): tiene onesto il piano —
  o1/o2, più la lente task→obiettivo verso il register;
- **`verdicts-review`** (nuova): tiene onesto il confronto — quattro domande
  per filo (è vero? è aperto? è _un_ filo? è stato, non log?), copertura
  bidirezionale obiettivo⟷segnale/filo, bonifica del plan dalla narrativa di
  stato, e il modo due dell'i3 (formazione goal, sempre in proposta).

`goal.md` è la cerniera che le due skill controllano da versanti opposti.

## L'attrito osservato (il sintomo che ha rivelato il buco)

Senza la review di valutazione, la narrativa di stato del mondo cola nel plan.
In `bi`: la sezione Note di `o1/plan.md` accumulava guardrail, verdetti su
proprietà del drift e fondazioni consegnate. In `economia` il sintomo è più
avanzato: il plan è 147 righe di cui 15 di tabella — la sezione «Cause delle
attese e delle pause» (46 righe) è fatta di debrief telefonici, posizioni
negoziali e letture convergenti: **mini-fili i3 mai nati**, parcheggiati nel
plan perché la colonna `Dip.` (`world`, `pause`) esige una giustificazione di
stato e non c'era un posto supervisionato dove metterla.

## Da valutare (i2→i3, non qui)

1. La **rinomina** `tasks-review` → `plan-review` tocca il canone: il nodo
   `kb/skill.md` e le bussole degli adottanti citano `tasks-review` per nome.
   Ratificare la simmetria nominale (`plan-review` : o1 :: `verdicts-review` :
   i3) o tenere il nome storico?
2. La **coppia** generalizza come pattern di canone (due review, una per
   braccio, col register Goal come cerniera)? La skill `verdicts-review` di
   `bi` è scritta in forma già portabile.
3. Il banco più severo non è `bi` ma **`economia`**, dove il sintomo è più
   avanzato e il register Goal non esiste ancora: candidato naturale a secondo
   adottante di register + coppia.

La coppia vive in `bi@52b2b600` (`.claude/skills/plan-review/`,
`.claude/skills/verdicts-review/`, filing back in README/CLAUDE/goal/
prescriptions).
