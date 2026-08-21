---
stato: maturo
---

# Cognitive fidelity

La fedeltà cognitiva è la capacità della KB di rappresentare il progetto reale
in una forma che umano e agente possano ricostruire. Una rete può avere link e
frontmatter perfetti ma restare infedele perché conserva storia superata,
esempi morti o punti di ingresso fuorvianti.

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

I controlli fattuali vanno attivati solo dopo aver identificato una fonte
primaria e un fatto utile che cambia abbastanza spesso da meritare il costo. La
documentazione non valida altra documentazione: se un fatto è disponibile solo
come testo mantenuto a mano, manca una fonte verificabile.

Il limite è intenzionale. Gli script intercettano regressioni note e indirizzano
l'attenzione; non simulano oggettività dove la fonte è interpretativa. L'esito
utile della review non è un punteggio, ma un giudizio motivato su cosa aggiornare,
fondere, dividere o eliminare.

Connessioni:

- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [kb-tools](kb-tools.md)
- [source-of-truth](source-of-truth.md)
- [action-cycle](action-cycle.md)
