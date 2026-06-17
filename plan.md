# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                               | Dip. |
| --- | -------------------------------------------------- | ---- |
| 1   | Disaccoppiamento adottante↔metodo: dichiara e taci | —    |
| 2   | Verifica cicli annidati: 16 celle e mappa-sorgente | —    |
| 3   | Strato di presentazione trasversale (deck→view)    | 2    |
| 4   | System image visiva: la home dell'atrio            | 2, 3 |
| 5   | Fonti pace-layering e maturazione nodo             | —    |
| 6   | Ingest fonti mente estesa (Andy Clark)             | —    |
| 7   | Fonti Engelbart e ridimensionamento di Karpathy    | —    |

I task 1-4 sono il cluster presentazione, aperto dalla sessione di design
2026-06-15 (allargamento della system image) e ridefinito il 2026-06-17 con la
distinzione dev/runtime. Il disaccoppiamento va per primo: riducendo i
riferimenti diffusi negli adottanti, il rename deck→view del task 3 propaga a
costo quasi nullo. Il task 2 è un gate di verifica precedente alla presentazione:
mette alla prova l'ipotesi dei due cicli annidati prima di costruirne la
rappresentazione, e può falsificarla o riformarla (cfr. `nested-cycles`).

I task 5-7 sono il fronte fonti, tutti dall'alto e senza dipendenze tecniche. Il
task 7 (Engelbart) ha già **fonte letta e decisione presa** — la cornice di sistema
H-LAM/T, cfr. `verdict.md` filo «I giganti ristrutturati» — ma due punti restano
formalizzati come vincolo, non come lavoro immediato:

- **Timing**: il suo residuo, la **chirurgia dei nodi fondativi** (`action-cycle` e
  il nodo nuovo `augmentation-system`), è una **passata deliberata a sé**, non da
  fare a caldo — è un hub ad alto rischio (33 backlink).
- **Debiti di fonte**: la chirurgia è gated dal pavimento ontologico non saldato,
  condiviso col task 6 — la Sez. III di Engelbart non è letta, Hutchins non vive in
  `world` (citato-non-sourced), di Clark è procurato solo _The Extended Mind_. Può
  procedere dichiarando il debito o dopo averne saldato almeno uno (la Sez. III è
  immediata).

## Dettagli task

- [Disaccoppiamento adottante↔metodo: dichiara e taci](tasks/disaccoppiamento-adottanti.md)
- [Verifica dei cicli annidati: 16 celle e mappa-sorgente](tasks/cicli-annidati-verifica.md)
- [Strato di presentazione trasversale (deck→view)](tasks/strato-presentazione.md)
- [System image visiva: la home dell'atrio](tasks/system-image-visiva.md)
- [Fonti pace-layering e maturazione nodo](tasks/fonti-pace-layering.md)
- [Ingest fonti mente estesa (Andy Clark)](tasks/fonti-mente-estesa.md)
- [Fonti Engelbart e ridimensionamento di Karpathy fra i giganti](tasks/fonti-engelbart.md)
