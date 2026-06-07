# Strumenti e skill

Porta-collezione di `tools/` nell'atrio di root: gli strumenti di manutenzione dell'artefatto —
la macchina del ciclo di *sviluppo* (agisce sull'artefatto), distinta dagli `scripts/` di output
del *runtime* (o3) nei repo code-based. Si vede a colpo d'occhio, si usa on-demand.
Approfondimento nel nodo [strumenti-kb](kb/strumenti-kb.md); esposizione operativa in `CLAUDE.md`.

## tools/

- `kb_tools.py` — backend deterministico portabile per l'audit della KB. Comandi:
  - `audit` — audit strutturale (link rotti, orfani, catalogo, naming, cluster, candidati termini); `--append-why` appende il report a `why.md`
  - `backlinks <nodo>` — link in/out di un nodo
  - `orphans` — nodi senza backlink
  - `readme` — copertura del catalogo `kb.md`
  - `migration` — frontmatter e footer Connessioni
  - `terms` — candidati a nuovi nodi da termini ricorrenti
  - `inventory` / `coverage` — inventario e copertura del codice (progetti code-based)

## skill

`metodo` versiona la triade base canonica in `.claude/skills/` (`audit-kb`,
`tasks-review`, `commit`) con wrapper Codex in `.codex/skills/`. È dogfooding: il
repo-modello applica a sé gli strumenti che teorizza, ed è la copia di riferimento
che gli adottanti forkano e parametrizzano sui propri check, fonti e segnali
locali. Cfr. [skill](kb/skill.md).
