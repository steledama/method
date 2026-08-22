---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                                            | Dip. |
| ----- | --- | ----------------------------------------------- | ---- |
| dev   | 1   | Rivalutazione clausola di uscita skill per arco | p1   |

Legenda dipendenze esterne:

`p1` = risveglio anticipato al battito `/adottanti` del **2026-09-01**:
decisione sulla base del primo mese d'uso e del confronto sui sei adottanti;
il 2026-11-01 resta solo fallback motivato se il materiale non fosse ancora
discriminante. Vedi `o2/rivalutazione-skill-per-arco.md`.

## Scadenze

- 2026-09-01 → `/adottanti`, audit runtime-o1 dei sei adottanti
  (mensile; secondo battito anticipato al 2026-08-01) → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md). Il giro verifica anche il
  recepimento delle tre prescrizioni aperte in `o3/` e le baseline dei due
  ingressi del 2026-08-12.

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
