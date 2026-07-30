---
ciclo: runtime
---

# Segnale: il verdetto deriva verso la storia migliore, e nessuna review guarda in quella direzione

Data: 2026-07-30 · Fonte: custode e agente, su esperienza `economia` (una
sessione con tre episodi indipendenti nello stesso giro)

## Il segnale

Tre casi osservati in una sola sessione, diversi per contenuto e identici per
forma: un artefatto i3 risultava **più sicuro, più elegante o più quantificato
del materiale che gli stava sotto**. La deriva non è casuale, ha una direzione:
va sempre verso la lettura più raccontabile.

**Caso 1 — il filo più ottimista del suo stesso task.** Un filo i3 registrava
una scoperta come «posta che crea denaro invece di ridistribuirlo». Il file
`o2/` corrispondente, scritto prima, portava già la cautela decisiva: la
controparte da cui incassare non è solvibile per l'importo in gioco, e nello
stesso stabile esiste un precedente di credito inesigibile. Il task era più
onesto del verdetto. Nessuna review confronta le due superfici: `plan-review`
guarda plan↔`o2/`, `verdicts-review` guarda filo↔segnali, e **filo↔`o2/` non è
di nessuno**.

**Caso 2 — narrativa costruita su una coincidenza, dall'agente.** Un pagamento
è arrivato per un importo che coincideva con la cifra di una controparte, e
l'agente ne ha ricavato una tesi forte («ha prevalso il numero di X, e questa è
la prova bancaria della lettura del canale»), scrivendola in un filo, in due
artefatti i2 e in un messaggio di commit. Era falsa: la corrispondenza
**inviata dal progetto stesso** tre giorni prima chiedeva testualmente quell'importo
e rinviava il resto a saldo. Il controllo costava una ricerca sulla propria
posta in uscita. È stato scoperto solo perché il custode ha chiesto altro.
Osservazione: la storia più elegante è quella che ha più bisogno di verifica, e
il processo non prevede nulla che lo dica.

**Caso 3 — una cifra usata come architrave, mai stata una misura.** Un filo
reggeva la tesi dell'urgenza su «~€400 al mese di erosione di valore». Il
numero era l'interpolazione fra **due sole dichiarazioni della stessa fonte**,
una delle quali riferita di terza mano e prodotta anni prima, e la fonte è
valutata nella KB stessa come di credibilità prossima a zero. Non era una
stima prudente: era una retta fra due asserzioni. Aveva già propagato in un
filo, in un'analisi i2 e nella classifica delle priorità di quell'analisi. Il
costo reale, calcolato quando è stato chiesto, era **un ordine di grandezza
inferiore**, e la sua caduta ha ribaltato una conclusione strategica.

Elemento comune ai tre: **il progetto aveva già in casa ciò che serviva a
smentire** (il file `o2/`, la propria posta inviata, la valutazione della fonte
nella KB). Non è un problema di accesso alle fonti, è che nulla obbliga a
guardarle quando il verdetto suona bene.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- il confronto **filo i3 ↔ file `o2/` che lo alimenta** appartiene a
  `verdicts-review`? Oggi la skill confronta il verdetto col «segnale reale»,
  ma il file task non è elencato fra i segnali, pur essendo spesso la
  registrazione più fresca e più cauta;
- la **corrispondenza in uscita del progetto** è una fonte primaria a tutti gli
  effetti? In `economia` la dottrina «i documenti primari prevalgono sulla
  memoria» era matura e non contemplava esplicitamente ciò che il progetto ha
  scritto **di suo**, che è la fonte più facile da consultare e la più
  dimenticata;
- una quantità che entra in un verdetto deve portare la propria **provenienza**
  (misurata / dichiarata da un terzo / derivata da dichiarazioni)? Il caso 3
  suggerisce che senza marcatura una cifra derivata da asserzioni acquisisce
  col tempo lo stesso peso di una misurata, e che la propagazione fra artefatti
  la consolida invece di eroderla;
- esiste un **asimmetria di attenzione** per cui una lettura elegante o
  sfavorevole-alla-controparte passa con meno controlli di una banale? Se sì è
  una proprietà da contrastare con la forma, non con la diligenza: la
  diligenza è esattamente ciò che manca nel momento in cui la storia convince;
- il fatto che il caso 2 sia stato prodotto da un **agente** e intercettato da
  un **umano** dice qualcosa sul punto di controllo? Il modello «umano
  in-the-loop» copre la decisione; qui è servito a intercettare una
  ricostruzione, cioè un passo che il metodo tratta come lavoro delegabile;
- quando una revisione **ritratta** qualcosa che aveva appena scritto e
  committato, la ritrattazione va registrata come tale (con la cannata agli
  atti) o basta correggere il testo? In `economia` esiste un artefatto locale
  che tiene le previsioni sbagliate «perché valgono doppio come antidoto alla
  presunzione», e la ritrattazione è finita lì: è un pattern locale o una
  capacità che il canone vuole.
