---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                                                                        | Dip.      |
| ----- | --- | --------------------------------------------------------------------------- | --------- |
| dev   | 1   | Trasloca il marker di allineamento a `i3/`, aggiorna prescrizione e propaga | —         |
| dev   | S   | Redraw tavole vista Interpretazioni (residui cosmetici)                     | —         |
| dev   | 3   | Enforcement della cucitura «agisci attraverso, ratifica»                    | pause [a] |
| dev   | 1   | Rivalutazione clausola di uscita skill per arco                             | pause [b] |
| dev   | 1   | Rinomina le skill secondo la regola sostantivo, propaga i casi canonici     | world [c] |

Legenda dipendenze esterne:

`[a]` = trattenuto finché un write-through di canone non passa **inosservato** (o
arriva un secondo utente su un adottante): allora la disciplina manuale non scala
più e il task si attiva. Vedi `o2/enforcement-cucitura-canone.md`.

`[b]` = risveglio al battito `/adottanti` del **2026-11-01**, il terzo
successivo al recepimento della rifilatura dai quattro (chiuso il
2026-08-01). Vedi `o2/rivalutazione-skill-per-arco.md`.

`[c]` = rename e riferimenti già applicati in `metodo`; resta il recepimento
dei quattro adottanti della prescrizione `o3/skill-nomi-verbo-sostantivo.md`.
Vedi `o2/skill-nomi-verbo-sostantivo.md`.

## Scadenze

- 2026-09-01 → `/adottanti`, audit runtime-o1 dei quattro adottanti
  (mensile; secondo battito anticipato al 2026-08-01) → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md)

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
