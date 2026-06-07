---
data: 2026-06-07
stato: aperto
---

# README come bussola: ritiro di `map.md`, scomposizione della mappa

Aperto il 2026-06-07. Un unico refactor che istituzionalizza in modo rigoroso la
regola **«il README orienta e punta, non immagazzina»** e ne dà sostanza concreta
ritirando `map.md` come file separato. Parte da `metodo` (prototipo) e si propaga
ai quattro adottanti.

## La decisione

Supera la regola del 2026-06-06 «`map` resta separato dal README per pace» (vedi
`why.md`, gruppo «cruscotto del ciclo» e `struttura-progetto`). Quella decisione
trattava "map" come **una cosa sola** (il modello che evolve). Oggi la scomponiamo
in **tre funzioni**:

- **bussola** (orientamento: cosa fa il progetto, obiettivi, principi, _dove_ sta
  ogni cosa) → stabile → **vive nel README**
- **modello del dominio** (la teoria che evolve) → vive già nei nodi `kb/` e in
  `presentations/`; il README ci _punta_, non lo copia
- **indice-di-dominio** (il territorio reale: host/entità/sistemi → nodi) → il
  register **`map.md`** (porta-collezione, on-demand), presente dove il dominio ha
  un territorio da mappare

La pace del 06-06 è rispettata meglio: lo strato veloce (il modello) resta fuori dal
README; nel README entra solo la bussola, che è stabile.

## La regola istituzionalizzata

**Il README è la bussola dell'artefatto: orienta e punta, non immagazzina.**

- contiene: sintesi del dominio/scopo, obiettivi, principi guida (in sintesi),
  orientamento operativo (dove vivono strumenti, output, fonti, catalogo, lavoro,
  ragioni) così che umano e LLM abbiano la visione d'insieme e sappiano dove trovare
  viste di portata minore o info puntuali
- non contiene: il modello del dominio, il catalogo dei nodi, i principi _estesi_,
  procedure/flag/troubleshooting, teoria del metodo → tutto questo vive nei nodi
  (es. `design-principles`), nei register e in `presentations/`; il README _punta_
- principi guida ed obiettivi, quando estesi, sono un nodo `kb/`: il README li sintetizza e rimanda

## Naming unificato

Un solo nome per l'indice-di-dominio: **`map.md`** (root, porta-collezione),
coppia register/concetto con `kb/map.md` come per `kb`/`plan`/`why`. Uccide il drift
`project-map.md` (nixos/bi) vs `mappa-progetto.md` (economia/salute).

## Bootstrap

`README → map → CLAUDE → nodo` diventa **`README → CLAUDE → nodo`**: `map` esce dal
bootstrap perché è una porta on-demand, non un file-ciclo. La bussola (README) punta
a `map` quando esiste.

## Stato e propagazione

- [x] **metodo (prototipo)**: README-bussola; `map.md` ritirato (dominio astratto,
      modello in nodi+presentations); `kb/readme.md` regola rigorosa; `kb/map.md`
      ri-mirato sul register-territorio; bootstrap `README → CLAUDE → nodo`;
      `struttura-progetto`/`metodo-kb`/`kb.md`/`CLAUDE`/`AGENTS` allineati; 06-06 segnato
      superato in `why.md`.
- [ ] **nixos**: README-bussola; `kb/project-map.md` → `map.md` (root register);
      bootstrap.
- [ ] **bi**: come nixos.
- [ ] **economia**: README-bussola assorbe il modello dell'attuale `map.md` root;
      `kb/mappa-progetto.md` → `map.md` (root register); bootstrap.
- [ ] **salute**: come economia.

## Questioni aperte da risolvere in propagazione

- **backlink alla promozione**: `kb/project-map.md` ha 8 backlink in nixos (1 in bi);
  promuovendolo a `map.md` root vanno ripuntati o accettati come link nodo→register.
  Decidere la semantica dei `Connessioni:` verso un register.
- verificare che il README di economia/salute assorba il modello senza gonfiarsi
  (lì non c'è un `presentations/` ricco come in metodo).
