# Runbook: adozione del nuovo atrio (collezioni, collocazione per funzione, tre specie)

Data: 2026-06-14 · o3 verso il Mondo runtime (adottanti) · esegue: `method-review` di ciascun repo
Verdetto sorgente: `verdict.md`, fili «L'atrio rifondato» e «Rifondazione
atrio↔azione» (atrio a tre specie). Commit di `method`: `7a1dc5d` (rinomina i1) +
i commit di collocazione/atrio e di atrio-a-tre-specie di queste sessioni.

Atto prescritto: portare un repo adottante al canone nuovo dell'atrio. Quattro
modifiche: il punto 4 fissa la convenzione di collocazione dell'atrio, di cui 1 e 3
sono applicazioni; 2 è indipendente.

## 1. La collezione i1 si chiama `perceptions/`

- se versioni catture i1 (export, JSON, referti) in una cartella con altro nome
  (`sources/`, `data/json/`, …), rinominala in `perceptions/`; la sua porta è
  l'indice interno omonimo `perceptions/perceptions.md` (non un file in root —
  vedi punto 4);
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

## 4. L'atrio ha tre specie di file-root; le porte-stadio stanno dentro la cartella

La vecchia categoria «porta-collezione» si scioglie in tre specie di file-root —
**file-ciclo** (la triade alta: `README`, `plan.md`=o1-sviluppo, `verdict.md`=i3-sviluppo,
più `CLAUDE`/`AGENTS`), **cataloghi trasversali** (`kb.md`, `tools.md`: stanno in root
perché la collezione attraversa tutto il ciclo), **register** (`map.md`, `sources.md`:
puntano fuori dall'artefatto).

- le **collezioni-stadio** (`perceptions/`, `interpretations/`, `prescriptions/`) sono
  cartelle col gradiente di cardinalità: l'indice non è un file in root ma un **indice
  interno omonimo** — `perceptions/perceptions.md`, ecc. — sottile (dichiara lo stadio,
  linka all'atomo `perceive`/`interpret`/`perform`, elenca i contenuti);
- se hai porte in root (`perceptions.md`, `interpretations.md`, `prescriptions.md`),
  spostale dentro la cartella omonima; se parti da zero, creale già lì;
- `tasks/` non ha indice interno: la indicizza `plan.md`.

## Esecuzione via `method-review`

Prompt per il `method-review` del repo:

> Allinea l'atrio al canone di `method` (verdict «L'atrio rifondato» e «atrio a
> tre specie»): rinomina la collezione i1 in `perceptions/`, declassa `sources` a
> register/`world`, colloca i file-ciclo di dominio per funzione (i1→`perceptions/`,
> i2→`interpretations/`, `scadenze`→sezione di `plan`), e tieni le porte-stadio
> come indice interno omonimo dentro la cartella (`perceptions/perceptions.md`,
> ecc.), non in root. Lascia il lavoro residuo in `plan.md`/`tasks/` locali.

## Stato di recepimento

- `economia` — da fare
- `salute` — da fare
- `nixos` — punti 1–2 se versiona i1, e 4 dove ha collezioni; nessun `stato`/`diario`/`scadenze`
- `bi` — punti 1–2 se versiona i1, e 4 dove ha collezioni

Quando un repo ha completato, segna l'esito nel suo `verdict.md`; questo runbook
si chiude quando tutte le righe sopra sono recepite.
