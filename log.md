# log.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta.

---

## 2026-05-24 — Creazione di `ponte` e `ciclo-azione`: tre giganti riconosciuti

Promossi al meta i due nodi previsti dal task `ponte-teoria-pratica`. `ponte.md` formalizza lo strato output del metodo: i tre livelli L1 macchina, L2 decisione umana, L3 azione nel mondo; la risoluzione del conflitto Zettelkasten/Karpathy (la sintesi vive nello strato output, non nei nodi); il ciclo che si chiude attraverso l'azione; lo stato dei quattro progetti adottanti.

`ciclo-azione.md` distilla il modello del ciclo di azione di Donald Norman: i sette stadi (Goal → Plan → Specify → Perform → Perceive → Interpret → Compare), i due gulf (execution, evaluation) come metriche delle distanze cognitive, le quattro proprietà cardine (visibilità, feedback, mapping, constraint) come criteri di qualità per L2. Introduce Norman come terzo gigante del metodo accanto a Luhmann (atomicità del nodo) e Karpathy (manutenzione LLM).

Aggiornati i README di `metodo` e di `salute` per citare i tre giganti. Aggiornato `confronto-progetti-adottanti.md` per registrare la promozione dello strato output da "componente locale aggiuntivo" a "componente universale con forme locali". Filing back: il file `salute/quadro/quadro-corporeo.md` linka ora i due nuovi nodi metodologici (dal locale verso il meta), pattern che diventa parte del metodo stesso.

Una formulazione che resta come fondamento: lo strato output esiste perché il KB possa restare puro. È la sua condizione di possibilità, non un'aggiunta opzionale.

Provocazione utile da Norman, ripresa nel nodo `ciclo-azione`: se l'utente non agisce, la KB è mal progettata, non l'utente è pigro. Lo strato output va dunque valutato sui criteri di Norman, non sulla bellezza dei nodi.

I due nodi sono in stato bozza. Maturazione attesa con l'uso reale del pilota in `salute`.

---

## 2026-05-24 — Strato output e terzo gigante Norman

Sessione cross-repo nata in `salute` con ricadute meta importanti. La riflessione ha riconosciuto una funzione cognitiva universale del metodo finora implicita: lo strato di OUTPUT, distinto dalla KB. Tre formulazioni stabilizzate.

Prima: il conflitto Zettelkasten/Karpathy sulla sintesi (atomicità vs pagine di sintesi nel wiki) si risolve separando KB e output. La sintesi vive nello strato output, non nei nodi. **Lo strato output esiste perché il KB possa restare puro.** Risolve anche pressioni attualmente visibili in alcuni nodi (es. `salute/kb/storia-clinica.md`, diventato di fatto un dashboard improprio).

Seconda: l'output universale ha tre livelli. L1 — macchina (JSON, dati strutturati, `.nix`), L2 — decisione umana (schemi, diagrammi, slides, termometri), L3 — azione nel mondo (email, parole dette, gesti corporei, transazioni). L3 ritorna come fonte chiudendo il ciclo. Stato attuale dei quattro progetti adottanti:

- `nixos`: L1 forte (`home/`, `hosts/`, `modules/`), L2 debole (architettura solo come testo in `kb/`), L3 forte (sistema in esecuzione)
- `bi`: forte su tutti i livelli (scripts notturni + `presentazione/` Reveal.js + decisioni business)
- `economia`: L1 forte (`output/json/`), L2 medio (`output/report*.md` solo tabelle), L3 forte (email, riunioni famigliari)
- `salute`: L1 implicito sparso, L2 assente (l'SVG su Drive era un proto-output fuori repo), L3 medio-forte

Pattern emergente: dove L2 è forte (`bi`) il progetto serve decisioni condivise con altri; dove è debole resta personale e introspettivo, e fatica a generare azione coordinata.

Terza: Donald Norman è il terzo gigante del metodo accanto a Luhmann e Karpathy. Il modello dei sette stadi e i due gulf (execution, evaluation) descrivono precisamente come L1/L2 servono L3. Le quattro proprietà cardine (visibilità, feedback, mapping, constraint) diventano criteri di qualità per L2. Provocazione utile: una KB con poche affordance e nessun feedback è mal progettata, non è la persona pigra.

Decisione: pilota prima in `salute/quadro/`, formalizzazione meta dopo. Aperto il task gemello `ponte-teoria-pratica` in `todo/`, con dipendenza esplicita dal pilota di salute. I due nodi che nasceranno in `kb/` sono `ponte.md` (lo strato, risoluzione Zettelkasten/Karpathy, tre livelli, ciclo chiuso) e `ciclo-azione.md` (distillazione metodologica di Norman, gemello formale di `pattern-karpathy.md`, non biografia). Aggiornamenti collaterali previsti: `confronto-progetti-adottanti.md` per promuovere l'output da "componente locale" a universale, e `metodo-kb.md` per citare i tre giganti.

---

## 2026-05-24 — Osservatorio salute chiuso

Chiuso il task `osservatorio-salute`: nel repo `salute` sono stati creati
`kb/mappa-progetto.md`, `kb/principi-salute.md` e
`kb/verifica-nel-vivere.md`, con aggiornamento di README, CLAUDE e log locali.

Il caso conferma tre regole metodologiche. Primo: le verifiche cross-repo
restano nel repo `metodo`, ma quando producono contenuto di dominio diventano
task locali. Secondo: per KB riflessive la mappa non deve simulare una mappa
tecnica; deve collegare assi concettuali, fonti, pratica e diario. Terzo:
README-only è accettabile per ingest semplici, mentre interventi strutturali o
serie di nodi richiedono `todo/` finché non vengono stabilizzati in nodi.

## 2026-05-22 — Fondazione del repo

Creato il repo `~/metodo` come fonte unica di verità per i nodi metodologici,
consolidando le versioni sparse in nixos, bi, economia e salute.

La versione nixos era la più evoluta su tutti i nodi. Il diff ha rilevato tre
contributi non banali dagli altri repo:

- `struttura-progetto`: da economia, aggiunta la nozione di "README come
  artefatto a doppia audience" e "revisione-tasks come chiusura sessione"
- `strumenti-kb`: da economia, aggiunto il dettaglio "tre livelli
  (errore/avviso/info)" nell'output di audit
- `fedelta-cognitiva`: generalizzato il livello fattuale per renderlo
  domain-agnostic; aggiunta sezione "Adattamento al dominio" con economia come
  esempio di adattamento al dominio legale/finanziario

`design-principles.md` è stato scritto ex novo unificando i due approcci
divergenti di nixos (ingegneria del codice) e bi (affidabilità dei sistemi
dati) in un documento stratificato: principi universali + principi code-based +
principi specifici di progetto nel README locale.

I nodi zettelkasten, connessione e pattern-karpathy erano identici in tutti i
repo: copiati verbatim.

Fase A.2 (symlink + pulizia locale) e Fase B (strumenti cross-repo) restano
task aperti in `~/nixos/todo/metodo-repo-centralizzato.md`.

---

## 2026-05-23 — Metodo KB come hub della ricetta metodologica

Riorganizzato `kb/metodo-kb.md` per eliminare la ripetizione tra componenti
portabili, skeleton minimo e prompt di creazione. L'inventario ora compare una
sola volta come "Ricetta metodologica"; le altre sezioni descrivono creazione,
criteri di separazione e varianti osservate nei progetti adottanti.

La revisione conferma che non serve ancora creare un nodo autonomo per ogni
componente: `nodo`, `struttura-progetto` e `strumenti-kb` sono gia separati
perche hanno regole proprie, mentre README, CLAUDE, AGENTS, log e todo restano
componenti strutturali descritti dall'hub finche non accumulano semantica
riusabile piu ampia.

Aggiunto `AGENTS.md` al repo metodo per allineare il repository alla propria
ricetta minima: wrapper breve, ordine di lettura esplicito, nessuna duplicazione
delle regole operative.

Aggiunto `scripts/kb_tools.py` come backend portabile: comandi base per audit,
backlink, orfani, README, migrazione e termini candidati; comandi generici
`inventory` e `coverage` per progetti code-based. I controlli di fedelta
specifici di dominio restano estensioni locali nei progetti adottanti.

Formalizzata la funzione del repo metodo come osservatorio cross-repo in
`kb/osservatorio-metodo.md`. Il repo non conserva solo il metodo generale, ma
osserva periodicamente come il metodo viene incarnato nei progetti adottanti:
README, CLAUDE, AGENTS, log, todo, nodi, strumenti, skill, fonti di verita e
salute complessiva delle KB. Il task cross-repo esistente e stato ampliato come
prima implementazione operativa dell'osservatorio.

Aggiornato il README con il titolo `Metodo KB` e con l'inquadramento a doppia
funzione: metodo portabile e osservatorio cross-repo. L'apertura ora esplicita
che le differenze tra progetti sono materiale di analisi per decidere cosa
generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Espanso `kb/metodo-kb.md` con un indice cognitivo del metodo e creati nodi
bozza per tutti i componenti della ricetta che non avevano ancora un nodo
autonomo: AGENTS, CLAUDE, README, indice, task aperti, mappa, todo, log, git
history, skill e fonte di verita. La scelta rende esplicito che il metodo e un
work in progress pratico: i componenti non maturi possono essere descritti,
collegati, confrontati tra repo e fatti maturare nel tempo.

---

## 2026-05-24 — Revisione task come funzione strutturale di sessione

Generalizzata l'intuizione emersa da `economia`: la revisione dei task non e
solo un adattamento locale per scadenze e pratiche aperte, ma una funzione
strutturale del metodo. Le sessioni LLM pianificano, analizzano e implementano
lavoro attraverso task espliciti; se README e `todo/` driftano, la sessione
parte da una supervisione falsa.

Aggiornati i nodi `task-aperti`, `claude`, `skill` e `struttura-progetto` per
distinguere tra funzione obbligatoria e implementazione locale: ogni progetto
deve avere un controllo leggero dei task nel bootstrap operativo; una skill
dedicata `revisione-tasks` diventa opportuna quando i task sono numerosi,
dipendono da fonti/scadenze esterne o il drift produce costo reale di sessione.

Formalizzata anche la governance dei task metodologici cross-repo: vivono nel
repo `metodo` e di norma hanno precedenza sui task di progetto. Anche quando
targettano un singolo repository, restano centrali finche il motivo del lavoro e
metodologico; un task locale nasce solo quando l'intervento diventa autonomo di
dominio. Di conseguenza la verifica su `nixos`, `bi` e `salute` resta nel task
cross-repo centrale con matrice per repository, mentre `economia` resta il caso
guida gia allineato.

La coda metodologica e stata poi divisa in task centrali specifici per repo:
`osservatorio-bi`, `osservatorio-economia`, `osservatorio-nixos` e
`osservatorio-salute`. Il vecchio task unico di valutazione cross-repo e stato
rimosso per rendere le priorita ordinabili per target senza duplicare lavoro nei
repo adottanti.
