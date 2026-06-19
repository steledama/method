# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                                     | Dip.    |
| --- | -------------------------------------------------------- | ------- |
| 1   | Verifica cicli annidati: 16 celle e mappa-sorgente       | —       |
| 2   | Ingest fonti mente estesa (Andy Clark)                   | —       |
| 3   | Fonti Norman: Things That Make Us Smart (integrale)      | —       |
| 4   | Fonti Engelbart e chirurgia dei giganti (H-LAM/T)        | 1, 2, 3 |
| 5   | Disaccoppiamento adottante↔metodo: dichiara e taci       | 1, 4    |
| 6   | Strato di presentazione trasversale (deck→view)          | 5       |
| 7   | System image visiva: la home dell'atrio                  | 1, 6    |
| 8   | Goal di sviluppo: dimensioni comuni, posizione auspicata | —       |

L'ordine privilegia il **fronte teorico/fondativo (1-4)** prima di quello
**implementativo (5-7)**, riordinato il 2026-06-17. Siamo in una fase di flusso
fondativo: la distinzione dev/runtime e la ristrutturazione dei giganti stanno
riscrivendo `action-cycle`, `knowledge-base` e `README`, gli stessi nodi da cui
presentazione e home derivano. Costruire l'implementazione prima che le fondamenta
si posino è lavoro buttato — lo si è già visto, la home era scopata male prima che
`nested-cycles` fosse esplicito.

**Guardrail**, da non perdere: teoria-prima vale _in questa fase_, non come regola
permanente. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione
(`method-development`), e l'implementazione resta il _falsificatore_ della teoria
(`action-cycle-matrix`); la teoria qui è già grounded in disagi reali, e appena le
fondamenta si posano l'implementazione torna a fare da prova.

Sul fronte teorico: la **verifica cicli (1)** è il gate dev/runtime, senza blocchi
esterni, e precede la **chirurgia dei giganti (4)** perché entrambe toccano l'hub
`action-cycle` e va sfregato una volta sola. **Clark (2)** e **Norman/TTMUS (3)** sono
ingest del pavimento ontologico già distillati (i2 fatto): il loro i3 non è una passata
a sé ma confluisce nella **revisione coordinata dei nodi fondativi** che è la chirurgia
(4) — per questo (4) dipende da 1, 2 e 3, e si toccano gli hub una volta sola.

Sul fronte implementativo: il **disaccoppiamento (5)** ha un nucleo indipendente
(ripulire i link accidentali negli adottanti), ma la sua sezione README canonica —
poli Goal/World, ora due World e cornice H-LAM/T — è informata dalla teoria, quindi
segue 1 e 4 per non ridefinire lo schema due volte. La **presentazione (6)** viene
dopo il disaccoppiamento (il rename deck→view propaga a costo quasi nullo); la
**home (7)** dopo presentazione e gate (il toggle dev/runtime dipende dall'esito di 1).

Il **task 8** (Goal di sviluppo) è teorico/fondativo — emerso dal gate (1), tocca
`goal` e `action-cycle`. La sua posizione in coda è **provvisoria**: appartiene al
fronte fondativo e va ricollocato alla chiusura del gate, quando l'ordine si riassesta.

## Dettagli task

- [Verifica dei cicli annidati: 16 celle e mappa-sorgente](tasks/cicli-annidati-verifica.md)
- [Ingest fonti mente estesa (Andy Clark)](tasks/fonti-mente-estesa.md)
- [Fonti Norman: Things That Make Us Smart (integrale)](tasks/fonti-norman-ttmus.md)
- [Fonti Engelbart e chirurgia dei giganti (H-LAM/T)](tasks/fonti-engelbart.md)
- [Disaccoppiamento adottante↔metodo: dichiara e taci](tasks/disaccoppiamento-adottanti.md)
- [Strato di presentazione trasversale (deck→view)](tasks/strato-presentazione.md)
- [System image visiva: la home dell'atrio](tasks/system-image-visiva.md)
- [Il polo Goal del ciclo di sviluppo: dimensioni comuni e posizione auspicata](tasks/goal-sviluppo-dimensioni.md)
