# Runbook: adozione del nuovo atrio (`perceptions/` + collocazione per funzione)

Data: 2026-06-14 · o3 verso il Mondo runtime (adottanti) · esegue: `method-review` di ciascun repo
Verdetto sorgente: `verdict.md`, filo «L'atrio rifondato». Commit di `method`:
`7a1dc5d` (rinomina i1) + il commit di collocazione/atrio di questa sessione.

Atto prescritto: portare un repo adottante al canone nuovo dell'atrio. Tre
modifiche indipendenti tra loro.

## 1. La collezione i1 si chiama `perceptions/`

- se versioni catture i1 (export, JSON, referti) in una cartella con altro nome
  (`sources/`, `data/json/`, …), rinominala in `perceptions/` e la sua porta in
  `perceptions.md`;
- aggiorna i path in `CLAUDE.md`/`README.md`/`map.md` locali e in `.gitignore`.
- **`economia`**: applicare durante la migrazione di `data/json/` (task locali 15
  / 16 / 22) adottando direttamente `perceptions/`, così la rinomina è una sola.

## 2. Le fonti grezze sono `world`, non una collezione

- i binari/documenti-fonte autorevoli (libri, PDF) vivono su Drive via `world/`,
  gitignorati: sono `source-of-truth`, fuori dall'artefatto;
- se ne tieni la provenienza, mettila in `sources.md` come **register** (non
  porta-collezione): «quale fonte regge quale nodo», base dei `## Riferimenti`.

## 3. I file-ciclo di dominio si collocano per funzione, non in root

- `diario` (cattura cronologica, i1) → `perceptions/`, tenuto valenza-neutro;
- `stato` (sintesi corrente, i2) → `interpretations/`, come i2 testuale accanto
  al deck; l'ordine di bootstrap in `CLAUDE` lo indica come prima lettura
  (posizione≠bootstrap);
- `scadenze` (vincolo di pianificazione) → una sezione di `plan.md`;
- la root resta il cruscotto del solo ciclo di sviluppo + porte/register.
- **`economia`**: `stato`, `scadenze` in root → migrare. **`salute`**: `diario`,
  `scadenze` → migrare.

## Esecuzione via `method-review`

Prompt per il `method-review` del repo:

> Allinea l'atrio al canone di `method` (verdict «L'atrio rifondato»): rinomina
> la collezione i1 in `perceptions/`, declassa `sources` a register/`world`, e
> colloca i file-ciclo di dominio per funzione (i1→`perceptions/`,
> i2→`interpretations/`, `scadenze`→sezione di `plan`). Lascia il lavoro residuo
> in `plan.md`/`tasks/` locali.

## Stato di recepimento

- `economia` — da fare
- `salute` — da fare
- `nixos` — solo punti 1–2 se versiona i1; nessun `stato`/`diario`/`scadenze`
- `bi` — solo punti 1–2 se versiona i1

Quando un repo ha completato, segna l'esito nel suo `verdict.md`; questo runbook
si chiude quando tutte le righe sopra sono recepite.
