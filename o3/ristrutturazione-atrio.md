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
ali trasversali sono `kb/` e `presentation/`; i register puntano fuori. Cfr.
`project-structure` («La root come atrio» e «Applicazione nei progetti
adottanti») e `nested-cycles` per la facet `ciclo`.

## La ricetta (nel lessico del metodo)

1. **Collezioni-stadio.** Crea/rinomina le sei collezioni nella forma
   `i1/`–`o3/` con gli indici interni: `i1/perceptions.md`,
   `i2/interpretations.md`, `i3/verdicts.md`, `o1/plan.md`, `o2/tasks.md`,
   `o3/prescriptions.md`. La collocazione è **per funzione**, non per nome:
   cattura cronologica (diario) → `i1/`; sintesi-documento (`interpretations/`,
   `stato`) → `i2/`; `plan.md` → `o1/plan.md`; `tasks/` → `o2/`; strumenti di
   **sviluppo** (`tools/` + indice `tools.md`) → `o3/` con indice
   `prescriptions.md`. Gli `scripts/` di dominio restano o3-runtime al loro
   posto (cfr. `project-structure`); `scadenze` diventa una sezione di
   `o1/plan.md`. Una collezione senza item nasce col solo indice: l'assenza si
   mostra, non si nasconde.
2. **Catalogo.** Il catalogo dei nodi diventa l'indice interno omonimo
   `kb/kb.md` (da `kb.md` in root o `kb/index.md`, dove sta oggi). Nessun rename
   di nodi.
3. **Verdetto a fili.** `verdict.md` si scinde in `i3/`: un file per filo/area
   aperta, aggiornato in place, con indice `i3/verdicts.md`; i verdetti chiusi
   non migrano — si rimuovono, la storia resta in git. Forma e disciplina in
   `verdict`.
4. **Superficie presentativa.** `views/`, `index.html` e gli asset condivisi
   confluiscono in `presentation/` (home `index.html`, viste generate,
   `assets/`). Nei repo che hanno già forkato il cluster, **risincronizza il
   fork** dall'`o3/` del metodo: motore della home semplificato (ciclo singolo,
   un collegamento primario per slot, CONFIG minimale — la lente dev/runtime è
   rimandata a filtri nelle viste, cfr. filo `i3/home-minimalista.md` del
   metodo), `presentation.py`, `build_views.py`, `build-*.sh` con i path
   `o3/` + `presentation/`. Poi rigenera.
5. **Facet `ciclo`.** Ogni item di collezione dichiara `ciclo: dev|runtime` nel
   frontmatter, letta dal Mondo su cui l'item insiste: artefatto → `dev`,
   dominio/Mondo esterno → `runtime` (`nested-cycles`). Dal frontmatter dei task
   il campo `stato:` è soppresso (canone 2026-07-04, cfr. `tasks`): restano
   `sintesi` e `ciclo`.
6. **Forma del plan.** `o1/plan.md` in forma tabellare canonica con colonne
   `Ciclo · Task · Dip.` (cfr. `plan`); i task identificati per nome, la storia
   in git.
7. **Bussole.** Aggiorna `README.md`/`CLAUDE.md`/`AGENTS.md` locali: bootstrap e
   path interni che puntano alle vecchie posizioni (`plan.md`, `verdict.md`,
   `tasks/`, `tools/`, `views/`), più gli eventuali path verso collezioni
   interne del metodo, che ha già migrato (i nodi via symlink non cambiano). La
   sezione README canonica non cambia.
8. **Verifica.** `kb_tools.py audit` pulito, viste rigenerate dai build script,
   e il controllo finale dell'atrio: un `ls` della root che dichiari il ciclo.

## Touchpoint per-repo (indizi da verificare in loco, non ordini)

Il modello che `method` ha di ciascun repo è una fotografia dell'osservatorio e
può derivare (`cognitive-fidelity`): l'ultimo miglio lo fa il `method-review`
dell'adottante contro lo stato reale del proprio repo.

- **`nixos`** — il pilot (coda piccola, ricetta coerente). Cluster presentazione
  già forkato (`tools/`, `views/`, `index.html`, `assets/`): la migrazione è
  rename + risync del motore. Catalogo in root (`kb.md`), `tools.md` in root,
  `plan.md` senza colonna `Ciclo`, task con probabile `stato:`. Nessuna cattura
  cronologica: `i1/` nasce col solo indice. `map.md` resta in root (porta).
- **`bi`** — come `nixos` più la superficie ricca. Attenzione a distinguere: in
  `o3/` vanno solo gli strumenti di **sviluppo** (`tools/`); `scripts/`,
  `output/`, `data/` e le directory operative del dominio non sono collezioni e
  non si toccano. `interpretations/` contiene anche asset (css, html) da
  smistare tra `i2/` (sorgenti) e `presentation/` (viste).
- **`economia`** — file di dominio in root da collocare per funzione:
  `stato` → `i2/`, `scadenze` → sezione di `o1/plan.md`, la cattura cronologica
  se esiste → `i1/`. `data/` resta membrana non versionata, `interpretations/`
  versionata → `i2/`.
- **`salute`** — `diario` → `i1/`, `scadenze` → sezione di `o1/plan.md`. KB
  ampia: la migrazione tocca solo il catalogo (→ `kb/kb.md`), nessun rename di
  nodi. Verificare se il cluster presentazione è stato forkato o va impiantato.

## Ordine e chiusura

Pilot su `nixos`: i cocci del pilot raffinano questa prescrizione prima che gli
altri tre la eseguano. La prescrizione resta attiva finché i quattro adottanti
non l'hanno recepita via il proprio `method-review`; recepita da tutti, si
rimuove dalla collezione e si aggiorna il task di tracciamento
(`o2/propagazione-atrio-adottanti.md`, che chiude con lei). La storia resta in
git.
