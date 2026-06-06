---
data: 2026-06-06
stato: aperto
---

# Runbook — migrazione del layout «cruscotto» nei repo adottanti

Runbook esecutivo per portare un repo adottante al layout ratificato il 2026-06-06: la
root come **cruscotto del ciclo di sviluppo** (vedi [[struttura-progetto]], la triade). È
la metà «adottanti» della migrazione atomica: il repo `metodo` è già migrato (commit
`be14bf3`), `nixos` e `bi` pure (allineati al cruscotto). Restano **economia** e **salute**.

Fonti del disegno — leggere prima di eseguire:
- commit `metodo@be14bf3` — la migrazione di riferimento, voce per voce nel messaggio;
- `why.md`, entry *2026-06-06 «Il root è il cruscotto del ciclo di sviluppo»* — il perché;
- [[struttura-progetto]] — la triade (root = bootstrap-essenziali del ciclo; cartelle =
  collezioni atomiche con file-meta dentro solo se on-demand; pace = criterio di compagnia,
  non di profondità; root estensibile dal basso con file di dominio).

## Regola di esecuzione — una sessione per repo

**Non eseguire più repo da una sola sessione.** Si apre una sessione *dentro* il repo
target, si bootstrappa sul suo dominio (`README → map → CLAUDE → nodo`), si esegue questo
runbook, si committa lì. Ragione: la parte di valore (Parte B) è giudizio di dominio — `map.md`
è l'o2 di *quel* dominio — e va fatta col contesto locale caricato, non a memoria da fuori. La
parte meccanica (Parte A) è invariante e va replicata identica a `nixos`/`bi`. I nodi condivisi
si propagano già via symlink `metodo → ../metodo/kb`: nessun coordinamento cross-repo serve.

---

## Parte A — passi meccanici (invarianti, identici su ogni repo)

1. **Rinomine root, con git mv** (preserva storia):
   - `git mv log.md why.md`
   - `git mv todo tasks`
   - *Non* esiste `presentazione/` negli adottanti (hanno già l'o-layer locale: `output/`
     economia, `quadro/` salute) → la rinomina `presentazione→presentation` **non si applica**.
2. **`why.md`** — adottare il nuovo modello di entry (decisione come titolo-tesi, data come
   metadato, commit citabile inline). Aggiungere in testa l'entry di questa migrazione (vedi
   passo Verifica/Filing back). Preservare la distinzione `why` (perché interpretativo) vs
   `diario.md` (cronologia di dominio) vs `stato.md`/`scadenze.md` (bootstrap di dominio):
   non fondere, restano file separati per pace.
3. **`plan.md` in root** — estrarre la lista task dal README (o da dove vive) in `plan.md`:
   stadio Plan, task aperti prioritizzati con dipendenze, una riga per file in `tasks/`. Regola:
   ogni file in `tasks/` ha una riga in `plan.md`; ogni riga sostanziale ha un file. Distinta da
   o1 (è il Plan dello *sviluppo*, non del runtime).
4. **`kb/index.md`** — register del catalogo dei nodi (inglese-vivo) spostato *dentro* `kb/`
   (consultato on-demand), tolto dal README. Generabile/verificabile con `kb_tools.py readme`.
   Il nodo-concetto resta `kb/indice.md` se presente (italiano-doc): la coppia vivo/doc è la
   policy linguistica.
5. **Referenze in CLAUDE.md / README.md / AGENTS.md** — riscrivere i puntatori rinominati:
   `log.md→why.md`, `todo/→tasks/`, e l'ordine di bootstrap che punta a `map.md`/`plan.md`/
   `kb/index.md`. È il caso «cambio nome/path di nodo» del `CLAUDE.md` del metodo. Grep di
   verifica: nessun `log\.md`, `todo/`, `task-aperti`, `mappa\.md` residuo.
6. **`scripts/kb_tools.py`** — `--append-log` → `--append-why`; escludere `kb/index.md`
   dall'audit nodi; ripuntare la copertura sul catalogo `kb/index.md`. ⚠️ Ogni adottante ha
   una **copia propria** di `kb_tools.py` evoluta in locale (non symlink) → vedi nota *Sync di
   kb_tools.py* sotto: decidere re-sync da `metodo` vs patch mirata.
7. **Skill `audit-kb`** (`.claude/skills/audit-kb/SKILL.md` + wrapper `.codex`) — aggiornare il
   riferimento `--append-log` → `--append-why`.

### Nota — Sync di kb_tools.py
Le copie locali differiscono per dimensione dalla `metodo` (evoluzione locale): **non**
sovrascrivere ciecamente. Due opzioni, da decidere in sessione: (a) cherry-pick delle tre
modifiche del passo 6 sulla copia locale (conservativo, preferito se la copia ha logica di
dominio); (b) re-sync completo da `metodo/scripts/kb_tools.py` se la copia locale era solo
indietro. Verificare con un diff prima di scegliere.

---

## Parte B — giudizio di dominio (richiede il contesto locale)

8. **`map.md` in root — l'o2 del dominio.** È il passo che giustifica la sessione dedicata. Né
   economia né salute hanno un nodo `kb/mappa.md` con quel nome esatto: `map.md` va *composto*
   come vista o2 concisa di bootstrap del modello di dominio (non inline nel README, per pace).
   Attingere al modello di dominio già esistente (nel README, in un root file, o nell'o-layer
   locale `output/`/`quadro/`) senza duplicarlo: `map.md` è la versione di bootstrap, la fonte
   ricca resta dove sta. Mantiene il passo `README → map → CLAUDE → nodo`.
9. **Cosa sale in root (punto 4 della triade).** Il set universale README/map/plan/CLAUDE/
   AGENTS/why è un *pavimento, non un soffitto*. Confermare i file bootstrap di dominio già in
   root con lo stesso criterio di altezza (economia: `stato.md`, `scadenze.md`, `diario.md`;
   salute: `scadenze.md`, `diario.md` — **niente `stato.md`**). Non aggiungerne di nuovi senza
   un'esigenza dal basso; non rimuovere quelli esistenti senza motivo.
10. **README alleggerito** — resta lo strato lento (identità, principi, dominio, come orientarsi)
    e *punta* a `map.md`, `plan.md`, `kb/index.md`. Escono l'indice dei nodi e la tabella task.

---

## Verifica (gate, prima del commit)

- `python3 scripts/kb_tools.py audit` → **0 link rotti** (come nixos/bi/metodo).
- `python3 scripts/kb_tools.py readme` → catalogo `kb/index.md` coperto.
- grep residui: nessun `log\.md`, `todo/`, `task-aperti`, `mappa\.md`, `append-log` nel repo
  (esclusa `tasks/` storica e `.git`).
- **Prima entry di `why.md`**: il perché della migrazione del layout in *questo* repo, con
  puntatore al commit `metodo@be14bf3` e all'entry `why.md` del metodo. La fondazione del file
  scritta nel file che la migrazione ha ribattezzato.
- Commit in-repo: `refactor(layout): allinea al cruscotto del metodo` (come nixos/bi). **Push
  mai automatico.**

---

## Schede per-repo (recon 2026-06-06)

### economia
- root `.md`: AGENTS, CLAUDE, **diario**, **log**, README, **scadenze**, **stato** → ha `stato.md`.
- `kb/`: nessun `mappa.md`/`indice.md`/`index.md` con quei nomi esatti → `map.md` e `kb/index.md`
  sono composizione (passo 8/4), non rinomina.
- o-layer locale: `output/`. `config/`, `src/`, `data/` = il «mondo» del dominio (fuori dalla
  competenza-layout del metodo).
- `scripts/kb_tools.py`: copia locale (≈24 KB) → passo 6 + nota Sync.
- `--append-log` in: `scripts/kb_tools.py`, `.claude/skills/audit-kb/SKILL.md`.
- referenze `log.md`/`todo/` in: `CLAUDE.md`, `README.md`.
- ⚠️ verificare `memory/` (possibile residuo dello store harness, anti-pattern per il `CLAUDE.md`
  del repo stesso): segnalato già nel disegno originale, valutarne la rimozione in sessione.

### salute
- root `.md`: AGENTS, CLAUDE, **diario**, **log**, README, **scadenze** → **niente `stato.md`**.
- `kb/`: nessun `mappa.md`/`indice.md`/`index.md` esatto → `map.md`/`kb/index.md` da comporre.
- o-layer locale: `quadro/` (i numeri = i2, il termometro/colore = i3, vedi [[output]] e
  `confronto-progetti-adottanti`). `tech/`, `fonti/`, `_plug/` = struttura di dominio.
- `scripts/kb_tools.py`: copia locale (≈19 KB) → passo 6 + nota Sync.
- `--append-log` in: `scripts/kb_tools.py`, `.claude/skills/audit-kb/SKILL.md`.
- referenze `log.md`/`todo/` in: `CLAUDE.md`, `README.md`.
- nota: i nomi-file accentati di salute (`realtà.md`, `qualità.md`, …) sono decisione locale
  consapevole (KB riflessiva italiana), **non** drift da «correggere» nella migrazione.

---

## Filing back

Se durante l'esecuzione su economia/salute emerge una generalizzazione portabile (un passo di
Parte A che andrebbe stabilizzato, o un criterio nuovo sulla root estensibile), riportarla in
[[struttura-progetto]] e aggiornare questo runbook. Quando entrambi i repo sono migrati e
verificati, questo task si chiude: la riga sparisce da `plan.md`, lo storico resta in git e in
`why.md` (di ciascun repo e del metodo).
