---
stato: maturo
---

# Node

Un nodo è l'unità atomica di una knowledge base basata su testo: un pezzo di conoscenza che si definisce in relazione con gli altri nodi, mai in isolamento. Il significato di un nodo emerge dalla rete di connessioni in cui partecipa, non dal suo contenuto intrinseco.

Il termine "nodo" è preferito a "nota" per tre ragioni. Prima: relazionalità — un nodo senza connessioni è incompleto, perché la sua funzione nasce dal posto che occupa nella rete. Seconda: generalizzabilità — "nodo" è un termine neutro applicabile a qualsiasi dominio (salute, finanza, configurazione sistemi, business intelligence) senza implicare un contesto specifico; lo stesso schema concettuale si trasferisce tra progetti con minima personalizzazione. Terza: interfaccia cognitiva condivisa — un LLM naviga una knowledge base di nodi esattamente come la mente umana, seguendo connessioni in una rete semantica; il termine rende esplicito questo protocollo condiviso e massimizza l'osmosi tra cognizione autonoma e cognizione aumentata dagli LLM.

Ogni nodo ha una struttura minimalista: frontmatter con lo stato di maturità, corpo in prosa pura senza link inline, sezioni opzionali (Caratteristiche, Esempi, altri label custom), sezione finale Connessioni con tutti i link deduplicate e ordinati per rilevanza. Il corpo è pensato per essere letto — la sezione Connessioni è pensata per essere navigata. L'atomicità non riguarda solo l'argomento, ma anche la funzione documentale: un nodo dovrebbe sapere se sta facendo da mappa, concetto, reference o runbook.

Template:

- frontmatter iniziale con solo lo stato
- H1 con titolo del nodo
- definizione in uno o tre paragrafi di prosa pura
- sezioni opzionali con label testuale e bullet piatti
- sezione finale Connessioni

Caratteristiche:

- atomicità: contiene una sola idea; troppi livelli annidati segnalano che va diviso in più nodi
- prosa pura nel corpo: nessun link inline; il testo è leggibile senza interruzioni sintattiche
- interfaccia esplicita: la sezione Connessioni è l'unico punto di uscita verso la rete
- frontmatter minimalista obbligatorio: solo stato (`bozza`, `iniziale`, `maturo`); le date — creazione e modifica — vivono in git, non nel frontmatter
- nome file inglese, tutto minuscolo con trattini, singolare come forma canonica
- prosa italiana per i concetti del dominio
- H1 inglese obbligatorio, coerente con il filename e leggibile anche fuori da esso
- sezioni non gerarchiche: preferire label testuali e bullet di primo livello a heading annidati
- stato bozza: nodo utile ma incompleto, da espandere o collegare meglio
- stato maturo: nodo stabile, collegato e sufficientemente autonomo
- niente storico operativo: task, checklist temporanee e piani di lavoro vivono in `o2/`
- presente permanente: la KB stabile descrive lo stato corrente; la storia resta in git e nei fili `i3/`
- funzione documentale esplicita: separare quando mappa, concetto, reference e runbook iniziano a convivere nello stesso file
- esempi vivi: privilegiare pattern realmente incarnati nel dominio rispetto a esempi didattici plausibili ma non canonici

## Frontmatter dei nodi

```yaml
---
stato: bozza | iniziale | maturo
---
```

Il frontmatter dei nodi è obbligatorio e volutamente minimale: un solo campo, `stato`. Serve agli strumenti per distinguere presenza e maturità del nodo senza trasformare la KB in un database manuale.

`stato` è l'unico campo che guadagna l'obbligo perché è un **giudizio non ricostruibile** da nessun'altra fonte. Le **date** — creazione e modifica — appartengono a git e non stanno nel frontmatter: una data registrata a mano sarebbe una seconda storia fragile e non verificabile (lo strumento ne controllerebbe la presenza, mai il valore), e derivabile dalla storia è comunque ridondante.

`stato` indica la maturità del nodo:

- `bozza`: nodo utile ma incompleto, ancora da espandere o collegare;
- `iniziale`: nodo appena impostato o ancora poco stabilizzato;
- `maturo`: nodo stabile, autonomo e sufficientemente collegato.

Non aggiungere campi come `updated`, `tags`, `owner`, `priority` o `depends_on` salvo decisione metodologica esplicita. Le relazioni vivono nei link, la storia in git, i task in `o2/`, priorità e dipendenze in `o1/plan.md`.

Il divieto colpisce ciò che è relazione, storia, lavoro o priorità travestito da metadato — non un **attributo intrinseco del nodo**. Per quest'ultimo il metodo sanziona un meccanismo di estensione: un adottante può dichiarare una proprietà di dominio oltre `{data, stato}` solo se soddisfa **tutti e quattro** i requisiti di demarcazione. È **intrinseca**: descrive il nodo in sé, non una relazione verso altri nodi (quella è un link), non storia (git), non lavoro (`o2/`), non priorità (`o1/plan.md`). È a **valori chiusi e singola**: classificazione faceted, un insieme finito e dichiarato di valori con uno solo per nodo — un attributo aperto o multi-valore è una relazione e va espresso come link, non come campo. È **non derivabile**: non ricostruibile da una fonte di verità esistente, per non aprire una seconda storia fragile. È **dichiarata e verificabile**: l'insieme dei valori ammessi è dichiarato e `kb_tools` ne verifica presenza e dominio, come già fa per `stato`.

La proprietà estesa è **locale all'adottante** — vive nella sua `kb/` e non nel canone, salvo che emerga come generalizzazione portabile: ciò che il metodo sanziona è il meccanismo, non la singola proprietà. Esempio: `nixos` marca ogni nodo con `mondo: lavoro | casa | trasversale`, attributo intrinseco a valori chiusi che rende meccanico un futuro split dei repository.

Il frontmatter appartiene ai nodi, ai task operativi e agli item delle collezioni-stadio, non a bussola, regole, register o indici ordinari. `README.md`, `CLAUDE.md`, `AGENTS.md`, `goal.md`, `world.md`, `kb/kb.md`, `i3/verdicts.md` e file locali come `stato.md`, `scadenze.md` o `diario.md` non devono avere frontmatter. `o1/plan.md` è l'eccezione: è insieme indice dello stadio o1 e istanza corrente del Plan, quindi dichiara `ciclo:`.

Regole di creazione:

- creare un nodo quando un concetto è stabile e riusabile
- aggiornare un nodo esistente quando la nuova informazione rafforza un concetto già presente
- dividere un nodo quando contiene due idee che possono essere interrogate separatamente
- dividere un nodo quando lettori o responsabilità diverse richiedono percorsi diversi
- dividere un nodo quando due flussi operativi possono divergere nel tempo anche se oggi condividono contesto
- evitare nodi enciclopedici se il progetto è personale e operativo
- creare un nodo nuovo solo quando migliora accessibilità o stabilità semantica, non solo perché un concetto è nominabile
- scegliere il nome più generale e singolare possibile
- usare termini del dominio locale, non gergo tecnico del metodo, salvo nodi metodologici

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [zettelkasten](zettelkasten.md)
- [knowledge-base](knowledge-base.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [connection](connection.md)
