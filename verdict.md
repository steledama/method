# verdict.md

Il verdetto attuale del progetto, per filo/area aperta — non un log. Il git log dice
_cosa_ è cambiato; questo file dice _come stanno le cose ora_ su ciascun filo
concettuale aperto, e _perché conta_. Specchio di `plan.md` sul lato valutazione:
`plan.md` fotografa i task aperti (o1), `verdict.md` i verdetti aperti (i3). Forma e
disciplina canoniche in [`kb/verdict.md`](kb/verdict.md).

Ogni gruppo `##` è un filo aperto; il corpo è lo **stato attuale**, aggiornato in
place, non una sequenza di entry datate (la cronologia di un filo è il git history di
questo file stesso). Quando un filo si chiude — verdetto stabile, nessuna tensione
aperta — il gruppo si rimuove: la storia resta in git. Il commit citato inline è il
puntatore alla storia verificabile.

---

## De-cablaggio del binomio «due agenti»: la seconda metà resta bottom-up

Il metodo è nato descrivendo due agenti — l'umano e un singolo LLM — e su quel binomio
aveva cablato la sua asimmetria in più nodi come se fosse _la_ struttura. Il nodo
`agent` lo ha riconosciuto per ciò che è: il **caso saliente** di una popolazione di
agenti più ampia (Norman: «person, animal, or machine»; la categoria macchina è un
gradiente, non un punto — un LLM di frontiera che pianifica e un agente locale che
esegue non sono lo stesso lettore sulla stessa KB). La prima metà è fatta, e
**additiva**: ammorbiditi `system-image`, `cognitive-system`, `knowledge-base`
togliendo al binomio lo statuto di struttura unica, senza cancellare il caso umano/LLM
— resta vero _come caso_, ed è l'unico in uso a valle (i nodi viaggiano per symlink).
La seconda metà — maturazione di `agent`, biforcazione di o1 per capacità dell'agente,
asse fiducia/privacy, divisione per stadio del ciclo — resta **deliberatamente non
scritta**: attende che un secondo livello di agente entri nell'uso reale. Scriverla ora
sarebbe inventare struttura prima dell'evidenza, l'opposto di come il metodo si
sviluppa.

## Maturazione dei nodi fondativi e debiti di fonte

La rifondazione ontologica (artefatto/sistema/metodo) e l'arco di input (i1/i2/i3)
hanno dato al metodo il vocabolario che gli mancava — cosa _è_ l'oggetto che coltiva,
cosa _vuole_ chi lo usa — ma i nodi che lo reggono sono ancora `bozza`, in attesa della
maturazione `bozza→maturo` dall'uso reale: `cognitive-artifact`, `cognitive-system`,
`goal`, `output`, `agent`, e i nodi i2 fondati su Norman (`affordance-signifier`,
`system-image`, `processing-layers`). **Nessun debito di fonte fondativo resta aperto**:
**Leontiev** (per `goal`, _Activity, Consciousness, and Personality_) è reperito e §3.5
«The General Structure of Activity» è sorzata nel nodo: conferma attività/motivo,
azione/goal o scopo cosciente, operazione/condizioni. Saldati
in precedenza: **Hutchins** (per `cognitive-system`) e il filone **mente estesa**
(Clark) sono ora sourced e **promossi nel pavimento ontologico** di `cognitive-system`
(active externalism, parity, scaffolding, 007, mente-come-controllore, più il criterio
scaffold action-oriented contro il modello «filing cabinet»). **_Things That Make
Us Smart_** (Norman 1993) è ora integrale e **distillato (i2)** nei capitoli portanti: Cap. 2
(esperienziale vs riflessivo — sorza la naturalezza e il «KB come scaffold del modo
riflessivo»; i due-modi 1993 sono l'origine dei tre-livelli di `processing-layers`) e Cap. 6
(la cognizione distribuita di **Norman stesso**, che cita Hutchins — pavimento Hutchins+Clark+Norman,
una famiglia UCSD; più «the world remembers by being there» ↔ membrana `world`, e gli errori
condivisi come training rigenerativo). Destinazioni i3 — `cognitive-artifact`, `cognitive-system`,
`processing-layers`, `affordance-signifier` — **scritte nella chirurgia del 2026-06-21**, insieme
al nodo nuovo `augmentation-system` (la cornice H-LAM/T che le contiene); resta aperta solo la
maturazione `bozza→maturo` di questi nodi, che attende l'uso reale. La
matrice 4D del ciclo, infine, è un falsificatore
costruito sulle definizioni del metodo stesso: il suo esito «zero forzati» resta
**provvisorio finché non lo si testa su un repo nato senza il metodo**.

## Il lato-input appena rifondato: verdict come i3, interpretations come i2-macro

Il fronte più fresco (commit `dd5c2e7` + questa sessione): due artefatti del ciclo di
sviluppo hanno appena preso forma sul lato valutazione. **`verdict.md` è il residuo
scritto dell'i3** (Compare) — da log datato append-only a stato corrente per filo
aggiornato in place; disciplina ora canonica in `kb/verdict.md`, e questa migrazione ne
è la prima istanza reale (ciò che ha portato il nodo a `maturo`). **`interpretations/`
è i2-macro**: la sintesi periodica che rilegge l'intero artefatto e rivela tensioni
non-locali tra nodi. Il pilot su `economia` ha corretto la distinzione troppo rigida
tra i repo: la stessa superficie è o2 quando viene prodotta come vista di decisione e
substrato i2 quando viene letta; selezione e rappresentazione dei dati sono già
interpretazione orientata dai goal. La porta canonica è quindi `interpretations/`
ovunque, con il carattere nel contenuto. La propagazione ora ha un protocollo:
`method-review` usa un marker SHA versionato e lascia il lavoro pertinente nel repo
adottante. `economia` è il primo pilot committato; `nixos` è il secondo, committato
in `5d076ae`, e conferma il carve-out per output di altra natura ontologica
(configurazione Nix runtime, nessuna porta `interpretations/` vuota). La
propagazione è conclusa nei quattro adottanti: `economia` in `4c633b8`, `nixos`
in `5d076ae`, `bi` in `48f9e2cc`, `salute` in `bc1eaef`. Il caso BI conferma che
l'uniformità del protocollo non deve
interferire con opzioni applicative omonime: `--append-note` resta dominio,
`--append-why` era infrastruttura di audit. Il caso salute conferma che privacy,
diario, scadenze, fonti e skill di ingest sono adattamenti di contenuto e
workflow, non eccezioni alla struttura comune. _Ri-derivazione del deck_: chiusa.
Il deck è stato ri-derivato — esprime il framing i2-micro/macro e ha ricevuto un
restage viscerale che applica `processing-layers` a sé stesso. La slide che diagnostica
«un o2 solo riflessivo non muove» era resa in registro puramente riflessivo: il deck
commetteva il peccato che descrive. Ora contrasto, gerarchia e tre slide-eroe (con
l'accento caldo che lega il viscerale alla membrana `world`) portano la sintesi fino al
viscerale; il colpo «Attractive things work better» segue la slide della stasi, così il
deck _performa_ la lezione invece di solo enunciarla. La disciplina del nodo `deck`
(HTML/CSS nativi, build unica `pandoc`+`prettier`) è rimasta intatta.

## L'atrio rifondato: i1 è `perceptions/`, le fonti sono `world`, i file di dominio per funzione

Emerso dal-basso dall'adozione in `economia` (migrazione di `data/json/` verso l'i1
versionata) e sciolto qui. Lo strato output nomina le collezioni per stadio cognitivo
— `interpretations/` (Interpret), `prescriptions/` (Prescrivi) — mentre l'i1 portava
`sources/`, un nome per provenienza: asimmetria e signifier che mente. La collezione i1
si chiama **`perceptions/`** (Perceive), come già fissava `input.md`; `project-structure`,
le porte e `README` sono allineati. Il nodo della decisione, sciolto in revisione: i
**libri sono `world`** — grezzo esterno autorevole (`source-of-truth`) che vive su Drive,
**fuori** dall'artefatto — e diventano i1 (`perceptions/`) solo se un'elaborazione li
cattura; altrimenti restano Mondo. Quindi `sources/` non era la collezione i1, era
classificato sull'asse sbagliato. `sources.md` **resta versionato** ma declassato da
porta-collezione a **register di provenienza** (sibling di `map.md`): il riflesso
portabile «quale edizione regge quale nodo» che alimenta i `## Riferimenti` (i3), mentre
i binari escono del tutto su `world`. `.gitignore` non ha più la regola `sources/*`
(niente cartella d'artefatto). `method` non materializza `perceptions/` (i1 effimera:
solo le citazioni nei Riferimenti). Propagazione: gli adottanti recepiscono via
`method-review`; `economia` adotta `perceptions/` direttamente nella migrazione imminente,
evitando la doppia rinomina.

Il gemello `collocazione-file-dominio` è sciolto: gli artefatti del **runtime del dominio**
si collocano per stadio cognitivo, non in root — `diario` (i1)→`perceptions/` tenuto
valenza-neutro, `stato` (i2)→`interpretations/` come i2 testuale accanto al deck. Le
`scadenze` non sono un artefatto i/o ma un **vincolo di pianificazione** che ordina i task:
vanno in una sezione di `plan.md`. La root resta il cruscotto del solo ciclo di sviluppo.
Nodo della decisione: «root estensibile dal basso» contraddiceva «il cruscotto è il ciclo
di sviluppo, non il runtime»; sciolta in favore della funzione, perché posizione≠bootstrap
(l'ordine in `CLAUDE` può puntare a `interpretations/stato.md` senza tenerlo in root).
Formalizzata in `project-structure` la **terza specie** di file-root — i _register_
(`map.md`, `sources.md`) che puntano fuori dall'artefatto — accanto a file-ciclo e
porte-collezione.

La propagazione ha ora una casa concreta, e con essa `method` completa il proprio
atrio. Il meta-artefatto materializza il suo arco i1/o3 attraverso la membrana degli
adottanti (il suo Mondo runtime): **`perceptions/`** (i1 — il segnale metodologico che
un adottante solleva, catturato valenza-neutro; un adottante perciò non pianifica il
canone nel proprio `plan.md`, emette un segnale) e **`prescriptions/`** (o3 — il runbook
di adozione, eseguito dal `method-review` dell'adottante: o3 prescrive, method-review
compie l'atto). Toglie la forzatura — far pianificare il canone dall'esterno — e dà
`method` l'atrio completo del ciclo (i1/i2/i3 e o2/o3), così fa da modello dogfoodando
input e output, non solo la KB. Primo i1 reale: `perceptions/adottanti-pianificano-il-canone-in-plan.md`;
il primo o3 reale fu il runbook di adozione del nuovo atrio, poi rimosso a propagazione
conclusa. La regola del canale vive in `project-structure`.

## Rifondazione atrio↔azione: gradiente di cardinalità, atomi di stadio, system image visiva

Filo di design aperto in questa sessione; **in esecuzione** (lavoro in `plan.md`). La
**disambiguazione KB riflessivo ↔ system-image**, gli **atomi di stadio** e l'**atrio a
tre specie** sono fatti; resta la **system image visiva**, che in sessione di
design 2026-06-15 si è allargata in un **cluster di task pianificati** (cfr.
`plan.md`, task 1-4), ridefinito il 2026-06-17 con la distinzione **dev/runtime**
resa esplicita e un gate di verifica inserito prima della costruzione. La categoria
«porta-collezione» era **falsamente uniforme**: trattava allo stesso modo la KB (system
image), gli strumenti (macchina del ciclo di sviluppo) e gli stadi i1/i2/o3 — cose di tre
specie diverse.

**Il gradiente di cardinalità** è la lettura che le separa e dà il razionale della
collocazione. Il ciclo è un funnel a due poli: il Goal è il punto di convergenza
(singolare), il Mondo la molteplicità grezza ritagliata per rilevanza. L'arco di
valutazione distilla il molteplice verso l'uno, l'arco di esecuzione dispiega l'uno
verso il molteplice. Quindi la **triade alta** — Goal (`README`), Plan/o1 (`plan.md`),
Compare/i3 (`verdict.md`) — ha un'unica istanza corrente aggiornata in place: entità =
**file**. Scendendo, ogni stadio accumula: Specify→`tasks/`, i1→`perceptions/`,
i2→`interpretations/`, o3→`prescriptions/`: entità = **cartella**. File in cima,
cartelle in fondo, combacia con i poli e con i tre livelli (riflessivo=unità,
behavioral/viscerale=molteplicità).

Conseguenze decise:

- **`plan.md` = o1-sviluppo, `verdict.md` = i3-sviluppo (fatto)**: qualificatore di ciclo,
  non negazione dell'omologia (`action-cycle` mappa Plan=o1, Compare=i3). Corretto in
  `project-structure`, `plan`, `verdict`, `output`; la vecchia «plan non è o1» è superata.
- **Atomi di stadio (fatto)**: cinque nodi-atomo nominati coi **verbi di Norman**
  — `perceive` (i1), `interpret` (i2), `specify` (o2), `perform` (o3), `compare` (i3) —
  coerenti con `goal`/`plan` già nominati per stadio. **o1 non è atomizzato**: sottile, e
  i suoi esempi vivono già nel runtime-macchina e nel `plan`-sviluppo (nota in `output`).
  `input`/`output` ridotti a **note-struttura** (Strukturzettel): tengono le tensioni tra
  stadi (specchio, cicli annidati, due sorgenti di i1↔due modi di i3, conflitto
  Zettelkasten/Karpathy) e linkano agli atomi; `action-cycle` resta il nodo-modello. I tre
  specchi (o3↔i1, o2↔i2, o1↔i3) materializzati in `processing-layers` come i tre livelli,
  con solo o2↔i2 attivo (il deck). `interpretations/` = i2 per identità corretto in
  `project-structure` e `output`. Audit: 45 nodi, 0 link rotti.
- **I tre specchi sono i tre livelli**: o3↔i1 (viscerale), o2↔i2 (behavioral), o1↔i3
  (riflessivo). Si sviluppano in `processing-layers` (che già accoppia gli stadi per
  livello), non negli atomi. Solo o2↔i2 ha oggi uno scopo attivo (il deck reale).
- **`interpretations/` = i2** (identità: il nome dice _interpret_); o2 è la **lettura
  speculare** della stessa superficie, non una seconda etichetta sulla cartella.
- **KB ≠ strato riflessivo (appiattimento corretto, fatto)**: il canone confondeva due
  framework di Norman. «KB = riflessivo» è lecito nel frame dei tre livelli (_Emotional
  Design_); ma la KB è anche la **system image**, _trasversale_ — non uno dei tre
  livelli, ne è il substrato (i1 la alimenta, o2 ne attinge per scendere al viscerale).
  Disambiguato in `processing-layers` (8, 30, 46-47), `knowledge-base` e
  `cognitive-artifact-design`, con `system-image` come **ancora** esplicita del
  «trasversale» (e i backlink aggiunti dove mancavano).
- **Porte svuotate + gradiente di cardinalità (fatto)**: le porte-stadio sono scese
  dentro la cartella come **indice interno omonimo** (`perceptions/perceptions.md`, ecc.),
  thin; il canone vive negli atomi. `kb.md`/`tools.md` restano in root come **cataloghi
  trasversali** (la collisione `kb/index.md` e la copertura di `.claude/skills/` sono
  sintomi della trasversalità), i register (`map.md`/`sources.md`) perché puntano fuori.
  Il razionale è il **gradiente di cardinalità**: unità al polo Goal (file in root),
  molteplicità al polo Mondo (cartelle). Tre specie di file-root + collezioni-stadio in
  cartella, formalizzato in `project-structure`; allineati README/CLAUDE/AGENTS, il runbook
  o3 e la sorgente del deck (ri-derivato). **Propagazione conclusa**: i quattro adottanti
  hanno revisionato l'intervallo `3b91094..9c45620` e avanzato il marker a `9c45620`;
  commit locali comunicati: `nixos` `f252e35`, `economia` `ad94568`, `salute` `a58c4b9`.
  Il runbook o3, esaurito, è rimosso dalla collezione attiva; la storia resta in Git.
- **System image visiva → cluster di presentazione (pianificato, sessione
  2026-06-15; ridefinito 2026-06-17)**: il task singolo si è allargato in tre
  fili pianificati in `plan.md`, in quest'ordine d'esecuzione (il disaccoppiamento
  adottante↔metodo «dichiara e taci», primo dei fili pianificati, è chiuso e
  rimosso: la storia resta in Git).
  - **Verifica dei cicli annidati: 16 celle + mappa-sorgente (gate CHIUSO, ratificato
    a freddo 2026-06-21)**: matrice riempita in dogfooding sulla sola colonna `method`
    (16 celle: **11 S, 4 D, 1 vuoto, 0 F** dopo che il Goal-dev è risalito da D a S,
    articolato nel nodo `development-goal`); gli adottanti restano al loro protocollo.
    **Esito (a)**: l'annidamento **regge** — due cicli genuini, zero forzati, cucitura
    Mondo-dev→macchina-runtime reale. Il verdetto sano, dopo la rilettura a freddo,
    **non è «due cicli pieni» ma «due cicli genuini con l'interno runtime nascente»**:
    la prima stesura sottostimava il runtime, il ribaltamento "a caldo" lo
    sovrastimava. **Call A — ribaltata**: il deck `interpretations/metodo-in-sintesi.md`
    è **i2/o2-dev** (sintesi del metodo), non runtime — l'indice `interpretations.md`
    già lo classificava così, contro lo stato reale della matrice; il vero i2/o2-runtime
    è l'**osservatorio** (`interpretations/baricentro-kb-adottanti.md`, prima istanza),
    genuinamente nascente (D perché una sola lettura, non in deriva). **Call B —
    confermata e ora suffragata**: l'arco top-down (o1-runtime) è il vero buco, ma è
    **scoccato end-to-end una volta** (prescrizione baricentro → `method-review` →
    recepimento di tutti gli adottanti); resta da costruire il **protocollo** d'audit
    periodico. **Esito (b)**: mappa-sorgente dei 16 prodotta e ri-sorgentata a freddo
    (i2-dev→deck; i2/o2-runtime→osservatorio). **Ricaduta sul cluster**: la
    rappresentazione a **due cicli** è giustificata, ma la home va disegnata
    sull'interno **nascente** (osservatorio come i2/o2-runtime, runtime-o1 muted, deck
    come i2-dev). **Conseguenza di canone: chiusa.** La riassegnazione del deck al
    runtime è **annullata** (era l'errore a caldo); la revisione di «non orchestra»
    (call B) è **incisa nel README** dalla chirurgia del 2026-06-21, con pari dignità
    del top-down runtime distinta dal micromanagement della coda adottante (cfr.
    `cognitive-artifact-design`, `method-development`).
  - **Strato di presentazione trasversale, deck→view (chiuso 2026-06-21)**: il nodo
    `deck` è scisso in **`view`**, motore trasversale a istanze multiple; la macchina
    è consolidata in root con `assets/` (CSS/token/primitivi condivisi) e `views/`
    (HTML generati e versionati). `interpretations/`, `tasks/`, `plan.md` e
    `verdict.md` restano sorgenti pure. Le tre viste attive sono
    `views/interpretations.html`, `views/tasks.html` e `views/verdict.html`, tutte
    apribili via `file://` e rigenerate da `tools/build-presentation.sh`.
  - **System image visiva, la home (chiusa 2026-06-21)**: `index.html` è l'atrio
    visivo, statico e offline, generato da `tools/build-system-image.sh`. Legge il
    polo Goal e il polo World dal README canonico, Plan da `plan.md`, e apre le tre
    view generate (`tasks`, `verdict`, `interpretations`). Il ciclo resta completo:
    Plan/Specify/Compare/Interpret sono navigabili; Perform e Perceive sono visibili,
    attenuati e senza destinazione. La home non è una seconda fonte: è una vista
    derivata e rigenerabile, come il resto dello strato `view`.
  - **Guardrail non negoziabile, su tutto il cluster: vista derivata, mai seconda
    fonte** — ogni vista si genera da sorgenti, anche il polo World.
  - **Orizzonte deliberatamente fuori**: i task come slide navigabili
    (`views/tasks.html`); una finestra-terminale per dialogare col modello, che
    **rompe l'invariante `file://`** (richiede backend servito) e sarà classe e
    nodo a sé.

**Fili parcheggiati** (gli atomi di stadio sono fatti; i **due-cicli** non sono più del
tutto parcheggiati — il nodo `nested-cycles` e il gate di verifica li stanno
esplicitando, e i fili sotto si scioglieranno man mano): la colonna di `plan` per
classificare i task su due assi ortogonali —
ciclo (sviluppo/runtime) × natura (metodologico/merito), stessa lista; l'omologia
esplicita tools=o3-sviluppo / scripts=o3-runtime / skill=prescrizioni narrative;
l'eventuale uniformità totale degli indici (tutti in-cartella) col suo costo (rinomina
del nodo `index`, split del catalogo `tools`).

## Tipologia-contenuto della KB e prima azione top-down su un adottante (salute)

Filo aperto 2026-06-20. Origine: la domanda «la KB è la system image dell'artefatto
_o_ una rappresentazione del mondo?», mal posta nel verbo (system image = **funzione**,
il canale tra agenti; rappresentazione = **contenuto**, cosa denota: assi ortogonali,
non alternativa). Guardando il secondo asse sui quattro adottanti — letti i cataloghi
`kb/` via `world/`, con campione verificato per repo — emerge che **il contenuto della
KB non è omogeneo: tassella i poli del ciclo**. Tre regioni: **ought** (Goal — concetti,
valori), **is** (Mondo runtime — la realtà del dominio), **macchina** (Mondo-dev — com'è
fatto l'artefatto). Due tensioni oneste, tenute esplicite non lisciate: la macchina si
sdoppia in _struttura_ (Mondo-dev) vs _repertorio d'atto_ (contenuto o3); e le
sorgenti-come-nodi sono un'anomalia (fonti che dovrebbero vivere nel register/`world`).
Ogni repo ha un **baricentro**: `economia`=is, `nixos`=macchina/atto, `bi`=span M↔A (il
più largo, ed è quello che esegue meglio), `salute`=ought. **Il baricentro è una
diagnosi**: un ciclo calcola uno scarto solo con _entrambi_ i poli (un is contro cui
misurare un ought); una KB tutta-ought non ha su cosa mordere.

Materializzato in due artefatti, distinti per stadio. **Osservazione (i2-runtime)**:
`interpretations/baricentro-kb-adottanti.md` (`bozza`) — ed è la **prima istanza
concreta dell'osservatorio cross-repo** che la rilettura a freddo del gate cicli
annidati segnava come mancante (cfr. il filo del gate, punto «il vero runtime è
l'osservatorio sugli adottanti»). **Generalizzazione (nodo)**: `kb/kb-content-typology.md`
(`bozza`) — riempie un buco reale (il canone trattava il contenuto KB come omogeneo),
connesso a `knowledge-base`, `system-image`, `nested-cycles`, `goal`, `world`. Resta
`bozza` per lo stesso caveat della matrice: i quattro repo li abbiamo plasmati col
metodo, il test esterno è un repo nato senza.

**Dalla diagnosi alla prescrizione, per `salute`.** Il caso peggiore è anche il più
istruttivo. `salute` ha il baricentro tutto-ought; l'is del corpo e l'arco d'azione
affamati; l'**aneurisma** dell'aorta ascendente è il caso più netto di segnale
**catturato (i1) ma mai interpretato (i2)** — vive come riga nella cronologia di
`storia-clinica`, senza un nodo, mentre la `sindrome-vasovagale` (allerta meno acuta)
ha un nodo completo. La diagnosi non si è fermata all'osservazione: ha prodotto una
**prescription** (o3-runtime), `riequilibrio-baricentro-kb` (poi chiusa, vedi sotto) — la forma
canonica con cui `method` agisce sul proprio Mondo runtime. Prescrive le linee guida nel
proprio lessico (classifica il catalogo per polo; riordina il `plan` mettendo prima is e
azione; parcheggia, non cancella, l'ought sovrappeso; promuovi a nodo i segnali catturati
ma non interpretati; controlla le sorgenti-come-nodi), con touchpoint per `salute` come
indizi da verificare in loco. L'**ultimo miglio** — quali task, quali nodi, quali
appuntamenti — lo esegue il `method-review` di `salute` contro lo stato reale: `method`
prescrive, l'adottante compie l'atto, senza che la mano del metodo entri nel runtime
altrui.

**Perché conta.** È la **prima istanza o3-runtime attiva** in `prescriptions/` (prima
vuota) e la **prima volta che l'arco top-down del runtime scocca** per davvero: evidenza
viva per la call B del gate (l'esecuzione top-down ha pari dignità della valutazione
bottom-up) e corpo a ciò che il buco runtime-o1 segnalava. Conferma la divisione del
lavoro o3 — `method` prescrive fino ai propri concetti, l'adottante personalizza
l'ultimo miglio.

**Ritorno (2026-06-20).** `salute` ha recepito e applicato la prescrizione al proprio
`method-review` (marker → `53968e8`, aligned). La diagnosi del baricentro è stata
**confermata contro controlli falsificabili** — arco d'azione vuoto, aneurisma senza
nodo, follow-up vascolare verificato non programmato via `gog` — non per ragionamento
accomodante: è la forma forte della conferma (il contrario della cella che non regge,
come il deck in deriva). Correzioni reali: promosso il nodo `aneurisma-aorta-ascendente`
(il segnale catturato finalmente interpretato), `plan` riordinato con l'ought sospeso,
arco d'azione costruito (prep incontri + canovaccio per l'appuntamento del 2/7, dove
l'impegnativa cardiologica/vascolare risulta da chiedere). Con ciò il **ciclo runtime si
chiude per intero** lungo il canale canonico — i2→i3→o3→adottante→i1 — non solo scocca:
prima chiusura completa dell'arco top-down, evidenza forte per la call B della chirurgia
dei giganti (poi chiusa il 2026-06-21). Il nodo
`kb-content-typology` ha **retto contro lo stato reale**: validazione **parziale**,
perché `salute` è plasmato dal metodo — il test esterno vero resta un repo nato senza.
La prescrizione è ora **recepita da tutti** e **chiusa** (2026-06-21, rimossa da
`prescriptions/`): `salute` l'ha eseguita, `economia`/`nixos`/`bi` l'hanno valutata
«non applicabile» al proprio `method-review` (baricentro già bilanciato — `is`,
`macchina/atto`, span `M↔A`) — e un «non applicabile» è anch'esso recepimento. Il
concetto resta nel nodo `kb-content-typology`; la ricetta riapparirà come o3 solo se
un nuovo adottante mostrerà uno squilibrio. Raffinatura emersa dal basso, foldata nel
nodo: il polo macchina è legittimamente assente quando la macchina dell'artefatto è il
`method` condiviso, gemella simmetrica dell'esenzione-ought di `nixos`.

## La membrana `method/` afforda scrittura: agisci attraverso, ratifica in `method`

Filo aperto 2026-06-23, emerso dal basso da `bi`. Risolvendo un problema concreto di
filing back — rendere `coverage` un gate bloccante per `/commit` (`coverage --check`,
exit non-zero se uno script non ha nodo) — l'agente in `bi` ha documentato la
generalizzazione modificando il nodo canonico `kb-tools`, che `bi` vede **via symlink**
`method/`. Si è poi accorto che la modifica **non compariva nel diff del proprio commit**,
ha indagato e ha chiesto: il file non è di `bi`, è il nodo in `method`, raggiunto in
scrittura attraverso la membrana. Cattura i1 in
`perceptions/modifica-di-canone-nata-in-un-adottante.md`.

**La riformulazione (i2).** Il canone descriveva il canale col suo **uso inteso** — gli
adottanti «leggono i nodi» — non con la sua **affordance**: il symlink è read-write, e
afforda la scrittura. Canone che _significa_ lettura, symlink che _offre_ scrittura: il
gap è quello che `affordance-signifier` già nomina, e la sorpresa «non compare nel mio
diff» ne è la firma. **Non è l'agente ad aver sbagliato: è il modello ad aver descritto
la membrana col suo uso inteso invece che con la sua affordance.** Corretto in `world.md`
(«Il Mondo del metodo»): la membrana afforda scrittura, dichiarata la cucitura.

**Dove la perdita si concentra (claim falsificabile).** Non è accaduto su un nodo di puro
concetto, ma su `kb-tools`, che ha una sezione **«Applicazione nei progetti adottanti»**,
per-repo: è insieme canone _e_ superficie di documentazione di uno strumento che `bi`
stava estendendo. Quando l'oggetto da stabilizzare in locale è documentato in un nodo
condiviso, **stabilizzazione locale e modifica del canone collassano nello stesso atto**.
La perdita è dunque **strutturale, non accidentale**, e si addensa sui nodi-strumento con
sezioni per-adottante. Falsificabile: se ricapita, dovrebbe ricapitare lì.

**La disciplina (i3).** Non un'anomalia da vietare: il riflesso i1/o3 è _on-demand_
(`world`), l'atto nel Mondo è primario. Quindi il write-through è la **membrana che
funziona**, e l'agente che si ferma e chiede è il trigger «richiede revisione» che scatta.

> **Agisci attraverso la membrana, ratifica in `method`.** Un agente che, risolvendo un
> problema in un adottante, modifica un nodo di canone via symlink compie un atto runtime
> legittimo: prosegue coi propri commit locali, ma _non committa l'edit di canone_ — lo
> segnala. `method` lo back-filla come perception e lo fa passare per i2/i3; solo allora
> l'edit diventa canone-di-record. **L'orfano non-committato nel working tree di `method`
> è la cucitura che funziona, non che fallisce.**

Tre precisazioni, pesate prima di incidere: (a) la disciplina **benedice** il
write-through come percorso bottom-up di prima classe — il gate di ratifica _è_ la
disciplina, non una toppa a una perdita; (b) la mossa dell'adottante è una sola —
_accorgersi e non committare l'edit di canone_; l'i1 è di `method` perché entra dalla sua
membrana runtime, e `method` ratifica; (c) il gate trattiene **solo il commit del nodo di
canone in `method`**, non i commit locali dell'adottante (l'implementazione di
`coverage --check` nei file di `bi` è il suo runtime, e prosegue).

**Collocazione nel ciclo.** È la **gamba bottom-up** del ciclo runtime — distinta da
`runtime-o1`, che è il buco _top-down_ (l'audit periodico verso gli adottanti). Finora il
verdetto descriveva quella gamba debolmente («un adottante solleva un segnale»), senza
meccanismo; l'evento le dà un **meccanismo concreto** — il write-through della membrana —
ed è la cucitura runtime→dev che scocca _dal basso_ (un atto nel Mondo runtime scrive sul
Mondo-dev). Arricchisce `nested-cycles`, non `runtime-o1`. È il primo arco bottom-up
runtime→dev che attraversa il symlink, gemello del top-down già scoccato una volta (il
_baricentro_ su `salute`).

**Stato.** La riga `kb-tools` è **ratificata come generalizzata** — il `--check` portabile
è scritto come tale ed è l'**oggetto-prova** della cucitura: ora è canone-di-record,
committabile. Il **nodo nuovo è tenuto in riserva**: un solo episodio, non si inventa
struttura prima dell'evidenza — la disciplina vive in questo filo e in `world.md` finché
un secondo write-through non chieda un atomo proprio.

---

## I quattro significanti di `Dip.`: la prontezza ha più di due stati

Pensare le dipendenze dei task solo come task↔task (`#n`) è troppo povero per
pianificare: appiattisce su «dipende / non dipende» situazioni che chiedono risposte
opposte. La `Dip.` di `plan.md` risponde ora a una domanda più fine — il task è pronto,
e se no _di chi è la mossa_ che lo sblocca — con quattro significanti: `—` (pronto),
`#n` (mossa nostra ma sequenziata), `world` (mossa altrui: si attende il mondo), `|`
(mossa nostra ma trattenuta deliberatamente). La linea di faglia è tra `world` e `|`:
con `world` il muro è fuori e non tocca a noi; con `|` il muro lo alziamo noi — per
lasciar maturare una negoziazione o per una valutazione a freddo.

Questo raffina e corregge il primo passo grezzo arrivato dall'operatività (`f929f7e`,
dove `world` assorbiva anche la pausa tattica e il differimento deciso da noi finiva in
`## Scadenze` lasciando il task `—`). Un task che teniamo deliberatamente sospeso non è
pronto: marcarlo `—` lo farebbe raccomandare come prossima mossa, che è l'errore. Ora
porta `|`, resta aperto e sorvegliato, ma non viene preso in carico. La data segue **chi
possiede l'orologio**: esogena (un atto altrui, una scadenza naturale, un termine
imposto) → `## Scadenze`, che muove la priorità avvicinandosi; autoimposta (la condizione
di risveglio di una pausa) → la riga di legenda del `|`, perché è parte della pausa, non
una pressione esterna. La forma sintetica regge tre livelli: significante in tabella,
chiosa in legenda (`world [a]`, `| [b]`), dettaglio nel file `tasks/`.

Il caso che ha forzato la distinzione è il **monitoraggio**: un task che non dipende da
un altro task ma dal tempo e da una condizione che evolve — il boot dei server dopo lo
switch al kernel LTS in `nixos` (`world`, chiuso in `c36c141`), l'autovalutazione delle
sessioni di meditazione in `salute` (`|` con risveglio autoimposto). Segnale sorto
operando su `economia` e giudicato lì generalizzabile; cattura i1 in
`perceptions/dipendenze-task-oltre-il-task-task.md`, recepimento i3 in `kb/plan.md`.

Coda risolta: la pausa tattica a granularità di **batch** (segnale da `salute`,
`perceptions/pausa-tattica-a-granularita-di-batch.md`) non richiede un significante
nuovo. Un gruppo di task trattenuti per la stessa ragione condivide una sola chiave
di legenda (`| [a]` su più righe); un fronte parcheggiato grande può raccogliersi
in una sezione di holding (come `## Sospesi` in `salute`), adattamento di dominio,
non variante del canone. Il `|` resta per-riga.
