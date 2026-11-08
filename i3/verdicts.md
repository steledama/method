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
  mensile `/adottanti`. Quinto audit il 2026-11-02, sui sei adottanti:
  marker `aligned` al 29/10 e coincidenti coi file per la quarta volta,
  quindi la verifica d'insieme si alleggerisce. Viste fresche in tutte e
  sette, `danea2` compreso. Tutti e sei girano da soli ogni giorno, e
  `baserow` ha chiuso il fronte backup. Gli esiti per stadio hanno dato il
  verdetto sulle skill per arco. Tre prescrizioni recepite nei file sono
  chiuse a mano, perché `prescrizioni.py` non riconosceva la forma dei
  marker.
- [ciclo-autonomo.md](ciclo-autonomo.md) — direzione costitutiva dal
  2026-10-11: con quali garanzie ogni repo arriva al giro `eval` → `exec` →
  commit senza custode? Piloti `salute` e `crm` a gradini. Push autonomo in `method` e
  prescritto ai sette; delega dei cicli avviati dal custode ratificata in
  `autonomy.md`, con Goal aggiornato; primi 18 casi della delega da tre
  adottanti, residuo nel checkout servito; timer acceso in `method` e nei sette
  adottanti, `crm` dismesso il 2026-10-22. Riesaminato il 2026-11-02, prossimo riesame il 2026-12-01,
  verdetto alla fine del pilota su fedeltà, delega, visibilità degli arresti
  e costo della supervisione.
- [skill-per-arco-tripartito.md](skill-per-arco-tripartito.md) — la
  tripartizione `eval`/`exec` regge? Il 2026-09-24 è rimasta, con la
  clausola corretta perché gli esiti nulli non lasciavano traccia. Il
  2026-11-02, sui numeri del trailer `Esiti:`, resta così per adesso; la
  clausola vale senza data.
- [maturazione-nodi-fondativi.md](maturazione-nodi-fondativi.md) — tre
  ipotesi del canone attendono il caso che le decide: quarta regione della
  tipologia, matrice del ciclo, facet estese.
- [toolchain-builder-presentazione.md](toolchain-builder-presentazione.md) —
  i builder assumevano il toolchain degli host Linux: codifica, reveal.js
  dalla versione di pandoc, link al disco locale e fine riga sono canone,
  recepito dai sei; il rumore di toolchain nel gate si è sciolto in `metodo`
  con le viste fuori da git; resta aperta la soglia di pandoc per i percorsi
  di reveal.js.
- [verdetto-piu-sicuro-del-materiale.md](verdetto-piu-sicuro-del-materiale.md)
  — la regola sulla provenienza è canone; resta aperto dove passa il confine
  della ricostruzione delegabile all'agente, e se le ritrattazioni salgono a
  canone.
