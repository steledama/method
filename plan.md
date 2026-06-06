# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, prioritizzati, con le loro
dipendenze. Sta in root — letto a ogni sessione — perché la sua altezza nel ciclo
vince sulla pace: è una vista veloce, ma è la prima a orientare il lavoro. I
dettagli operativi di ciascun task vivono in `tasks/`; qui sta solo la supervisione.

Regola: ogni file in `tasks/` ha una riga qui; ogni riga sostanziale ha un file.
Quando un task è completato la riga sparisce — lo storico resta in git, `why.md` e
nei nodi aggiornati.

## Task aperti

- [sostanza-why](tasks/sostanza-why.md) — runbook per ribaltare `why.md` da log datato a memoria per motivazione, un repo per sessione. `metodo` ✅ fatto; **prossimo `bi`**, poi `nixos`, ed `economia`/`salute` quando raggiungibili
- [fonti-pace-layering](tasks/fonti-pace-layering.md) — verifica delle fonti (Duffy, Brand) e maturazione del nodo `pace-layering` da bozza a maturo
- [de-cablaggio-agenti](tasks/de-cablaggio-agenti.md) — de-cablaggio fatto (binomio «due agenti» ammorbidito a caso saliente nei nodi); resta solo la maturazione di `agente`, bottom-up, quando l'uso multi-agente diventa reale
