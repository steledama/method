---
data: 2026-06-14
stato: aperto
---

# Collocazione per funzione dei file-ciclo di dominio

Emerso dall'adozione in `economia`, subito dopo che `data/json/` è diventato la
collezione i1 versionata. La domanda: i file-ciclo che un dominio aggiunge alla
root — `stato.md`, `diario.md`, `scadenze.md` — vanno collocati **per funzione
cognitiva** nelle collezioni i1/i2, o restano in root come «bootstrap di dominio»?

## L'osservazione

`diario.md` è la cattura cronologica dei controlli: è i1. `stato.md` è il quadro
sintetico corrente: è i2. Eppure entrambi vivono in root. La giustificazione
finora ([[project-structure]], «root estensibile dal basso», che nomina proprio
`stato`/`diario`/`scadenze`) era la lettura-a-ogni-sessione. Ma lo stesso
[[project-structure]] afferma che «in root non significa letto al bootstrap: il
signifier che dice cosa leggere e quando è l'ordine di bootstrap, non la
posizione del file». Le due affermazioni sono in tensione: se la posizione non
determina il caricamento, l'argomento bootstrap non giustifica la root, e la
collocazione-per-funzione (i1 → `perceptions`, i2 → `interpretations`)
dovrebbe prevalere — come già accade per o2 (`interpretations/`) e o3
(`prescriptions/`).

## Perché ora

Finché l'i1 di un dominio non era una collezione versionata (in `economia`
viveva in `data/json/` gitignorato), `diario` non aveva una collezione i1 dove
stare e la root era una scelta obbligata. Ora che `economia` ha sia `perceptions/`
(i1) sia `interpretations/` (i2), la collocazione-per-funzione è possibile. La
decisione registrata in `method-review` di `economia` («restano in root come
componenti di dominio») va quindi riconsiderata alla luce del nuovo assetto.

## Il lavoro

- decidere la regola: i file-ciclo di dominio con uno stadio i chiaro si
  collocano nella collezione corrispondente (i1 → `perceptions`, i2 →
  `interpretations`), non in root; la root resta per il cruscotto del ciclo di
  sviluppo (README, plan, CLAUDE, verdict) e per le porte;
- distinguere il caso di `stato`: è i2 **testuale**, altitudine distinta dal deck
  grafico (`index.html`); entrambe le forme dell'i2 convivono in `interpretations/`
  (cfr. [[input]], «la forma segue il dominio: grafica dove i dati sono molti,
  testuale dove concettuale»). La mossa non è fondere `stato` nel deck — perde la
  leggibilità al bootstrap — ma collocarlo come i2 testuale accanto ad esso;
- esaminare `diario`: la cattura cronologica è i1, ma le «osservazioni» valenzate
  possono sconfinare in i2 (confine i1→i2 = ingresso della valenza, cfr. [[input]],
  [[world]]); decidere se resta i1 puro o si scinde;
- trattare `scadenze` (presente in `salute`) con lo stesso criterio: che stadio è
  e dove va;
- revisionare la regola «root estensibile dal basso» in [[project-structure]] e
  riconciliarla col principio posizione≠bootstrap;
- propagare agli adottanti: aggiornare i `CLAUDE.md`/`README.md` di `economia` e
  `salute`, le porte e l'ordine di bootstrap.

## Relazione con il naming i1 (risolto)

Il gemello che decideva _come si chiama_ la collezione i1 è chiuso: il nome è
**`perceptions/`** (cfr. `verdict.md`); le fonti-mondo sono `world`, non una
collezione, e `sources.md` è un register di provenienza, non una porta. Questo
task decide _che cosa ci va dentro_ — la membership dei file-ciclo di dominio — e
tocca la dottrina dell'atrio. Il path di destinazione è quindi noto: i file-ciclo
con stadio i1 chiaro migrano in `perceptions/`, quelli i2 in `interpretations/`.
