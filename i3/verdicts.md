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
`goal.md` (`kb/verdict.md`, «Che cosa è un filo»); l'indice non li ripete.

- [audit-adottanti.md](audit-adottanti.md) — verdetto aggregato dell'audit
  mensile `/adottanti` (quarto battito 2026-10-01, puntuale): tutti e sei a
  `47d8204`, `aligned`, coincidenti coi file per il terzo giro; viste fresche
  verificate per rigenerazione; `crm` col plan fermo da 41 giorni. Il
  battito del 2026-11-01 conta i trailer `Esiti:` e decide se la verifica
  delle prescrizioni nei file si alleggerisce.
- [skill-per-arco-tripartito.md](skill-per-arco-tripartito.md) — la
  tripartizione `eval`/`exec` regge? Il 2026-09-24 è rimasta, con la
  clausola corretta perché gli esiti nulli non lasciavano traccia; si
  riapre il 2026-11-01 sui numeri del trailer `Esiti:`.
- [maturazione-nodi-fondativi.md](maturazione-nodi-fondativi.md) — tre
  ipotesi del canone attendono il caso che le decide: quarta regione della
  tipologia, matrice del ciclo, facet estese.
- [toolchain-builder-presentazione.md](toolchain-builder-presentazione.md) —
  i builder assumevano il toolchain degli host Linux: codifica UTF-8 e
  reveal.js scelto dalla versione di pandoc sono canone; resta aperto il
  controllo di freschezza tra host con pandoc diversi.
- [verdetto-piu-sicuro-del-materiale.md](verdetto-piu-sicuro-del-materiale.md)
  — la regola sulla provenienza è canone; resta aperto dove passa il confine
  della ricostruzione delegabile all'agente, e se le ritrattazioni salgono a
  canone.
