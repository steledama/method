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
misurabile: manca il campione riletto contro le fonti.

- **Copertura**: il criterio `ciclo-autonomo` è ratificato in `method` e nei
  sei adottanti. Il timer è acceso in `salute` dal 2026-10-12, in `economia`
  dal 16, in `nixos`, `method`, `bi` e `baserow` dal 17 (`nixos` `7fad7d2`,
  `d1c4346`, `e3f463a`) e in `danea-auto` su Windows, fuori `nixos`, col
  primo giro riuscito il 22 (`de11b1a`). `crm` è uscito il 2026-10-19 ed è
  dismesso come adottante dal 22 (`a0deb15`, `458eb4b`). L'andamento sta in
  `o2/pilota-ciclo-autonomo.md`.
- **Affidabilità**: dal 2026-10-22 ogni giro schedulato partito per intero,
  in `method` e nei sei adottanti, è riuscito con commit e push
  (`tentativi.jsonl` su `deck`, misurati; per `svezia` e Windows i commit coi
  trailer su `origin`). Gli scarti precedenti hanno avuto una causa trovata e
  corretta: il 14 `salute` fallito sul Drive irraggiungibile, ora registrato
  da `ciclo-namespace`; il 20 `economia` fermo prima del commit, col tree
  sporco di una sessione Codex che `ciclo-sessioni` non vedeva (`nixos`
  `101e32b`). I sei arresti per sessione aperta dal 19 al 24 sono il sistema
  che funziona; quelli di `salute` ed `economia` stanno nella cartella
  dell'unità, non in `i1/giri`
  (`i1/arresto-economia-fuori-giri-2026-10-21.md`, decisione in
  `o2/lanciatore-ciclo-nel-metodo.md`).
- **Costo**: su `deck` un giro ordinario costa fra 0,6 e 2,4 USD e arriva a
  77 turni e 13 minuti, lontano dal tetto di 45 minuti e 5 USD. I
  `tentativi.jsonl` di `svezia` e Windows non sono leggibili da `deck`.
- **Dinieghi**: da zero a tre per giro, su grafie note (composti, `for`,
  graffe, `python3 -c`, scritture fuori perimetro) che `/cycle` segnala dal
  2026-10-26 (`e88d81f`). Le lacune trovate sono chiuse: letture degli
  adottanti con `o3/adottanti.py` (`911b120`), fetch di `svezia` nel passo
  `ciclo-fetch` dell'unità (`i1/giro-method-2026-10-20.md`), controlli `gh`
  in sola lettura per `nixos` (`7eb86ac`). La perdita vera resta il gesto
  abbandonato dopo un diniego (`kb/agent-as-user.md`).
- **Quando si aggiorna**: un giorno in cui ogni giro riesce senza fatti nuovi
  conferma questo stato e non lo riscrive. Il filo si tocca per un
  fallimento, un arresto invisibile, un diniego di classe nuova, un costo o
  una durata fuori fascia, un cambio di copertura. Le serie per giorno
  restano in `tentativi.jsonl` e nei trailer.

La prima delega resta
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
  condizione parallela, non successiva (`kb/view.md`).
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
- **Il testo del giro contro il recinto**, 2026-10-16/17: al primo giro
  autonomo di `bi` e di `baserow` bootstrap, prompt o skill chiedevano letture
  e un pull che `ciclo.json` o il register negavano
  (`i2/casi-delega-adottanti.md`). Diniego preso come confine e dichiarato in
  ogni caso, nessun atto fuori delega; correzioni locali e a mano. Il
  2026-10-19 `baserow` estende il giro al pull dello standby su un secondo
  host, con guardie e verifica dell'hash (`437b11b`): da rileggere ai primi
  esercizi.
- **File e tracce del giro nell'artefatto**, 2026-10-19: proposta di `bi`,
  decisa dal custode. Prompt e permessi del giro vanno in `o3/ciclo/`,
  versionati, e non si modificano nel giro. Le trascrizioni e gli esiti vanno
  in `i1/giri/`, ignorati da git, dove `eval perceive` li legge
  (`kb/perceive.md`, `o3/ciclo-autonomo.md`). Le frizioni del giro
  rientrano così nel ciclo senza una sessione col custode. Migrazione da
  coordinare con `nixos` (path e campo `giri` in `o3/cicli.nix`).
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
il pilota. Il 2026-10-26 sono chiusi il task dell'esecutore, col modulo
`nixos` in esercizio, e quello della home, verificata dal custode senza le
sezioni «fatto» e «da fare» (scadenze e attese restano nel plan); portare il
lanciatore nel metodo è un task proprio, senza effetto sul pilota. Il task dei criteri è chiuso il
2026-10-25: `ciclo-autonomo` ratificato in `method` e nei sei adottanti col
timer, proposte da decidere e register della delega raggiungibili dalla home
(campo `decidere:` dei task `o2/`), collaudo sui casi portato nel campione
del pilota. Esecutore, criterio e semaforo dei tentativi nella home sono in
uso nei giri; del pilota restano i residui scritti nel suo file `o2/`. Per il ciclo avviato dal custode il controllo è già nel resoconto finale.

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
