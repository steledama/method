---
data: 2026-10-09
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Il Goal conserva il nord e punta ai segnali

## Cosa e perché

Il contratto di `kb/goal-register.md` conserva motivo, obiettivi, posizione
auspicata di sviluppo e puntatori ai segnali. Lo stato del lavoro vive nei
fili `i3/` e nel plan, le misure osservate nella fonte; le decisioni prese
su quelle misure restano versionate con provenienza.

La [lettura del churn](../i2/churn-goal-adottanti.md) mostra che la seconda
copia dello stato nel Goal alimentava aggiornamenti senza cambiare il nord.
Il custode ha ratificato la separazione; è applicata in `method`. Il
recepimento dei sette adottanti resta da verificare tramite il loro `/method`.

## Ricetta locale

1. Leggere insieme `goal.md`, i fili che raggiunge, `o1/plan.md` e le fonti
   delle misure. Distinguere scopi e soglie desiderate da esiti osservati,
   stato del lavoro, conteggi e recepimenti. Conservare motivo, obiettivi,
   numerazione e posizione auspicata del Goal di sviluppo.
2. Per ogni fotografia da rimuovere confrontare la destinazione: se il
   Goal porta il fatto più fresco, fonderlo prima nel filo o nel task
   pertinente. Conservare decisione e provenienza delle misure necessarie
   a ricostruirla; non cancellare l'unica evidenza e non creare un nuovo
   contenitore solo per spostare la copia.
3. Per ogni obiettivo lasciare il puntatore al segnale vivo — filo, audit,
   report o vista — oppure dichiarare il buco di misura. Il puntatore
   descrive dove verificare, senza ricopiare l'ultimo esito. La coda resta
   la fonte del lavoro futuro; il Goal di sviluppo dichiara il desiderato,
   i segnali rendono la posizione osservata e lo scarto.
4. Allineare README, disciplina del register e fork di `eval`, `exec` e
   `commit`: verificare copertura e puntatori, aggiornare lo stato nei fili
   e nel plan. Conservare i gate e le autorizzazioni locali. Il cambio di
   un puntatore non equivale a un nuovo scopo e questa ricetta non concede
   autonomia aggiuntiva.
5. Verificare i lettori del Goal, comprese le viste e i builder di dominio.
   Una vista che mostra lo stato per obiettivo lo deriva dai segnali,
   senza esigere una copia nel register. Mantenere le chiavi e le ancore
   usate da plan e fili; eseguire `python3 o3/view/build.py --check` e i
   controlli locali pertinenti.
6. Registrare nel marker commit del canone, file verificati, esito,
   adattamenti motivati e limiti. Il canone prescrive la forma; il dominio
   decide la mappatura sulle proprie fonti.

## Indizi da verificare in loco

In `danea-auto` il clean-rate e in `bi` i conteggi erano i casi principali
di misure ricopiate nella finestra studiata. Verificare la situazione
corrente: la vista può leggerli da log o export; se non lo fa ancora,
dichiarare fonte e modo di consultarla senza perdere il riscontro. Non
imporre qui un nuovo builder o la rimozione generale delle misure da Git:
la ricetta elimina la duplicazione nel Goal e conserva l'evidenza delle
decisioni. Negli altri adottanti il campione indicava soprattutto copie di
stato qualitativo, da confrontare con fili e plan.

## Verifica e chiusura

Il `/method` locale verifica che il nord sia conservato, ogni obiettivo
abbia un segnale raggiungibile o un buco dichiarato, nessun fatto fresco
sia perso e i consumatori rispettino il contratto. La build verifica la
struttura, la revisione locale la semantica. La prescrizione resta attiva
fino all'esito dei sette, con adattamenti motivati dove necessari;
`i3/audit-adottanti.md` ne segue il recepimento, senza governare le code locali.
