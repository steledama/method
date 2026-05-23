---
data: 2026-05-23
stato: bozza
---

# Skill

Una skill è un workflow ricorrente codificato per l'agente. Risponde alla domanda: quali workflow ricorrenti sono codificati? Traduce una procedura ripetibile in istruzioni operative, spesso appoggiandosi a script versionati per la parte deterministica.

Le skill sono interfacce operative, non documentazione di dominio. Una buona skill non reimplementa parser e logiche fragili in prompt: chiama strumenti versionati, interpreta output e guida l'agente nelle decisioni che richiedono giudizio.

Regole:

- vive nel progetto quando il workflow dipende dal dominio
- può avere una base portabile e wrapper locali
- deve preferire script versionati a regex improvvisate
- deve dichiarare scope, limiti e comportamento atteso
- non deve duplicare contenuto stabile che appartiene ai nodi
- va confrontata cross-repo quando più progetti hanno workflow simili

Connessioni:

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [claude](claude.md)
- [agents](agents.md)
- [osservatorio-metodo](osservatorio-metodo.md)
