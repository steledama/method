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
(Clark) sono ora sourced — cfr. il filo «I giganti ristrutturati», dove il pavimento
ontologico Hutchins+Clark è confermato e destinato a `cognitive-system`. **_Things That Make
Us Smart_** (Norman 1993) è ora integrale e **distillato (i2)** nei capitoli portanti: Cap. 2
(esperienziale vs riflessivo — sorza la naturalezza e il «KB come scaffold del modo
riflessivo»; i due-modi 1993 sono l'origine dei tre-livelli di `processing-layers`) e Cap. 6
(la cognizione distribuita di **Norman stesso**, che cita Hutchins — pavimento Hutchins+Clark+Norman,
una famiglia UCSD; più «the world remembers by being there» ↔ membrana `world`, e gli errori
condivisi come training rigenerativo). Destinazioni i3 — `cognitive-artifact`, `cognitive-system`,
`processing-layers`, `affordance-signifier` — da scrivere nella passata deliberata, non ora. La
matrice 4D del ciclo, infine, è un falsificatore
costruito sulle definizioni del metodo stesso: il suo esito «zero forzati» resta
**provvisorio finché non lo si testa su un repo nato senza il metodo**.

## I giganti ristrutturati: Engelbart come cornice di sistema (H-LAM/T)

Filo aperto 2026-06-17. Origine: accostare Karpathy a Luhmann e Norman come terzo «gigante»
era un'**asimmetria di pedigree** — sulla questione il suo contributo è un post, non una
tradizione di pensiero — anche se il suo _slot funzionale_ (il _chi mantiene_ la KB) è reale.
Il difetto era aver ancorato quello slot a una fonte troppo leggera.

**Decisione presa (2026-06-17), dopo aver letto Engelbart 1962** (_Augmenting Human Intellect_,
Sez. I/II/IV; provenienza in `sources.md`): non «tre giganti pari con Engelbart al posto di
Karpathy» (opzione a), ma **Engelbart come gigante _di sistema_** (opzione b) — più onesto,
perché Engelbart è troppo unificante per essere una gamba sola. La sua cornice **H-LAM/T**
(Human using Language, Artifacts, Methodology, in which he is Trained) _contiene_ gli altri,
non li affianca. Nuova architettura del pensiero:

- **Engelbart / H-LAM/T = la cornice di sistema**: l'umano + LLM + artefatto è _un sistema di
  augmentation_, non tre componenti giustapposti. I quattro means mappano sull'anatomia del
  metodo (Artifacts = repo/KB; Language = nodi e terminologia; Methodology = il metodo;
  Training = bootstrap/`CLAUDE.md`). L'intelligenza è **synergism** distribuito nel sistema
  accoppiato, non in un componente. E il **bootstrap** di Engelbart — «Tools Developed vs Tools
  Used» (§IV-E), il sistema che si solleva «by its own bootstraps» — è l'antenato del 1962 di
  due strutture del metodo: il **dogfooding** e i **cicli annidati** (`nested-cycles`: il Mondo
  di sviluppo diventa la macchina del runtime, con l'o3-sviluppo come atto che lo modifica;
  stessa distinzione e stesso avvertimento sulla confusione terminologica).
- **Dentro la cornice**: Luhmann dà il means _Language_ / l'unità atomica (symbol-structuring);
  Norman dà l'interfaccia col Mondo (il ciclo d'azione); la gamba di **manutenzione/
  rigenerazione** è il _Methodology/Training_ engelbartiano, di cui **Karpathy è l'istanza
  contemporanea per l'era LLM** (non un pilastro).
- **Sotto la cornice**: il pavimento _ontologico_ — perché un sistema accoppiato sia
  genuinamente cognizione — è **Hutchins/Clark** (cognizione distribuita / mente estesa),
  non Karpathy.

**Deciso vs debito.** È decisa la _cornice_ (questa è l'i3). La **chirurgia dei nodi** resta
da fare come corpo del task 7 — è un hub ad alto rischio (`action-cycle` «I tre giganti», 33
backlink), più `README`, `knowledge-base`, `karpathy-pattern` (→ istanza), un nodo nuovo per
l'H-LAM/T e il riferimento a Engelbart in `nested-cycles`. Da non riscrivere a caldo: la
fedeltà chiede un passo deliberato. **Debito Sez. III chiuso** (letta integralmente): rafforza
la decisione (b) sul testo primario, non per analogia — la cornice H-LAM/T contiene già, nel
1962, nodi atomici con link tipizzati e provenienza (il sistema di schede edge-notched di
Engelbart è un Zettelkasten ante litteram), la mossa di ingest/distillazione i1→i2 («type the
article in, tear it apart... it sits in the archives like an orange rind»), un loop di
valutazione (la review periodica man-computer) e la cooperazione collaborativa con tracciamento
delle contese (l'antenato del verdict). Sul **pavimento ontologico**: Clark è ora _sourced per
intero_ (Extended Mind + Being There letti) e la **destinazione è decisa — pavimento unico in
`cognitive-system`** (Hutchins+Clark insieme: active externalism, parità, scaffolding, 007,
mind-as-controller). Esito scomodo e prezioso di Being There: Clark apre attaccando il modello
«filing cabinet» della mente (CYC), e la risoluzione è un **criterio di progetto del KB** — è
legittimo solo come _scaffold action-oriented_ (pushmi-pullyu, descrittivo e prescrittivo), non
brain-dump passivo; coincide con la critica di Norman e va portato in `system-image`/
`cognitive-artifact-design`. **Debito di pavimento chiuso**: Hutchins (_Cognition in the Wild_, 1995) è ora sourced — lettura mirata che conferma tesi (cognizione come processo culturale/
sociale, unità di analisi oltre la pelle, il team come sistema cognitivo-computazionale),
«cognition in the wild» (vs laboratorio «in captivity»), propagazione dello stato
rappresentazionale tra media, e la sintesi del cap. 9 (non scambiare le proprietà del sistema
socioculturale per quelle della mente individuale) — il punto stesso che Clark cita. Il
pavimento Hutchins+Clark è ora **interamente sourced**: la chirurgia può promuoverlo senza
debito. La scrittura dei nodi resta la passata deliberata, non ora.

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
  2026-06-15; ridefinito 2026-06-17)**: il task singolo si è allargato in quattro
  fili pianificati in `plan.md`, in quest'ordine d'esecuzione.
  - **Disaccoppiamento adottante↔metodo «dichiara e taci» (1°)**: il dolore
    ricorrente — a ogni rename di nodo si toccano CLAUDE/README dei 4 adottanti —
    è sintomo di over-coupling. Cura: interfaccia stabile, struttura volatile.
    L'adottante dipende dal metodo _come tutto_ — una dichiarazione nel `README`
    - il symlink `method/` + il **hub** `cognitive-artifact-design` (unico nome a
      contratto di stabilità) — e **evita i link sparsi a path di nodi**. Va per
      primo perché ripulisce i riferimenti prima del rename sotto, rendendone la
      propagazione quasi nulla. Casa del principio **decisa**: sezione in
      `method-development` (il principio) + struttura README canonica in `kb/readme.md`
      (il veicolo). La sezione README canonica — comune ai 5 repo — dichiara adozione,
      symlink `method/` e i due poli Goal/World, e diventa la sorgente da cui la home
      legge i poli, **senza org-guessing dal remote** (`bi` su `tt-sviluppo`, gli altri
      su `steledama`). Gli step di onboarding nel README di `method`, che oggi
      prescrivono di hardcodare i path, vanno invertiti. Propagazione in **due round**:
      1° disaccoppiamento + README canonico, 2° rename `deck→view`. Nota dev/runtime:
      per `method` i poli World sono **due** (sviluppo = `kb/`, runtime = adottanti);
      lo schema README canonico potrà doverlo riflettere, ed è il gate sotto a deciderlo.
  - **Verifica dei cicli annidati: 16 celle + mappa-sorgente (gate eseguito; apre
    chirurgia di canone)**: matrice riempita in dogfooding sulla sola colonna
    `method` (16 celle: 10 S, 4 D, 2 vuoto, 0 F); gli adottanti restano al loro
    protocollo. **Esito (a), ribaltato in revisione collaborativa**: l'annidamento
    regge — e più della prima lettura — non come cucitura su mezzo ciclo ma come
    **due cicli genuini**, entrambi sostanzialmente popolati, zero forzati. La prima
    stesura («membrana runtime popolata, interno vuoto che collassa nel dev») era un
    **sotto-conteggio**: nasceva dal contare il deck come dev-only e dal negare l'arco
    top-down. Corretto su due punti, decisi con l'autore: **(A)** il deck
    `interpretations/` è **i2/o2-runtime**, non i2-dev — è la vetrina rivolta agli
    adottanti (oggi in deriva: interpreta i nodi del metodo, non i 4 domini → D);
    **(B)** l'arco **top-down del runtime** (o1 = come gli artefatti adottanti devono
    diventare) è il **vero buco**, negato dal principio README «`metodo` non orchestra
    task sui adottanti» — che il gate trova **da rivedere**: l'esecuzione top-down ha
    pari dignità della valutazione bottom-up, e la sua assenza è la sovra-esposizione
    del dal-basso. Asimmetrie reali (non simmetria assunta): dev-i2 vuoto vs runtime-i2
    in deriva; runtime-o1 il gap. **Esito (b)**: mappa-sorgente dei 16 prodotta.
    **Ricaduta sul cluster, ribaltata**: una rappresentazione a **due cicli** è ora
    _giustificata_ (l'errore era darla per scontata _prima_ del gate), con runtime-o1
    **muted** (il gap dichiarato), il deck come livello behavioral (o2↔i2) del runtime
    e la cucitura al polo Mondo-dev: il Mondo di sviluppo diventa macchina del runtime,
    mentre l'o3-sviluppo è l'atto che lo modifica. **Conseguenze di canone (sacrosante,
    da passata deliberata, accodate a «chirurgia dei giganti» per toccare gli hub una
    volta sola)**: riassegnare `interpretations/` da i2-dev a i2/o2-runtime (tocca
    README, `interpretations.md`, `action-cycle` §«il deck come cerniera», `processing-layers`,
    `project-structure`, `output`); rivedere «non orchestra» nel README ammettendo il
    movimento top-down; dare a `method-development` l'arco top-down runtime. Da non
    riscrivere a caldo (`cognitive-fidelity`). La presentazione (sotto) **non incide
    finché non sono ratificate**.
  - **Strato di presentazione trasversale, deck→view (3°, dip. dal gate)**: il nodo `deck`
    confonde il **motore** di presentazione e la sua **istanza**
    (`interpretations/`). Si scinde: `deck.md` → **`view.md`**, motore trasversale
    a istanze multiple (una vista per collezione), con la macchina consolidata in
    root — `assets/` (CSS/lib condivisi) e `views/` (HTML **generati**, specie
    nuova nell'atrio). `interpretations/` e `tasks/` tornano **sorgenti pure**
    (twin). L'invariante `deck` è intatto: apertura `file://` dal checkout, HTML
    generati versionati.
  - **System image visiva, la home (4°, dip. dal gate e dal 3°)**: `index.html` in
    root — l'atrio visivo, statico e offline (nessun Reveal), generato dallo stesso
    motore. Layout sul diagramma `action-cycle`: header GOAL (polo Goal del
    `README`), due colonne (o1/o2/o3 ↔ i3/i2/i1, con o3/i1 **muted** finché
    `prescriptions/`/`perceptions/` sono vuote), footer WORLD (adottanti dal polo
    World canonico del `README`, riferimenti espliciti). La rappresentazione dei due
    cicli è **decisa dal gate** (sopra), nella lettura ribaltata: **due cicli
    genuini**, non un ciclo solo. La home può mostrarli entrambi, con **runtime-o1
    muted** (il gap top-down dichiarato), il deck come livello behavioral (o2↔i2) del
    runtime e la cucitura di output al polo Mondo (footer WORLD). Subordinata però alle
    conseguenze di canone che il gate apre (riassegnazione del deck, revisione di «non
    orchestra»): la vista non incide finché non sono ratificate. Cura della stasi
    `processing-layers:53` e specchio o2↔i2 reso letterale.
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
**prescription** (o3-runtime), `prescriptions/riequilibrio-baricentro-kb.md` — la forma
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
prima chiusura completa dell'arco top-down, evidenza forte per il gate (task 1). Il nodo
`kb-content-typology` ha **retto contro lo stato reale**: validazione **parziale**,
perché `salute` è plasmato dal metodo — il test esterno vero resta un repo nato senza.
La prescrizione **resta attiva** finché `nixos`/`bi`/`economia` non si auto-valutano al
proprio `method-review` (un «non applicabile» è anch'esso recepimento). Raffinatura
emersa dal basso, foldata nel nodo: il polo macchina è legittimamente assente quando la
macchina dell'artefatto è il `method` condiviso, gemella simmetrica dell'esenzione-ought
di `nixos`.

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
