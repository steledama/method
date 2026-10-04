---
sintesi: "Provare un laboratorio delle ipotesi nella collezione i2 di ogni adottante: file autonomi classificati tramite tipo: sintesi|ipotesi, riscontri, revisioni e scioglimento propri; i3 conserva i confronti contro il Goal. Prototipi su economia e nixos, generalità su salute e bi, riesame tramite eval e permanenza degli esiti utili. Misurare separatamente le perdite nella potatura dei sedici fili originari; consegnare un modello verificato senza incidere il canone."
ciclo: dev
---

# Ipotesi e confronti i2/i3

Task di prova, non di migrazione. Nato il 2026-10-04 dalla revisione della
presentazione e separato lo stesso giorno dalla migrazione delle viste, ora
chiusa nel canone e prescritta ai sei (`o3/migrazione-viste.md`): liberare i2
dal deck non dice ancora che cosa i2 debba custodire, e la risposta va provata
sui casi prima di diventare obbligo canonico. Dall'esito dipende il seguito
tracciato di quella prescrizione: la revisione del deck di `nixos`, che
mescola racconto dell'artefatto e lettura del boot. Il suo prodotto è un modello sottoposto al
custode; canone, ristrutturazione di `metodo` e prescrizione ai sei nascono
come task propri solo dopo la ratifica.

## Il problema

Il canone assegna già a i2 letture, assunzioni e incertezza, ma non
esplicita il contratto per rendere raggiungibili le **convinzioni sul Mondo
ancora esposte alla prova**, riesaminarle sui riscontri e conservarne gli
esiti utili. Le pratiche esistono: previsioni in `economia`, spiegazioni del
boot in `nixos`, letture esplorative in `salute`.

Due bisogni si misurano separatamente: il presidio incompleto delle ipotesi e
l'eventuale perdita di letture nelle potature recenti — `5ea8204` in `metodo`
(sedici fili ridotti a cinque), da 38 a 19 nell'aggregato dei sei. Una potatura
corretta non smentisce il bisogno di riesame osservato altrove.

## Direzione concordata e modello da verificare

La revisione con il custode del 2026-10-04 ha concordato la direzione;
cardinalità, schema e ciclo di vita si provano sui casi.

- **i2 rende concreta la lettura**: evidenze e provenienza, chiavi
  interpretative, ipotesi, alternative, assunzioni e limiti. Qui vivono le
  ipotesi da verificare, comprese le previsioni già praticate in
  `economia`. La lettura è orientata dal Goal sulla rilevanza;
  spiegare o prevedere non equivale a giudicare il successo rispetto al Goal.
- **i3 governa i confronti**: le questioni valutative vive, collegate alle
  letture i2, con obiettivo, giudizio corrente e condizione di riesame. Il
  confronto porta una sintesi valutativa: che cosa la lettura significa
  rispetto allo scopo, quale tensione rivela, quali conseguenze propone per
  l'azione o per il Goal, compresa l'aggiunta, la rettifica o la
  ridefinizione di un obiettivo. La modifica del Goal resta una decisione del
  custode, resa esplicita nel register.
  L'ordine esprime priorità di attenzione e verifica; il plan mantiene la
  priorità dell'azione. Una questione può essere importante mentre non
  autorizza ancora nessuna mossa.
- **Il legame è esplicito, la biunivocità non è presupposta**: ogni confronto
  raggiunge il materiale che lo sostiene; una sintesi può alimentare più
  confronti o restare utile senza un confronto aperto. Ogni ipotesi che attende
  verifica deve però essere raggiungibile dal presidio di `eval`, anche quando
  non richiede una propria riga i3. Il contratto deve impedire ipotesi
  dimenticate senza creare confronti fittizi per completare una coppia.
- **La verifica e la chiusura sono distinte**: chiudere un task, stabilizzare
  un giudizio operativo e confermare una spiegazione sono eventi diversi.

La simmetria o1↔i3, o2↔i2 è funzionale: impegni d'azione e impegni di
valutazione, specifiche dell'azione e letture del Mondo. Non impone di
stringere il contratto plan×o2 né di ridurre tutti gli stadi a file Markdown:
in `bi` esistono anche prodotti automatici runtime i2 e i3.

## Oggetti della collezione e laboratorio delle ipotesi

Direzione concordata col custode: istituzionalizzare il laboratorio delle
ipotesi nella collezione esistente `i2/` di ogni adottante, senza imporre
ipotesi da produrre né una nuova collezione. Una collezione senza ipotesi
correnti è legittima. Il nome comune è «ipotesi»; il nome scherzoso della
pratica di `economia` non entra nel modello.

Provare la facet `tipo: sintesi|ipotesi`, a valori chiusi e singola per file,
accanto a `ciclo: dev|runtime`, dichiarata nel canone e verificabile dagli
strumenti. Oggi questa facet non esiste in i2: è una proposta da provare,
non un controllo già implementato. L'indice esistente rende raggiungibili
entrambi i tipi; le viste possono selezionare le ipotesi dai metadati.

L'unità del presidio è l'ipotesi, non il file: identità e contenitore sono
scelte distinte. Ogni ipotesi ha un identificativo stabile, il file stesso o
un'ancora, che `eval`, i collegamenti e le letture dipendenti possono citare
e che permette di seguirne formulazione, riscontri e revisioni. Il contenitore
può ospitare una o più ipotesi, ma un'ipotesi presidiata vive solo in un file
`tipo: ipotesi`: la selezione per `tipo` trova così tutti i contenitori senza
imporre un file per ipotesi. Una sintesi resta libera di porre domande
esplorative; non ospita ipotesi presidiate.

`tipo` è una facet del contenitore. Esito e orizzonte appartengono invece alla
singola ipotesi, non al frontmatter del file, quando il file ne contiene più
d'una: la prova dello schema ne tiene conto, e il costo di leggere metadati
dentro le sezioni, anche per l'audit, è una variabile da misurare. La
granularità resta una variabile della prova: in `economia` la calibrazione su
Caprioli nasce dal confronto fra le previsioni 0, 1 e 7, e la prova esercita
entrambe le scelte. La calibrazione trasversale è comunque responsabilità della
sintesi, qualunque granularità si scelga.

Una sintesi può contenere domande e ipotesi esplorative. Una lettura diventa
un'ipotesi presidiata quando richiede riscontri, revisioni e criteri di
scioglimento propri o condiziona decisioni nel tempo. La prova determina se
ospitarla in un file autonomo o in una sezione identificata di un contenitore
`tipo: ipotesi`. L'orizzonte è una proprietà possibile, non il requisito per
avere una casa. La prova verifica
il confine fra i tipi e la loro copertura, compresi i prodotti runtime.

Tenere distinti tipo dell'oggetto, esito dei riscontri e maturità dei nodi KB:
`stato: bozza|iniziale|maturo` non esprime corroborazione o falsificazione.
Provare se l'esito debba essere un campo a valori chiusi; formulazione,
alternative, prove, vincoli di scioglimento e revisioni restano nel corpo.

Il confine con i3 resta sulla valenza. Un'ipotesi dichiara che cosa accade o
accadrà e da quale osservazione lo si saprebbe; che cosa l'esito significhi per
il Goal, e se muova il plan, vive nel confronto i3. L'esito registra lo stato
del riscontro, non un giudizio favorevole o sfavorevole. Una lettura che
condiziona decisioni riceve un file perché quelle decisioni dipendono dal suo
riscontro, non perché il file le giudichi.

### Precedenti nelle altre collezioni

La proposta si confronta con la classificazione già praticata: in o3
convivono prescrizioni, runbook ed esecutori; i Markdown delle prescrizioni
possono dichiarare ciclo, stato, data e destinatari. In i1 convivono catture
singole e stato corrente rigenerato, come `nixos/i1/manutenzione.json`
(segnale `i1/registro-perpetuo-vs-cattura-singola.md`).

In `bi`, `kb/percezioni.md` e `o3/lib/perception.js` dichiarano invece un
contratto runtime: envelope JSON con produttore, consumatori, versione dello
schema e stadio, registry e controlli sulle chiamate reali. I metadati
sistematizzano classificazione e provenienza; il codice applica il contratto.
Frontmatter Markdown e envelope JSON hanno ruoli analoghi, ma formati e
controlli distinti. Non aggiungere un inventario manuale parallelo al registry
né imporre frontmatter a script o JSON.

Usare questi precedenti per verificare la proposta i2, distinguendo natura,
ciclo di vita e contratto di produzione/consumo. Il task non generalizza una
tassonomia di tutti gli stadi né migra i contratti runtime degli adottanti.

## Ipotesi e riscontri

Provare una forma minima che renda riconoscibili:

- formulazione originaria, autore, data e fonti disponibili in quel momento;
- lettura alternativa e osservazione che permetterebbe di distinguerle;
- criterio di verifica stabilito prima del riscontro, con evento atteso o
  orizzonte temporale quando pertinenti;
- riscontri effettivi con provenienza e data, distinti dalle inferenze;
- esito motivato: in attesa, corroborata, falsificata, mista o non valutabile,
  con limiti del riscontro e conseguenze sulla lettura corrente.

Il file autonomo mantiene la lettura corrente e i passaggi significativi
che ne spiegano le revisioni. Ogni ipotesi autonoma è raggiungibile dal
presidio di `eval`, anche senza scadenza o confronto i3. Le domande ancora
esplorative possono restare nella prosa della sintesi; la prova verifica il
gradiente senza imporre campi privi di senso.

Una corroborazione non prova automaticamente la causa o l'intenzione attribuita.
L'assenza di dati non è conferma né falsificazione; il mancato evento vale come
riscontro solo se finestra e copertura dell'osservazione lo consentono. Le
ipotesi composte si separano quando una conferma parziale nasconderebbe una
smentita. Probabilità numeriche e previsioni non sono campi obbligatori.

La formulazione e il criterio originari non si riscrivono alla luce dell'esito.
Una revisione dichiara cosa cambia e perché, conservando il predecessore e il
suo esito. Git conserva la storia completa; il file conserva i precedenti
necessari a capire la lettura corrente, senza un diario delle sessioni.

## Permanenza degli esiti

Il canone vigente governa lo stato corrente dei fili i3 e già protegge le
altre funzioni vive. La proposta esplicita una funzione di i2: **un esito
resta finché condiziona una lettura corrente**. Il file indica quale lettura
ne dipende, con una frase o un collegamento; la previsione smentita su
Caprioli in `economia` è un caso di calibrazione ancora utile.

Quando il dettaglio non condiziona più nulla, ne resta la lezione nella
sintesi o in un nodo e il dettaglio torna a Git. Provare sia la conservazione
di un precedente utile sia la condensazione di materiale consumato. Il
criterio impedisce accumulo senza funzione corrente, non crescita legittima
per nuove ipotesi. La promozione nella KB richiede giudizio e non cancella un
precedente ancora necessario a ricordare una smentita.

## Presidio della skill eval

Il futuro protocollo collega i1 → i2 → i3:

1. **Perceive** rende riconoscibili gli eventi nuovi e le fonti raggiungibili.
   La presenza di un file, la sua data di modifica o l'ultimo commit non
   certificano da soli che un evento sia stato valutato.
2. **Interpret** controlla quali ipotesi possono ricevere riscontro dagli
   eventi, leggendo anche materiale di casa e fonti primarie. Registra
   riscontri, alternative, esiti e correzioni alle sintesi dipendenti.
3. **Compare** giudica le conseguenze rispetto al Goal e aggiorna i confronti;
   rende espliciti gli eventuali impatti sul plan, senza eseguire azioni per il
   solo fatto che una previsione si sia avverata.

Un controllo periodico cerca ipotesi il cui evento o orizzonte è già arrivato e
riscontri rimasti senza confronto, anche senza nuovi eventi nel giro, e
consente di riaprire un'ipotesi corroborata quando emergono smentite.

Il costo va tenuto basso. Provare l'identificazione delle ipotesi tramite
`tipo` del contenitore, identificativo e un eventuale orizzonte per ipotesi;
l'audit delle scadenze richiede un'estensione esplicita di `o3/kb_tools.py`,
non è una capacità già presente. Gli eventi senza data e le correzioni delle
fonti richiedono un riesame semantico. Ogni ipotesi è raggiungibile dal suo
identificativo, anche quando il materiale originario raccoglie più previsioni
in un file.

La prova esercita un evento pertinente, uno irrilevante, una scadenza senza
nuovi eventi e una correzione della fonte. Il trailer `Esiti:` conta gli esiti
per stadio; non certifica quali ipotesi o riscontri siano stati coperti.
Definire la traccia minima necessaria al riesame evitando un registro
parallelo o un resoconto di ogni coppia ipotesi × evento. Pertinenza,
sufficienza e indipendenza delle evidenze restano giudizio; rilevare e
proporre non significa applicare nuovi giudizi, goal o azioni senza la
ratifica prevista dalle skill.

## Prova

### Prima: misurare il bisogno

Rileggere i sedici fili originari di `5ea8204`: undici eliminati e cinque
conservati e riscritti. Per ciascuno dichiarare destinazione e funzione del
materiale, distinguendo chiusura corretta, conoscenza risalita e lettura
persa da ripristinare in i2,
con il presidio pertinente. Non associare automaticamente una riga i3 al
materiale recuperato. È il test più economico: dice quanto il buco pesa prima
di costruire lo schema per riempirlo. Le potature degli adottanti si
rivalutano allo stesso modo solo dopo la ratifica, ciascuna nel proprio repo.

### Poi: i casi

Analisi del 2026-10-04 sui checkout locali, puliti e allineati ai rispettivi
`origin/main`; nessuna verifica live degli host, delle controparti o degli
eventi sanitari. Riferimenti Git e file sono fonti della diagnosi degli
artefatti, non conferme indipendenti dei fatti esterni. Si parte dai due casi
con il segnale più netto; gli altri due provano la generalità.

- **economia**, potatura `3c8d84b`: quattro fili eliminati; fonti, lente
  patrimonio/reddito e linea Fiano ricollocate nella KB e nei task. È l'unico
  adottante che pratica già criteri anteriori ed errori conservati. Prova: dalle
  previsioni di `i2/angolo-nostradamus.md` (path sorgente attuale) ricavare le
  due granularità, file per previsione e file con ancore, e applicarvi il
  criterio di permanenza. La previsione 8 sulla risposta di Orsi è ancora
  «aperta» mentre altri materiali riportano il chiarimento successivo: è
  un'ipotesi scaduta senza presidio, da riesaminare contro il documento
  originale senza dedurne qui un esito.
- **nixos**, potatura `068e25b`: quattro fili eliminati, con regole
  consolidate nella KB e lavoro nei task. La lettura causale del boot resta
  distribuita fra `i2/nixos-in-sintesi.md`,
  `o2/investigate-server-boot-recurrence.md` e
  `i3/affidabilita-boot-server.md`. È il caso canonico di chiusura ≠
  spiegazione: tre reboot sani per server possono chiudere come «non
  ricorso», senza dimostrare la causa del guasto. La scadenza della prova è
  quella del riesame, anche senza una data di risoluzione dell'ipotesi
  causale: è un orologio nostro (`kb/plan.md`, «Tempo e fonti») e verifica
  che il presidio scatti, non che il Mondo abbia risposto. Si dichiara così e
  non vale come la scadenza esogena di `economia`.

  Divisione attesa del lavoro, da verificare nel prototipo. i2 tiene la
  lettura: entrambi gli incidenti sono avvenuti al primo riavvio dopo un
  `nixos-rebuild switch`, mentre un reboot successivo senza rebuild è riuscito
  (`i2/nixos-in-sintesi.md`, `o2/investigate-server-boot-recurrence.md`); la
  correlazione resta un'ipotesi presidiata, con le alternative e
  l'incertezza. i3 confronta quella lettura con l'obiettivo di affidabilità.
  Il criterio corrente di `i3/affidabilita-boot-server.md`, tre primi reboot
  dopo un rebuild senza emergency mode, misura la non ricorrenza; il
  confronto può concludere che non basta a dire l'obiettivo raggiunto mentre
  la causa resta ignota, e proporre di rettificarne il criterio di successo.
  La proposta resta tale: la modifica del Goal la decide il custode nel
  register di `nixos`.

- **salute**, potatura `ae9a174`: tre fili eliminati; baricentro accorpato al
  quadro corporeo e domande autobiografiche conservate in
  `i2/educazione-cattolica.md`. Prova il gradiente: rabbia inavvertita e
  tenuta della pratica dopo il ritiro, distinguendo regolarità delle sedute e
  cambiamento nelle relazioni; una lettura esplorativa può restare utile senza
  scheda né confronto aperto.
- **bi**, potatura `f1e304b5`: quattro fili eliminati, con contenuti stabili
  ricollocati e monitoraggio automatico conservato. Prova: i presidi del ciclo
  giornaliero che attendevano il primo fallimento reale, oltre alle ipotesi
  correnti su drift e orfani. Una regola implementata non ha ancora dimostrato
  efficacia sul guasto reale. Un report riscritto a ogni run non è una serie
  storica: verificare la disponibilità della serie di riscontri.

Per ciascun caso produrre una proposta concreta di i2 e presidio del riesame;
aggiungere un confronto i3 solo quando esiste una questione valutativa contro
il Goal. Includere un caso senza confronto i3. Indicare cosa cambia, cosa non
ha riscontro e dove vivono dati ed esiti. Nessuna
migrazione degli adottanti è implicita in questa prova.

## Condizione di caduta

I criteri si fissano prima dei prototipi e si esercitano due volte, sulla
pratica corrente e sul modello, con le stesse quattro situazioni: un evento
pertinente, uno irrilevante, una scadenza senza nuovi eventi, una correzione
della fonte.

Il confronto misura i protocolli, non quanto si guida il lettore. I due bracci
ricevono gli stessi materiali, fissati a un commit dichiarato dell'adottante,
la stessa richiesta e lo stesso budget di attenzione, senza indicare quale
ipotesi riesaminare. La richiesta naturale è lo stesso comando, `eval
interpret` sugli eventi nuovi, con la skill corrente in un braccio e quella
modificata per la prova nell'altro; ogni braccio gira in una sessione nuova,
perché chi ha eseguito il primo arriva al secondo sapendo cosa cercare.

La previsione 8 di `economia`, rimasta aperta dopo il chiarimento che la
riguardava, documenta un fallimento storico della pratica corrente. Non
sostituisce la prova: rileggendo oggi quel materiale, la pratica corrente
potrebbe intercettarla, e solo il confronto alla pari lo dice.

Il modello si generalizza solo se, in entrambi i prototipi (`economia` e
`nixos`):

- gestisce correttamente tutte e quattro le situazioni: l'evento pertinente
  avvia il riesame, quello irrilevante non forza un esito, la scadenza emerge
  senza nuovi eventi, la correzione della fonte riapre la lettura che ne
  dipende;
- la pratica corrente ne manca almeno una; altrimenti in quel dominio il
  modello non serve;
- ogni file, campo o collegamento introdotto sostiene un comportamento della
  prova o una lettura dipendente identificabile; essere letto da una vista non
  basta, perché una vista può leggere qualsiasi campo senza renderlo utile.
  Gli elementi superflui si eliminano;
- il criterio di permanenza condensa almeno un dettaglio consumato e conserva
  almeno un precedente utile, e fra i dettagli condensati il custode non
  riconosce una lezione ancora viva.

`salute` e `bi` non decidono la generalizzazione: ne tracciano il perimetro.
Un limite di dominio lì delimita il modello invece di farlo cadere, e si
dichiara. Un'incompatibilità con un contratto canonico comune torna invece sul
modello generale: non ogni fallimento si assorbe come eccezione locale.

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
  `ingresso-adottante` da rileggere), prescrizione ai sei.

## Feedback

- La rilettura di `5ea8204` dichiara per ogni filo originario l'esito, anche
  quando è «chiuso a ragione».
- I casi rendono distinguibili evidenze, ipotesi, giudizio contro il Goal e
  azioni. Nessuna spiegazione risulta confermata per la sola chiusura
  operativa del problema.
- Un evento i1 pertinente raggiunge un'ipotesi e ne provoca il riesame; un
  evento irrilevante non forza un esito. Dati mancanti restano tali.
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
