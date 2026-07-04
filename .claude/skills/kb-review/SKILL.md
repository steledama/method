---
description: Health check completo della knowledge base del metodo usando gli strumenti versionati del repo.
user-invocable: true
---

# kb-review

Esegui un health check completo sulla knowledge base del metodo usando
`o3/kb_tools.py` come backend deterministico. Lo script è la fonte di verità
per parsing markdown, link, catalogo `kb/kb.md`, frontmatter, footer `Connessioni:` e
statistiche strutturali. Questa è la copia canonica della skill: gli adottanti la
forkano e la parametrizzano sul proprio dominio.

## Procedura

1. Dalla root del repository esegui:

```bash
python3 o3/kb_tools.py audit
```

2. Leggi il report e fai una breve valutazione qualitativa:

- problemi reali vs falsi positivi
- eventuali interventi ovvi e a basso rischio
- candidati terminologici che meritano o non meritano un nuovo nodo, ricordando
  che un nodo entra in `kb/` solo se è metodologico e applicabile ad almeno due
  progetti diversi
- esito sintetico della checklist di `kb/fedelta-cognitiva.md`

3. Il report è una diagnosi i1 rigenerabile: vive su stdout, **non** si archivia
   nei fili in `i3/`. Sono il verdetto corrente per filo aperto, non un log di
   audit datati (cfr. `kb/verdict.md`). Se l'audit fa _cambiare un verdetto_ su un filo,
   è il punto 2 di `/commit` ad aggiornarlo in place — non l'append di un report.

4. Se modifichi script Python durante l'audit, formatta con:

```bash
ruff format o3/*.py
```

5. Non correggere automaticamente i problemi trovati dentro lo stesso audit,
   salvo richiesta esplicita dell'utente. L'audit fotografa lo stato; le
   correzioni sono un intervento separato.

## Comandi utili

```bash
python3 o3/kb_tools.py backlinks nodo.md
python3 o3/kb_tools.py orphans
python3 o3/kb_tools.py readme
python3 o3/kb_tools.py migration
python3 o3/kb_tools.py terms --limit 20
python3 o3/kb_tools.py audit --format json
```

## Formatter

- Markdown, JSON, YAML, JS, TS, CSS, HTML: `prettier`
- Python: `ruff format`

## Cosa controlla

- link rotti tra nodi
- nodi orfani per backlink
- nodi isolati
- copertura e link validi nel catalogo `kb/kb.md` (escluso dal conteggio dei nodi)
- convenzioni sui nomi file
- stato della migrazione frontmatter + footer `Connessioni:`
- link markdown rimasti nel corpo dei nodi
- cluster isolati nel catalogo
- candidati a nuovi nodi da termini ricorrenti
- hub principali per backlink

## Checklist semantica

Usa `kb/cognitive-fidelity.md` per valutare ciò che gli script non possono
decidere: funzione documentale dei nodi, presente vs storia, accessibilità
cognitiva, aderenza degli esempi e confini futuri emergenti. Specifico del
`metodo`: verifica che ogni nodo resti metodologico e portabile (applicabile ad
almeno due progetti), non scivolato in dettaglio di un singolo dominio.

## Output

Concludi indicando all'utente i problemi più importanti e chiedendo se vuole
procedere con le correzioni.
