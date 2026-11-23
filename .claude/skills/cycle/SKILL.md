---
description: Il ciclo congiunto — cycle — un giro completo del ciclo d'azione, eval all → exec all → commit, in sessione
user-invocable: true
metadata:
  compone: eval exec commit
---

Compi un giro completo del ciclo d'azione: `eval all`, poi `exec all`, poi
`/commit`, invocando le skill `eval`, `exec` e `commit` del repository. È il
**ciclo congiunto** di [`autonomy.md`](../../../autonomy.md): la verità prima
delle priorità, le priorità prima del commit. La skill non aggiunge stadi né
giudizi: è la composta (`kb/skill-composition.md`), decide ordine e
condizioni e passa a `/commit` gli esiti di `eval` ed `exec`, che restano
distinti e contabili nel trailer `Esiti:` (cfr. `kb/skill.md`,
`kb/action-cycle.md`). Questa è la copia
canonica: gli adottanti la forkano e la parametrizzano sul proprio dominio.

Il custode avvia il ciclo in sessione entro `ciclo-delegato`. Invoca i due archi nell'ordine indicato e poi `/commit`, riportando gli esiti degli stadi e il prossimo task. Restano valide le regole della sessione e le decisioni riservate al custode.
