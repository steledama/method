---
sintesi: "Ritagliare il quartetto lungo il modello: `plan-review` e `verdicts-review` diventano `exec` ed `eval`, con i tre stadi del proprio arco come scope (`plan|specify|perform`, `perceive|interpret|compare`). Le procedure esistenti non si buttano, si rifilano sotto il loro stadio; si guadagna la casa per i1, i2 e o3, oggi scoperti. Le skill di dominio della flotta migrano a scope delle due canoniche, su entrambi gli archi. Pilota `metodo`, poi prescrizione o3 per i quattro."
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

**`plan`** — la coda: drift `o1/plan.md`↔`o2/`, ordine e priorità, dipendenze
reali (non preferenze d'ordine), direzione task→obiettivo letta dalla colonna
`Ob.`, `## Scadenze` e finestre tattiche, task consigliato per la sessione. È il
cuore dell'attuale `plan-review`.

**`specify`** — i dettagli, con un confine netto verso `plan`: `plan` guarda la
corrispondenza e l'ordine delle righe (il piano come coda), `specify` la
qualità interna dei file `o2/`. Ogni task sostanziale ha il suo file, il
frontmatter è completo (`sintesi`, `ciclo`), i diari di sessione si potano a
chiusura; il contratto plan×`o2/` lo verifica il generatore — lo scope lo
invoca e ne interpreta l'esito, non lo reimplementa. Qui vivono le **quattro
proprietà cardine** come criteri di qualità dell'o2 — visibilità, feedback,
mapping, constraint (`kb/specify.md`) — che oggi nessuna skill controlla mai.

**`perform`** — predisporre o compiere l'atto, secondo autorizzazione. Nel
canone: la collezione `o3/` tiene solo il vivo (prescrizioni consumate potate,
`kb/perform.md`), gli strumenti registrati sono ancora eseguibili, i runbook di
propagazione riflettono il canone corrente. Quando l'atto è locale, reversibile
e già autorizzato, `exec perform` lo compie davvero; quando tocca il Mondo o
richiede nuova autorità, produce o valida la prescrizione e si ferma al confine.
Gli atti di dominio si montano secondo la direzione dichiarata nella sezione
seguente — non più «ammesso, non prescritto».

## Scope di dominio: la direzione dichiarata

La ricognizione della flotta (sotto) rovescia l'inciso «un dominio può montare
qui i propri atti»: le skill di dominio esistenti non sono atti da appendere a
`perform` — si distribuiscono sui sei stadi, su **entrambi** gli archi. La
direzione è del custode (2026-08-01, incisa nel filo): **le skill di dominio
diventano scope delle due canoniche**, montate sullo stadio che servono; la
mappatura di dettaglio resta all'adottante, dentro la prescrizione. Regole del
montaggio:

- **grammatica a due livelli**: lo scope di dominio conserva i propri
  argomenti — `exec aggiorna casa`, `exec categorizza life 50`,
  `eval finanze`;
- **la scelta del ramo sale nella skill**: giorno contro `## Scadenze`, host
  corrente, cadenze in config dichiarativa per entità — ciò che oggi decide
  l'umano scegliendo l'argomento;
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

## La flotta reale (ricognizione 2026-08-01)

Verificata sul posto per tutti e quattro (2026-08-01; `economia` e `salute`
via `norvegia`→`deck`).

- **`nixos`** — `aggiorna [ia|casa|lavoro|docker|all]` (già `update`,
  rinominata coi rami nuovi): tre rami su quattro sono valutazione (gli script
  versioni sono perceive, delta e changelog sono interpret, il «vale la pena
  ora?» è il verdetto), solo `ia` è perform pieno — ed esegue, committa e
  pusha già oggi in autonomia. Candidata `exec aggiorna <ramo>`, con
  l'avvertenza che i rami diagnostici sono materia d'arco eval: la
  mappatura fine è del pilota-adottante. `nix-overlay-update` non è registrata
  nel canone ed è una procedura più che un'interfaccia: candidata a
  retrocedere a runbook `o3/` invocato da `exec perform`.
- **`bi`** — tre skill di dominio, non una. `ordini` è l'**intero arco exec
  a runtime**: compone l'ordine dai goal in priorità lessicografica (plan), a
  regime persiste il file-ordine `o2/` (specify), l'import Danea e l'invio
  futuri sono perform con ratifica umana al confine → `exec ordini
<fornitore>`. `categorizza` e `tassonomia` sono perform con guardrail (solo
  lo script scrive) → `exec categorizza`, `exec tassonomia`.
- **`economia`** — tre skill di dominio, non una. `finanze-review` è il giro
  runtime di valutazione intero (parser = perceive, verifiche/fotografia/
  diario = interpret, riconciliazione scadenze = il confronto con o1);
  `posta` e `registrazioni` sono **canali i1 puri** — cattura valenza-neutra,
  sola lettura, handoff alle review senza eseguirle: `eval perceive`
  runtime da manuale → candidate `eval finanze`, `eval posta`,
  `eval registrazioni`. Il canone conosce solo `finanze-review`.
- **`salute`** — `elabora-trascrizione` distilla la trascrizione grezza in
  documento per `perceptions/`: perceive con distillazione, arco eval →
  candidata `eval trascrizione`. Frontmatter di vecchio stile
  (`name`/`disable-model-invocation`, niente `user-invocable`): la
  prescrizione la normalizza.
- **Arretrato dei fork**: **tutti e quattro** portano quattro domande in
  `verdicts-review` (manca «è più sicuro del suo materiale?», `64f0ec0`): la
  prescrizione assorbe rifilatura e arretrato in un solo recepimento. E gli
  handoff delle skill-canale di `economia` (`posta`, `registrazioni`) citano
  `/verdicts-review` e `/plan-review` **per nome**: il grep della rinomina va
  esteso alle skill di dominio degli adottanti.

## Invarianti che sopravvivono alla rifilatura

La rifilatura si fa **a diff contro le due SKILL.md correnti**: ogni passo
esistente ha una destinazione dichiarata sotto uno stadio, o una rimozione
motivata. In particolare i pezzi che le enumerazioni sopra non nominano:

- il **gate proponi-poi-applica**: le modifiche a collezioni e register si
  applicano dopo conferma del custode; fa eccezione solo l'atto che
  l'autorizzazione dello scope già copre (`aggiorna ia`);
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
- **Nodi che citano le due skill per nome**: `kb/plan.md`, `kb/goal.md`,
  `kb/verdict.md`, `kb/perceive.md`, `kb/interpret.md`, `kb/compare.md`,
  `kb/specify.md`, `kb/perform.md` — da verificare con un grep, non a memoria.
  Gli atomi degli stadi guadagnano il rimando alla propria fetta di skill.
- **Bussole**: `README.md` e `CLAUDE.md` di `metodo` (l'elenco commentato delle
  skill), e negli adottanti gli stessi due file più le righe `## Scadenze` e le
  skill di dominio che citano la coppia per nome nei propri handoff (`posta`,
  `registrazioni`).
- **`i1/perceptions.md`, `i2/interpretations.md`, `o3/prescriptions.md`**: i tre
  indici finora senza guardiano guadagnano il rimando alla fetta di skill che
  li mantiene.

## Sequenza

1. riscrivere `kb/skill.md` col taglio nuovo (il canone prima delle skill: le
   skill sono interfacce sul canone, non la sua sede); il nodo resta
   `stato: bozza` fino a pilota concluso — l'incisione è al passo 5;
2. scrivere `eval` ed `exec` in `metodo`, rifilando le procedure
   esistenti **a diff contro le due SKILL.md correnti** (§Invarianti) e
   aggiungendo i tre stadi scoperti; wrapper Codex;
3. l'ipotesi su `adopters-review` è fissata (task e filo): resta skill di
   dominio distinta e produce materiale che `eval perceive` può acquisire;
   l'assorbimento è una variante da rivalutare solo dopo l'uso, non
   un'ambiguità dell'interfaccia da pilotare;
4. **pilotare su `metodo`** i due archi end-to-end su almeno un evento reale —
   candidato naturale il battito `/adopters-review` del 2026-08-11, che porta
   esattamente la posta che `eval perceive` raccoglie; ogni scope
   restituisce un esito esplicito, anche nullo, e il filo registra attriti,
   sovrapposizioni e passaggi che non hanno cambiato l'artefatto _prima_ di
   propagare;
5. aggiornare nodi e bussole (incisione di `kb/skill.md`); emettere la
   prescrizione `o3/` per i quattro, col pilota-adottante scelto lì (candidato
   `nixos`: multi-scope collaudato e `aggiorna` come primo montaggio). La
   prescrizione porta, per ogni adottante, la mappatura skill-di-dominio→scope
   (la ricognizione è completa, 2026-08-01) e l'arretrato dei fork (la quinta
   domanda);
6. alla chiusura, aprire il task di rivalutazione `pause` con la condizione di
   risveglio della clausola di uscita (filo `i3/`).

## Criterio di chiusura

Le due skill esistono in `metodo` e sono state invocate end-to-end su almeno un
evento reale; ogni scope ha restituito un esito esplicito, anche nullo, e il
filo registra attriti, sovrapposizioni e passaggi che non hanno cambiato
l'artefatto. Il canone in `kb/skill.md` è inciso e la prescrizione per i quattro
è aperta. Il recepimento degli adottanti **non** è parte di questo task: è loro
coda, e si misura col battito mensile.
