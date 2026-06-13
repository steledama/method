---
data: 2026-05-09
stato: maturo
---

# Nodo

Un nodo è l'unità atomica di una knowledge base basata su testo: un pezzo di conoscenza che si definisce in relazione con gli altri nodi, mai in isolamento. Il significato di un nodo emerge dalla rete di connessioni in cui partecipa, non dal suo contenuto intrinseco.

Il termine "nodo" è preferito a "nota" per tre ragioni. Prima: relazionalità — un nodo senza connessioni è incompleto, perché la sua funzione nasce dal posto che occupa nella rete. Seconda: generalizzabilità — "nodo" è un termine neutro applicabile a qualsiasi dominio (salute, finanza, configurazione sistemi, business intelligence) senza implicare un contesto specifico; lo stesso schema concettuale si trasferisce tra progetti con minima personalizzazione. Terza: interfaccia cognitiva condivisa — un LLM naviga una knowledge base di nodi esattamente come la mente umana, seguendo connessioni in una rete semantica; il termine rende esplicito questo protocollo condiviso e massimizza l'osmosi tra cognizione autonoma e cognizione aumentata dagli LLM.

Ogni nodo ha una struttura minimalista: frontmatter con data di creazione e stato di maturità, corpo in prosa pura senza link inline, sezioni opzionali (Caratteristiche, Esempi, altri label custom), sezione finale Connessioni con tutti i link deduplicate e ordinati per rilevanza. Il corpo è pensato per essere letto — la sezione Connessioni è pensata per essere navigata. L'atomicità non riguarda solo l'argomento, ma anche la funzione documentale: un nodo dovrebbe sapere se sta facendo da mappa, concetto, reference o runbook.

Template:

- frontmatter iniziale con solo data e stato
- H1 con titolo del nodo
- definizione in uno o tre paragrafi di prosa pura
- sezioni opzionali con label testuale e bullet piatti
- sezione finale Connessioni

Caratteristiche:

- atomicità: contiene una sola idea; troppi livelli annidati segnalano che va diviso in più nodi
- prosa pura nel corpo: nessun link inline; il testo è leggibile senza interruzioni sintattiche
- interfaccia esplicita: la sezione Connessioni è l'unico punto di uscita verso la rete
- frontmatter minimalista obbligatorio: solo data (creazione, non ultima modifica) e stato (`bozza`, `iniziale`, `maturo`)
- nome file tutto minuscolo con trattini, singolare come forma canonica
- lingua italiana per i concetti del dominio
- H1 obbligatorio: il titolo deve essere leggibile anche fuori dal filename
- sezioni non gerarchiche: preferire label testuali e bullet di primo livello a heading annidati
- stato bozza: nodo utile ma incompleto, da espandere o collegare meglio
- stato maturo: nodo stabile, collegato e sufficientemente autonomo
- niente storico operativo: task, checklist temporanee e piani di lavoro vivono in tasks/
- presente permanente: la KB stabile descrive lo stato corrente; la storia resta in git e verdict.md
- funzione documentale esplicita: separare quando mappa, concetto, reference e runbook iniziano a convivere nello stesso file
- esempi vivi: privilegiare pattern realmente incarnati nel dominio rispetto a esempi didattici plausibili ma non canonici

## Frontmatter dei nodi

```yaml
---
data: YYYY-MM-DD
stato: bozza | iniziale | maturo
---
```

Il frontmatter dei nodi è obbligatorio e volutamente minimale. Serve agli strumenti per distinguere presenza, maturità e stato editoriale del nodo senza trasformare la KB in un database manuale.

`data` è la data di creazione del nodo. Non è la data di ultima modifica: quella appartiene a git. Aggiornare manualmente una data di modifica nel frontmatter creerebbe una seconda storia fragile e incompleta.

`stato` indica la maturità del nodo:

- `bozza`: nodo utile ma incompleto, ancora da espandere o collegare;
- `iniziale`: nodo appena impostato o ancora poco stabilizzato;
- `maturo`: nodo stabile, autonomo e sufficientemente collegato.

Non aggiungere campi come `updated`, `tags`, `owner`, `priority` o `depends_on` salvo decisione metodologica esplicita. Le relazioni vivono nei link, la storia in git, i task in `tasks/`, priorità e dipendenze in `plan.md`.

Il frontmatter appartiene ai nodi e ai task operativi, non ai file root. `README.md`, `CLAUDE.md`, `AGENTS.md`, `map.md`, `plan.md`, `verdict.md` e file locali come `stato.md`, `scadenze.md` o `diario.md` non devono avere frontmatter.

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

- [metodo-kb](metodo-kb.md)
- [zettelkasten](zettelkasten.md)
- [knowledge-base](knowledge-base.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [connessione](connessione.md)
