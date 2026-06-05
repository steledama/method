---
data: 2026-06-05
stato: bozza
---

# Sistema cognitivo

Unità di analisi proposta da Edwin Hutchins per studiare la cognizione dove accade davvero: non dentro la testa di un singolo individuo, ma nell'accoppiamento tra persone, artefatti e ambiente. Un sistema cognitivo è «a collection of individuals and artifacts and their relations to each other in a particular work practice». La tesi di Hutchins è che la cognizione è *distribuita* — non solo tra le persone di un gruppo, ma tra persone e strumenti, tra mente e mondo.

Cosa si distribuisce non è solo l'informazione ma anche i processi: rappresentazioni e trasformazioni si propagano attraverso agenti e artefatti in sequenza. Hutchins lo dimostra sulla navigazione navale — tracciare una rotta non è il lavoro di nessuna mente singola, ma del sistema composto da equipaggio, grafici, strumenti e procedure condivise. «Cognition is not locked inside individual minds, but unfolds in the interaction between people, tools, and context».

Norman converge sulla stessa conclusione: quando una persona usa un artefatto cognitivo, «the person and the artifact become a system in which cognition is distributed between the person and the device, creating a system with expanded and enhanced capabilities over the individual alone». L'artefatto non è un'estensione della mente — è un componente del sistema cognitivo che trasforma ciò che il sistema è capace di fare.

## Il sistema cognitivo del metodo

Nel metodo il sistema cognitivo è l'accoppiamento che prende vita a ogni sessione: artefatto (la KB, lo strato output, lo strato input) + umano + LLM + harness tecnico. È dove la cognizione del metodo accade. Non è portabile — emerge dall'uso e si scioglie quando la sessione finisce.

Questo lo distingue dall'artefatto cognitivo, che invece è portabile: il repo sopravvive al cambio di modello, al cambio di harness, al cambio di utente. Il metodo coltiva l'artefatto *perché* il sistema funzioni; ma l'artefatto e il sistema non sono la stessa cosa.

## L'asimmetria dei due agenti

Il sistema cognitivo del metodo ha un'asimmetria strutturale tra i due agenti che leggono l'artefatto. Per l'umano la KB è impalcatura esterna a un modello mentale che possiede già — un promemoria, un ancoraggio. Per l'LLM la KB *è* il modello mentale: riparte da zero a ogni sessione e non ha altra fonte. Lo user's model di Norman (cfr. `system-image`) coincide, per l'LLM, con il system image — non c'è strato intermedio.

Questa asimmetria ha conseguenze di progetto: l'artefatto deve essere autosufficiente per l'agente che non porta nulla, senza per questo essere ridondante per l'agente che porta già molto. Non è un equilibrio facile — è la tensione che motiva la distinzione L1/L2 nello strato output, e che richiede che certe cose (assunzioni, contesto, ragioni di una decisione) siano esplicite nell'artefatto anche quando l'umano le ricorderebbe.

## Tripartizione

I tre concetti — artefatto, sistema, metodo — si dividono il lavoro in modo netto:

- *artefatto cognitivo*: la rappresentazione esterna progettata e persistente; ciò che il metodo coltiva; portabile
- *sistema cognitivo*: l'accoppiamento dinamico tra artefatto, umano e LLM in una sessione; dove la cognizione accade; non portabile
- *metodo*: la pratica con cui si coltiva l'artefatto perché il sistema performi

La distinzione è operativa: dire «il metodo è portabile» significa dire «l'artefatto è portabile» — il sistema cognitivo no, perché dipende dall'agente e dall'harness disponibili in quel momento. La tesi di vendor-neutrality e di sopravvivenza al cambio di modello si regge su questa distinzione.

## Riferimenti

- Edwin Hutchins, _Cognition in the Wild_ (MIT Press, 1995) — fonte primaria sul sistema cognitivo come unità di analisi; volume non ancora disponibile in `sources/`.
- Donald Norman, «Cognitive Artifacts», in J. Carroll (ed.), _Designing Interaction_ (Cambridge University Press, 1991) — definizione dell'artefatto cognitivo e della persona-più-artefatto come sistema.
- Donald Norman, _Things That Make Us Smart_ (Addison-Wesley, 1993), Cap. 3 — cfr. `kb/artefatto-cognitivo.md` per la distillazione.

Connessioni:

- [artefatto-cognitivo](artefatto-cognitivo.md)
- [ciclo-azione](ciclo-azione.md)
- [system-image](system-image.md)
- [affordance-signifier](affordance-signifier.md)
- [knowledge-base](knowledge-base.md)
- [metodo-kb](metodo-kb.md)
