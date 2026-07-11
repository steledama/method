# Goal

Il motivo di `metodo` è **custodire il metodo portabile e propagarne il canone
agli adottanti senza micromanagiarne le code**: la cognizione condivisa
umano-LLM retta da artefatti portabili, indipendenti dal modello, adattabili,
capaci di autocorrezione e rigorosi sulle fonti.

## Obiettivi runtime

### 1. Custodire un canone coerente e fedele alle fonti

I nodi `kb/` reggono il peso del metodo: atomici, connessi, verificabili contro
le fonti-mondo.

- **Rete dei nodi sana e verificata** — segnali: audit `o3/kb_tools.py`
  (`/kb-review`), filo [maturazione-nodi-fondativi](i3/maturazione-nodi-fondativi.md);
  lavoro: nessun task aperto — obiettivo **a regime**, i verdetti pendenti
  attendono l'uso reale (bozza→maturo, tipologia, matrice, facet).

### 2. Propagare il canone e chiudere il loop con gli adottanti

Il top-down legittimo: prescrizioni o3 che gli adottanti recepiscono col
proprio `method-review`, senza che `metodo` gestisca le loro code.

- **Canone recepito dai quattro** — atrio e poli-register/quartetto chiusi
  (2026-07-11, ultimo `salute`); segnali: marker `method-review.md` degli
  adottanti, filo [audit-adottanti](i3/audit-adottanti.md) (verdetto
  dell'audit mensile), filo
  [poli-register-goal-world](i3/poli-register-goal-world.md);
  lavoro: il battito mensile `/adopters-review` (primo giro 2026-07-11),
  nessuna prescrizione in `o3/` — obiettivo **a regime**, il giro vive nei
  `method-review` degli adottanti; watchpoint: la disciplina del register di
  `salute` al suo primo `verdicts-review`.

### 3. Ascoltare il basso

Il bottom-up: il canale i1 con gli adottanti resta vivo e i segnali passano per
i2/i3 invece di incidere il canone di straforo.

- **Canale-perception funzionante** — segnali: [i1/perceptions.md](i1/perceptions.md),
  fili [membrana-afforda-scrittura](i3/membrana-afforda-scrittura.md) e
  [de-cablaggio-binomio-due-agenti](i3/de-cablaggio-binomio-due-agenti.md);
  lavoro: event-driven sul segnale — obiettivo **a regime**, l'enforcement
  della cucitura resta trattenuto («Enforcement della cucitura», `pause`).

## Goal di sviluppo

Posizione auspicata lungo le dimensioni comuni
([development-goal](kb/development-goal.md)): ciclo **event-driven** sul
segnale dell'adottante, umano **in-the-loop**, **basso attrito di lettura**
(bussola snella, viste che si aprono dal checkout), KB riflessiva coerente,
loop di propagazione che si chiude. Lavoro corrente che la serve: il battito
mensile `/adopters-review` (l'audit runtime-o1 che chiude il giro dall'alto),
«Redraw tavole vista Interpretazioni» (attrito di lettura della vista i2).

## Disciplina

- Register del polo Goal, gemello di [`world.md`](world.md): il goal è il nord,
  il world è il territorio. Forma e contratto (l'intro è il polo che la home
  rende) in [goal](kb/goal.md).
- Fotografia aggiornata in place, non documento di aspirazioni; il razionale
  vive nei nodi ([goal](kb/goal.md), [development-goal](kb/development-goal.md)).
- Custode umano: Stefano. Gli agenti propongono scostamenti, non riscrivono il
  nord.
- Ogni obiettivo ha almeno un segnale vivo; ogni task di `o1/plan.md` serve un
  obiettivo di questo register — `/plan-review` verifica la direzione
  task→obiettivo, `/verdicts-review` la direzione obiettivo→segnale/filo.
