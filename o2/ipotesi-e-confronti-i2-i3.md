---
sintesi: "Provare un laboratorio delle ipotesi nella collezione i2 di ogni adottante: file autonomi classificati tramite tipo: sintesi|ipotesi, riscontri, revisioni e scioglimento propri; i3 conserva i confronti contro il Goal. Prototipi su economia e nixos, perimetro sugli altri cinque adottanti, riesame tramite eval e permanenza degli esiti utili. Misurare separatamente le perdite nella potatura dei sedici fili originari; consegnare un modello verificato senza incidere il canone."
ciclo: dev
---

# Ipotesi e confronti i2/i3

Task di prova, non di migrazione. Nato il 2026-10-04 dalla revisione della
presentazione e separato lo stesso giorno dalla migrazione delle viste, ora
chiusa nel canone e prescritta ai sei (`o3/migrazione-viste.md`): liberare i2
dal deck non dice ancora che cosa i2 debba custodire, e la risposta va provata
sui casi prima di diventare obbligo canonico. Dall'esito dipende il seguito
tracciato di quella prescrizione, la revisione del deck di `nixos`, che
mescola racconto dell'artefatto e lettura del boot. Il prodotto è un modello
sottoposto al custode; canone, ristrutturazione di `metodo` e prescrizione
agli adottanti nascono come task propri solo dopo la ratifica.

## Il problema

Il canone assegna già a i2 letture, assunzioni e incertezza, ma non
esplicita il contratto per rendere raggiungibili le **convinzioni sul Mondo
ancora esposte alla prova**, riesaminarle sui riscontri e conservarne gli
esiti utili. Le pratiche esistono: previsioni in `economia`, spiegazioni del
boot in `nixos`, un'ipotesi con precursore e scadenza in `danea-auto`,
letture esplorative in `salute`.

Due bisogni si misurano separatamente: il presidio incompleto delle ipotesi e
l'eventuale perdita di letture nelle potature recenti — `5ea8204` in `metodo`
(sedici fili ridotti a cinque); nei sei adottanti di allora i file i3,
cursore compreso, sono passati da 37 a 19 (riconteggio del 2026-10-05 sui
commit di potatura elencati nei casi). Una potatura corretta non smentisce il
bisogno di riesame osservato altrove.

## Il modello da verificare

La revisione con il custode del 2026-10-04 ha concordato la direzione;
cardinalità, schema e ciclo di vita si provano sui casi.

### i2 legge, i3 confronta

- **i2 rende concreta la lettura**: evidenze e provenienza, chiavi
  interpretative, ipotesi, alternative, assunzioni e limiti. Il Goal ne
  orienta la rilevanza, ma spiegare o prevedere non equivale a giudicare il
  successo. Un'ipotesi dichiara che cosa accade o accadrà e da quale
  osservazione lo si saprebbe; il suo esito registra lo stato del riscontro,
  non un giudizio favorevole o sfavorevole.
- **i3 governa i confronti**: le questioni valutative vive, collegate alle
  letture i2, con obiettivo, giudizio corrente e condizione di riesame. Il
  confronto porta la sintesi valutativa: che cosa la lettura significa per lo
  scopo, quale tensione rivela, quali conseguenze propone per l'azione o per
  il Goal, compresa l'aggiunta, la rettifica o la ridefinizione di un
  obiettivo. La modifica del Goal resta una decisione del custode, resa
  esplicita nel register. L'ordine dei confronti esprime priorità di
  attenzione; il plan mantiene la priorità dell'azione, e una questione può
  essere importante senza autorizzare ancora nessuna mossa.
- **Il legame è esplicito, la biunivocità non è presupposta**: ogni confronto
  raggiunge il materiale che lo sostiene; una sintesi può alimentare più
  confronti o restare utile senza un confronto aperto. Ogni ipotesi che
  attende verifica è raggiungibile dal presidio di `eval` anche senza
  scadenza né riga i3: il contratto impedisce ipotesi dimenticate senza
  creare confronti fittizi per completare una coppia.
- **Verifica e chiusura sono distinte**: chiudere un task, stabilizzare un
  giudizio operativo e confermare una spiegazione sono eventi diversi.

La simmetria o1↔i3, o2↔i2 è funzionale: impegni d'azione e di valutazione,
specifiche dell'azione e letture del Mondo. Non impone di stringere il
contratto plan×o2 né di ridurre tutti gli stadi a file Markdown: in `bi`
esistono anche prodotti automatici runtime i2 e i3.

### Oggetti della collezione

Il laboratorio delle ipotesi vive nella collezione esistente `i2/` di ogni
adottante, senza imporre ipotesi da produrre né una nuova collezione: una
collezione senza ipotesi correnti è legittima. Il nome comune è «ipotesi»; il
nome scherzoso della pratica di `economia` non entra nel modello.

- **Facet `tipo: sintesi|ipotesi`**, a valori chiusi e singola per file,
  accanto a `ciclo: dev|runtime`, dichiarata nel canone e verificabile dagli
  strumenti. Oggi non esiste: è una proposta, non un controllo implementato.
  L'indice esistente rende raggiungibili entrambi i tipi; le viste possono
  selezionare le ipotesi dai metadati.
- **L'unità del presidio è l'ipotesi, non il file.** Ogni ipotesi ha un
  identificativo stabile, il file stesso o un'ancora, che `eval`, i
  collegamenti e le letture dipendenti citano. Un contenitore `tipo: ipotesi`
  ne ospita una o più; un'ipotesi presidiata vive solo lì, così la selezione
  per `tipo` trova tutti i contenitori senza imporre un file per ipotesi.
- **Gradiente.** Una sintesi può porre domande e ipotesi esplorative in
  prosa, ma non ospita ipotesi presidiate. Una lettura diventa presidiata
  quando richiede riscontri, revisioni e criteri di scioglimento propri o
  condiziona decisioni nel tempo: riceve una casa perché quelle decisioni
  dipendono dal suo riscontro, non perché la giudichi. L'orizzonte è una
  proprietà possibile, non il requisito per avere una casa.
- **Metadati per ipotesi.** `tipo` è del contenitore; esito e orizzonte
  appartengono alla singola ipotesi quando il file ne contiene più d'una. Il
  costo di leggere metadati dentro le sezioni, anche per l'audit, è una
  variabile da misurare, come la granularità: in `economia` la calibrazione
  su Caprioli nasce dal confronto fra le previsioni 0, 1 e 7, e la prova
  esercita entrambe le scelte. La calibrazione trasversale resta comunque
  della sintesi.
- **Tipo, esito e maturità restano distinti**: `stato: bozza|iniziale|maturo`
  dei nodi non esprime corroborazione o falsificazione. Provare se l'esito
  debba essere un campo a valori chiusi; formulazione, alternative, prove,
  vincoli di scioglimento e revisioni restano nel corpo.

La prova verifica il confine fra i tipi e la loro copertura, compresi i
prodotti runtime, confrontandosi con la classificazione già praticata
altrove. In o3 convivono prescrizioni, runbook ed esecutori, e i Markdown
delle prescrizioni dichiarano ciclo, stato, data e destinatari. In i1
convivono catture singole e stato corrente rigenerato, come
`nixos/i1/manutenzione.json` (segnale
`i1/registro-perpetuo-vs-cattura-singola.md`). In `bi`, `kb/percezioni.md` e
`o3/lib/perception.js` dichiarano un contratto runtime: envelope JSON con
produttore, consumatori, versione dello schema e stadio, registry e controlli
sulle chiamate reali. Frontmatter Markdown ed envelope JSON hanno ruoli
analoghi, ma formati e controlli distinti: non aggiungere un inventario
manuale parallelo al registry né imporre frontmatter a script o JSON. Il task
non generalizza una tassonomia di tutti gli stadi né migra i contratti
runtime degli adottanti.

### Forma minima di un'ipotesi

- formulazione originaria, autore, data e fonti disponibili in quel momento;
- lettura alternativa e osservazione che permetterebbe di distinguerle;
- criterio di verifica stabilito prima del riscontro, con evento atteso o
  orizzonte temporale quando pertinenti;
- riscontri effettivi con provenienza e data, distinti dalle inferenze;
- esito motivato: in attesa, corroborata, falsificata, mista o non valutabile,
  con limiti del riscontro e conseguenze sulla lettura corrente.

Una corroborazione non prova automaticamente la causa o l'intenzione
attribuita. L'assenza di dati non è conferma né falsificazione; il mancato
evento vale come riscontro solo se finestra e copertura dell'osservazione lo
consentono. Le ipotesi composte si separano quando una conferma parziale
nasconderebbe una smentita. Probabilità numeriche e previsioni non sono campi
obbligatori, e la prova non impone campi privi di senso.

Formulazione e criterio originari non si riscrivono alla luce dell'esito. Una
revisione dichiara cosa cambia e perché, conservando il predecessore e il suo
esito. Git conserva la storia completa; il file conserva la lettura corrente
e i precedenti necessari a capirla, senza un diario delle sessioni.

### Permanenza degli esiti

Il canone vigente governa lo stato corrente dei fili i3 e già protegge le
altre funzioni vive. La proposta esplicita una funzione di i2: **un esito
resta finché condiziona una lettura corrente**. Il file indica quale lettura
ne dipende, con una frase o un collegamento; la previsione smentita su
Caprioli in `economia` è un caso di calibrazione ancora utile. Quando il
dettaglio non condiziona più nulla, ne resta la lezione nella sintesi o in un
nodo e il dettaglio torna a Git. Il criterio impedisce accumulo senza
funzione corrente, non crescita legittima per nuove ipotesi. La promozione
nella KB richiede giudizio e non cancella un precedente ancora necessario a
ricordare una smentita.

### Presidio della skill eval

Il futuro protocollo collega i1 → i2 → i3:

1. **Perceive** rende riconoscibili gli eventi nuovi e le fonti raggiungibili.
   La presenza di un file, la sua data di modifica o l'ultimo commit non
   certificano da soli che un evento sia stato valutato.
2. **Interpret** controlla quali ipotesi possono ricevere riscontro dagli
   eventi, leggendo anche materiale di casa e fonti primarie, e registra
   riscontri, alternative, esiti e correzioni alle sintesi dipendenti.
3. **Compare** giudica le conseguenze rispetto al Goal e aggiorna i confronti;
   rende espliciti gli impatti sul plan, senza eseguire azioni per il solo
   fatto che una previsione si sia avverata.

Un controllo periodico cerca ipotesi il cui evento o orizzonte è già arrivato
e riscontri rimasti senza confronto, anche senza nuovi eventi nel giro, e
consente di riaprire un'ipotesi corroborata quando emergono smentite.

Il costo va tenuto basso: identificazione tramite `tipo` del contenitore,
identificativo ed eventuale orizzonte per ipotesi. L'audit delle scadenze
richiede un'estensione esplicita di `o3/kb_tools.py`, non è una capacità già
presente; eventi senza data e correzioni delle fonti richiedono un riesame
semantico. Il trailer `Esiti:` conta gli esiti per stadio, non certifica
quali ipotesi o riscontri siano stati coperti: definire la traccia minima
necessaria al riesame, senza un registro parallelo né un resoconto di ogni
coppia ipotesi × evento. Pertinenza, sufficienza e indipendenza delle
evidenze restano giudizio; rilevare e proporre non significa applicare nuovi
giudizi, goal o azioni senza la ratifica prevista dalle skill.

## Prova

### Prima: misurare il bisogno

Rileggere i sedici fili originari di `5ea8204`, undici eliminati e cinque
conservati e riscritti. Per ciascuno dichiarare destinazione e funzione del
materiale, distinguendo chiusura corretta, conoscenza risalita e lettura persa
da ripristinare in i2 con il presidio pertinente, senza associare
automaticamente una riga i3 al materiale recuperato. È il test più economico:
dice quanto il buco pesa prima di costruire lo schema per riempirlo.

L'esito non fa cadere il modello, ma ha due conseguenze dichiarate. Una
lettura persa e ancora viva si ripristina subito in `i2/` di `metodo` come
sintesi corrente, in un commit proprio, senza attendere lo schema. Il
conteggio di chiusure, risalite e perdite passa al custode come peso del
bisogno nel dominio di `metodo` e orienta l'ordine in cui, dopo la ratifica,
si rivalutano le potature degli adottanti, ciascuna nel proprio repo.

#### Esito della misura (2026-10-05)

Riletti i sedici fili a `5ea8204^`, cercandone la destinazione nel repo
corrente e, per i watchpoint, l'evento atteso negli adottanti. Su sedici:
cinque conservati con le tensioni intatte, due chiusi a ragione, sette
risaliti con una destinazione raggiungibile, due con una lettura viva senza
casa, ripristinata in i2. In più, tre risalite hanno lasciato orfana una
verifica.

- **Conservati e riscritti** (5): `audit-adottanti`,
  `maturazione-nodi-fondativi`, `skill-per-arco-tripartito`,
  `toolchain-builder-presentazione` e `verdetto-piu-sicuro-del-materiale`
  tengono le loro tensioni. L'ipotesi sul montaggio degli scope di dominio
  era già regola in `kb/skill.md`; il watchpoint sulle ritrattazioni di
  `economia` è ora materia di questo task. Si perde solo la nota sul costo di
  discoverability in `bi`, senza lettura che ne dipenda.
- **Chiusi a ragione** (2): `home-minimalista`, con decisioni incise, il
  mini-server «fuori orizzonte» superato dalle presentazioni permanenti e il
  watchpoint sulle tavole generalizzato in `kb/presentation.md` («Fedeltà
  alle fonti»); `liste-o3-i1-fedeli-alla-fonte`, il cui watchpoint si è
  sciolto perché `i1/perceptions.md` non porta più cronaca.
- **Risaliti** (7): `de-cablaggio-binomio-due-agenti` nello `stato: bozza`
  di `kb/agent.md`, con la condizione d'uso reale; `bootstrap-adottanti` e
  `aligned-copre-prescrizioni-aperte` nelle tensioni datate di
  `i3/audit-adottanti.md`; `vista-derivata-e-verificata` in `kb/view.md`
  («Freschezza», con l'escalation); `igiene-stadi-output` in `kb/plan.md`
  (`Ob.`, chiave `S`), con la contraddizione di `economia` sciolta;
  `protocollo-post-evento` e `ricorrenza-per-battito` in `kb/skill.md` e
  `kb/plan.md`.
- **Verifiche orfane** dentro le risalite (3): l'email come superficie i1
  attende ancora la seconda istanza, `acquisti@` di `bi`, che il suo task
  `skill-ordini-fornitori` rinvia; la skill `ordini` di `bi`, prima istanza
  attesa della cadenza in configurazione per entità, esiste dal 2026-07-22 e
  nessuno l'ha valutata; la skill `update` di `nixos`, il cui ramo
  quotidiano doveva collaudare la coesistenza di righe di specie diverse,
  non esiste più. Nessuna lettura corrente ne dipende: per il criterio di
  permanenza tornano a Git, ma sono tre istanze del difetto che il presidio
  deve impedire, con l'evento arrivato e nessun riesame.
- **Letture vive senza casa** (2), ripristinate in i2 con un commit proprio:
  - `attese-a-finestra`: la regola è in `kb/plan.md`, `stato: maturo`, ma la
    verifica attesa è sparita. Il marcatore `!` non compare in nessun commit
    dei plan dei sette adottanti dal 2026-08-22; ora vive in
    `i2/attese-a-finestra.md`. Mostra il limite della regola di potatura:
    lo `stato` di un nodo con più funzioni non porta l'ipotesi di una sola;
  - `ingresso-adottante`: il collaudo prospettico è arrivato con `baserow`
    il 2026-10-05. La prescrizione è stata eseguita e corretta in un punto,
    l'accento delle viste (`f44b6c0`), ma l'esito non era registrato nella
    lettura, ora aggiornata in `i2/ingresso-adottante.md`.

Peso del bisogno nel dominio di `metodo`: la potatura non ha perso
conoscenza stabile, ha perso **verifiche**. Cinque attese su sedici fili
sono rimaste senza presidio, e in tre l'evento era già arrivato. È il
difetto che il modello deve correggere; la misura non lo dimostra negli
adottanti, dove le potature si rivalutano dopo la ratifica.

### Poi: i casi

Analisi sui checkout locali, puliti e allineati ai rispettivi `origin/main`
dopo il fetch del 2026-10-05, ai commit che la prova fissa:

- `economia` `84cefbc`, `nixos` `6262067`, `salute` `e8e323a`, `bi`
  `4be04bcb`, `crm` `d638a64`, `danea-auto` `c3acb33`, `baserow` `3a84767`.

Nessuna verifica live degli host, delle controparti o degli eventi sanitari:
riferimenti Git e file sono fonti della diagnosi degli artefatti, non
conferme indipendenti dei fatti esterni. I due prototipi sono i casi col
segnale più netto; gli altri cinque provano la generalità e ne tracciano il
perimetro.

#### Prototipi

- **economia**, potatura `3c8d84b`: quattro fili eliminati; fonti, lente
  patrimonio/reddito e linea Fiano ricollocate nella KB e nei task. È
  l'unico adottante che pratica già criteri anteriori ed errori conservati.
  Dalle previsioni di `i2/angolo-nostradamus.md` ricavare le due
  granularità, file per previsione e file con ancore, e applicarvi il
  criterio di permanenza.

  La previsione 8 sulla risposta di Orsi è ancora «aperta» mentre altri
  materiali riportano il chiarimento successivo: è un'ipotesi scaduta senza
  presidio, da riesaminare contro il documento originale senza dedurne qui
  un esito.

  Il file numera le profezie da 0 a 8 in un ordine che non segue quello del
  testo (0, 1, 3, 4, 5, 6, 7, 2, 8): i numeri sono già identificativi stabili
  indipendenti dalla posizione, il caso concreto per scegliere fra ancore e
  file per ipotesi. Gli esiti praticati, `APERTA`, `AVVERATA`, `SBAGLIATA` e
  mista, si mappano su quelli proposti, e la mappatura è un costo da
  misurare: «avverata» non diventa «corroborata» senza verificare caso per
  caso criterio e riscontro.

- **nixos**, potatura `068e25b`: quattro fili eliminati, con regole
  consolidate nella KB e lavoro nei task. Da `fcf60a7` (2026-10-04,
  recepimento della migrazione delle viste) `i2/nixos-in-sintesi.md` non
  esiste più e `i2/` contiene il solo indice: la lettura causale del boot è
  passata nel deck, `presentation/presentation.md` § «Affidabilità del boot
  dei server», e resta distribuita fra il deck,
  `o2/investigate-server-boot-recurrence.md` e
  `i3/affidabilita-boot-server.md`. Il prototipo legge quella sezione e
  propone dove la lettura vivrebbe in i2, senza modificare il deck: la sua
  revisione resta il seguito tracciato di `o3/migrazione-viste.md` e parte
  dopo la ratifica, con la proposta del prototipo come ingresso.

  È il caso canonico di chiusura ≠ spiegazione: tre reboot sani per server
  possono chiudere come «non ricorso» senza dimostrare la causa del guasto.
  La scadenza della prova è quella del riesame, anche senza una data di
  risoluzione dell'ipotesi causale: è un orologio nostro (`kb/plan.md`,
  «Tempo e fonti»), verifica che il presidio scatti, non che il Mondo abbia
  risposto, e non vale come la scadenza esogena di `economia`.

  Divisione attesa del lavoro, da verificare. i2 tiene la lettura: entrambi
  gli incidenti sono avvenuti al primo riavvio dopo un `nixos-rebuild
switch`, mentre un reboot successivo senza rebuild è riuscito; la
  correlazione resta un'ipotesi presidiata, con alternative e incertezza. i3
  confronta quella lettura con l'obiettivo di affidabilità: il criterio
  corrente, tre primi reboot dopo un rebuild senza emergency mode, misura la
  non ricorrenza, e il confronto può concludere che non basta a dire
  l'obiettivo raggiunto mentre la causa resta ignota e proporre di
  rettificarlo. La modifica la decide il custode nel register di `nixos`.

#### Perimetro

- **salute**, potatura `ae9a174`: tre fili eliminati; baricentro accorpato al
  quadro corporeo e domande autobiografiche conservate in
  `i2/educazione-cattolica.md`. Prova il gradiente: rabbia inavvertita e
  tenuta della pratica dopo il ritiro, distinguendo regolarità delle sedute e
  cambiamento nelle relazioni; una lettura esplorativa può restare utile
  senza scheda né confronto aperto.
- **bi**, potatura `f1e304b5`: quattro fili eliminati, con contenuti stabili
  ricollocati e monitoraggio automatico conservato. Prova i presidi del ciclo
  giornaliero che attendevano il primo fallimento reale e le ipotesi correnti
  su drift e orfani: una regola implementata non ha ancora dimostrato
  efficacia sul guasto reale, e un report riscritto a ogni run non è una
  serie storica, quindi verificare la disponibilità della serie di riscontri.
- **crm**, potatura `8d0e338`: due fili eliminati, la scelta architetturale
  già ratificata nel nodo maturo e il registro clienti già consegnato come
  handoff in o2; in i3 resta il solo cursore. Prova il caso senza confronto
  i3 e il confine fra sintesi e ipotesi: `i2/registro-clienti-unificato.md`
  chiude con tre incognite aperte (sistema delle newsletter, autorità
  dell'indirizzo commerciale, significato operativo di SalesKing) che
  condizionano l'import senza essere ipotesi formulate;
  `i2/valutazione-twenty.md` porta un esito concluso, il no-go del pilot, da
  cui dipende la lettura corrente sulla soluzione custom. Verificare se
  quelle incognite restano domande in prosa o diventano ipotesi presidiate,
  e se l'esito di Twenty soddisfa il criterio di permanenza.
- **danea-auto**, potatura `230f1e2`: un filo eliminato, Controlp chiuso nel
  nodo `kb/affidabilita-gui.md`. È la pratica più vicina al modello senza
  averlo: `i3/rallentamento-libreoffice.md` formula un'ipotesi (LibreOffice
  rallenta con l'uptime), un precursore misurato da `o3/stats.ps1` con
  soglia e una scadenza esogena, l'istanza del 01/10 all'età della rampa
  intorno al 13/10, con le due uscite dichiarate. L'ipotesi vive però nel
  confronto i3 insieme all'effetto sull'obiettivo: prova la separazione di
  valenza su un caso in cui la pratica corrente funziona. La scadenza cade
  durante la prova e offre una situazione «scadenza senza nuovi eventi»
  reale, osservata senza intervenire sul runtime. In `i2/` le finestre di
  osservazione sono sintesi con misure; il deck è uscito in `presentation/`
  col recepimento di `migrazione-viste` (`1443454`).
  `i2/chiusura-danea-connessione-persa.md`, del 2026-10-05, rilegge quattro
  chiusure di Danea con la stessa firma in `Easyfatt.log`: una lettura
  causale su ricorrenze, banco per distinguere una firma ricorrente da una
  causa dimostrata.
- **baserow**, nessuna potatura: adottante dal 2026-10-05. `i2/` è vuota per
  scelta dichiarata, misure in i1 e giudizio nei fili i3. Prova la
  collezione legittimamente senza ipotesi e il confine con la verifica
  operativa: `i3/redis-overcommit.md` attende che il warning sparisca al
  primo riavvio del container, dopo una correzione applicata da `nixos`.
  Stabilire se un'attesa di questo tipo, legata a un evento pianificato e a
  una correzione di un altro repo, è un'ipotesi sul Mondo da presidiare in
  i2 o la condizione di chiusura di un confronto, e se il presidio regge una
  dipendenza fra adottanti.

Per ciascun caso produrre una proposta concreta di i2 e presidio del riesame,
indicando cosa cambia, cosa non ha riscontro e dove vivono dati ed esiti.
Aggiungere un confronto i3 solo quando esiste una questione valutativa contro
il Goal; almeno un caso, `crm` o `baserow`, resta senza confronto i3.

#### Esiti attesi: la scadenza di `danea-auto`

Fissati il 2026-10-05, prima dell'osservazione, a `c3acb33`. È un caso del
perimetro, quindi non si fanno girare i due bracci: si osserva se la pratica
corrente fa emergere la scadenza da sola. Nessuno la ricorda alle sessioni di
`danea-auto`, altrimenti l'osservazione è contaminata.

- **Ipotesi**: LibreOffice rallenta con l'uptime
  (`i3/rallentamento-libreoffice.md`). Istanza viva dal 01/10 alle 11:42;
  età della rampa osservata intorno ai 12 giorni, quindi verso il 13/10;
  l'istanza della crisi del 25/09 aveva 16 giorni.
- **Riscontro**: le righe di ritentativo `^+s` contate per giorno da
  `o3/stats.ps1`, con la soglia di 10 righe di `kb/affidabilita-gui.md`.
- **Esito corretto, secondo la finestra**:
  - righe sopra soglia mentre l'istanza invecchia: l'ipotesi si rafforza,
    ma la corroborazione resta sul precursore e non prova la causa. La
    conseguenza proposta è il task già dichiarato, il riavvio di LibreOffice
    insieme a quello delle 05:45;
  - zero righe con l'istanza ininterrotta almeno fino al 17/10, cioè oltre
    l'età della crisi del 25/09: l'uptime non è la variabile alla scala
    osservata, e la lettura si rivede;
  - istanza rinnovata prima dei 12 giorni, per chiusura manuale o riavvio
    di `danea2`, compreso quello di Windows ancora da osservare: non
    valutabile. L'orizzonte si sposta, e il mancato evento non vale come
    falsificazione.
- **Cosa si misura**: se il primo giro `eval` di `danea-auto` dopo il 13/10
  fa emergere l'ipotesi senza un nuovo evento che la nomini. La lettura si
  fa sui commit pubblicati, col trailer `Esiti:` e il diff del filo.

## Condizione di caduta

I criteri si fissano prima dei prototipi e si esercitano due volte, sulla
pratica corrente e sul modello, con quattro situazioni:

- **evento pertinente**: avvia il riesame dell'ipotesi che raggiunge;
- **evento irrilevante**: non forza un esito, e i dati mancanti restano tali;
- **scadenza senza nuovi eventi**: emerge comunque;
- **correzione della fonte**: riapre la lettura che ne dipende.

Il confronto misura i protocolli, non quanto si guida il lettore. I due bracci
ricevono gli stessi materiali, la stessa richiesta e lo stesso budget, senza
indicare quale ipotesi riesaminare. La richiesta è la stessa sequenza,
`/eval interpret` e poi `/eval compare`, con la skill corrente in un braccio
e quella modificata per la prova nell'altro. Serve anche `compare`, perché
nella pratica corrente scadenze e conteggi di chiusura vivono nei fili i3.
`perceive` resta fuori: gli eventi sono già catturati, e ai due bracci si
dice allo stesso modo di lavorare solo sui file del repo, senza accesso a
host, rete o servizi. Ogni braccio gira in una sessione nuova, perché chi ha
eseguito il primo arriva al secondo sapendo cosa cercare, e non apre
`metodo/o2/`, dove vivono gli esiti attesi.

- **Eventi**: si usano eventi reali quando esistono al commit fissato; gli
  altri si costruiscono come file i1 identici per i due bracci. Per ogni
  situazione l'esito atteso si scrive prima di eseguire i bracci.
- **Dove**: entrambi i bracci girano in un worktree dell'adottante al commit
  fissato; eventi costruiti e skill modificata vivono solo lì e non arrivano
  mai su `main` dell'adottante.
- **Giudice**: una sessione distinta confronta gli output, anonimizzati come
  A e B, con gli esiti attesi; il custode dirime i casi dubbi.
- **Budget**: stesso modello, stesso livello di sforzo e stesso limite
  dichiarato di turni, nessuna indicazione aggiuntiva.
- **Varianza**: due run per braccio e per prototipo; una situazione conta
  come gestita solo se lo è in entrambi i run, e la divergenza fra run si
  dichiara come instabilità, non come successo.

### Criteri fissati (2026-10-05)

Eventi ed esiti attesi dei due prototipi, scritti prima di costruirli.
Ciascun evento costruito vive solo nel worktree; gli esiti
di giudizio sono stati ratificati dal custode il 2026-10-05.

**`economia`, a `84cefbc`**, ultimo giro `eval` il 2026-10-02:

- **pertinente**, costruito: una cattura `i1/email/` in cui Teresa scrive
  nel thread dei comproprietari mettendo Carlo in copia e chiedendogli di
  esprimersi, senza che nessuno del ramo Pompa l'abbia sollecitata. Atteso:
  riesame della profezia 6, esito falsificata per il suo criterio
  («sbagliata se uno dei tre lo porta dentro spontaneamente»), con la
  conseguenza sulla lettura che ne dipendeva, la convergenza di interessi
  sul silenzio di Carlo; nessuna mossa sul credito di Carlo senza compare e
  plan. Prima dell'evento la profezia ha già due riscontri parziali, la
  compensazione a carico di Carlo proposta da Caprioli il 01/09 e il
  contatto diretto di Stefano il 03/09: nessuno dei due la falsifica (ratificato), perché il primo è contabilità e non porta Carlo al tavolo, e
  il secondo è iniziativa nostra;
- **irrilevante**, costruito: una comunicazione della banca sul conto
  personale che non tocca Fiano. Atteso: nessun esito su nessuna profezia;
- **scadenza senza nuovi eventi**, reale: la profezia 8 attende la risposta
  di Orsi, catturata il 13/08 in `i1/email/2026-08-13.json` e mai riportata
  sulla profezia. Atteso: la profezia emerge come valutabile senza che un
  evento nuovo la nomini, con esito corroborata (ratificato): Orsi
  conferma il riparto del residuo secondo le indicazioni ricevute, rinvia la
  differenza a un conguaglio fra comproprietari e definisce anomala una nota
  di credito. Emerge anche la profezia 5, la partita Orsi saldata per
  bonifici separati il 13/08 e il 18/08, con esito mista (ratificato): la separazione dei pagamenti si è avverata, ma il conguaglio è stato chiesto per iscritto nel thread;
- **correzione della fonte**, costruita: una ricattura del thread di metà
  agosto mostra che la domanda del 14/08 sull'unico pagamento era di Ilaria
  a Stefano, e che da Teresa e Maurizio non c'è risposta scritta, solo il
  bonifico del 18/08. L'esito di oggi della profezia 7 si regge su quel
  messaggio, che non è catturato in i1. Atteso: riapertura dell'esito,
  rivalutato contro il criterio originario, con la formulazione intatta e il
  predecessore conservato. Si riapre anche la lezione di calibrazione che ne
  dipende, la «cannata collegata».

**`nixos`, a `6262067`**, ultimo giro `eval` il 2026-09-27:

- **pertinente**, reale: `i1/manutenzione.json` registra il 2026-10-05
  `rebuild switch` e reboot di `norvegia` e poi di `svezia`, entrambi senza
  unità fallite; il reboot di `svezia` è avvenuto senza il runbook. Il
  conteggio in `o2/investigate-server-boot-recurrence.md` è ancora 0/3 per
  entrambi. Atteso: due primi reboot sani dopo un rebuild, e il conteggio
  passa a 1/3 per ciascun server. L'ipotesi resta in attesa: un esito sano
  non la falsifica, perché il guasto non è deterministico, e non conferma
  alcuna causa. Il reboot senza runbook è una variabile da annotare, non un
  riscontro sul boot;
- **irrilevante**, costruito: un aggiornamento del ramo `ia` di
  `manutenzione.json` applicato al solo `deck`. Atteso: nessun effetto
  sull'ipotesi del boot;
- **scadenza senza nuovi eventi**, costruita: nei materiali dei due bracci
  la data di rivalutazione del filo e del task passa dal 2026-12-31 al
  2026-10-01. È un orologio nostro: verifica che il presidio scatti, non che
  il Mondo abbia risposto. Atteso: la scadenza emerge; si dichiara il numero
  di eventi, 1/3 per server dopo l'evento pertinente, e si sposta la data
  senza chiudere;
- **correzione della fonte**, costruita: una rettifica alla cattura
  `i1/svezia-boot-failure-20260907.md` mostra che il fallimento del 09/07
  era il secondo reboot dopo il rebuild, non il primo, e che il primo era
  riuscito. Atteso: si riapre la lettura che regge la pista principale,
  perché la correlazione «primo reboot dopo `switch`» perde una delle due
  istanze. Le alternative riprendono peso, la definizione del conteggio va
  rivista, e nessuna causa nuova si attribuisce senza evidenza
  discriminante.

La pratica corrente di `nixos` ha già mancato l'evento pertinente nel Mondo:
la sessione di manutenzione del 2026-10-05 ha registrato i due reboot sani
senza aggiornare il conteggio. È un indizio, non il confronto: quella
sessione non era un giro `eval`.

La previsione 8 di `economia` documenta un fallimento storico della pratica
corrente ma non sostituisce la prova: rileggendo oggi quel materiale, la
pratica corrente potrebbe intercettarla, e solo il confronto alla pari lo
dice.

Il modello si generalizza solo se, in entrambi i prototipi (`economia` e
`nixos`):

- gestisce correttamente tutte e quattro le situazioni;
- la pratica corrente ne manca almeno una; altrimenti in quel dominio il
  modello non serve;
- ogni file, campo o collegamento introdotto sostiene un comportamento della
  prova o una lettura dipendente identificabile; essere letto da una vista non
  basta, perché una vista può leggere qualsiasi campo senza renderlo utile.
  Gli elementi superflui si eliminano;
- il criterio di permanenza condensa almeno un dettaglio consumato e conserva
  almeno un precedente utile, e fra i dettagli condensati il custode non
  riconosce una lezione ancora viva.

Gli altri cinque adottanti non decidono la generalizzazione: ne tracciano il
perimetro. Un limite di dominio lì delimita il modello invece di farlo
cadere, e si dichiara; un'incompatibilità con un contratto canonico comune
torna invece sul modello generale, perché non ogni fallimento si assorbe come
eccezione locale.

Non sono condizioni di caduta, né vanno lette come conferme:

- l'assenza di letture perse in `5ea8204`: smentisce il sospetto sulla
  potatura, non il bisogno di presidio negli adottanti;
- un caso esplorativo che resta in prosa;
- la crescita della collezione per nuove ipotesi, distinta dall'accumulo senza
  funzione corrente.

Se un prototipo fallisce, il task consegna una regola più piccola, per esempio
il solo identificativo con orizzonte sulle letture esistenti, oppure delimita
la pratica al dominio che ne beneficia.

## Decisioni da consegnare al custode

- schema minimo della facet `tipo`, eventuale `esito` e gradiente fra
  sintesi esplorativa e ipotesi autonoma, anche senza orizzonte;
- granularità: identificativo per ipotesi, con file per ipotesi o ancore in
  un file comune;
- criterio di permanenza degli esiti;
- forma di i3: orientamento verso un file per confronto, che porta la
  sintesi valutativa in prosa, con un indice tabellare come o1 e o2; la sola
  tabella non ha posto per quella prosa, che non può scendere in i2 perché
  i2 sospende la valenza, e una cella è illeggibile a larghezza mobile
  (`CLAUDE.md`). Da ratificare dopo la prova;
- destinazione di cursori e contratti come `i3/allineamento-metodo.md`;
- etichetta della collezione i3: «Verdetti» o «Confronti», con rinomina dei
  nodi `verdict` e `compare` o senza;
- copertura e costo del presidio di `eval`;
- quali task nascono dopo la ratifica: nodi (`node`, `verdict`, `interpret`,
  `compare`, `plan`, `tasks`, `specify` dove toccati), skill `eval`,
  `adottanti`, `method`, `commit`, eccezione tabellare di i3 in `CLAUDE.md`,
  triage di `i2/` in `metodo` (`potatura-kb` conclusa,
  `baricentro-kb-adottanti` materiale di nodo, `bootstrap-adottanti` e
  `ingresso-adottante` da rileggere), prescrizione agli adottanti.

## Feedback

- La rilettura di `5ea8204` dichiara per ogni filo originario l'esito, anche
  quando è «chiuso a ragione».
- I casi rendono distinguibili evidenze, ipotesi, giudizio contro il Goal e
  azioni. Nessuna spiegazione risulta confermata per la sola chiusura
  operativa del problema.
- La prova sulle previsioni di `economia` verifica il caso rimasto aperto e
  mantiene consultabili almeno un esito falsificato e uno corroborato, con
  formulazione e criterio originari, e condensa un dettaglio non più utile
  dichiarando la lezione conservata. Un nuovo riscontro contrario può riaprire
  la lettura.
- Il modello consegnato dichiara quale condizione di caduta è stata
  esercitata e con quale esito.

## Vincoli

- Nessuna potatura elimina ipotesi ancora da verificare, esiti cognitivamente
  utili, cursori o contratti senza una destinazione esplicita e raggiungibile.
- Il task non autorizza modifiche al Goal, al canone, azioni runtime o
  migrazioni negli adottanti: le proposte sui casi restano proposte finché
  ciascun adottante non le decide nel proprio dominio.
- Le analisi dei casi sono materiale di lavoro di questo task; ciò che ne
  sopravvive alla ratifica va nelle letture i2 pertinenti, non resta in o2.
