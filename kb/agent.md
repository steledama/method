---
data: 2026-06-06
stato: bozza
---

# Agent

L'agente è l'attore che agisce nell'artefatto cognitivo e con esso: chi legge la knowledge base, la interroga, la modifica e la usa per agire sul mondo. È distinto dal file AGENTS.md, che è solo il punto di ingresso operativo verso le istruzioni: quello indirizza gli agenti, questo nodo descrive chi sono e quanti livelli possono avere.

Il metodo è nato descrivendo due agenti — l'umano e un singolo LLM — e su quel binomio ha costruito la sua asimmetria: per l'umano la KB è la vista di un modello che già possiede, per l'LLM è il modello mentale intero, ricostruito a ogni sessione. Il binomio è un caso particolare, non la struttura. Norman definisce l'agente come «person, animal, or machine»: la categoria macchina non è un punto ma un gradiente, perché gli agenti-macchina differiscono per capacità, costo, località e fiducia. Un LLM di frontiera che pianifica ad alto livello e un agente locale più semplice che esegue non sono lo stesso lettore, anche quando leggono la stessa KB.

Riconoscere la popolazione di agenti invece del binomio ha una conseguenza sul metodo: la divisione del lavoro non passa solo tra umano e LLM, ma tra livelli di agente per capacità, per stadio del ciclo dell'azione e per fiducia nel trattamento dei dati. Lo stadio di specifica — i dettagli operativi che vivono in tasks/ — diventa allora anche l'interfaccia con cui un agente alto prepara il lavoro per un agente basso. Questo nodo resta in bozza di proposito: apre la stanza senza fissarne gli arredi, perché la struttura multi-agente va stabilizzata quando emerge dall'uso reale, non anticipata.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [agents](agents.md)
- [affordance-signifier](affordance-signifier.md)
- [system-image](system-image.md)
- [cognitive-system](cognitive-system.md)
- [knowledge-base](knowledge-base.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
- [consent](consent.md)
