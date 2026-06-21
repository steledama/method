# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                                     | Dip. |
| --- | -------------------------------------------------------- | ---- |
| 1   | Chirurgia dei giganti e nodi fondativi (H-LAM/T)         | —    |
| 2   | Goal di sviluppo: dimensioni comuni, posizione auspicata | #1   |
| 3   | Disaccoppiamento adottante↔metodo: dichiara e taci       | #1   |
| 4   | Strato di presentazione trasversale (deck→view)          | #3   |
| 5   | System image visiva: la home dell'atrio                  | #4   |

Il **gate dei cicli annidati è chiuso** (ratificato a freddo, 2026-06-21, cfr.
`verdict.md` e `kb/action-cycle-matrix.md`): l'annidamento regge — due cicli
genuini, con l'interno runtime **nascente** (l'osservatorio sugli adottanti è
i2/o2-runtime, una sola istanza; runtime-o1 il gap top-down, scoccato una volta
ma senza protocollo d'audit). La mappa-sorgente dei 16 elementi è prodotta e
ri-sorgentata a freddo: è ciò che la presentazione e la home consumano.

L'ordine privilegia il **fronte fondativo** (1-2) prima dell'**implementativo**
(3-5). La **chirurgia (#1)** è la radice: riscrive gli hub `action-cycle`,
`cognitive-system`, `knowledge-base` e `README` incorporando in una passata sola
gli i2 già pronti di Engelbart, Clark e Norman (cfr. `verdict.md`, fili «I giganti
ristrutturati» e «Maturazione dei nodi fondativi») — gli stessi hub si toccano una
volta sola. Il **Goal di sviluppo (#2)** segue la chirurgia perché tocca lo stesso
hub `action-cycle`/`goal` e scioglie lo split Goal-dev/Goal-runtime lasciato
provvisorio dal gate.

**Guardrail**, da non perdere: teoria-prima vale _in questa fase_, non come regola
permanente. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione
(`method-development`), e l'implementazione resta il _falsificatore_ della teoria
(`action-cycle-matrix`); la teoria qui è già grounded in disagi reali, e appena le
fondamenta si posano l'implementazione torna a fare da prova.

Sul fronte implementativo: il **disaccoppiamento (#3)** ha un nucleo indipendente
(ripulire i link accidentali negli adottanti), ma la sua sezione README canonica —
ora con due poli World e la revisione di «non orchestra» suffragata dall'arco
top-down scoccato — segue la chirurgia per non ridefinire lo schema due volte. La
**presentazione (#4)** viene dopo (il rename deck→view propaga a costo quasi
nullo); la **home (#5)** dopo presentazione, e consuma la mappa-sorgente del gate.

## Dettagli task

- [Chirurgia dei giganti e nodi fondativi (H-LAM/T)](tasks/fonti-engelbart.md)
- [Il polo Goal del ciclo di sviluppo: dimensioni comuni e posizione auspicata](tasks/goal-sviluppo-dimensioni.md)
- [Disaccoppiamento adottante↔metodo: dichiara e taci](tasks/disaccoppiamento-adottanti.md)
- [Strato di presentazione trasversale (deck→view)](tasks/strato-presentazione.md)
- [System image visiva: la home dell'atrio](tasks/system-image-visiva.md)
