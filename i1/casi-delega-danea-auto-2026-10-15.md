---
ciclo: runtime
---

# Caso della delega: chiusura preventiva di LibreOffice in `danea-auto`

Data: 2026-10-15 · Fonte: `danea-auto`
`i1/delega-chiusura-libreoffice-preventiva.md` a `18e95bf` su `origin/main`,
inoltrato dalla sessione del custode su `danea2` il 2026-10-19. Il testo
inoltrato aggiorna il riscontro al 19/10 09:16; il file a `18e95bf` lo ferma
alla misura del 16/10 11:19 (zero ritentativi in 25 run orari e nel
giornaliero), il resto coincide. Portato in `method` su richiesta del
custode. Nel repo di origine il caso resta «da inoltrare» finché un giro
locale non lo segna «acquisita da method».

## Contesto

Ciclo congiunto `/eval` + `/exec` avviato dal custode su `danea2`. Il
confine in gioco è in `autonomy.md` di `danea-auto`, «Confini di dominio»
(versione del 2026-10-09): entro la delega rientra «il ripristino di
LibreOffice incastrato: chiusura delle istanze `soffice` e wizard di
ripristino». La prevenzione automatica è una proposta separata e ancora da
decidere (`o2/riavviare-libreoffice-col-riavvio.md`: chiusura giornaliera
alle 05:45, settimanale o manuale); è una funzionalità nuova in produzione e
resta fuori dalla delega in ogni caso.

## Il caso

**Situazione.** Alle 10:3x `stats.ps1` segnalava la rampa del precursore
(43, 75, 39 ritentativi `^+s` al giorno dal 13/10) su un'istanza LibreOffice
di 14 giorni, senza documenti aperti; il run delle 10:00 era già caduto. Le
due crisi note erano arrivate 4–5 giorni dopo l'inizio della rampa.

**Confine.** LibreOffice non era incastrato ma in degrado misurato: l'atto
era lo stesso del confine, la condizione no.

**Comportamento.** L'agente ha chiesto sul punto, con la chiusura
raccomandata, e intanto ha proseguito il resto del ciclo. Alternative:
chiudere entro la delega leggendo «incastrato» in senso largo; lasciar
girare e registrare solo la rampa. Il custode ha scelto la chiusura,
eseguita alle 10:34 in modo ordinato.

**Riscontro.** Fatto: chiusura senza wizard e senza processo forzato. Fatto
misurato il 19/10 alle 09:16 (`stats.ps1` e conteggio nel log): sull'istanza
nuova, partita alle 10:37:52 del 15/10, zero ritentativi `^+s` in 95 run
orari e 4 giornalieri, tutti puliti; nei tre giorni precedenti ogni run ne
aveva almeno uno. Resta da vedere se la rampa torna intorno ai 12 giorni
d'uptime (verso il 27/10), e quindi se la prevenzione serviva davvero. Il
riesame tocca alle prossime `/eval` di `danea-auto`.

**Questione per il metodo.** Un atto delegato per lo stato guasto di una
risorsa copre anche la prevenzione, quando un precursore misurato e già
validato annuncia quel guasto? Ipotesi dell'adottante, non regola: sì, se
l'atto è identico, avviene fuori slot e il precursore ha una soglia scritta
in uno strumento.
