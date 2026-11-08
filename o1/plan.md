---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Task

| Ciclo | Ob. | Task                            | Dip.                              |
| ----- | --- | ------------------------------- | --------------------------------- |
| dev   | S   | Agente come utilizzatore        | —                                 |
| dev   | S   | Progettazione delle skill       | —                                 |
| dev   | S   | Lanciatore del ciclo nel metodo | —                                 |
| dev   | S   | Ricorrenza dei dinieghi         | —                                 |
| dev   | S   | Pilota del ciclo autonomo       | —                                 |
| dev   | S   | Uscita dal deck                 | —                                 |
| dev   | S   | Pubblicazione decisa dal repo   | ↳ Lanciatore del ciclo nel metodo |
| dev   | S   | Traduzione in inglese           | —                                 |
| dev   | S   | Strumento delle scadenze        | —                                 |
| dev   | 2   | Snellire /adottanti             | —                                 |

## Ricorrenze

| Prossima   | Cadenza    | Esecutore | Ob. | Ricorrenza                                         |
| ---------- | ---------- | --------- | --- | -------------------------------------------------- |
| config     | quotidiano | scheduler | S   | [Ciclo autonomo](../o3/ciclo/prompt.md)            |
| 2026-12-01 | mensile    | sessione  | 2   | [/adottanti](../.claude/skills/adottanti/SKILL.md) |

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
