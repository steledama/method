---
stato: bozza
---

# Agent

L'agente è l'attore che agisce nell'artefatto cognitivo e con esso: chi legge la
knowledge base, la interroga, la modifica e la usa per agire sul mondo. È
distinto dal file AGENTS.md, che è solo il punto di ingresso operativo verso le
istruzioni: quello indirizza gli agenti, questo nodo descrive chi sono e quanti
livelli possono avere.

Il caso umano/LLM presenta un'asimmetria: l'umano integra l'artefatto con
esperienza e memoria personale; l'LLM ricostruisce il contesto di progetto
soprattutto dall'artefatto persistente, insieme a richiesta corrente, strumenti
e segnali del Mondo. La KB ne è il nucleo formalizzato, non il modello intero.

Il binomio è un caso particolare di una popolazione di agenti. Le macchine
possono differire per capacità, costo, località e fiducia; un agente che
pianifica e uno che esegue possono aver bisogno di superfici diverse anche
quando leggono la stessa KB. Questa articolazione è una proposta del metodo, da
stabilizzare nell'uso.

Riconoscere la popolazione di agenti invece del binomio ha una conseguenza sul
metodo: la divisione del lavoro non passa solo tra umano e LLM, ma tra livelli
di agente per capacità, per stadio del ciclo dell'azione e per fiducia nel
trattamento dei dati. Lo stadio di specifica — i dettagli operativi che vivono
in `o2/` — diventa allora anche l'interfaccia con cui un agente alto prepara il
lavoro per un agente esecutore. Il nodo resta in bozza perché una gerarchia
operativa va stabilizzata quando emerge dall'uso reale.

Questo nodo descrive attori, livelli e divisione del lavoro. L'effetto del loro
accoppiamento sulla cognizione della sessione e l'asimmetria fra modello umano e
modello ricostruito dall'LLM appartengono invece a `cognitive-system`.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [claude](claude.md)
- [affordance-signifier](affordance-signifier.md)
- [system-image](system-image.md)
- [cognitive-system](cognitive-system.md)
- [knowledge-base](knowledge-base.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
- [consent](consent.md)
