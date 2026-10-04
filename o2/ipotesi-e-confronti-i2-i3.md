---
sintesi: "Provare su economia e nixos, poi salute e bi, un modello in cui i2 tiene le ipotesi interpretative esposte alla prova del Mondo e i3 i confronti contro il Goal, con eval che verifica le ipotesi sui nuovi eventi i1 e conserva gli esiti finché condizionano una lettura. Misurare prima il bisogno sulle potature recenti; consegnare al custode un modello da ratificare, con la propria condizione di caduta, senza incidere il canone."
ciclo: dev
---

# Ipotesi e confronti i2/i3

Task di prova, non di migrazione. Nato il 2026-10-04 dalla revisione della
presentazione e separato lo stesso giorno da
[viste-e-presentazione](viste-e-presentazione.md): liberare i2 dal deck non
dice ancora che cosa i2 debba custodire, e la risposta va provata sui casi
prima di diventare obbligo canonico. Il suo prodotto è un modello sottoposto al
custode; canone, ristrutturazione di `metodo` e prescrizione ai sei nascono
come task propri solo dopo la ratifica.

## Il problema

Il canone non ha casa per le **convinzioni sul Mondo ancora esposte alla
prova**. `kb/verdict.md` manda l'ipotesi in attesa allo `stato: bozza` del suo
nodo: copre le ipotesi sul canone, non la causa del boot di `nixos`, la
profezia su Orsi di `economia` o la rabbia inavvertita di `salute`. Il
criterio «un filo misura un obiettivo» ha potato i fili senza obiettivo, e la
lettura a valenza sospesa non aveva altro posto. Le potature recenti — `5ea8204`
in `metodo` (sedici fili ridotti a cinque), da 38 a 19 nell'aggregato dei sei
— possono aver cacciato letture vive insieme ai verdetti morti. È un sospetto
fondato, non ancora misurato.

## Direzione concordata e modello da verificare

La revisione con il custode del 2026-10-04 ha concordato la direzione;
cardinalità, schema e ciclo di vita si provano sui casi.

- **i2 rende concreta la lettura**: evidenze e provenienza, chiavi
  interpretative, ipotesi, alternative, assunzioni e limiti. Qui vivono le
  ipotesi da verificare, comprese le previsioni oggi raccolte nell'Angolo di
  Nostradamus di `economia`. La lettura è orientata dal Goal sulla rilevanza;
  spiegare o prevedere non equivale a giudicare il successo rispetto al Goal.
- **i3 governa i confronti**: le questioni valutative vive, collegate alle
  letture i2, con obiettivo, giudizio corrente e condizione di riesame.
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

## Ipotesi e riscontri

Provare una forma minima che renda riconoscibili:

- formulazione originaria, autore, data e fonti disponibili in quel momento;
- lettura alternativa e osservazione che permetterebbe di distinguerle;
- criterio di verifica stabilito prima del riscontro, con evento atteso o
  orizzonte temporale quando pertinenti;
- riscontri effettivi con provenienza e data, distinti dalle inferenze;
- esito motivato: in attesa, corroborata, falsificata, mista o non valutabile,
  con limiti del riscontro e conseguenze sulla lettura corrente.

La forma completa vale per le ipotesi con un evento atteso o un orizzonte: sono
quelle che il presidio di `eval` deve raggiungere. Una lettura esplorativa
resta prosa i2 con le sue domande discriminanti, senza scheda. La prova dice se
il gradiente regge o se una delle due forme assorbe l'altra.

Una corroborazione non prova automaticamente la causa o l'intenzione attribuita.
L'assenza di dati non è conferma né falsificazione; il mancato evento vale come
riscontro solo se finestra e copertura dell'osservazione lo consentono. Le
ipotesi composte si separano quando una conferma parziale nasconderebbe una
smentita. Probabilità numeriche e previsioni non sono campi obbligatori.

La formulazione e il criterio originari non si riscrivono alla luce dell'esito.
Una revisione dichiara cosa cambia e perché, conservando il predecessore e il
suo esito. Il tono locale di Nostradamus può restare; il presidio della
verifica deve funzionare senza dipendere da quel nome o da un singolo dominio.

## Permanenza degli esiti

È la decisione centrale e contraddice il canone vigente: `kb/verdict.md` vuole
lo stato aggiornato in place e la storia in Git, mentre una falsificazione è
materiale cognitivo vivo. Criterio proposto, da provare: **un esito resta in i2
finché condiziona una lettura corrente** — la profezia 0 di `economia` tiene
viva la calibrazione su Caprioli. Quando non condiziona più nulla ne resta la
lezione, nella sintesi o in un nodo, e il dettaglio torna a Git. Senza un
criterio del genere «conserva anche le falsificazioni» diventa un registro
perpetuo (cfr. `i1/registro-perpetuo-vs-cattura-singola.md`); Nostradamus,
281 righe, è il banco di prova. La promozione nella KB richiede giudizio e non
cancella il precedente necessario a ricordare una smentita.

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

Il costo va tenuto basso. Un resoconto per giro di ogni ipotesi controllata,
non pertinente o non verificabile cresce con ipotesi × eventi; un cursore sul
materiale già valutato rischia di replicare il registro i1. Ipotesi da provare
per prima: la parte deterministica si riduce a un campo di orizzonte nel
frontmatter delle ipotesi, che l'audit `o3/kb_tools.py` segnala alla scadenza
come già fa coi contratti; il conto del giro entra nel trailer `Esiti:`
esistente invece che in un nuovo registro. Pertinenza, sufficienza e
indipendenza delle evidenze restano giudizio; rilevare e proporre non
significa applicare nuovi giudizi, goal o azioni senza la ratifica prevista
dalle skill.

## Prova

### Prima: misurare il bisogno

Rileggere i sedici fili rimossi da `5ea8204` con il modello in mano: per ciascuno
«chiuso a ragione», «salito in un nodo» oppure «lettura da ripristinare in i2»,
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
  adottante che pratica già criteri anteriori ed errori conservati. Prova:
  istituzionalizzare le ipotesi di `i2/angolo-nostradamus.md` e applicarvi il
  criterio di permanenza. La profezia 8 sulla risposta di Orsi è ancora
  «aperta» mentre altri materiali riportano il chiarimento successivo: è
  un'ipotesi scaduta senza presidio, da riesaminare contro il documento
  originale senza dedurne qui un esito.
- **nixos**, potatura `068e25b`: quattro fili eliminati, con regole
  consolidate nella KB e lavoro nei task. La lettura causale del boot resta
  distribuita fra `i2/nixos-in-sintesi.md`,
  `o2/investigate-server-boot-recurrence.md` e
  `i3/affidabilita-boot-server.md`. È il caso canonico di chiusura ≠
  spiegazione: tre reboot sani per server possono chiudere come «non
  ricorso», senza dimostrare la causa del guasto.
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

Per ciascun caso produrre una proposta concreta di i2 e riga i3, indicando
cosa cambia, cosa non ha riscontro e dove vivono dati ed esiti. Nessuna
migrazione degli adottanti è implicita in questa prova.

## Condizione di caduta

Proposta da ratificare prima di aprire i casi, come il task chiede alle
ipotesi che presidia. Il modello non sale a canone se:

- la rilettura di `5ea8204` non trova letture da ripristinare, o le poche
  trovate hanno già casa in un nodo `bozza` o in un task;
- in `nixos`, `salute` o `bi` la scheda produce campi senza un'osservazione
  che distingua davvero le alternative, o ripete il confronto i3 senza ridurre
  duplicazioni;
- il criterio di permanenza non impedisce a Nostradamus di crescere, o
  l'applicarlo fa perdere una lezione che il custode considera viva.

In quei casi l'esito è una regola più piccola — per esempio il solo campo di
orizzonte sulle letture i2 esistenti — oppure il riconoscimento che la pratica
resta di dominio in `economia`.

## Decisioni da consegnare al custode

- schema minimo e gradiente tra ipotesi con orizzonte e letture esplorative;
- criterio di permanenza degli esiti;
- forma di i3: file per confronto con indice tabellare come o1 e o2, oppure
  sola tabella; dove vive la prosa del giudizio, dato che i2 sospende la
  valenza e una cella è illeggibile a larghezza mobile (`CLAUDE.md`);
- destinazione di cursori e contratti come `i3/allineamento-metodo.md`;
- etichetta della collezione i3: «Verdetti» o «Confronti», con rinomina dei
  nodi `verdict` e `compare` o senza;
- copertura e costo del presidio di `eval`;
- quali task nascono dopo la ratifica: nodi (`verdict`, `interpret`,
  `compare`, `plan`, `tasks`, `specify` dove toccati), skill `eval`,
  `adottanti`, `method`, `commit`, eccezione tabellare di i3 in `CLAUDE.md`,
  triage di `i2/` in `metodo` (`potatura-kb` conclusa,
  `baricentro-kb-adottanti` materiale di nodo, `bootstrap-adottanti` e
  `ingresso-adottante` da rileggere), prescrizione ai sei.

## Feedback

- La rilettura di `5ea8204` dichiara per ogni filo rimosso l'esito, anche
  quando è «chiuso a ragione».
- I casi rendono distinguibili evidenze, ipotesi, giudizio contro il Goal e
  azioni. Nessuna spiegazione risulta confermata per la sola chiusura
  operativa del problema.
- Un evento i1 pertinente raggiunge un'ipotesi e ne provoca il riesame; un
  evento irrilevante non forza un esito. Dati mancanti restano tali.
- La prova su Nostradamus verifica il caso rimasto aperto e mantiene
  consultabili almeno un esito falsificato e uno corroborato, con formulazione
  e criterio originari. Un nuovo riscontro contrario può riaprire la lettura.
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
