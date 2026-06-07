# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, prioritizzati, con le loro
dipendenze. Sta in root — letto a ogni sessione — perché la sua altezza nel ciclo
vince sulla pace: è una vista veloce, ma è la prima a orientare il lavoro. I
dettagli operativi di ciascun task vivono in `tasks/`; qui sta solo la supervisione.

Regola: ogni file in `tasks/` ha una riga qui; ogni riga sostanziale ha un file.
Quando un task è completato la riga sparisce — lo storico resta in git, `why.md` e
nei nodi aggiornati.

## Task aperti

- [rename-metodo-method](tasks/rename-metodo-method.md) — rinominare repository, directory locale, symlink e path trans-repo da `metodo` a `method`
- [method-review](tasks/method-review.md) — progettare e pilotare la skill locale che verifica il drift degli adottanti rispetto ai commit di `metodo` — _dipende da_ rename `metodo` → `method`
- [fonti-pace-layering](tasks/fonti-pace-layering.md) — verifica delle fonti (Duffy, Brand) e maturazione del nodo `pace-layering` da bozza a maturo
- [fonti-mente-estesa](tasks/fonti-mente-estesa.md) — ingest delle fonti di Andy Clark (mente estesa) e vaglio del filone come pavimento del metodo; disciplina i1→i2→i3, niente nodo dal sentito dire
