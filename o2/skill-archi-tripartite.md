---
sintesi: "Ritagliare il quartetto lungo il modello: `plan-review` e `verdicts-review` diventano `exec` ed `eval`, con i tre stadi del proprio arco come scope (`plan|specify|perform`, `perceive|interpret|compare`). Le procedure esistenti non si buttano, si rifilano sotto il loro stadio; si guadagna la casa per i1, i2 e o3, oggi scoperti. Si incide inizialmente solo la coppia canonica; il montaggio delle skill di dominio come argomenti resta ipotesi sperimentale da provare negli adottanti, nell'ordine `nixos` → `salute` → `economia` → `bi`."
ciclo: dev
---

# Skill per arco: `eval` ed `exec` tripartite

Verdetto e razionale nel filo
[`i3/skill-per-arco-tripartito.md`](../i3/skill-per-arco-tripartito.md); qui la
forma concreta e la sequenza di lavoro.

## Il canovaccio di `eval [perceive|interpret|compare|all]`

Il braccio di valutazione, nell'ordine del ciclo. Default `all`; ogni stadio può
essere invocato da solo, e ogni stadio può **chiudere in una riga** quando non ha
materia («nessun segnale nuovo»): la chiusura vuota è esito legittimo, non un
passo saltato.

**`perceive`** — raccogliere il grezzo dal Mondo, **valenza-neutro**. In `metodo`:
i marker `method-review.md` dei quattro adottanti, gli esiti già prodotti da
`kb-review`, i segnali che il custode porta da un altro repo. Negli adottanti:
posta, log, output di strumenti, documenti arrivati. `eval perceive` può
acquisire una diagnosi di `kb-review`, ma non la esegue implicitamente:
`kb-review` resta la capacità diagnostica dell'ala trasversale, fuori dai due
archi. Si cattura in `i1/` **solo** ciò che è effimero o che per precisione e
durata chiede un riflesso stabile
(`kb/perceive.md`): il grezzo persistente resta fuori. Nessuna valutazione qui —
il confine i1→i2 è l'ingresso della valenza, e anticiparlo è il difetto che lo
stadio esiste per impedire. Esito: cosa è entrato, cosa è stato catturato e
perché, cosa resta fuori.

**`interpret`** — distillare il grezzo in sintesi, **orientati dai goal sulla
rilevanza e neutri sulla valenza** (`kb/goal.md`). È lo stadio che oggi non ha
casa, e i suoi tre obblighi vengono dritti dai segnali appena valutati:

- **la provenienza delle quantità** (`kb/verdict.md`): un numero che entra in una
  sintesi dichiara se è misurato, dichiarato da terzi o derivato da
  dichiarazioni. Una quantità derivata non fa da architrave;
- **la cascata all'indietro**: quando un claim cambia o cade, le sintesi `i2/`
  che lo usavano si cercano e si correggono. La skill individua riferimenti
  espliciti e candidati semantici da verificare, senza promettere di riconoscere
  automaticamente ogni dipendenza implicita. È il buco che ha lasciato propagare
  la cifra dei «400 €/mese» in un'analisi e nella sua classifica di priorità dopo
  che era stata smentita;
- **il materiale di casa prima**: il file `o2/`, la corrispondenza in uscita, la
  valutazione di credibilità già scritta nella KB sono fonti primarie, non
  contesto.

Esito: quali sintesi sono nate o cambiate, contro quale materiale sono state
verificate, quali affermazioni restano non verificate e sono dichiarate tali.

**`compare`** — il verdetto contro il Goal: è la procedura attuale di
`verdicts-review`, rifilata sotto il suo stadio. Le cinque domande per ogni filo
(è ancora vero rispetto al segnale, incluso il file `o2/`? è più sicuro del suo
materiale? è ancora aperto? è ancora _un_ filo? è stato, non log?), la copertura
bidirezionale col register `goal.md`, la formazione-goal sugli input esogeni
**sempre in proposta al custode**, la bonifica del plan dalla narrativa di stato,
e l'handoff «impatti sul piano» verso `exec`.

## Il canovaccio di `exec [plan|specify|perform|all]`

Il braccio di esecuzione, nell'ordine del ciclo, simmetrico a `eval`: default
`all`, ogni stadio invocabile da solo, e anche qui ogni stadio può **chiudere
in una riga** quando non ha materia («coda coerente, nessun intervento») — il
criterio di chiusura pretende un esito esplicito da tutti e sei gli scope, e
l'esito nullo è esito.

**`plan`** — la coda: drift `o1/plan.md`↔`o2/` — il contratto plan×`o2/` lo
verifica il generatore, e lo scope lo invoca e ne interpreta l'esito, non lo
reimplementa —, ordine e priorità, dipendenze reali (non preferenze d'ordine),
direzione task→obiettivo letta dalla colonna `Ob.`, `## Scadenze` e finestre
tattiche, task consigliato per la sessione. È il cuore dell'attuale
`plan-review`.

**`specify`** — i dettagli, con un confine netto verso `plan`: `plan` guarda la
corrispondenza e l'ordine delle righe (il piano come coda, generatore incluso),
`specify` la qualità interna dei file `o2/` — la corrispondenza non si verifica
in due case. Ogni task sostanziale ha il suo file, il frontmatter è completo
(`sintesi`, `ciclo`), i diari di sessione si potano a chiusura. Qui vivono le
**quattro proprietà cardine** come criteri di qualità dell'o2 — visibilità,
feedback, mapping, constraint (`kb/specify.md`) — che oggi nessuna skill
controlla mai.

**`perform`** — predisporre o compiere l'atto, secondo autorizzazione. Nel
canone: la collezione `o3/` tiene solo il vivo (prescrizioni consumate potate,
`kb/perform.md`), gli strumenti registrati sono ancora eseguibili, i runbook di
propagazione riflettono il canone corrente. Quando l'atto è locale, reversibile
e già autorizzato, `exec perform` lo compie davvero; quando tocca il Mondo o
richiede nuova autorità, produce o valida la prescrizione e si ferma al confine.
La sezione seguente conserva la ricognizione degli atti di dominio come ipotesi
da pilotare, senza anticiparne il montaggio nel canone.

## Scope di dominio: ipotesi da pilotare

La ricognizione della flotta (sotto) suggerisce che le skill di dominio non
siano tutte atti da appendere a `perform`: si distribuiscono sui sei stadi e su
entrambi gli archi. È una direzione promettente, non ancora canone. Il primo
taglio incide soltanto i **sei scope-stadio canonici**; l'eventuale
declassamento delle skill di dominio ad argomenti di `eval` ed `exec` resta
un'ipotesi sperimentale da verificare negli adottanti attraverso la
prescrizione e il loro `method-review`.

Il pilota deve risolvere il contratto di dispatch, che il canone iniziale non
finge già noto:

- gli scope-stadio (`eval interpret`, `exec perform`) sono riservati e hanno
  semantica identica in ogni repo;
- uno scope di dominio candidato (`eval finanze`, `exec ordini`) può
  attraversare uno o più stadi del proprio arco, ma deve dichiararne la mappa e
  produrre un esito distinto per ciascuno;
- se una capacità attraversa entrambi gli archi, il pilota decide se
  rappresentarla con due argomenti omonimi, dividerla o lasciarla skill
  autonoma: non la forza sotto l'arco sbagliato per conservare il nome;
- l'invocazione di un singolo stadio dentro uno scope di dominio e la
  composizione con `all` sono questioni aperte del pilota, non grammatica
  canonica anticipata.

Indicazioni di massima da sottoporre al pilota:

- **grammatica candidata a due livelli**: lo scope di dominio conserva i propri
  argomenti — `exec aggiorna casa`, `exec categorizza life 50`,
  `eval finanze`;
- **se il pilota la conferma, la scelta del ramo sale nella skill**: giorno
  contro `## Scadenze`, host corrente, cadenze in config dichiarativa per
  entità — ciò che oggi decide l'umano scegliendo l'argomento;
- **nomi**: le canoniche portano l'arco del modello in inglese — il telos è
  portare il metodo intero, KB compresa, in inglese — nella forma abbreviata
  che la mano digita: **`eval`** ed **`exec`** (custode, 2026-08-01). La forma
  lunga Evaluate/Execute sopravvive solo come nome dell'arco nel canone, mai
  come nome della skill: un nome solo ovunque, o qualcuno «correggerà»
  `eval`→`evaluate` credendo di sanare un drift. Gli scope-stadio restano per
  esteso — sono i nomi degli atomi e degli indici, e la catena
  `eval interpret` → `kb/interpret.md` → `i2/interpretations.md` non si
  abbrevia. Gli scope di dominio portano il vocabolario del dominio
  (`aggiorna`, `ordini` — in italiano dove la regola locale lo chiede, come in
  `nixos`), che resta nella lingua del suo Mondo anche a metodo anglicizzato;
- **autorizzazione**: il confine segue le risorse dello scope, non la skill —
  lo stesso arco è esecutivo su un ramo e diagnostico su un altro.

## Matrice sperimentale della flotta (ricognizione 2026-08-01)

Verificata sul posto per tutti e quattro (2026-08-01; `economia` e `salute`
via `norvegia`→`deck`).

- **`nixos` · `aggiorna [ia|casa|lavoro|docker|all]`** — collocazione candidata:
  `eval aggiorna` per i rami diagnostici ed `exec aggiorna` per quelli
  esecutivi, oppure skill autonoma se il doppio montaggio aumenta l'attrito;
  stadi: `perceive` → `interpret` → `compare` per tre rami, `perform` pieno per
  `ia`; confidenza: **media**; questione del pilota: una capacità unica può
  abitare due archi senza mentire nel signifier? `nix-overlay-update` non è
  registrata nel canone ed è candidata a retrocedere a runbook `o3/`.
- **`salute` · `elabora-trascrizione`** — collocazione candidata: `eval
trascrizione`; stadi: soprattutto `perceive`, con una distillazione il cui
  confine verso `interpret` va verificato; confidenza: **alta** sulla famiglia
  `eval`, **media** sullo stadio; questione del pilota: la distillazione produce
  ancora grezzo catturato o già una sintesi? Il frontmatter è di vecchio stile
  (`name`/`disable-model-invocation`, niente `user-invocable`).
- **`economia` · `finanze-review`** — collocazione candidata: `eval finanze`;
  stadi: intero arco (`perceive` parser, `interpret` verifiche/fotografia/diario,
  `compare` riconciliazione delle scadenze); confidenza: **alta**; questione del
  pilota: il nuovo argomento conserva un handoff leggibile verso `exec plan`?
- **`economia` · `posta`, `registrazioni`** — collocazione candidata: `eval
posta` ed `eval registrazioni`; stadi: `perceive`; confidenza: **alta**;
  questione del pilota: evitare che un canale event-driven diventi un passaggio
  rituale. Le skill sono sola lettura e oggi citano `/verdicts-review` e
  `/plan-review` per nome.
- **`bi` · `ordini <fornitore>`** — collocazione candidata: `exec ordini
<fornitore>`; stadi: intero arco (`plan` priorità lessicografica, `specify`
  file-ordine, `perform` import Danea e invio futuri); confidenza: **media**;
  questione del pilota: preservare ratifica umana, config per fornitore e
  confine fra specifica presente e atti futuri. È il caso più complesso e si
  pilota per ultimo.
- **`bi` · `categorizza`, `tassonomia`** — collocazione candidata: `exec
categorizza`, `exec tassonomia`; stadi: `perform` con guardrail; confidenza:
  **alta** sulla collocazione; questione del pilota: dimostrare che
  l'assorbimento non nasconda il vincolo «solo lo script scrive».
- **Arretrato dei fork**: **tutti e quattro** portano quattro domande in
  `verdicts-review` (manca «è più sicuro del suo materiale?», `64f0ec0`). Il
  backport è **sganciato** da questo task (custode, 2026-08-01): viaggia
  subito nella mini-prescrizione `o3/quinta-domanda-verdetti.md` — la domanda
  è la guardia contro il modo di fallimento dei «400 €/mese», e attenderne la
  rinomina l'avrebbe lasciata spenta negli adottanti per settimane note; la
  prescrizione grande porta solo la rifilatura. E gli
  handoff delle skill-canale di `economia` (`posta`, `registrazioni`) citano
  `/verdicts-review` e `/plan-review` **per nome**: il grep della rinomina va
  esteso alle skill di dominio degli adottanti.

## Invarianti che sopravvivono alla rifilatura

La rifilatura si fa **a diff contro le due SKILL.md correnti**: ogni passo
esistente ha una destinazione dichiarata sotto uno stadio, o una rimozione
motivata. In particolare i pezzi che le enumerazioni sopra non nominano:

- il **gate proponi-poi-applica**: le modifiche a collezioni e register si
  applicano dopo conferma del custode, e il gate **prevale
  sull'autorizzazione generica delle bussole** — in `metodo` il `CLAUDE.md`
  consente la scrittura di `o1/plan.md` e dei fili `i3/` senza chiedere, ma
  quella copertura è per il lavoro ordinario di sessione, non per
  l'auto-applicazione degli esiti di una supervisione; fa eccezione solo
  l'atto che l'autorizzazione dello scope già copre (`aggiorna ia`);
- i **due handoff**: `eval compare` emette «impatti sul piano», `exec
plan` chiude con l'inverso «verdetti da rivalutare» — il ritorno resta
  l'eccezione da giustificare al custode, il vuoto resta buon segno;
- la **lettura strategica delle mosse** (il passo 3b di `plan-review`:
  mandato/canale, sequenza/informazione, effetti di secondo ordine) vive sotto
  `exec plan`;
- le **lezioni della bonifica** («migrare è fondere, non cancellare»; «chi
  altro legge la copia, macchine incluse») vivono sotto `eval compare`.

## Cosa tocca

- **Skill**: `.claude/skills/eval/`, `.claude/skills/exec/` e i wrapper
  `.codex/skills/` corrispondenti; rimozione di `plan-review` e
  `verdicts-review` **dopo** che il contenuto è stato rifilato, non prima.
- **`kb/skill.md`**: è la riscrittura più profonda — «Base ufficiale», la coppia
  simmetrica di supervisione, la regola dei nomi (che passa da «l'indice che
  tiene onesto» a «l'arco del modello, abbreviato per la mano: `eval`/`exec`»,
  con le due ragioni del cambio — la copertura e il telos inglese), il
  protocollo post-evento (che cita le skill per nome), «Applicazione nei repo
  del metodo» — quest'ultima riscritta **dalla realtà della flotta**
  (ricognizione sopra), non dal testo corrente, che è già stantio
  (`update`→`aggiorna`, `nix-overlay-update` mai registrata, le tre skill di
  `bi`).
- **Consumatori della coppia corrente**: fare un grep completo al momento
  della migrazione e classificare ogni occorrenza come normativa, operativa o
  storica. Le occorrenze normative e operative vanno migrate; i fili storici
  possono conservare il nome che descrive il fatto passato. L'inventario vivo
  noto comprende almeno `goal.md`, `kb/skill.md`, `kb/plan.md`, `kb/goal.md`,
  `kb/verdict.md`, `kb/perceive.md`, `kb/interpret.md`, `kb/compare.md`,
  `kb/specify.md`, `kb/perform.md`, `kb/project-structure.md`,
  `kb/cognitive-artifact-design.md`, `kb/adopter-comparison.md`,
  `.claude/skills/commit/SKILL.md` e `.claude/skills/method-review/SKILL.md`.
  Gli atomi degli stadi guadagnano il rimando alla propria fetta di skill.
- **Bussole**: `README.md` e `CLAUDE.md` di `metodo` (l'elenco commentato delle
  skill), e negli adottanti gli stessi due file più le righe `## Scadenze` e le
  skill di dominio che citano la coppia per nome nei propri handoff (`posta`,
  `registrazioni`).
- **`i1/perceptions.md`, `i2/interpretations.md`, `o3/prescriptions.md`**: i tre
  indici finora senza guardiano guadagnano il rimando alla fetta di skill che
  li mantiene.

## Sequenza

1. **fatto** (`20299fd`) — riscrivere `kb/skill.md` col taglio nuovo (il
   canone prima delle skill: le skill sono interfacce sul canone, non la sua
   sede); il nodo resta `stato: bozza` fino a pilota concluso — l'incisione è
   al passo 5;
2. **fatto** (`f1e654e`) — scrivere `eval` ed `exec` in `metodo`, rifilando le
   procedure esistenti **a diff contro le due SKILL.md correnti**
   (§Invarianti) e aggiungendo i tre stadi scoperti; wrapper Codex;
3. l'ipotesi su `adopters-review` è fissata (task e filo): resta skill di
   dominio distinta e produce materiale che `eval perceive` può acquisire;
   l'assorbimento è una variante da rivalutare solo dopo l'uso, non
   un'ambiguità dell'interfaccia da pilotare;
4. **pilotare su `metodo`** i due archi end-to-end su almeno un evento reale;
   ogni scope restituisce un esito esplicito, anche nullo, e il filo registra
   attriti, sovrapposizioni e passaggi che non hanno cambiato l'artefatto
   _prima_ di propagare. **Primo giro compiuto** (2026-08-01: sei esiti,
   attriti e conferme nel filo); il secondo collaudo candidato è il battito
   `/adopters-review` del 2026-08-11, che porta esattamente la posta che
   `eval perceive` raccoglie — l'incisione del passo 5 attende quel giro;
5. aggiornare nodi, register, bussole e skill consumatrici (incisione dei soli
   sei scope canonici in `kb/skill.md`); emettere la prescrizione `o3/` per i
   quattro. La prescrizione porta la matrice sopra come **ipotesi di
   montaggio**, non come esito già deciso; l'arretrato della quinta domanda
   viaggia già per conto suo (`o3/quinta-domanda-verdetti.md`);
6. prescrivere il pilotaggio del montaggio di dominio attraverso i
   `method-review` degli adottanti, nell'ordine **`nixos` → `salute` →
   `economia` → `bi`**. L'esecuzione resta nelle loro code; ogni pilota decide
   esplicitamente per ciascuna skill: assorbita come argomento, divisa fra i
   due archi oppure mantenuta autonoma. I risultati correggono la prescrizione
   e solo le forme provate risalgono poi a canone;
7. alla chiusura, aprire il task di rivalutazione `pause` con la condizione di
   risveglio della clausola di uscita (filo `i3/`).

## Criterio di chiusura

Le due skill esistono in `metodo` e sono state invocate end-to-end su almeno un
evento reale; ciascuno dei **sei scope-stadio canonici** ha restituito un esito
esplicito, anche nullo, e il filo registra attriti, sovrapposizioni e passaggi
che non hanno cambiato l'artefatto. Il canone iniziale in `kb/skill.md` incide
soltanto quei sei scope; la prescrizione per i quattro è aperta e dichiara
sperimentale il montaggio di dominio. Il task `pause` di rivalutazione esiste
con risveglio al terzo battito successivo al recepimento dai quattro. Il
recepimento completo degli adottanti **non** è parte di questo task: è la loro
coda e si misura col battito mensile.
