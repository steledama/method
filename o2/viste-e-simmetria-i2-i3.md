---
sintesi: "Restituire a i2 le ipotesi interpretative esposte alla prova del Mondo e a i3 il cruscotto dei confronti contro il Goal: eval verifica le ipotesi sui nuovi eventi i1 e conserva anche gli esiti falsificati. Provare il modello su nixos, salute, economia e bi prima di incidere il canone; separare il deck dalle viste derivate e migrare senza perdere letture, cursori o servizi."
ciclo: dev
---

# Viste, presentazione e simmetria i2/i3

Decisione del custode (2026-10-04), nata dalla revisione della presentazione:
in `presentation/` convivono due cose diverse, e la confusione si è
propagata fino allo stadio i2.

- **Viste**: la traduzione 1:1 di un `.md` in una pagina HTML, con la
  navigazione. Derivate, rigenerate, mai scritte a mano (`kb/view.md`).
- **Presentazione**: l'unico deck Reveal, il racconto curato
  dell'artefatto. Scritta, non derivata. Non è uno stadio: la home la
  linka come voce a sé.

Il deck di `metodo` oggi occupa i2 (`i2/metodo-in-sintesi.md` e le tavole),
mescolando il racconto curato dell'artefatto con l'interpretazione dei segnali.
La separazione deve restituire a i2 una funzione autonoma. Negli adottanti
alcuni deck sono invece sintesi di dominio generate dai dati: la loro funzione
interpretativa non scompare cambiando formato o cartella.

## Direzione concordata e modello da verificare

La revisione con il custode del 2026-10-04 ha portato il centro del task dalla
simmetria delle cartelle al presidio delle **convinzioni ancora esposte alla
prova del Mondo**. La direzione è concordata; cardinalità, schema e ciclo di
vita si provano sui casi prima di diventare obblighi canonici.

- **i2 rende concreta la lettura**: evidenze e provenienza, chiavi
  interpretative, ipotesi, alternative, assunzioni e limiti. Qui vivono le
  ipotesi da verificare, comprese le previsioni oggi raccolte nell'Angolo di
  Nostradamus di `economia`. La lettura è orientata dal Goal sulla rilevanza;
  spiegare o prevedere non equivale a giudicare il successo rispetto al Goal.
- **i3 governa i confronti**: una tabella delle questioni valutative vive,
  collegata alle letture i2, con obiettivo, giudizio corrente e condizione di
  riesame. L'ordine esprime priorità di attenzione e verifica; il plan mantiene
  la priorità dell'azione. Una questione può essere importante mentre non
  autorizza ancora nessuna mossa.
- **Il legame è esplicito, la biunivocità non è presupposta**: ogni confronto
  raggiunge il materiale che lo sostiene; una sintesi può alimentare più
  confronti o restare utile senza un confronto aperto. Ogni ipotesi che attende
  verifica deve però essere raggiungibile dal presidio di `eval`, anche quando
  non richiede una propria riga i3. Il contratto deve impedire ipotesi
  dimenticate senza creare confronti fittizi per completare una coppia.
- **La verifica e la chiusura sono distinte**: chiudere un task, stabilizzare
  un giudizio operativo e confermare una spiegazione sono eventi diversi.
  L'esito di un'ipotesi resta consultabile dopo la chiusura del confronto;
  anche una falsificazione è materiale cognitivo vivo, non solo storia Git.

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

Una corroborazione non prova automaticamente la causa o l'intenzione attribuita.
L'assenza di dati non è conferma né falsificazione; il mancato evento vale come
riscontro solo se finestra e copertura dell'osservazione lo consentono. Le
ipotesi composte si separano quando una conferma parziale nasconderebbe una
smentita. Probabilità numeriche e previsioni non sono campi obbligatori: alcune
letture esplorative richiedono domande discriminanti, non una falsa precisione.

La formulazione e il criterio originari non si riscrivono alla luce dell'esito.
Una revisione dichiara cosa cambia e perché, conservando il predecessore e il
suo esito. Definire come mantenere consultabili ipotesi corroborate e
falsificate senza accumulare cronache o un secondo indice manuale: la sede
resta i2, la forma di conservazione è da provare. La promozione di conoscenza
nella KB richiede giudizio e non cancella il precedente necessario a ricordare
una smentita. Il tono locale di Nostradamus può restare; il presidio della
verifica deve funzionare senza dipendere da quel nome o da un singolo dominio.

## Presidio della skill eval

Il futuro protocollo deve collegare esplicitamente i1 → i2 → i3:

1. **Perceive** rende riconoscibili gli eventi nuovi e le fonti raggiungibili.
   La presenza di un file, la sua data di modifica o l'ultimo commit non
   certificano da soli che un evento sia stato valutato.
2. **Interpret** controlla quali ipotesi possono ricevere riscontro dagli
   eventi, leggendo anche materiale di casa e fonti primarie. Registra
   riscontri, alternative, esiti e correzioni alle sintesi dipendenti.
3. **Compare** giudica le conseguenze rispetto al Goal e aggiorna i confronti;
   rende espliciti gli eventuali impatti sul plan, senza eseguire azioni per il
   solo fatto che una previsione si sia avverata.

Ogni giro con nuovi eventi dichiara quali ipotesi ha controllato, quali non sono
pertinenti e quali restano non verificabili. Un controllo periodico cerca
ipotesi il cui evento o orizzonte è già arrivato e riscontri rimasti senza
confronto, anche quando non sono entrati nuovi eventi nel giro. Deve consentire
di riaprire un'ipotesi precedentemente corroborata quando emergono smentite.

Definire un riferimento persistente al materiale già valutato e una modalità
di rilettura dopo correzioni delle fonti, senza replicare il registro i1 o
promettere copertura semantica automatica. L'inventario e i link sono
verificabili deterministicamente; pertinenza, sufficienza e indipendenza delle
evidenze richiedono giudizio. Un esito di supervisione resta soggetto alla
ratifica prevista dalle skill: rilevare e proporre non significa applicare
automaticamente nuovi giudizi, goal o azioni. Cadenza e sede delle tracce di
verifica vanno definite nella prova, evitando log di sessione nei confronti.

## Prima analisi degli adottanti e prova del modello

Analisi del 2026-10-04 sui checkout locali, puliti e allineati ai rispettivi
`origin/main`; nessuna verifica live degli host, delle controparti o degli
eventi sanitari. Riferimenti Git e file sono fonti della diagnosi degli
artefatti, non conferme indipendenti dei fatti esterni.

- **nixos**, potatura `068e25b`: quattro fili eliminati, con regole consolidate
  nella KB e lavoro nei task. La lettura causale del boot resta distribuita fra
  `i2/nixos-in-sintesi.md`, `o2/investigate-server-boot-recurrence.md` e
  `i3/affidabilita-boot-server.md`. Prova: separare spiegazioni e alternative,
  raccolta delle evidenze e giudizio operativo. Tre reboot sani per server
  possono chiudere come «non ricorso», senza dimostrare la causa del guasto.
- **salute**, potatura `ae9a174`: tre fili eliminati; baricentro accorpato al
  quadro corporeo e domande autobiografiche conservate in
  `i2/educazione-cattolica.md`. Prova: rabbia inavvertita e tenuta della pratica
  dopo il ritiro, distinguendo regolarità delle sedute e cambiamento nelle
  relazioni. Una lettura può sostenere più confronti; un'interpretazione
  esplorativa può rimanere utile senza un confronto aperto.
- **economia**, potatura `3c8d84b`: quattro fili eliminati; fonti, lente
  patrimonio/reddito e linea Fiano ricollocate nella KB e nei task. Prova:
  istituzionalizzare le ipotesi di `i2/angolo-nostradamus.md` conservando criteri
  anteriori ed errori. La profezia 8 sulla risposta di Orsi è ancora «aperta»
  mentre altri materiali riportano il chiarimento successivo: riesaminarla
  contro il documento originale, senza dedurne qui un esito definitivo.
- **bi**, potatura `f1e304b5`: quattro fili eliminati, con contenuti stabili
  ricollocati e monitoraggio automatico conservato. Prova: i presidi del ciclo
  giornaliero che attendevano il primo fallimento reale, oltre alle ipotesi
  correnti su drift e orfani. Una regola implementata non ha ancora dimostrato
  efficacia sul guasto reale; il presidio di quell'attesa deve restare visibile.
  Conservare i contratti runtime dei JSON e verificare la disponibilità della
  serie di riscontri: un report riscritto a ogni run non è una serie storica.

Per ciascun caso produrre una proposta concreta di i2 e riga i3, indicando
cosa cambia, cosa non ha riscontro e dove vivono dati ed esiti. Valutare se la
nuova forma riduce duplicazioni e rende più facile cambiare idea. Nessuna
migrazione degli adottanti è implicita in questa prova.

## Cartelle

Una sola cartella generata e servita, chiusa su se stessa: `serve.py` serve
una cartella e la home deve linkare il deck senza uscirne.

```
presentation/   sorgente del deck: presentation.md e tavole
view/           generata: index.html, presentation.html, pagine che
                ricalcano i path del repo (goal.html, o1/plan.html,
                o2/*.html, i2/*.html, i3/*.html, …), assets/
o3/view/        i builder (oggi o3/presentation/)
```

Ricalcare i path facilita la riscrittura dei link: un `.md` reso diventa il suo
`.html`, un file non reso resta etichetta. Definire il perimetro delle fonti
rese e degli asset, anche per symlink, dati personali e prodotti runtime:
non si pubblica automaticamente ogni `.md` del checkout. «1:1» significa
fedeltà al contenuto e alla struttura della pagina sorgente; non restringe
la nozione generale di vista derivata, che può essere una sintesi o un grafico.

## Fasi

1. **Prova e specifica del modello.** I quattro casi sopra, schema minimo di
   ipotesi e confronti, conservazione degli esiti, copertura di `eval` e
   destinazione di cursori e contratti come `i3/allineamento-metodo.md`.
   Esplicitare le decisioni ancora aperte e sottoporre il modello al custode
   prima di incidere il canone.
2. **Canone.** Nodi `view` (resa delle pagine, build, servizio sulle reti private),
   `presentation` (il racconto curato dell'artefatto e la sua fedeltà alle
   fonti, distinto dalle viste derivate), `verdict`, `interpret`,
   `compare`, `project-structure`, `plan`, `tasks` e `specify` dove toccati.
   Skill `eval` (eventi, ipotesi, riscontri e confronti), `adottanti`, `method`
   (cursore e migrazione) e `commit` (filing back e nuova build).
   `CLAUDE.md` e `README.md`, compresa l'eccezione tabellare di i3. Commit
   coerente dei nodi interdipendenti, con transizione dichiarata per gli
   adottanti che li leggono via symlink ma non hanno ancora migrato.
3. **Ristrutturazione di `metodo`.** Deck e tavole in `presentation/`;
   i cinque fili riletti secondo il modello validato; triage degli altri file di
   `i2/` (`potatura-kb` conclusa, `baricentro-kb-adottanti` materiale di
   nodo, `bootstrap-adottanti` e `ingresso-adottante` da rileggere).
   **Rivalutazione della potatura** `5ea8204` (sedici fili ridotti a
   cinque): il criterio era «un filo misura un obiettivo», e senza una
   casa per la lettura a valenza sospesa alcune interpretazioni vive
   possono essere state cacciate insieme ai verdetti morti. Per ogni filo
   rimosso: chiuso a ragione, salito in un nodo, oppure lettura da
   ripristinare in i2, con il presidio di verifica pertinente. Non associare
   automaticamente una riga i3 a ogni materiale recuperato.
4. **Builder.** Pagine fedeli alle fonti con Pandoc e riscrittura dei link; barra di
   navigazione comune (home, indice della collezione, pallini sul filo
   d'accento per le collezioni a sequenza, orizzontale su schermo stretto);
   `goal.html` con un'ancora per obiettivo, destinazione della chiave
   `Ob.`; `plan.html` con dipendenze e scadenze, tabella a scorrimento
   proprio; home col link «Presentazione». Etichetta «Confronti» al posto
   di «Verdetti»; sigle degli stadi nel colore neutro, non `--warm`.
   Contratti su riferimenti, obiettivi, ipotesi e riscontri secondo lo schema
   validato; nessuna pretesa di certificare semanticamente un esito con la build.
   Coordinare il cambio della cartella servita col servizio di `metodo` quando
   avviene, prima della propagazione agli adottanti.
5. **Prescrizione ai sei** in `o3/`: migrazione di cartelle e fili, la
   rivalutazione delle proprie potature recenti dei fili (da 38 a 19
   nell'aggregato) con lo stesso criterio della fase 3, e il nuovo path
   nei servizi permanenti degli host (`nixos`, `danea-auto` su `danea2`)
   che oggi controllano `presentation/index.html`. Il deck di `nixos` si
   riscrive distinguendo racconto dell'artefatto e interpretazione del boot.
   Ogni adottante decide e applica la migrazione nel proprio dominio;
   preservare funzioni interpretative dei deck generati e contratti runtime.

## Feedback

- I quattro casi rendono distinguibili evidenze, ipotesi, giudizio contro il
  Goal e azioni. Nessuna spiegazione risulta confermata per la sola chiusura
  operativa del problema.
- Un evento i1 pertinente raggiunge un'ipotesi e ne provoca il riesame; un
  evento irrilevante non forza un esito. Dati mancanti restano tali.
- La prova su Nostradamus verifica il caso rimasto aperto e mantiene
  consultabili almeno un esito falsificato e uno corroborato, con formulazione
  e criterio originari. Un nuovo riscontro contrario può riaprire la lettura.
- La build passa col contratto di riferimenti validato e il presidio del compartimento
  stagno su `view/`.
- Ogni pagina si apre via `file://` e via `serve.py`; la navigazione regge a
  larghezza mobile.
- La rivalutazione delle potature dichiara per ogni filo rimosso l'esito,
  anche quando è «chiuso a ragione».
- Il battito `/adottanti` successivo alla prescrizione legge la migrazione
  nei file, non nei marker.

## Vincoli

- Nessuna vista derivata mantenuta a mano; le sorgenti possono essere Markdown
  o dati strutturati secondo il dominio. Il racconto curato dell'artefatto è
  distinto dalle interpretazioni e dalle loro rese grafiche.
- Nessuna potatura elimina ipotesi ancora da verificare, esiti cognitivamente
  utili, cursori o contratti senza una destinazione esplicita e raggiungibile.
- Il task non autorizza modifiche al Goal, azioni runtime o migrazioni negli
  adottanti per effetto della sola ristrutturazione.
- La rinomina della cartella servita non si fa senza aggiornare nello stesso
  giro i servizi permanenti degli host: un servizio fermo in silenzio è
  l'«assenza leggibile» mancata.
- Le fasi 1–4 si chiudono in `metodo` prima di prescrivere ai sei; la finestra
  di transizione fra canone e adottanti è esplicita.
