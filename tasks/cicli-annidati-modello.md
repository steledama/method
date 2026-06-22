---
data: 2026-06-22
stato: aperto
sintesi: "Il diagramma «Cicli annidati» va rifatto come annidamento per contenimento: ciclo di sviluppo esterno (Goal-dev universale in cima), il cui World=Artefatto contiene il ciclo runtime (Goal-runtime → sei stadi → World-runtime che sporge sul dominio). Quattro vincoli da incidere in nested-cycles prima di ri-derivare la slide."
---

# Cicli annidati: modello dei poli + diagramma rifatto

## Problema

La slide «Cicli annidati: due Mondi» (`interpretations/metodo-in-sintesi.md`)
rappresenta i due cicli come **due colonne `vertical-cycle` alla pari**, ciascuna
ridotta a Goal → o3 → World. È difettosa su due piani:

- **viola il nodo**: `nested-cycles` §«La cucitura, non l'affiancamento» dice che
  mostrare i due cicli «come due stati alla pari — due colonne, due schede
  commutabili — appiattisce l'annidamento in parallelismo e perde proprio ciò che
  il metodo aggiunge a Norman»;
- **mancano i sei atti**: ogni ciclo è lo specchio a sei atti, ma il diagramma ne
  mostra uno solo (o3) più il ritorno i1.

## Il modello-bersaglio (deciso 2026-06-22)

Annidamento **per contenimento**, non due colonne alla pari:

```
            ◆ GOAL-DEV   dimensioni comuni a TUTTI i domini
            │            (attrito · autonomia · temporalità,
            │             calibrate per dominio, non ridefinite)
   ┌────────┴─────────┐
   ↓ o1            i3 ↑
   ↓ o2  esec ‖ val i2 ↑     CICLO DI SVILUPPO
   ↓ o3            i1 ↑
 ┌─┴──────────────────────────────────┐
 │  ARTEFATTO  = World-dev             │
 │                                     │
 │          ◆ GOAL-RUNTIME  scopo dom. │
 │   ┌──────┴──────┐                   │
 │   ↓ o1      i3 ↑    CICLO RUNTIME   │
 │   ↓ o2      i2 ↑                    │
 │   ↓ o3      i1 ↑                    │
 │          ● WORLD-RUNTIME  realtà    │
 └──────────────────│──────────────────┘
                     ▼ agisce sul dominio (fuori)
```

- **Goal-dev in cima, universale**: le dimensioni comuni a tutti i domini,
  calibrate per dominio e non ridefinite (`development-goal`). È la parte
  portabile; scendendo si diventa domain-specifici fino al World-runtime — un
  **gradiente di portabilità** verticale che oggi non si vede.
- **due cicli interi a sei stadi** (esecuzione ‖ valutazione), non mozzati.
- **artefatto = World-dev**: polo-fondo del dev e contenitore del runtime — la
  cucitura.
- **quattro poli** (Goal-dev · Artefatto · Goal-runtime · World-runtime), con
  l'artefatto come contenitore-cucitura. (Non i «3» della prima ipotesi: la
  struttura conta più del numero.)

## I quattro vincoli da incidere in `nested-cycles` (i3)

Il modello tocca la prosa attuale del nodo: vanno fissati **prima** di ri-derivare
la slide (il deck rivela, i nodi risolvono).

1. **Verso dell'annidamento** — il dev è esterno, il runtime è dentro l'artefatto
   (lettura _operativa_: l'artefatto in opera ospita il runtime). Il nodo oggi
   narra l'inverso (_«apre la scatola nera»_ del runtime e dentro trova il dev —
   lettura _di provenienza_). È la stessa cucitura vista dai due capi: rendere la
   prosa coerente col verso del disegno, o dichiararla esplicitamente duale.
2. **World-runtime sporge** — il dominio (mail, transazioni, salute) non è
   contenuto nell'artefatto: l'artefatto ci agisce sopra. Nel disegno il
   World-runtime esce dal fondo della scatola, non ci sta chiuso dentro.
3. **Agente ⊥ annidamento** — i due cicli non sono «uno umano, uno IA»: entrambi
   sono umano + LLM (il dev lo percorriamo in due, adesso). Cambia il _mix_, ed è
   un gradiente — peso umano alto nel dev, che scivola verso l'LLM nel runtime con
   l'umano da _in-the-loop_ a _on-the-loop_. Quella posizione è essa stessa una
   dimensione del Goal-dev (`development-goal`, autonomia). Il diagramma può
   suggerire il mix (velatura, etichetta) ma tiene agente e annidamento su assi
   distinti — collassarli è lo stesso errore che aveva fatto «sparire» o1.
4. **I sei stadi sono punti di controllo/rientro** — ogni stadio reso visibile è
   insieme il punto dove l'umano ispeziona e interviene e il punto dove l'LLM
   rientra nel loop senza ricostruirlo (`action-cycle`, §«Saltare uno stadio»).
   Vanno mostrati e osservabili in _entrambi_ i cicli: è la ragione anti-collasso
   (collassarli fa perdere il controllo a entrambi gli agenti, con frustrazione di
   tutti), non l'estetica.

## Cautela

- `development-goal` tiene Goal-dev e Goal-runtime distinti (forma vs scopo): il
  contenimento li mette su altitudini diverse, non li fonde.
- Il diagramma resta **resa**: il modello si chiude prima nel nodo (i3), poi la
  slide e la home si ri-derivano (cfr. `presentazione-i2`).

## Criterio di chiusura

`nested-cycles` dichiara i quattro vincoli sopra senza ambiguità; il diagramma è
ri-derivato come annidamento per contenimento (due cicli interi, l'artefatto
contenitore, il World-runtime che sporge, l'agente come asse ortogonale) e rispetta
il nodo; audit `kb_tools.py` pulito.
