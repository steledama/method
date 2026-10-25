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
`ciclo-autonomo` è ratificato in `salute`, `economia`, `nixos`,
`method`, `bi` e `baserow`; `crm` ne è uscito il 2026-10-19 per decisione del
custode (`nixos` `1be1e2d`) ed è dismesso come adottante dal 2026-10-22,
rimosso da tutti gli host (`a0deb15`, `458eb4b`); il timer è acceso in `salute` dal 2026-10-12 e in `economia` dal
2026-10-16, in `nixos` e `method` dal 2026-10-17 (`nixos` `7fad7d2`),
in `bi` su `svezia` dal 2026-10-17 (`nixos` `d1c4346`), in `baserow` su
`svezia` dal 2026-10-17 (`nixos` `e3f463a`), in `danea-auto` su Windows,
fuori `nixos`, deciso dal custode il 2026-10-21, col primo giro schedulato
riuscito il 22 (`danea-auto` `de11b1a`, `85b27f5`, `1a6b33f`)
(`o2/pilota-ciclo-autonomo.md`, «Andamento»). Dei giri
schedulati di `salute` fino al 2026-10-15 (`tentativi.jsonl` e journal su
`deck`, letti in sessione col custode): riusciti il 13 e il 15; il 12 saltato
con `deck` spento all'orario; il 14 fallito alla preparazione del namespace
per il Drive irraggiungibile, senza riga nello stato, ora registrato da
`ciclo-namespace` (`nixos` `kb/cicli.md`). Dal 2026-10-16 al 2026-10-19
(`tentativi.jsonl`, misurati, letti dai giri di `method`) ogni giro
schedulato di `deck` partito per intero è riuscito con commit e push:
`salute` quattro su quattro (0,62–1,52 USD), `economia` quattro su quattro
(0,66–0,87 USD), `nixos` tre su tre (1,19–1,95 USD; il 19 alle 04:30, non
più alle 14:00). Due arresti visibili per sessione aperta, cioè il sistema
che funziona: `method` il 2026-10-19 alle 15:00 e `nixos` il 2026-10-20
alle 04:30, entrambi ripartiti alle 07:17 del 20, avviati a mano dal
custode (confermato in sessione). Il 2026-10-20 la serie si incrina:
`salute` riuscito alle 08:30 con commit e push (1,35 USD), `economia` alle
13:00 chiuso dall'unità come `riuscito` ma senza commit, con tree sporco
dopo il giro e due dinieghi, uno su `git rm` di due file `o3/`. La home lo
mostra giallo, quindi non è un arresto invisibile. Causa letta in sessione
col custode dal trascritto: alle 12:59 il custode lavorava in `economia`
con una sessione Codex (`/method`), che `ciclo-sessioni` non vede perché
cerca solo processi Claude con la cwd nel checkout, e le sessioni Codex
sono thread di un daemon `app-server` con la cwd altrove. Il giro ha visto
quattro file non suoi e si è fermato prima del commit, come prescrive la
skill; i dinieghi erano un `for` composto e `git rm -q`, fuori pattern,
entrambi aggirati. Il tree è tornato pulito con `deba9f5` e `c2e70a4`,
commit delle due sessioni Codex che contengono anche il lavoro del giro. La
correzione di `ciclo-sessioni` sui rollout Codex è in `nixos` `101e32b`, attiva su `deck` dallo switch del 2026-10-20: un rollout con la cwd nel checkout scritto nell'ultima ora ferma il giro col codice 15. Il 2026-10-21 (`tentativi.jsonl`, misurati) `nixos` e `salute` sono riusciti con commit e push (1,44 e 1,20 USD, due e cinque dinieghi). `economia` alle 13:00 si è fermato per sessione aperta, col custode al lavoro (`ee5daa3`, 13:11). La riga dell'arresto però sta nella cartella dell'unità, non in `i1/giri` dichiarato dal repo. La vista la rende come partenza mancata: rossa lo stesso, ma col motivo sbagliato (`i1/arresto-economia-fuori-giri-2026-10-21.md`, proposta in `o2/home-fatto-da-fare.md`). I sei dinieghi del giro di `method` del 20 alle 15:00 erano letture dirette degli altri checkout, quindi una lacuna. La chiude `o3/adottanti.py` (`911b120`): il giro del 21 legge gli adottanti con quello, e il suo unico diniego è un `python3 -c`, vincolo voluto, sostituito con Read. Il 2026-10-22 tutti e sei gli adottanti col timer hanno un giro schedulato riuscito con commit e push: su `deck` `nixos`, `salute` ed `economia` (`tentativi.jsonl`, misurati: 1,46, 1,08 e 1,31 USD, con due, zero e un diniego), su `svezia` `baserow` e `bi` e su Windows `danea-auto` (commit coi trailer `ciclo-autonomo` su `origin`; i loro `tentativi.jsonl` non sono leggibili da `deck`). Dal 23 al 25 (`tentativi.jsonl`, misurati; commit su `origin` dopo i fetch riusciti delle 15:00) ogni giro schedulato partito per intero è riuscito con commit e push: `nixos` (1,02, 0,87 e 1,97 USD; zero, tre e zero dinieghi; il 25 13 minuti e 71 turni, con agenti, `home-manager` e `gogcli` aggiornati), `economia` (1,29, 2,37 e 0,77 USD, il secondo con 77 turni e un diniego su un comando composto, che il suo prompt recepisce in `dc6b092`), `salute` il 23 e il 25 (0,99 e 1,19 USD, il 25 un diniego su `python3 -c`, vincolo voluto), `bi`, `baserow` e `danea-auto` tutti e tre i giorni. Il 25, al ritorno dell'ora solare, le partenze di `deck` cadono all'ora locale dei timer (`+01:00`). Tre arresti per sessione aperta, il sistema che funziona: `method` il 23 alle 15:00 e `salute` il 23 alle 09:55 e il 24 alle 09:00, coi commit concordati del custode attorno (`salute` `d8062a4`, 10:03). Gli arresti di `salute` stanno nella cartella dell'unità, non in `i1/giri`, come ammette la decisione del 2026-10-21 in `o2/home-fatto-da-fare.md`. Il giro di `nixos` del 18 è il più lungo finora
(`5b19d5c`, 9,7 minuti, 69 turni), dentro il tetto di 45 minuti e 5 USD:
manutenzione piena, bump di `ai`, `home-manager` e `gogcli` con build e
switch su `deck`; i tre dinieghi erano `gh api`/`gh release list` per le
versioni upstream (trascritto riletto in sessione col custode, 2026-10-19).
I dinieghi per giro vanno da uno a quattro (`bi`, giro manuale: tre,
`i1/casi-delega-bi-2026-10-17.md`). Dal 2026-10-19 il giro di `method` legge
tutto `~/.local/state/ciclo/` tranne `giri/`, `method` compreso, gli
`autonomy.md` e i prompt del ciclo degli adottanti, e i marker di `svezia` da
`origin` aggiornato dal passo `ciclo-fetch` dell'unità prima del giro: nel
recinto in sola lettura il fetch dal giro falliva
(`i1/giro-method-2026-10-20.md`), dal passo il primo giro schedulato del
2026-10-20 trova i quattro fetch riusciti (`fetch.json`); `tentativi.jsonl` porta `dinieghi` e `oggetto` dal
2026-10-19 (`nixos` `60c2314`), e i controlli `gh` in sola lettura erano già
concessi al giro di `nixos` dal 18 sera (`nixos` `7eb86ac`). La prima delega resta
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
