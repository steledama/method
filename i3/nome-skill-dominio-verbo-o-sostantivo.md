---
ciclo: dev
---

# Il nome di una skill è sostantivo, non verbo imperativo

Ratificato (custode, 2026-08-01) dalla percezione «il nome di una skill di
dominio è verbo o sostantivo?» (nixos, consumata qui): **il sostantivo vince**,
sia per le skill di dominio sia per i composti canonici in `-review`.
L'imperativo ripetuto a ogni invocazione suona da comando più che da nome di
capacità; generalizza il criterio già in canone per `monthly-review`→
`finanze-review` («l'oggetto tenuto onesto, non l'azione»). La rilevazione che
ha preceduto la decisione — tabella verificata contro l'`ls` reale di
`.claude/skills/` nei cinque repo, non contro le fotografie — vive in
[o2/skill-nomi-verbo-sostantivo.md](../o2/skill-nomi-verbo-sostantivo.md), che
porta anche il lavoro di rename/propagazione. Il corollario con gli esempi è
inciso in `kb/skill.md`, «La regola dei nomi».

**Due assi restano indipendenti**, e la regola tocca solo uno dei due: il
doppio rename di nixos nello stesso giorno (`aggiorna`→`manutenzione`,
sostantivo; `nix-overlay-update`→`aggiorna-overlay`, ancora verbo ma solo per
lingua inglese→italiano) mostra che lingua e classe grammaticale non sono la
stessa mossa. La regola qui ratificata decide solo la seconda; non elimina le
rinomine future, elimina l'oscillazione su questo asse specifico.

## Casi decisi

- **`categorizza` (bi) resta `categorizzazione`**: già sostantivo, non
  `categorie` — collisione evitata con `tassonomia`, che già custodisce
  «marche/categorie» come struttura; `categorizzazione` nomina l'atto di
  smistare i fornitori dentro quella struttura, non la struttura stessa.
  Nessun cambio da applicare.
- **`kb-review` (canone) → `kb`**: il nome combacia con la cartella che
  audita, stesso pattern di `eval interpret` → `i2/`. Canonica, identica nei
  cinque repo: richiede l'incisione in `kb/skill.md` (fatta) e una
  prescrizione `o3/` per la propagazione. `commit` la invoca già
  condizionalmente (`commit/SKILL.md:12`): l'invito diventerà "Vuoi eseguire
  /kb prima del commit?".
- **`method-review` (canone) → `method`**: stesso principio. La possibile
  ambiguità con il nome del repo `metodo` non tiene: il repo cambierà nome in
  futuro (verso qualcosa di più "commerciale"), quindi non è un vincolo
  stabile su cui appoggiare il nome della skill. Canonica, stessa
  propagazione di `kb`.
- **`adopters-review` (metodo) → `adottanti`**: stesso principio; a
  differenza delle due sopra è **locale a `metodo`** — non si forka (il suo
  Mondo sono gli adottanti stessi), quindi nessuna propagazione.
- **`aggiorna-overlay` (nixos) → `overlay`**: stesso principio, locale a
  nixos, nessuna propagazione.

Nessun caso resta aperto: i cinque nomi bersaglio sono decisi. Il lavoro di
rename delle cartelle vive e — per i tre casi canonici — la prescrizione di
propagazione sono nel task
[o2/skill-nomi-verbo-sostantivo.md](../o2/skill-nomi-verbo-sostantivo.md),
handoff a `exec`.
