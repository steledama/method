---
stato: bozza
---

# Specify (o2)

Lo stadio o2 del ciclo d'azione: la vista di decisione per l'umano, lo stadio Specify di Norman sul lato esecuzione. Traduce la conoscenza in una superficie che permette di scegliere cosa fare ora. È la lettura speculare della superficie i2 (`interpret`): la stessa collezione `i2/` è o2 quando la si produce come vista di decisione (feedforward, scende) e substrato i2 quando la si legge per attribuire significato (feedback, risale).

## La forma dell'o2 segue la domanda

L'o2 non è una sola forma. Karpathy: la forma della risposta segue la domanda — pagina markdown, tabella di confronto, deck di slide, grafico, canvas (cfr. `karpathy-pattern`). Il deck è la forma-default per la sintesi che si scorre, ma per un'altra domanda l'o2 giusto può essere una tabella o un grafico. Lo strumento del deck resta uniforme tra i repo (cfr. `deck`); il repertorio delle forme no: si sceglie per funzione, non per uniformità.

## o2 e o1 sono due altitudini

o1 (macchina) e o2 (decisione) non sono lo stesso stadio rivolto a due agenti: sono due _altitudini_ dell'arco di output (cfr. `output`). o1 è il livello-macchina vicino alla KB, o2 la vista di decisione per l'umano. L'agente che li consuma (LLM/umano) è una dimensione ortogonale all'altitudine (cfr. `action-cycle`). Un JSON denso è inutile per la decisione umana, un'infografica colorata è inefficiente per l'LLM.

## Le quattro proprietà cardine come criteri di qualità

Norman riassume il buon design in quattro proprietà, che diventano criteri diretti di valutazione per o2:

- **visibilità** — tutti gli stati attivi sono percepibili a colpo d'occhio, niente di rilevante è nascosto;
- **feedback** — dopo ogni evento l'esito è evidente, senza bisogno di indagine;
- **mapping** — la disposizione visiva corrisponde alla struttura reale del dominio, non a un ordine convenzionale;
- **constraint** — la struttura impedisce di dimenticare le parti che servono insieme (es. raccomandazioni accanto allo stato).

Perché l'o2 muova davvero l'azione deve raggiungere anche il registro viscerale, non solo quello riflessivo: un o2 solo riflessivo parla alla parte che già sa e non muove la parte che fa (cfr. `processing-layers`).

Connessioni:

- [action-cycle](action-cycle.md)
- [output](output.md)
- [interpret](interpret.md)
- [perform](perform.md)
- [view](view.md)
- [karpathy-pattern](karpathy-pattern.md)
- [affordance-signifier](affordance-signifier.md)
- [constraint](constraint.md)
- [processing-layers](processing-layers.md)
