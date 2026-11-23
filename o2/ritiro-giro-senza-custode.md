---
sintesi: "Il giro senza custode esce dal canone e resta in git, deciso dal custode il 2026-11-23: nessun adottante noto lo esercita più, e il recinto con lo stesso utente delle sessioni non è sicuro per costruzione. Via skill, strumenti e rotte del giro, prescrizione che chiude il criterio ciclo-autonomo, rilascio come minor."
ciclo: dev
---

# Ritiro del giro senza custode

## Origine

Segnale di `nixos-lavoro` del 2026-11-23: dopo casa anche il gruppo lavoro
rinuncia al ciclo senza custode, e chiede che statuto abbiano nel canone
prescrizione, lanciatore, esecutore, `/cycle autonomo`, rotte `/_ciclo/` e
`dopo --giro` se nessuno li usa più. Lo stesso giorno il custode decide
l'uscita anche di `danea-auto`, l'ultimo adottante noto col giro
(il filo `i3/ciclo-autonomo.md`, in git fino a `2988d7d`).

## Decisione del 2026-11-23

Il custode sceglie di **togliere**, non di isolare
([snellimento-skill](snellimento-skill.md), «Il giro senza custode nelle
skill forkate»):

- il motivo dell'abbandono è del canone, non di un repo: il recinto con lo
  stesso utente delle sessioni non è sicuro per costruzione;
- con `method` distribuito a sconosciuti, un'opzione documentata che si sa
  insicura è un rischio consegnato a loro;
- tenerla vuol dire mantenere strumenti, test e rimandi senza uso, mentre
  cinque adottanti li hanno già potati a mano;
- la storia resta in git: un giro con un recinto vero, un utente per ciclo,
  andrebbe comunque ridisegnato sul confine di esecuzione.

Il ciclo in sessione resta: `/cycle` senza argomento, criterio
`ciclo-delegato`.

## Stato del lavoro nel canone — 2026-11-23

Rimossi il lanciatore, l'esecutore Codex, la modalità senza custode di
`/cycle`, le rotte e la sezione della vista, e i controlli del gate legati
alle trascrizioni; `ultimo_giro.py` resta perché serve alle sessioni. La
prescrizione di recepimento è predisposta in `o3/ritiro-ciclo-senza-custode.md`.
La pausa della traduzione è tolta. Il filo è chiuso, il lettore dei dinieghi
e il monitoraggio del giro sono rimossi. Restano il recepimento negli
adottanti e il rilascio. La review integrale della KB è rinviata a una
sessione dedicata. Le modifiche locali non sono ancora un rilascio.

Verdetto del filo, chiuso il 2026-11-23: alla domanda «con quali garanzie
ogni repo arriva al giro senza custode?» la risposta è che, con la stessa
utenza delle sessioni, nessuna garanzia regge per costruzione. Il giro è
uscito da tutti gli adottanti noti e dal canone; un ritorno è un progetto
nuovo sul confine di esecuzione.

## Le potature già fatte negli adottanti

Cinque adottanti hanno già potato le skill forkate, il 2026-11-23:
`nixos-lavoro` (`cycle`, `eval`, `exec`, `commit`, `manutenzione`, con la
differenza dichiarata nel suo `kb/cicli.md`), `bi` `7b4a763f`, `baserow`
`c57cd83`, `abbinatore` `bfc74d8` e `danea-auto`. Quest'ultima è riferita
senza SHA e non riletta qui; la differenza dal canone è dichiarata nella sua
skill `/method` e nel marker, come attesa fino al tag che pota le skill
canoniche. I fork vanno confrontati durante il recepimento.

`danea-auto` ha tenuto, perché serve anche alla sessione: `/cycle` senza
argomento con `Esiti:` e `Prossimo:`, il minimo per stadio,
`o3/ultimo_giro.py`, `o3/scadenze.py`, la visione d'insieme di `exec plan`
e il gate di `/commit`. Ha lasciato anche le rotte `/_ciclo/` del suo
servizio delle viste. Il censimento ha confermato che `ultimo_giro.py`
serve anche alla sessione.

## Passi rimasti

1. Verificare e completare il recepimento della prescrizione negli adottanti
   del custode; per quelli mantenuti da altri fa fede la versione dichiarata.
2. Preparare il rilascio `v0.3.0` con le note per gli adottanti.

## Criterio di chiusura

Il canone non contiene più il giro senza custode, la prescrizione è
recepita dagli adottanti del custode, il filo è chiuso e `v0.3.0` è
pubblicata.

Connessioni:

- [snellimento-skill](snellimento-skill.md)
- [strumenti-del-coordinatore](strumenti-del-coordinatore.md)
