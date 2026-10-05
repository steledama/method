---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo   | Ob. | Task                                            | Dip. |
| ------- | --- | ----------------------------------------------- | ---- |
| runtime | 2   | Ingresso di baserow nell'osservatorio           | w1   |
| dev     | 1   | Ipotesi e confronti i2/i3                       | —    |
| dev     | 1   | Rivalutazione clausola di uscita skill per arco | p1   |

Legenda dipendenze esterne:

`w1` = adozione locale in `~/baserow`, condotta da una sessione lì sul
passaggio di consegne di `TODO.md`; si sblocca col marker `aligned`. Vedi
`o2/ingresso-baserow.md`.

`p1` = battito `/adottanti` del **2026-11-01**: il risveglio conta gli
esiti per stadio nei trailer `Esiti:` registrati dopo il recepimento di
`o3/esiti-per-stadio-nel-commit.md`. Vedi `o2/rivalutazione-skill-per-arco.md`.

## Scadenze

- 2026-11-01 → `/adottanti`, audit runtime-o1 mensile dei sei adottanti
  → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md). Il giro conta i
  trailer `Esiti:` per stadio e per repository (risveglio di `p1`) e
  conferma o meno che `aligned` e i file coincidono.

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
