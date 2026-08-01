---
stato: bozza
---

# Skill

Una skill è un workflow ricorrente codificato per l'agente. Risponde alla
domanda: quali workflow ricorrenti sono codificati? Traduce una procedura
ripetibile in istruzioni operative, spesso appoggiandosi a script versionati per
la parte deterministica.

Le skill sono interfacce operative, non documentazione di dominio. Una buona
skill non reimplementa parser e logiche fragili in prompt: chiama strumenti
versionati, interpreta output e guida l'agente nelle decisioni che richiedono
giudizio. E sono interfacce **sul canone**, non la sua sede: il significato
degli stadi vive negli atomi (`perceive` … `perform`), la skill lo esercita.

Nota di stato (bozza): la rifilatura per arco descritta qui è ratificata
(filo `i3/skill-per-arco-tripartito.md`) ed è in pilota su `metodo`; finché il
pilota non chiude, le due skill montate nei repo restano `plan-review` e
`verdicts-review`, e l'incisione definitiva di questo nodo segue il pilota
(task `o2/skill-archi-tripartite.md`).

Regole:

- vive nel progetto quando il workflow dipende dal dominio
- può avere una base portabile e wrapper locali
- deve preferire script versionati a regex improvvisate
- deve dichiarare scope, limiti e comportamento atteso
- non deve duplicare contenuto stabile che appartiene ai nodi
- va confrontata cross-repo quando più progetti hanno workflow simili
- ogni repo del metodo — `metodo` incluso — deve esporre il quartetto operativo
  ufficiale: **`eval`**, **`exec`**, `kb-review`, `commit`. Gli adottanti
  espongono anche `method-review`, che controlla il drift rispetto al metodo.
  La copia in `metodo` è quella canonica di riferimento; gli adottanti la
  forkano e la parametrizzano
- il quartetto distingue le nature: due **verbi d'arco** (`eval` ed `exec`
  compiono gli stadi del ciclo, e dentro gli stadi vive la supervisione),
  un'**ala diagnostica** (`kb-review` fotografa, non corregge), un **gate
  preventivo** (`commit` verifica il filing back prima di fissare nella storia)

## Base ufficiale

Il quartetto si ritaglia lungo il modello, non lungo la storia della propria
crescita: **due capacità, sei scope** —

- `eval [perceive|interpret|compare|all]` — il braccio di valutazione
- `exec [plan|specify|perform|all]` — il braccio di esecuzione

La regola precedente — ogni review porta il nome dell'indice che tiene onesto
(`plan-review` : `o1/plan.md` :: `verdicts-review` : `i3/verdicts.md`) — era
vera quando una skill teneva onesto _un_ indice, ed è morta di copertura:
`plan-review` copriva o1 e o2, `verdicts-review` i3 e parte di i1, e gli stadi
degradati — **i1, i2, o3** — erano esattamente quelli che nessun nome nominava:
ciò che il signifier non dichiara è ciò che nessuno mantiene. Il taglio nuovo
dà a ogni stadio un guardiano senza moltiplicare le skill: l'arco vale come
sequenza, e spezzarlo in sei decisioni di invocazione dissolverebbe il
protocollo post-evento che è già canone.

La conferma che il taglio è quello vero: **l'argomento di scope è il nome
dell'atomo, che è il nome dell'indice della collezione** — `eval interpret` →
`kb/interpret.md` → `i2/interpretations.md`. Nessuna nomenclatura nuova da
inventare.

Le giurisdizioni, una riga per stadio (la procedura vive nelle SKILL.md, il
significato negli atomi):

- **`eval perceive`** — raccoglie il grezzo dal Mondo, valenza-neutro; cattura
  in `i1/` solo l'effimero o ciò che chiede un riflesso stabile (cfr.
  `perceive`)
- **`eval interpret`** — distilla il grezzo in sintesi `i2/` orientate dai goal
  sulla rilevanza e neutre sulla valenza; provenienza delle quantità, cascata
  all'indietro quando un claim cade, materiale di casa come fonte primaria
  (cfr. `interpret`, `verdict`)
- **`eval compare`** — il verdetto contro il Goal: le cinque domande per ogni
  filo, la copertura bidirezionale col register `goal.md`, la formazione-goal
  sempre in proposta al custode, la bonifica del plan dalla narrativa di stato
  (cfr. `compare`, `verdict`)
- **`exec plan`** — la coda: drift plan↔`o2/` (verificato dal generatore, che
  lo scope invoca e interpreta), ordine e priorità, dipendenze reali, direzione
  task→obiettivo, lettura strategica delle mosse (cfr. `plan`)
- **`exec specify`** — la qualità interna dei file `o2/`: frontmatter completo,
  diari di sessione potati, e le quattro proprietà cardine — visibilità,
  feedback, mapping, constraint (cfr. `specify`)
- **`exec perform`** — due piani: la supervisione della collezione `o3/` (solo
  il vivo, strumenti ancora eseguibili, runbook freschi) e l'atto stesso quando
  l'autorizzazione dello scope già lo copre; ciò che tocca il Mondo senza
  autorità produce o valida la prescrizione e si ferma al confine (cfr.
  `perform`)

Ogni stadio può **chiudere in una riga** quando non ha materia («nessun segnale
nuovo», «coda coerente»): l'esito nullo è esito, non un passo saltato. Il
default è `all` su entrambi gli archi.

`kb-review` sta fuori dai due archi perché `kb/` è un'ala trasversale al ciclo.
È la skill diagnostica: misura salute strutturale, link, copertura, frontmatter,
footer e segnali di drift cognitivo visibili a posteriori; può interpretare
strumenti locali come `o3/kb_tools.py`, ma non deve trasformarsi in procedura di
correzione automatica. `eval perceive` può acquisirne gli esiti come segnale,
senza eseguirla implicitamente.

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

## Protocollo post-evento e gate

Dopo eventi del mondo l'ordine è **`eval` → `exec`** — la verità prima delle
priorità — e i due archi comunicano per handoff, non per fusione: `eval
compare` emette «impatti sul piano», `exec plan` chiude con l'inverso
«verdetti da rivalutare». Il movimento è asimmetrico: l'andata è ordinaria, il
ritorno è l'eccezione da giustificare al custode — e un ritorno vuoto è il
segnale che l'ordine ha funzionato, non un fallimento. L'handoff è input, non
comando: lo scope ricevente conserva il giudizio e dichiara le divergenze.
Verso l'alto i due archi non scrivono mai: l'affilatura dei goal viaggia sempre
come proposta al custode (cfr. `goal`). Il protocollo è collaudato in
`economia` (2026-07-12) nella forma precedente della coppia: cattura email →
verdetto aggiornato → piano riprioritizzato, handoff inverso vuoto.

Il **gate proponi-poi-applica** vale su entrambi gli archi: le modifiche a
collezioni e register si applicano dopo conferma del custode, e il gate prevale
sull'autorizzazione generica delle bussole — quella copertura è per il lavoro
ordinario di sessione, non per l'auto-applicazione degli esiti di una
supervisione. Fa eccezione solo l'atto che l'autorizzazione dello scope già
copre.

## La regola dei nomi

Le due canoniche portano **l'arco del modello, abbreviato per la mano che lo
digita**: `eval` ed `exec`. La regola sostituisce «l'indice che tiene onesto»
per due ragioni: la **copertura** — una skill che mantiene tre indici non può
portare il nome di uno solo — e il **telos inglese** — il metodo intero, KB
compresa, migra verso l'inglese, e le canoniche fanno da avanguardia. Le forme
lunghe Evaluate/Execute sopravvivono solo come nomi degli archi nel canone, mai
come nome della skill: un nome solo ovunque, o qualcuno «correggerà»
`eval`→`evaluate` credendo di sanare un drift.

Gli **scope-stadio** restano per esteso: sono i nomi degli atomi e degli indici,
e la catena `eval interpret` → `kb/interpret.md` → `i2/interpretations.md` non
si abbrevia. Gli **scope di dominio** portano il vocabolario del loro Mondo
(`aggiorna`, `ordini`), nella lingua che la regola locale chiede, anche a metodo
anglicizzato. Resta vero il corollario storico: la cadenza non entra mai nel
nome (cfr. sotto) — il nome porta la capacità (skill di dominio) o l'arco
(canoniche), il ritmo vive in `## Scadenze`.

## Skill di dominio e ricorrenza

Una skill non è un task e non vive negli stadi di lavoro futuro: il task si
consuma (riga in `o1/plan.md` e file in `o2/` eliminati a completamento), la
skill resta — capacità permanente, versionata. Quando un workflow è ricorrente
il metodo separa i due piani:

- la **capacità** → skill in `.claude/skills/`, appoggiata a script o
  procedure in `o3/` per la parte deterministica;
- la **ricorrenza** → righe in `## Scadenze` di `o1/plan.md`, **una per
  battito** (cfr. `plan`): il soggetto della riga non è la skill ma la coppia
  invocazione + porzione di mondo su cui insiste; se l'esecuzione è
  automatizzata da uno scheduler, la sua configurazione versionata diventa la
  fonte di verità sulla cadenza e la riga perde la data (terza specie, cfr.
  `plan`).

I due piani non vanno riaccoppiati di nascosto: una capacità non porta
necessariamente un solo battito. Una skill può prendere un **argomento di
scope** che seleziona il ramo (`all` come default di sweep), e ogni ramo può
avere cadenza propria — perché l'orologio appartiene alla porzione di mondo
servita, non allo strumento (cfr. `plan`, «chi possiede l'orologio»); lo
stesso argomento può persino mappare su risorse diverse secondo la porzione di
mondo. Corollari:

- la skill multi-scope **non si spezza per ritmo**: si spezza solo se diverge
  la capacità (procedura, giudizio, strumenti) — il ritmo non è mai un
  criterio di fissione;
- la stessa capacità può essere **esecutiva su un ramo e diagnostica su un
  altro**: il confine di autorizzazione segue le risorse dello scope, non la
  skill;
- quando le porzioni di mondo si moltiplicano (molte entità, ciascuna col suo
  battito), le cadenze migrano in **config dichiarativa per entità**,
  versionata accanto alla skill: la config diventa la fonte di verità e il
  plan tiene solo il polso aggregato — stessa logica della config scheduler
  per la terza specie.

L'origine dal basso è `finanze-review` in `economia` (nata `monthly-review`,
rinominata 2026-07-12 proprio per il corollario del nome: l'oggetto tenuto
onesto sono le finanze, non il mese): la skill orchestra i parser, la
procedura vive in `o3/ciclo-finanze.md`, la ricorrenza in `## Scadenze` come
`(mensile)` col trigger esogeno (la busta paga) — il caso mono-battito è
quello degenere, non la norma: lì la porzione di mondo ha un orologio solo. Il
multi-battito è collaudato in `nixos` (refactor 2026-07-12 di `update-review`,
oggi `aggiorna` coi rami `ia|casa|lavoro|docker|all`): cadenze diverse per la
stessa capacità, esecutiva sul ramo AI e diagnostica sugli altri, dove lo
stesso argomento aggiorna input diversi. La skill `ordini` in `bi` (fornitore
come argomento, default `all`) porta il caso a molte entità: la cadenza tipica
di ogni fornitore vive nella config dichiarativa per fornitore ed è **modulata
dai segnali del mondo** (le vendite) — la cadenza dichiarata è l'attesa, il
mondo la corregge.

La ricorrenza può anche essere **a evento** invece che a orologio
(`elabora-trascrizione` in `salute`: il trigger è una nuova trascrizione da
ingerire, non una data): allora nessuna riga in `## Scadenze` — l'evento stesso
è il segnale, e forzarlo in una cadenza inventerebbe un orologio che non
esiste.

### Il montaggio come scope delle canoniche: ipotesi in pilota

La ricognizione della flotta (2026-08-01) mostra che le skill di dominio non
sono tutte atti da appendere a `perform`: si distribuiscono sui sei stadi e su
entrambi gli archi. Il canone incide **soltanto i sei scope-stadio**;
il declassamento delle skill di dominio ad argomenti delle canoniche
(`eval finanze`, `exec ordini <fornitore>`) è un'ipotesi sperimentale,
pilotata negli adottanti attraverso i loro `method-review` nell'ordine
`nixos` → `salute` → `economia` → `bi`. Il contratto di dispatch è la materia
del pilota: gli scope-stadio sono riservati e identici in ogni repo; uno scope
di dominio dichiara la mappa degli stadi che attraversa e produce un esito per
ciascuno; la capacità che attraversa entrambi gli archi non si forza sotto
l'arco sbagliato per conservare il nome. Ogni pilota decide per ciascuna
skill — assorbita come argomento, divisa fra i due archi, mantenuta autonoma —
e solo le forme provate risalgono a canone (dettaglio nel task
`o2/skill-archi-tripartite.md` finché il pilota è aperto).

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

Fotografia dalla ricognizione della flotta (2026-08-01, verificata sul posto;
`economia` e `salute` via `norvegia`→`deck`):

- **`metodo`** — quartetto canonico e copia di riferimento di `method-review`
  in `.claude/skills/`, con wrapper Codex; più la skill di dominio
  `adopters-review` — l'audit runtime-o1 mensile sugli adottanti (ricorrenza
  in `## Scadenze`, esiti nel filo `i3/audit-adottanti.md`), che non si forka
  perché il suo Mondo sono gli adottanti stessi e resta distinta dai due
  archi: produce materiale che `eval perceive` acquisisce. È il pilota dei sei
  scope canonici — il repo-modello applica a sé gli strumenti che teorizza.
- **`nixos`** — quartetto più `method-review` e la skill di dominio
  `aggiorna [ia|casa|lavoro|docker|all]` (già `update`): tre rami insistono
  sull'arco di valutazione (script-versioni come perceive, delta e changelog
  come interpret, il «vale la pena ora?» come compare), `ia` è perform pieno —
  esegue, committa e pusha in autonomia per regola del suo `CLAUDE.md`.
  `nix-overlay-update` non è registrata nel canone ed è candidata a
  retrocedere a runbook `o3/`. Primo pilota del montaggio di dominio.
- **`economia`** — quartetto più `method-review` e tre skill di dominio:
  `finanze-review` (l'arco di valutazione intero: parser come perceive,
  verifiche/fotografia/diario come interpret, riconciliazione delle scadenze
  come compare; procedura in `o3/ciclo-finanze.md`), `posta` e
  `registrazioni` (canali perceive puri: cattura valenza-neutra, sola lettura,
  handoff verso le review — che oggi citano per nome, da migrare alla
  rinomina). Register `goal.md`/`world.md` nati qui (pilot poli-register
  2026-07-09); catalogo delle skill locali in `o3/tools.md`, divergenza di
  forma-item intenzionale registrata nel ledger locale.
- **`bi`** — **origine della coppia di supervisione** (`52b2b600`, insieme al
  register `goal.md`) e tre skill di dominio: `ordini <fornitore>` (l'intero
  arco di esecuzione a runtime: composizione in priorità lessicografica come
  plan, file-ordine come specify, import Danea e invio come perform con
  ratifica umana al confine), `categorizza` e `tassonomia` (perform con
  guardrail: solo lo script scrive). È il caso più complesso e si pilota per
  ultimo.
- **`salute`** — quartetto più `method-review` e la skill di dominio
  `elabora-trascrizione`: perceive con distillazione (il confine verso
  interpret è da verificare nel pilota), ricorrenza a evento. Frontmatter di
  vecchio stile da normalizzare al recepimento. È il precedente del catalogo
  skill locali nell'indice o3.

La regola generale è: la funzione è ufficiale e metodologica, l'applicazione è
parametrizzata per-progetto. Il repo `metodo` non si limita a documentare il
pattern: lo dogfooda, possedendo la base canonica di riferimento; ogni repo
adottante la forka con la stessa struttura e con letture contestuali diverse.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [perceive](perceive.md)
- [interpret](interpret.md)
- [compare](compare.md)
- [plan](plan.md)
- [specify](specify.md)
- [perform](perform.md)
- [verdict](verdict.md)
- [goal](goal.md)
- [tasks](tasks.md)
- [kb-tools](kb-tools.md)
- [claude](claude.md)
- [agents](agents.md)
- [method-observatory](method-observatory.md)
