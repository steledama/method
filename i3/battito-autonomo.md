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

- **Push autonomo**: in `method` dal 2026-10-08 (`a6c6ccc`), recepito dai
  sette lo stesso giorno e prescrizione chiusa (dettaglio in
  `i3/audit-adottanti.md`); `bi` lo esclude per i commit che toccano il
  codice eseguito dal ciclo. `danea-auto` lo applica dal 2026-10-07 e la
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

- **A favore**: giri entro gli atti delegati, impatti motivati e proposte
  alte leggibili fino alla decisione; ricostruzioni fedeli alle fonti nel
  campione concordato; meno interventi e meno tempo di ricostruzione per il
  custode rispetto al confronto assistito. Le stime sbagliate affinano i
  criteri, ma non assolvono atti fuori delega o errori che alterano decisioni.
- **Contro**: un livello senza motivo ricostruibile, un atto fuori delega,
  un impatto alto applicato invece che proposto, una ricostruzione errata
  che altera una decisione, arresti o partenze mancate invisibili, oppure
  maggiore lavoro di supervisione senza beneficio dimostrato. Criteri che
  crescono più in fretta dei casi concreti restano un segnale negativo.
- **Da decidere prima**: se «in-the-loop» nel Goal di sviluppo diventa
  «on-the-loop». È una decisione del custode sul nord, sollevata in
  `o2/criteri-autonomia.md`, e non la prende questo filo.

## Il percorso

La terminologia è fissata il 2026-10-08 nel README: **agente** è l'IA,
**custode** il ruolo umano che decide. Lo stesso giorno i trailer
`Autonomia:`, `Impatto:` e `Impatto-motivo:` sono entrati nella skill di
commit e il consenso differito in `kb/consent.md`. Il Goal è separato dallo
stato in `method`; la [prescrizione](../o3/goal-senza-fotografia.md) porta il
contratto ai sette adottanti. I passi restanti sono task in `o1/plan.md`:
criteri di autonomia nel trittico costitutivo, home con fatto e da fare,
scelta dell'esecutore e pilota. La
ricerca sull'esecutore può partire indipendentemente; il pilota attende
criteri, home ed esecutore. La visibilità deve esistere prima che la
conferma si tolga e deve includere i tentativi senza commit.

Il filo [verdetto più sicuro del materiale](verdetto-piu-sicuro-del-materiale.md)
impedisce di equiparare un motivo leggibile a una ricostruzione fedele.
La delega sulla manutenzione dell'artefatto non estende automaticamente
quella sulle azioni di dominio. La revisione concordata il 2026-10-09
specifica il percorso, senza decidere un nuovo Goal, scegliere il pilota o
concedere nuovi permessi. L'esito deve misurare anche il costo per il custode:
un battito frequente e ben documentato può comunque aumentarlo.

## Condizione di chiusura

Riesame al battito `/adottanti` del **2026-11-01**: avanzamento del
percorso, decisione sul Goal di
sviluppo. Il verdetto vero arriva alla fine dell'osservazione del pilota,
con durata e criterio di riuscita fissati in `o2/pilota-battito.md`. A quel
punto il loop di base diventa canone e si prescrive, si corregge, oppure si
torna indietro.
