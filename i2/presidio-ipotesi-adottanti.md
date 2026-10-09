---
ciclo: runtime
---

# Il presidio serve dove le ipotesi restano fuori dal riesame

La prova del 2026-10-05 su `economia` e `nixos` confronta la pratica corrente
(braccio A) con un modello che aggiunge contenitori di ipotesi, facet `tipo`
e presidio in `eval` (braccio B). Non giustifica quel modello generale:
il custode ha ratificato solo la regola minima, recepita in
[interpret](../kb/interpret.md) e prescritta in
[presidio-ipotesi](../o3/presidio-ipotesi.md).
La [misura sulla potatura del canone](potatura-fili-e-verifiche.md) è distinta.

## Protocollo e provenienza

Otto sessioni nuove, due run per braccio e prototipo, stessa richiesta
`eval interpret` poi `eval compare`, solo file locali, nessuna applicazione.
Eventi uguali fra i bracci; quattro situazioni: evento pertinente,
irrilevante, scadenza senza nuovo evento e correzione della fonte.
Il protocollo prescriveva stesso modello, sforzo e budget; i resoconti non
forniscono una misura indipendente dell'effettiva parità del costo.
Il giudice ha letto gli output prima della mappa; due dubbi sono stati
risolti dal custode prima di aprirla. Una situazione conta come gestita
solo se lo è in entrambi i run del braccio.

La generalizzazione richiedeva tutte e quattro le situazioni gestite da B
e almeno una mancata da A in entrambi i prototipi, utilità identificabile
di ogni elemento introdotto e permanenza selettiva degli esiti. Quest'ultima
non era misurata dai bracci: spettava al custode; non se ne deduce qui un
collaudo autonomo. La caduta sui primi criteri basta a respingere il modello.

Fonti persistenti: commit `ef8abb3` per protocollo e preparazione,
`8deb856` per giudizio e limiti, `da41329` per ratifica, nel Git di `metodo`.
Le fixture e gli otto cloni temporanei sono materiale consumato; questa
lettura conserva criteri, mappa, risultati e limiti necessari al riesame,
non i resoconti integrali. Le fonti di dominio restano nei rispettivi repo.
Gli esiti attesi ratificati sono criteri della prova, non giudizi applicati
al dominio reale: questi spettano agli adottanti.

## Criteri ed eventi della prova

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
- **irrilevante**, costruito: la fattura telefonica WINDTRE di settembre,
  addebitata sul conto personale, che non tocca Fiano. Atteso: nessun esito su nessuna profezia;
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
  dipende, la «cannata collegata». L'originale, letto in sola lettura con `gog` il
  2026-10-05 (thread `19fb231b7df13ed5`, 14/08 alle 08:45), è firmato
  «Teresa e Maurizio» e conferma l'esito attuale: la correzione lo
  contraddice per costruzione, e nessuno dei due bracci ha accesso alla
  casella.

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

## Risultati e limiti

Otto run, giudicati alla cieca da una sessione separata; la mappa è stata
aperta dopo il giudizio e dopo due decisioni del custode sui dubbi sollevati
dal giudice.

- **Fixture di `nixos` viziata**: la correzione costruita contraddice
  `1ff314b`, che registra `svezia` spenta dalle 19:50 del 06/09 alle 08:55
  del 07/09. Il criterio è stato rivisto: con fonti in conflitto la
  gestione corretta è riaprire la lettura dipendente senza scegliere in
  silenzio e senza attribuire cause. Tutti e quattro i run la riaprono; tre
  vedono il conflitto, uno (`r2`) accetta la rettifica senza vederlo.
- **Conteggio di `nixos` ambiguo**: il 06/09 `norvegia` ha fatto un primo
  reboot sano dopo un rebuild, prima del guasto dell'08/09. Il criterio del
  filo non dice se un guasto azzera il conteggio, e i run arrivano a totali
  diversi. La situazione misura solo l'incremento dovuto al 05/10;
  l'ambiguità è un risultato per `nixos`, non un errore dei run.

Esiti per situazione (gestita in entrambi i run del braccio, altrimenti no):

- **`economia`, braccio A** (`r3`, `r4`): pertinente no (`r3` non nomina la
  profezia 6); irrilevante sì; scadenza no (`r3` non fa emergere né la P8 né
  la P5, `r4` la sola P8); correzione no (`r3` non conserva il
  predecessore);
- **`economia`, braccio B** (`r1`, `r2`): pertinente sì; irrilevante sì;
  scadenza parziale in entrambi, perché la P8 emerge corroborata e la P5
  emerge ma come avverata invece che mista; correzione sì;
- **`nixos`, braccio A** (`r2`, `r3`) e **braccio B** (`r1`, `r4`): tutte e
  quattro gestite in tutti i run.

Condizione di caduta: **il modello non si generalizza**.

- in `nixos` la pratica corrente non manca nessuna situazione: il filo i3
  porta già criterio, conteggio e data di rivalutazione, e il ciclo li
  esercita;
- in `economia` il modello migliora la pratica e la rende stabile: il
  braccio A ha due run molto diversi, il B no. Ma non gestisce del tutto la
  scadenza, perché sulla P5 il giudizio diverge dall'esito ratificato.
  Contare la sola emersione, come fa la riga della condizione di caduta,
  darebbe la scadenza per gestita: l'esito non cambierebbe, perché la
  caduta viene da `nixos`.

Che cosa dice: il valore sta dove un'ipotesi non ha già un presidio. In
`economia` le profezie non compaiono nella skill `eval`, non hanno un
orizzonte dichiarato e il loro riesame dipende da chi legge; in `nixos`
l'ipotesi vive nel filo con conteggio e data, e il ciclo la trova. È la
regola più piccola prevista dal task: **ogni ipotesi in attesa dichiara
orizzonte e riscontro con fonte, ed è raggiungibile da `eval`**. Dove già
lo è, come nel filo di `nixos`, non serve altro; il resto del modello
(facet `tipo`, separazione obbligata dei contenitori, presidio per tutti gli
adottanti) non ha dimostrato di servire.

Limiti: due run per braccio; una fixture viziata e corretta dopo il
giudizio, prima della mappa; il criterio della P5 è stato ratificato prima
dei run ma resta un giudizio. Deviazioni di protocollo senza effetto sui
giudizi: `nixos-r3` ha proseguito con un `/exec plan` non chiesto,
`nixos-r4` ha eseguito `hostname`.

## Perimetro osservato, non validazione aggiuntiva

Le fotografie dei cinque altri adottanti non decidono la generalizzazione:
`salute` a `e8e323a` conserva letture esplorative in prosa; `bi` a `4be04bcb`
ha prodotti runtime e contratti JSON, a cui non si impone frontmatter;
`crm` a `d638a64` distingue incognite ancora non formulate come ipotesi
nell'import clienti e un esito Twenty da cui dipende la scelta corrente;
`baserow` a `3a84767` ha i2 vuota legittimamente e un'attesa operativa sul
warning Redis; `danea-auto` a `c3acb33` offre l'osservazione sotto.
Sono indizi sui file, non collaudi conclusi del modello né verifiche live.

Il conteggio dei file i3, cursori compresi, nei sei adottanti allora presenti
passa da 37 a 19: misura registrata il 2026-10-05 sui commit di potatura
`3c8d84b` (economia), `068e25b` (nixos), `ae9a174` (salute),
`f1e304b5` (bi), `8d0e338` (crm), `230f1e2` (danea-auto).
Non prova che quelle potature abbiano perso letture vive.

Resta una lezione sulle fonti: il giro email di `economia` del 19/08,
pur dichiarando copertura dal 14/08, aveva perso la risposta di Teresa e
Maurizio del 14/08 su cui poggiava P7; la cattura è arrivata il 2026-10-05
(`97c644f`). La finestra dichiarata di un giro non certifica la copertura.

## Osservazione aperta: danea-auto

**Presidio in attesa.** Orizzonte dal **2026-10-13**, con osservazione
valutabile almeno fino al **2026-10-17** per l'assenza del precursore.
`eval interpret` di `metodo` la raggiunge dalle
[Scadenze del plan](../o1/plan.md#scadenze). Il riesame legge i commit
pubblicati di `danea-auto`: trailer `Esiti:` e diff di
`i3/rallentamento-libreoffice.md`; il dato di dominio proviene da
`o3/stats.ps1` e dalla soglia di `kb/affidabilita-gui.md`.
Se non arriva un giro `eval` o manca la copertura, il riscontro resta
mancante e si dichiara il prossimo riesame: nessun silenzio vale come esito.

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

L'ipotesi osservativa di `metodo` è che il presidio corrente faccia emergere
la scadenza da solo. Non ricordarla alle sessioni dell'adottante. Se prima
del giro la skill locale cambia per recepire la prescrizione, dichiarare
la contaminazione: il risultato non misurerebbe più la pratica precedente.
Il 2026-10-09 il custode ha scelto di far recepire subito a `danea-auto`
`delega-ciclo` e `goal-senza-fotografia`, che toccano anche `eval`,
accettandone il costo: un repository in osservazione non deve fermare il
canone. Il riesame lo dichiara come limite. Restano escluse
`presidio-ipotesi` e ogni menzione dell'ipotesi o della scadenza.
Il recepimento (`bf186fb`) non nomina l'ipotesi né la scadenza, ma
`autonomy.md` locale delega il ripristino di LibreOffice incastrato:
una chiusura delle istanze `soffice` da parte dell'agente rinnova l'istanza
e ricade nell'esito «non valutabile». Il riesame la cerca nei commit e
nelle diagnostiche prima di leggere le righe di ritentativo. Il 2026-10-09
`danea-auto` ha recepito anche `pull-autonomo` (`e7b3bad`): il fork di
`/method` ora aggiorna da solo il checkout di `method`, che contiene questa
nota, e `eval perceive` ha un formato dei casi più ricco. Il commit non
nomina l'ipotesi né la scadenza; il riesame dichiara entrambe le modifiche
come limite.
Il trailer da solo non certifica il riesame della specifica ipotesi.
