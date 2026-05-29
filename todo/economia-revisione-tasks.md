---
data: 2026-05-24
stato: aperto
---

# Portabilità skill revisione-tasks

`economia` ha implementato la skill `revisione-tasks` con un pattern di controllo leggero a inizio sessione e revisione completa quando cambiano fatti, scadenze o dipendenze. Valutare se il pattern è portabile agli altri repo come skill standard del metodo.

## Azione

- leggere `economia/.claude/skills/revisione-tasks` per distinguere cosa è specifico del dominio da cosa è pattern universale
- testare mentalmente su `bi` e `nixos`: quale parte va parametrizzata per funzionare?
- decidere: portare nel metodo come skill standard con varianti locali, o documentare come pattern in `kb/skill.md` senza implementare una skill portabile

## Criterio di chiusura

`kb/skill.md` aggiornato con la decisione e la motivazione. Se si decide di portare la skill, aprire task separato per scrivere la versione portabile.
