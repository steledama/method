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

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | Skill `audit-kb` e `commit`, con wrapper Codex corrispondenti. | Caso base: workflow comuni, legati a strumenti versionati e formatter locali. |
| `bi` | Skill `audit-kb`, `commit`, `graphify`, con wrapper Codex. | Mostra una skill realmente locale: Graphify esplora import/call graph e non appartiene automaticamente al metodo. |
| `economia` | Skill `audit-kb`, `commit`, `revisione-tasks`, con wrapper Codex per le prime due. | `revisione-tasks` è un adattamento di dominio utile: fine sessione con scadenze e pratiche aperte. |
| `salute` | Skill `audit-kb`, `commit`, `elabora-trascrizione`, con wrapper Codex. | `elabora-trascrizione` è locale al ciclo ingest fonti; conferma che le skill possono specializzare il metodo senza diventare portabili. |

Il confronto indica che solo `audit-kb` e `commit` sono candidate a una base comune. Le altre skill sono esempi di adattamento sano: codificano workflow ripetuti ma radicati in un dominio o in uno strumento locale.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [claude](claude.md)
- [agents](agents.md)
- [osservatorio-metodo](osservatorio-metodo.md)
