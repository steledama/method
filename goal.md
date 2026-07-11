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

- **Atrio recepito dai quattro** — **raggiunto** (2026-07-11, chiusura di `bi`
  validata dal run notturno di produzione); segnali: marker `method-review.md`
  degli adottanti; lavoro: nessun task aperto, prescrizione rimossa da `o3/`.
- **Poli-register e quartetto di review propagati** — segnali: filo
  [poli-register-goal-world](i3/poli-register-goal-world.md) — recepito da
  `economia`, `nixos` e `bi`, resta `salute`; lavoro:
  «Propagazione poli-register e quartetto di review».

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
loop di propagazione che si chiude. Lavoro corrente che la serve: «Protocollo
runtime-o1» (l'audit periodico top-down che manca al giro), «Redraw tavole
vista Interpretazioni» (attrito di lettura della vista i2).

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
