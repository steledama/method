---
ciclo: dev
obiettivo: S, 2
---

# Il ciclo autonomo: con quali garanzie ogni repo ci arriva?

Il custode, 2026-10-08: gli adottanti sono abbastanza maturi da iniziare a
girare da soli. Le ultime modifiche al canone rendono esplicite, scritte e
rintracciabili le ipotesi e le interpretazioni dietro decisioni e azioni
(provenienza, presidio delle ipotesi, trailer `Esiti:`). La conseguenza
attesa è un **loop agentico di base**, uguale per tutti: un giro `eval` →
`exec` che chiude con un commit e il push, schedulato da ogni repo e senza
custode. I loop di dominio si articolano poi su questa base.

Il custode, 2026-10-11: il ciclo autonomo di runtime è parte costitutiva del
metodo (`goal.md`, Goal di sviluppo). Ogni repo ci va, gradualmente e con i
propri limiti; l'artefatto deve avere un ambito di autonomia e strumenti
rigorosi di tracciabilità, controllo e verifica. La domanda non è più _se_
l'artefatto regga un giro senza custode, ma _con quali garanzie_ ci arriva
ciascun repo, e quando un gradino va ritirato.

## La scommessa

L'artefatto è ormai abbastanza esplicito da sostenere l'agente da solo
**senza perdere fedeltà**. Al custode serve meno essere nel giro, purché lo
controlli a colpo d'occhio e tenga in mano i criteri.

La tensione si misura contro due obiettivi:

- **S**: il Goal di sviluppo ora delega il governo operativo dei cicli
  avviati dal custode e conserva la supervisione degli esiti. Il ciclo autonomo
  schedulato richiede un'ulteriore estensione e visibilità senza sessione.
- **2**: il loop si propaga come canone agli adottanti, e lì incontra le
  differenze di dominio.

## Lo stato del verdetto

Il ciclo autonomo è in esercizio a gradini, ma il verdetto non è ancora
misurabile: manca il campione riletto contro le fonti. Il criterio
`ciclo-autonomo` è ratificato in `salute`, `crm`, `economia`, `nixos` e
`method`; il timer è acceso in `salute` dal 2026-10-12 e deciso in `crm`
dal 2026-10-15; `economia`, `nixos` e `method` sono al gradino 0 dal
2026-10-16 (`o2/pilota-ciclo-autonomo.md`, «Andamento»). Dei giri
schedulati di `salute` fino al 2026-10-15 (`tentativi.jsonl` e journal su
`deck`, letti in sessione col custode): riusciti il 13 e il 15; il 12 saltato
con `deck` spento all'orario; il 14 fallito alla preparazione del namespace
per il Drive irraggiungibile, senza riga nello stato, ora registrato da
`ciclo-namespace` (`nixos` `kb/cicli.md`). La prima delega resta
ratificata e operativa nei cicli avviati dal custode (`autonomy.md`): niente
conferme ordinarie fra valutazione, esecuzione e chiusura. La concordanza
frequente riferita dal custode motiva la riduzione dell'attrito, non prova
la fedeltà delle ricostruzioni. I fatti ulteriori:

- **Primo giro reale**, 2026-10-11: `salute` su `deck`, gradino 0 avviato
  a mano dall'unità del modulo `cicli` di `nixos`. Riuscito con commit e
  push, materia in tutti gli stadi, una proposta lasciata al custode, un
  errore di strumento corretto con test, errori minori dichiarati
  dall'agente. Dettaglio e punti aperti in `o2/pilota-ciclo-autonomo.md`. Il
  custode ha giudicato ottimo il test; la fedeltà resta da misurare sul
  campione. Il custode ha posto la visibilità del ciclo autonomo nella home come
  condizione parallela, non successiva (`o2/home-fatto-da-fare.md`).
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
  l'ha fermata. Un ciclo autonomo senza custode incontrerà lo stesso caso e non
  potrà chiedere.
- **Primi riscontri sulla prima delega**, 2026-10-09/10: 18 casi inoltrati
  da `bi`, `crm` e `baserow` (`i2/casi-delega-adottanti.md`). Nessuna
  autonomia rivelatasi sbagliata con danno; due errori dichiarati
  dall'agente, uno dei quali giudicato corretto dal custode; quattro
  conferme rivelate inutili, con il criterio allentato in `crm`. Il
  residuo di dominio è il checkout che è anche superficie servita: in `bi`
  il commit è già rilascio, in `crm` una pubblicazione. Un ciclo autonomo senza
  custode non potrebbe chiedere su quel confine: va riconosciuto prima
  dell'atto. Il custode ha deciso il 2026-10-10 che la delega vale anche lì,
  con eccezioni nominate in `autonomy.md` ([consent](../kb/consent.md));
  recepito dai sette lo stesso giorno.

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
- **Ancora da fissare**: campione da rileggere, misura del costo di
  supervisione e confronto assistito, in `o2/pilota-ciclo-autonomo.md` («Da
  fissare alla partenza»), mentre i gradini avanzano già.

## Il percorso

La terminologia è fissata il 2026-10-08 nel README: **agente** è l'IA,
**custode** il ruolo umano che decide. Lo stesso giorno i trailer
`Autonomia:`, `Impatto:` e `Impatto-motivo:` sono entrati nella skill di
commit e il consenso differito in `kb/consent.md`. Il Goal è separato dallo
stato in `method` e nei sette adottanti (`goal-senza-fotografia`, chiusa
il 2026-10-09). I passi restanti sono task in `o1/plan.md`:
criteri del ciclo autonomo schedulato, home con fatto e da fare,
esecutore e pilota. Esecutore, criterio e semaforo dei tentativi nella home
sono in uso nei giri; dei primi tre task restano i residui scritti nei loro
file `o2/`. Per il ciclo avviato dal custode il controllo è già nel resoconto finale.

Il filo [verdetto più sicuro del materiale](verdetto-piu-sicuro-del-materiale.md)
impedisce di equiparare un motivo leggibile a una ricostruzione fedele.
La delega sulla manutenzione dell'artefatto non estende automaticamente
quella sulle azioni di dominio. Il custode ha ratificato il nuovo Goal e la prima delega del ciclo il
2026-10-09; il pilota e la sua estensione restano da decidere. L'esito deve misurare anche il costo per il custode:
un ciclo autonomo frequente e ben documentato può comunque aumentarlo.

## Condizione di chiusura

Riesame all'audit `/adottanti` del **2026-11-01**: avanzamento del
percorso e riscontri sulla prima delega. Il verdetto vero arriva alla fine dell'osservazione del pilota,
con durata e criterio di riuscita fissati in `o2/pilota-ciclo-autonomo.md`. A quel
punto il loop di base diventa canone e si prescrive, oppure si corregge. Il
ritorno alla modalità assistita resta possibile per il singolo repo o
gradino, non per la direzione.
