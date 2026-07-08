---
ciclo: dev
---

# Il polo World è reso fedele dal README, senza card

Segnale d'origine: `salute`, allineando la home al canone di presentazione
(`i1/home-world-readme-driven.md`). Quando la home ha smesso di decorare il World
con card hardcoded nel builder e ha iniziato a **leggere** `### World` dal README,
la sezione è diventata un contratto: il testo di pipeline che vi era rimasto
(`world/`, `i1/`, `i2/`, `map.md`) è finito visibilmente nel polo World. L'errore
non era nel builder ma nel README.

Verdetto ratificato: **il builder resta stupido e fedele**. Prende il blocco
markdown sotto `### World` (e `### Goal`) e lo rende come markdown→HTML — una
bullet list resta bullet list, la prosa resta prosa, un misto resta misto.
Nessuna card, nessuna resa strutturata, nessuna euristica per repo. Tutta la
libertà di forma passa al README, che è dominio dell'adottante.

Questo scioglie il criterio «forma del World → resa» che la percezione lasciava
aperto (card se lista di entità, testo se prosa): non c'è più niente da decidere
lato builder. Di conseguenza **`method` e `nixos` perdono le card** nel polo
World — adottanti e host diventano bullet list markdown. Non erano casi speciali:
una lista markdown resa fedelmente _è già_ la loro rappresentazione.

Il canone è inciso in `kb/readme.md`: `### World` è la **visione del Mondo che
l'artefatto tiene** (non l'inventario delle fonti), può crescere in prosa anche
dentro una lista, e la membrana/pipeline non vi appartiene — sta nelle sezioni
operative o nei nodi.

Propagazione ai builder — **chiusa** su tutti e cinque i repo. Il renderer
condiviso (`inline_markdown`/`render_block`/`render_markdown`, con `link_prefix`
per correggere i link relativi dalla home) è identico nelle cinque fork di
`build_system_image.py`; ognuna chiama `render_markdown(sezione, "../")`.

- `salute` — pilota: World misto (prosa + lista `corpo`/`mente` + prosa). La
  lista minima mette in scena la tesi non-dualista del progetto — nomina i due
  versanti e la prosa li rifonde («due nomi per una cosa sola»).
- `economia` — rimosso il dict `WORLD` hardcoded (era membrana: `world/`, `i1/`,
  `map.md`) e la coda di pipeline dal `### World`; ora prosa dal README.
- `bi` — via `first_paragraph` (troncava a 400, non rendeva l'inline) → render
  fedele; tolta dal `### World` la frase su membrana e register.
- `nixos` — host come **bullet list** nel `### World` (scelta ratificata); il
  dettaglio hardware resta in `## Host`. Il builder non legge più `## Host`.
- `method` — adottanti come bullet list con link (non più card né URL GitHub
  ricostruiti); `link_prefix` risolve `../nixos/` → `../../nixos/` dalla home.

Watchpoint residui (cosmetici): la duplicazione nome+ruolo host tra `### World`
e `## Host` di `nixos` è voluta (sintesi vs dettaglio). Il residuo CSS nato in
`economia` non resta come eccezione locale: il canone ora pota
`system-image.css` al set vivo della home minimalista, quindi `world-grid` e
`world-item` non appartengono più al contratto condiviso.
