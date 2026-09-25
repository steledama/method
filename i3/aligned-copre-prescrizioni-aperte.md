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

## Tensioni aperte

- collaudo: il passo arriva agli adottanti nel delta del prossimo `/method`,
  quindi si esercita a partire dal giro successivo al suo recepimento. Il
  primo caso utile è `bi`, che ha ancora aperta la prescrizione sul lessico;
- il battito `/adottanti` continua a verificare nei file e non nei marker,
  finché i giri non mostrano che `aligned` e i file coincidono. Se coincidono,
  la verifica d'insieme delle prescrizioni si può alleggerire.
