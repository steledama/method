---
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
- ogni repo del metodo — `metodo` incluso — deve esporre il quartetto operativo
  ufficiale: `kb-review`, `plan-review`, `verdicts-review`, `commit`. Gli
  adottanti espongono anche `method-review`, che controlla il drift rispetto al
  metodo. La copia in `metodo` è quella canonica di riferimento; gli adottanti
  la forkano e la parametrizzano
- deve distinguere diagnosi, supervisione e prevenzione: `kb-review` fotografa lo
  stato, la coppia `plan-review`/`verdicts-review` mantiene vere le due
  supervisioni del cruscotto, `commit` verifica che le modifiche appena fatte
  siano documentate nel posto giusto prima di fissarle nella storia

## Base ufficiale

Il quartetto operativo del metodo è `kb-review`, `plan-review`,
`verdicts-review` e `commit`. Ogni repo deve averlo nella propria
`.claude/skills/`, con wrapper Codex corrispondente in `.codex/skills/`. Questo
vale anche per `metodo` stesso: è il repo-modello e fa dogfooding degli
strumenti che teorizza. `method-review` è la quinta skill condivisa, ma opera
sul confine: la copia canonica vive in `metodo` e viene eseguita negli
adottanti per revisionare i commit del metodo successivi al marker versionato
locale.

Il cuore del quartetto è la **coppia simmetrica di supervisione**, una per
braccio del ciclo, col register `goal.md` come cerniera controllata dai due
versanti opposti. Prima della coppia il cruscotto aveva un'asimmetria: il
braccio di esecuzione aveva cura capillare (`commit`) e periodica
(`tasks-review`), quello di valutazione solo la capillare — nessuno rivedeva
mai l'insieme dei fili `i3/`, e la narrativa di stato colava nel plan
(mini-fili mai nati, parcheggiati tra le note). I nomi portano la simmetria:
ogni review porta il nome dell'**indice che tiene onesto** (`plan-review` :
`o1/plan.md` :: `verdicts-review` : `i3/verdicts.md`) — la rinomina da
`tasks-review` corregge anche un signifier che mentiva, perché l'oggetto della
skill è il piano, non i task (cfr. `goal` sul non mescolare altitudini nei
nomi).

`kb-review` è la skill diagnostica. Misura salute strutturale, link, copertura,
frontmatter, footer e segnali di drift cognitivo visibili a posteriori. Può
interpretare strumenti locali come `o3/kb_tools.py`, ma non deve trasformarsi
in procedura di correzione automatica.

`plan-review` è la supervisione del braccio di esecuzione. Controlla coerenza
tra `o1/plan.md` e `o2/`, rivaluta priorità e dipendenze, individua task
superati o nuovi task emersi dai fatti, verifica la direzione task→obiettivo
verso il register `goal.md` e propone il prossimo lavoro. Resta parametrizzata
per-progetto perché i segnali che cambiano i task dipendono dal dominio:
scadenze e pratiche in `economia`, rebuild e host in `nixos`, flussi dati in
`bi`, ingest, diario e quadro in `salute`, generalizzazioni emerse e rinomine
di nodi da propagare in `metodo`.

`verdicts-review` è la supervisione del braccio di valutazione. Quattro domande
per ogni filo `i3/` (è ancora vero rispetto ai segnali? è ancora aperto? è
ancora _un_ filo? è stato, non log?), copertura bidirezionale col register
(ogni obiettivo ha un segnale vivo, ogni filo dichiara quale obiettivo misura),
bonifica del plan e dei task dalla narrativa di stato che vi si parcheggia, e
il modo due dell'i3 — la formazione-goal sugli input esogeni, sempre in
proposta al custode umano.

`commit` è la skill preventiva. Intercetta il drift nel punto più capillare,
prima che una modifica venga fissata nella storia, chiedendo se README, CLAUDE,
register dei poli, nodo KB, task in `o2/` o fili `i3/` siano stati aggiornati
coerentemente.

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

Il quartetto evita gli errori ricorrenti: chiedere all'audit di correggere ciò
che deve solo fotografare, lasciare che la coda dei task diventi un backlog
morto, lasciare che i fili degenerino in log o che la narrativa di stato coli
nel plan, oppure committare cambiamenti operativi senza filing back nella KB.
L'audit resta diagnostico; le due review mantengono vere le supervisioni dei
due bracci; il commit è il gate di documentazione.

## Skill di dominio e ricorrenza

Una skill non è un task e non vive negli stadi di lavoro futuro: il task si
consuma (riga in `o1/plan.md` e file in `o2/` eliminati a completamento), la
skill resta — capacità permanente, versionata. Quando un workflow è ricorrente
il metodo separa i due piani:

- la **capacità** → skill in `.claude/skills/`, appoggiata a script o
  procedure in `o3/` per la parte deterministica;
- la **ricorrenza** → riga in `## Scadenze` di `o1/plan.md` con la cadenza tra
  parentesi e la prossima occorrenza come data (cfr. `plan`); se l'esecuzione è
  automatizzata da uno scheduler, la sua configurazione versionata diventa la
  fonte di verità sulla cadenza e la riga può cadere.

L'origine dal basso è `monthly-review` in `economia`: la skill orchestra i
parser, la procedura vive in `o3/ciclo-mensile.md`, la ricorrenza in
`## Scadenze` come `(mensile)` col trigger esogeno (la busta paga). Il pattern
è collaudato da una seconda istanza: `update-review` in `nixos` (diagnosi
settimanale degli aggiornamenti disponibili, 2026-07-11), nata già in questa
forma.

La ricorrenza può anche essere **a evento** invece che a orologio
(`elabora-trascrizione` in `salute`: il trigger è una nuova trascrizione da
ingerire, non una data): allora nessuna riga in `## Scadenze` — l'evento stesso
è il segnale, e forzarlo in una cadenza inventerebbe un orologio che non
esiste.

### Dove sono elencate

La collezione delle skill è `.claude/skills/` (wrapper Codex in
`.codex/skills/`): il suo `ls` è l'inventario — la regola dell'atrio — ed è
l'harness stesso a leggerlo, iniettando le skill disponibili in contesto a
inizio sessione. Non serve un registro parallelo per gli agenti; i punti di
lettura umani sono due, con ruoli diversi:

- `CLAUDE.md` porta l'elenco commentato di bootstrap (una riga per skill),
  distinguendo le **skill di metodo** (il quartetto più `method-review`,
  forkate dal canone) dalle **skill di dominio** (locali al progetto);
- l'indice `o3/prescriptions.md` può catalogare le skill locali accanto agli
  strumenti che avvolgono (precedente: `salute`), perché il Perform è il loro
  stadio.

Elencarle in `o2/tasks.md` sarebbe un errore di collezione: quello è l'indice
del lavoro che si consuma, e la skill non si consuma.

## Applicazione nei repo del metodo

- **`metodo`** — situazione attuale: quartetto canonico `kb-review`, `plan-review`, `verdicts-review`, `commit` e copia canonica di `method-review` in `.claude/skills/`, con wrapper Codex. Confronto con il metodo: copia di riferimento e dogfooding — il repo-modello applica a sé gli strumenti che teorizza; gli adottanti forkano da qui.
- **`bi`** — situazione attuale: **origine della coppia** — `plan-review` (rinomina) e `verdicts-review` sono nate lì (`52b2b600`) insieme al register `goal.md`; marker `method-review` a `572890b`, nessuna skill di dominio (distinzione metodo/dominio degenere, come in `metodo`); `## Scadenze` porta il battito ricorrente, incluse le righe senza data dei run automatizzati (pilota della terza specie, cfr. `plan`). Confronto con il metodo: la forma è stata scritta già portabile e la ratifica l'ha promossa a canone.
- **`nixos`** — situazione attuale: quartetto completo più `method-review` (marker a `572890b`) e prima skill di dominio `update-review` (diagnosi aggiornamenti home/system/docker sui tre script versionati, ricorrenza settimanale in `## Scadenze`); elenco CLAUDE.md già nella forma metodo/dominio. Confronto con il metodo: primo adottante a recepire il canone skill-non-task e seconda istanza del pattern di ricorrenza; conferma che le skill comuni preservano formatter, fidelity, `tools/check.sh`, distinzione Home/System e vincoli di rebuild.
- **`economia`** — situazione attuale: quartetto completo più `method-review` (marker a `572890b`) e skill di dominio `monthly-review`; register `goal.md`/`world.md` nati qui (pilot poli-register 2026-07-09); elenco CLAUDE.md nella forma metodo/dominio. Il catalogo delle skill locali vive in `o3/tools.md` accanto a `prescriptions.md`: divergenza di forma-item intenzionale, registrata nel ledger locale. Confronto con il metodo: ha corretto la falsa eccezione `presentations/`, mostrando che anche la fotografia finanziaria è interpretazione orientata dai goal; è l'origine del pattern skill-ricorrente ↔ `## Scadenze` con `monthly-review`.
- **`salute`** — situazione attuale: quartetto completo più `method-review` (marker a `572890b`) e skill di dominio `elabora-trascrizione`; è il **precedente** del catalogo skill locali nell'indice o3, e la sua §Skill porta la distinzione metodo/dominio. Confronto con il metodo: privacy sanitaria, diario, scadenze, fonti e registro azioni restano adattamenti locali senza derogare all'anatomia comune; `elabora-trascrizione` incarna la ricorrenza a evento.

La regola generale è: la funzione è ufficiale e metodologica, l'applicazione è
parametrizzata per-progetto. Il repo `metodo` non si limita a documentare il
pattern: lo dogfooda, possedendo la base canonica di riferimento; ogni repo
adottante la forka con la stessa struttura e con letture contestuali diverse. La
vecchia regola — `metodo` esente dal versionare skill — confondeva due cose: che
le skill siano parametrizzate per-progetto (vero) e che `metodo` ne sia esente
(non-sequitur, dato che `metodo` è esso stesso una KB con `o1/plan.md`, `o2/` e fili `i3/`).

Le altre skill sono esempi di adattamento sano: codificano workflow ripetuti ma radicati in un dominio o in uno strumento locale.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [kb-tools](kb-tools.md)
- [claude](claude.md)
- [agents](agents.md)
- [method-observatory](method-observatory.md)
