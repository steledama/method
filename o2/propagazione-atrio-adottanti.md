---
sintesi: "La ristrutturazione dell'atrio (2026-07-04) è la prima divergenza strutturale del canone dalla forma che i quattro adottanti conoscono. Il risultato atteso è la prescrizione o3 — il runbook che ogni adottante esegue col proprio method-review — che li porta alle collezioni i1/–o3/, al catalogo kb/kb.md, agli strumenti di sviluppo in o3/ e a presentation/: propagazione progettata, non lasciata al drift."
ciclo: runtime
---

# Prescrizione di propagazione dell'atrio agli adottanti

## Problema

Con la ristrutturazione dell'atrio il canone descrive una struttura che nessun
adottante ha ancora: collezioni-stadio `i1/`–`o3/` coi loro indici, catalogo
`kb/kb.md`, verdetto a fili in `i3/`, strumenti di sviluppo in `o3/`,
`presentation/`, facet `ciclo: dev|runtime` sugli item di collezione. Gli
adottanti leggono i nodi via symlink: ogni loro sessione legge
`project-structure` e gli altri nodi strutturali che contraddicono l'albero
locale. È la prima divergenza **strutturale** (non additiva) del canone; senza
una prescrizione, si chiude per drift — ogni repo migrerebbe a modo suo, o non
migrerebbe affatto.

## Risultato atteso

Una prescrizione in `o3/`, registrata in `prescriptions.md`, che ogni adottante
recepisce col proprio `/method-review` come task locale (il canone dichiara, la
coda resta dell'adottante — cfr. `method-development`, «dichiara e taci»). Il
runbook copre, per repo:

- rinomina delle collezioni nella forma `i1/`–`o3/` con gli indici interni
  (`perceptions.md`, `interpretations.md`, `verdicts.md`, `plan.md`,
  `tasks.md`, `prescriptions.md`) e collocazione-per-funzione dei file di
  dominio (`diario`→`i1/`, `stato`→`i2/`, `scadenze`→sezione di `o1/plan.md`);
- catalogo `kb/index.md`→`kb/kb.md`; verdetto scisso in fili `i3/`;
- strumenti di **sviluppo** in `o3/` (gli `scripts/` di dominio restano
  o3-runtime, cfr. `project-structure`);
- superficie presentativa in `presentation/` dove esiste;
- facet `ciclo: dev|runtime` nel frontmatter degli item di collezione;
- forma `plan.md`: colonne `Ciclo · Task · Dip.` (canone 2026-07-04);
- frontmatter dei task senza `stato:` (soppresso 2026-07-04, cfr. `tasks`):
  restano `sintesi` e `ciclo`;
- aggiornamento dei path nei `CLAUDE.md`/`README.md` locali che puntano a
  collezioni interne del metodo.

## Decisioni aperte

- prescrizione unica parametrizzata o un runbook per repo (il round baricentro
  usò runbook per repo); ordine suggerito: partire dal repo a coda piccola
  (`nixos`) come pilot;
- se il fork del motore della home (`build_system_image.py` + CONFIG, cfr.
  filo `i3/home-16-slot.md`) viaggia nella stessa prescrizione o in una
  successiva.

## Riferimenti

- filo `i3/ristrutturazione-atrio.md` (chiuso con questa pianificazione; storia
  in git) — le decisioni ratificate e i cocci raccolti
- `kb/project-structure.md`, «Applicazione nei progetti adottanti» — i target
  di migrazione per funzione
