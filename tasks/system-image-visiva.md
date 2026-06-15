---
data: 2026-06-14
stato: aperto
---

# System image visiva: strato di rappresentazione in root

Aperto in sessione di design 2026-06-14 (cfr. `verdict.md`, filo «Rifondazione
atrio↔azione»). Gli atomi di stadio e l'atrio a tre specie sono fatti: gli stadi e le
collezioni danno ora le fonti da rappresentare. Lo strato di rappresentazione grafica — oggi
confinato come deck in `interpretations/` — sale a **componente root**: la **system image
visiva**, controparte grafica dell'atrio testuale (`ls`). Mostrerà il ciclo dell'azione
di dominio «all'opera viva» e darà il tono all'intero progetto.

I tre punti "da sciogliere" della prima apertura sono stati discussi in sessione
2026-06-15 e risolti — vedi «Decisioni». Questo task ora descrive la
**visione** e l'**implementazione** da eseguire.

## Decisioni

1. **Entry-file + asset**: `index.html` in root (vista derivata, generata) +
   cartella `assets/` in root per CSS/JS dedicati alla system image.
2. **Cockpit (o2) vs sintesi (i2)**: **un'unica vista navigabile**, non due
   superfici separate. Riusa il diagramma `action-cycle` già presente in
   `interpretations/metodo-in-sintesi.md` (GOAL in cima, due colonne
   esecuzione/valutazione, WORLD in fondo), reso interattivo/cliccabile.
3. **Portabilità + World derivabile**: niente elenco adottanti hardcoded nel
   generatore. Il polo World si deriva dalla sezione `## Progetti adottanti`
   di `README.md` (lista `[nome](path-relativo)`, già esistente) per nome e
   descrizione, combinata con l'org GitHub letta da `git remote get-url
origin` del repo corrente (`steledama` per `method`) per costruire
   `https://github.com/<org>/<nome>`. Il link GitHub è quindi **derivato**,
   non una seconda fonte scritta a mano. Il meccanismo (sezione README
   designata + org da git remote) è il pattern portabile; quali repo elencare
   resta contenuto di dominio di ciascun progetto — in `method` è "Progetti
   adottanti", in un adottante potrebbe essere un'altra sezione o assente.

## Visione

Una singola pagina `index.html`, layout verticale che ricalca il diagramma
`action-cycle`:

- **header — polo GOAL**: titolo e intro presi da `README.md` (H1 + primo
  paragrafo)
- **corpo — due colonne**:
  - colonna esecuzione: card **o1 · Plan** (righe-task da `plan.md`, con
    dipendenze) → card **o2 · Specify** (ogni task linka al proprio dettaglio
    cliccabile in `tasks/*.md`) → card **o3 · Perform** (`prescriptions/`,
    **muted** — non cliccabile, collezione vuota oggi)
  - colonna valutazione: card **i3 · Compare** (fili aperti da `verdict.md`,
    titoli `##` con link `verdict.md#anchor`) → card **i2 · Interpret** (link
    al deck `interpretations/index.html`) → card **i1 · Perceive**
    (`perceptions/`, **muted**, vuota oggi)
- **footer — polo WORLD**: elenco dei progetti adottanti derivato da
  `README.md` (nome + descrizione), ciascuno linkato a
  `https://github.com/<org>/<nome>`

Le card muted (o3/i1) restano nel layout per dare a vedere il ciclo completo
(coerenza con `action-cycle`/`processing-layers`: il terzo specchio o3↔i1 è
oggi concettuale), ma senza `<a>` e con stile a bassa opacità. Diventeranno
attive quando `prescriptions/`/`perceptions/` avranno contenuti.

## Guardrail (non negoziabile)

- **vista derivata, mai seconda fonte**: si genera da
  `README`/`plan`/`verdict`/`tasks`/collezioni/`git remote`; non duplica
  contenuto a mano in `index.html`. Vale anche per il polo World: derivato,
  non un secondo elenco mantenuto a mano.
- `interpretations/` resta la collezione delle sorgenti i2; il sito generato
  vive in root; `build-presentation.sh` resta per il deck, un nuovo script
  affianca senza sovrapporsi.

## Implementazione

1. **`assets/system-image.css`** (nuovo) — CSS standalone (no dipendenza da
   Reveal.js/CDN): porta le CSS variables di palette e le classi diagramma
   (`.diagram.action-cycle`, `.cycle-columns`, `.cycle-side`, `.card`,
   `.card.pole`, `.card.world`, `.arrow`) da `interpretations/reveal.css`
   (righe ~1-280), rimuove lo scoping `.reveal`, aggiunge layout responsive a
   due colonne con header/footer per i poli. Le card o3/i1 ottengono una
   classe `.card.muted` (bassa opacità, nessun `:hover`, nessun `<a>`).

2. **`tools/build_system_image.py`** (nuovo, stdlib-only come `kb_tools.py`):
   - `parse_readme()` → titolo H1 + primo paragrafo (polo GOAL) e sezione
     "Progetti adottanti" (polo World: nome + descrizione + path)
   - `parse_plan()` → righe della tabella `plan.md` (`# | Task | Dip.`) e
     sezione "Dettagli task" per i link a `tasks/*.md`
   - `parse_verdict()` → titoli `##` (fili aperti) da `verdict.md`, con link
     `verdict.md#<anchor>`
   - `check_collection(name)` → presenza/assenza di contenuti oltre
     all'indice interno omonimo in `prescriptions/`/`perceptions/`, per
     decidere se la card o3/i1 resta muted o diventa link
   - `github_org()` → deriva l'org da `git remote get-url origin`
   - `render_html()` → assembla `index.html` da template a stringa (no
     Jinja2, non disponibile)
   - `main()` scrive `index.html` in root

3. **`tools/build-system-image.sh`** — wrapper: `python3
tools/build_system_image.py` poi `prettier --write index.html`, mirror di
   `build-presentation.sh`.

4. **Genera e committa `index.html`** (artefatto generato, come
   `interpretations/index.html`).

5. **Aggiornamenti documentali**:
   - `tools.md` — nuova voce per `build_system_image.py` /
     `build-system-image.sh`
   - `kb/project-structure.md` — nota nello skeleton: `index.html` (system
     image visiva, generata) + `assets/` come nuovo componente root, vista
     derivata del ciclo intero
   - `README.md` — un punto nell'atrio che segnala `index.html` come
     controparte visiva dell'`ls`
   - `plan.md` — segnare questo task completato/rimuoverlo dalla tabella a
     fine lavoro
   - `verdict.md` — aggiornare il filo «Rifondazione atrio↔azione» a fine
     lavoro: system image visiva v1 fatta, prossimi passi (o3/i1 attivi)
     eventualmente come nuovo task
