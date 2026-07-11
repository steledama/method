---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Task                                                     | Dip.      |
| ----- | -------------------------------------------------------- | --------- |
| dev   | Redraw tavole vista Interpretazioni (residui cosmetici)  | —         |
| dev   | Protocollo runtime-o1 (audit periodico top-down)         | —         |
| dev   | Enforcement della cucitura «agisci attraverso, ratifica» | pause [a] |

Legenda dipendenze esterne:

`[a]` = trattenuto finché un write-through di canone non passa **inosservato** (o
arriva un secondo utente su un adottante): allora la disciplina manuale non scala
più e il task si attiva. Vedi `o2/enforcement-cucitura-canone.md`.

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
