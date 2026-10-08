---
ciclo: dev
obiettivo: S, 2
---

# Il battito autonomo: l'artefatto regge un giro senza custode?

Il custode, 2026-10-08: gli adottanti sono abbastanza maturi da iniziare a
girare da soli. Le ultime modifiche al canone rendono esplicite, scritte e
rintracciabili le ipotesi e le interpretazioni dietro decisioni e azioni
(provenienza, presidio delle ipotesi, trailer `Esiti:`). La conseguenza
attesa è un **loop agentico di base**, uguale per tutti: un giro `eval` →
`exec` che chiude con un commit e il push, schedulato da ogni repo e senza
custode. I loop di dominio si articolano poi su questa base.

## La scommessa

L'artefatto è ormai abbastanza esplicito da sostenere l'agente da solo
**senza perdere fedeltà**. Al custode serve meno essere nel giro, purché lo
controlli a colpo d'occhio e tenga in mano i criteri.

La tensione si misura contro due obiettivi:

- **S**: il Goal di sviluppo dice oggi «umano **in-the-loop**» e «basso
  attrito di lettura». Il battito sposta il custode verso la supervisione
  del giro e chiede che la lettura diventi ancora più immediata. Il primo
  movimento contraddice la lettera del Goal; il secondo la estende.
- **2**: il loop si propaga come canone agli adottanti, e lì incontra le
  differenze di dominio.

## Lo stato del verdetto

Non ancora misurabile: nessun giro autonomo è avvenuto. I fatti finora:

- **Push autonomo**: in `method` dal 2026-10-08 (`a6c6ccc`), prescritto ai
  sette (`o3/push-autonomo.md`). `danea-auto` lo applica dal 2026-10-07 e la
  sua sessione dell'08/10 ha chiuso due giri `eval`/`exec` con commit e push
  senza intervento sul push.
- **Primo attrito reale**, 2026-10-08: il primo push autonomo di `method` è
  stato rifiutato perché un altro checkout aveva pubblicato nel frattempo.
  La regola ha tenuto: nessuna forzatura, arresto, riferimento al custode. Il
  rebase ha chiesto la cancellazione di due file, e il permesso dell'harness
  l'ha fermata. Un battito senza custode incontrerà lo stesso caso e non
  potrà chiedere.
- **Residuo di dominio**: in `bi` gli script automatici fanno `pull` prima di
  girare, quindi un push autonomo è un rilascio in produzione.

## Cosa sposterebbe il verdetto

- **A favore**: giri del pilota in cui il custode, leggendo la home, non
  avrebbe cambiato nessun verde né giallo, e ogni rosso arriva come proposta
  leggibile.
- **Contro**: un giallo che il custode avrebbe respinto, un rosso mancato
  (incisione sul nord applicata invece che proposta), giri che si fermano su
  conflitti che nessuno vede, criteri di autonomia che crescono più in
  fretta dei casi concreti che li giustificano.
- **Da decidere prima**: se «in-the-loop» nel Goal di sviluppo diventa
  «on-the-loop». È una decisione del custode sul nord, sollevata in
  `o2/criteri-autonomia.md`, e non la prende questo filo.

## Il percorso

I passi sono task in `o1/plan.md`: terminologia agente/custode, trailer di
autonomia e incisione, home con fatto e da fare, criteri di autonomia nel
trittico costitutivo, dove gira il battito, pilota. L'ordine mette la
visibilità prima dell'autonomia: il controllo deve esistere prima che la
conferma si tolga.

## Condizione di chiusura

Riesame al battito `/adottanti` del **2026-11-01**: recepimento di
`push-autonomo` nei sette, avanzamento del percorso, decisione sul Goal di
sviluppo. Il verdetto vero arriva alla fine dell'osservazione del pilota,
con durata e criterio di riuscita fissati in `o2/pilota-battito.md`. A quel
punto il loop di base diventa canone e si prescrive, si corregge, oppure si
torna indietro.
