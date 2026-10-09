---
sintesi: "Il giudizio di settembre (2026-09-24) ha mantenuto la tripartizione eval/exec e corretto la clausola: ogni giro registra l'esito per stadio nel commit (trailer Esiti:). Il task resta pause fino al battito /adottanti del 2026-11-01, che conta gli esiti registrati dopo il recepimento. I sintomi vivono nella clausola del filo i3/skill-per-arco-tripartito.md; qui vivono condizione, data e materiale."
ciclo: dev
---

# Rivalutazione clausola di uscita skill per arco

Task `pause`. Il giudizio anticipato a settembre è stato preso il
**2026-09-24**, dopo il battito `/adottanti` arretrato: la tripartizione
resta, la clausola si corregge (verdetto nel filo
[`i3/skill-per-arco-tripartito.md`](../i3/skill-per-arco-tripartito.md)). Il
fallback del **2026-11-01** è riattivato, con l'evidenza mancante dichiarata:
a settembre gli esiti nulli per stadio non si potevano contare, perché non
lasciavano traccia.

## Cosa si valuta al risveglio

I **sintomi** — «troppo», «ha pagato», cosa si snellisce per primo — vivono
nella clausola di uscita del filo, dove vive il verdetto: qui non si
ricopiano, o le due liste divergerebbero alla prima rifinitura. Il task porta
la condizione, la data e il materiale.

## Materiale da raccogliere

- il **conteggio degli esiti** per stadio e per repository, dai trailer
  `Esiti:` dei commit dopo il recepimento della prescrizione
  `o3/esiti-per-stadio-nel-commit.md`:
  `git log --format='%(trailers:key=Esiti,valueonly)'`. Il dato vale solo per
  i repository che l'hanno recepita: gli altri si dichiarano, non si
  stimano;
- il **profilo muto**: `crm` (plan fermo dal 2026-08-21, nessun giro con
  `Esiti:`). Se resta senza giri, lo si dice: assenza di uso, non evidenza
  per l'una o l'altra direzione. `danea-auto`, muto fino a settembre, dal
  2026-09-26 è il repository con più giri registrati;
- nuovi casi di **«ha pagato»**: un errore intercettato da uno stadio che il
  giro monolitico non avrebbe visto. Ad oggi l'unico documentato è in
  `metodo`;
- il **costo dell'assorbimento** in `salute` ed `economia`, solo se nel
  frattempo compare un segnale: a settembre non era stato sentito.

## Criterio di chiusura

Verdetto esplicito nel filo, sui numeri del trailer: la tripartizione resta
com'è, si snellisce (quali scope si accorpano e perché), o si corregge il
canone. La decisione è del custode; il task si consuma col verdetto inciso.
Se la prescrizione non fosse recepita in tempo, il verdetto lo dichiara e
fissa la data successiva sul recepimento, non su un'attesa generica.

## Integrità e contesto della misura

Confrontare i trailer riconosciuti da Git con le righe `Esiti:` nel corpo:
`baserow` `205c627` è un caso documentato di perdita nel parsing. Contarlo
una volta, dichiarando il recupero; l'adozione del presidio in `danea-auto`
non prova un secondo incidente. `/commit` canonico richiede ora tutti i
trailer nell'ultimo paragrafo.

Quando la fonte lo permette, distinguere giri innescati da eventi o dal
custode e giri periodici autonomi; se non lo permette, dichiarare il limite.
Una maggiore frequenza programmata può aumentare gli esiti vuoti senza
smentire la tripartizione. L'assenza di un commit non prova l'assenza di un
tentativo: gli arresti prima del commit richiedono una fonte dell'esecutore.
