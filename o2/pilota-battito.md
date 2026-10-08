---
sintesi: "Un adottante scelto insieme fa girare il battito autonomo a intervalli concordati per un periodo di osservazione, e il suo esito decide se e come estenderlo agli altri."
ciclo: dev
---

# Pilota del battito

Un repo fa da apripista per il loop agentico di base, su cui poi si
articolano i loop di dominio.

## Prerequisiti

- Push autonomo recepito nel repo pilota: soddisfatto, recepito dai sette
  il 2026-10-08 (in `bi` con l'eccezione del codice del ciclo).
- Trailer di autonomia e impatto (in `/commit` dal 2026-10-08) e sezione
  «fatto» della home: il custode
  deve vedere i giri prima di toglierne la conferma.
- Il primo criterio di autonomia scritto nel register.
- La scelta di dove gira il battito.

## Scelta del pilota (aperta, da fare insieme)

- Esclusi `bi` (il più complesso, e ogni push è un rilascio) e `method` (i
  nodi arrivano agli adottanti via symlink, un errore autonomo si propaga).
- Candidato: `nixos`, perché `/manutenzione` committa e pusha già da sola con
  un lock condiviso tra host. Limite: è il repo che governa gli host.
- Alternative: `baserow` (semplice, ma con pochi cambi farebbe soprattutto
  giri vuoti), `salute`, `economia`.

## Da fissare alla partenza

Intervallo, durata dell'osservazione e criterio di riuscita: ad esempio
ogni livello d'impatto con un motivo ricostruibile, nessun impatto alto
applicato invece che proposto.
