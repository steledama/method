# log.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta.

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
