---
data: 2026-06-22
stato: aperto
sintesi: "Revisione i2/o2 della presentazione (deck + home): rendere visibili le frecce del ciclo d'azione, ridisegnare la slide «Sviluppo del metodo» come risalita→generalizzazione→ridiscesa, allineare le slide seguenti a system-image=artefatto e rimuovere la slide «Approfondimento»."
---

# Revisione i2 della presentazione

Tre interventi sullo strato `view`, tutti **resa** (non modello): si correggono
nel deck (`interpretations/metodo-in-sintesi.md` + `assets/`) e nella home
(`tools/build_system_image.py` + `assets/`), poi le viste si ri-derivano. Il
diagramma dei cicli annidati è trattato a parte (task 1, perché porta una
decisione di modello).

## 1 — Frecce del ciclo d'azione visibili (task 2)

Gli archi del ciclo — le frecce `arrow up/down/right` nei diagrammi e gli archi
output/input nella home — sono poco o per niente visibili. Sono il cuore del
modello di Norman (esecuzione che scende, valutazione che risale): non possono
sparire. Diagnosi del CSS in `assets/` (classi `arrow`, `branch-arrows`,
`return-step`) e del rendering della home in `build_system_image.py`; verificare
su **tutte** le istanze (ciclo d'azione, altitudini del goal, anatomia, routing).

## 2 — Slide «Sviluppo del metodo» ridisegnata (task 3)

Oggi la slide «Sviluppo del metodo: dal basso e dall'alto» è disposta tutta
top-to-bottom, e la freccia etichettata «bottom-up» punta in giù (`<b>↓</b>`) —
contraddice ciò che dice. Il movimento va reso come **forma a Λ**: risalita
dal basso (esigenza concreta dagli adottanti → filing back), **generalizzazione
all'apice** (la cornice teorica / il giudizio «generalizzabile?»), poi ridiscesa
top-down (propagazione e verifica nei domini). Coerente con `method-development`
(i due movimenti in alternanza) e col guardrail «`metodo` non è il backlog degli
adottanti».

## 3 — Coerenza slide seguenti + rimozione «Approfondimento» (task 4)

- Passata di coerenza sulle slide dopo «Sviluppo del metodo» — «Dove vive cosa»,
  «Le interpretazioni di questo repo», «Ogni sezione è un'interpretazione», «Il
  deck rivela» — alla luce del task system-image (il _system image_ è l'artefatto,
  la KB ne è il nucleo formalizzato): controllare che nessuna slide equipari ancora
  KB e system image / medium interno.
- **Rimuovere** la slide «Approfondimento» (l'elenco di rimandi ai nodi): ridondante
  con i pointer già distribuiti e con `kb.md`. Dip. task 1 per la slide cicli
  annidati a monte.

## Criterio di chiusura

Deck e home ri-derivati dai sorgenti; frecce del ciclo visibili in ogni diagramma;
slide «Sviluppo del metodo» a forma di risalita→apice→ridiscesa; «Approfondimento»
rimossa; nessun residuo di KB-come-system-image nelle slide; viste apribili via
`file://` e ispezionate a vista.
