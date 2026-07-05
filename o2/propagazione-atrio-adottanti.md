---
sintesi: "La prescrizione della ristrutturazione dell'atrio è attiva (o3/ristrutturazione-atrio.md). Recepita da nixos (rebuild reale), economia (a0538f5) e salute (9f997c8, il suo coccio ha corretto il link checker del canone). Resta solo bi, lo stress-test del fit: il task chiude quando anche bi l'ha recepita per intero."
ciclo: runtime
---

# Recepimento della prescrizione dell'atrio

## Stato

La ristrutturazione dell'atrio (2026-07-04) è la prima divergenza strutturale
del canone dalla forma che i quattro adottanti conoscono. La prescrizione che la
propaga è scritta e attiva: [`o3/ristrutturazione-atrio.md`](../o3/ristrutturazione-atrio.md)
— runbook unico nel lessico del metodo con touchpoint per-repo (la ricetta è
identica in forma per tutti; divergono solo _quali_ file esistono, cfr.
`o3/prescriptions.md`, «Divisione del lavoro»). Include il risync del fork del
cluster presentazione alla home semplificata (cfr. filo `i3/home-minimalista.md`).

Ogni adottante la recepisce col proprio `/method-review` come task locale: il
canone dichiara, la coda resta dell'adottante (`method-development`, «dichiara e
taci»).

## Recepimento

- `nixos` — **recepito** (pilot, 2026-07-05): migrazione strutturale completa
  via `/method-review` (marker a `0f74186`, `status: aligned`, ri-esecuzione
  idempotente); i due cocci del pilot (risync `kb_tools.py`; facet su item, non
  su indici) sono incisi nel runbook (`9033223`). Il passo 1 ha poi corretto il
  canone: non basta dichiarare il corpo di dominio in root; bisogna spostare il
  contenuto versionato negli spazi funzionali. Nixos lo ha eseguito spostando
  `home/`, `hosts/`, `modules/`, `identity/`, `patches/` e `scripts/` sotto
  `o3/` come o3-runtime; `flake.nix`/`flake.lock` restano eccezioni di
  toolchain; `secrets/` resta eccezione non versionata/materia del Mondo;
  `result*`, `world` e cache sono traffico runtime gitignored.
- `bi` — da eseguire; è il caso più costoso dell'inventario e il suo verdetto
  di fit il più informativo per l'osservatorio: i contenuti versionati vanno
  ricollocati, non solo classificati
- `economia` — **recepito** (2026-07-05, commit `a0538f5`, marker a `77d8225`,
  `status: aligned`): ricollocazione completa (strumenti, script, libreria,
  config e test → `o3/`; viste → `presentation/`; legenda dell'atrio estesa
  all'`ls -A`; verdetto di fit 0 eccezioni), audit/facet/tasks puliti, viste
  rigenerate, working tree pulito. I quattro cocci del secondo giro — i3 a
  file-per-filo (non indice-wrapper sul monolite), un solo indice per
  collezione, dotfile in legenda, chiusura solo col commit via gate — sono
  incisi nel runbook (`97c4571`) e chiusi in loco prima del commit; rimosso
  anche il symlink `memory` (anti-pattern del canone, store vuoto). Il marker
  è un commit indietro rispetto a `97c4571`, che incide i suoi stessi cocci:
  il prossimo `/method-review` lo avanza come `gia-soddisfatto`.
- `salute` — **recepito** (2026-07-06, commit `9f997c8`, marker a `1a79a65`,
  `status: aligned`): migrazione chiusa in sessione con commit unico e working
  tree pulito — collezioni-stadio, verdetto scisso reale a file-per-filo,
  `tools.md` soppresso in `prescriptions.md` (forma preferita), legenda su
  `ls -A`, facet su 31 item, 197 nodi tutti indicizzati, sette divergenze
  intenzionali registrate. Il suo coccio ha corretto il canone per tutti: il
  link checker contava rotti i cross-link validi al canone via symlink
  (`fix` in `1a79a65`, inciso al passo 2 del runbook). Unico residuo
  informativo il `[CLUSTER-ISOLATO]` sulle fonti i1, isolato per natura
  (le catture sono foglie), non per drift.

## Chiusura

Recepita da tutti e quattro, la prescrizione si rimuove da `o3/` e questo task
chiude con lei; la storia resta in git.
