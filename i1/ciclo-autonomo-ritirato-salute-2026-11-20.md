---
ciclo: runtime
---

# Ciclo autonomo ritirato in `salute` per il costo del confine

Data: 2026-11-20 · Fonte: `salute` `i1/casi-delega.md`, sezione «Ciclo
autonomo ritirato per il costo del confine», e commit `0ce53a5`, letti nel
checkout `~/salute`; inoltro della sessione `salute` via Herdr su richiesta
del custode. Le prove di `nixos` (`bda240d`, `i2/confine-dei-cicli.md`) sono
riferite da `salute`, non rilette qui. Nel repo di origine il caso resta «da
inoltrare» finché non risulta acquisito da `method`.

## Il caso

Il `/method` di `salute` del 2026-11-20 recepisce il contratto «Delega e
confine di esecuzione» (`15f4d3f`, [consent](../kb/consent.md)). Le prove di
`nixos` sul giro `ciclo-salute` di `deck` danno un recinto chiuso
sull'accesso diretto ai file e aperto sulle capacità della stessa identità:
manager utente, niri, Herdr, keyring, chiave SSH, rete, `rclone.conf`
sull'intero Drive. Il giro esegue codice, quindi i deny dei permessi non
limitano.

Alternative valutate dal custode: chiudere i canali con la stessa identità,
un utente dedicato per repo (la forma più portabile fra sistemi operativi),
il loop dell'harness (stessi problemi, più legame all'harness), ritirare il
gradino. Sceglie il ritiro: in un repo molto personale privacy e minimalismo
pesano più del valore del giro, e il ciclo resta in sessione (`/cycle`).

In `salute` è fatto in `0ce53a5` (`Autonomia: concordato`): tolti
`o3/ciclo/`, il criterio `ciclo-autonomo`, la modalità `cycle autonomo` e i
rami senza custode in `eval` ed `exec`; chiuso come non pertinente il task
del confine. La divergenza è dichiarata nel marker
`i3/allineamento-metodo.md`. Resta a `nixos` togliere l'unità
`ciclo-salute`.

## Le tre questioni per il metodo

1. **Quando un gradino va ritirato.** Il filo
   filo sul ciclo autonomo, conservato nella storia Git lo chiede; `salute` è il primo
   ritiro, per scelta del custode sul rapporto costo/valore e non per un
   rosso (nessun atto fuori delega, nessun fallimento a motivarlo).
2. **Il Goal di sviluppo.** Il custode propone di passare da «ogni repo un
   artefatto cognitivo con il proprio ciclo autonomo di runtime» a «… con il
   proprio ciclo di runtime»: l'autonomia sarà importante in alcuni progetti
   e da togliere in altri. Il cambio del Goal è del custode.
3. **Il contratto del confine e l'host.** Dichiarare il confine coi
   meccanismi di un host lega l'adottante a un altro repo (`nixos`), contro
   l'agnosticismo dal sistema operativo. Il contratto potrebbe chiedere
   all'adottante capacità ed esclusioni in termini neutri, con l'host che le
   attua e le prova, eventualmente con uno strumento di prova del canone.

## Fatti accanto al caso

- Il filo dice già, in «Condizione di chiusura», che «il ritorno alla
  modalità assistita resta possibile per il singolo repo o gradino, non per
  la direzione». Il testo del Goal («ogni repo … ciclo autonomo») non
  contempla quel ritorno: la proposta 2 allineerebbe il Goal a una clausola
  che il filo ha già.
- Il filo non ha criteri di ritiro: «Cosa sposterebbe il verdetto» elenca
  segnali contro la direzione, non condizioni per il singolo repo. Il caso
  introduce un motivo che lì non compare: il costo del confine rispetto al
  valore del giro, giudicato dal custode.
- Il contratto in [consent](../kb/consent.md) si dichiara «indipendente da
  sistema operativo e harness» e lascia ad adottante e host «l'attuazione
  adatta», ma chiede all'adottante anche «meccanismo che limita le capacità»
  ed «evidenza riferita alla configurazione effettiva». Sono queste due voci a
  portare nell'adottante i meccanismi dell'host: la proposta 3 le
  sposterebbe all'host, lasciando all'adottante dati, capacità ed esclusioni.
- Per `method` su `deck` il confine non è ancora dichiarato nella forma del
  contratto (filo, «Confine di esecuzione»): la proposta 3 tocca anche lui.
- Copertura del filo: `salute` esce dal ciclo autonomo il 2026-11-20.
  `nixos` ritira l'unità `ciclo-salute` in `9ebc6f7` (su `origin/main`);
  su `deck` non c'è più un timer del giro di `salute`, verificato con
  `systemctl list-timers` il 2026-11-20 (resta il timer della
  pubblicazione della presentazione).
- Un caso solo, ma con decisione del custode già attuata.
