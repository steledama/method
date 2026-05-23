---
data: 2026-05-23
stato: bozza
---

# Git history

La git history è la storia verificabile dei cambiamenti. Risponde alla domanda: che cosa è cambiato davvero? Conserva diff, commit, autori, date e messaggi, rendendo ricostruibile l'evoluzione del progetto senza trasformare la KB in archivio storico.

Nel metodo KB la git history sostiene la leggerezza della documentazione. I nodi descrivono il presente permanente; log.md interpreta le decisioni significative; git conserva il dettaglio analitico di ogni modifica. Quando serve sapere esattamente cosa è cambiato, si torna al commit.

Regole:

- è la fonte di verità per il cosa è cambiato
- non sostituisce log.md come memoria del perché
- permette di rimuovere task completati senza perdere storia
- rende ricostruibili audit e report su commit passati
- sostiene commit piccoli, leggibili e tematici
- non va usata come discarica per decisioni non documentate

Connessioni:

- [metodo-kb](metodo-kb.md)
- [log](log.md)
- [task-aperti](task-aperti.md)
- [strumenti-kb](strumenti-kb.md)
- [design-principles](design-principles.md)
