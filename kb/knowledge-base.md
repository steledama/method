---
stato: maturo
---

# Knowledge base

La knowledge base è la memoria stabile e cumulativa del progetto. Non conserva
materiale grezzo né si limita a recuperarlo: integra conoscenza già interpretata
in nodi collegati, aggiornando ciò che una nuova fonte conferma, corregge o
contraddice. Ciò che vi entra non dovrebbe essere ricostruito a ogni sessione.

Per un agente la KB è anche un'interfaccia cognitiva. Catalogo, punti di
ingresso, fonti di verità riconoscibili e nodi con una funzione dominante
rendono il dominio ricostruibile senza leggere tutto. La validità dei link non
basta: la rete deve restare aderente al progetto reale (`cognitive-fidelity`).

La KB orienta il ciclo ma non lo sostituisce. Non contiene task aperti, segnali
grezzi o prescrizioni: conserva concetti, decisioni e conoscenza che devono
sopravvivere al singolo giro. Le collezioni `i*` e `o*` trattano invece il
lavoro in transito; README orienta, CLAUDE istruisce l'agente, Git conserva la
storia.

La manutenzione divide responsabilità diverse. L'umano resta autore e decide
cosa è vero o rilevante; l'LLM integra, collega e segnala incoerenze; gli script
versionati eseguono i controlli ripetitivi (`kb-tools`). Questa separazione
permette alla rete di crescere senza trasformare giudizi interpretativi in
automatismi fittizi.

Il formato è Markdown portabile. Un nucleo metodologico può essere adottato da
più repository, ma ogni progetto mantiene autonomamente i propri nodi di
dominio, le fonti e le estensioni locali.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [node](node.md)
- [kb-tools](kb-tools.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [project-structure](project-structure.md)
- [system-image](system-image.md)
- [kb-content-typology](kb-content-typology.md)
