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
- **Separazione dati / interpretazioni versionate** (`8eab442`): dove l'adottante
  ha uno strato dati (`economia/output`, `salute`, `bi`), fonte-di-verità fuori da
  Git in `data/` locale, sintesi interpretativa curata e versionata in
  `interpretations/`. _Adatta al dominio nei contenuti, non nell'anatomia._
- **Rename repo `metodo` → `method`** (`b593899`): verifica symlink
  (`method/ → ../method/kb`) e path `metodo/`→`method/` in `CLAUDE`/`README` locali.
  _Perlopiù già fatto col rename — verifica residui._
- **Split `output.md` → `output.md` + `input.md`** (commit di questa sessione):
  l'arco di input non è più una sottosezione di `output`, ma un nodo pari; la
  geometria (specchio, cerniere, annidamento) è consolidata in `ciclo-azione`.
  Entrambi i nodi arrivano per symlink. Verifica nei riferimenti locali
  (`README`/`CLAUDE`/nodi) i puntatori a `method/output.md` usati per l'_arco di
  input_ e ripuntali a `method/input.md`. _Diretto, verifica._
- **Nodo `presentazione.md` → `deck.md`** (commit di implementazione della
  skill): `interpretations/` è la collezione canonica, l'interpretazione è la
  funzione cognitiva, il deck una sua forma navigabile. Aggiorna i riferimenti
  locali; alla fotografia attuale ne esistono in `bi/why.md` e
  `salute/tasks/quadro-deck-viscerale.md`, nessuno in `economia` o `nixos`.
  _Diretto._

- **`presentations/` → `interpretations/`** (`dd5c2e7`): nome canonico della
  superficie di sintesi in tutti i repo. Anche negli adottanti la selezione,
  aggregazione e rappresentazione dei dati non è neutra: interpreta il Mondo
  secondo i goal dell'artefatto. Il dominio colora contenuti, metriche e forme,
  non l'anatomia né il nome della porta. Rinomina directory, porta root,
  generatori e riferimenti locali. _Diretto._

## Pilota

1. Definire il contratto della skill in `metodo` e il formato del marker
   versionato.
2. Implementare la copia canonica con wrapper Codex.
3. Pilotarla su un solo adottante usando il backlog di drift qui sopra come
   materiale reale (candidato: `economia`, bisogno massimo).
4. Verificare che distingua correttamente canone comune e adattamento locale.
5. Solo dopo il pilota, replicarla negli altri adottanti e aggiornare il nodo
   `skill`.

## Decisioni di progetto

- Il marker vive in `method-review.md` nella root dell'adottante: frontmatter
  machine-readable (`method_commit`, `reviewed_at`, `status`) e corpo leggibile
  per adattamenti intenzionali e limiti.
- Il cursore è uno SHA completo del repo `method`, non una data o uno SHA del
  repo adottante.
- `status: aligned` significa che tutte le modifiche pertinenti sono applicate,
  già soddisfatte, preservate esplicitamente oppure affidate a un task locale.
  Un task locale può quindi sbloccare il marker senza fingere che il lavoro sia
  concluso.
- Se resta una modifica pertinente senza risoluzione o task,
  `status: action-required` e lo SHA non avanza.
- La classificazione include `gia-soddisfatto`: il pilot ha mostrato che un
  backlog statico può diventare stale mentre i repo evolvono in parallelo.
- La skill non fa `fetch`/`pull`: revisiona il checkout locale di `method` e
  dichiara eventuali modifiche non committate fuori intervallo.
- Il primo baseline non viene inventato: va ricostruito dalla storia e confermato
  dall'utente prima di creare il marker.

## Pilot su economia (2026-06-13)

Baseline candidato: `b593899b6459c806f751875907cf1b9e3dae92aa`
(`method` rinominato e riferimenti locali già aggiornati dal commit economia
`8ca40bd`). Intervallo osservato:
`b593899..ec99335c59d228d3df9fa25a5722ef703714b13b`.

- `f17ee07` tabelle vs elenchi: **gia-soddisfatto** da `aeb2f18`; la regola è
  presente nel `CLAUDE.md` locale.
- `8eab442` separazione dati/interpretazioni: **gia-soddisfatto** nella sostanza
  da `ea282bc`; `data/` resta locale e la sintesi resta versionata. Il nome della
  porta viene corretto separatamente sotto.
- `dd5c2e7` rename `why.md` → `verdict.md`: **diretto-editoriale**, applicato nel
  pilot.
- `dd5c2e7` rename `/audit-kb` → `/kb-review`: **diretto**, applicato nei wrapper
  e nei riferimenti.
- `dd5c2e7` check i2/i3 e cascata nella skill `/commit`: **diretto con merge
  locale**, applicato preservando le checklist finanziarie.
- `dd5c2e7` `presentations/` → `interpretations/`: inizialmente classificato
  **divergenza-intenzionale**, poi corretto in **diretto**. La fotografia
  finanziaria seleziona e rappresenta i numeri secondo i goal: è
  un'interpretazione di dominio, non un'eccezione all'anatomia comune.
- `8f0b74f` rimozione append audit: **diretto**, applicato alla skill, a
  `tools/kb_tools.py` e a `tools.md`.
- `b29a894` split input/output: **gia-soddisfatto** per i nodi condivisi; nessun
  riferimento locale all'arco di input trovato da ripuntare.
- forma uniforme di `plan.md`: **gia-soddisfatto** dal commit economia
  `028329e`; la voce del backlog centrale era già stale.
- `ec99335` aggiorna solo il task di progettazione in `method`:
  **non-pertinente** all'implementazione locale.

Il pilot applicativo su `economia` ha completato la migrazione
`why.md`→`verdict.md`, il rename `/audit-kb`→`/kb-review`, la rimozione
`--append-why`, l'integrazione dei check i2/i3 in `/commit`, l'installazione della
skill locale e del marker, l'audit pulito e una seconda esecuzione idempotente
con intervallo vuoto. La classificazione iniziale di `presentations/` come
divergenza intenzionale è stata corretta nel repo: directory e porta root
rinominate `interpretations/` e `interpretations.md`, riferimenti e generatore
aggiornati, divergenza rimossa dal marker e natura interpretativa registrata nel
verdetto locale. La generazione produce un HTML identico al precedente, l'audit
resta pulito, non restano riferimenti a `presentations` e `/method-review` è
idempotente con marker a
`ec99335c59d228d3df9fa25a5722ef703714b13b`. Il pilot su `economia` è quindi
validato; resta la replica negli altri adottanti.

## Secondo pilot su nixos (2026-06-13)

Intervallo revisionato:
`b593899b6459c806f751875907cf1b9e3dae92aa..df9e65113ebb454c1111b7b673f3f895dcddcd9f`.
Esito: 2 cambiamenti già soddisfatti, 7 diretti, 1 adattamento NixOS, 2 non
pertinenti, 1 divergenza intenzionale e nessun task locale. Il marker è
`aligned` a `df9e65113ebb454c1111b7b673f3f895dcddcd9f`; la seconda esecuzione ha
intervallo vuoto.

Il pilot ha migrato `why.md`→`verdict.md`, rinominato
`/audit-kb`→`/kb-review`, rimosso `--append-why`, installato `method-review` e
allineato `/commit` preservando formatter, `tools/check.sh`, distinzione
Home/System e policy harness-agnostic. Ha inoltre aggiornato i riferimenti a
`output`, `input` e `deck`, verificato l'enforcement di auto-memory su tutti i
cinque profili Home Manager e corretto il parser locale di facts/coverage per
gli elenchi Markdown correnti.

La divergenza intenzionale è ontologica, non nominale: `nixos` non crea una
porta `interpretations/` vuota perché il suo output principale è la
configurazione Nix in esecuzione, o1/runtime. Questo conferma il carve-out già
definito in `struttura-progetto`: uniformità delle collezioni standard quando la
funzione esiste, non obbligo di materializzare collezioni senza contenuto.

Verifiche riferite dal pilot: audit pulito su 40 nodi, inventory 55/55 moduli,
facts e 9 macro-aree allineati, fidelity senza segnali, `tools/check.sh` e
`git diff --check` superati. Nessun rebuild, flake check, staging, commit o push.
Il secondo pilot è validato e fissato nella storia di `nixos` dal commit
`5d076aec247fa1e776929c1035f32c0cfd12861f`.

## Terzo pilot su bi (2026-06-13)

Intervallo revisionato:
`b593899b6459c806f751875907cf1b9e3dae92aa..18424f8af8111876e3da3943fc3e62748aadb73b`.
Nove commit classificati in 2 cambiamenti già soddisfatti, 3 diretti, 2
adattamenti BI e 2 non pertinenti. Il marker è `aligned` a
`18424f8af8111876e3da3943fc3e62748aadb73b`; la seconda esecuzione ha intervallo
vuoto e worktree invariato.

Il pilot ha migrato `why.md`→`verdict.md`, riducendo il log storico a tre fili
correnti; rinominato `presentations/`→`interpretations/` e la relativa porta;
rinominato `/audit-kb`→`/kb-review`; installato `method-review`; rimosso
`--append-why`; aggiornato `/commit` con i check i2/i3 e la policy
harness-agnostic, preservando i guardrail BI. I riferimenti a `output`, `input` e
`deck` sono allineati; gli undici usi applicativi di `--append-note` restano
intatti perché non appartengono al protocollo di audit.

Verifiche riferite dal pilot: audit pulito su 82 nodi, 315 link e 45 script
documentati; Prettier, Ruff, `py_compile`, audit JSON e `git diff --check`
superati; nessun riferimento ai nomi precedenti; deck e CSS serviti on-demand
con HTTP 200 e contenuti byte-identici dopo il rename. Configurazioni host
esterne non verificate. Il terzo pilot è validato e fissato nella storia di `bi`
dal commit `48f9e2ccf3fd802a75fbefc36db51ceaa0aad4aa`.

## Criterio di chiusura

La skill è presente e documentata in `metodo`, validata su un adottante e
replicata nei quattro repo. Ogni esecuzione può determinare in modo verificabile
quali commit del metodo sono stati revisionati e lascia eventuale lavoro futuro
nel `plan.md`/`tasks/` del repo locale, non in quello di `metodo`.
