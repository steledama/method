# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, prioritizzati, con le loro
dipendenze. Sta in root — letto a ogni sessione — perché la sua altezza nel ciclo
vince sulla pace: è una vista veloce, ma è la prima a orientare il lavoro. I
dettagli operativi di ciascun task vivono in `tasks/`; qui sta solo la supervisione.

Regola: ogni file in `tasks/` ha una riga qui; ogni riga sostanziale ha un file.
Quando un task è completato la riga sparisce — lo storico resta in git, `why.md` e
nei nodi aggiornati.

## Task aperti

- [refactor-atrio](tasks/refactor-atrio.md) — ridisegno della root come atrio/system image (Filosofia B): `metodo` ✅ (commit c66cf82); nixos ✅, bi ✅; economia e salute hanno il task `adotta-atrio` aperto (carrier eseguito)

- [fonti-pace-layering](tasks/fonti-pace-layering.md) — verifica delle fonti (Duffy, Brand) e maturazione del nodo `pace-layering` da bozza a maturo
- [fonti-mente-estesa](tasks/fonti-mente-estesa.md) — ingest delle fonti di Andy Clark (mente estesa) e vaglio del filone come pavimento del metodo; disciplina i1→i2→i3, niente nodo dal sentito dire
- [de-cablaggio-agenti](tasks/de-cablaggio-agenti.md) — de-cablaggio fatto (binomio «due agenti» ammorbidito a caso saliente nei nodi); resta solo la maturazione di `agente`, bottom-up, quando l'uso multi-agente diventa reale
