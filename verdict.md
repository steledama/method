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
`system-image`, `processing-layers`). Due debiti di fonte li tengono zoppi
sul lato fedeltà (i3): _Things That Make Us Smart_ (Norman 1993, fonte di «artefatto
cognitivo» e cognizione distribuita) è distillato solo nel Cap. 3 (in `world`), il
volume completo non è reperito; Hutchins (per `cognitive-system`) e Leontiev (per
`goal`) sono citati nei Riferimenti ma non vivono ancora in `world`. L'ingest delle
fonti mancanti è tracciato in `plan` (mente estesa,
pace-layering). La matrice 4D del ciclo, infine, è un falsificatore costruito sulle
definizioni del metodo stesso: il suo esito «zero forzati» resta **provvisorio finché
non lo si testa su un repo nato senza il metodo**.

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
primo o3 reale: `prescriptions/adozione-nuovo-atrio.md`, la ricetta per `economia`/`salute`
di questo stesso cambio. La regola del canale vive in `project-structure`.

## Rifondazione atrio↔azione: gradiente di cardinalità, atomi di stadio, system image visiva

Filo di design aperto in questa sessione; **in esecuzione** (lavoro in `plan.md`). La
**disambiguazione KB riflessivo ↔ system-image** e gli **atomi di stadio** sono fatti;
restano atrio a tre specie e system image visiva. La categoria «porta-collezione» era
**falsamente uniforme**: trattava allo stesso modo la KB (system image), gli strumenti
(macchina del ciclo di sviluppo) e gli stadi i1/i2/o3 — cose di tre specie diverse.

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

- **`plan.md` = o1-sviluppo, `verdict.md` = i3-sviluppo**, col qualificatore di ciclo.
  `action-cycle:46` già mappa Plan=o1 e Compare=i3; la frase di `project-structure:64-66`
  («plan non è o1») è imprecisa — la guardia giusta non è negare l'omologia ma
  qualificare il ciclo (o1/i3-sviluppo vs o1/i3-runtime), come tools (o3-sviluppo) vs
  prescriptions (o3-runtime).
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
- **Porte svuotate**: il contenuto comune delle porte-stadio migra negli atomi; la porta
  resta come **indice sottile dentro la cartella** che indicizza (tiene viva la cartella
  vuota in git, dichiara lo stadio). `kb.md` e `tools.md` **restano in root** come
  cataloghi _trasversali_ (la collisione `kb/index.md` e il fatto che `tools.md` copra
  anche `.claude/skills/` sono sintomi della trasversalità, non casi sfortunati); i
  register (`map.md`, `sources.md`) restano in root perché puntano fuori. Tre specie, tre
  collocazioni, ognuna con un _perché_ nel modello.
- **System image visiva** («dà il tono al progetto»): lo strato di
  rappresentazione grafica generato — oggi confinato come deck in `interpretations/` —
  sale a **componente root**, controparte visiva dell'atrio testuale (`ls`). Mostrerà il
  ciclo dell'azione di dominio «all'opera viva» (tasks da `plan`, verdetto, salute dei
  nodi). È la cura della stasi già diagnosticata (`processing-layers:53`: un o2 solo
  riflessivo non muove; serve scendere al viscerale) e lo specchio o2↔i2 reso letterale.
  **Guardrail non negoziabile: vista derivata, mai seconda fonte** — si genera da
  nodi/`plan`/`verdict`/collezioni, non ne ospita copia. `interpretations/` resta la
  collezione delle sorgenti i2; il sito generato vive in root; `build-presentation.sh`
  cresce di conseguenza.

**Fili parcheggiati** (si scioglieranno a catena quando atomi di stadio e due-cicli
saranno espliciti): la colonna di `plan` per classificare i task su due assi ortogonali —
ciclo (sviluppo/runtime) × natura (metodologico/merito), stessa lista; l'omologia
esplicita tools=o3-sviluppo / scripts=o3-runtime / skill=prescrizioni narrative;
l'eventuale uniformità totale degli indici (tutti in-cartella) col suo costo (rinomina
del nodo `index`, split del catalogo `tools`).
