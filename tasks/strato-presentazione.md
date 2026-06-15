---
data: 2026-06-15
stato: aperto
---

# Strato di presentazione trasversale (deck → view)

Aperto in sessione di design 2026-06-15, allargando lo scope della system image
visiva (cfr. `verdict.md`, filo «Rifondazione atrio↔azione»). Il nodo `deck`
confonde due cose: il **motore di presentazione** (come si rende navigabile una
vista — HTML/CSS nativi, Reveal, apertura `file://`, build) e la sua **istanza**
(la cartella `interpretations/`). Le scindiamo: il motore sale a **strato di
presentazione in root**, trasversale agli stadi; le sue istanze diventano
molteplici — una vista navigabile per ogni collezione che la merita.

## Decisioni

- **Rinomina `kb/deck.md` → `kb/view.md`**, con broadening del concetto: da
  «deck di slide delle interpretazioni» a «motore di viste navigabili derivate»,
  a istanze multiple. La propagazione (rename = aggiornare i link negli
  adottanti) è resa quasi gratuita dal task disaccoppiamento, che lo precede e
  ripulisce i riferimenti prima.
- **`interpretations/` e `tasks/` tornano sorgenti pure** (solo `.md` + indice),
  twin tra loro: `interpretations.md` e `plan.md` ne sono gli indici.
- **Macchina di presentazione consolidata in root**:
  - `assets/` — CSS condivisi (palette + classi-diagramma, oggi in
    `interpretations/reveal.css`) e, se si vuole l'offline, Reveal vendorizzato;
  - `views/` — gli HTML **generati** per-stadio (`views/interpretations.html` =
    il deck attuale; in futuro `views/tasks.html`, ecc.);
  - `index.html` in root — la home/atrio visivo, entry navigabile (task
    system-image, che dipende da questo).
- **`views/` è una specie nuova nell'atrio**: artefatti di presentazione
  _generati_, distinti da file-ciclo / cataloghi trasversali / register /
  collezioni-stadio (che sono sorgenti). Da nominare in `project-structure.md`.
- **Versionare gli HTML generati** (non gitignore): preserva l'affordance
  `file://` «doppio click dal checkout» che `view.md` eredita da `deck.md`
  (emersa dal basso in `bi`). Si accetta il churn di rigenerazione.
- **Reveal**: la home non lo usa (statica, offline). Solo le viste-deck lo
  caricano. Vendoring in `assets/` solo se serve l'offline del deck; altrimenti
  CDN come oggi.

## Vincoli ereditati (non negoziabili)

- apertura `file://` dal checkout senza build/servizi/`fetch` di file locali
  (`deck.md:29-31`, `49-53`): i `<link>`/`<script src>` relativi cross-cartella
  funzionano, `fetch` no;
- vista derivata, mai seconda fonte: ogni vista si genera da sorgenti
  (`README`/`plan`/`verdict`/`tasks`/`interpretations`/`kb`/`git`), non ne ospita
  copia.

## Implementazione

1. `kb/view.md` — rinomina da `deck.md`, riscrittura: motore trasversale,
   istanze multiple, macchina in root (`assets/` + `views/`), invariante
   `file://`, sorgenti pure nelle collezioni.
2. `kb.md` — aggiorna la riga di catalogo deck→view.
3. backlink — aggiorna i nodi che linkano `deck.md` (`output`, `action-cycle`,
   `cognitive-fidelity`, `processing-layers`, `karpathy-pattern`,
   `project-structure`, `verdict`) al nuovo target `view.md`.
4. `kb/project-structure.md` — nuova specie «artefatti di presentazione
   generati» (`index.html`, `views/`, `assets/`); twin sorgenti pure; skeleton e
   naming aggiornati.
5. struttura fisica — crea `assets/` (sposta `interpretations/reveal.css` →
   `assets/`), crea `views/`, sposta `interpretations/index.html` →
   `views/interpretations.html`; aggiorna `tools/build-presentation.sh` ai nuovi
   path.
6. riferimenti — aggiorna README/CLAUDE/AGENTS/`tools.md` e la sorgente del deck
   dove citano `deck` o `interpretations/index.html`.
7. propagazione ai 4 adottanti — eseguita **dopo** il task disaccoppiamento, che
   riduce i riferimenti negli adottanti prima: a quel punto il rename costa poco
   o nulla per i repo già ripuliti.

## Orizzonte (non in questo task)

- `views/tasks.html`: i task come slide navigabili (data di creazione, data di
  modifica da git, titolo, urgenza da `plan`, sintesi) — forma viscerale di o2;
  arriva dopo che lo strato esiste.
- finestra-terminale per dialogare col modello: **rompe l'invariante `file://`**
  (richiede backend servito). Classe diversa, nodo a sé, deliberatamente fuori
  dallo strato di presentazione statico.
