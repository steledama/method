# Goal

Il motivo di `metodo` è **custodire il metodo portabile e propagarne il canone
agli adottanti senza micromanagiarne le code**: la cognizione condivisa
umano-LLM retta da artefatti portabili, indipendenti dal modello, adattabili,
capaci di autocorrezione e rigorosi sulle fonti.

## Obiettivi runtime

### 1. Custodire un canone coerente e fedele alle fonti

I nodi `kb/` reggono il peso del metodo: atomici, connessi, verificabili contro
le fonti-mondo.

- **Rete dei nodi sana e verificata** — segnali: audit `o3/kb_tools.py` (`/kb`)
  e filo [maturazione-nodi-fondativi](i3/maturazione-nodi-fondativi.md); lavoro:
  rifinitura semantica applicata, con distinzioni e attribuzioni corrette. Il
  mantenimento è event-driven sui segnali di incoerenza; il lavoro aperto si
  legge nel plan. Le ipotesi su tipologia, matrice e facet attendono nuove
  evidenze d'uso, mentre le fonti mancanti restano dichiarate nel register
  World. Un audit verde non sostituisce queste verifiche.

### 2. Propagare il canone e chiudere il loop con gli adottanti

Il top-down legittimo: prescrizioni o3 che gli adottanti recepiscono col proprio
`method`, senza che `metodo` gestisca le loro code.

- **Canone recepito dagli adottanti** — struttura, register e quartetto chiusi
  (2026-07-11, ultimo `salute`); segnali: marker `i3/allineamento-metodo.md`
  degli adottanti, filo [audit-adottanti](i3/audit-adottanti.md) (verdetto
  dell'audit mensile); lavoro: sei adottanti dal 2026-08-12 (`crm` e
  `danea-auto` quinto e sesto); obiettivo con **un fronte aperto** — il giro
  vive nei `method` degli adottanti e il battito è la riga mensile
  `/adottanti` in `## Scadenze`. Alla verifica fuori giro del 2026-10-03 tutti e sei sono a
  `91cf874`, `aligned`, e i marker coincidono coi file; le viste sono fresche
  in tutti e sei, verificate rigenerando il 2026-10-02. `/method` rilegge a ogni giro le
  prescrizioni aperte.
  Prescrizioni aperte: `esiti-per-stadio-nel-commit`, scritta da cinque repo
  su sei e da contare il 2026-11-01, quando si riapre la clausola delle skill
  per arco; `migrazione-viste`, emessa il 2026-10-04 (viste in `view/`,
  deck in `presentation/`); `revisione-bootstrap-adottante` e
  `ingresso-adottante`, non verificate nel merito.

### 3. Ascoltare il basso

Il bottom-up: il canale i1 con gli adottanti resta vivo e i segnali passano per
i2/i3 invece di incidere il canone di straforo.

- **Canale-perception funzionante** — segnali:
  [i1/perceptions.md](i1/perceptions.md) e le pull request degli adottanti
  mantenuti da terzi; lavoro: event-driven sui segnali, senza task aperti — i
  task che servono l'obiettivo si leggono dalla colonna `Ob.` di
  [`o1/plan.md`](o1/plan.md).

## Goal di sviluppo

Posizione auspicata lungo le dimensioni candidate comuni
([development-goal](kb/development-goal.md)): ciclo **event-driven** sul segnale
dell'adottante, umano **in-the-loop**, **basso attrito di lettura** (bussola
snella, viste che si aprono dal checkout), KB riflessiva coerente, loop di
propagazione che si chiude. Il lavoro che la serve porta `Ob. S` in
[`o1/plan.md`](o1/plan.md); il battito mensile `/adottanti` — l'audit runtime-o1
che chiude il giro dall'alto — vive in `## Scadenze`.

## Disciplina

- Register del polo Goal, gemello di [`world.md`](world.md): il goal è il nord,
  il world è il territorio. Forma e contratto (l'intro è il polo che la home
  rende) in [goal](kb/goal.md).
- Fotografia aggiornata in place, non documento di aspirazioni; il razionale
  vive nei nodi ([goal](kb/goal.md),
  [development-goal](kb/development-goal.md)).
- Custode umano: Stefano. Gli agenti propongono scostamenti, non riscrivono il
  nord.
- Ogni obiettivo ha almeno un segnale vivo; ogni task di `o1/plan.md` serve un
  obiettivo di questo register — `exec plan` verifica la direzione
  task→obiettivo, `eval compare` la direzione obiettivo→segnale/filo.
- La direzione task→obiettivo vive nella colonna `Ob.` del plan, non in un
  elenco qui: la chiave è il **numero** dell'obiettivo runtime, `S` per il Goal
  di sviluppo ([plan](kb/plan.md)). Numerazione stabile: rinumerare un obiettivo
  invalida le chiavi in tabella.
