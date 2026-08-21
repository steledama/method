---
stato: bozza
---

# Action cycle

Il metodo adatta il ciclo d'azione di Donald Norman all'agente umano+LLM che opera attraverso un artefatto versionato. Tra i poli Goal e Mondo corrono sei atti:

1. **Plan (o1)** — scegliere la direzione;
2. **Specify (o2)** — rendere concrete azioni e vincoli;
3. **Perform (o3)** — predisporre ed eseguire l'atto;
4. **Perceive (i1)** — catturare il segnale;
5. **Interpret (i2)** — attribuirgli significato;
6. **Compare (i3)** — giudicarlo rispetto al Goal.

Goal e Mondo sono stati ai bordi, non operazioni. I sei atti formano due archi: `output` scende dal Goal al Mondo come feedforward; `input` risale come feedback. L'artefatto conserva i prodotti intermedi affinché l'LLM possa riprendere il lavoro e l'umano possa ispezionarlo.

Le coppie speculari sono ordinate per distanza dai poli: o1↔i3 vicino al Goal, o2↔i2 al centro, o3↔i1 alla membrana del Mondo. I numeri non si accoppiano perché i due archi procedono in versi opposti.

Il modello riduce due distanze cognitive. Il _gulf of execution_ separa l'intenzione dalla possibilità di agire; plan, specifica e prescrizione lo attraversano. Il _gulf of evaluation_ separa l'esito dal suo significato; percezione, interpretazione e confronto lo attraversano. Saltare uno stadio può essere legittimo quando non serve un artefatto persistente, ma diventa un guasto quando elimina un punto di controllo o un'informazione necessaria alla sessione successiva.

La qualità di ogni prodotto si giudica chiedendo se fornisce l'informazione necessaria al proprio atto. Per le superfici di decisione valgono in particolare visibilità, feedback, mapping e constraint.

Lo stesso schema opera nel dominio reale e nello sviluppo dell'artefatto. Il rapporto tra ciclo runtime e meta-ciclo vive in `development-meta-cycle`; la sua verifica empirica in `action-cycle-matrix`.

Connessioni:

- [goal](goal.md)
- [world](world.md)
- [input](input.md)
- [output](output.md)
- [processing-layers](processing-layers.md)
- [development-meta-cycle](development-meta-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [system-image](system-image.md)
