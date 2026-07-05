---
data: 2026-07-05
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute (pilot: nixos)
---

# Ristrutturazione dell'atrio: le collezioni-stadio arrivano agli adottanti

## Cosa e perché

Con la ristrutturazione dell'atrio (2026-07-04) il canone descrive una struttura
che nessun adottante ha ancora: è la prima divergenza **strutturale** (non
additiva) del canone dalla forma che i quattro repo conoscono. Gli adottanti
leggono i nodi via symlink: ogni loro sessione legge `project-structure` e gli
altri nodi strutturali che contraddicono l'albero locale. Senza prescrizione la
divergenza si chiude per drift — ogni repo migrerebbe a modo suo, o non
migrerebbe affatto.

Il principio dell'atrio: la root è l'ingresso dell'artefatto e l'`ls` ne
dichiara l'anatomia, che **è il ciclo stesso**. Le sei collezioni-stadio portano
il codice del loro stadio (`i1/` Perceive, `i2/` Interpret, `i3/` Compare, `o1/`
Plan, `o2/` Specify, `o3/` Perform), ognuna col proprio indice interno; le due
ali trasversali sono `kb/` e `presentation/`; i register puntano fuori. Nei
repo di dominio l'atrio non è un contenitore di comodo per il corpo di dominio:
è il punto in cui si vede se il dominio accetta la grammatica del metodo. Il
cuore della migrazione non è il rename delle stanze, è decidere voce per voce
**in quale spazio versionato previsto** vive ogni contenuto. Ciò che non entra
resta fuori solo come eccezione dichiarata; se le eccezioni diventano troppe, il
verdetto non è un adattamento locale ma un limite di fit del metodo su quel
dominio. Cfr. `project-structure` («La root come atrio», «L'inventario
dell'atrio», «Applicazione nei progetti adottanti») e `nested-cycles` per la
facet `ciclo`.

## La ricetta (nel lessico del metodo)

1. **L'inventario dell'atrio — il cuore della migrazione.** Elenca ogni voce
   dell'`ls` della root e assegnale una classe (cfr. `project-structure`,
   «L'inventario dell'atrio»): bussola/regole, collezione-stadio, ala,
   register, contenuto versionato collocato per funzione negli stadi,
   **eccezione di toolchain** (file che lo strumento inchioda alla root:
   `flake.nix`, `package.json` — dichiarata una volta), **traffico runtime**
   (cache, log, output intermedi → membrana `world/` o gitignore). Il corpo di
   dominio non è una classe che autorizza la permanenza in root: è materiale da
   portare nello spazio funzionale previsto (`i1` cattura, `i2` sintesi, `o1`
   piano, `o2` specifica, `o3` atto/prescrizione/esecutore), salvo eccezione
   motivata. Nessuna voce resta senza classe: ciò che non si lascia
   classificare si conta, e il conteggio è il **verdetto di fit** del metodo
   sul dominio, da riportare nell'esito del `method-review` — la negazione
   onesta è un verdetto, il non-averci-provato no. Il resto della ricetta
   esegue questo inventario; senza di esso le sei stanze sono una
   sovrastruttura vuota posata accanto al dominio.
2. **Collezioni-stadio.** Crea/rinomina le sei collezioni nella forma
   `i1/`–`o3/` con gli indici interni: `i1/perceptions.md`,
   `i2/interpretations.md`, `i3/verdicts.md`, `o1/plan.md`, `o2/tasks.md`,
   `o3/prescriptions.md`. La collocazione è **per funzione**, non per nome:
   cattura cronologica (diario) → `i1/`; sintesi-documento (`interpretations/`,
   `stato`) → `i2/`; `plan.md` → `o1/plan.md`; `tasks/` → `o2/`; strumenti di
   **sviluppo** (`tools/` + indice `tools.md`) → `o3/` con indice
   `prescriptions.md`, che **assorbe** `tools.md` in una sezione «Strumenti»
   — la forma di `method` e `nixos`: una collezione ha un solo indice.
   Declassare il vecchio catalogo a item indicizzato (la via di `economia`) è
   tollerato, non preferito (coccio `economia`); dichiarazioni, script,
   moduli, client o altri sorgenti
   che compiono/preparano l'atto sul Mondo → `o3/` come o3-runtime, con
   sottocartelle di dominio quando serve. `scadenze` diventa una sezione di
   `o1/plan.md`. Una collezione senza item nasce col solo indice: l'assenza si
   mostra, non si nasconde. Nel trasloco, **risincronizza `kb_tools.py`**
   dall'`o3/` del metodo: il fork pre-atrio non conosce i path nuovi e conta il
   catalogo `kb/kb.md` come nodo (il canonico lo esclude per nome, con fallback
   legacy per `kb.md` in root) — coccio del pilot `nixos`; le copie fino a
   `f89076c` contano rotti anche i cross-link validi al canone via symlink
   `method/` (l'inventario copre solo la `kb/` locale: il canonico ora valida
   con `resolved.exists()`, come il catalogo) — coccio `salute`.
3. **Catalogo.** Il catalogo dei nodi diventa l'indice interno omonimo
   `kb/kb.md` (da `kb.md` in root o `kb/index.md`, dove sta oggi). Nessun rename
   di nodi.
4. **Verdetto a fili.** `verdict.md` si scinde in `i3/`: un file per filo/area
   aperta, aggiornato in place, con indice `i3/verdicts.md`; i verdetti chiusi
   non migrano — si rimuovono, la storia resta in git. La scissione è reale:
   il monolite dei verdetti non si incarta dietro un indice-wrapper (coccio
   `economia`). Forma e disciplina in `verdict`, citato come nodo via symlink
   (`method/verdict.md`): il symlink espone solo `kb/`, un path come
   `method/i3/…` è rotto per costruzione.
5. **Superficie presentativa.** `views/`, `index.html` e gli asset condivisi
   confluiscono in `presentation/` (home `index.html`, viste generate,
   `assets/`). Nei repo che hanno già forkato il cluster, **risincronizza il
   fork** dall'`o3/` del metodo: motore della home semplificato (ciclo singolo,
   un collegamento primario per slot, CONFIG minimale — la lente dev/runtime è
   rimandata a filtri nelle viste, cfr. filo `i3/home-minimalista.md` del
   metodo), `presentation.py`, `build_views.py`, `build-*.sh` con i path
   `o3/` + `presentation/`. Poi rigenera.
6. **Facet `ciclo`.** Ogni **item** di collezione dichiara `ciclo: dev|runtime`
   nel frontmatter, letta dal Mondo su cui l'item insiste: artefatto → `dev`,
   dominio/Mondo esterno → `runtime` (`nested-cycles`). Gli **indici** di
   collezione restano senza frontmatter; l'eccezione è `o1/plan.md`, insieme
   indice e unico item del suo stadio, che la dichiara (cfr. il canonico —
   coccio del pilot `nixos`). Dal frontmatter dei task il campo `stato:` è
   soppresso (canone 2026-07-04, cfr. `tasks`): restano `sintesi` e `ciclo`.
7. **Forma del plan.** `o1/plan.md` in forma tabellare canonica con colonne
   `Ciclo · Task · Dip.` (cfr. `plan`); i task identificati per nome, la storia
   in git.
8. **Bussole.** Aggiorna `README.md`/`CLAUDE.md`/`AGENTS.md` locali: bootstrap e
   path interni che puntano alle vecchie posizioni (`plan.md`, `verdict.md`,
   `tasks/`, `tools/`, `views/`), più gli eventuali path verso collezioni
   interne del metodo, che ha già migrato (i nodi via symlink non cambiano). Il
   README acquisisce la **legenda dell'atrio**: ogni voce di root con la sua
   classe, eccezioni comprese — l'inventario copre l'`ls -A`, dotfile inclusi
   (`.gitignore`, `.env.example`, `.claude/`; coccio `economia`); il contenuto
   versionato non resta in root per inerzia, ma viene ricollocato nello stadio
   funzionale previsto. La sezione README canonica non cambia.
9. **Verifica.** `kb_tools.py audit` pulito, viste rigenerate dai build script,
   e il controllo finale dell'atrio: un `ls` della root in cui ogni voce o
   dichiara il ciclo o è classificata dall'inventario del passo 1 — nessuna
   voce senza classe. La migrazione chiude solo col **commit locale** (gate
   `/commit`): avanzare il marker `method-review.md` su un working tree non
   committato è uno stato incoerente — coccio `economia`.

## Touchpoint per-repo (indizi da verificare in loco, non ordini)

Il modello che `method` ha di ciascun repo è una fotografia dell'osservatorio e
può derivare (`cognitive-fidelity`): l'ultimo miglio lo fa il `method-review`
dell'adottante contro lo stato reale del proprio repo.

- **`nixos`** — il pilot: la migrazione strutturale è **recepita** (2026-07-05)
  e il passo 1 ha forzato la correzione del canone: il corpo dichiarativo
  versionato non resta in root ma va in `o3/` come o3-runtime (`home/`,
  `hosts/`, `modules/`, `identity/`, `patches/`, `scripts/`). `flake.nix` e
  `flake.lock` restano eccezioni di toolchain inchiodate alla root; `secrets/`
  è eccezione non versionata/materia del Mondo; `result*`, `world` e cache sono
  traffico runtime gitignored.
- **`bi`** — come `nixos` più la superficie ricca, ed è il caso più costoso
  dell'**inventario**: la root mescola sorgenti da ricollocare per funzione
  (`client/`, `scripts/` e strumenti), traffico runtime da portare in membrana o
  gitignore (`cache/`, `logs/`, `temp/`, `processed/`, `pending/`, `output/`,
  `foto/`) e vincoli di toolchain (`package.json`, `node_modules/`) — qui il
  passo 1 è il grosso del lavoro, e il suo verdetto di fit è il più informativo
  per l'osservatorio. `interpretations/` contiene anche asset (css, html) da
  smistare tra `i2/` (sorgenti) e `presentation/` (viste); gli esecutori e il
  corpo performativo vanno in `o3/` salvo eccezione dichiarata.
- **`economia`** — **recepita** (2026-07-05, commit `a0538f5`, marker a
  `77d8225`, audit e facet puliti, verdetto di fit 0 eccezioni, working tree
  pulito): ricollocazione completa in `o3/` e `presentation/`, i3 scisso a
  file-per-filo, `tools.md` indicizzato da `prescriptions.md`, legenda estesa
  all'`ls -A`, symlink `memory` (anti-pattern del canone) rimosso. I suoi
  quattro cocci sono incisi nei passi 2, 4, 8 e 9 di questo runbook.
- **`salute`** — `diario` → `i1/`, `scadenze` → sezione di `o1/plan.md`. KB
  ampia: la migrazione tocca solo il catalogo (→ `kb/kb.md`), nessun rename di
  nodi. Verificare se il cluster presentazione è stato forkato o va impiantato.

## Ordine e chiusura

Pilot su `nixos`: i cocci del pilot hanno raffinato questa prescrizione e reso
vincolante la collocazione completa del contenuto versionato negli spazi
funzionali. La prescrizione resta attiva finché i quattro adottanti non l'hanno
recepita via il proprio `method-review`; recepita da tutti, si rimuove dalla
collezione e si aggiorna il task di tracciamento
(`o2/propagazione-atrio-adottanti.md`, che chiude con lei). La storia resta in
git.
