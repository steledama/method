---
data: 2026-06-13
stato: aperto
---

# Membrana `world`: ri-fondazione dei due archi attorno al Mondo

Task fondazionale emerso dal basso (salute, economia) in sessione 2026-06-13.
Introduce la convenzione concreta `world/` come materializzazione del nodo
`mondo`, e con essa corregge un'asimmetria latente nei nodi `input`/`output`: il
Mondo è una **membrana** non versionata attraversata nei due versi, e i1/o3 sono
i suoi due **riflessi versionati** che la baciano da dentro l'artefatto.

## Il modello

Lo specchio per altitudine del metodo (`ciclo-azione`) accoppia gli stadi:
o1↔i3 (vicino alla KB), o2↔i2 (la sintesi), **o3↔i1 (la cerniera Mondo)**. Da
qui la ri-fondazione:

- **`world`** — la membrana non versionata, esterna all'artefatto. Grezzo in
  entrata, atto in uscita. È sempre presente. Istanza concreta: un symlink
  `world` nella root del repo → la cartella di progetto su Drive (`salute`,
  `economia`, …). Nome **uniforme** (come `interpretations/`, `data/`); il
  carattere del dominio vive nel contenuto, non nel nome (in `bi` il Mondo è la
  relazione coi fornitori/Danea: contenuto dentro `world/`, non una porta
  `client/`).
- **i1** (`perceptions/` in salute) — cattura **versionata** del Perceive,
  filtrata-per-rilevanza e **valenza-neutra**. Record all'indietro.
- **o3** (canovacci, promemoria) — prescrizione **versionata** del Perform.
  Predisposizione in avanti.
- **i2/o2** — la sintesi (specchio già nominato in `input.md`).
- **i3/o1** — vicino alla KB.

Il riflesso versionato (i1 o o3) è **on-demand**: `world` e l'atto/segnale ci
sono sempre, il riflesso lo crei quando l'atto/segnale richiede **precisione o
durata** (le mail ripulite per il confronto scrupoloso → i1; il canovaccio
stampato per l'incontro ad alta posta → o3). Stesso criterio ai due capi.

## I tre confini (criterio di smistamento)

Lo stesso tipo di artefatto (es. una trascrizione) atterra in strati diversi
secondo il suo stato. Il criterio compatto, cuore del nodo:

- **world vs i1** — versionato e filtrato-per-rilevanza (i1), oppure
  grezzo/non-versionato (world)?
- **i1 vs i2** — è entrata la valenza/interpretazione (il "perché", il
  confronto)? La fedeltà (lossless vs lossy) **non** è il confine: la selezione
  per rilevanza resta i1, l'ingresso della valenza è i2.
- **o2 vs o3** — superficie di decisione versionata (o2), o prescrizione
  dell'atto versionata (o3)? L'atto realizzato è `world`.

## Ridefinizione di o3

`output.md` oggi definisce o3 come _l'effetto nel mondo_ («parole dette, gesti;
vive fuori dal repo»): chiama o3 l'**atto**. Ma l'atto è `world`. Per lo specchio
o3↔i1, o3 è la **prescrizione versionata** che sta accanto alla membrana, come i1
è la cattura versionata. Le voci o3 attuali (salute: «yoga, controlli,
conversazioni mediche») sono `world`; i veri o3 versionati sono i promemoria di
meditazione e i canovacci.

Caso-prova (economia), un cappio intero in un dominio:

> o2 (canovaccio) → o3 (l'incontro, in `world`) → i1 (trascrizione ripulita in
> `perceptions`) → i2 (analisi)

Bonus scoperto: lavorare sul canovaccio (o3) ha fatto **emergere goal latenti**
non ancora in KB. L'arco di output, predisponendo l'atto, retroalimenta il Goal —
triage-goal sull'arco di esecuzione, non solo sull'input esogeno. Va annotato in
`goal`/`output`.

## I due assi di Norman

Il modello fonde due framework di Norman distinti (mossa del metodo, non di
Norman): gli **assi verticali** sono i golfi di esecuzione/valutazione (→ archi
output/input, dai _sette stadi_ in DOET); le **tre altitudini** sono i _livelli
di elaborazione_ di _Emotional Design_ (viscerale/comportamentale/riflessivo). Il
livello è l'altitudine assoluta; il numero o/i codifica la posizione-nel-flusso
(o-numeri scendono, i-numeri salgono). Il nodo `visceral-behavioral-reflective`
ha già la mappatura: qui va solo raffinato perché il viscerale (cerniera Mondo)
ora comprende `world` (atto/grezzo) + i1/o3 (riflessi versionati), e o3 è
prescrizione, non atto.

## Deliverable

- **rename** `kb/mondo.md` → `kb/world.md`; aggiornare i backlink in tutti i
  nodi e nei `CLAUDE.md`/`README.md` dei repo collegati (cfr. regola di
  propagazione rename in `CLAUDE.md`).
- `kb/world.md` (ex mondo): aggiungere la membrana fisica e i due riflessi
  versionati on-demand.
- `kb/output.md`: ridefinire o3 (prescrizione versionata; l'atto è `world`);
  ri-etichettare gli esempi adottanti; nota goal-surfacing.
- `kb/input.md`: le due tessiture di i1 (estrazione 1:1 lossless / distillazione
  filtrata-per-rilevanza lossy, entrambe i1); il confine i1→i2 è la valenza, non
  la fedeltà; il riflesso versionato on-demand (specchio di o3).
- **rename** `kb/visceral-behavioral-reflective.md` → `kb/processing-layers.md`
  (usa "layers" invece di "levels": resta vicino a Norman ma risuona con gli
  strati input/output del metodo ed evita l'omonimia col framework "levels of
  processing" di Craik-Lockhart). Una riga nel nodo lo chiarisce. Aggiornare i
  backlink, **incluse le righe `Connessioni` di questi stessi task**.
- `kb/processing-layers.md` (ex v-b-r): raffinare il viscerale (world + i1/o3);
  o3 prescrizione non atto.
- `sources.md`: relazione con `world` (i binari gitignored in-repo sono un
  `world` degenere che siede nella cartella; criterio "versioni la cattura
  Perceive solo se il grezzo è effimero" — salute sì, libri di method no).
- `kb/struttura-progetto.md`: registrare la convenzione `world/`: un **symlink**
  alla cartella di progetto su Drive, contenuto non versionato, **nessun file
  manifest** (a differenza di `sources.md`: `world/` è solo la membrana).

I rename qui (`mondo→world`, `visceral-behavioral-reflective→processing-layers`)
sono casi della migrazione nomi inglese (`tasks/migrazione-nomi-inglese.md`),
fatti qui perché tocchiamo già questi nodi.

## La `world/` del metodo stesso (dogfooding)

Il metodo è meta-artefatto con due Mondi (cfr. `mondo`): il Mondo _di sviluppo_
sono i nodi `kb/`, il Mondo _runtime_ sono i repo adottanti. La sua `world/`
materializza il secondo: una cartella `world/` con **symlink ai repo adottanti**
(`economia`, `salute`, `nixos`, `bi`), **gitignorata** come ogni membrana
(symlink a path host-local, non versionati). Bidirezionale: l'esigenza dal basso
entra come i1 (le due task di questa sessione sono arrivate da `salute` così), il
filing back/propagazione esce come o3 verso gli stessi repo. È il duale del link
`metodo/` con cui gli adottanti vedono la dipendenza, e standardizza l'accesso
dell'osservatorio (`osservatorio-metodo`, skill `method-review`).

## Cosa resta locale (non task di method)

- **salute**: creare il symlink `world` → Drive, confermare `perceptions/` = i1
  (naming già corretto), aggiornare i doc locali. Lavoro nel repo `salute`.
- **economia**: ripulire le mail Capiroli/Maurizio → `perceptions` (i1), il
  confronto → i2. Lavoro nel repo `economia`.

Questi sono casi motivanti del filing back, non task del repo metodo (cfr. nodo
`plan`: le verifiche operative restano nel repo adottante).

Connessioni:

- [mondo](../kb/mondo.md) (→ world)
- [input](../kb/input.md)
- [output](../kb/output.md)
- [visceral-behavioral-reflective](../kb/visceral-behavioral-reflective.md) (→ processing-layers)
- [ciclo-azione](../kb/ciclo-azione.md)
- [goal](../kb/goal.md)
- [struttura-progetto](../kb/struttura-progetto.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
