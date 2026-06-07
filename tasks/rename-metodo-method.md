---
data: 2026-06-07
stato: aperto
---

# Rinominare metodo in method

Rinominare l'identificatore strutturale del repository e della dipendenza
trans-repo da `metodo` a `method`, in coerenza con la policy già adottata per
slug, directory e componenti vivi. La prosa e i concetti possono restare in
italiano: questo task riguarda il nome tecnico esposto nel filesystem, nei path
e nel repository remoto, non la futura traduzione dei contenuti.

## Superfici del rename

- directory locale: `~/metodo/` → `~/method/`;
- repository remoto GitHub: `steledama/metodo` → `steledama/method`, con verifica
  del comportamento dei redirect;
- symlink nei quattro adottanti: `metodo/ → ../metodo/kb` diventa
  `method/ → ../method/kb`;
- link relativi e path operativi: `metodo/*.md`, `../metodo/*.md`,
  `~/metodo/...`;
- URL espliciti a `github.com/steledama/metodo`;
- controlli hardcoded negli strumenti, in particolare i check trans-repo di
  `economia/tools/kb_tools.py`;
- README, CLAUDE, AGENTS, map, cataloghi, skill, task e riferimenti rapidi nei
  cinque repository;
- configurazioni esterne versionate che assumono il path locale del repository.

Le menzioni storiche in `why.md` vanno valutate semanticamente: aggiornare i path
operativi e aggiungere una nota di supersessione, senza riscrivere
indiscriminatamente la storia.

## Sequenza proposta

1. Inventariare tutti i riferimenti nei cinque repository e distinguere path
   vivi, URL remoti, testo concettuale e memoria storica.
2. Rinominare il repository remoto e aggiornare `origin`.
3. Rinominare la directory locale e i quattro symlink.
4. Aggiornare path, link, strumenti e istruzioni operative in ogni repository.
5. Eseguire audit e controlli specifici di ciascun adottante.
6. Committare separatamente in ciascun repository, senza task centrali di
   propagazione aggiuntivi.

## Rischi e vincoli

- il rename della directory corrente può interrompere sessioni e processi che
  conservano il vecchio working directory: eseguirlo in una sessione dedicata;
- i symlink relativi devono restare portabili tra host;
- non tradurre automaticamente nomi di nodi, prosa o concetti italiani;
- verificare eventuali integrazioni esterne, bookmark, clone e automazioni che
  usano `~/metodo` o l'URL GitHub;
- evitare una fase intermedia in cui gli adottanti puntano a un symlink rotto.

## Criterio di chiusura

Il repository è disponibile localmente come `~/method` e remotamente come
`steledama/method`; i quattro adottanti espongono `method/ → ../method/kb`;
nessun riferimento operativo vivo usa più `metodo/`, `../metodo`, `~/metodo` o
l'URL remoto precedente. Audit e link check dei cinque repository sono puliti.
