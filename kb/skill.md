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
- ogni repo del metodo — `metodo` incluso — deve esporre la triade base ufficiale:
  `audit-kb`, `tasks-review`, `commit`. La copia in `metodo` è quella canonica di
  riferimento; gli adottanti la forkano e la parametrizzano
- deve distinguere diagnosi, supervisione e prevenzione: `audit-kb` fotografa lo
  stato, `tasks-review` mantiene viva la coda del lavoro futuro, `commit`
  verifica che le modifiche appena fatte siano documentate nel posto giusto
  prima di fissarle nella storia

## Triade base ufficiale

Le tre skill base ufficiali del metodo sono `audit-kb`, `tasks-review` e
`commit`. Ogni repo del metodo deve averle nella propria `.claude/skills/`, con
wrapper Codex corrispondente in `.codex/skills/`. Questo vale anche per `metodo`
stesso: è il repo-modello e fa dogfooding degli strumenti che teorizza — la sua
triade è la copia canonica di riferimento, parametrizzata sul dominio «manutenzione
della KB del metodo», che gli adottanti forkano e adattano al proprio dominio.

`audit-kb` è la skill diagnostica. Misura salute strutturale, link, copertura,
frontmatter, footer e segnali di drift cognitivo visibili a posteriori. Può
interpretare strumenti locali come `tools/kb_tools.py`, ma non deve trasformarsi
in procedura di correzione automatica.

`tasks-review` è la skill di supervisione del lavoro futuro. Controlla
coerenza tra `plan.md` e `tasks/`, rivaluta priorità e dipendenze, individua task
superati o nuovi task emersi dai fatti e propone il prossimo lavoro. Resta
parametrizzata per-progetto perché i segnali che cambiano i task dipendono dal
dominio: scadenze e pratiche in `economia`, rebuild e host in `nixos`, flussi dati
in `bi`, ingest, diario e quadro in `salute`, generalizzazioni emerse e rinomine di
nodi da propagare in `metodo`.

`commit` è la skill preventiva. Intercetta il drift nel punto più capillare,
prima che una modifica venga fissata nella storia, chiedendo se README, CLAUDE,
map, nodo KB, tasks o why siano stati aggiornati coerentemente.

Questa triade evita tre errori ricorrenti: chiedere all'audit di correggere ciò
che deve solo fotografare, lasciare che la coda dei task diventi un backlog
morto, oppure committare cambiamenti operativi senza filing back nella KB.
L'audit resta diagnostico; la revisione task mantiene vera la supervisione del
lavoro; il commit è il gate di documentazione.

## Applicazione nei repo del metodo

| Progetto   | Situazione attuale                                                                        | Confronto con il metodo                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `metodo`   | Triade canonica `audit-kb`, `tasks-review`, `commit` in `.claude/skills/`, con wrapper Codex. | Copia di riferimento e dogfooding: il repo-modello applica a sé gli strumenti che teorizza; gli adottanti forkano da qui. |
| `nixos`    | Skill `audit-kb`, `tasks-review` e `commit`, con wrapper Codex corrispondenti.         | Caso base: workflow comuni parametrizzati su task tecnici, rebuild, reboot, host e moduli.                                     |
| `bi`       | Skill `audit-kb`, `tasks-review`, `commit`, `graphify`, con wrapper Codex.             | `tasks-review` segue flussi BI e task strutturali; Graphify resta skill realmente locale per import/call graph.             |
| `economia` | Skill `audit-kb`, `tasks-review`, `commit`, con wrapper Codex corrispondenti.          | Caso originario della revisione task: priorità, scadenze, pratiche aperte e dipendenze esterne richiedono controllo frequente. |
| `salute`   | Skill `audit-kb`, `tasks-review`, `commit`, `elabora-trascrizione`, con wrapper Codex. | `tasks-review` è adattata a ingest, scadenze, diario e quadro; `elabora-trascrizione` resta locale al ciclo fonti.          |

La regola generale è: la funzione è ufficiale e metodologica, l'applicazione è
parametrizzata per-progetto. Il repo `metodo` non si limita a documentare il
pattern: lo dogfooda, possedendo la triade canonica di riferimento; ogni repo
adottante la forka con la stessa struttura e con letture contestuali diverse. La
vecchia regola — `metodo` esente dal versionare skill — confondeva due cose: che
le skill siano parametrizzate per-progetto (vero) e che `metodo` ne sia esente
(non-sequitur, dato che `metodo` è esso stesso una KB con `plan`/`tasks`/`why`).

Le altre skill sono esempi di adattamento sano: codificano workflow ripetuti ma radicati in un dominio o in uno strumento locale.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [claude](claude.md)
- [agents](agents.md)
- [osservatorio-metodo](osservatorio-metodo.md)
