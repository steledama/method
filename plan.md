# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                                     | Dip.   |
| --- | -------------------------------------------------------- | ------ |
| 1   | Verifica cicli annidati: 16 celle e mappa-sorgente       | —      |
| 2   | Chirurgia dei giganti e nodi fondativi (H-LAM/T)         | #1     |
| 3   | Disaccoppiamento adottante↔metodo: dichiara e taci       | #1, #2 |
| 4   | Strato di presentazione trasversale (deck→view)          | #3     |
| 5   | System image visiva: la home dell'atrio                  | #1, #4 |
| 6   | Goal di sviluppo: dimensioni comuni, posizione auspicata | \| [a] |

Legenda dipendenze esterne:

- `[a]` — `|` pausa tattica: ricollocare alla chiusura del gate (#1); appartiene
  al fronte fondativo, posizione provvisoria finché l'ordine non si riassesta.

L'ordine privilegia il **fronte teorico/fondativo** prima dell'**implementativo**
(riordinato il 2026-06-17). Siamo in una fase di flusso fondativo: la distinzione
dev/runtime e la ristrutturazione dei giganti stanno riscrivendo `action-cycle`,
`knowledge-base` e `README`, gli stessi hub da cui presentazione e home derivano.
Costruire l'implementazione prima che le fondamenta si posino è lavoro buttato —
lo si è già visto, la home era scopata male prima che `nested-cycles` fosse
esplicito. Le dipendenze `#n` codificano la cascata: tutto risale al **gate
(#1)**, e la **chirurgia (#2)** tocca gli hub una volta sola incorporando gli i2
già pronti di Clark e Norman (cfr. `verdict.md`, fili «I giganti ristrutturati» e
«Maturazione dei nodi fondativi»).

**Guardrail**, da non perdere: teoria-prima vale _in questa fase_, non come regola
permanente. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione
(`method-development`), e l'implementazione resta il _falsificatore_ della teoria
(`action-cycle-matrix`); la teoria qui è già grounded in disagi reali, e appena le
fondamenta si posano l'implementazione torna a fare da prova.

Il **task 6** (Goal di sviluppo) è teorico/fondativo — emerso dal gate, tocca
`goal` e `action-cycle`. È in **pausa tattica** (`|`): appartiene al fronte
fondativo, ma se ne tiene sospesa la collocazione finché il gate (#1) non chiude e
l'ordine si riassesta.

## Dettagli task

- [Verifica dei cicli annidati: 16 celle e mappa-sorgente](tasks/cicli-annidati-verifica.md)
- [Chirurgia dei giganti e nodi fondativi (H-LAM/T)](tasks/fonti-engelbart.md)
- [Disaccoppiamento adottante↔metodo: dichiara e taci](tasks/disaccoppiamento-adottanti.md)
- [Strato di presentazione trasversale (deck→view)](tasks/strato-presentazione.md)
- [System image visiva: la home dell'atrio](tasks/system-image-visiva.md)
- [Il polo Goal del ciclo di sviluppo: dimensioni comuni e posizione auspicata](tasks/goal-sviluppo-dimensioni.md)
