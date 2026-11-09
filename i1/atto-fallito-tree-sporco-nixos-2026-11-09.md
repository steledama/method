---
ciclo: runtime
---

# Segnale: un atto del giro fallito senza effetti blocca i giri seguenti

Data: 2026-11-09 · Fonte: messaggio inoltrato dalla sessione `nixos` su
`deck`, su richiesta del custode; diff di `nixos` `8167598` e `f612c91`, di
`nixos-lavoro` `b80b3b9`

## Il segnale

Il giro del 2026-11-09 di `nixos` ha fatto il bump dell'input `ai` e lo
switch è fallito in build per un guasto upstream (codex 0.167.0,
NixOS/nixpkgs #585124). Il prompt diceva «niente commit, working tree com'è».
`deck` è rimasto intatto, ma il tree sporco avrebbe fermato il giro seguente
col codice 10 e bloccato le correzioni di testo degli altri stadi. Il guasto,
emerso in `perform` dopo `compare` e `plan`, stava solo nel resoconto e nello
stream, non nel repo.

Nella stessa notte, in sessioni distinte, i due repo hanno scritto la stessa
regola: l'atto si ritira, il lock torna a `HEAD`, il ramo non si registra e
resta dovuto, il resto del giro si committa, il guasto va nel corpo del
commit e in `Attenzione:`.

## Le differenze

- **Quando si ritira.** `nixos`: solo se la build fallisce prima
  dell'attivazione e del bump è cambiato solo `flake.lock`; altrimenti tree
  com'è. `nixos-lavoro`: a ogni switch fallito, restaurando il solo lock, così
  gli adeguamenti fatti per il bump resterebbero e finirebbero nel commit.
- **Il controllo dopo il ritiro.** `nixos`: `home-drift.sh` deve dare
  `allineato`, il confronto con la generazione di `HEAD`. `nixos-lavoro`:
  `home-manager generations`, generazione invariata.
- **L'attesa.** `nixos` ha provato e tolto un'attesa nel piano
  (`o2/bump-ia-dopo-fix-codex.md`, cancellato da `f612c91`): col ritiro il
  tentativo di ogni notte si ripara da solo, l'attesa chiedeva uno sblocco
  manuale. Il costo del ritentare è misurato su una notte sola.

## Limite della prova

I due repo non sono indipendenti: `nixos-lavoro` è separato da `nixos` dal
2026-11-04, incidente e skill `manutenzione` sono gli stessi. Gli altri prompt
di giro controllati su `deck` (`baserow`, `bi`, `danea-auto`, `economia`,
`method`, `salute`) non hanno una regola sull'atto fallito.

## Rilievo sul lanciatore

Il messaggio segnala che `push: true` in `tentativi.jsonl` significa solo HEAD
uguale a `@{u}`, e compare anche in un giro senza commit. `o3/lanciatore.py`
aveva la stessa semantica; l'unica logica che usa il campo,
`o3/view/ciclo.py`, è protetta da `commit`.

## Stato

Recepito il 2026-11-09 col custode: principio nella skill `cycle`,
meccanismo nei prompt dei repo, `push` nullo nei giri senza commit. Resta
aperto `nixos-lavoro`, che ritira anche quando il bump ha toccato altri file.
Si chiude quando quel fork restringe la condizione.
