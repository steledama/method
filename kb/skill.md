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
- deve distinguere audit e prevenzione: `audit-kb` fotografa lo stato,
  `commit` verifica che le modifiche appena fatte siano documentate nel posto
  giusto prima di fissarle nella storia

## Coppia audit/commit

Le skill `audit-kb` e `commit` formano una coppia anti-drift. `audit-kb` misura
salute strutturale e segnala drift cognitivi visibili a posteriori; `commit`
intercetta il drift nel punto più capillare, chiedendo per ogni modifica
significativa se README, CLAUDE, mappa, nodo KB, todo o log siano stati aggiornati
coerentemente.

Questa distinzione evita due errori simmetrici: chiedere all'audit di correggere
automaticamente ciò che deve solo fotografare, oppure committare cambiamenti
operativi senza filing back nella KB. L'audit resta diagnostico; il commit è il
gate di documentazione.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                 | Confronto con il metodo                                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `nixos`    | Skill `audit-kb` e `commit`, con wrapper Codex corrispondenti.                     | Caso base: workflow comuni, legati a strumenti versionati e formatter locali.                                                                    |
| `bi`       | Skill `audit-kb`, `commit`, `graphify`, con wrapper Codex.                         | Mostra una skill realmente locale: Graphify esplora import/call graph e non appartiene automaticamente al metodo.                                |
| `economia` | Skill `audit-kb`, `commit`, `revisione-tasks`, con wrapper Codex per le prime due. | `audit-kb` ora include revisione cognitiva di README/CLAUDE/mappa; `commit` controlla il filing back prima di fissare cambiamenti significativi. |
| `salute`   | Skill `audit-kb`, `commit`, `elabora-trascrizione`, con wrapper Codex.             | `elabora-trascrizione` è locale al ciclo ingest fonti; conferma che le skill possono specializzare il metodo senza diventare portabili.          |

Il confronto indica che solo `audit-kb` e `commit` sono candidate a una base
comune, proprio perché corrispondono ai due momenti generali della manutenzione:
diagnosi periodica e gate pre-commit. Le altre skill sono esempi di adattamento
sano: codificano workflow ripetuti ma radicati in un dominio o in uno strumento
locale.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [claude](claude.md)
- [agents](agents.md)
- [osservatorio-metodo](osservatorio-metodo.md)
