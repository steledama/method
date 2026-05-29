---
data: 2026-05-24
stato: aperto
---

# Regress check CLAUDE.md bi

Verificare che `bi/CLAUDE.md` non sia tornato manuale di dominio a distanza di tempo dalla compattazione del 2026-05-23 (commit `b195b8ff`).

## Azione

- aprire `bi/CLAUDE.md` e verificare che non siano rispuntate sezioni descrittive di flussi, script o API
- se supera ~100 righe o contiene descrizioni di come funziona qualcosa: aprire task in `bi` per compattare di nuovo
- se regge: annotare in `log.md` come evidenza che il principio "costituzione operativa" è stabile senza rinforzo esterno e chiudere il task

## Criterio di chiusura

Il file è ≤ ~100 righe e contiene solo regole operative. Esito registrato in `log.md` in entrambi i casi.
