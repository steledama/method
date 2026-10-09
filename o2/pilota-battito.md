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
- Criteri per il battito schedulato concordati nel register: la delega
  corrente copre solo cicli avviati dal custode.
- La scelta di dove gira il battito.

## Scelta del pilota (aperta, da fare insieme)

- Esclusi `bi` (il più complesso, e ogni push è un rilascio) e `method` (i
  nodi arrivano agli adottanti via symlink, un errore autonomo si propaga).
- Candidato: `nixos`, perché `/manutenzione` committa e pusha già da sola con
  un lock condiviso tra host. Limite: è il repo che governa gli host.
- Alternative: `baserow` (semplice, ma con pochi cambi farebbe soprattutto
  giri vuoti), `salute`, `economia`.

## Da fissare alla partenza

Fissare prima dell'avvio intervallo, durata, perimetro degli atti delegati,
criteri di riuscita e condizioni di arresto. I prerequisiti dipendono dai
risultati dei tre task: [criteri](criteri-autonomia.md),
[home](home-fatto-da-fare.md) e [esecutore](dove-gira-il-battito.md).

- Concordare un campione di decisioni e ricostruzioni da rileggere contro le
  fonti, includendo i verdetti modificati: motivo comprensibile e trailer
  corretti non bastano a provarne la qualità.
- Misurare interventi necessari del custode e tempo di ricostruzione degli
  esiti, con un confronto assistito concordato prima della partenza. Il
  beneficio atteso è meno lavoro di supervisione a qualità conservata;
  frequenza dei giri e quantità dei commit non lo dimostrano.
- Osservare i tentativi anche quando non producono commit: mancata partenza,
  arresto e fallimento devono essere visibili al custode.
- Concordare quando sospendere il pilota e come tornare alla modalità
  assistita, almeno per un atto fuori delega, un impatto alto applicato,
  un arresto invisibile o una ricostruzione errata che altera una decisione.

La delega sulla manutenzione dell'artefatto resta distinta dalle azioni di
dominio. L'esperienza di `/manutenzione` in `nixos` non dimostra da sola la
delegabilità di `eval compare`; negli altri candidati vale lo stesso esame
contro il Goal locale. Nessun candidato è ancora scelto.

## Criterio di chiusura

A fine osservazione, verdetto nel filo [battito autonomo](../i3/battito-autonomo.md)
su fedeltà delle ricostruzioni, rispetto della delega, visibilità degli
arresti e costo per il custode. Dichiarare copertura e limiti del campione;
un pilota privo di casi informativi non certifica l'autonomia. Il custode
decide se estendere, correggere o tornare alla modalità assistita.
