---
data: 2026-06-14
stato: aperto
---

# System image visiva: la home dell'atrio

Aperto in sessione di design 2026-06-14 (cfr. `verdict.md`, filo «Rifondazione
atrio↔azione»), riallineato 2026-06-15. Lo strato di rappresentazione grafica
sale a **componente root**: la **system image visiva**, controparte grafica
dell'atrio testuale (`ls`). Con l'allargamento di scope del 2026-06-15 questo
task **poggia su** lo strato di presentazione trasversale (cfr.
`strato-presentazione.md`): non costruisce una propria macchina, ma è la
**home** — una delle viste generate dal motore, l'entry navigabile che sintetizza
e mostra il dominio dell'artefatto.

## Dipendenza

Dipende da **Strato di presentazione trasversale (deck→view)**
(`strato-presentazione.md`): `assets/` (CSS condivisi), la convenzione `views/`,
l'invariante `file://` e la disciplina «vista derivata» vengono da lì. La home è
`index.html` in root, generata dallo stesso motore che produce
`views/interpretations.html`.

## Visione

Una singola pagina `index.html` in root, layout verticale che ricalca il
diagramma `action-cycle`:

- **header — polo GOAL**: titolo e intro presi da `README.md` (H1 + primo
  paragrafo)
- **corpo — due colonne**:
  - colonna esecuzione: card **o1 · Plan** (righe-task da `plan.md`, con
    dipendenze) → card **o2 · Specify** (ogni task linka al proprio dettaglio in
    `tasks/*.md`; in futuro alla vista `views/tasks.html`) → card **o3 ·
    Perform** (`prescriptions/`, **muted** — non cliccabile, collezione vuota
    oggi)
  - colonna valutazione: card **i3 · Compare** (fili aperti da `verdict.md`,
    titoli `##` con link `verdict.md#anchor`) → card **i2 · Interpret** (link a
    `views/interpretations.html`) → card **i1 · Perceive** (`perceptions/`,
    **muted**, vuota oggi)
- **footer — polo WORLD**: elenco dei progetti adottanti derivato da `README.md`
  (nome + descrizione), ciascuno linkato a `https://github.com/<org>/<nome>`
  (org da `git remote get-url origin`)

Le card muted (o3/i1) restano nel layout per dare a vedere il ciclo completo
(coerenza con `action-cycle`/`processing-layers`: il terzo specchio o3↔i1 è oggi
concettuale), senza `<a>` e a bassa opacità. Diventeranno attive quando
`prescriptions/`/`perceptions/` avranno contenuti.

## Guardrail (non negoziabile)

- **vista derivata, mai seconda fonte**: si genera da
  `README`/`plan`/`verdict`/`tasks`/collezioni/`git remote`; non duplica
  contenuto a mano in `index.html`. Vale anche per il polo World: derivato, non
  un secondo elenco mantenuto a mano.
- la home è statica e offline (nessun Reveal/JS): la dipendenza dal CDN resta
  confinata alle viste-deck (cfr. `strato-presentazione.md`).

## Implementazione

1. `assets/system-image.css` — stile della home, sopra i primitivi-diagramma
   condivisi in `assets/` (cfr. `strato-presentazione.md`); classe `.card.muted`
   per o3/i1. Niente duplicazione: riusa la palette/classi dello strato.
2. `tools/build_system_image.py` (stdlib-only, stile `kb_tools.py`):
   - `parse_readme()` → titolo H1 + primo paragrafo (GOAL) e sezione «Progetti
     adottanti» (World: nome + descrizione)
   - `parse_plan()` → righe della tabella `plan.md` e link a `tasks/*.md`
   - `parse_verdict()` → titoli `##` (fili aperti) con link `verdict.md#anchor`
   - `check_collection()` → presenza/assenza contenuti in
     `prescriptions/`/`perceptions/` per attivare o lasciare muted o3/i1
   - `github_org()` → org da `git remote get-url origin`
   - `render_html()` → assembla `index.html` (template a stringa, no Jinja2)
3. `tools/build-system-image.sh` — wrapper `python3 …` + `prettier --write
index.html`, mirror di `build-presentation.sh`.
4. genera e versiona `index.html` in root.
5. aggiornamenti documentali a fine lavoro: `tools.md` (nuovo script),
   `kb/project-structure.md` (la home tra gli artefatti di presentazione
   generati), `README.md` (punto nell'atrio: `index.html` controparte visiva
   dell'`ls`), `plan.md` (task completato), `verdict.md` (filo aggiornato).
