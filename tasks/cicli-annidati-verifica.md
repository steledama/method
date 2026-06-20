---
data: 2026-06-17
stato: aperto
revisione: 2026-06-19
---

# Verifica dei cicli annidati: 16 celle e mappa-sorgente

> **Stato (2026-06-19): gate eseguito, esito ribaltato, NON chiuso di proposito.**
> Matrice riempita e ribaltata in revisione collaborativa (16 celle: 10 S, 4 D, 2
> vuoto, 0 F — **due cicli genuini**, non una cucitura su mezzo ciclo); verdetto e
> mappa-sorgente prodotti in `kb/action-cycle-matrix.md`; esito catturato in
> `verdict.md`. **Rilettura a freddo in corso**: la riassegnazione del deck a
> i2/o2-runtime è sospetta e probabilmente sbagliata. `interpretations/metodo-in-sintesi.md`
> è oggi interpretazione di sintesi del metodo e della KB — quindi i2-dev — non
> osservatorio stabile degli adottanti. Il vero o2/i2-runtime va cercato in una
> superficie fissa di monitoraggio cross-repo, alimentata da audit periodici sugli
> adottanti. **Tenuto aperto perché è l'architrave dell'artefatto**: il ribaltamento
> verso la simmetria è avvenuto a caldo e va riletto a mente fresca prima di chiudere
> — proprio dove la matrice avverte che «chi cerca simmetria la trova sempre».
> Riprendere dalla «Rilettura a freddo» sotto, non dalle fondamenta.
>
> **Aggiornamento (2026-06-20).** Due punti della rilettura a freddo hanno ora un
> riscontro reale (cfr. `verdict.md`, filo «Tipologia-contenuto della KB e prima
> azione top-down»). **Punto 2 (l'osservatorio è il vero runtime)**: ha la sua
> **prima superficie** — `interpretations/baricentro-kb-adottanti.md`, lettura
> cross-repo del baricentro-contenuto dei quattro adottanti (i2-runtime). Conferma
> che il vero i2-runtime non è la sintesi interna del metodo ma l'analisi stabile
> sugli adottanti. **Call B (l'arco top-down)**: è **scoccato per la prima volta**,
> nella forma canonica — una **prescription** (`prescriptions/riequilibrio-baricentro-kb.md`,
> prima istanza o3-runtime attiva): `method` prescrive le linee guida, il
> `method-review` dell'adottante compie l'atto sul proprio stato reale. Conferma la
> distinzione della rilettura: l'o1-runtime resta osservazione periodica, non
> micromanagement delle code; l'azione top-down passa per l'o3-runtime (la
> prescrizione), non per la mano del metodo nel runtime altrui. Il buco runtime-o1 e
> la deriva di `interpretations/` (i2-runtime su Mondo-dev invece dei 4 domini)
> restano confermati. **Chiusura (stesso giorno)**: `salute` ha recepito e applicato
> la prescrizione (`method-review` aligned, marker `53968e8`) e il segnale è tornato —
> il ciclo runtime si è **chiuso per intero** (i2→i3→o3→adottante→i1), non solo acceso.
> Prima dimostrazione che l'arco top-down è percorribile fino in fondo; rafforza il
> verdetto «due cicli genuini» del gate.

Aperto in sessione 2026-06-17. La distinzione dev/runtime è teorizzata in
`action-cycle` (annidamento, la seconda delle quattro dimensioni) e ora ha un
nodo proprio, `nested-cycles`, ma non è ancora operativa nei due artefatti da cui
la presentazione dovrebbe derivare: `action-cycle-matrix` collassa l'annidamento
(8 righe, non 16) e la home pianificata da «System image visiva» si restringe al
solo ciclo di sviluppo, attenuando proprio Perform e Perceive — i due atti i cui
home runtime (`prescriptions/`, `perceptions/`) esistono già.

Questo task è un **gate di verifica precedente** ai due task di presentazione
(«Strato di presentazione» e «System image visiva»): mette alla prova l'ipotesi
dei due cicli annidati prima di costruirne la rappresentazione. Non genera la
presentazione e non costruisce il toggle: lo abilita o lo falsifica.

## I due output

Il task produce due artefatti distinti, di natura diversa.

- **(a) Verdetto-gate** — le 16 celle di `method` (6 atti + 2 poli, per ciascuno
  dei due cicli), ognuna con verdetto S/D/F/vuoto e una riga di giustificazione
  onesta, nello spirito anti-complicità di `action-cycle-matrix`. È un giudizio:
  l'annidamento a 16 celle regge per `method`, o è una forzatura elegante?
- **(b) Mappa-sorgente** — _solo se (a) regge_, per ciascuno dei 16 elementi il
  file o la collezione che ne è la casa nell'atrio. È un indice, non un giudizio,
  ed è ciò che i due task di presentazione consumano per generare la home a
  toggle e le viste senza inventare la geometria a mano.

## Criterio di falsificazione

Se nel verdetto (a) le celle forzate o vuote del ciclo runtime di `method`
restano molte, l'ipotesi del toggle a due cicli è sbagliata per questo
artefatto: **non si aggiusta la home, si ridiscute il toggle stesso**. Un
risultato atteso e onesto è che il ciclo runtime di `method` sia sparso —
o3/i1 solidi (`prescriptions/`/`perceptions/`) ma interno debole o vuoto. Saperlo
prima di disegnare una UI a due poli simmetrici è il valore del gate; scoprirlo
dopo averla costruita è il fallimento che il gate previene.

## La cucitura va marcata, non i due blocchi affiancati

Le 16 celle non sono due blocchi da 8 indipendenti. La verifica deve marcare la
sutura dell'annidamento (cfr. `nested-cycles`): il Mondo del ciclo di sviluppo —
l'artefatto — è la macchina del ciclo runtime. La matrice e ogni
rappresentazione derivata devono rendere visibile questa identità tra Mondo-dev
e macchina-runtime; l'o3-sviluppo modifica quel Mondo, ma non coincide con la
macchina. I due cicli non vanno affiancati come stati alla pari.

## Scope: method qui, adottanti col loro protocollo

Il task estende la **struttura** di `action-cycle-matrix` all'asse annidamento
(da 8 a 16 righe) e riempie in dogfooding **solo la colonna `method`**. Le
colonne degli adottanti restano al protocollo esistente del nodo: ogni repo
riempie la propria via il proprio `method-review` / prima slide, e il verdetto
risale qui come fotografia aggregata. `method` non orchestra questo lavoro nei
repo adottanti (cfr. `adopter-comparison`). Il toggle dev/runtime è inteso anche
per gli adottanti, ma la sua verifica per dominio non è oggetto di questo task.

## Implementazione

1. Estendere `action-cycle-matrix.md`: aggiungere l'asse annidamento (dev/runtime)
   alle 8 righe esistenti, aggiornandone l'introduzione e la scala; aggiornare la
   riga di catalogo in `kb.md` se il conteggio caselle cambia.
2. Riempire le 16 celle della colonna `method` con verdetto e giustificazione,
   leggendo le sorgenti reali (`plan.md`, `tasks/`, `verdict.md`,
   `interpretations/`, `perceptions/`, `prescriptions/`, `README`).
3. Marcare esplicitamente la cella/giunzione dell'annidamento (Mondo-dev →
   macchina-runtime; o3-sviluppo è l'atto che lo modifica), non lasciare i due
   cicli affiancati.
4. Pronunciare il verdetto-gate: se l'annidamento regge, produrre la
   mappa-sorgente (b) dei 16 elementi; altrimenti registrare la falsificazione e
   riaprire i due task di presentazione.
5. Aggiornare il verdetto corrente con l'esito del gate e l'eventuale ricaduta
   sul cluster presentazione.

## Relazione con gli altri task

- **Disaccoppiamento** resta valido e autonomo, eseguibile a prescindere. L'unico
  ritocco che questo gate può imporgli: la sezione README canonica oggi dichiara
  un solo polo World, ma per `method` i World sono due (sviluppo = `kb/`, runtime
  = adottanti). Dipendenza inversa lieve, non un blocco.
- **Strato di presentazione** e **System image visiva** dipendono da questo gate:
  se l'annidamento è falsificato, il loro scope a due cicli cambia o decade; se
  regge, consumano la mappa-sorgente (b).

## Rilettura a freddo: nuova impostazione da verificare

Il crinale da cui ripartire, in ordine di carico:

1. **Il deck non salva il runtime.** `interpretations/metodo-in-sintesi.md`, per come
   esiste oggi, è interpretazione di sintesi del metodo: rilegge la KB, i nodi e
   l'architettura dell'artefatto. È dunque **i2-dev** (e forse anche o2-dev quando
   viene usato come vista di decisione sul metodo), non i2/o2-runtime degli
   adottanti. La riassegnazione al runtime è la cella più sospetta del ribaltamento:
   sembra aver riempito il ciclo perché serviva alla simmetria.
2. **Il vero runtime di `method` è l'osservatorio sugli adottanti.** Il Mondo-runtime
   sono `nixos`, `bi`, `economia`, `salute`; quindi l'o2/i2-runtime non può essere la
   sintesi interna del metodo, ma una **analisi stabile cross-repo**: matrice per
   ciascun adottante, confronto dei drift, lacune, convergenze, segnali di attrito e
   di utilità reale del canone. Non un task occasionale: una superficie fissa da
   mantenere come monitoraggio del runtime.
3. **L'arco di esecuzione runtime va progettato come audit periodico, non come
   micromanagement.** o1-runtime dovrebbe essere il protocollo/macchina di
   osservazione: quali audit quantitativi e qualitativi eseguire, con quale cadenza,
   su quali repo e con quali criteri. o2-runtime è la vista comparativa che orienta
   decisioni sul metodo; o3-runtime resta il runbook/prescrizione di propagazione.
   Questo non significa pianificare i task interni degli adottanti: significa
   progettare il modo in cui `method` osserva il proprio Mondo e agisce sul canone.
4. **L'arco di valutazione runtime va alimentato dai segnali degli adottanti.** i1-runtime
   sono i segnali grezzi/audit/percezioni dai repo adottanti; i2-runtime è la loro
   interpretazione comparativa stabile; i3-runtime è la valutazione rispetto ai goal
   del metodo e dei domini — portabilità, attrito, fedeltà, autonomia, drift,
   capacità di generare azione. Oggi questi elementi esistono solo sparsi tra
   `perceptions/`, `verdict.md`, `method-review` e confronti ad hoc.
5. **Conseguenza sulla matrice.** Il gate continua a reggere come annidamento e come
   cucitura Mondo-dev→macchina-runtime, ma la pienezza del runtime è stata probabilmente
   sovrastimata. Le celle o2/i2-runtime vanno declassate o marcate come gap finché non
   esiste una superficie stabile di osservatorio; o1-runtime resta il gap di protocollo;
   i3-runtime resta sparso. Il verdetto sano non è «due cicli pieni», ma «due cicli
   genuini, con interno runtime da costruire».
6. **Goal-dev / Goal-runtime provvisori.** Lo split degli obiettivi costitutivi verso
   il runtime (e Goal-dev a D) dipende dalle «dimensioni del Goal» (task 8): finché
   quelle non si posano, i due verdetti Goal restano provvisori.
7. **Generalizzazione agli adottanti.** La matrice dev/runtime va probabilmente fatta
   per ciascun repo adottante in modo fisso, non solo per `method`: è il nucleo
   dell'osservatorio runtime. Resta da decidere se vive in `action-cycle-matrix`, in
   una nuova interpretazione stabile (`interpretations/osservatorio-adottanti.md`) o
   in entrambi, con ruoli distinti.

## Fuori perimetro

- riempire le colonne degli adottanti nella matrice;
- costruire la home, le viste o il toggle dev/runtime;
- la verifica dell'annidamento per i domini adottanti;
- modifiche al nodo `nested-cycles` oltre eventuali correzioni emerse dal verdetto.
