---
data: 2026-06-07
stato: aperto
---

# Skill method-review per riallineare gli adottanti

Progettare una skill base condivisa `method-review`, canonica in `metodo` e
replicata nei repo adottanti, per verificare il drift locale rispetto
all'evoluzione del metodo senza aprire task centrali di propagazione.

La skill si esegue nel repo adottante. Legge i commit di `metodo` successivi
all'ultima revisione registrata, confronta le generalizzazioni portabili con
l'implementazione locale e distingue:

- cambiamenti applicabili direttamente;
- cambiamenti da adattare al dominio;
- cambiamenti non pertinenti;
- divergenze locali intenzionali da preservare;
- problemi locali che richiedono un task nel repo adottante.

Non deve orchestrare modifiche cross-repo dal repository `metodo`, applicare
ciecamente ogni differenza o sostituire `tasks-review`: `method-review` controlla
la relazione adottante-metodo; `tasks-review` supervisiona il lavoro futuro del
dominio.

## Questioni da risolvere

- come registrare in modo versionato e leggibile l'ultimo commit di `metodo`
  revisionato, senza stato host-locale o opaco;
- quali superfici confrontare: README, CLAUDE, AGENTS, porte root, nodi
  metodologici, skill base, strumenti e convenzioni;
- quali controlli possono essere deterministici e quali richiedono giudizio;
- se la skill debba solo proporre modifiche o possa applicarle dopo conferma;
- come gestire modifiche locali legittime alle skill forkate senza sovrascriverle;
- come produrre un esito sintetico: allineato, adattamento necessario, non
  pertinente, task locale aperto;
- come evitare che il marker di revisione dichiari allineamento quando restano
  modifiche pertinenti non applicate;
- **blind spot host-config (dichiarato, non risolvibile dalla skill):** alcune
  regole del metodo si impongono in config fuori dai repo (es. il disable di
  `auto-memory`, versionato in `nixos`, non in ciascun adottante). La skill legge
  il `git log` dei repo e non vede questo strato: deve dichiararlo come limite, non
  certificarlo allineato. Cfr. verdict.md «La memoria dell'harness: regola portabile a
  L2…».

## Backlog di drift da propagare (fotografia 2026-06-13)

Generalizzazioni portabili entrate in `method` dopo l'ultimo allineamento ampio
degli adottanti (atrio + README-bussola, 2026-06-07). La skill le porterà un repo
per volta; è il drift reale su cui pilotarla, e il marker di revisione parte da qui.

**Nodi condivisi via symlink — allineamento automatico, nessuna azione** (la skill
li verifichi solo per riferimenti locali stantii): `consenso`, `vincolo`,
`matrice-ciclo-azione` e il framing i2-micro/macro in `ciclo-azione`. Anche
`kb/verdict.md` arriva per symlink: la _disciplina_ è già condivisa, manca solo la
migrazione del file locale (sotto).

**Da propagare (per repo):**

- **`why.md` → `verdict.md` + disciplina per-filo** (`dd5c2e7`, `8f0b74f`): gli
  adottanti hanno ancora `why.md` append-only. Rinomina il file, asciuga il
  preambolo, migra i fili aperti a stato-corrente, rimuovi i chiusi; aggiorna i
  riferimenti in `README`/`CLAUDE`/`AGENTS`/nodi. Supera il vecchio runbook
  `tasks/sostanza-why.md` (era per `log`→`why`; ora la meta è `verdict`). _Diretto
  ma editoriale_: la migrazione dei fili è giudizio, non meccanica.
- **`/audit-kb` → `/kb-review`** (`dd5c2e7`): rinomina `.claude/skills/audit-kb` e
  il wrapper `.codex/skills/audit-kb`; aggiorna `name`/trigger/path nei wrapper e i
  riferimenti in `CLAUDE`/`README`/`tools.md`/`plan.md`/nodi. _Diretto._
- **Rimozione `--append-*` da `kb_tools.py` e da `/kb-review`** (`8f0b74f`):
  l'audit è una diagnosi i1 su stdout, non si archivia nel file dei verdetti.
  Rimuovi flag, funzione di append e i passi di append nella skill. _Diretto, se
  l'adottante ha forkato `kb_tools.py`._
- **`/commit` con check i2/i3 espliciti + cascata plan/tasks/Goal** (`dd5c2e7`):
  allinea la skill forkata ai due check leggeri (i2 ri-derivazione del deck, i3
  aggiornamento del verdetto) e alla cascata. _Diretto._
- **Forma `plan.md` `#`/footer uniforme** (`85927c9`, `e14eb0c`, `1a313ed`):
  invariante su tutti i repo; `method` e `bi` conformati. Pendenti: `nixos`,
  `economia`, `salute`. _Diretto._
- **Regola tabelle vs elenchi per mobile** (`1cb16ed`, `f17ee07`): converti i
  confronti tabellari in elenchi puntati (eccezione `plan.md`); aggiungi la regola
  al `CLAUDE.md` locale se manca. _Diretto._
- **Separazione dati / presentazioni versionate** (`8eab442`): dove l'adottante ha
  uno strato dati (`economia/output`, `salute`, `bi`), fonte-di-verità fuori da Git
  in `data/` locale, deck/o2 curato versionato. _Adatta al dominio._
- **Rename repo `metodo` → `method`** (`b593899`): verifica symlink
  (`method/ → ../method/kb`) e path `metodo/`→`method/` in `CLAUDE`/`README` locali.
  _Perlopiù già fatto col rename — verifica residui._
- **Split `output.md` → `output.md` + `input.md`** (commit di questa sessione):
  l'arco di input non è più una sottosezione di `output`, ma un nodo pari; la
  geometria (specchio, cerniere, annidamento) è consolidata in `ciclo-azione`.
  Entrambi i nodi arrivano per symlink. Verifica nei riferimenti locali
  (`README`/`CLAUDE`/nodi) i puntatori a `method/output.md` usati per l'_arco di
  input_ e ripuntali a `method/input.md`. _Diretto, verifica._

**Da adattare, non propagare ciecamente:**

- **`presentations/` → `interpretations/`** (`dd5c2e7`): in `method` il deck è
  **i2-macro** (rilegge l'artefatto), per questo «interpretations»; negli adottanti
  lo stesso deck è prevalentemente **o2** (cruscotto sul mondo). Il nome uniforme
  vale per il _tool_, non per la _porta_ quando il ruolo nel ciclo differisce: la
  skill segnali la divergenza e lasci la scelta del nome al giudizio locale, senza
  rinominare d'ufficio.

## Pilota

1. Definire il contratto della skill in `metodo` e il formato del marker
   versionato.
2. Implementare la copia canonica con wrapper Codex.
3. Pilotarla su un solo adottante usando il backlog di drift qui sopra come
   materiale reale (candidato: `economia`, bisogno massimo).
4. Verificare che distingua correttamente canone comune e adattamento locale.
5. Solo dopo il pilota, replicarla negli altri adottanti e aggiornare il nodo
   `skill`.

## Criterio di chiusura

La skill è presente e documentata in `metodo`, validata su un adottante e
replicata nei quattro repo. Ogni esecuzione può determinare in modo verificabile
quali commit del metodo sono stati revisionati e lascia eventuale lavoro futuro
nel `plan.md`/`tasks/` del repo locale, non in quello di `metodo`.
