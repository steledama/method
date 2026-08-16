---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                                                     | Dip.      |
| ----- | --- | -------------------------------------------------------- | --------- |
| dev   | 3   | Enforcement della cucitura «agisci attraverso, ratifica» | pause [a] |
| dev   | 1   | Rivalutazione clausola di uscita skill per arco          | pause [b] |

Legenda dipendenze esterne:

`[a]` = trattenuto finché un write-through di canone non passa **inosservato** (o
arriva un secondo utente su un adottante): allora la disciplina manuale non scala
più e il task si attiva. Vedi `o2/enforcement-cucitura-canone.md`.

`[b]` = risveglio anticipato al battito `/adottanti` del **2026-09-01**:
decisione sulla base del primo mese d'uso e del confronto sui sei adottanti;
il 2026-11-01 resta solo fallback motivato se il materiale non fosse ancora
discriminante. Vedi `o2/rivalutazione-skill-per-arco.md`.

## Scadenze

- 2026-09-01 → `/adottanti`, audit runtime-o1 dei sei adottanti
  (mensile; secondo battito anticipato al 2026-08-01) → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md)

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
