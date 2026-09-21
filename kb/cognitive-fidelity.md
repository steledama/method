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
- cronaca redazionale superata e lavoro aperto sono distinti dalla storia del
  dominio e dalle lezioni ancora necessarie?
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
conservare, arricchire, aggiornare, fondere, dividere o eliminare.

La copertura ha tre significati distinti: quali nodi sono stati letti, quali
affermazioni sono state riscontrate e quali domande reali trovano una risposta
utilizzabile. Una lettura integrale non certifica tutti i fatti; la disposizione
editoriale di un nodo non sostituisce il giudizio sulle sue affermazioni.
Quando manca una fonte decisiva, quel giudizio resta sospeso. Per ogni metrica
quantitativa contano corpus, denominatore ed esclusioni: la copertura del codice
non misura la copertura delle fonti o dei bisogni conoscitivi.

Il riferimento dell'utilità viene dal Goal e dall'uso. Una prova di accesso
parte da una domanda del dominio e segue ingresso, nodo, fonte e limite fino
alla decisione che la conoscenza può informare. Può rivelare un nodo mancante,
ma anche un router debole, una fonte inaccessibile o conoscenza già presente
altrove. La lacuna non impone una nuova voce nel catalogo.

Fatti, ipotesi, interpretazioni, norme e attribuzioni non hanno la stessa
autorità. Prima di dichiarare contraddittorie due affermazioni si confrontano
oggetto, tempo, condizioni e significato; osservazioni discordanti possono
essere entrambe da conservare. Git custodisce la storia dei documenti, ma non
sostituisce una ricostruzione clinica, documentale o causale ancora necessaria.

L'output macchina è rigenerabile; il razionale di un giudizio semantico non lo
è nello stesso senso. Non serve archiviare ogni report: serve conservare la
conoscenza, la sintesi o il verdetto che cambia nella superficie pertinente.

Connessioni:

- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [kb-tools](kb-tools.md)
- [source-of-truth](source-of-truth.md)
- [action-cycle](action-cycle.md)
