---
data: 2026-08-01
stato: attiva
ciclo: runtime
target: nixos (pilota montaggio per primo), salute, economia, bi
---

# La rifilatura per arco: `plan-review`/`verdicts-review` → `exec`/`eval`

## Cosa e perché

Il quartetto operativo si ritaglia lungo il modello invece che lungo la storia
della sua crescita (ratifica 2026-07-31/08-01, filo
`i3/skill-per-arco-tripartito.md`, canone in `kb/skill.md`): `plan-review` e
`verdicts-review` diventano **`exec`** ed **`eval`**, ciascuna coi tre stadi
del proprio arco come scope —

- `eval [perceive|interpret|compare|all]` — il braccio di valutazione
- `exec [plan|specify|perform|all]` — il braccio di esecuzione

Le due ragioni del cambio di regola dei nomi: la **copertura** (una skill che
mantiene tre indici non può portare il nome di uno solo, e gli stadi
degradati — i1, i2, o3 — erano esattamente quelli che nessun nome nominava) e
il **telos inglese** (le canoniche fanno da avanguardia della migrazione).
Niente si butta: le procedure esistenti si rifilano sotto il loro stadio, e
si guadagna la casa per ciò che non ne aveva. Il quartetto resta un
quartetto: due archi, un'ala (`kb-review`), un gate (`commit`). Pilotato in
`metodo` (2026-08-01, due giri: end-to-end e battito `/adopters-review`).

## La ricetta (nel lessico del metodo)

1. **Forka `eval` ed `exec` dal canone** (`method/.claude/skills/eval/`,
   `.../exec/`, wrapper Codex corrispondenti) e **rifila a diff contro il tuo
   fork corrente**: ogni parametrizzazione locale delle due vecchie skill
   (segnali di dominio, esempi, passi aggiunti) migra sotto lo stadio che le
   compete nel canovaccio nuovo — non si copia il canone perdendo l'ultimo
   miglio. Gli scope-stadio sono riservati e hanno semantica identica in ogni
   repo; il default è `all`; ogni stadio può chiudere in una riga.
2. **Rimuovi `plan-review` e `verdicts-review`** (`.claude/skills/` e
   `.codex/skills/`) **dopo** che il contenuto locale è stato rifilato, non
   prima.
3. **Quinta domanda**: se la prescrizione `quinta-domanda-verdetti` non è
   ancora recepita, il fork di `eval` la porta già dentro (`compare`, cinque
   domande): recepirla qui chiude anche quella per questo repo — dichiaralo
   nel marker.
4. **Bussole e consumatori**: l'elenco skill di `CLAUDE.md`/`README`, le
   righe `## Scadenze` che citano le skill per nome, e le skill di dominio i
   cui handoff citano la coppia (`posta` e `registrazioni` in `economia`).
   Fai un grep e classifica: normative e operative si migrano, i fili storici
   conservano il nome che descrive il fatto passato.
5. **Recepimento ordinario**: canale `method-review`, marker avanti dopo la
   classificazione.

## Il montaggio di dominio: esperimento sequenziale, non esito deciso

La ricognizione della flotta (2026-08-01, matrice in
`o2/skill-archi-tripartite.md` di `method` finché il task è aperto) suggerisce
che le skill di dominio non siano tutte atti da appendere a `perform`: si
distribuiscono sui sei stadi e su entrambi gli archi. È **ipotesi da
pilotare**, nell'ordine **`nixos` → `salute` → `economia` → `bi`** — dal caso
multi-scope collaudato al più complesso. Ogni pilota decide esplicitamente,
per ciascuna skill: **assorbita** come argomento delle canoniche
(`eval finanze`, `exec ordini <fornitore>`), **divisa** fra i due archi, o
**mantenuta autonoma**. I risultati correggono questa prescrizione; solo le
forme provate risalgono a canone. Le collocazioni candidate:

- **`nixos`** — `aggiorna`: `eval aggiorna` per i rami diagnostici ed
  `exec aggiorna` per `ia`, oppure autonoma se il doppio montaggio attrita;
  questione del pilota: una capacità può abitare due archi senza mentire nel
  signifier? `nix-overlay-update` candidata a retrocedere a runbook `o3/`.
- **`salute`** — `elabora-trascrizione` → `eval trascrizione`; questione: la
  distillazione produce grezzo catturato o già una sintesi? Qui si normalizza
  anche il frontmatter di vecchio stile.
- **`economia`** — `finanze-review` → `eval finanze` (arco intero); `posta` e
  `registrazioni` → `eval posta`, `eval registrazioni` (canali `perceive`);
  questione: l'argomento conserva un handoff leggibile verso `exec plan`? un
  canale event-driven non diventi passaggio rituale.
- **`bi`** — `categorizza`/`tassonomia` → `exec categorizza`,
  `exec tassonomia` (`perform` con guardrail «solo lo script scrive»);
  `ordini <fornitore>` → `exec ordini` (arco intero, ratifica umana al
  confine): il caso più delicato, per ultimo.

L'autorizzazione segue le risorse dello scope, non la skill: lo stesso arco
può essere esecutivo su un ramo e diagnostico su un altro.

## Ordine e chiusura

La **rifilatura** (passi 1-5) si recepisce in qualunque ordine, al prossimo
`method-review` di ciascuno. Il **pilota del montaggio** è sequenziale
(`nixos` per primo) e vive nelle code locali: questa prescrizione non
inserisce task — la decisione di quando pilotare è dell'adottante, l'ordine
fra adottanti è del custode. La prescrizione resta attiva finché i quattro
non hanno recepito la rifilatura; gli esiti del montaggio la correggono
strada facendo. Recepita da tutti, si rimuove dalla collezione — la storia
resta in git — e in `method` si sveglia il task `pause` di rivalutazione
della clausola di uscita (terzo battito `/adopters-review` successivo).
