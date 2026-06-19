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
> `verdict.md`; conseguenze di canone (riassegnazione del deck a i2/o2-runtime,
> revisione di «non orchestra») accodate a `tasks/fonti-engelbart.md` per toccare gli
> hub una volta sola. **Tenuto aperto perché è l'architrave dell'artefatto**: il
> ribaltamento verso la simmetria è avvenuto a caldo e va riletto a mente fresca prima
> di chiudere — proprio dove la matrice avverte che «chi cerca simmetria la trova
> sempre». Riprendere dalle «Domande aperte» in fondo, non dalle fondamenta.

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
rappresentazione derivata devono rendere visibile dove l'o3 di sviluppo deposita
la macchina che il runtime muove, non affiancare i due cicli come stati alla
pari.

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
3. Marcare esplicitamente la cella/giunzione dell'annidamento (o3-sviluppo →
   macchina-runtime), non lasciare i due cicli affiancati.
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

## Domande aperte (per la sessione fresca)

Il crinale da cui ripartire, in ordine di carico:

1. **La complicità del ribaltamento.** Il flip da «mezzo ciclo» a «due cicli pieni»
   è avvenuto in dialogo, in parte riclassificando il deck e ammettendo il top-down.
   A mente fredda: il runtime è _genuinamente_ pieno, o ce lo siamo raccontato? Il
   deck tenuto a D è la guardia che ha funzionato; ma l'intero flip va riletto contro
   l'avvertimento della matrice.
2. **Cosa è l'i2-dev?** Se il deck è i2-runtime, il ciclo di sviluppo resta senza
   interpretazione viva (i2-dev vuoto). È una mancanza strutturale o un vuoto
   legittimo? Lo sviluppo _dovrebbe_ auto-interpretarsi, e con quale superficie?
3. **La linea di B.** Dove passa esattamente il confine tra «`metodo` pianifica il
   proprio output di canone e le convergenze» (top-down legittimo) e «micromanagement
   della coda interna degli adottanti» (resta fuori)? È il crinale che decide se la
   revisione di «non orchestra» reintroduce la forzatura che il bottom-up aveva tolto.
4. **Goal-dev / Goal-runtime provvisori.** Lo split degli obiettivi costitutivi verso
   il runtime (e Goal-dev a D) dipende dalle «dimensioni del Goal» (task 8): finché
   quelle non si posano, i due verdetti Goal restano provvisori.
5. **Generalizzazione agli adottanti.** Abbiamo riempito solo `metodo`. Se il suo
   runtime è un ciclo pieno con arco top-down, l'asse annidamento vale per tutti e
   cinque — e la matrice a 8 righe lo collassa per tutti. È una peculiarità del
   meta-artefatto o vale per ogni adottante?

## Fuori perimetro

- riempire le colonne degli adottanti nella matrice;
- costruire la home, le viste o il toggle dev/runtime;
- la verifica dell'annidamento per i domini adottanti;
- modifiche al nodo `nested-cycles` oltre eventuali correzioni emerse dal verdetto.
