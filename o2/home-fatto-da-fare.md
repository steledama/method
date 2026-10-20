---
sintesi: "La home della vista apre con «fatto», «da fare» e il ciclo autonomo: una riga per tentativo col semaforo verde, giallo o rosso che porta alla pagina del giro; proposte pendenti e tentativi restano visibili."
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

## Il ciclo autonomo nella home

Decisione del custode del 2026-10-11, dopo il primo giro reale (`salute`,
gradino 0): la manifestazione del ciclo autonomo nella vista va **in parallelo** al
ciclo autonomo stesso, non dopo. È la punta degli strumenti di controllo e verifica,
la gamba che fa da bilancia all'autonomia: senza, il giro autonomo apre un
golfo di valutazione ([action-cycle](../kb/action-cycle.md), visibilità e
feedback). È prerequisito del gradino 1 del [pilota](pilota-ciclo-autonomo.md).

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

### Contratto del ciclo autonomo nella vista

Ratificato dal custode il 2026-10-11; si implementa nel canone
(`o3/view/`) e si prescrive a tutti. Un repo senza ciclo autonomo rende la sezione
vuota con la sua ragione: la direzione è comune, i tempi no.

**Due strati.** La release resta costruita dal commit (`build.py --publish`,
provenienza = hash). Il ciclo autonomo è stato operativo che cambia anche senza
commit: un tentativo fermato prima del commit non innesca nessuna
pubblicazione. Non entra quindi nella release ma si legge **a richiesta**,
come `/_stato` rende già `status.json`: `serve.py` riceve la cartella di
stato (`--ciclo-state`, passata dal modulo `presentations` di `nixos`) e
rende `/_ciclo/` e `/_ciclo/<id>`. Ogni lettura dichiara il proprio
momento, distinto dalla revisione della release. Ciclo autonomo e pubblicazione di
un repo stanno quindi sullo stesso host: in `nixos` diventa un vincolo fra
`cicli.nix` e `presentations.nix`.

**Fonte**, contratto col modulo `cicli` di `nixos`
(`~/.local/state/ciclo/<repo>/`):

- `tentativi.jsonl`: una riga `partenza` e una `chiusura` per tentativo,
  stesso `id` (`INVOCATION_ID`); la chiusura porta esito, motivo, codice,
  commit, push, tree sporco, permessi negati, costo, durata, `attenzione`;
- `giri/<id>.jsonl`: lo stream del giro; `decisioni.json`: stato e cadenza
  del repo, per calcolare le partenze mancate.

**Righe nella home**: gli ultimi cinque tentativi, dal più recente, caricati
da uno script inline che legge `/_ciclo/` (se lo script non gira resta il
collegamento alla pagina), con data e ora,
semaforo, esito in parole e collegamento alla pagina del giro. Stati senza
tentativi, distinti fra loro: «nessun ciclo autonomo dichiarato» (repo assente da
`decisioni.json`), «fuori nixos» (stato `esterno`), «mai partito», «fonte
non leggibile» (stato dichiarato ma cartella assente o illeggibile).

**Semaforo**, calcolato da campi espliciti; il giudizio dell'agente alza,
non abbassa:

- **rosso**: esito diverso da riuscito (arresto, errore, timeout); commit
  senza push; partenza senza chiusura oltre il tempo massimo; con stato
  `timer`, nessuna partenza entro la cadenza più una tolleranza;
- **giallo**: riuscito, ma con permessi negati, oppure `attenzione` non
  nulla o assente, oppure trailer `Prossimo:` assente o diverso da quello
  precedente nella storia (cambio di priorità, anche se dichiarato
  confermato);
- **verde**: riuscito, commit e push, nessun permesso negato,
  `attenzione` nulla. Un giro tutto vuoto è verde.

`attenzione` viene dal resoconto dell'agente: il prompt del ciclo autonomo lo fa
chiudere con una riga `Attenzione: nessuna` oppure `Attenzione: <voci>`
(proposte «da decidere», incertezze, errori dichiarati), che lo script di
chiusura estrae. La riga mancante vale giallo: l'assenza di un segnale non è
un via libera.

**Pagina del giro**: metadati del tentativo (inizio, durata, costo, codice,
motivo, commit con i trailer, push), il resoconto finale reso come pagina,
le voci di `attenzione`, gli atti sul Mondo e l'elenco dei comandi e degli
strumenti invocati ricavato dallo stream; lo stream completo resta
scaricabile. Eredita il compartimento della vista del repo: in `salute`
dati sanitari, serviti in LAN come il resto.

**Percorso**: contratto ratificato → implementazione nel canone `o3/view/`
(`serve.py`, home) con verifiche su uno stato di prova → modulo
`presentations` e chiusura del ciclo autonomo in `nixos` (`--ciclo-state`, campo
`attenzione`) → prescrizione `o3/` ai sette, `salute` per primo perché ha un
ciclo autonomo vero da mostrare.

## Contratto di supervisione e riuscita

La home deve rendere distinguibili l'ultimo commit riuscito e l'ultimo
tentativo del ciclo autonomo: un giro interrotto prima del commit, un push rifiutato
o una partenza mancata non diventano un successo per assenza di nuovi commit.
Il task [Dove gira il ciclo autonomo](dove-gira-il-ciclo-autonomo.md) definisce fonte,
freschezza e stati dei tentativi; qui si definisce come leggerli. Finché la
fonte non esiste, la vista dichiara il dato non disponibile.

- «Fatto» conserva gli ultimi cinque commit; le proposte ancora da decidere
  restano raggiungibili anche quando escono da quel campione. La loro fonte
  e il loro consumo sono definiti in [Criteri del ciclo autonomo schedulato](criteri-autonomia.md).
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
