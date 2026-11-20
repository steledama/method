---
sintesi: "Un sito per gruppo: l'istanza dichiara i membri nel proprio world.md, ogni repo pubblica la sua vista come oggi, e un servizio unico per host instrada verso le viste pubblicate con una home del gruppo. Casa su deck:8002, chiuse 8003 e 8004."
ciclo: dev
---

# Sito di gruppo

## Origine

Primo sotto-lavoro del [coordinatore di gruppi](coordinatore-di-gruppi.md),
sezione «Il sito di gruppo», aperto dal custode il 2026-11-20.

## Forma

Il sito non ricostruisce nulla: ogni membro pubblica la propria vista da un
commit pulito, come oggi (`kb/view-publishing.md`, «Pubblicazione»), e il
sito instrada verso le cartelle pubblicate.

- **registro dei membri**: una sezione `## Membri` nel `world.md`
  dell'istanza, una voce per repo col nome del checkout in grassetto. La
  build dell'istanza la rende in `view/gruppo.json`, così anche l'elenco
  servito viene da un commit;
- **rotte**: `/` è la home del gruppo, `/<repo>/` la versione pubblicata di
  quel repo, istanza compresa. La home si compone a ogni richiesta
  dall'elenco pubblicato dell'istanza e dalle viste pubblicate dei membri
  (titolo, accento, presentazione); un membro senza versione valida resta
  in elenco come non pubblicato;
- **caso minimo**: un'istanza senza membri serve sé sola;
- **servitore**: `serve.py --gruppo BASE --istanza NOME`, dove `BASE` contiene
  una cartella di pubblicazione per repo (`BASE/<repo>`).

## Decisioni del custode

- 2026-11-20: casa su `deck:8002`, al posto della vista di `nixos`; le viste
  `deck:8003` e `deck:8004` si chiudono subito, senza periodo di prova in
  parallelo. `method` resta su `deck:8001`, fuori dal gruppo;
- 2026-11-20: l'elenco dei repo da pubblicare resta anche in
  `o3/presentations.nix` di `nixos`; la coerenza con il `world.md` dell'istanza
  la controlla `/adottanti`;
- il ritorno alla home del gruppo dalle viste dei membri resta al browser in
  questo primo rilascio.

## Passi

1. ~~Canone in `method`~~ fatto il 2026-11-20: `o3/view/gruppo.py`,
   `gruppo.json` in build, `serve.py --gruppo`, `tests/test_gruppo.py`,
   contratto in `kb/view-publishing.md`, «Sito di gruppo».
2. `casa`: sezione `## Membri` in `world.md`.
3. `nixos`: servizio di gruppo su `8002` da `~/casa`, `casa` fra i repo
   pubblicati, ritiro dei servizi per repo di `nixos`, `salute` ed
   `economia`; indirizzi in `world.md` di `method`.

I passi 2 e 3 toccano altri repo: si fanno su autorizzazione esplicita del
custode o nelle loro sessioni.

## Criterio di chiusura

`deck:8002` serve la home di casa con i quattro repo, `8003` e `8004` non
rispondono, e l'audit degli adottanti legge i nuovi indirizzi.
