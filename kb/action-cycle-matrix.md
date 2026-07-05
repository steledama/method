---
stato: bozza
---

# Action cycle matrix

Strumento di verifica sul campo della teoria del ciclo di azione: applica gli otto elementi del ciclo — sei atti più due poli, cfr. `action-cycle` — a ciascuno dei cinque artefatti (`nixos`, `bi`, `economia`, `salute` e `metodo` stesso) per mettere alla prova l'ipotesi della simmetria invece di darla per scontata. Una seconda passata apre l'**asse annidamento** (dev/runtime, `nested-cycles`) — le otto righe diventano sedici — per la sola colonna `metodo` in dogfooding, mettendo alla prova l'ipotesi dei due cicli prima di costruirne la rappresentazione. Non è una mappa che illustra la teoria: è un test che può falsificarla. Nasce dalla domanda aperta — la simmetria a otto elementi è una struttura reale che affina lo strumento, o una forzatura elegante che piega la realtà all'esigenza teorica?

> **IL RISCHIO È LA COMPLICITÀ CON SÉ STESSI.** Una matrice che parte cercando simmetria la trova sempre: la ragione motivata fabbrica corrispondenze su misura. Questo strumento vale solo se ogni casella riceve un verdetto onesto con una riga di giustificazione, e solo se «forzato» è un esito _gradito_, non un fallimento da smussare. Se a fine verifica le caselle forzate o vuote restano molte, l'ipotesi della simmetria è sbagliata e va abbandonata, non difesa. Lo strumento serve a uccidere la teoria se lo merita, non a incoronarla.

## Scala di verdetto

- **S — solido**: l'elemento esiste nell'artefatto, ben formato e riconoscibile senza forzature.
- **D — debole**: esiste ma è sotto-sviluppato, implicito o sparso.
- **F — forzato**: l'accostamento regge solo piegando la realtà alla teoria; è il verdetto che falsifica.
- **? — da verificare**: non ancora ispezionato sul campo nel repo. Non un giudizio, un debito.
- **vuoto — legittimamente assente**: l'elemento _non esiste_ per quell'artefatto e la sua assenza è un verdetto onesto — per design o per cucitura dell'annidamento — non un debito da colmare come il `?`.

## La matrice — primo passaggio

Riempito solo dove esiste grounding diretto (`output.md`, `goal.md`, `world.md`, ispezione di `i2/`); il resto è marcato `?` per onestà, non per cautela.

- **Goal (polo)** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Plan · o1** — `nixos`: S; `bi`: S; `economia`: S; `salute`: D; `metodo`: S
- **Specify · o2** — `nixos`: D; `bi`: S; `economia`: D; `salute`: D; `metodo`: D
- **Perform · o3** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Perceive · i1** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Interpret · i2** — `nixos`: D; `bi`: S; `economia`: D; `salute`: D; `metodo`: D
- **Compare · i3** — `nixos`: D; `bi`: S; `economia`: S; `salute`: D; `metodo`: S
- **Mondo (polo)** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S

Conteggio: 29 S, 11 D, 0 ?, 0 F (dopo aver riempito i2/i3 — vedi sotto).

## Cosa dice il primo passaggio (lettura spietata)

Il conteggio sembra confortante. Non lo è, e leggerlo come una vittoria sarebbe esattamente la complicità contro cui avverte il riquadro.

- **Venti dei ventinove S sono quasi tautologici.** Le quattro righe-bordo — Goal, Perform (o3), Perceive (i1), Mondo — sono solide _perché le abbiamo definite noi_ per ciascun artefatto in `goal.md` e `world.md`. Un elemento che combacia perché l'abbiamo ritagliato su misura non è prova della simmetria: è la simmetria messa lì a mano. Vanno scontate.
- **Tolti i bordi, l'interno è in larga parte debole.** Plan (4 S, 1 D), Specify/o2 (1 S, 4 D), Interpret/i2 (1 S, 4 D), Compare/i3 (3 S, 2 D). i2 e i3, prima vuote, sono ora riempite mappando su artefatti che _esistono davvero_ — la sintesi (i2) e i fili di verdetto (i3) — non per relabeling: è teoria che regge il test sull'arco di input. Ma il risultato non è un trionfo di simmetria, è una diagnosi: l'interno è debole, e la debolezza è la stessa ovunque — la rappresentazione (o2/i2) e la disciplina del verdetto (i3).
- **Lo zero forzati ha ora un significato diverso.** Riempite i2 e i3, nessuna casella ha richiesto di piegare la realtà: il modello ha mappato su artefatti reali (sintesi, fili `i3/`). È un risultato — il ciclo è descrittivamente adeguato a questa classe di repo — ma resta provvisorio per una ragione circolare: questi repo li abbiamo già plasmati col metodo. Il vero test esterno è un repo costruito _senza_ il metodo: il ciclo vi mapperebbe ancora? Finché non lo proviamo, lo zero-forzati è incoraggiante, non conclusivo. Il primo `F` onesto, quando arriverà, varrà più di tutti gli `S`.
- **`o2` è la colonna-spia.** Debole in quattro artefatti su cinque (solo `bi` con Reveal.js la salva). È lo strato di rappresentazione/decisione: la conferma che il collo di bottiglia di tutti gli artefatti è la vista che dovrebbe generare azione. È la stessa diagnosi della stasi di `salute`, l'unico artefatto debole su _entrambi_ o1 e o2 — quasi tutto l'arco di output assente, eppure o3 «medio»: agisce per intuizione senza che l'artefatto lo sostenga, che è il profilo del loop a vuoto.
- **`metodo` non è stato segnato tutto-S di proposito.** Un artefatto che dà il massimo a sé stesso si sta adulando. Anche così sta in alto, e proprio per questo merita la revisione esterna più dura, non la più indulgente.

**La matrice sopra collassa l'annidamento.** Le otto righe trattano ogni artefatto come se avesse un solo ciclo d'azione, ma sono due, annidati (`nested-cycles`): è la seconda delle quattro dimensioni ortogonali di `action-cycle`, quella la cui omissione fa «sparire» un cappio intero. La sezione che segue apre quell'asse per la **sola colonna `metodo`** (dogfooding): le otto righe diventano sedici, otto per ciclo. Gli adottanti restano al protocollo della prima slide (cfr. «Protocollo di riempimento»): la loro verifica dell'annidamento per dominio non è oggetto di questa passata.

## L'asse annidamento (dev/runtime): le 16 celle di `metodo`

I due cicli si distinguono unicamente per _cosa sia il loro Mondo_ in fondo (`nested-cycles`): il ciclo di **sviluppo** ha per Mondo l'artefatto stesso; il ciclo **runtime** ha per Mondo i progetti adottanti. La verifica non affianca due blocchi da otto: marca la **cucitura** dove il Mondo-dev — l'artefatto risultante — diventa la macchina che il runtime muove.

### Ciclo di sviluppo (Mondo = l'artefatto stesso)

- **Goal (polo) — S**: il polo è ora articolato. Il contenuto _dev-specifico_ — la posizione auspicata dello sviluppo lungo dimensioni comuni a tutti gli artefatti (attrito/golfi, autonomia dell'umano, temporalità del loop) — è formulato in `development-goal`, che scioglie lo split provvisorio col Goal runtime (al runtime gli obiettivi costitutivi del dominio, al dev la forma auspicata del ciclo). Da D a S: il polo è ben formato e riconoscibile, non più mescolato; resta `bozza` come il resto, perché le dimensioni sono candidate finché un repo esterno non le mette alla prova.
- **Plan · o1 — S**: `o1/plan.md`, qualificato esplicitamente o1-sviluppo: task aperti, prioritizzati, con dipendenze, in forma-macchina vicino alla KB.
- **Specify · o2 — S**: `o2/` dà la specifica concreta dei task elencati in `plan`, pronta a essere affinata e poi eseguita — o corretta quando gli obiettivi interni e le relazioni con gli altri task vengono definiti meglio.
- **Perform · o3 — S**: il commit / l'edit ai nodi `kb/` e gli esecutori in `o3/` sono l'atto versionato sull'artefatto; è l'atto più reale del ciclo e modifica il Mondo-dev da cui passa la cucitura, ma non coincide con la macchina che il runtime esegue.
- **Perceive · i1 — S**: `o3/kb_tools.py` via `/kb-review` cattura il segnale sull'artefatto — link rotti, orfani, copertura del catalogo, audit «45 nodi, 0 link rotti» — valenza-neutro.
- **Interpret · i2 — D**: `i2/metodo-in-sintesi.md` è l'auto-interpretazione dello sviluppo — la sintesi illustrata del metodo, dei nodi e dell'architettura dell'artefatto: **i2-dev** (e o2-dev quando lo si usa come vista di decisione sul metodo). La rilettura a freddo del gate ha **ribaltato la riassegnazione "a caldo" al runtime**: la sintesi i2 rilegge il Mondo-dev (i nodi del metodo), non i quattro domini, quindi è dev, non runtime — e l'indice `i2/interpretations.md` già lo classifica così. D e non S perché la sua derivazione non è disciplinata (è `bozza`, e le viste derivate driftano se non ri-generate: è il presidio di `cognitive-fidelity`).
- **Compare · i3 — S**: i fili in `i3/`, qualificati esplicitamente i3-sviluppo; la migrazione a stato-per-filo aggiornato in place ne è la prima istanza canonica reale.
- **Mondo (polo) — S**: l'artefatto stesso, dichiarato Mondo di sviluppo nel README. **È anche la macchina del ciclo runtime — qui passa la cucitura.**

### Ciclo runtime (Mondo = i progetti adottanti)

- **Goal (polo) — S**: il ciclo runtime ha obiettivi costitutivi reali, distribuiti nell'artefatto più che raccolti in un goal-artefatto unico — portabilità, indipendenza dal modello, adattabilità a domini molto diversi (e quindi flessibilità), meccanismi di autocorrezione, rigore delle fonti, il pavimento teorico su cui il metodo poggia. Il polo è ben costituito ai bordi (un polo si costituisce, non si esegue); per `method` è più ricco del Goal-dev. La ripartizione tra Goal-runtime e Goal-dev è ora sciolta in `development-goal`: al runtime gli obiettivi costitutivi del dominio (questi), al dev la posizione auspicata lungo le dimensioni comuni.
- **Plan · o1 — vuoto (gap)**: la pianificazione **top-down** — come gli artefatti adottanti dovrebbero diventare — non esiste. A differenza degli altri vuoti non è legittimo-per-design: è l'arco che il principio «`metodo` non orchestra task sui adottanti» ha finora negato, e che il gate trova **da costruire** (l'esecuzione top-down ha pari dignità della valutazione bottom-up; la sua assenza è sovra-esposizione del dal-basso). È il vero buco del ciclo runtime.
- **Specify · o2 — D**: la superficie o2-runtime è l'**osservatorio sugli adottanti** — la vista comparativa cross-repo che orienta le decisioni sul canone. Esiste come **prima istanza** (`i2/baricentro-kb-adottanti.md`, che ha già orientato una decisione reale: la prescrizione baricentro), ma non è ancora una superficie stabile e mantenuta che copra i quattro domini su tutti gli archi: nascente, quindi D. (Non `metodo-in-sintesi.md`, che è i2/o2-**dev**.)
- **Perform · o3 — S**: `o3/` è il canale o3 reale e canonizzato in `project-structure`; runbook reali vi sono transitati (il runbook d'atrio). Oggi senza prescrizioni attive, ma **ha già funzionato**: S per capacità reale, non per pienezza istantanea.
- **Perceive · i1 — S**: `i1/` è il canale i1 reale, con un segnale catturato (`adottanti-pianificano-il-canone-in-plan.md`), valenza-neutro. Ha già funzionato: stesso metro di o3.
- **Interpret · i2 — D**: l'interpretazione del Mondo-runtime è l'**osservatorio** — la rilettura comparativa dei quattro adottanti. Ha la sua **prima istanza** (`i2/baricentro-kb-adottanti.md`, i2-runtime: legge i cataloghi `kb/` dei domini, non i nodi del metodo) più i ledger `method-review` come materiale grezzo. D perché è una sola lettura, non un osservatorio stabile e periodico. La call A "a caldo" (`metodo-in-sintesi.md` è i2-runtime) è **ribaltata**: la sintesi i2 del metodo interpreta il metodo, non i domini — la deriva non esisteva, era un'assegnazione sbagliata. Segnare S qui sarebbe la simmetria-compiacente che la matrice esiste per prevenire.
- **Compare · i3 — D**: la valutazione-osservatorio — confrontare la fotografia dei quattro domini contro gli obiettivi-runtime — è inquadrata da `adopter-comparison` (la lente) e vive in parte nei fili adottanti di `i3/`, ma non è materializzata come verdetto-runtime a sé. Presente, sparsa.
- **Mondo (polo) — S**: i progetti adottanti (`nixos`, `bi`, `economia`, `salute`), dichiarati Mondo runtime nel README; reali, distinti e raggiunti via symlink.

Conteggio `metodo`, 16 celle: **11 S, 4 D, 1 vuoto, 0 F** (dev: 7 S, 1 D; runtime: 4 S, 3 D, 1 vuoto). Zero forzati, ma il dato che parla è la _forma_: le quattro D segnano gli archi immaturi — incluso l'**interno runtime**, che la rilettura a freddo ha ricondotto da pieno (la sintesi i2 del metodo) a nascente (l'osservatorio, una sola istanza); l'unico vuoto è il **vero gap** runtime-o1 (il protocollo top-down). Il Goal-dev è risalito da D a S una volta articolato in `development-goal`; resta D nel dev solo `metodo-in-sintesi.md` (i2-dev), dove la disciplina di derivazione è il limite.

### I due cicli, la cucitura e le asimmetrie reali

Il riempimento, **riletto a freddo**, rivede sia la prima lettura sia il ribaltamento "a caldo". Il ciclo runtime di `metodo` è un ciclo genuino con entrambi gli archi, ma il suo **interno è nascente**, non pieno. Le due letture:

- **Call A — ribaltata.** `i2/metodo-in-sintesi.md` non è i2/o2 del runtime: è **i2/o2-dev**, la sintesi che rilegge il Mondo-dev (i nodi del metodo). L'assegnazione al runtime era la cella che la simmetria aveva fabbricato; l'indice `i2/interpretations.md`, contro lo stato reale, già lo classifica i2-dev. Il vero i2/o2-runtime è l'**osservatorio sugli adottanti** (`i2/baricentro-kb-adottanti.md`, prima istanza), genuinamente nascente: D non perché in deriva, ma perché è una sola lettura, non una superficie stabile.
- **Call B — confermata.** L'**arco top-down del runtime** (o1) è il vero buco — non un vuoto-per-design ma un vuoto-gap, negato finora dal principio «`metodo` non orchestra task sui adottanti». L'arco è ora **scoccato end-to-end una volta** (prescrizione baricentro → `method-review` degli adottanti → recepimento), prova che è percorribile; ma il **protocollo** o1-runtime — l'audit periodico, non il micromanagement delle code — resta da costruire. Quindi o1 resta vuoto-gap.

Resta vera la **cucitura di output** (la canonica di `nested-cycles`): il Mondo-dev — l'artefatto — _è_ la macchina del runtime. Ciò che lo sviluppo costruisce è esattamente ciò che gli adottanti eseguono via symlink; l'o3-runtime (`o3/`) propaga le modifiche a quella macchina. Ma non è l'unico legame: i due cicli condividono il polo Goal (obiettivi in larga parte runtime) e si parlano in entrambi i versi.

Le asimmetrie reali, a freddo: **dev-i2 è la sintesi illustrata del metodo** (presente ma a derivazione non disciplinata, D), mentre **l'i2/o2-runtime è l'osservatorio nascente** (una istanza, D); e soprattutto **runtime-o1 il buco** — l'arco top-down con la macchina d'osservazione ancora da costruire.

### Verdetto-gate

L'annidamento a 16 celle **regge per `metodo`** — questo è fermo, e ratificato a freddo: non una cucitura su mezzo ciclo, ma **due cicli genuini** (11 S, 4 D, 1 vuoto, 0 F). Ma il verdetto sano **non è «due cicli pieni»**: è **«due cicli genuini, con l'interno runtime nascente/da costruire»**. La prima stesura sottostimava il runtime (membrana su interno vuoto); il ribaltamento "a caldo" lo sovrastimava (interno pieno via sintesi i2 del metodo); la rilettura a freddo lo coglie per quello che è: archi reali, interno immaturo.

- **Regge la struttura**: zero celle forzate; entrambi i cicli hanno poli costituiti e membrana fisica (o3/i1 runtime).
- **L'interno runtime è nascente, non pieno**: l'i2/o2-runtime è l'osservatorio a una sola istanza (`baricentro-kb-adottanti.md`), non `metodo-in-sintesi.md` (che è i2-dev); l'i3-runtime è sparso; e **runtime-o1 è il buco** — l'arco top-down scoccato una volta ma senza protocollo d'audit.

**Conseguenza per la presentazione.** Una rappresentazione a **due cicli** resta _giustificata sul piano analitico_ (l'errore non era pensarli due), ma la home non la rende: dalla semplificazione ratificata il 2026-07-05 la home è **minimalista** — ciclo singolo, un collegamento primario per slot, pura affordance di navigazione — e la lente dev/runtime è rimandata **a valle, come filtro nelle singole viste** (tasks, plan) quando l'uso lo chiederà. La matrice a 16 celle e la scala a cinque valori restano lo strumento analitico di questo nodo, distinto dalla superficie di navigazione. La mossa di canone «rivedere "non orchestra"» (call B), suffragata da un arco scoccato per intero, è ora **incisa nel `README`** (e in `cognitive-artifact-design`, `method-development`) dalla chirurgia dei giganti: il top-down runtime ha pari dignità del bottom-up, distinto dal micromanagement della coda adottante.

### Mappa-sorgente (b)

Prodotta perché (a) regge. Per ciascuno dei 16 elementi, la sua casa nell'atrio — l'indice che i task di presentazione consumano senza inventare la geometria a mano.

Ciclo di sviluppo:

- Goal-dev → `README.md` (bussola) + `development-goal` (posizione auspicata lungo le dimensioni comuni)
- o1-dev → `o1/plan.md`
- o2-dev → `o2/`
- o3-dev → git commit / l'edit ai nodi `kb/` / esecutori in `o3/`
- i1-dev → `o3/kb_tools.py` (`/kb-review`: audit, backlink, copertura)
- i2-dev → `i2/metodo-in-sintesi.md` (sintesi del metodo; o2-dev quando è vista di decisione)
- i3-dev → fili in `i3/`
- Mondo-dev → l'artefatto stesso — **= macchina del runtime (cucitura)**

Ciclo runtime:

- Goal-runtime → `README.md` (obiettivi distribuiti: portabilità, indipendenza dal modello, adattabilità, autocorrezione, rigore fonti, pavimento teorico)
- o1-runtime → ∅ oggi — il **gap top-down** (protocollo d'audit periodico da costruire; l'arco è scoccato una volta via prescrizione, ma senza macchina d'osservazione)
- o2-runtime → `i2/baricentro-kb-adottanti.md` (osservatorio come vista-di-decisione; prima istanza, da estendere ai 4 domini)
- o3-runtime → `o3/` (runbook di propagazione)
- i1-runtime → `i1/` (segnale metodologico dell'adottante)
- i2-runtime → `i2/baricentro-kb-adottanti.md` (osservatorio: rilegge i cataloghi dei 4 domini; prima istanza nascente)
- i3-runtime → `adopter-comparison` (lente) + fili adottanti in `i3/` + ledger `method-review` (non materializzato a sé)
- Mondo-runtime → progetti adottanti: `../nixos`, `../bi`, `../economia`, `../salute`

## Protocollo di riempimento

I verdetti deboli e quelli riempiti per ragionamento si verificano sul campo, non a tavolino qui. Il luogo della verifica è la prima slide di ciascun artefatto — il suo autoritratto attraverso i sei atti e i due poli, applicati al proprio dominio: dove l'accostamento è debole o forzato, tanto meglio, costringe a guardare l'artefatto in modo analitico. `metodo` non orchestra questo lavoro nei repo adottanti (cfr. `adopter-comparison`): ogni repo riempie la propria colonna, e il verdetto risale qui come fotografia aggregata. Le righe i2/i3 sono ora riempite per ragionamento (mappano su artefatti reali); questo nodo resta `bozza` finché la verifica esterna repo-per-repo non le conferma — o le smentisce.

Connessioni:

- [action-cycle](action-cycle.md)
- [world](world.md)
- [goal](goal.md)
- [development-goal](development-goal.md)
- [output](output.md)
- [system-image](system-image.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
