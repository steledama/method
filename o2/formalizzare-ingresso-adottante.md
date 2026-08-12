---
sintesi: "Formalizzare un protocollo leggero per ammettere un nuovo adottante nel territorio: inventario canonico, marker verificato, baseline locale, conteggi storici preservati e viste rigenerate. I due casi reali sono crm e danea-auto; l'automazione resta rinviata finché una ricorrenza ne dimostra il valore."
ciclo: dev
---

# Formalizzare il protocollo d'ingresso adottante

## Problema

Gli ingressi di `crm` e `danea-auto` hanno richiesto la stessa bonifica manuale
su register, bussola, nodi, piano, audit e viste. Nessuna interfaccia del metodo
copre l'ammissione: `/adottanti` osserva un territorio già dato e `method`
allinea un progetto già riconosciuto come adottante.

## Atto

- scegliere la casa minima del protocollo nell'osservatorio, senza creare una
  skill autonoma prima che la frequenza la giustifichi;
- elencare le rappresentazioni correnti da aggiornare e i controlli da eseguire;
- imporre la distinzione fra conteggi correnti e fotografie storiche datate;
- includere marker, baseline, adattamenti intenzionali, limiti di verifica e
  prima finestra `/adottanti`;
- verificare la procedura retrospettivamente sui due ingressi del 2026-08-12.

## Vincoli

- il protocollo non modifica le code degli adottanti;
- una ricerca testuale propone candidati, non riscrive automaticamente numeri;
- l'adozione di un artefatto produttivo non certifica il suo runtime;
- le viste derivate vengono rigenerate, non aggiornate a mano;
- nessuna nuova skill o automazione senza un terzo uso che ne mostri il costo.

## Criterio di chiusura

Un runbook canonico permette di ricostruire entrambi gli ingressi senza memoria
di sessione, distingue correttamente inventario e storia, e indica quale segnale
sarà letto al primo audit del nuovo adottante.
