---
ciclo: runtime
---

# Ritiro del ciclo senza custode

Il canone ritira il giro senza custode: nessun adottante noto lo usa più e il
recinto con la stessa utenza delle sessioni non è sicuro per costruzione.
Il ciclo avviato in sessione e la delega interattiva restano. La storia è in Git.

## Recepimento nell'adottante

1. Verificare localmente stato di unità, timer, lanciatori e configurazioni;
   fermare e rimuovere quelli dedicati al giro senza custode secondo le
   autorizzazioni e i vincoli dell'host. Non presumere lo stato dai marker.
2. Ritirare il criterio `ciclo-autonomo`, prompt, permessi, strumenti, test,
   rotte e riferimenti dedicati; confrontare le skill forkate con il canone.
   Conservare strumenti e contratti che servono anche alle sessioni.
3. Aggiornare viste, indici e documentazione, verificare test e build, quindi
   registrare il recepimento nel marker secondo `/method`.

## Criterio di recepimento

La prescrizione è recepita quando `i3/allineamento-metodo.md` ha una voce
che nomina `ritiro-ciclo-senza-custode` come recepita, con lo SHA del commit
di recepimento, e nell'adottante non restano unità o timer del giro, il
criterio `ciclo-autonomo` né la modalità `cycle autonomo`. La verifica la fa
`python3 o3/prescrizioni.py verifica ritiro-ciclo-senza-custode`.

Un eventuale progetto futuro parte da una nuova progettazione sicura: utenza
dedicata, privilegi minimi, confini di esecuzione espliciti e verificati.
Questa prescrizione non autorizza atti su host o repository altrui.
