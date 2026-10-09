---
ciclo: runtime
---

# Segnale: lo stato corrente vive anche nel README

Data: 2026-10-09 · Fonte: lettura del bootstrap su `origin` di `crm`
(`cc0500b`) e `baserow` (`305de15`), revisione di
`revisione-bootstrap-adottante`

## Il segnale

Il README di `crm` ha una sezione «Stato»: esito del pilot Twenty, runtime
provato su `svezia`, RPO, «il prossimo incremento» e ciò che resta a valle.
Quello di `baserow` ne ha una con versione corrente, data dell'aggiornamento,
avvio del backup notturno e condizione di chiusura del task. In entrambi i
fatti hanno già una sede: plan, fili `i3/`, catture `i1/` o `world.md`.

`goal-senza-fotografia` ha tolto lo stato corrente dal Goal; il contratto
del README in `kb/readme.md` chiede che il file «punti alle fonti senza
duplicarle», ma non nomina lo stato del lavoro. Oggi le due sezioni
concordano con le fonti: il «prossimo incremento» di `crm` è la prima riga
del suo plan. Nessun controllo della build le confronta con le fonti.

## Contesto

Due casi su sette, entrambi nel gruppo con README costruiti sullo stesso
schema (`crm` e `baserow` condividono «Mappa del repository» e «Metodo»).
Gli altri cinque rimandano allo stato senza riportarlo. Non è verificato se
la sezione serva un lettore distinto, per esempio chi apre il repo su GitHub
senza la home.

## Questione per il metodo

Se lo stato corrente nel README sia una fotografia da trattare come quella
del Goal o un orientamento legittimo per un lettore che non apre il plan.
