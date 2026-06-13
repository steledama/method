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
- ogni repo del metodo — `metodo` incluso — deve esporre la triade operativa
  ufficiale: `kb-review`, `tasks-review`, `commit`. Gli adottanti espongono anche
  `method-review`, che controlla il drift rispetto al metodo. La copia in
  `metodo` è quella canonica di riferimento; gli adottanti la forkano e la
  parametrizzano
- deve distinguere diagnosi, supervisione e prevenzione: `kb-review` fotografa lo
  stato, `tasks-review` mantiene viva la coda del lavoro futuro, `commit`
  verifica che le modifiche appena fatte siano documentate nel posto giusto
  prima di fissarle nella storia

## Base ufficiale

La triade operativa del metodo è `kb-review`, `tasks-review` e `commit`. Ogni repo
deve averla nella propria `.claude/skills/`, con wrapper Codex corrispondente in
`.codex/skills/`. Questo vale anche per `metodo` stesso: è il repo-modello e fa
dogfooding degli strumenti che teorizza. `method-review` è la quarta skill
condivisa, ma opera sul confine: la copia canonica vive in `metodo` e viene
eseguita negli adottanti per revisionare i commit del metodo successivi al marker
versionato locale.

`kb-review` è la skill diagnostica. Misura salute strutturale, link, copertura,
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
map, nodo KB, tasks o `verdict.md` siano stati aggiornati coerentemente.

`method-review` è la skill di allineamento trans-repo. Distingue cambiamenti già
soddisfatti, diretti, da adattare, non pertinenti e divergenze intenzionali; usa
uno SHA completo di `method` come cursore e non avanza il marker finché ogni voce
pertinente non è risolta o tracciata in un task locale.

Il marker vive in `method-review.md` nella root dell'adottante, con
`method_commit`, `reviewed_at` e `status`. `aligned` non significa che ogni
differenza sia stata cancellata: significa che ciascun cambiamento pertinente è
stato applicato, risultava già soddisfatto, è registrato come divergenza
intenzionale oppure è affidato a un task locale. Lo SHA avanza solo dopo questa
classificazione; la storia delle revisioni resta in Git, non nel marker.

La triade evita tre errori ricorrenti: chiedere all'audit di correggere ciò
che deve solo fotografare, lasciare che la coda dei task diventi un backlog
morto, oppure committare cambiamenti operativi senza filing back nella KB.
L'audit resta diagnostico; la revisione task mantiene vera la supervisione del
lavoro; il commit è il gate di documentazione.

## Applicazione nei repo del metodo

- **`metodo`** — situazione attuale: triade canonica `kb-review`, `tasks-review`, `commit` e copia canonica di `method-review` in `.claude/skills/`, con wrapper Codex. Confronto con il metodo: copia di riferimento e dogfooding — il repo-modello applica a sé gli strumenti che teorizza; gli adottanti forkano da qui.
- **`nixos`** — situazione attuale: secondo pilot di `method-review` completato, idempotente e committato (`5d076ae`), con triade riallineata e marker a `df9e651`. Confronto con il metodo: conferma che le skill comuni possono preservare formatter, fidelity, `tools/check.sh`, distinzione Home/System e vincoli di rebuild.
- **`bi`** — situazione attuale: terzo pilot di `method-review` completato, idempotente e committato (`48f9e2cc`), con triade riallineata, marker a `18424f8` e rename `interpretations/`. Confronto con il metodo: i guardrail BI e gli usi applicativi di `--append-note` restano locali, mentre il protocollo comune si applica senza confonderli con l'append dell'audit.
- **`economia`** — situazione attuale: primo pilot completato, idempotente e committato (`4c633b8`), con triade riallineata e `method-review`. Confronto con il metodo: ha corretto la falsa eccezione `presentations/`, mostrando che anche la fotografia finanziaria è interpretazione orientata dai goal.
- **`salute`** — situazione attuale: quarto pilot completato, idempotente e committato (`bc1eaef`), con triade riallineata, marker a `7b97c0b` e rename `interpretations/`. Confronto con il metodo: privacy sanitaria, diario, scadenze, fonti, registro azioni e `elabora-trascrizione` restano adattamenti locali senza derogare all'anatomia comune.

La regola generale è: la funzione è ufficiale e metodologica, l'applicazione è
parametrizzata per-progetto. Il repo `metodo` non si limita a documentare il
pattern: lo dogfooda, possedendo la base canonica di riferimento; ogni repo
adottante la forka con la stessa struttura e con letture contestuali diverse. La
vecchia regola — `metodo` esente dal versionare skill — confondeva due cose: che
le skill siano parametrizzate per-progetto (vero) e che `metodo` ne sia esente
(non-sequitur, dato che `metodo` è esso stesso una KB con `plan`/`tasks`/`verdict.md`).

Le altre skill sono esempi di adattamento sano: codificano workflow ripetuti ma radicati in un dominio o in uno strumento locale.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [claude](claude.md)
- [agents](agents.md)
- [osservatorio-metodo](osservatorio-metodo.md)
