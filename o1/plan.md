---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                                            | Dip.                                                                                           |
| ----- | --- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| dev   | S   | Criteri del ciclo autonomo schedulato           | —                                                                                              |
| dev   | S   | Home con fatto e da fare                        | —                                                                                              |
| dev   | S   | Dove gira il ciclo autonomo                     | —                                                                                              |
| dev   | S   | Pilota del ciclo autonomo                       | ↳ Criteri del ciclo autonomo schedulato; Home con fatto e da fare; Dove gira il ciclo autonomo |
| dev   | 1   | Rivalutazione clausola di uscita skill per arco | p1                                                                                             |

Legenda dipendenze esterne:

`p1` = audit `/adottanti` del **2026-11-01**: il risveglio conta gli
esiti per stadio nei trailer `Esiti:` registrati dopo il recepimento di
`o3/esiti-per-stadio-nel-commit.md`. Vedi `o2/rivalutazione-skill-per-arco.md`.

## Scadenze

- 2026-11-01 → `/adottanti`, audit runtime-o1 mensile dei sette adottanti
  → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md). Il giro conta i
  trailer `Esiti:` per stadio e per repository (risveglio di `p1`) e
  conferma o meno che `aligned` e i file coincidono. Riesame del filo
  [i3/ciclo-autonomo.md](../i3/ciclo-autonomo.md): avanzamento del
  percorso e riscontri sulla prima delega.

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
