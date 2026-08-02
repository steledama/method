---
description: Audit runtime-o1 periodico dei progetti adottanti — distanza dal telos, canale del canone, lezioni che risalgono — senza toccare le code locali
user-invocable: true
---

# adottanti

Esegui questa skill dalla root di `metodo`. È l'**o1-runtime** del ciclo:
l'audit periodico top-down sui progetti adottanti dichiarati in `world.md`.
Chiede «l'adottante è ancora coerente col canone? quanto dista dal telos?
quale lezione risale?» — **mai** «ecco i tuoi task». È una skill di dominio di
`metodo` (il suo Mondo runtime sono gli adottanti): non fa parte del quartetto
e gli adottanti non la forkano.

La cadenza è la riga `(mensile)` in `## Scadenze` di `o1/plan.md`; gli esiti
aggregano nel filo [`i3/audit-adottanti.md`](../../../i3/audit-adottanti.md),
aggiornato in place a ogni giro.

## Confini (la lama)

- **Sola lettura** sui repo adottanti: nessun file scritto, nessun task
  proposto o inserito nelle loro code.
- L'audit **misura la maturità, non gestisce la coda**. La distanza dal telos
  (cfr. `kb/development-goal.md`, il punto asintotico) si legge contro la
  posizione auspicata del `goal.md` _dell'adottante_: la gradualità è di
  dominio — un dominio in-the-loop per costituzione non è «indietro».
- Se emerge drift di canone, l'atto top-down è una **prescrizione in `o3/`**;
  se risale una lezione dal basso, è un **segnale in `i1/`**; tutto il resto è
  coda di dominio e non ci riguarda.
- Non sostituisce `method` (il giro per-adottante guidato dal marker,
  eseguito _nell'adottante_): questo è il giro d'insieme, dall'alto.

## Procedura

### 1. Perimetro

Leggi l'elenco degli adottanti dal register `world.md` e l'HEAD di `metodo`
(`git log -1 --format='%H %ad %s' --date=short`).

### 2. Canale del canone (per adottante)

Leggi `i3/allineamento-metodo.md` dell'adottante: `method_commit`,
`reviewed_at`, `status`. Misura il ritardo marker→HEAD in commit
(`git rev-list --count <marker>..HEAD`) e scorri i soggetti non recepiti.
`status: action-required` o un ritardo che accumula canone strutturale sono i
segnali rossi; un ritardo di pochi commit editoriali è fisiologico.

### 3. Composizione delle code (la metrica del telos)

Leggi `o1/plan.md` dell'adottante e fotografa la composizione (cfr.
`kb/plan.md`, «Scadenze» e la terza specie):

- tabella task: quante righe `dev`, quante `runtime`; sezioni di holding;
- `## Scadenze`: ricorrenti a orologio manuale (con data), run automatizzati
  (senza data, rimando alla config), date stantie (occorrenza passata =
  orologio fermo);
- ricorrenza a evento: skill di dominio senza riga (legittima, non un buco).

La firma del telos: tabella dev che si svuota, battito ricorrente visibile,
quota schedulata che cresce — sempre pesata sulla gradualità del dominio.

### 4. Inventario skill

`ls .claude/skills/` dell'adottante: quartetto più `method` presente;
skill di dominio; residui (nomi vecchi dopo una rinomina, doppioni).

### 5. Superfici e viste

L'unica lente che attraversa il confine tra una vista e ciò da cui deriva: gli
audit strutturali non lo attraversano, quindi una superficie può contraddire la
propria fonte mentre ogni altro controllo dice che va tutto bene (cfr.
`kb/view.md`, «Derivata implica verificata», e il filo
[`i3/vista-derivata-e-verificata.md`](../../../i3/vista-derivata-e-verificata.md)).

Per adottante, in sola lettura:

- **quali superfici esistono** (`presentation/` o l'equivalente dichiarato nel
  suo `world.md`) e **quali sono generate** da uno script versionato: una vista
  il cui file cambia senza che cambi un generatore è mantenuta a mano;
- tra le generate, **quali derivano da più fonti** che possono contraddirsi, e
  se il generatore le legge come contratto o si limita a trasformare (una vista
  a fonte unica non può divergere: non è un buco);
- il test rapido su una vista a mano è il confronto con l'**ultima** modifica
  della fonte, non un campione sul contenuto vecchio: il drift colpisce il fatto
  più fresco, cioè quello per cui la vista si apre.

Il costo **ordina, non classifica**: la regola è una per tutti, ma una vista a
mano che rende fatti su cui si agisce (salute, denaro, scadenze) si guarda per
prima. Segnale rosso: la vista invita a un'azione che la fonte ha già ritirato.

### 6. Verdetto aggregato

Aggiorna `i3/audit-adottanti.md` in place: una fotografia sottile per
adottante (canale, composizione, distanza dal telos contro la sua gradualità)
più le lezioni cross-repo. Classifica ogni scostamento: **prescrizione o3**
(drift di canone), **segnale i1** (lezione dal basso), **niente** (coda di
dominio). Aggiorna la riga del filo nell'indice `i3/verdicts.md`.

### 7. Chiudi il giro

Avanza la data della riga `(mensile)` in `## Scadenze` di `o1/plan.md` alla
prossima occorrenza. Riporta in conversazione: fotografia per adottante,
scostamenti classificati, prescrizioni o segnali aperti.
