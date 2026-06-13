---
data: 2026-05-23
stato: bozza
---

# Git history

La git history è la storia verificabile dei cambiamenti. Risponde alla domanda: che cosa è cambiato davvero? Conserva diff, commit, autori, date e messaggi, rendendo ricostruibile l'evoluzione del progetto senza trasformare la KB in archivio storico.

Nel metodo la git history sostiene la leggerezza della documentazione. I nodi descrivono il presente permanente; verdict.md interpreta le decisioni significative; git conserva il dettaglio analitico di ogni modifica. Quando serve sapere esattamente cosa è cambiato, si torna al commit.

Regole:

- è la fonte di verità per il cosa è cambiato
- non sostituisce verdict.md come memoria del perché
- permette di rimuovere task completati senza perdere storia
- rende ricostruibili audit e report su commit passati
- sostiene commit piccoli, leggibili e tematici
- non va usata come discarica per decisioni non documentate

## Applicazione nei progetti adottanti

Tutti i progetti usano git come memoria analitica dei cambiamenti e `verdict.md` come memoria interpretativa. La differenza è nel peso della storia: `nixos` e `bi` hanno commit frequenti legati a codice e documentazione; `economia` alterna aggiornamenti di dati, nodi e pratiche; `salute` conserva una storia più legata a ingest, rinomine e maturazione metodologica.

Il confronto conferma la regola del metodo: i task completati possono sparire da `tasks/` perché git conserva il dettaglio, ma le decisioni che cambiano il modo di lavorare devono essere registrate in `verdict.md` o nei nodi. La sola git history non basta a ricostruire il perché.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [verdict](verdict.md)
- [plan](plan.md)
- [kb-tools](kb-tools.md)
- [design-principles](design-principles.md)
- [adopter-comparison](adopter-comparison.md)
