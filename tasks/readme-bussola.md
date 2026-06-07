---
data: 2026-06-07
stato: aperto
---

# README come bussola: ritiro di `map.md`, scomposizione della mappa

Aperto il 2026-06-07. Un unico refactor che istituzionalizza «il README orienta e
punta, non immagazzina» e ne dà sostanza ritirando `map.md` come file separato.
Parte da `metodo` (prototipo, fatto) e si propaga ai quattro adottanti.

## La decisione

Supera la regola del 2026-06-06 «`map` resta separato dal README per pace». Si
scompone "map" in **tre funzioni**:

- **bussola** (orientamento: scopo, dominio in breve, _dove_ sta ogni cosa) → stabile → **README**
- **modello del dominio** (la teoria che evolve) → nodi `kb/` e `presentations/`; il README _punta_
- **indice-di-dominio** (il territorio reale: host/entità/sistemi → nodi) → register **`map.md`**, porta-collezione on-demand, presente solo dove il dominio ha un territorio

Rationale completo in `why.md` («README come bussola»). La pace è rispettata
meglio: lo strato veloce resta fuori dal README.

## Regola istituzionalizzata

**Il README è la bussola: orienta e punta, non immagazzina.** Principi/obiettivi
estesi → nodo (`design-principles`), il README sintetizza e rimanda. Bootstrap:
`README → CLAUDE → nodo` (map è una porta on-demand, non un file-ciclo). Nome
unico **`map.md`** per l'indice-territorio (supera `project-map.md` /
`mappa-progetto.md`).

## Ricetta di propagazione (risolta dal pilota nixos)

Decisioni fissate, valide per tutti gli adottanti:

1. **Promozione**: `kb/project-map.md` o `kb/mappa-progetto.md` → **`map.md`** in root (`git mv`).
2. **Frontmatter**: rimuoverlo (i register root non ne hanno); H1 → `# Map`.
3. **Backlink**: i footer `Connessioni:` che citano la mappa si **rimuovono** — un register è un indice monodirezionale come `kb.md`, i nodi non lo ri-citano. L'accesso resta top-down (README + bootstrap).
4. **Catalogo**: togliere la riga della mappa da `kb.md` (è un register, non un nodo `kb/`).
5. **Tool**: nei repo code-based controllare path hardcoded in `tools/kb_tools.py` (`facts`/`fidelity` leggono la mappa). In `nixos` erano 3 (`kb/project-map.md` → `map.md`); in `bi` **nessuno**.
6. **Bootstrap**: `CLAUDE.md` + `AGENTS.md` → `README → CLAUDE → nodo`; map elencata tra le porte-collezione (da aprire prima di toccare codice nei repo code-based).
7. **README**: deve restare/diventare bussola; aggiornare i riferimenti alla mappa a `map.md` (root); non indicizzare i nodi `metodo/`.
8. **Skill**: aggiornare i riferimenti a `kb/project-map.md` → `map.md` nelle SKILL.md (`audit-kb`, `tasks-review`, `commit` dove presenti).
9. **why.md**: aggiungere entry di propagazione con `How to apply`.
10. **Verifica**: `audit` + (code-based) `facts`/`fidelity` puliti; nessun residuo `project-map`/`mappa-progetto` fuori dalle entry storiche di `why.md`.

**Extra per economia e salute**: hanno **sia** un `map.md` root (l'attuale o2/compass, 60/69 righe) **sia** `kb/mappa-progetto.md` (l'indice). Quindi: (a) ripiegare il contenuto-compass dell'attuale `map.md` root nel README (bussola), poi (b) sostituire `map.md` root col contenuto promosso da `kb/mappa-progetto.md` (l'indice-territorio). Verificare che il README assorba il modello senza gonfiarsi (lì non c'è un `presentations/` ricco come in metodo).

## Stato

- [x] **metodo** — prototipo. README-bussola + nuovo titolo-banner; `map.md` ritirato; `kb/readme.md` (regola rigorosa); `kb/map.md` (register-territorio); `struttura-progetto`/`metodo-kb`/`kb.md`/`CLAUDE`/`AGENTS`/`claude`/`osservatorio` allineati; 06-06 segnato superato. Commit `0ba053f`. Audit pulito.
- [x] **nixos** — `kb/project-map.md` → `map.md`; 8 backlink rimossi; `kb_tools.py` (3 path), `CLAUDE`/`AGENTS`/README/skill `tasks-review`; frontmatter tolto. Commit `8c7ec7a`. Audit/facts/fidelity puliti.
- [ ] **bi** — _non iniziato, intatto_ (rimandabile ad altro account). Specifico: 1 solo footer backlink (`kb/graphify.md`), **nessun** hardcoding nei tool. Riferimenti da aggiornare: `kb.md` (riga prosa + riga catalogo), `CLAUDE.md` (bootstrap), README (bootstrap righe 22-23), 3 skill (`audit-kb`/`tasks-review`/`commit`), `tasks/kb-tools-facts-coverage-fidelity.md`, menzione inline in `kb/graphify.md:55` (testo "BI non ha ancora una mappa…" ormai stale, da correggere). AGENTS minimale, nessuna modifica.
- [ ] **economia** — _priorità_. Vedi "Extra" sopra (compass→README + `kb/mappa-progetto.md`→`map.md`).
- [ ] **salute** — _priorità_. Come economia.

## Questioni aperte

- nei code-based, valutare se rinominare anche gli identificatori interni `project_map_*` in `kb_tools.py` (cosmetico; in nixos lasciati invariati, aggiornati solo i path).
