---
stato: bozza
---

# Development meta-cycle

Il runtime cycle usa l'artefatto per agire sul dominio reale. Il development
meta-cycle usa la stessa geometria a sei atti per modificare l'artefatto stesso:
edit e commit sono azioni; test, audit e drift sono segnali; il Goal di sviluppo
descrive la forma desiderata della macchina.

I due movimenti non sono cicli paralleli. La cucitura è questa: **il Mondo del
meta-ciclo è l'artefatto che diventa la macchina del runtime**. Il runtime resta
lo scopo; lo sviluppo lo rende più adatto, ispezionabile e correggibile. È il
bootstrap di Engelbart applicato al repository.

Ne derivano quattro poli distinti: Goal e Mondo del dominio, Goal di sviluppo e
artefatto/Mondo-dev. Il gradiente di portabilità cresce avvicinandosi al
Goal-dev e diminuisce verso il Mondo specifico del dominio.

La distinzione runtime/dev non coincide con umano/LLM. Entrambi gli agenti
possono attraversare entrambi i cicli; cambia il grado di autonomia consentito,
non la geometria. I prodotti intermedi restano punti di controllo condivisi.

Ogni adottante possiede entrambi i movimenti. `action-cycle-matrix` consente di
verificare sul campo dove siano solidi, deboli, assenti o forzati.

Connessioni:

- [action-cycle](action-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [development-goal](development-goal.md)
- [augmentation-system](augmentation-system.md)
- [world](world.md)
- [goal](goal.md)
