---
stato: maturo
---

# Node

Un nodo è l'unità atomica di una knowledge base basata su testo: conoscenza con
una responsabilità autonoma, resa più comprensibile e utilizzabile dalle
connessioni. Il corpo deve potersi leggere da solo; la rete ne esplicita
contesto, dipendenze e possibili percorsi.

Il termine "nodo" sottolinea questa relazionalità ed è applicabile a domini
diversi. Umani e agenti possono usare gli stessi collegamenti per orientarsi: è
un'interfaccia condivisa, senza assumere che i loro processi cognitivi siano
identici.

Ogni nodo ha una struttura minimalista: frontmatter con lo stato di maturità,
corpo in prosa pura senza link inline, sezioni opzionali (Caratteristiche,
Esempi, altri label custom), sezione finale Connessioni con tutti i link
deduplicati e ordinati per rilevanza. Il corpo è pensato per essere letto — la
sezione Connessioni è pensata per essere navigata. L'atomicità non riguarda solo
l'argomento, ma anche la funzione documentale: un nodo dovrebbe sapere se sta
facendo da mappa, concetto, reference o runbook.

Template:

- frontmatter iniziale con `stato`, salvo estensioni di dominio dichiarate
- H1 con titolo del nodo
- definizione in uno o tre paragrafi di prosa pura
- sezioni opzionali con label testuale e bullet piatti
- `## Riferimenti` prima delle Connessioni, quando il nodo distilla una fonte
  primaria: nome canonico unico, per non moltiplicare le forme della stessa
  funzione
- sezione finale Connessioni

Caratteristiche:

- atomicità: contiene una sola idea; troppi livelli annidati segnalano che va
  diviso in più nodi
- prosa pura nel corpo: nessun link inline; il testo è leggibile senza
  interruzioni sintattiche
- interfaccia esplicita: la sezione Connessioni è l'unico punto di uscita verso
  la rete
- frontmatter minimo obbligatorio: `stato` (`bozza`, `iniziale`, `maturo`), con
  il meccanismo di estensione descritto sotto; le date vivono in Git
- nome file inglese, tutto minuscolo con trattini, singolare come forma canonica
- prosa italiana per i concetti del dominio
- H1 inglese obbligatorio, coerente con il filename e leggibile anche fuori da
  esso
- sezioni non gerarchiche: preferire label testuali e bullet di primo livello a
  heading annidati
- stato bozza: nodo utile ma incompleto, da espandere o collegare meglio
- stato maturo: nodo stabile, collegato e sufficientemente autonomo
- niente storico operativo: task, checklist temporanee e piani di lavoro vivono
  in `o2/`
- presente permanente: la KB descrive la conoscenza corrente; Git conserva la
  storia, `i3/` i giudizi sulle tensioni ancora aperte
- funzione documentale esplicita: separare quando mappa, concetto, reference e
  runbook iniziano a convivere nello stesso file
- esempi vivi: privilegiare pattern realmente incarnati nel dominio rispetto a
  esempi didattici plausibili ma non canonici
- esempi portabili: illustrare con la configurazione ricorrente, non con
  l'inventario di chi la incarna oggi; un elenco per-adottante dentro un nodo è
  una seconda rappresentazione del register che deriva in silenzio
- righe a capo entro ~80 colonne nel corpo: il testo si legge e si diffa per
  righe, e un paragrafo su riga unica rende illeggibile ogni modifica successiva

## Frontmatter dei nodi

```yaml
---
stato: bozza | iniziale | maturo
---
```

Il frontmatter base dei nodi è obbligatorio e minimale: il campo `stato`. Serve
agli strumenti per distinguere presenza e maturità del nodo senza trasformare la
KB in un database manuale.

`stato` è l'unico campo che guadagna l'obbligo perché è un **giudizio non
ricostruibile** da nessun'altra fonte. Le **date** — creazione e modifica —
appartengono a git e non stanno nel frontmatter: una data registrata a mano
sarebbe una seconda storia fragile e non verificabile (lo strumento ne
controllerebbe la presenza, mai il valore), e derivabile dalla storia è comunque
ridondante.

`stato` indica la maturità del nodo:

- `bozza`: nodo utile ma incompleto, ancora da espandere o collegare;
- `iniziale`: nodo appena impostato o ancora poco stabilizzato;
- `maturo`: nodo stabile, autonomo e sufficientemente collegato.

Non aggiungere campi come `updated`, `tags`, `owner`, `priority` o `depends_on`
salvo decisione metodologica esplicita. Le relazioni vivono nei link, la storia
in git, i task in `o2/`, priorità e dipendenze in `o1/plan.md`.

Il divieto colpisce ciò che è relazione, storia, lavoro o priorità travestito da
metadato — non un **attributo intrinseco del nodo**. Per quest'ultimo il metodo
sanziona un meccanismo di estensione: un adottante può dichiarare una proprietà
di dominio oltre `stato` solo se soddisfa **tutti e quattro** i requisiti di
demarcazione. È **intrinseca**: descrive il nodo in sé, non una relazione verso
altri nodi (quella è un link), non storia (git), non lavoro (`o2/`), non
priorità (`o1/plan.md`). È a **valori chiusi e singola**: classificazione
faceted, un insieme finito e dichiarato di valori con uno solo per nodo — un
attributo aperto o multi-valore è una relazione e va espresso come link, non
come campo. È **non derivabile**: non ricostruibile da una fonte di verità
esistente, per non aprire una seconda storia fragile. È **dichiarata e
verificabile**: l'insieme dei valori ammessi è dichiarato e `kb_tools` ne
verifica presenza e dominio, come già fa per `stato`.

La proprietà estesa è **locale all'adottante** — vive nella sua `kb/` e non nel
canone, salvo che emerga come generalizzazione portabile: ciò che il metodo
sanziona è il meccanismo, non la singola proprietà. Un esempio è la facet
`mondo: lavoro | casa | trasversale`, usata per distinguere ambiti di una KB di
configurazione. Valori e copertura effettivi si verificano nel fork che la
dichiara, senza mantenerne qui una fotografia corrente.

Il frontmatter appartiene ai nodi, ai task operativi e agli item delle
collezioni-stadio, non a bussola, regole, register o indici ordinari.
`README.md`, `CLAUDE.md`, `AGENTS.md`, `goal.md`, `world.md`, `kb/kb.md`,
`i3/verdicts.md` e file locali come `stato.md` o `diario.md` non devono avere
frontmatter. `o1/plan.md` è l'eccezione: è insieme indice dello stadio o1 e
istanza corrente del Plan, quindi dichiara `ciclo:`.

Regole di creazione:

- creare un nodo quando un concetto è stabile e riusabile
- aggiornare un nodo esistente quando la nuova informazione rafforza un concetto
  già presente
- dividere un nodo quando contiene due idee che possono essere interrogate
  separatamente
- dividere un nodo quando lettori o responsabilità diverse richiedono percorsi
  diversi
- dividere un nodo quando due flussi operativi possono divergere nel tempo anche
  se oggi condividono contesto
- evitare nodi enciclopedici se il progetto è personale e operativo
- creare un nodo nuovo solo quando migliora accessibilità o stabilità semantica,
  non solo perché un concetto è nominabile
- scegliere il nome più generale e singolare possibile
- usare termini del dominio locale, non gergo tecnico del metodo, salvo nodi
  metodologici

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [zettelkasten](zettelkasten.md)
- [knowledge-base](knowledge-base.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [connection](connection.md)
