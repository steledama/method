---
sintesi: "La home della vista apre con «fatto», «da fare» e il battito: una riga per tentativo col semaforo verde, giallo o rosso che porta alla pagina del giro; proposte pendenti e tentativi restano visibili."
ciclo: dev
---

# Home con fatto e da fare

Più autonomia all'agente chiede un controllo che il custode legge in un
colpo d'occhio. La vista web è il luogo: le due sezioni stanno in cima alla
home, prima dei poli Goal e World.

## Le due sezioni

- **Fatto**: gli ultimi 5 commit, con data e ora, titolo, autonomia e
  impatto vestito col semaforo, e il motivo leggibile accanto. La fonte è `git log` con i trailer, letto dall'host che pubblica
  dal commit.
- **Da fare**: la prossima mossa pronta nell'ordine del plan, le scadenze
  ordinate per data e le dipendenze `w`/`p` di `o1/plan.md`, anche senza
  data. Oggi si leggono solo aprendo il plan.

## Vincoli

- È un cambio del canone delle viste (`kb/view.md`, builder in `o3/view/`):
  si prescrive agli adottanti come gli altri.
- «Da fare» non dipende da nulla e può partire subito. «Fatto» mostra
  `Esiti:` e i trailer `Autonomia:`/`Impatto:` dove ci sono, già in `/commit`.
- La pubblicazione costruisce da `git archive`: verificare come il builder
  legge la storia senza rompere il contratto del commit pulito.

## Il battito nella home

Decisione del custode del 2026-10-11, dopo il primo giro reale (`salute`,
gradino 0): la manifestazione del battito nella vista va **in parallelo** al
battito stesso, non dopo. È la punta degli strumenti di controllo e verifica,
la gamba che fa da bilancia all'autonomia: senza, il giro autonomo apre un
golfo di valutazione ([action-cycle](../kb/action-cycle.md), visibilità e
feedback). È prerequisito del gradino 1 del [pilota](pilota-battito.md).

- **Riga di log nella home**, una per tentativo recente, col semaforo:
  - **verde**: giro riuscito, commit e push, niente che chieda attenzione;
  - **giallo**: giro riuscito ma con qualcosa per il custode (proposte «da
    decidere», permessi negati, incertezze o errori dichiarati, commit senza
    push);
  - **rosso**: blocco — arresto all'avvio, errore, timeout, push rifiutato,
    partenza mancata rispetto alla cadenza.
- **Pagina del giro**: cliccando la riga si atterra su una pagina HTML col
  report completo: resoconto finale dell'agente, esiti per stadio, atti sul
  Mondo, proposte, metadati del tentativo (durata, costo, codice, commit e
  push) e il percorso allo stream dei comandi.

Vincoli da risolvere nel progetto:

- La fonte è lo stato host-locale dell'unità (`~/.local/state/battito/<repo>/`,
  modulo `battiti` di `nixos`), non la storia git: il builder la legge
  dall'host che pubblica. Pubblicazione e battito devono stare sullo stesso
  host, oppure lo stato deve viaggiare.
- Un tentativo fermato prima del commit non innesca la pubblicazione: la
  chiusura dell'unità deve aggiornare la vista anche senza commit.
- Il semaforo si calcola da campi espliciti della riga di chiusura e del
  resoconto, non da un giudizio sul testo; la regola va scritta.
- Il report eredita il compartimento della vista del repo: in `salute` sono
  dati sanitari, serviti in LAN come il resto della vista.

## Contratto di supervisione e riuscita

La home deve rendere distinguibili l'ultimo commit riuscito e l'ultimo
tentativo del battito: un giro interrotto prima del commit, un push rifiutato
o una partenza mancata non diventano un successo per assenza di nuovi commit.
Il task [Dove gira il battito](dove-gira-il-battito.md) definisce fonte,
freschezza e stati dei tentativi; qui si definisce come leggerli. Finché la
fonte non esiste, la vista dichiara il dato non disponibile.

- «Fatto» conserva gli ultimi cinque commit; le proposte ancora da decidere
  restano raggiungibili anche quando escono da quel campione. La loro fonte
  e il loro consumo sono definiti in [Criteri del battito schedulato](criteri-autonomia.md).
- «Da fare» rende anche la prossima mossa pronta senza data, rispettando
  l'ordine del plan. Le attese senza data restano tali, senza date inventate.
- La storia estratta per la pubblicazione termina al commit esportato con
  `git archive`; una pubblicazione dello stesso commit non incorpora commit
  successivi. Lo stato operativo corrente dichiara separatamente provenienza
  e momento della lettura.

Il task si chiude quando il custode trova una mossa pronta, ricostruisce
motivo e impatto di un commit e raggiunge una proposta ancora pendente oltre
i cinque commit. Prima dell'avvio del pilota deve essere verificata anche
la resa di un tentativo fallito o non partito, usando la fonte concordata
con l'esecutore. La pubblicazione continua a rispettare i contratti delle viste.

## Register della delega

`autonomy.md` contiene la prima delega operativa del ciclo richiesto dal
custode. Il resoconto con diff e commit è già il controllo di quel giro;
la home deve renderne raggiungibili i criteri e le proposte pendenti prima
del pilota schedulato. Il register è per ora leggibile dal repository:
aggiungerlo al perimetro delle pagine e concordarne la resa nella home con
il residuo di `criteri-autonomia`, senza introdurre un nuovo stadio.
