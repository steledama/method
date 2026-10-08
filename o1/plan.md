---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                                            | Dip.                                            |
| ----- | --- | ----------------------------------------------- | ----------------------------------------------- |
| dev   | 1   | Bozza agente e custode                          | —                                               |
| dev   | S   | Trailer di autonomia e incisione                | —                                               |
| dev   | S   | Home con fatto e da fare                        | —                                               |
| dev   | S   | Criteri di autonomia nel trittico costitutivo   | ↳ Trailer di autonomia e incisione              |
| dev   | S   | Dove gira il battito                            | —                                               |
| dev   | S   | Pilota del battito                              | ↳ Criteri di autonomia nel trittico costitutivo |
| dev   | 1   | Rivalutazione clausola di uscita skill per arco | p1                                              |

Legenda dipendenze esterne:

`p1` = battito `/adottanti` del **2026-11-01**: il risveglio conta gli
esiti per stadio nei trailer `Esiti:` registrati dopo il recepimento di
`o3/esiti-per-stadio-nel-commit.md`. Vedi `o2/rivalutazione-skill-per-arco.md`.

## Scadenze

- Dal 2026-10-13, con osservazione almeno fino al 2026-10-17 → `eval interpret`
  riesamina l'[osservazione su danea-auto](../i2/presidio-ipotesi-adottanti.md#osservazione-aperta-danea-auto):
  primo giro locale dopo il 13/10, trailer `Esiti:` e diff del filo pubblicati;
  fonte del precursore `o3/stats.ps1`. Nessuna sollecitazione all'adottante;
  se giro o copertura mancano, dichiarare il limite e il prossimo riesame.
  Chiusa l'osservazione, sollecitare `danea-auto` a recepire
  `presidio-ipotesi`, rinviata nel suo marker fino a quella sollecitazione.

- 2026-11-01 → `/adottanti`, audit runtime-o1 mensile dei sette adottanti
  → esiti nel filo
  [i3/audit-adottanti.md](../i3/audit-adottanti.md). Il giro conta i
  trailer `Esiti:` per stadio e per repository (risveglio di `p1`) e
  conferma o meno che `aligned` e i file coincidono.

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
