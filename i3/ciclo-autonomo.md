---
ciclo: dev
obiettivo: S, 2
---

# Il ciclo autonomo: con quali garanzie ogni repo ci arriva?

Il custode, 2026-10-11: il ciclo autonomo di runtime è parte costitutiva del
metodo (`goal.md`, Goal di sviluppo). Ogni repo ci va gradualmente e con i
propri limiti, dentro un ambito di autonomia e con strumenti rigorosi di
tracciabilità, controllo e verifica. La domanda non è _se_ l'artefatto regga
un giro senza custode, ma _con quali garanzie_ ci arriva ciascun repo e
quando un gradino va ritirato. La base comune è un giro `eval` → `exec` che
chiude con commit e push; i loop di dominio si articolano su di essa.

## La scommessa

L'artefatto è abbastanza esplicito da sostenere l'agente da solo **senza
perdere fedeltà**: al custode serve meno essere nel giro, purché lo
controlli a colpo d'occhio e tenga in mano i criteri. Si misura contro:

- **S**: il Goal di sviluppo delega il governo operativo dei cicli avviati
  dal custode e conserva la supervisione degli esiti; il ciclo schedulato
  chiede in più estensione e visibilità senza sessione;
- **2**: il loop si propaga come canone agli adottanti e lì incontra le
  differenze di dominio.

## Lo stato del verdetto

In esercizio a gradini, verdetto non ancora misurabile: manca il campione
riletto contro le fonti.

- **Copertura**: criterio `ciclo-autonomo` ratificato in `method` e nei sei
  adottanti, timer acceso in tutti dal 2026-10-22 (`danea-auto` su Windows,
  fuori `nixos`, `de11b1a`). `crm` è dismesso dal 22/10 (`a0deb15`).
  Settimo dal 2026-11-05 `nixos-lavoro`, separato da `nixos` il 04/11:
  gradino 0 e due giri a mano riusciti (`92afebd`, `3438713`), poi gradino 1
  col timer delle 04:30 sullo standby `norvegia` (`1f7c780`), con un commit
  di registro della production oltre a quello del giro. Andamento in
  `o2/pilota-ciclo-autonomo.md`. Dall'08/11 cambia il meccanismo di
  `danea-auto`: parte dal lanciatore canonico di `method` (marker del repo,
  giro a mano `0624d2f`, timer dal 09/11). Ipotesi del giro dell'08/11: anche
  la partenza di `method` delle 19:37 (`87eac6f5`, avvio a mano) viene dal
  lanciatore, perché la riga ha la forma di `o3/lanciatore.py` e non quella
  compatta dell'unità. La smentirebbe una `chiusura` di quell'id in forma
  compatta; riscontro in `i1/giri/tentativi.jsonl` al giro del 09/11.
- **Affidabilità**: dal 2026-10-22 ogni giro partito per intero è riuscito
  con commit e push, tranne uno: `method` il 2026-11-01, errore di rete
  dell'API (`EAI_AGAIN`) dopo 15 turni, visibile in `tentativi.jsonl`, tree
  pulito. Gli arresti prima del giro sono il recinto che funziona: sei per
  sessione aperta fra il 19 e il 24/10, uno `pull-in-sola-lettura` il 29/10
  (`369d5ea`, rilancio a mano). Il limite è che un arresto o un fallimento
  non si rilancia da solo: `method` è rimasto senza giro il 31/10 e il
  01/11. Regola provvisoria in `o2/pilota-ciclo-autonomo.md`, disegno in
  `o2/lanciatore-ciclo-nel-metodo.md`. Il 2026-11-06 `danea-auto` non ha
  il commit del giro su `origin`, pur col timer delle 08:10 e la ripresa
  delle 10:10 (`14b1231`): il fetch delle 15:00 è riuscito e `origin/main`
  resta a `0840a4b` del 05/11. Il 07/11 su `origin` arriva solo il giro
  della ripresa delle 10:10 (`6ebecfb`), nessuno delle 08:10. L'08/11 il
  timer delle 08:10 torna a committare (`376d042`, 08:12): i giorni senza
  commit del timer restano due. Da `deck` non si vede se quei giri siano
  mancati, fermi o senza push, perché i tentativi di Windows non si
  leggono da qui: la causa va accertata su `danea2`, voce in
  `o2/pilota-ciclo-autonomo.md`. Gli scarti prima del 22/10 hanno
  avuto causa trovata e corretta (`nixos` `101e32b`,
  `i1/arresto-economia-fuori-giri-2026-10-21.md`).
- **Costo**: su `deck` un giro ordinario costa fra 0,6 e 2,4 USD e arriva a
  100 turni (`nixos` dell'08/11, 2,32 USD in 9 minuti, primo giro di
  `nixos` con gli stadi invocati) e 13 minuti, sotto il tetto di 45 minuti
  e 5 USD. I
  `tentativi.jsonl` di `svezia`, `norvegia` e Windows non sono leggibili da
  `deck`.
- **Fedeltà degli esiti**: «riuscito» non vuol dire «eseguito». Il
  2026-11-07, dopo il caso `nixos`, la verifica ha trovato che nessun giro
  di nessun repo invoca `eval` o `exec` come skill. `Esiti:` nomina sempre i
  sei stadi, e `goal.md` lo legge quasi nessuno, quindi il verdetto dei fili
  non si è mai rinnovato nei giri
  (`i1/giri-stadi-dichiarati-senza-traccia-2026-11-07.md`). È un segnale
  contro la misura, non un atto fuori delega: la KB non mostra danni. Il
  canone ora chiede l'invocazione, un minimo per stadio e la verifica ex post
  `commit_gate.py stadi`. La misura torna leggibile quando «Stadi dei giri»
  di `adottanti.py audit` è senza rossi. Primo riscontro il 2026-11-07:
  il giro di `salute` delle 9:00 (`a81e024`) ha invocato i bracci col tool
  Skill, con zero dinieghi, e ha dato «stadi ok». Ha letto `goal.md` e tutti
  i fili, e `compare=vuoto` è un vuoto vero. È costato 69 turni e 1,76 USD,
  contro 25-56 turni e 0,52-1,28 USD della settimana prima. È un giro solo:
  salute lo osserva fino al 14/11. Il gate verde non dice se il giudizio
  regge: in `nixos`, l'8 novembre, minimi soddisfatti con finestre troppo
  corte, oggetti al posto dei corpi e atti prima del verdetto
  (`i1/giri-lettura-fatta-giudizio-sottile-2026-11-08.md`). Dal 2026-11-08
  il resoconto traccia ogni filo e obiettivo e `stadi` verifica il passo 3c;
  il giudizio si misura sul campione.
- **Dinieghi**: da zero a tre per giro, su grafie note che `/cycle` segnala
  dal 2026-10-26 (`e88d81f`); le lacune trovate sono chiuse (`911b120`,
  `7eb86ac`, `i1/giro-method-2026-10-20.md`). La perdita vera resta il gesto
  abbandonato dopo un diniego (`kb/agent-as-user.md`).
- **Quando si aggiorna**: un giorno in cui ogni giro riesce senza fatti
  nuovi è una lettura che non sposta e non riscrive il filo
  (`kb/interpret.md`). Il filo si tocca per un fallimento, un arresto
  invisibile, un diniego di classe nuova, un costo o una durata fuori
  fascia, un cambio di copertura. Le serie per giorno restano in
  `tentativi.jsonl`, nei trailer e in `i1/giri/`.

## I casi che hanno mosso il giudizio

La prima delega è ratificata dal 2026-10-09 e operativa nei cicli avviati
dal custode (`autonomy.md`). La concordanza frequente riferita dal custode
motiva la riduzione dell'attrito, non prova la fedeltà delle ricostruzioni
([verdetto più sicuro del materiale](verdetto-piu-sicuro-del-materiale.md)).

- **Primo giro reale**, 2026-10-11, `salute` a gradino 0: riuscito, con la
  visibilità nella home posta dal custode come condizione parallela
  (`kb/view.md`).
- **Push rifiutato**, 2026-10-08: nessuna forzatura e arresto; il rebase si
  è fermato sul permesso dell'harness. Un giro senza custode incontrerà lo
  stesso caso e non potrà chiedere.
- **Checkout che è superficie servita** (`bi`, `crm`, 18 casi dal 09 al
  10/10, `i2/casi-delega-adottanti.md`): nessuna autonomia sbagliata con
  danno; il custode ha esteso la delega anche lì con eccezioni nominate
  ([consent](../kb/consent.md)).
- **Testo del giro contro il recinto**, 16-17/10, `bi` e `baserow`: prompt e
  skill chiedevano atti che i permessi negavano; diniego preso come confine.
  Ne nascono prompt e permessi versionati in `o3/ciclo/` e tracce in
  `i1/giri/` lette da `eval perceive` (prescrizione chiusa il 28/10).
- **Standby su secondo host**, `baserow` `437b11b` (19/10): da rileggere ai
  primi esercizi.

## Cosa sposterebbe il verdetto

- **A favore**: giri entro gli atti delegati, impatti motivati e proposte
  alte leggibili fino alla decisione; ricostruzioni fedeli alle fonti nel
  campione concordato; meno interventi e meno tempo di ricostruzione per il
  custode rispetto al confronto assistito. Le stime sbagliate affinano i
  criteri, ma non assolvono atti fuori delega o errori che alterano decisioni.
- **Contro**: un livello senza motivo ricostruibile, un atto fuori delega,
  un impatto alto applicato invece che proposto, una ricostruzione errata
  che altera una decisione, arresti o partenze mancate invisibili, oppure
  più lavoro di supervisione senza beneficio dimostrato. Criteri che
  crescono più in fretta dei casi concreti restano un segnale negativo.
- **Ancora da fissare**: campione da rileggere, misura del costo di
  supervisione e confronto assistito (`o2/pilota-ciclo-autonomo.md`, «Da
  fissare alla partenza»).

## Condizione di chiusura

Riesame del 2026-11-02, con l'audit `/adottanti`: copertura completa, giri
schedulati da 17 a 25 per repository dall'08/10 (`i3/audit-adottanti.md`),
nessun caso nuovo sulla prima delega. Il passo che blocca non è la
copertura ma il campione e la misura del costo di supervisione, ancora da
fissare. La delega sulla manutenzione dell'artefatto non estende da sola
quella sulle azioni di dominio, e l'esito deve misurare anche il costo per
il custode.

Prossimo riesame all'audit del **2026-12-01**. Il verdetto arriva alla fine
dell'osservazione del pilota: il loop di base diventa canone e si
prescrive, oppure si corregge. Il ritorno alla modalità assistita resta
possibile per il singolo repo o gradino, non per la direzione.
