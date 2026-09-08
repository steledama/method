---
stato: maturo
---

# Cognitive fidelity

La fedeltà cognitiva è la capacità della KB di rappresentare il progetto reale
in una forma che umano e agente possano ricostruire. Una rete può avere link e
frontmatter perfetti ma restare infedele perché conserva storia superata, esempi
morti o punti di ingresso fuorvianti.

La verifica ha tre livelli:

- **strutturale**: la rete è integra? Link, catalogo, orfani e formato sono
  verificabili con `kb-tools`;
- **fattuale**: i fatti ad alta deriva concordano con fonti primarie leggibili?
  Codice, filesystem, dati strutturati e documenti autoritativi dipendono dal
  dominio;
- **semantico**: la KB è ancora una buona interfaccia cognitiva? Questo richiede
  giudizio.

La revisione semantica pone poche domande:

- README, CLAUDE, catalogo e nodi hanno funzioni distinte e punti di ingresso
  coerenti con gli intenti reali?
- ogni nodo ha una funzione dominante, descrive il presente e giustifica il
  proprio peso?
- storia, workaround e lavoro aperto sono rimasti fuori dalla conoscenza
  permanente?
- decisioni importanti registrano l'assunzione che ne imporrebbe la revisione?
- esempi, entità e confini descritti esistono ancora nel dominio?
- nuove distinzioni operative richiedono di dividere un nodo, oppure la
  separazione aggiungerebbe solo lessico?

I controlli fattuali partono da una fonte primaria e da un'affermazione il cui
costo d'errore, incertezza o volatilità giustifica la verifica. Anche un fatto
stabile può richiederla se regge una distinzione fondamentale. Una sintesi non
si verifica contro una sua copia narrativa; un contratto, un atto o una
decisione documentata possono invece essere fonti primarie. Va esplicitato chi
ha autorità sul fatto e quale evidenza è indipendente dalla sintesi. Se manca
una fonte, si dichiara il limite senza promuovere il consenso fra testi a prova.

Il limite è intenzionale. Gli script intercettano regressioni note e indirizzano
l'attenzione; non simulano oggettività dove la fonte è interpretativa. L'esito
utile della review non è un punteggio, ma un giudizio motivato su cosa
aggiornare, fondere, dividere o eliminare.

Connessioni:

- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [kb-tools](kb-tools.md)
- [source-of-truth](source-of-truth.md)
- [action-cycle](action-cycle.md)
