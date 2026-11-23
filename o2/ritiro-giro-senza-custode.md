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
([ciclo autonomo](../i3/ciclo-autonomo.md)).

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

## Le potature già fatte negli adottanti

Cinque adottanti hanno già potato le skill forkate, il 2026-11-23:
`nixos-lavoro` (`cycle`, `eval`, `exec`, `commit`, `manutenzione`, con la
differenza dichiarata nel suo `kb/cicli.md`), `bi` `7b4a763f`, `baserow`
`c57cd83`, `abbinatore` `bfc74d8` e `danea-auto`. Quest'ultima è riferita
senza SHA e non riletta qui; la differenza dal canone è dichiarata nella sua
skill `/method` e nel marker, come attesa fino al tag che pota le skill
canoniche. Il confronto del passo 2 parte da questi fork.

`danea-auto` ha tenuto, perché serve anche alla sessione: `/cycle` senza
argomento con `Esiti:` e `Prossimo:`, il minimo per stadio,
`o3/ultimo_giro.py`, `o3/scadenze.py`, la visione d'insieme di `exec plan`
e il gate di `/commit`. Ha lasciato anche le rotte `/_ciclo/` del suo
servizio delle viste. È un primo riscontro per il censimento del passo 1:
`ultimo_giro.py` è nell'elenco di ciò che esce, e va verificato se serve
davvero alla sessione.

## Passi

1. Censire nel canone ciò che esiste solo per il giro senza custode:
   `o3/lanciatore.py`, `o3/esecutore_codex.py`, `o3/ciclo/`,
   `o3/ultimo_giro.py`, `o3/view/ciclo.py` e le rotte `/_ciclo/` di
   `serve.py`, `dopo --giro` e il controllo `stadi` di `commit_gate.py`, i
   test, la modalità `autonomo` di `/cycle` e i rimandi in `eval`, `exec`,
   `commit` e nei nodi (`kb/consent.md`, `kb/view-publishing.md`, «Stato
   operativo letto a richiesta»). Per ciascuno: esce, oppure serve anche alla
   sessione e resta.
2. Togliere, coi test e le viste verdi, e potare le skill canoniche
   confrontandole con quelle già potate di `nixos-lavoro`.
3. Prescrizione in `o3/` che chiude il criterio `ciclo-autonomo` negli
   adottanti e allinea i fork; per gli adottanti mantenuti da altri fa fede
   la versione.
4. Aggiornare la «Direzione» di `o1/plan.md`, `autonomy.md` e `goal.md` dove
   parlano del giro senza custode; chiudere il filo `i3/ciclo-autonomo.md`
   col verdetto; togliere la pausa `p1` della traduzione, che aspettava il
   riesame del filo.
5. Rilascio `v0.3.0` con le note: chiede qualcosa agli adottanti.

## Criterio di chiusura

Il canone non contiene più il giro senza custode, la prescrizione è
recepita dagli adottanti del custode, il filo è chiuso e `v0.3.0` è
pubblicata.

Connessioni:

- [snellimento-skill](snellimento-skill.md)
- [strumenti-del-coordinatore](strumenti-del-coordinatore.md)
- [ciclo autonomo](../i3/ciclo-autonomo.md)
