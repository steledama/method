---
data: 2026-06-19
stato: aperto
---

# Il polo Goal del ciclo di sviluppo: dimensioni comuni e posizione auspicata

Emerso dal gate dei cicli annidati (task «Verifica dei cicli annidati»), riempiendo
la cella **Goal-dev** di `metodo` in `action-cycle-matrix`. La cella è stata
declassata a **D** perché il contenuto _dev-specifico_ del polo Goal del ciclo di
sviluppo non è articolato: il `README` dichiara portabilità e osservatorio, che sono
in parte proprietà-bersaglio del **runtime**, non l'obiettivo proprio dello sviluppo.

## L'ipotesi

I Goal dei cicli di **sviluppo** non sono solo contenuto di dominio: condividono
**dimensioni comuni a tutti gli artefatti**, e ogni progetto _fotografa_ (più che
«definisce») la **posizione auspicata** lungo quelle dimensioni — la misura in cui
l'artefatto vuole posizionarsi. Il dominio non determina le dimensioni, determina la
gradualità scelta su ciascuna.

Conseguenza strutturale, coerente con la cucitura (`nested-cycles`): poiché il
Mondo-dev _è_ la macchina del runtime, gli obiettivi del ciclo di sviluppo sono in
larga parte **proprietà desiderate del ciclo runtime**. Il polo Goal-dev è dunque per
natura il luogo dove vivono le desiderata sulla forma del runtime — il che spiega
perché «portabilità» suoni di runtime pur essendo _voluta dallo_ sviluppo.

## Dimensioni candidate (da raffinare)

Emerse nella riflessione, messe alla prova sui cinque artefatti:

- **attrito / golfi / fluidità** — quanto il ciclo scorre senza gulf of execution o
  evaluation;
- **autonomia dell'umano** — umano _in-the-loop_ (dentro ogni iterazione) vs
  _on-the-loop_ (a supervisione);
- **loop-ness e temporalità** — se il ciclo runtime debba essere un loop o meno, e con
  quale cadenza.

Fotografie per artefatto (esempi emersi, da verificare sul campo):

- `salute`: loop quotidiano, umano profondamente in-the-loop;
- `bi`: sync schedulato, umano on-the-loop (monitoraggio);
- `nixos`: episodico, set-and-review;
- `economia`: decisioni episodiche, umano in-the-loop;
- `metodo`: event-driven sul segnale dell'adottante, umano in-the-loop.

Le tre dimensioni paiono raggrupparsi in due famiglie — chiusura/attrito del ciclo
(i golfi) e autonomia/automazione (posizione dell'umano + temporalità) — da
verificare.

## Define vs photograph

Il polo Goal è la **posizione auspicata** (il punto-bersaglio nello spazio delle
dimensioni); il riempimento del ciclo nella matrice è la **fotografia dello stato
attuale**; la **distanza** tra i due è il golfo a scala macro che il ciclo di
sviluppo lavora a chiudere.

## Destinazione

Da sviluppare in modo **deliberato**, non a caldo: candidato il nodo `goal` (e/o un
nodo nuovo sulle dimensioni), con ricaduta su `action-cycle` e `action-cycle-matrix`
(la cella Goal-dev risale da D quando il polo è articolato). Guardia dal-basso
(`method-development`): è teoria-dall'alto, va ancorata a un disagio reale — qui il
disagio è la cella Goal-dev mal-filed — e non sovra-ingegnerizzata prima dell'uso.

## Fuori perimetro

- riempire le posizioni auspicate degli adottanti (ognuno la propria);
- modificare la geometria del gate già chiuso oltre la cella Goal-dev.
