---
sintesi: "Gli strumenti che leggono gli adottanti (adottanti.py e prescrizioni.py) presuppongono che method osservi tutti dal proprio world.md, anche via ssh. Nel modello dei gruppi guardare i membri è compito del coordinatore: gli strumenti prendono --root e leggono il world.md dell'istanza, method perde audit e ssh, ingresso e osservatorio si riscrivono sul coordinatore."
ciclo: runtime
---

# Strumenti del coordinatore

## Origine

Aperto il 2026-11-23 dal custode, sulla domanda di `nixos` dopo che è
diventato coordinatore del gruppo casa: `adottanti.py` accetta una radice, come `build.py` e `kb_tools.py`, o che cosa ne resta
per i gruppi, ritirato `/adottanti`? Raccoglie i residui del ritiro, prima
nel task [canale-in-entrata](canale-in-entrata.md).

## Stato di partenza

- `o3/adottanti.py`: legge gli adottanti dal `world.md` di `method`, li trova
  per remote fra i cloni della home o via `ssh`; sottocomandi `stato`, `log`,
  `show` e `audit`, quest'ultimo la parte meccanica del `/adottanti`
  ritirato. `o3/skill_tools.py` lo importa per la classifica delle skill.
- `o3/prescrizioni.py`: verifica e chiude una prescrizione sui marker di
  tutti gli adottanti, anche via `ssh`. Dal 2026-11-23 per un adottante
  mantenuto da altri fa fede la versione dichiarata
  (`kb/method-development.md`, «Versioni»).
- `o3/ingresso-adottante.md` e `kb/method-observatory.md` descrivono
  `method` come osservatore che fa entrare e misura gli adottanti.

## Proposta

- **`--root` per gli strumenti di gruppo**: `adottanti.py` legge i membri dal `world.md` dell'istanza indicata (la sezione
  `## Membri`, la stessa del sito di gruppo), così `nixos` li lancia sul
  gruppo casa e `nixos-lavoro` sul gruppo lavoro. Senza `--root` vale
  `method`.
- **Via da `method` l'audit e l'ssh**: il sottocomando `audit` e la lettura
  via `ssh` si tolgono; l'ssh, se serve, resta al coordinatore che ha i
  membri su un altro host (`nixos-lavoro` e `danea2`).
- **`prescrizioni.py` verifica solo i repo del custode**; per gli altri la
  chiusura segue la versione.
- **Ingresso e osservatorio**: l'ingresso di un membro diventa una procedura
  del coordinatore; `kb/method-observatory.md` passa da audit a lettura dei
  contributi (issue e PR) e a ciò che i coordinatori riportano.
- **`world.md` di `method`**: gli adottanti di lavoro restano come voce del
  territorio, non come checkout da leggere.

## Passi

1. `--root` e lettura di `## Membri` in `adottanti.py`, coi test.
2. Togliere `audit` e `ssh` da `adottanti.py` e `prescrizioni.py`;
   `prescrizioni.py` sulla regola della versione.
3. Riscrivere `o3/ingresso-adottante.md`, `kb/method-observatory.md` e la
   parte di `world.md` sugli accessi ssh.
4. Rilascio con le note: chiede qualcosa ai coordinatori, quindi una minor.

## Criterio di chiusura

`nixos` lancia gli strumenti sul gruppo casa con `--root`, `method` non legge
più nessun adottante via `ssh`, e osservatorio e ingresso descrivono il
coordinatore.

Connessioni:

- [canale-in-entrata](canale-in-entrata.md)
- [method-observatory](../kb/method-observatory.md)
