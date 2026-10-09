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
  (`/kb`) e filo [maturazione-nodi-fondativi](i3/maturazione-nodi-fondativi.md).
  La provenienza e i limiti delle fonti si verificano in [World](world.md#fonti).
  Un audit strutturale non sostituisce la verifica semantica e delle fonti.

### 2. Propagare il canone e chiudere il loop con gli adottanti

Il top-down legittimo: prescrizioni o3 che gli adottanti recepiscono col proprio
`method`, senza che `metodo` gestisca le loro code.

- **Canone recepito dagli adottanti** — segnali: marker
  `i3/allineamento-metodo.md` sulle superfici dichiarate in [World](world.md),
  filo [audit-adottanti](i3/audit-adottanti.md) per il verdetto aggregato.

### 3. Ascoltare il basso

Il bottom-up: il canale i1 con gli adottanti resta vivo e i segnali passano per
i2/i3 invece di incidere il canone di straforo.

- **Canale-perception funzionante** — segnali:
  [i1/perceptions.md](i1/perceptions.md) e le pull request degli adottanti
  mantenuti da terzi.

## Goal di sviluppo

Posizione auspicata lungo le dimensioni candidate comuni
([development-goal](kb/development-goal.md)): ciclo **event-driven** sul segnale
dell'adottante, umano **in-the-loop**, **basso attrito di lettura** (bussola
snella, viste facilmente consultabili e riproducibili dalle fonti), KB riflessiva coerente, loop di
propagazione che si chiude.

Segnali: [battito autonomo](i3/battito-autonomo.md),
[ricostruzione delegabile](i3/verdetto-piu-sicuro-del-materiale.md),
[toolchain delle viste](i3/toolchain-builder-presentazione.md), audit e build
`o3/view/build.py --check`. Il lavoro è raggiungibile dalla colonna `Ob. S`
del [plan](o1/plan.md).

## Disciplina

- Register del polo Goal, gemello di [`world.md`](world.md): il goal è il nord,
  il world è il territorio. Forma e contratto (l'intro è il polo che la home
  rende) in [goal](kb/goal.md).
- Motivo, obiettivi e puntatori ai segnali; lo stato corrente vive nei fili
  e nel plan, le misure nelle fonti. Contratto in
  [goal-register](kb/goal-register.md), razionale in [goal](kb/goal.md) e
  [development-goal](kb/development-goal.md).
- Custode umano: Stefano. Gli agenti propongono scostamenti, non riscrivono il
  nord.
- Ogni obiettivo ha almeno un segnale vivo; ogni task di `o1/plan.md` serve un
  obiettivo di questo register — `exec plan` verifica la direzione
  task→obiettivo, `eval compare` la direzione obiettivo→segnale/filo.
- La direzione task→obiettivo vive nella colonna `Ob.` del plan, non in un
  elenco qui: la chiave è il **numero** dell'obiettivo runtime, `S` per il Goal
  di sviluppo ([plan](kb/plan.md)). Numerazione stabile: rinumerare un obiettivo
  invalida le chiavi in tabella.
