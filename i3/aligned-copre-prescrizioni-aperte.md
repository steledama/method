---
ciclo: dev
---

# `aligned` copre anche le prescrizioni aperte

**Misura**: «Propagare il canone e chiudere il loop con gli adottanti»
(`goal.md`, obiettivo 2).

## Verdetto

Il marker `aligned` dell'adottante non certificava ciò che dichiarava. Il
`/method` leggeva solo i commit di `method` successivi al proprio cursore:
una prescrizione nata prima del cursore e rimasta aperta usciva dal suo
orizzonte, e il marker che avanzava la copriva senza che nessuno l'avesse
riletta. Il caso è `semplificazione-lessico-struttura`, nata il 2026-08-21:

- il 2026-08-22 il gap è visto in `bi` e `crm` e tenuto come watchpoint;
- il 2026-09-24 è vivo in `bi`, `crm` ed `economia`, tutti `aligned`. È il
  secondo segnale che la guardia dal-basso aspettava;
- il 2026-09-25 tutti e sei girano `/method` fino a `eb3f400`. `crm` ed
  `economia` recepiscono la prescrizione; `salute` dichiara nel marker di aver
  riletto le prescrizioni aperte nei file. `bi` passa `aligned` col lessico
  ancora vivo, al terzo `/method` dopo la segnalazione.

Il canone ricevuto era lo stesso commit per tutti. La differenza stava in cosa
leggeva il giro: chi rileggeva le prescrizioni aperte le chiudeva, chi leggeva
solo il delta no. La rilettura dipendeva dalla memoria di chi conduceva il
giro, non da un passo della skill.

Delle due risposte possibili si è scelta la prima. `/method` ha un passo
proprio, «Rileggi le prescrizioni aperte»: a ogni giro legge `## Contenuti` di
`o3/prescriptions.md` e verifica ciascuna prescrizione nei file dell'adottante.
`aligned` ora copre anche queste, e il marker non avanza finché una
prescrizione pertinente resta senza esito. L'alternativa, restringere
`aligned` a «delta dei commit recepito», avrebbe reso il marker onesto ma
avrebbe lasciato le prescrizioni senza un giro che le verifica: toccava al
battito mensile `/adottanti`, che è d'insieme e in sola lettura.

Il costo è contenuto: le prescrizioni sono poche e si potano quando tutti le
hanno recepite, quindi la rilettura è una ricerca mirata per ciascuna.

## Primo collaudo: `bi`, 2026-09-25

`bi` ha recepito il passo nel proprio fork e lo ha applicato nello stesso
giro (`51ec6bce`, marker a `6408f55`). Letto nei file e non nel marker, il
giro ha retto:

- il lessico sopravvissuto a tre `/method` è sparito da `README.md`,
  `CLAUDE.md`, `i2/bi-in-sintesi.md` e dal fork `eval`. Restano solo tre
  menzioni del «recepimento dell'atrio» in `goal.md`, `i2/interpretations.md`
  e `kb/convenzioni-script.md`, dichiarate nel marker come cronaca di un task
  chiuso: la distinzione fra cronaca e lessico vivo è stata fatta, non
  saltata;
- la rilettura ha preso anche una prescrizione che nessuno aveva segnalato:
  `revisione-bootstrap-adottante`, applicata riducendo l'inventario
  duplicato «Strumenti» del README a un rimando alla sezione omonima di
  `CLAUDE.md`, che esiste e porta skill, comandi e formatter;
- il marker nomina ogni prescrizione aperta con il suo esito, comprese
  quelle già soddisfatte e quella non pertinente (`ingresso-adottante`).

È un caso solo, e condotto con un prompt che indicava il bersaglio: prova che
il passo funziona quando si esegue, non ancora che si esegua senza essere
ricordato.

## Secondo collaudo: `nixos` e `crm`, 2026-09-25

Lo stesso giorno `nixos` (`33714d0`) e `crm` (`a13da6b`) hanno girato
`/method` fino a `a8ab92e`. Nessuna prescrizione nominava i loro residui,
e ciascuno ha trovato il proprio: «questa stanza» nell'indice `o3/` di `nixos`,
«inventario dell'atrio» nell'indice `o3/` di `crm`, più un commento in
`pyproject.toml` che la ricerca d'insieme sul solo Markdown non vedeva. I due
marker riportano l'esito di ogni prescrizione aperta. Il fork di `crm`
rimanda alla skill canonica invece di copiarla: il passo gli è arrivato
senza recepimento.

Letti nei file su origin, i sei non hanno più il lessico vivo: restano
cronaca («recepimento dell'atrio», commenti di codice sulla «Fase B» in
`bi`) e italiano comune. `semplificazione-lessico-struttura` è potata da
`o3/`.

## Tensioni aperte

- `economia`, `salute` e `danea-auto` non hanno ancora girato col passo: il
  loro primo giro dirà se regge anche senza una prescrizione che li
  riguardi, cioè se la rilettura resta una verifica o scivola in rito;
- il battito `/adottanti` continua a verificare nei file e non nei marker,
  finché i giri non mostrano che `aligned` e i file coincidono. Due giri in cui
  coincidevano sono il primo dato; se il battito del
  2026-11-01 lo conferma, la verifica d'insieme delle prescrizioni si può
  alleggerire.
