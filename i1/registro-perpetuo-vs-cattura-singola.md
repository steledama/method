---
ciclo: runtime
---

# Segnale: un registro perpetuo è una specie di i1, e i register di stadio non tassonomizzano le nature dei file che contengono

Data: 2026-08-01 · Fonte: nixos — `i1/manutenzione.json`, stato prodotto
dalla skill `/manutenzione`

## Il segnale

`method/perceive.md` fissa un ciclo di vita solo: una cattura i1 nasce
on-demand, viene **consumata** da un verdetto in `i3/` (o giudicata non
pertinente) e a quel punto **si elimina** — "un i1 che accumula segnali
consumati è un archivio travestito, l'archivio è git". Ogni esempio citato
nel canone (log diagnostico, referto `hw-report.sh`, trascrizione) è uno
scatto **singolo e datato**: catturato una volta, valutato, sparisce.

`i1/manutenzione.json` (nixos) non segue questo ciclo. È un file scritto
dalla skill `/manutenzione` a ogni run (versioni pacchetti confrontate con
`nixpkgs-unstable`, stato dei workaround upstream tracciati in
`o1/plan.md`): **una voce corrente per ramo, sovrascritta**, mai un evento
singolo da giudicare e poi rimuovere. Non ha mai un momento di "consumo" —
resta sempre attuale, sempre presente. Due ragioni pratiche l'hanno tenuto
versionato invece di gitignorato (traiettoria completa in nixos, non
riportata qui per intero): serve a calcolare la freschezza di ogni ramo al
run successivo (ha bisogno del `git log` come storico, non di un file che
cresce, per lo stesso principio anti-duplicazione del canone), ed è il
meccanismo con cui la freschezza si **sincronizza tra i cinque host** — un
repo multi-host dove git è già il canale di sync tra le macchine.

## L'attrito osservato

Il caso è stato risolto localmente per analogia, non per regola: si è
scelto di tenerlo in `i1/` (tematicamente è cattura di segnale, valenza-
neutra, dal confronto sistema/upstream) ma **dichiarando esplicitamente**
nell'indice (`i1/perceptions.md`) che questo file non segue il ciclo di vita
standard — un'eccezione nominata, non un'estensione silenziosa della regola.

Due domande restano aperte, di ampiezza diversa:

1. **La specie stessa**: un registro perpetuo (stato skill-owned, mai
   consumato, sincronizzato via git tra ambienti) è una seconda specie
   legittima di i1 accanto alla cattura singola, o merita un nome e un posto
   propri fuori dal ciclo a sei stadi? Il canone ha già un precedente
   strutturale simile altrove — la «terza specie» di riga in `## Scadenze`
   (run automatizzato da scheduler, senza data, la config come fonte di
   verità) è nata dalla stessa osservazione: uno stato che si rinnova da sé
   non è un evento da archiviare. Se il pattern regge, `i1` (e forse gli
   altri stadi) potrebbe avere bisogno di un vocabolario analogo.
2. **La domanda più ampia**, sollevata esplicitamente dal custode durante la
   sessione che ha prodotto questo segnale: i register di collezione (qui
   `i1/perceptions.md`, ma la domanda vale per `i2/interpretations.md`,
   `i3/verdicts.md`, `o2/tasks.md`, `o3/prescriptions.md`) oggi elencano i
   contenuti senza **classificarne esplicitamente la natura** — una cattura
   singola e un registro perpetuo convivono nello stesso indice, distinti
   solo da una nota in prosa scritta caso per caso (come qui). Se questa
   eterogeneità è reale e ricorrente, i register meriterebbero una
   tassonomia dichiarata delle nature dei file che ospitano, coi nomi giusti
   — non solo per `i1`.

## Perché non è generalizzato qui

Il caso è uno solo (`nixos`, un file). Non basta a distinguere un pattern
vero da un'eccezione locale, né a proporre nomi per le specie mancanti:
serve un secondo caso reale (altro adottante, o un secondo file nello stesso
repo) prima che valga la pena formalizzare — stessa cautela già praticata
per «il criterio del significato senza artefatto» in `world.md`.

Nessun verdetto qui (i1 è valenza-neutro): se questa sia una seconda specie
di i1 da nominare, se la tassonomia dei register vada estesa a tutti gli
stadi, e con quali nomi, è valutazione i2→i3 in `method`.
