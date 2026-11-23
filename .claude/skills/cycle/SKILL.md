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

Il custode avvia il ciclo in sessione, entro `ciclo-delegato`; restano le
regole della sessione e i punti riservati da `confine-delega`.

- Invoca `eval all` ed `exec all` col tool Skill: leggere il loro `SKILL.md`
  non vale come invocazione. Su un harness senza tool Skill, come Codex, vale
  la lettura indicata dal wrapper.
- Uno stadio che il giro non compie col suo minimo si dichiara: resta fuori
  da `Esiti:` e il motivo va nel resoconto.
- Una procedura del dominio al centro del giro sta dentro gli stadi, non al
  loro posto: la diagnosi in sola lettura è un canale di `perceive`, gli atti
  stanno in `perform`, dopo `compare` e `plan`, così il verdetto può ancora
  fermarli (giro di `nixos` del 2026-11-08).
- Il resoconto finale riporta gli esiti degli stadi, il prossimo task e i
  punti da segnalare al custode.
