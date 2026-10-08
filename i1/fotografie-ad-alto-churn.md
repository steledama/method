---
ciclo: dev
---

# Segnale: le fotografie numeriche hanno un churn che il register del Goal non regge

Data: 2026-10-08 · Fonte: il custode, in sessione, discutendo i trailer di
autonomia e impatto · Caso: `danea-auto` `2afd7bf`

## Il segnale

Classificando l'impatto di commit reali, un giro `eval`+`exec` di
`danea-auto` (`2afd7bf`) tocca `goal.md` per aggiornare la fotografia: il
clean-rate di ottobre da 105/109 a 175/179 e un fatto nuovo sul click alla
cieca. Nessun obiettivo cambia. Un criterio d'impatto basato sul file
toccato lo leggerebbe come cambio del nord.

Il custode non sposta il criterio ma il contenuto:

- in `goal.md` dovrebbero stare solo gli obiettivi; la fotografia attuale,
  al più, la si referenzia da lì;
- le fotografie coi numeri sono dati ad alto **churn** e dubita che vadano
  versionate del tutto;
- sui numeri si prendono decisioni e valutazioni: quelle si versionano, i
  numeri no.

## Cosa tocca

- `kb/goal-register.md`: il register porta oggi «gli obiettivi, i segnali
  che li misurano e il lavoro corrente».
- Il `goal.md` di tutti e otto i repo.
- Il task `o2/criteri-autonomia.md`: con il solo nord nel register, ogni
  modifica a `goal.md` diventa impatto alto senza distinguere le sezioni.
- Canone vicino: `kb/pace-layering.md` (modello durevole separato dallo
  stato transitorio) e `kb/view.md` (non versionare ciò che si deriva).
- Segnale vicino in questa collezione:
  [registro-perpetuo-vs-cattura-singola](registro-perpetuo-vs-cattura-singola.md),
  sulla natura dei file che i register ospitano.

## Da misurare in i2

Il churn reale di `goal.md` negli otto repo: quanti commit toccano solo
numeri o fatti datati e quanti un obiettivo; da quale fonte ogni numero
potrebbe derivarsi al momento della vista invece che vivere nel file.
