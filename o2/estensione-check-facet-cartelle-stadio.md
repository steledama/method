---
stato: aperto
ciclo: dev
sintesi: "La facet `ciclo: dev|runtime` è applicata agli item delle sei collezioni-stadio (2026-07-04, ristrutturazione dell'atrio), ma kb_tools.py verifica le facet solo su DOC_DIRS (`kb/`): estendere il check [FACET] alle cartelle-stadio, così `ciclo` è presidiata dal deterministico e non solo dichiarata."
---

# Estensione del check facet alle cartelle-stadio

## Contesto

Con la ristrutturazione dell'atrio (collezioni `i1/`–`o3/`) ogni item di
collezione dichiara nel frontmatter la facet `ciclo: dev|runtime`, letta dal
Mondo su cui l'item insiste: artefatto → `dev`, adottanti → `runtime` (cfr.
`kb/nested-cycles.md`). Il meccanismo `[FACET]`/`EXTENDED_FACETS` di
`o3/kb_tools.py` però scandaglia solo `DOC_DIRS = ("kb", …)`: la facet nelle
collezioni-stadio oggi non è verificata da nessuno strumento.

## Lavoro

- estendere il check facet (o un check gemello) alle sei cartelle-stadio,
  distinguendo item (facet attesa) e indici di collezione (esenti);
- dichiarare `ciclo` come facet di `method` — primo caso in cui `method` stesso
  usa il meccanismo che finora offriva solo agli adottanti (`mondo` in `nixos`,
  `tipo` in `economia`);
- decidere se `required` (ogni item la dichiara) o opzionale col solo dominio
  chiuso `{dev, runtime}`.

## Criterio di done

`kb-review`/`audit` segnala un item di collezione con `ciclo` mancante (se
required) o fuori dominio; gli indici non generano falsi positivi.
