# log.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta.

---

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
