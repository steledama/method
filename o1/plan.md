---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Direzione

Questo repository custodisce il metodo portabile e osserva come gli adottanti
lo usano. È in sviluppo verso un ciclo di runtime autonomo in ciascun repo,
con deleghe e controlli espliciti; qui il lavoro aperto consolida strumenti,
skill e viste che rendono quel ciclo ricostruibile e governabile.

## Task

| Ciclo | Ob. | Task                          | Dip. |
| ----- | --- | ----------------------------- | ---- |
| dev   | S   | Ricorrenza dei dinieghi       | —    |
| dev   | S   | Pubblicazione decisa dal repo | —    |
| dev   | S   | Traduzione in inglese         | —    |

## Ricorrenze

| Prossima   | Cadenza    | Esecutore | Ob. | Ricorrenza                                         |
| ---------- | ---------- | --------- | --- | -------------------------------------------------- |
| config     | quotidiano | scheduler | S   | [Ciclo autonomo](../o3/ciclo/prompt.md)            |
| 2026-12-01 | mensile    | sessione  | 2   | [/adottanti](../.claude/skills/adottanti/SKILL.md) |

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
