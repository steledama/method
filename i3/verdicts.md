# Verdicts

Indice della collezione `i3/`: lo **stadio i3** (Compare) del ciclo — il
verdetto attuale del progetto, un file per tensione aperta misurata contro un obiettivo, non un log. Il git
log dice _cosa_ è cambiato; ogni filo dice _come stanno le cose ora_ e _perché
conta_. Specchio di `o1/plan.md` sul lato valutazione: `plan.md` fotografa i
task aperti (o1), i fili qui i verdetti aperti (i3). Forma e disciplina
canoniche in [`kb/verdict.md`](../kb/verdict.md).

Ogni filo è lo **stato attuale**, aggiornato in place, non una sequenza di entry
datate (la cronologia di un filo è il git history del suo file). Quando un filo
si chiude — verdetto stabile, nessuna tensione aperta e nessuna altra funzione
viva — il file si rimuove: la storia resta in git. Cursori e contratti correnti
restano, come previsto da `kb/verdict.md`. Il commit citato inline è il puntatore alla storia
verificabile.

## Contenuti

Ogni filo dichiara nel frontmatter `ciclo` e `obiettivo`, verificato contro
`goal.md` (`kb/verdict.md`, «Che cosa è un filo»). L'indice porta solo la
domanda del filo: stato, date ed esiti vivono nel file, aggiornato in place.

- [audit-adottanti.md](audit-adottanti.md) — verdetto aggregato dell'audit
  mensile `/adottanti`: il canone arriva agli adottanti e quanto distano dal
  telos?
- [ciclo-autonomo.md](ciclo-autonomo.md) — con quali garanzie ogni repo
  arriva al giro `eval` → `exec` → commit senza custode?
- [skill-per-arco-tripartito.md](skill-per-arco-tripartito.md) — la
  tripartizione `eval`/`exec` regge?
- [maturazione-nodi-fondativi.md](maturazione-nodi-fondativi.md) — le
  ipotesi del canone che attendono il caso che le decide.
- [toolchain-builder-presentazione.md](toolchain-builder-presentazione.md) —
  quanto del toolchain degli host i builder possono assumere?
- [verdetto-piu-sicuro-del-materiale.md](verdetto-piu-sicuro-del-materiale.md)
  — dove passa il confine della ricostruzione delegabile all'agente?
