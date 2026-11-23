---
ciclo: dev
---

# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`, i verdetti nei
fili di `i3/`, la storia in git; qui restano solo i task e il loro stato di
pianificazione.

## Direzione

Questo repository custodisce il metodo portabile, da distribuire a chi il
custode non conosce, con i gruppi di repo coordinati da un loro membro. Gli
strumenti del coordinatore sono passati ai gruppi con `v0.4.0`, e la via è
decisa: un ingresso proprio, sito di gruppo e chat. Ora le skill, snellite e
rese canone in una sola tornata per gli adottanti; poi identità e
distribuzione, cioè nome, lingua e pacchetto versionato.

## Task

| Ciclo   | Ob. | Task                                     | Dip.                                       |
| ------- | --- | ---------------------------------------- | ------------------------------------------ |
| dev     | S   | Presentazione oltre il deck              | —                                          |
| dev     | S   | Snellimento delle skill `eval` ed `exec` | —                                          |
| dev     | S   | Skill dal canone                         | ↳ Snellimento delle skill `eval` ed `exec` |
| dev     | S   | Chat del coordinatore                    | ↳ Skill dal canone                         |
| dev     | S   | Ricordo del gruppo                       | ↳ Chat del coordinatore                    |
| dev     | S   | Nome del progetto                        | —                                          |
| dev     | S   | Traduzione in inglese                    | ↳ Nome del progetto                        |
| dev     | S   | Diffusione oltre il custode unico        | ↳ Traduzione in inglese                    |
| runtime | 3   | Canale in entrata                        | w1                                         |

Legenda delle attese (`w`) e delle pause (`p`), con risveglio e termine di
riesame (`kb/plan.md`, «Risveglio»):

- `w1` — 2026-11-24: la skill che smista i contributi si progetta sulla
  prima issue vera, non a tavolino (`o2/canale-in-entrata.md`, passo 4);
  arrival: la prima issue o PR di un adottante su `steledama/method`, vista
  in sessione; by: 2026-12-31

Le dipendenze seguono le specifiche: Skill dal canone parametrizza le skill
già snellite, così gli adottanti recepiscono una volta sola; il `/cycle` da
chat aspetta le skill canoniche, e il ricordo parte dai suoi episodi; la rinomina e la lingua vanno fatte una
volta ciascuna, prima del pacchetto. La decisione su Skill dal canone
(`decidere:`) può arrivare prima dei tagli.

## Ricorrenze

Nessuna dal 2026-11-23: l'audit mensile `/adottanti` è ritirato
([diffusione-oltre-custode-unico](../o2/diffusione-oltre-custode-unico.md),
«Decisione del 2026-11-23»).

I dettagli e il contesto dei task vivono in `o2/`, indicizzati da
[`o2/tasks.md`](../o2/tasks.md).
