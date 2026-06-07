---
data: 2026-06-07
stato: aperto
---

# Propaga la root-atrio a economia e salute (carrier)

Task **transitorio** (come fu `sostanza-why`): porta le bozze pronte dei task locali
`adotta-atrio` per `economia` e `salute`, che non sono raggiungibili dall'host dove l'atrio
è stato applicato a `metodo`. Una nuova istanza su un host di casa apre questo file ed
esegue le istruzioni sotto.

Il canone vive in `metodo` (commit `c66cf82`): nodo `metodo/struttura-progetto.md` (via
symlink nei figli) ed entry `why.md` 2026-06-07. Le bozze sotto elencano solo le differenze
specifiche di dominio; la teoria sta nel canone.

## Istruzioni per l'istanza di casa

Per **ciascun** repo (`../economia`, `../salute`):

1. crea `tasks/adotta-atrio.md` con il contenuto del blocco corrispondente qui sotto;
2. aggiungi in `plan.md` la riga `[Adotta la root-atrio del metodo](tasks/adotta-atrio.md)`
   con dipendenza `metodo c66cf82` (rispettando il formato del `plan.md` locale: bullet o
   tabella);
3. commita nel repo locale (non in `metodo`).

Il task `adotta-atrio` poi **esegue e si chiude nel repo figlio**, con giudizio umano sui
confini ambigui. Quando entrambi i figli hanno il loro `adotta-atrio` committato, questo
carrier si elimina (la riga sparisce da `plan.md` di metodo; lo storico resta in git).

Stato propagazione: `nixos` ✅ (commit `cd25028`), `bi` ✅ (commit `383f8f92`),
`economia` ⏳, `salute` ⏳.

## Bozza — `economia/tasks/adotta-atrio.md`

````markdown
---
data: 2026-06-07
stato: aperto
---

# Adotta la root-atrio del metodo

Conforma la root di `economia` al modello atrio del metodo (commit `metodo` `c66cf82`).
Canone: nodo `metodo/struttura-progetto.md` (via symlink) + entry `why.md` 2026-06-07 del
repo metodo. Leggerli prima; qui solo le differenze specifiche di economia.

## Interventi specifici di economia

1. **Catalogo → `kb.md`** (porta-collezione in root, link prefissati `kb/`; il README punta).
2. **`scripts/` → split.** `kb_tools.py` (strumento dell'artefatto) → `tools/` + `tools.md`.
   Gli script che *generano* `output/json/` sono output del runtime → restano `scripts/`
   (decisione umana sul confine).
3. **`output/` resta.** È o1 (JSON) + o2 (report tabellari): natura-dati, non
   sintesi-documento → non diventa `presentations/`. Una `presentations/` nasce solo se/quando
   c'è un deck di sintesi.
4. **`sources/`** solo se esistono fonti i1 versionate; altrimenti niente.
5. **File-ciclo di dominio** (`stato.md`, `scadenze.md`, `diario.md`) restano in root
   (root estensibile dal basso).
6. **Tooling**: adegua `tools/kb_tools.py` come metodo `c66cf82` (catalogo in root, report).
7. Aggiorna path in README/CLAUDE/AGENTS/nodi; rifonda il bootstrap sull'atrio.

## Verifica
- `python tools/kb_tools.py audit` → 0 link rotti, catalogo pieno.
- grep residui: `kb/index`, `scripts/kb_tools`, catalogo nel README.
- `why.md` locale: entry che cita il canone (`metodo` `c66cf82`).

Si apre e si chiude qui, in economia; non scrive nel repo metodo.
````

## Bozza — `salute/tasks/adotta-atrio.md`

````markdown
---
data: 2026-06-07
stato: aperto
---

# Adotta la root-atrio del metodo

Conforma la root di `salute` al modello atrio del metodo (commit `metodo` `c66cf82`).
Canone: nodo `metodo/struttura-progetto.md` (via symlink) + entry `why.md` 2026-06-07 del
repo metodo. Leggerli prima; qui solo le differenze specifiche di salute.

## Interventi specifici di salute

1. **Catalogo → `kb.md`** (porta-collezione in root, link prefissati `kb/`; il README punta).
2. **`quadro/` → `presentations/`** + porta `presentations.md`. Non è solo uniformità: rimuove
   una contraddizione — il nome `quadro` evoca il quadro *clinico*, contro l'essenza
   non-dualista corpo/mente della KB.
3. **`fonti/` → `sources/`** + porta `sources.md`.
4. **`scripts/` → `tools/`** + `tools.md` (kb_tools.py e strumenti di manutenzione; la skill
   ingest resta skill).
5. **File-ciclo di dominio** (`diario.md`, `scadenze.md`) restano in root.
6. **Tooling**: adegua `tools/kb_tools.py` come metodo `c66cf82`.
7. Aggiorna path in README/CLAUDE/AGENTS/nodi; rifonda il bootstrap sull'atrio.

## Design di dominio di `presentations/` (ex `quadro/`) — preservare

La presentazione non è il quadro *clinico* ma la sintesi olistica del **vivere meglio**.
Vincolo per slide: ogni slide tiene insieme la dimensione corporea e quella
mentale/esistenziale — mai una senza l'altra, perché la non-separazione corpo/mente è
l'essenza della KB. L'output mira a *istruzioni pratiche e concrete per vivere meglio*, non a
una fotografia diagnostica. Arricchimento previsto: disegni personalizzati (commissione
esterna) uno per slide, come strato visceral/affettivo (cfr. `visceral-behavioral-reflective`)
che tiene l'umano nel loop. Riconciliare con eventuali task esistenti su `quadro/`, senza
duplicare.

## Verifica
- `python tools/kb_tools.py audit` → 0 link rotti, catalogo pieno.
- grep residui: `quadro/`, `fonti/`, `kb/index`, `scripts/kb_tools`, catalogo nel README.
- `why.md` locale: entry che cita il canone (`metodo` `c66cf82`) e il perché del rename `quadro`.

Si apre e si chiude qui, in salute; non scrive nel repo metodo.
````
