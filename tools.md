# Strumenti e skill

Porta-collezione di `tools/` nell'atrio di root: gli strumenti di manutenzione dell'artefatto —
la macchina del ciclo di _sviluppo_ (agisce sull'artefatto), distinta dagli `scripts/` di output
del _runtime_ (o3) nei repo code-based. Si vede a colpo d'occhio, si usa on-demand.
Approfondimento nel nodo [strumenti-kb](kb/strumenti-kb.md); esposizione operativa in `CLAUDE.md`.

## tools/

- `kb_tools.py` — backend deterministico portabile per l'audit della KB. Comandi:
  - `audit` — audit strutturale (link rotti, orfani, catalogo, naming, cluster, candidati termini); il report è una diagnosi i1 su stdout, non si archivia
  - `backlinks <nodo>` — link in/out di un nodo
  - `orphans` — nodi senza backlink
  - `readme` — copertura del catalogo `kb.md`
  - `migration` — frontmatter e footer Connessioni
  - `terms` — candidati a nuovi nodi da termini ricorrenti
  - `inventory` / `coverage` — inventario e copertura del codice (progetti code-based)
- `build-presentation.sh` — genera il deck Reveal standalone
  `interpretations/index.html` dalla sorgente `interpretations/metodo-in-sintesi.md`
  tramite Pandoc

## skill

`metodo` versiona la triade operativa canonica in `.claude/skills/`
(`kb-review`, `tasks-review`, `commit`) e la skill di allineamento
`method-review`, con wrapper Codex in `.codex/skills/`. È dogfooding: il
repo-modello applica a sé gli strumenti che teorizza, ed è la copia di riferimento
che gli adottanti forkano e parametrizzano sui propri check, fonti e segnali
locali. Cfr. [skill](kb/skill.md).
