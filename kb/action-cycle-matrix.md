---
data: 2026-06-09
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

Riempito solo dove esiste grounding diretto (`output.md`, `goal.md`, `world.md`, ispezione delle `interpretations/`); il resto è marcato `?` per onestà, non per cautela.

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
- **Tolti i bordi, l'interno è in larga parte debole.** Plan (4 S, 1 D), Specify/o2 (1 S, 4 D), Interpret/i2 (1 S, 4 D), Compare/i3 (3 S, 2 D). i2 e i3, prima vuote, sono ora riempite mappando su artefatti che _esistono davvero_ — la sintesi (i2) e `verdict.md` (i3) — non per relabeling: è teoria che regge il test sull'arco di input. Ma il risultato non è un trionfo di simmetria, è una diagnosi: l'interno è debole, e la debolezza è la stessa ovunque — la rappresentazione (o2/i2) e la disciplina del verdetto (i3).
- **Lo zero forzati ha ora un significato diverso.** Riempite i2 e i3, nessuna casella ha richiesto di piegare la realtà: il modello ha mappato su artefatti reali (sintesi, `verdict.md`). È un risultato — il ciclo è descrittivamente adeguato a questa classe di repo — ma resta provvisorio per una ragione circolare: questi repo li abbiamo già plasmati col metodo. Il vero test esterno è un repo costruito _senza_ il metodo: il ciclo vi mapperebbe ancora? Finché non lo proviamo, lo zero-forzati è incoraggiante, non conclusivo. Il primo `F` onesto, quando arriverà, varrà più di tutti gli `S`.
- **`o2` è la colonna-spia.** Debole in quattro artefatti su cinque (solo `bi` con Reveal.js la salva). È lo strato di rappresentazione/decisione: la conferma che il collo di bottiglia di tutti gli artefatti è la vista che dovrebbe generare azione. È la stessa diagnosi della stasi di `salute`, l'unico artefatto debole su _entrambi_ o1 e o2 — quasi tutto l'arco di output assente, eppure o3 «medio»: agisce per intuizione senza che l'artefatto lo sostenga, che è il profilo del loop a vuoto.
- **`metodo` non è stato segnato tutto-S di proposito.** Un artefatto che dà il massimo a sé stesso si sta adulando. Anche così sta in alto, e proprio per questo merita la revisione esterna più dura, non la più indulgente.

**La matrice sopra collassa l'annidamento.** Le otto righe trattano ogni artefatto come se avesse un solo ciclo d'azione, ma sono due, annidati (`nested-cycles`): è la seconda delle quattro dimensioni ortogonali di `action-cycle`, quella la cui omissione fa «sparire» un cappio intero. La sezione che segue apre quell'asse per la **sola colonna `metodo`** (dogfooding): le otto righe diventano sedici, otto per ciclo. Gli adottanti restano al protocollo della prima slide (cfr. «Protocollo di riempimento»): la loro verifica dell'annidamento per dominio non è oggetto di questa passata.

## L'asse annidamento (dev/runtime): le 16 celle di `metodo`

I due cicli si distinguono unicamente per _cosa sia il loro Mondo_ in fondo (`nested-cycles`): il ciclo di **sviluppo** ha per Mondo l'artefatto stesso; il ciclo **runtime** ha per Mondo i progetti adottanti. La verifica non affianca due blocchi da otto: marca la **cucitura** dove l'o3 di sviluppo deposita la macchina che il runtime muove.

### Ciclo di sviluppo (Mondo = l'artefatto stesso)

- **Goal (polo) — D**: il polo esiste — `README` è la bussola — ma il suo contenuto _dev-specifico_ è sotto-articolato e mescolato col goal runtime. Ciò che il README dichiara (portabilità, osservatorio) sono in parte proprietà-bersaglio del runtime; la posizione auspicata dello sviluppo lungo le sue dimensioni proprie (attrito/golfi, autonomia dell'umano, temporalità del loop) non è formulata da nessuna parte. Vedi il task dedicato sulla generalizzazione di questo polo.
- **Plan · o1 — S**: `plan.md`, qualificato esplicitamente o1-sviluppo: task aperti, prioritizzati, con dipendenze, in forma-macchina vicino alla KB.
- **Specify · o2 — S**: `tasks/` dà la specifica concreta dei task elencati in `plan`, pronta a essere affinata e poi eseguita — o corretta quando gli obiettivi interni e le relazioni con gli altri task vengono definiti meglio.
- **Perform · o3 — S**: il commit / l'edit ai nodi `kb/` è l'atto versionato sull'artefatto; è l'atto più reale del ciclo e l'**origine della cucitura** — deposita la macchina che il runtime esegue.
- **Perceive · i1 — S**: `tools/kb_tools.py` via `/kb-review` cattura il segnale sull'artefatto — link rotti, orfani, copertura del catalogo, audit «45 nodi, 0 link rotti» — valenza-neutro.
- **Interpret · i2 — vuoto**: il ciclo di sviluppo non ha oggi un'interpretazione propria viva. Il deck `interpretations/`, finora letto come i2-dev-macro, è **riassegnato all'i2-runtime** (è la vetrina rivolta agli adottanti, non l'auto-interpretazione dello sviluppo); la sua ri-canonizzazione è una conseguenza del gate. Lo sviluppo si auto-interpreta semmai quando un segnale risale, ma non ha un i2-dev vivo allo stato.
- **Compare · i3 — S**: `verdict.md`, qualificato esplicitamente i3-sviluppo; la migrazione a stato-per-filo aggiornato in place ne è la prima istanza canonica reale.
- **Mondo (polo) — S**: l'artefatto stesso, dichiarato Mondo di sviluppo nel README. **È anche la macchina del ciclo runtime — qui passa la cucitura.**

### Ciclo runtime (Mondo = i progetti adottanti)

- **Goal (polo) — S**: il ciclo runtime ha obiettivi costitutivi reali, distribuiti nell'artefatto più che raccolti in un goal-artefatto unico — portabilità, indipendenza dal modello, adattabilità a domini molto diversi (e quindi flessibilità), meccanismi di autocorrezione, rigore delle fonti, il pavimento teorico su cui il metodo poggia. Il polo è ben costituito ai bordi (un polo si costituisce, non si esegue); per `method` è più ricco del Goal-dev. La ripartizione fine di questi obiettivi tra Goal-runtime e Goal-dev è materia del task dedicato sulle dimensioni del Goal.
- **Plan · o1 — vuoto (gap)**: la pianificazione **top-down** — come gli artefatti adottanti dovrebbero diventare — non esiste. A differenza degli altri vuoti non è legittimo-per-design: è l'arco che il principio «`metodo` non orchestra task sui adottanti» ha finora negato, e che il gate trova **da costruire** (l'esecuzione top-down ha pari dignità della valutazione bottom-up; la sua assenza è sovra-esposizione del dal-basso). È il vero buco del ciclo runtime.
- **Specify · o2 — D**: il deck `interpretations/`, letto come vista-di-decisione/vetrina, è la superficie o2 del runtime — il concentrato interpretato della KB, dove il metodo si presenta. Esiste e funziona, ma gli mancano le **slide comparative sui quattro domini** e le **specifiche** (per un dominio o per tutti) che ne farebbero la fotografia senza-drift valutabile contro gli obiettivi: D, non S.
- **Perform · o3 — S**: `prescriptions/` è il canale o3 reale e canonizzato in `project-structure`; runbook reali vi sono transitati (il runbook d'atrio). Oggi senza prescrizioni attive, ma **ha già funzionato**: S per capacità reale, non per pienezza istantanea.
- **Perceive · i1 — S**: `perceptions/` è il canale i1 reale, con un segnale catturato (`adottanti-pianificano-il-canone-in-plan.md`), valenza-neutro. Ha già funzionato: stesso metro di o3.
- **Interpret · i2 — D**: stessa superficie del deck, letta come interpretazione (call A: il deck è i2-runtime, non i2-dev). Vocazione runtime, ma oggi interpreta i nodi del metodo (Mondo-dev), non i quattro domini (Mondo-runtime): è la **deriva** che lo tiene a D. Segnarlo S sarebbe la simmetria-compiacente che la matrice esiste per prevenire.
- **Compare · i3 — D**: la valutazione-osservatorio — confrontare la fotografia dei quattro domini contro gli obiettivi-runtime — è inquadrata da `adopter-comparison` (la lente) e vive in parte nei thread adottanti di `verdict.md`, ma non è materializzata come verdetto-runtime a sé. Presente, sparsa.
- **Mondo (polo) — S**: i progetti adottanti (`nixos`, `bi`, `economia`, `salute`), dichiarati Mondo runtime nel README; reali, distinti e raggiunti via symlink.

Conteggio `metodo`, 16 celle: **10 S, 4 D, 2 vuoto, 0 F** (dev: 6 S, 1 D, 1 vuoto; runtime: 4 S, 3 D, 1 vuoto). Zero forzati anche dopo aver popolato l'interno runtime — ma il dato che parla è la _forma_: le quattro D segnano gli archi immaturi, e i due vuoti distinguono il quiescente-legittimo (dev-i2) dal vero gap (runtime-o1).

### I due cicli, la cucitura e le asimmetrie reali

Il riempimento rivede la prima lettura. Il ciclo runtime di `metodo` non è una membrana ricucita su un interno vuoto: è **un ciclo genuino con entrambi gli archi**, parte dei quali immaturi. Due letture corrette in corso d'opera, da ratificare (cfr. «Verdetto-gate»):

- il **deck** (`interpretations/`) non è i2 del ciclo di sviluppo ma **i2/o2 del runtime** (call A): è la vetrina rivolta agli adottanti. Oggi però interpreta i nodi del metodo (Mondo-dev), non i quattro domini (Mondo-runtime): la deriva che lo tiene a D.
- l'**arco top-down del runtime** (o1) è il vero buco — non un vuoto-per-design ma un vuoto-gap, negato finora dal principio «`metodo` non orchestra task sui adottanti», che il gate trova **da rivedere** (call B). L'esecuzione top-down ha pari dignità della valutazione bottom-up.

Resta vera la **cucitura di output** (la canonica di `nested-cycles`): il Mondo-dev — l'artefatto — _è_ la macchina del runtime. Ciò che lo sviluppo costruisce è esattamente ciò che gli adottanti eseguono via symlink; l'o3-runtime (`prescriptions/`) propaga le modifiche a quella macchina. Ma non è più l'unico legame: i due cicli condividono il polo Goal (obiettivi in larga parte runtime) e si parlano in entrambi i versi, non solo dal-basso.

Le asimmetrie sono dunque reali, non simmetria assunta: **dev-i2 vuoto** (lo sviluppo non si auto-interpreta dal vivo) contro **runtime-i2 presente ma deriva** (il deck); e soprattutto **runtime-o1 il buco** (l'arco top-down mai costruito perché negato dal canone).

### Verdetto-gate

L'annidamento a 16 celle **regge per `metodo`, e più di quanto la prima lettura dicesse**: non una cucitura su mezzo ciclo, ma **due cicli genuini**, entrambi sostanzialmente popolati (10 S, 4 D, 2 vuoto, 0 F).

- **Regge la struttura**: zero celle forzate; entrambi i cicli hanno poli costituiti, membrana fisica (o3/i1 runtime) e — corretta la lettura — anche interno (il deck come o2/i2-runtime, la valutazione-osservatorio come i3-runtime).
- **Le asimmetrie sono reali, non simmetria assunta**: dev-i2 vuoto contro runtime-i2 in deriva; e **runtime-o1 il buco** — l'arco top-down mai costruito perché negato dal canone.

**Conseguenza per la presentazione.** Ribaltata rispetto alla prima stesura: una rappresentazione a **due cicli** è ora _giustificata_ — l'errore non era pensarli due, era darlo per scontato prima del gate. La home mostra due cicli, con **runtime-o1 muted** (il gap dichiarato), il deck come livello behavioral (o2↔i2) del runtime, la cucitura di output al polo Mondo. Ma — caveat anti-complicità — questa pienezza poggia su due mosse di canone (riassegnare il deck al runtime, rivedere «non orchestra»): il gate le **segnala come il lavoro**, non le dà per fatte. Vanno ratificate in una passata deliberata prima che la presentazione le incida.

### Mappa-sorgente (b)

Prodotta perché (a) regge. Per ciascuno dei 16 elementi, la sua casa nell'atrio — l'indice che i task di presentazione consumano senza inventare la geometria a mano.

Ciclo di sviluppo:

- Goal-dev → `README.md`
- o1-dev → `plan.md`
- o2-dev → `tasks/`
- o3-dev → git commit / l'edit ai nodi `kb/`
- i1-dev → `tools/kb_tools.py` (`/kb-review`: audit, backlink, copertura)
- i2-dev → ∅ vivo (il deck è riassegnato all'i2-runtime; lo sviluppo non si auto-interpreta dal vivo)
- i3-dev → `verdict.md`
- Mondo-dev → l'artefatto stesso — **= macchina del runtime (cucitura)**

Ciclo runtime:

- Goal-runtime → `README.md` (obiettivi distribuiti: portabilità, indipendenza dal modello, adattabilità, autocorrezione, rigore fonti, pavimento teorico)
- o1-runtime → ∅ oggi — il **gap top-down** da costruire (cfr. revisione di «non orchestra»)
- o2-runtime → `interpretations/` (deck come vetrina/decisione; manca la comparativa 4-domini e le specifiche)
- o3-runtime → `prescriptions/` (runbook di propagazione)
- i1-runtime → `perceptions/` (segnale metodologico dell'adottante)
- i2-runtime → `interpretations/` (deck come interpretazione; oggi in deriva su Mondo-dev)
- i3-runtime → `adopter-comparison` (lente) + thread adottanti in `verdict.md` (non materializzato a sé)
- Mondo-runtime → progetti adottanti: `../nixos`, `../bi`, `../economia`, `../salute`

## Protocollo di riempimento

I verdetti deboli e quelli riempiti per ragionamento si verificano sul campo, non a tavolino qui. Il luogo della verifica è la prima slide di ciascun artefatto — il suo autoritratto attraverso i sei atti e i due poli, applicati al proprio dominio: dove l'accostamento è debole o forzato, tanto meglio, costringe a guardare l'artefatto in modo analitico. `metodo` non orchestra questo lavoro nei repo adottanti (cfr. `adopter-comparison`): ogni repo riempie la propria colonna, e il verdetto risale qui come fotografia aggregata. Le righe i2/i3 sono ora riempite per ragionamento (mappano su artefatti reali); questo nodo resta `bozza` finché la verifica esterna repo-per-repo non le conferma — o le smentisce.

Connessioni:

- [action-cycle](action-cycle.md)
- [world](world.md)
- [goal](goal.md)
- [output](output.md)
- [system-image](system-image.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
