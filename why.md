# why.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta. La decisione è la chiave dell'entry, la data un metadato, il commit un puntatore citabile inline.

---

## 2026-06-06 — Ri-derivazione dell'o2: il metodo gira il proprio Compare su sé stesso

Il task `affinamento-o2` chiedeva una «rilettura ravvicinata» della presentazione, ma alla luce dei
refactor recenti la parola era riduttiva: non un affinamento, ma una **ri-derivazione** — l'`i1→i2→i3`
che la disciplina dell'o2 prescrive da sé («l'o2 rivela, i nodi risolvono, poi si ri-deriva l'o2»). I
nodi avevano appena risolto (de-cablaggio, stessa giornata); toccava all'o2 ri-derivare.

Prima la calibrazione onesta, perché conta: l'o2 **non era largamente stale**. L'allineamento al
cruscotto (anatomia, routing, `AGENTS.md` come wrapper) e i cambi del 05-06 (la matrice 4D che
rimpiazza «due agenti», i cicli annidati come capitolo) erano già dentro; le «cose da approfondire»
del task erano per lo più già fatte. Riscrivere da capo sarebbe stato disonesto verso ciò che reggeva.
La ri-derivazione ha quindi propagato solo i due deltas davvero pendenti.

**Delta 1 — de-cablaggio propagato.** L'agente, ancora cablato come binario «umano · LLM» in tre
punti (diagramma *Cosa è*, matrice *Quattro dimensioni*, *Approfondimento*), è diventato «caso
saliente di una popolazione» — con la glossa di Norman «person, animal, or machine» e il gradiente
per capacità. Vincolo rispettato: **niente anticipazione** della struttura multi-agente (la
maturazione di `agente` resta bottom-up); si è solo tolto al binomio lo statuto di struttura unica,
esattamente come nei nodi.

**Delta 2 — o2-come-Compare elevato.** L'intro della presentazione prometteva da tempo «perché
questa pagina ne sia un esempio, si chiarisce più avanti» e non manteneva. Una nuova sezione scioglie
la promessa: l'o2 è la forma cristallizzata dello **stadio Compare** (i3) del ciclo di sviluppo,
simmetrico a `plan.md` (lo stadio Plan); rivela le contraddizioni *non-locali* invisibili da dentro i
nodi atomici, che poi si risolvono giù nei nodi. È la prima volta che la tesi «o2 come organo di
valutazione» — annotata nel task come maturazione attesa — atterra *nell'o2 stesso*: dogfooding, la
pagina dice cosa è e cita la propria revisione come esempio.

Verifica: PDF rigenerato con `md2pdf` e ispezionato pagina per pagina — i diagrammi rendono, i tre
punti del de-cablaggio e la nuova sezione 11 ci sono; il PDF (o3) non è versionato. Con la verifica
fatta, `affinamento-o2` è completo e **chiuso**: la sua tesi vive ora nell'o2 e in questa entry, lo
storico in git. La maturazione facoltativa — condensare «o2 come Compare» in una nota di nodo dentro
`system-image` o `output` — resta da far emergere dall'uso, non come task in piedi.

## 2026-06-06 — De-cablaggio del binomio «due agenti»: il caso saliente non è la struttura

Il metodo era nato descrivendo due agenti — l'umano e un singolo LLM — e su quel binomio aveva
cablato la sua asimmetria in più nodi come se fosse *la* struttura. Con la creazione del nodo
`agente` (bozza, stessa giornata) il binomio è stato riconosciuto per ciò che è: il **caso
saliente** di una popolazione di agenti più ampia. Norman definisce l'agente come «person, animal,
or machine», e la categoria macchina non è un punto ma un gradiente — un LLM di frontiera che
pianifica e un agente locale che esegue non sono lo stesso lettore, anche sulla stessa KB.

Questa sessione esegue la prima metà del task `de-cablaggio-agenti`: l'ammorbidimento dei nodi che
portavano la falsa certezza. Principio di lavoro: **additivo, non distruttivo**. L'asimmetria
umano/LLM non si cancella — resta vera *come caso* —, le si toglie solo lo statuto di struttura
unica. Tre nodi: `system-image` (il binomio dichiarato caso saliente, non struttura), `sistema-cognitivo`
(la sezione «asimmetria dei due agenti» diventa «asimmetria umano / LLM», con la cornice di
popolazione in apertura) e `knowledge-base` (maturo, tocco minimo: una frase *condizionale* — la
divisione del lavoro può ripartirsi tra livelli di agente «quando l'uso multi-agente diventa reale»).

Due scelte di metodo che contano. *Perché condizionale e non descrittivo:* la seconda metà del task
— la maturazione di `agente`, la biforcazione di o1 per capacità, l'asse fiducia/privacy, la
divisione per stadio del ciclo — resta esplicitamente **bottom-up, non anticipata**. Si aspetta che
un secondo livello di agente entri nell'uso reale; scrivere ora quegli arredi sarebbe inventare
struttura prima dell'evidenza, l'opposto di come il metodo si sviluppa. *Perché additivo basta per
gli adottanti:* i nodi sono condivisi via symlink da nixos/bi/economia/salute; un ammorbidimento che
preserva il caso umano/LLM non rompe il senso a valle, dove quel caso è ancora l'unico in uso.

Effetto collaterale che chiude un debito: i tre nodi ora linkano `agente`, che era nato orfano —
il de-cablaggio ripara anche il backlink mancante (audit: 0 link rotti, nessun orfano residuo).

## 2026-06-06 — Il root è il cruscotto del ciclo di sviluppo: la fondazione del file che il ridisegno ha ribattezzato

Questa è la prima entry di `why.md`, ed è il perché del file stesso. La migrazione del layout ha
ribattezzato `log.md` in `why.md` e con essa l'intero top level dei repo. La decisione di fondo:
**la root non è "ciò che è più stabile" ma il cruscotto del ciclo di sviluppo** — i pochi artefatti
letti a ogni sessione per capire il tutto. Il vecchio criterio «più in alto = più stabile» era già
stato demolito da `pace-layering`; mancava cosa mettesse al suo posto. La risposta è la triade
ora in `struttura-progetto`: (1) root = bootstrap-essenziali del ciclo, (2) cartelle = collezioni
atomiche con file-meta dentro solo se on-demand, (3) la pace decide cosa non fondere, non la
profondità. Quando altezza e pace confliggono, l'altezza decide la collocazione (per questo `plan`
e `why` stanno in root pur essendo veloci) e la pace decide che restino file separati (per questo
`map` e `plan` non si fondono nel README).

**Cosa cambia, e perché ognuna conta.**

- `log.md` → `why.md`: il nome dice la funzione (il perché), non il tipo di file. Nuovo modello di
  entry: decisione come titolo-tesi, data come metadato, commit inline.
- catalogo dei nodi dal README → register `kb/index.md`: il catalogo è il file-meta di una
  collezione consultata on-demand, quindi vive *dentro* `kb/`, non in root. Il README si alleggerisce
  e punta.
- lista task dal README → `plan.md` in root: la meta-istanza dei task è lo stadio Plan del ciclo,
  letta a ogni sessione; l'altezza la solleva fuori da `tasks/`. Distinta da o1, il Plan del runtime.
- `mappa` → `map.md` in root: il modello del dominio (o2) come file root conciso, separato dal README
  per pace; nel `metodo` la presentazione resta l'o2/o3 ricco, `map` ne è la versione di bootstrap.
- `todo/` → `tasks/`, e i nodi `task-aperti`→`plan`, `todo`→`tasks`, `mappa`→`map`, `log`→`why`:
  allineamento al vocabolario del metodo (nome del nodo = nome dell'artefatto).
- policy linguistica: forma in inglese per gli artefatti strutturali vivi (`map`/`plan`/`why`/`index`),
  italiano per nodi-concetto e prosa. La coppia `kb/index.md` (vivo) / `kb/indice.md` (doc) è il
  significante della policy.

Il ridisegno è applicazione di `sviluppo-metodo`: cornice posata dall'alto (il ciclo di Norman) e
verificata dal basso contro le root reali dei quattro adottanti — da cui è emerso il punto 4 della
triade, la root estensibile con file di dominio (`stato.md`, `scadenze.md`, `diario.md`). Migrazione
eseguita su `metodo`, `nixos` e `bi`; `economia` e `salute` seguiranno con lo stesso passaggio.

## 2026-06-05 — Il ciclo è uno specchio simmetrico, i cicli annidati sono la spina dorsale: ritratto «o1 = secondo agente»

La revisione della presentazione (o2) ha fatto emergere una contraddizione interna alla KB,
non un difetto della slide. `output.md` e `ciclo-azione.md` dicevano insieme due cose
incompatibili: (A) «cappio a due cerniere asimmetriche, *non* uno specchio; o1 non sta
sull'arco principale, vive sul ciclo del secondo agente (l'LLM); due cicli, uno per agente»;
(B) «cicli annidati: sviluppo (mondo = il codice) dentro runtime (mondo = la realtà)». La (A)
spiegava *dov'è o1* assegnandolo a un altro agente; la (B) spiegava il raddoppio con
l'annidamento. Le due non combaciano.

**Risoluzione (confronto con Stefano, che aveva in mente fin dall'inizio il doppio cappio
simmetrico alla Norman).**

- *La simmetria resta.* Ogni ciclo è lo specchio di Norman: esecuzione che scende, valutazione
  che risale, Goal all'apice, Mondo in fondo. Lo specchio è **per altitudine**: o3↔i1 al Mondo
  (Perform/Perceive), o2↔i2 in mezzo (decisione/interpretazione), o1↔i3 alla KB (piano
  strutturato / conoscenza formalizzata). Lo «specchio o1↔i3» che il 04-06 aveva *negato* è in
  realtà quello corretto. I numeri sembrano non combaciare solo perché contano la distanza
  dall'inizio dell'arco (output scende, input risale).
- *L'asimmetria è locale all'apice.* La cerniera-KB è scrivi-poi-leggi (i3 scrive, il Goal legge
  dalla memoria persistente). È reale, ma è proprietà del vertice — non ampùta la simmetria degli
  archi. Si tengono entrambe: archi speculari + apice speciale.
- *o1 non manca e non è «di un altro agente».* È il livello-macchina dell'arco di output.
  L'errore era collassare il **livello** (1/2/3) nell'**agente** (umano/LLM): sono dimensioni
  *ortogonali*.
- *I due cicli sono annidati per Mondo, non divisi per agente.* Runtime agisce sulla realtà,
  sviluppo agisce sull'artefatto. o1/2/3 e i1/2/3 si raddoppiano: o3-sul-mondo (transazione) vs
  o3-sull'artefatto (commit); i1-dal-mondo (referto) vs i1-dall'artefatto (lint/audit/test).
  L'o3 del ciclo di sviluppo *è* la macchina del ciclo runtime — è l'incastro dell'annidamento.
- *Quattro dimensioni ortogonali.* Ogni elemento del metodo si colloca su: agente (umano/LLM),
  annidamento (runtime/sviluppo), livello (1/2/3), lato del cappio (output/input). La matrice
  sostituisce il taglio rigido «per agente» e la tabella piatta «stato dei progetti adottanti»
  come lente per confrontare i domini e leggere cosa è sviluppato, cosa manca perché inutile,
  cosa manca e servirebbe.

**Ritrattazione.** Rimosse da `output.md` e `ciclo-azione.md` le affermazioni «o1 vive sul ciclo
del secondo agente / due cicli uno per agente» e «o1 e o2 sono lo stesso stadio per due agenti».
Promossi i cicli annidati da caso particolare code-based a struttura portante del modello.

**Perché conta.** È la prima volta che la revisione dell'o2 (la presentazione di sintesi) ritorna
come correzione nei *nodi* canonici: l'arco di input del ciclo di sviluppo che lavora sul metodo
stesso. Il dubbio era di Stefano fin dall'inizio (il doppio cappio simmetrico); la presentazione
ha reso la contraddizione interna abbastanza visibile da scioglierla. Bottom-up, dogfooded.

**Resta aperto.** Riallineare i capitoli 2/3/4/6 della presentazione al modello corretto (la
matrice 4D sostituisce «due agenti»; i cicli annidati diventano un capitolo); la confusione
`AGENTS.md` vs `CLAUDE.md` nell'anatomia.

---

## 2026-06-05 — La presentazione (o2) riallineata alla rifondazione: da 5 a 8 diagrammi

Lo sweep nomenclatura del 06-05 aveva già toccato `presentazione/metodo-in-sintesi.md`
(diagramma del ciclo con o/i, freccia di ritorno i3→KB), ma la presentazione era rimasta
ferma *a metà*: spiegava la *meccanica* del metodo (i tre giganti) senza il *salto di quota*
della rifondazione — lo strato che sta sopra i giganti, *cosa è* l'oggetto e *cosa vuole* chi
lo usa. L'o2 mostrava come funziona il metodo ma non diceva mai cosa coltiva.

**Scelta di scope: rifondazione piena, non refresh minimo.** Vagliate tre opzioni (solo
data+link; cornice ontologica; tutti i diagrammi). Scelta la piena, accettando il rischio di
gonfiare l'o2, perché la tripartizione è la cornice che dà senso a tutto il resto: tenerla
fuori dalla vista d'insieme la lasciava implicita proprio dove serve esplicita. Tensione reale
registrata e non nascosta: l'o2 distilla il *stabile*, ma i tre nodi nuovi sono `bozza`. Risolta
con una nota di fedeltà nell'intro — lo strato concettuale superiore è dichiarato come
rifondazione recente in maturazione `bozza→maturo`, non spacciato per consolidato.

**Arco esplicito ontologia → meccanica → processo.** Da 5 a 8 diagrammi:
- *Cosa è: artefatto, sistema, metodo* (nuovo) — tripartizione con l'artefatto al centro tra i
  due agenti dentro il sistema; il metodo che lo coltiva. Include l'argomento decisivo: la tesi
  "artefatto portabile, vendor-neutro" è dicibile solo con la definizione artefatto-centrica.
- *I tre giganti* (tenuto, riposizionato sotto l'ontologia) — formula "Luhmann è la KB /
  Karpathy la governa / Norman la connette al mondo".
- *Il cappio a due cerniere* (rifatto dal "ciclo che si chiude") — Goal apice, Mondo fondo,
  discesa esecuzione / risalita valutazione; cerniera Mondo simmetrica, cerniera KB scrivi-poi-leggi.
- *Il goal: tre altitudini* (nuovo) — motivo/goal/operazione, confine aperto, i due modi di i3.
- *I due agenti sulla stessa KB* (nuovo) — o1 vs o2, asimmetria dei modelli mentali, gradiente
  di autonomia.
- *Anatomia / Bottom-up / Dove vive cosa* (tenuti invariati).

**Collaterali.** Data `06.04→06.05`; sezione "strato output di questo repo" aggiornata (i1 cita
ora `sources/`); Approfondimento linka i tre nodi nuovi. README: riscritta la riga che parlava
di "cinque diagrammi" con il nuovo arco. PDF (o3) rigenerato con `md2pdf`, non versionato.

Dogfooding: questa è la prima volta che l'o2 del repo metodo viene riallineato a un cambiamento
*concettuale* dei nodi, non solo nomenclaturale — il criterio di aggiornamento dichiarato nel
file ("quando un gigante, un livello, un componente o un concetto fondativo cambia, qui si
aggiorna il diagramma") applicato a sé stesso.

---

## 2026-06-05 — Chiusura del ciclo concettuale: tre nodi nuovi, sweep nomenclatura, todo/ svuotato

Sessione esecutiva che chiude il lavoro concettuale avviato il 04-06 e portato in pianificazione il 05-06 mattina. Due filoni paralleli: (1) tre nuovi nodi di quota superiore fondati su fonti; (2) sweep completo della rifondazione input/output.

**`representation.pdf` scioglie il gap di fonte.** In `sources/` erano già presenti i testi di Norman distillati nelle sessioni precedenti; oggi è apparso anche `representation.pdf` — il Capitolo 3 di *Things That Make Us Smart* (1993), con due estrazioni testuali (`pdftotext` e GLM-OCR). È esattamente la fonte che mancava per fondare `artefatto-cognitivo` e `sistema-cognitivo` su un testo reale invece che su citazioni di seconda mano. Il gap registrato in `sources/README.md` e in `ingest-norman` si chiude parzialmente: il Cap. 3 è ora distillato, il volume completo resta da reperire.

**Tre nodi di quota superiore.** Il lavoro concettuale del 04-06 — tripartizione artefatto/sistema/metodo, gerarchia del goal, genus/species — era rimasto in `log.md` e in `todo/artefatto-cognitivo.md`. Questa sessione lo porta nei nodi:

- `kb/artefatto-cognitivo.md` — fondato sul Cap. 3 di Norman: definizione di artefatto cognitivo, sistema di rappresentazione (represented/representing world), distinzione cognizione esperienziale vs riflessiva, principio di naturalezza (Simon: "solving a problem simply means representing it so as to make the solution transparent"). Aggancio diretto al metodo: la KB è ben progettata quando la risposta giusta emerge per ispezione, non per calcolo.
- `kb/sistema-cognitivo.md` — fondato su Hutchins (*Cognition in the Wild*, 1995) e Norman (1991): il sistema cognitivo come accoppiamento dinamico artefatto + umano + LLM; asimmetria strutturale tra i due agenti (per l'LLM la KB *è* il modello mentale, non un promemoria); tripartizione artefatto/sistema/metodo con la distinzione operativa portabile/emergente. Aggiunta nella seconda passata la sezione Genus e species: lo stack di messa-in-opera (A) vs la discendenza degli artefatti (B); il metodo come genere, i quattro repo come specie; auto-riferimento del metodo che si applica a sé stesso.
- `kb/goal.md` — fondato su Leontiev (activity theory): gerarchia motivo → goal → operazione; `goal`/`task`/`todo` come tre altitudini non sinonime. Confine aperto di Norman: il ciclo presuppone il goal ma non lo forma. Due modi di i3: verdetto (loop noti, delegabile) e triage/formazione-goal (esogeno, la cosa meno esternalizzabile — eco di Bainbridge).

I tre nodi completano il vocabolario che il metodo non aveva: sapeva cosa produce (output), come lo produce (ciclo), dove lo conserva (KB), ma non aveva il nome preciso di *cosa è* l'oggetto che coltiva né di *cosa vuole* chi lo usa.

**Sweep nomenclatura: rifondazione completata.** La conversione `ponte → output`, `L1/L2/L3 → o1/o2/o3` era pianificata da settimane e sempre posticipata perché toccava molti file. Questa sessione la esegue per intero:

- `kb/output.md` — nodo nuovo che sostituisce `ponte.md`: o1/o2/o3 + strati input i1/i2/i3 + cappio con due cerniere asimmetriche (Mondo e KB). Il cappio era formulato nel log del 04-06 e mai disegnato; ora è nel corpo del nodo e nel diagramma mermaid della presentazione.
- `kb/ciclo-azione.md` — tabella sinottica Norman → o/i; sezione gulf estesa a i1/i2/i3; cappio a due cerniere come struttura del ciclo. La nomenclatura L è eliminata ovunque.
- `presentazione/metodo-in-sintesi.md` — il diagramma "ciclo che si chiude" mostra ora entrambi gli archi (o1/o2/o3 e i1/i2/i3) con la freccia di ritorno i3→KB.
- Sweep in 10 nodi: affordance-signifier, confronto-progetti-adottanti, design-principles, knowledge-base, mappa, metodo-kb, pattern-karpathy, strumenti-kb, struttura-progetto, zettelkasten.
- `kb/ponte.md` eliminato.

**`todo/` svuotato.** Per la prima volta da quando la rifondazione era stata aperta, `todo/` è vuoto. I tre task (`rifondazione-input-output`, `ingest-norman`, `artefatto-cognitivo`) sono stati eliminati — non marcati completato nel frontmatter, eliminati: il contenuto era tutto nei nodi, il perché in questo log, la storia in git. La regola del metodo applicata a sé stessa.

**Cosa resta aperto (non come task, come stato dei nodi).** I cinque nuovi nodi bozza del 05-06 (`artefatto-cognitivo`, `sistema-cognitivo`, `goal`, `output`, più i tre del mattino) attendono la maturazione `bozza→maturo` che arriverà dall'uso reale. Il volume completo di *Things That Make Us Smart* non è ancora reperito: Hutchins e Leontiev sono citati nei Riferimenti ma non in `sources/`. La fonte primaria Hutchins per `sistema-cognitivo` e la fonte Leontiev per `goal` sono debit di fedeltà da colmare.

---

## 2026-06-05 — Primo arco input dogfoodato: `i1` Norman in `sources/`, tre `i2` come nodi bozza

Sessione breve e operativa, ma scioglie una decisione che era ferma sulla carta. Il task
`ingest-norman` prevedeva il primo pilota dello strato input; `rifondazione-input-output`
aveva la decisione cardine #1 ("dove vivono le fonti grezze i1?") esplicitamente sospesa,
*da sciogliere col dogfooding, non a scrivania*. Questa sessione fa proprio quello: posa un
i1 reale e lascia che sia la posa a decidere la struttura.

**`sources/`, non `fonti/`.** Scelto l'inglese: anticipa la traduzione del repo già decisa,
si allinea alla nomenclatura i1/i2/i3 e tiene il nome separato dalla sigla (la cartella è
*dove vivono gli i1*, non si chiama `i1`).

**I binari non si versionano, la provenienza sì.** Tre ragioni convergono: i libri sono
sotto copyright e il repo è pubblico (versionarli = distribuirli); metodologicamente l'i1
grezzo sta *separato* dai nodi distillati (il repo versiona i2/i3, non il binario); e il
`.gitignore` già escludeva i `*.pdf` — ma per l'altro motivo (output derivati), e l'EPUB
sarebbe sfuggito. Sistemato con `sources/*` + `!sources/README.md`. Il manifest versionato
registra edizione, formato e ISBN di ogni fonte: è la base dei `## Riferimenti` (i3, fedeltà
alle fonti — *quale libro per quale idea*), riproducibile senza distribuire i file.

**La scelta della copia è un atto di fedeltà, non di igiene.** Erano arrivate quattro copie
di DOET. Tenuta solo l'**EPUB 2013 Revised and Expanded** perché è l'edizione che *aggiunge*
affordance e signifier rispetto all'orig. 1988 — i concetti che servono — e perché l'EPUB ha
testo nativo, qualità superiore al PDF per la distillazione i1→i2. Scartate l'ed. 2002 (priva
di signifier), una scansione da 23 MB senza strato testo (5 caratteri estraibili in 5 pagine,
inservibile) e il PDF 2013 ridondante. *Emotional Design* (2004) resta come copia unica.
Registrato anche il gap noto: *Things That Make Us Smart* (1993) — fonte dei concetti nuovi
(artefatto cognitivo, cognizione distribuita) — non ancora reperito.

**Primo i2, e la decisione su dove vive.** Nella stessa sessione il passaggio è andato avanti
fino all'i2: la prima nota distillata, dal testo *reale* dell'EPUB (estratto con `pandoc`,
non a memoria — fedeltà alla fonte). Concetto scelto: **affordance e signifier**, Cap. 1 di
DOET 2013 — esattamente l'aggiunta per cui avevamo tenuto questa edizione (Norman la dichiara
«the most important addition to the chapter»). Decisione sciolta col dogfooding: **l'i2 non
ha una casa separata, *è* un nodo bozza in `kb/`**, e il passaggio i2→i3 *è* la maturazione
`bozza→maturo`. Coerente con come il repo già fa maturare i nodi (`ponte`, `ciclo-azione`
sono bozza per scelta); scartate la co-locazione in `sources/` e una cartella `i2/` dedicata
perché avrebbero introdotto una terza casa per qualcosa che è già conoscenza in formazione.

Due i2 posati nella stessa sessione, entrambi bozza, collegati a/da `ciclo-azione`,
indicizzati, lint pulito. Il guadagno concettuale non è didascalico: in entrambi è la *fonte*
a fondare l'estensione del metodo, non il metodo a forzare la fonte.

- `kb/affordance-signifier.md`: la definizione di Norman dell'agente che interagisce — «a
  person, animal, **or machine**» — fonda testualmente il ciclo a due agenti. I due strati
  output (L1 macchina, L2 umano) sono i signifier di cui ciascun agente ha bisogno.
- `kb/system-image.md`: il triangolo design model / system image / user's model, con «the
  entire burden of communication is on the system image», fonda testualmente la tesi *la KB è
  il system image condiviso dai due agenti*. L'asimmetria già annotata il 04-06 trova qui la
  sua radice in Norman: per l'umano la KB è impalcatura esterna a un modello che già possiede,
  per l'LLM il system image e lo user's model coincidono (riparte da zero). E un aggancio non
  cercato: Norman dice che un modello semplificato vale «only as long as the assumptions that
  support them hold true» — è il meccanismo esatto del guasto `bi`/1018022 e la giustificazione
  del check "decisioni e assunzioni" in `fedelta-cognitiva`.
- `kb/visceral-behavioral-reflective.md` (da *Emotional Design* 2004): i tre livelli di
  elaborazione. La KB è lo strato *reflective* — «the learning of new concepts and
  generalizations about the world» —, e l'esempio della staccionata di Norman (riflettere
  sull'esito, «move the fence... so we don't have to walk around next time... also tell other
  people») *è* il filing back, parola per parola. Il limite del riflessivo, «it does not have
  direct access to the control of behavior... it watches over and tries to bias the behavioral
  level», è il gulf of execution in termini neuropsicologici e la ragione per cui lo strato
  output esiste: il sapere non agisce, condiziona l'azione altrui. Questa fonte aggiunge ciò
  che le altre due non danno — la dimensione affettiva (orgoglio/possesso/storia del repo),
  che tiene l'umano nel loop quando il behavioral è delegato alla macchina.

Sono anche i primi tre `## Riferimenti` posati con provenienza esatta (edizione, capitolo,
sezione) invece della citazione vaga di seconda mano — il payoff dell'i3 sulla fedeltà.

**Cos'è l'estrazione testuale di una fonte.** Domanda emersa dogfoodando: il `.txt` prodotto
da `pandoc`/`pdftotext` è i1 o i2? È **i1 in forma testuale canonica** — stesso contenuto del
binario, nessuna interpretazione; la linea i1→i2 è l'*interpretazione*, e lì non ce n'è. Vive
in `sources/` accanto al binario come superficie di lavoro (greppabile, verificabile), e per
copyright è ignorata esattamente come il binario — anzi a maggior ragione, essendo testo
pieno cercabile. Il manifest ora versiona la *ricetta di rigenerazione*, non il testo.

**Cosa resta.** La decisione cardine #1 è sciolta su entrambe le metà (i1 in `sources/`, i2
come nodo bozza), e le fonti che abbiamo sono ora distillate (tre i2, due da DOET, uno da
*Emotional Design*). Restano: il gap di *Things That Make Us Smart* (artefatto cognitivo,
cognizione distribuita) che tiene zoppo l'i3 sui nodi `artefatto-cognitivo`/`sistema-cognitivo`;
e la maturazione `bozza→maturo` dei tre nuovi nodi, primo i2→i3 da osservare nell'uso.

## 2026-06-05 — Cicli annidati e il guasto del gulf di valutazione (caso bi/1018022)

Sessione mista: confronto terminologico + un caso reale di `bi` usato come banco di prova,
sfociata in due modifiche ai nodi.

**Terminologia input/output — deciso di tenerla.** Vagliata l'alternativa
`esecuzione/valutazione` (fedele a Norman, più "vestita"). Tenuto `input/output` perché:
le sigle `i1..i3`/`o1..o3` derivano dalle iniziali e sono sistematiche (due regole, sei
sigle derivabili), mentre i nomi di Norman vanno memorizzati uno a uno; in inglese
*execution* ed *evaluation* collidono sulla `e`; e — punto dirimente — la circolarità del
ciclo (Norman è opportunistico: può partire dal goal o dallo stimolo/affordance) toglie
ogni "ordine corretto", lasciando intatto solo il significato *direzionale* di input/output
(dentro/fuori dal sistema), che è invariante rispetto al punto d'innesco. Scartata l'idea
di usare i nomi-stadio di Norman come etichette degli strati: gli stadi sono *atti
cognitivi* (verbi), gli strati sono *artefatti* (il referto non "percepisce", è il
percepito) — mismatch ontologico. Sintesi adottata: sigla i/o come struttura, verbo di
Norman come *glossa* d'insegnamento.

**Cicli annidati (contributo nuovo, in `ciclo-azione`).** Un progetto code-based non ha un
ciclo d'azione ma due, annidati: il *ciclo di sviluppo* (Goal → todo → commit; mondo = il
codebase; il suo `o3`/L3 *è il codice*) dentro il *ciclo runtime* (il codice esegue e
produce L1/L2/L3). Il codice è insieme L3 del primo e macchina del secondo. Risalire da un
output al task — `output → codice → commit → todo → goal` — è attraversare l'annidamento:
`git-history`/`log`/`todo` sono le fonti che registrano il ciclo di cui ogni artefatto è un
fossile. È il senso preciso in cui il metodo *estende* Norman: il Mondo, scatola nera per
Norman, qui è esso stesso un artefatto con provenienza — il metodo la apre.

**Affinata `o1`/`o2` (continuità col 2026-06-04).** Non due stadi diversi di Norman ma lo
stesso Plan/Specify rivolto a due *consumatori* (macchina/umano) — la stessa intuizione già
annotata ieri ("o1 non manca: è il ciclo applicato al secondo agente"), ora portata nel
corpo del nodo.

**Il guasto e il nuovo check di fedeltà.** Caso `bi`/1018022: un cliente ha comprato 2 pezzi
contro giacenza 1, perché il payload pubblicato portava `backorders: notify` + `preordine`
+ `supplier_name: nd` su un prodotto a *solo magazzino*. Radice: il commit 25848303
ripristinò un comportamento storico ("presente nei backorders ⇒ fornitore esterno") *dopo*
che il 26-05 il modello dati aveva cambiato significato (la sorgente interna era entrata nei
backorders). Il guasto non vive nel runtime ma nel **gulf of evaluation del ciclo di
sviluppo**: la decisione fu eseguita (commit) ma la sua *assunzione* non fu formalizzata in
`log.md` — visse nel messaggio di commit — quindi mai ri-valutata quando i dati cambiarono.
Da qui un check in `fedelta-cognitiva` ("Decisioni e assunzioni"): una decisione di
compatibilità deve registrare *su quale assunzione poggia*, non solo cosa preserva — "X
presuppone Y; se Y cambia, riaprire". Il caso 1018022 è anche la prima prova empirica,
event-driven, che lo strato input non è simmetria teorica: un `o3` non riconciliato via `i3`
produce drift silenzioso che esplode mesi dopo nel mondo.

**Nota d'implementazione.** I due nodi sono scritti in `L1/L2/L3`, non in `o1/o2/o3`, per
non frammentarli: la conversione la fa in blocco `rifondazione-input-output`, che già lista
`ciclo-azione` tra i file da convertire. Questa stessa voce di log è l'`i3` del ciclo di
sviluppo di oggi — scritta apposta per non ricadere nel guasto che ha appena formalizzato.

## 2026-06-04 — Rifondazione: salto di quota concettuale (artefatto cognitivo)

Sessione di dialogo concettuale, ancora **pre-implementazione** (si seziona prima di
agire). Il task `rifondazione-input-output` è salito di quota: non più "rinominare e
chiudere la simmetria", ma rispondere alla domanda di fondo — *cosa è* l'oggetto che
stiamo costruendo. La risposta riordina tutto il resto e andrà a riscrivere il task.

**Tripartizione (tre parole, tre cose).** Si scioglie la sineddoche "KB = metodo"
distinguendo:
1. *Artefatto cognitivo* (Norman stretto, *Cognitive Artifacts* 1991: dispositivo
   rappresentazionale esterno) = la rappresentazione che si progetta e che persiste —
   KB + strato output + strato input + struttura. È ciò che il metodo coltiva. **È
   portabile**: sopravvive al cambio di modello o di harness.
2. *Sistema cognitivo* (Hutchins, cognizione distribuita) = artefatto + umano + LLM +
   harness, accoppiati. È *dove la cognizione accade davvero*. Non è portabile (contiene
   agenti specifici) e non si progetta come oggetto: emerge dall'uso.
3. *Metodo* = la pratica (il "come") con cui si coltiva l'artefatto perché il sistema
   performi.

**Argomento decisivo per la definizione artefatto-centrica**: la tesi del progetto
("harness portabile, vendor-neutro") è dicibile *solo* se l'artefatto è la
rappresentazione e non il sistema d'interazione. La definizione sistema-centrica toglie
la parola "portabile". L'utente — laureato in interazione uomo-macchina, tradizione
ergonomia cognitiva / cognizione distribuita — tende per formazione a pensare "sistema";
si è convenuto di tenere *entrambi* i concetti ma con nomi distinti, per non perdere ciò
che quella tradizione coglie (la cognizione vive nell'accoppiamento) senza rinunciare
alla portabilità.

**Stack a livelli.** L0 modello → L1 harness tecnico (Claude Code/Codex, sostituibile)
→ L2 = il metodo come *harness cognitivo* portabile e leggibile dall'umano. Norman vive
a L2 (design dell'interazione: visibilità, feedback, mapping, constraint), non a L1
(meccanismo). `agents.md` e i wrapper `.codex` sono già la cucitura L1↔L2.

**L0 è un agente, non un artefatto.** La novità — *l'artefatto che legge* — regge solo
tenendo distinti artefatto (KB) e agente (LLM). Tesi originale che estende Norman: Norman
scriveva per artefatti passivi; qui l'artefatto è letto e rielaborato da una seconda
mente. Il ciclo d'azione va riscritto per due agenti che condividono lo stesso system
image. Conseguenza che chiude un buco: o1 (output macchina) non manca dalla mappatura di
Norman — è il ciclo applicato al secondo agente. Asimmetria dei modelli mentali: per
l'umano la KB è impalcatura esterna a un modello che già possiede; per l'LLM la KB *è*
il modello mentale (riparte da zero ogni sessione).

**Il Goal come confine aperto di Norman.** Il metodo traccia i task (Plan/Specify) ma non
i Goal (il perché). `goal` / `task` / `todo` sono tre *altitudini*, non sinonimi —
disciplinabili con la gerarchia dell'activity theory: motivo (attività) → goal (azione) →
operazione (task). Architettura: i3 (input formalizzato) ha *due* destinazioni, la KB e
la revisione dei goal — è il Compare→nuovo Goal di Norman. Decisione: **non** rinominare
`todo/`→`goals/` (nasconderebbe il concetto e mentirebbe sul contenuto attuale); scrivere
il *nodo* sul Goal e lasciare emergere l'apparato quando il lavoro lo richiede.

**Struttura nodi propensa (taglio B + cerniera)**: `artefatto-cognitivo`,
`sistema-cognitivo` (cerniera, dove vive l'asimmetria dei modelli mentali), nodo `goal` /
gerarchia dell'azione; `ciclo-azione` riscritto come ciclo a due agenti.

**Decisioni che superano l'entry precedente**: la lingua del repo è **inglese** (non più
"aperta"). Servono *più libri di Norman*, non solo DOET: "cognitive artifact" e cognizione
distribuita vengono da *Things That Make Us Smart* (1993). L'ingest dei libri di Norman
diventa un **task separato** (`todo/ingest-norman.md`), candidato a essere il primo pilota
reale dello strato input.

**Forma del ciclo: due cerniere, non uno specchio** (scioglie il filo del "mirror").
La struttura di Norman non è uno specchio (i3 ↔ o1) ma un *cappio con due cerniere*. Il
Goal è l'apice (sta sopra entrambi i gulf), il Mondo è il fondo; l'esecuzione (Q2 Plan,
Q3 Specify = o2 → Q4 Perform = o3) è la discesa, la valutazione (Q5 Perceive = i1 → Q6
Interpret = i2 → Q7 Compare = i3) è la risalita. Le due cerniere:
- **Mondo** (Q4→Q5): o3 agisce, i1 percepisce — stesso luogo, due versi: *simmetrico*.
- **KB** (Q7→Q1): l'apice. i3 *scrive* l'esito nella KB; il Goal *legge* l'intenzione
  dalla KB. Scrivi-poi-leggi, non riflesso. L'asimmetria al confine KB è **feature**: la
  KB è la memoria persistente dove il ciclo si chiude.
o1 non sta su questo arco — vive sul ciclo del *secondo agente* (l'LLM che legge la KB
per agire), che ha un proprio lato-input macchina (audit, lint, errori, test). Due cicli,
uno per agente, stessa KB all'apice. Va disegnato così in `ciclo-azione` e nel mermaid
"ciclo che si chiude" (sostituisce le due colonne speculari). Cautela di fedeltà sul Goal:
la KB *informa e raffina* il Goal, non lo *genera* — il Goal nasce all'incrocio motivo
(da sopra) + KB; è l'estensione di Norman "sul Goal".

**Gradiente di autonomia e passaggio di consegne** (concetto nuovo, forse il più
originale). Il repo versionato è la *traccia* di un passaggio di consegne graduale
umano→LLM: git registra la delega progressiva mentre l'harness di guardrail e
autocorrezioni si accumula. Traiettoria human-in → human-*on* (controllo supervisorio,
Sheridan) → human-out, dove la fase "on" è la più insidiosa — *ironie dell'automazione*
(Bainbridge 1983): le skill si atrofizzano e la ripresa del controllo è richiesta proprio
quando è più difficile. L'autonomia non è uno slider unico ma un *profilo per stadio del
ciclo* (livelli di automazione, Parasuraman/Sheridan) e dipende da **quanto del motivo è
esternalizzabile nell'artefatto**. Gradiente sui quattro repo: `nixos` (motivo
codificabile → autonomia alta) → `bi`/`economia` (media, gate umani obbligatori) →
`salute` (motivo non esternalizzabile → supervisione permanente). Il README di ogni
progetto dovrebbe dichiarare scopi generali + grado di autonomia attuale/aspirato.
Conseguenza che ribalta l'obiezione bottom-up sul lato input: **il lato valutazione
(i1→i2→i3) è il meccanismo di sicurezza che rende possibile l'uscita dell'umano dal
loop** — non simmetria teorica ma load-bearing. o2 non sparisce con la fine dei PDF: si
trasforma in *spiegazione resa su richiesta*, perché per le decisioni ad alta posta
l'umano deve *capire* (formarsi un modello mentale), non solo interrogare — altrimenti
perde la capacità di valutare. (Fonti: il "flusso" è di Csikszentmihalyi, Norman lo
adotta.)

**Due principi dell'arco di input (dal caso economia, bottom-up).**
1. *i2 goal-guidato sulla rilevanza, neutro sulla valenza.* I goal scelgono legittimamente
   cosa mostrare, granularità, confronti (rilevanza), mai il verdetto buono/cattivo
   (valenza), che è compito di i3. Test: due persone con goal di valenza opposta devono
   produrre lo *stesso* i2 e dissentire solo a i3; se i2 differisce già nel giudizio,
   l'artefatto non ospita una valutazione, riflette il bias. i2 = rappresentazione
   condivisa e contestabile; i3 = dove avviene il contrasto (cruciale nel multi-stakeholder,
   es. conti personale/comune di due partner in `economia`). Pattern già presente in
   `salute/quadro`: i numeri = i2, il termometro/colore = i3. Un i2 goal-saturo distrugge
   il gulf of evaluation e annulla la funzione di sicurezza dell'arco di input — l'artefatto
   non può più portare cattive notizie.
2. *L'arco di input è più ampio dell'arco di valutazione di Norman.* i1 ha due sorgenti:
   feedback (risposta a o3, chiude un goal esistente, Norman puro) ed esogeno (il mondo
   agisce da sé — busta paga, normativa, alert — apre spesso un goal nuovo). Quindi i3 ha
   due modi: verdetto (Compare contro goal esistente) e triage/formazione-goal (per
   l'esogeno). Conseguenza autonomia: *delega la chiusura di loop noti, tieni l'umano per
   l'apertura di loop nuovi* (il triage dell'esogeno = decidere cosa conta = formazione del
   goal, la cosa meno esternalizzabile; eco di Bainbridge). Il metodo apre il confine-Mondo
   (il mondo non solo risponde, agisce) come apre il confine-Goal: estensione di Norman a
   entrambi gli estremi.

**Metodo di sviluppo del metodo (concordato).** Validare i concetti teorici calandoli
bottom-up nei quattro domini, ognuno banco di prova di una parte diversa: `economia`
(multi-stakeholder, irreversibilità, valenza), `salute` (motivo non esternalizzabile,
corpo), `nixos` (autonomia alta, determinismo, feedback-heavy, poco esogeno), `bi`
(decisioni condivise, input esogeno dai colleghi). `nixos` e `bi` sono quasi opposti
sull'asse feedback/esogeno — il confronto valida la criticità 2. Più si cala la parte poco
chiara in un dominio, più si illumina l'intero.

**Anti-dogma per costruzione.** Ciò che va "scritto nella pietra" non sono i verdetti
(output di i3, sempre revisionabili) ma i *meccanismi di autocorrezione* (i2 neutro sulla
valenza, input come intake del mondo): sono ciò che tiene l'artefatto capace di smentire i
propri goal e di ascoltare il mondo che agisce. La pietra è l'impegno a restare corrigibili,
non le conclusioni. Mappa sulla distinzione che il repo già ha: metodo/nodi stabili (pietra)
vs goal/valutazioni revisionabili (fluido).

**Fili ancora da sezionare** prima di riscrivere il task: il sottoscoping dei file da
aggiornare (`pattern-karpathy`, `knowledge-base`, `mappa` sono riscritture concettuali,
non solo link); lo stato bozza/maturo e la dipendenza con `salute/quadro/` tracciata in
`confronto-progetti-adottanti`; la trappola del grep ("ponte" è anche metafora viva in
`agents.md`, `mappa.md` e nei `project-map` dei repo adottanti — non sostituire ciecamente).

**Nota di metodo (dogfooding su me stesso)**: in questa sessione avevo salvato gli appunti
concettuali nello store di memoria dell'harness (`~/.claude/`). È l'anti-pattern
dell'artefatto portabile — host-locale, opaco, non versionato. Rimossi; la regola "la
memoria del progetto vive versionata nel repo" è ora in `CLAUDE.md` (sezione `## Memoria`),
e questi appunti vivono qui, dove dovevano stare.

---

## 2026-06-04 — Rifondazione input/output: pianificazione e formulazioni fondative

Sessione di pianificazione metodologica con tre prodotti concreti: frontmatter PDF,
strategia di condivisione con Luigi, task rifondativo aperto.

**Firma PDF**: aggiunto frontmatter YAML a `presentazione/metodo-in-sintesi.md`
(title, subtitle, author, date). Il template LaTeX esistente in `nixos/modules/home/md2pdf.nix`
gestisce già `\maketitle` condizionale — nodi senza frontmatter non sono influenzati.

**Strategia GitHub aziendale**: definiti tre livelli di accesso (metodo pubblico,
`bi` in sola lettura ai colleghi, nixos/salute/economia privati). Redatta email a Luigi
per invitarlo a creare un account GitHub personale — solo il primo passo, senza condividere
il metodo finché non dà un segnale concreto di interesse reale.

**Task rifondativo** `todo/rifondazione-input-output.md`: il task più denso aperto finora
in questo repo. Tre questioni operative (rename ponte→output, L1/L2/L3→o1/o2/o3, lingua
italiano→inglese) e una ristrutturazione concettuale profonda. Le formulazioni fondative
emerse durante la sessione, da usare come apertura dei nodi riscritti:

*I tre giganti rispetto alla KB*: Luhmann è la KB — Karpathy governa la KB — Norman
connette la KB al mondo. Più preciso dell'attuale "si dividono il lavoro in modo nitido":
dice dove ognuno lavora, non solo cosa porta.

*Il metodo come estensione di Norman*: Norman dà per scontati due elementi ai confini
del ciclo — il Goal e il Mondo. Il metodo interviene su entrambi: la KB è il luogo dove
i goal si formano (non sono dati); lo strato input governa come il Mondo entra nel sistema
(non è una scatola nera). Il metodo non applica Norman: lo estende verso i suoi estremi
irrisolti.

*KB come sineddoche del metodo*: "KB" viene usata spesso quando si intende il sistema
intero. La KB in senso stretto è solo i nodi in `kb/`. Durante la riscrittura in inglese:
"the method" per il sistema intero, "the KB" solo per i nodi di conoscenza.

*Base empirica degli strati input*: il pattern di ingest non governato esiste già nei
quattro repo — estratti conto e referti in `economia` e `salute`, errori e alert in
`nixos`, segnalazioni dei colleghi in `bi`. La formalizzazione i1/i2/i3 è bottom-up.

Tre decisioni aperte nel task: nomenclatura (input/output vs esecuzione/valutazione),
lingua (italiano vs inglese, propensione per l'inglese per fedeltà cognitiva alle fonti),
strato input come componente obbligatorio o opzionale.

---

## 2026-06-03 — Revisione qualitativa profonda dei nodi e strato output del metodo

Revisione semantica di tutti i 25 nodi, oltre il lint strutturale (sempre pulito).
Diagnosi: KB matura e coerente, ma sovradimensionata e ridondante rispetto al suo
stesso scopo (portabilità, basso costo di comprensione). Ironia di fondo: il
metodo predica fonte-unica-di-verità e "la sintesi vive nel ponte perché la KB
resti pura", ma violava entrambe le regole su sé stesso. Intervento in quattro
passaggi, un commit ciascuno.

Pass 1 — dati cross-repo centralizzati in `confronto-progetti-adottanti`. I
conteggi per repo (nodi, link, righe CLAUDE, task, audit datati) erano duplicati
e già stantii in `strumenti-kb`, `indice`, `task-aperti`, `claude`, `agents`:
mini-fotografie sparse che nessuno risincronizzava. Tolti i numeri fragili,
lasciata la lezione qualitativa.

Pass 2 — de-duplicati i blocchi concettuali ripetuti, con case canoniche: tre
giganti → `ciclo-azione`, L1/L2/L3 e conflitto Zettelkasten/Karpathy → `ponte`,
esposizione strumenti → `strumenti-kb`, quattro proprietà di Norman →
`ciclo-azione`. Altrove: ruolo proprio del nodo + rimando, niente
ri-derivazione. Applicata fonte-unica anche ai concetti, non solo ai dati.

Pass 3 — `struttura-progetto` (146→112 righe) ripeteva liste di regole con nodo
dedicato (`Regole AGENTS/CLAUDE/todo`, `Sezioni README`). Keep/relocate/remove:
bullet unici spostati in `claude`, liste sostituite da pointer. Il nodo resta
overview dei pilastri; i criteri di revisione vivono nei nodi-casa. Nessun nodo
rimosso: `agents` e `git-history` restano sottili ma con funzione distinta, e lo
stato `bozza` lo segnala onestamente.

Pass 4 — creato il primo strato output del repo `metodo`:
`presentazione/metodo-in-sintesi.md`, cinque diagrammi Mermaid (tre giganti,
ciclo dell'azione, anatomia del progetto, sviluppo bottom-up, routing dei
contenuti). Dogfooding: il metodo applica il proprio principio `ponte` a sé
stesso — la sintesi vive nello strato output, non in un nodo `kb/`. Il file
dichiara anche L1/L2/L3 del repo metodo. Era l'L2 mancante: il metodo descriveva
sé stesso solo a parole, senza una vista a colpo d'occhio.

---

## 2026-06-03 — Seconda fotografia dell'osservatorio

Rinfrescato `confronto-progetti-adottanti` dopo che la prima fotografia (2026-05-23)
era invecchiata di 11 giorni mentre i repo adottanti continuavano a muoversi.
La rilettura è funzione di osservatorio (lettura dei repo), non orchestrazione,
quindi coerente col flusso bottom-up.

Cosa è cambiato dai dati reali: `economia` è cresciuta (51→55 nodi, 184→198 link)
e ha audit pulito — i "segnali strutturali da correggere" del vecchio nodo erano
ormai falsi; `bi` ha chiuso due task (todo 9→7) restando stabile a 84 nodi;
`nixos` e `salute` invariati nei numeri. Aggiornate le tre tabelle del nodo
(stato, dati strutturali, azioni suggerite) e marcate come completate le azioni
ormai concluse (bi CLAUDE, salute mappa, economia audit).

Due osservazioni metodologiche registrate nel nodo. Primo: i 10 file accentati di
`salute` (`realtà.md`, `qualità.md`, …) sono un default strumentale che non aderisce
al dominio, non un drift — la regola "niente accenti nei nomi" è convenzione tecnica
che una KB riflessiva italiana può legittimamente non seguire; resta decisione locale.
Secondo: `ponte` e `ciclo-azione` sono ancora `stato: bozza` per scelta, non per
dimenticanza — la promozione a maturo è un filing back atteso dal pilota
`salute/quadro/` quando produrrà 2-3 cicli L2→L3→fonte→KB documentati.

Conferma operativa: l'osservatorio si ricostruisce a mano in poche query
(`kb_tools.py audit` per repo), quindi un report cross-repo automatico resta non
necessario finché il costo non cresce — niente task preventivo, in linea bottom-up.

---

## 2026-06-01 — Formalizzazione sviluppo bottom-up del metodo

Formalizzato nei nodi centrali il principio emerso dalla revisione dei task:
lo sviluppo del metodo è bottom-up. Una modifica metodologica nasce da
un'esigenza concreta in un repo adottante, viene risolta lì nel merito, poi viene
riportata in `metodo` solo se produce una generalizzazione portabile. Gli altri
repo adottanti recepiscono la modifica leggendo i commit del metodo e applicando
localmente ciò che è pertinente.

Aggiornati `metodo-kb`, `osservatorio-metodo`, `task-aperti`, `todo` e README.
La conseguenza operativa è che `metodo/todo/` non è una backlog board
cross-repo: i task qui devono riguardare il metodo stesso, la sua presentazione,
la coerenza dei nodi, strumenti comuni già giustificati o generalizzazioni
emerse dall'uso reale.

---

## 2026-06-01 — Chiusura task residui e triade skill ufficiale

Chiusi gli ultimi due task aperti in `metodo`. Il task `Confronto skill
audit-kb e commit cross-repo` è stato assorbito nella formalizzazione della
triade ufficiale `audit-kb` / `revisione-tasks` / `commit` in `kb/skill.md`: non
serve mantenere un task separato di confronto perché i quattro repo adottanti
espongono già la triade con parametrizzazioni locali.

Chiuso anche `Superficie portabile kb_tools.py: comandi avanzati` senza
implementazione centrale. I comandi avanzati come `facts`, `fidelity`,
`coverage` e `inventory` restano locali finché un bisogno concreto in un repo
adottante non produce una generalizzazione bottom-up. Il repo `metodo` non
mantiene più task preventivi su strumenti nati in un singolo repo.

Il README ora registra nessun task aperto. Questa è la forma desiderata per il
repo `metodo`: entrare qui raramente, per ristrutturare, semplificare o custodire
generalizzazioni già emerse dai repo adottanti.

---

## 2026-06-01 — Skill revisione-tasks applicata ai repo adottanti

Chiuso il task `Portabilità skill revisione-tasks` applicando subito il pattern
a tutti i repo adottanti. `economia` resta il caso originario; `nixos`, `bi` e
`salute` hanno ora una skill `.claude/skills/revisione-tasks` con wrapper Codex
corrispondente, discovery in README e riga operativa in CLAUDE.md.

La decisione metodologica è che la funzione è comune, ma la skill vive locale:
ogni repo deve rivedere task, priorità e dipendenze rispetto ai propri segnali
concreti. `kb/skill.md` registra quindi la triade comune `audit-kb` /
`revisione-tasks` / `commit`, senza introdurre un task centrale top-down.

---

## 2026-06-01 — Task file locali di dominio spostato in economia

Spostato il task `Formalizza pattern file-dominio` dal repo `metodo` al repo
`economia`, dove ora vive come `todo/file-locali-dominio.md`. Il criterio sui
componenti locali di dominio deve nascere dall'uso concreto di `stato.md`,
`scadenze.md` e `diario.md`; `metodo/kb/struttura-progetto.md` riceverà solo il
filing back se il pattern si dimostra portabile.

Questa chiusura segue la stessa regola bottom-up adottata per `salute/quadro/`:
il repo adottante produce l'evidenza, il repo metodo custodisce la
generalizzazione.

---

## 2026-06-01 — Task pilota quadro spostato in salute

Spostato il task `Osservazioni dal pilota salute/quadro/` dal repo `metodo` al
repo `salute`, dove ora vive come `todo/osservazioni-quadro-pilota.md`. La
verifica richiede uso reale del quadro, raccolta di cicli L2 -> L3 -> fonte ->
KB -> quadro e osservazione delle decisioni locali; tenerla in `metodo` la
rendeva un controllo top-down su un repo adottante.

In `metodo` resta solo la destinazione del filing back: `kb/ponte.md` dovrà
essere aggiornato se dal pilota di `salute` emergeranno criteri portabili sullo
strato output. Questa chiusura rafforza la regola operativa bottom-up: il repo
adottante produce l'evidenza, il repo metodo custodisce la generalizzazione.

---

## 2026-06-01 — Chiusura task README narrativo salute

Chiuso il task centrale `README narrativo di salute: quando è accettabile?`
senza lavorarlo da `metodo`. Il task era formulato come verifica top-down sul
README di un repo adottante; secondo la direzione bottom-up emersa nella
revisione dei task, una revisione del README di `salute` deve nascere dentro
`salute` da un problema concreto di bootstrap, orientamento o drift.

Se da quel lavoro locale emerge un criterio generalizzabile sulla narratività
dei README in domini riflessivi, il filing back corretto sarà aggiornare
`kb/readme.md` in `metodo` dal repo adottante, non mantenere qui un task di
controllo preventivo su `salute`.

---

## 2026-06-01 — Chiusura regress check CLAUDE.md BI

Chiuso il task `Regress check CLAUDE.md bi` dopo verifica della storia locale
di `../bi`. Il commit `b195b8ff` (`docs(kb): compatta CLAUDE e chiudi task
metodo`) ha eliminato il task locale `todo/revisione-claude-md.md`, rimosso la
riga dal README di BI e registrato in `log.md` la riduzione di `CLAUDE.md` da
manuale esteso a costituzione operativa. Il commit successivo `a78091c1` ha
aggiunto solo la tabella operativa degli strumenti propagata da `~/metodo`, non
un ritorno alla documentazione narrativa di dominio.

Il criterio quantitativo indicato nel task centrale (`~100 righe`) era troppo
rigido rispetto al caso reale: già dopo la chiusura locale BI `CLAUDE.md` era a
162 righe, e oggi è a 187 per effetto della tabella strumenti. La soglia utile
resta qualitativa: `CLAUDE.md` non deve tornare manuale parallelo alla KB.

---

## 2026-05-29 — Filing back da economia: audit pulito non basta

La revisione di `economia` ha mostrato un drift non rilevato dall'audit
strutturale: il README indicizzava nodi metodologici condivisi come se fossero
contenuto locale, pur avendo link validi e audit 0/0/0. Il metodo viene chiarito:
i progetti adottanti devono dichiarare il repo `metodo` come dipendenza
trans-repo e tenere separati indice locale, mappa del dominio e contenuto
metodologico condiviso.

Aggiornati `fedelta-cognitiva`, `skill`, `readme` e `indice`: `audit-kb` fotografa
lo stato e deve includere una revisione qualitativa di README/CLAUDE/mappa;
`commit` è il gate più capillare per prevenire drift, perché impone il filing
back prima che una modifica venga fissata nella storia.

La stessa sessione ha chiarito anche la regola di esposizione degli strumenti:
devono essere scopribili nel README, operativi in CLAUDE.md e approfonditi nei
nodi. Questa tripartizione aumenta la consapevolezza dell'LLM senza trasformare
README o CLAUDE in manuali duplicati.

---

## 2026-05-24 — Rafforzamento operativo dello strato output

Il pilota `salute/quadro/` ha chiarito un criterio che mancava al nodo `ponte`: uno strato output non è maturo quando ha file ben formattati, ma quando lascia traccia di cicli completi L2→L3→fonte→KB→quadro. Aggiornato `kb/ponte.md` con la dichiarazione minima dello strato output (L1 macchina, L2 decisione, L3 azione, fonte di ritorno, criterio di aggiornamento) e con il segnale empirico di maturità: osservare almeno 2-3 cicli completi.

Aggiornato il task `salute-quadro-pilota` per trasformarlo da osservazione passiva del pilota a verifica attiva: registro azioni, prossime decisioni, fonti prodotte e ritorno nel quadro. La maturazione del metodo passa ora dall'uso reale di `salute/quadro/azioni.md`.

---

## 2026-05-24 — Creazione di `ponte` e `ciclo-azione`: tre giganti riconosciuti

Promossi al meta i due nodi previsti dal task `ponte-teoria-pratica`. `ponte.md` formalizza lo strato output del metodo: i tre livelli L1 macchina, L2 decisione umana, L3 azione nel mondo; la risoluzione del conflitto Zettelkasten/Karpathy (la sintesi vive nello strato output, non nei nodi); il ciclo che si chiude attraverso l'azione; lo stato dei quattro progetti adottanti.

`ciclo-azione.md` distilla il modello del ciclo di azione di Donald Norman: i sette stadi (Goal → Plan → Specify → Perform → Perceive → Interpret → Compare), i due gulf (execution, evaluation) come metriche delle distanze cognitive, le quattro proprietà cardine (visibilità, feedback, mapping, constraint) come criteri di qualità per L2. Introduce Norman come terzo gigante del metodo accanto a Luhmann (atomicità del nodo) e Karpathy (manutenzione LLM).

Aggiornati i README di `metodo` e di `salute` per citare i tre giganti. Aggiornato `confronto-progetti-adottanti.md` per registrare la promozione dello strato output da "componente locale aggiuntivo" a "componente universale con forme locali". Filing back: il file `salute/quadro/quadro-corporeo.md` linka ora i due nuovi nodi metodologici (dal locale verso il meta), pattern che diventa parte del metodo stesso.

Una formulazione che resta come fondamento: lo strato output esiste perché il KB possa restare puro. È la sua condizione di possibilità, non un'aggiunta opzionale.

Provocazione utile da Norman, ripresa nel nodo `ciclo-azione`: se l'utente non agisce, la KB è mal progettata, non l'utente è pigro. Lo strato output va dunque valutato sui criteri di Norman, non sulla bellezza dei nodi.

I due nodi sono in stato bozza. Maturazione attesa con l'uso reale del pilota in `salute`.

---

## 2026-05-24 — Strato output e terzo gigante Norman

Sessione cross-repo nata in `salute` con ricadute meta importanti. La riflessione ha riconosciuto una funzione cognitiva universale del metodo finora implicita: lo strato di OUTPUT, distinto dalla KB. Tre formulazioni stabilizzate.

Prima: il conflitto Zettelkasten/Karpathy sulla sintesi (atomicità vs pagine di sintesi nel wiki) si risolve separando KB e output. La sintesi vive nello strato output, non nei nodi. **Lo strato output esiste perché il KB possa restare puro.** Risolve anche pressioni attualmente visibili in alcuni nodi (es. `salute/kb/storia-clinica.md`, diventato di fatto un dashboard improprio).

Seconda: l'output universale ha tre livelli. L1 — macchina (JSON, dati strutturati, `.nix`), L2 — decisione umana (schemi, diagrammi, slides, termometri), L3 — azione nel mondo (email, parole dette, gesti corporei, transazioni). L3 ritorna come fonte chiudendo il ciclo. Stato attuale dei quattro progetti adottanti:

- `nixos`: L1 forte (`home/`, `hosts/`, `modules/`), L2 debole (architettura solo come testo in `kb/`), L3 forte (sistema in esecuzione)
- `bi`: forte su tutti i livelli (scripts notturni + `presentazione/` Reveal.js + decisioni business)
- `economia`: L1 forte (`output/json/`), L2 medio (`output/report*.md` solo tabelle), L3 forte (email, riunioni famigliari)
- `salute`: L1 implicito sparso, L2 assente (l'SVG su Drive era un proto-output fuori repo), L3 medio-forte

Pattern emergente: dove L2 è forte (`bi`) il progetto serve decisioni condivise con altri; dove è debole resta personale e introspettivo, e fatica a generare azione coordinata.

Terza: Donald Norman è il terzo gigante del metodo accanto a Luhmann e Karpathy. Il modello dei sette stadi e i due gulf (execution, evaluation) descrivono precisamente come L1/L2 servono L3. Le quattro proprietà cardine (visibilità, feedback, mapping, constraint) diventano criteri di qualità per L2. Provocazione utile: una KB con poche affordance e nessun feedback è mal progettata, non è la persona pigra.

Decisione: pilota prima in `salute/quadro/`, formalizzazione meta dopo. Aperto il task gemello `ponte-teoria-pratica` in `todo/`, con dipendenza esplicita dal pilota di salute. I due nodi che nasceranno in `kb/` sono `ponte.md` (lo strato, risoluzione Zettelkasten/Karpathy, tre livelli, ciclo chiuso) e `ciclo-azione.md` (distillazione metodologica di Norman, gemello formale di `pattern-karpathy.md`, non biografia). Aggiornamenti collaterali previsti: `confronto-progetti-adottanti.md` per promuovere l'output da "componente locale" a universale, e `metodo-kb.md` per citare i tre giganti.

---

## 2026-05-24 — Osservatorio salute chiuso

Chiuso il task `osservatorio-salute`: nel repo `salute` sono stati creati
`kb/mappa-progetto.md`, `kb/principi-salute.md` e
`kb/verifica-nel-vivere.md`, con aggiornamento di README, CLAUDE e log locali.

Il caso conferma tre regole metodologiche. Primo: le verifiche cross-repo
restano nel repo `metodo`, ma quando producono contenuto di dominio diventano
task locali. Secondo: per KB riflessive la mappa non deve simulare una mappa
tecnica; deve collegare assi concettuali, fonti, pratica e diario. Terzo:
README-only è accettabile per ingest semplici, mentre interventi strutturali o
serie di nodi richiedono `todo/` finché non vengono stabilizzati in nodi.

## 2026-05-22 — Fondazione del repo

Creato il repo `~/metodo` come fonte unica di verità per i nodi metodologici,
consolidando le versioni sparse in nixos, bi, economia e salute.

La versione nixos era la più evoluta su tutti i nodi. Il diff ha rilevato tre
contributi non banali dagli altri repo:

- `struttura-progetto`: da economia, aggiunta la nozione di "README come
  artefatto a doppia audience" e "revisione-tasks come chiusura sessione"
- `strumenti-kb`: da economia, aggiunto il dettaglio "tre livelli
  (errore/avviso/info)" nell'output di audit
- `fedelta-cognitiva`: generalizzato il livello fattuale per renderlo
  domain-agnostic; aggiunta sezione "Adattamento al dominio" con economia come
  esempio di adattamento al dominio legale/finanziario

`design-principles.md` è stato scritto ex novo unificando i due approcci
divergenti di nixos (ingegneria del codice) e bi (affidabilità dei sistemi
dati) in un documento stratificato: principi universali + principi code-based +
principi specifici di progetto nel README locale.

I nodi zettelkasten, connessione e pattern-karpathy erano identici in tutti i
repo: copiati verbatim.

Fase A.2 (symlink + pulizia locale) e Fase B (strumenti cross-repo) restano
task aperti in `~/nixos/todo/metodo-repo-centralizzato.md`.

---

## 2026-05-23 — Metodo KB come hub della ricetta metodologica

Riorganizzato `kb/metodo-kb.md` per eliminare la ripetizione tra componenti
portabili, skeleton minimo e prompt di creazione. L'inventario ora compare una
sola volta come "Ricetta metodologica"; le altre sezioni descrivono creazione,
criteri di separazione e varianti osservate nei progetti adottanti.

La revisione conferma che non serve ancora creare un nodo autonomo per ogni
componente: `nodo`, `struttura-progetto` e `strumenti-kb` sono gia separati
perche hanno regole proprie, mentre README, CLAUDE, AGENTS, log e todo restano
componenti strutturali descritti dall'hub finche non accumulano semantica
riusabile piu ampia.

Aggiunto `AGENTS.md` al repo metodo per allineare il repository alla propria
ricetta minima: wrapper breve, ordine di lettura esplicito, nessuna duplicazione
delle regole operative.

Aggiunto `scripts/kb_tools.py` come backend portabile: comandi base per audit,
backlink, orfani, README, migrazione e termini candidati; comandi generici
`inventory` e `coverage` per progetti code-based. I controlli di fedelta
specifici di dominio restano estensioni locali nei progetti adottanti.

Formalizzata la funzione del repo metodo come osservatorio cross-repo in
`kb/osservatorio-metodo.md`. Il repo non conserva solo il metodo generale, ma
osserva periodicamente come il metodo viene incarnato nei progetti adottanti:
README, CLAUDE, AGENTS, log, todo, nodi, strumenti, skill, fonti di verita e
salute complessiva delle KB. Il task cross-repo esistente e stato ampliato come
prima implementazione operativa dell'osservatorio.

Aggiornato il README con il titolo `Metodo KB` e con l'inquadramento a doppia
funzione: metodo portabile e osservatorio cross-repo. L'apertura ora esplicita
che le differenze tra progetti sono materiale di analisi per decidere cosa
generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Espanso `kb/metodo-kb.md` con un indice cognitivo del metodo e creati nodi
bozza per tutti i componenti della ricetta che non avevano ancora un nodo
autonomo: AGENTS, CLAUDE, README, indice, task aperti, mappa, todo, log, git
history, skill e fonte di verita. La scelta rende esplicito che il metodo e un
work in progress pratico: i componenti non maturi possono essere descritti,
collegati, confrontati tra repo e fatti maturare nel tempo.

---

## 2026-05-24 — Revisione task come funzione strutturale di sessione

Generalizzata l'intuizione emersa da `economia`: la revisione dei task non e
solo un adattamento locale per scadenze e pratiche aperte, ma una funzione
strutturale del metodo. Le sessioni LLM pianificano, analizzano e implementano
lavoro attraverso task espliciti; se README e `todo/` driftano, la sessione
parte da una supervisione falsa.

Aggiornati i nodi `task-aperti`, `claude`, `skill` e `struttura-progetto` per
distinguere tra funzione obbligatoria e implementazione locale: ogni progetto
deve avere un controllo leggero dei task nel bootstrap operativo; una skill
dedicata `revisione-tasks` diventa opportuna quando i task sono numerosi,
dipendono da fonti/scadenze esterne o il drift produce costo reale di sessione.

Formalizzata anche la governance dei task metodologici cross-repo: vivono nel
repo `metodo` e di norma hanno precedenza sui task di progetto. Anche quando
targettano un singolo repository, restano centrali finche il motivo del lavoro e
metodologico; un task locale nasce solo quando l'intervento diventa autonomo di
dominio. Di conseguenza la verifica su `nixos`, `bi` e `salute` resta nel task
cross-repo centrale con matrice per repository, mentre `economia` resta il caso
guida gia allineato.

La coda metodologica e stata poi divisa in task centrali specifici per repo:
`osservatorio-bi`, `osservatorio-economia`, `osservatorio-nixos` e
`osservatorio-salute`. Il vecchio task unico di valutazione cross-repo e stato
rimosso per rendere le priorita ordinabili per target senza duplicare lavoro nei
repo adottanti.
