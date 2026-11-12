---
sintesi: "Costruiti il 2026-11-12 o3/dinieghi.py, che conta per classe di grafia i dinieghi ricorrenti fra repo con l'esito sul segnale canonico, e o3/ultimo_giro.py, lo strumento che toglie la grafia più ricorrente; prescrizione ultimo-giro ai sette. Verifica su un giro vero di method riuscita il 2026-11-12; resta la classe parentesi da mappare su de3fe56 in SEGNALI, poi la chiusura in sessione."
ciclo: dev
---

# Ricorrenza dei dinieghi

## Origine

Nasce il 2026-10-27 da un coordinamento fra la sessione `method` e la
sessione `nixos` su `deck`, via Herdr, su richiesta del custode. Il giro di
`nixos` della notte (`nixos` `28090d8`) ha pagato tre dinieghi: due volte
`gh issue view`, che non è negli allow, con ripiego su WebFetch, e un
`git commit -F - <<EOF && git log`. Negli ultimi dieci giri di `nixos` erano
già comparse graffe `{a,b}` (22 e 26 ottobre), un heredoc `python3` e un
messaggio di commit in `/tmp` (24 ottobre).

Oggi il passo 4 del perceive (skill `eval`, `5de8edb`) legge solo i dinieghi
dell'ultimo giro vero. La memoria durevole di un diniego che ricorre è il
segnale nella skill, come le grafie in `/cycle` (`e88d81f`), oppure il
permesso chiuso in sessione col custode. Manca però il passo che si accorge
della ricorrenza: `e88d81f` è nato perché una sessione ha messo insieme a
mano i giri di `method`, `nixos` ed `economia` dal 20 al 26 ottobre.
Rileggere a ogni avvio gli ultimi N giri costerebbe contesto e riproporrebbe
diagnosi già chiuse: per questo il custode vuole uno script deterministico,
non una lettura del modello.

## Le tre precisazioni di `nixos`

1. **Prima il recepimento, poi la regola.** Una parte della ricorrenza è
   ritardo di recepimento. Le graffe sono ricomparse in `nixos` il 26
   ottobre, quando `5de8edb` e `771388b` erano canone dal 22, ma `nixos` non
   li aveva ancora recepiti. Prima di proporre una regola nuova si verifica
   se esiste già un segnale canonico che l'adottante non ha recepito. In quel
   caso l'azione è `/method`, non una regola in più.
2. **Stesso diniego vuol dire stessa grafia.** Si confronta per classe di
   grafia, non per comando: heredoc, graffe, composto (`;`, `&&`, `|` verso
   un comando non concesso), `for`, `python3 -c`, fuori perimetro
   (scrittura o lettura fuori dal checkout). La ricorrenza conta anche fra
   repo diversi, come per `e88d81f`.
3. **Il conteggio lo fa uno script.** `tentativi.jsonl` porta già in ogni
   chiusura il campo `dinieghi`, una lista di `{tool, input}` col comando
   negato alla lettera. Uno script deterministico, sul modello di
   `maintenance-due.sh` di `nixos`, raggruppa per classe gli ultimi N giri e
   restituisce solo le ricorrenze, in poche righe. Il giro legge l'output,
   non i giri.

## La proposta da costruire

- **Lo script.** In `o3/`, accanto a `adottanti.py` e `prescrizioni.py`,
  concesso per nome in `o3/ciclo/permessi.json`. Legge le chiusure con giro
  non nullo dei repo con ciclo autonomo (`world.md`, cartella `i1/giri` o
  stato dell'unità), assegna a ogni diniego una o più classi con regole
  sulla grafia e stampa una riga per classe ricorrente: classe, numero di
  giri, repo, date. Una classe non riconosciuta si stampa come «altro», col
  comando, perché una grafia nuova è proprio ciò che il giro deve vedere.
  Candidata alla mappa: le parentesi non quotate in un argomento, come
  `--grep=^docs(ciclo)`. Il comando non è valido in bash e l'harness lo
  nega, mentre la forma fra virgolette passa. È ricorsa nei giri di
  `method` del 03/11 (causa accertata in `fc73956`), dell'08/11 e di nuovo
  nel giro a mano dell'08/11, due volte su comandi che la skill scrive
  quotati, ciascuna al costo di un rilancio; il
  diniego di `economia` del 03/11 su un `git log --format` non quotato è
  forse della stessa classe, da verificare. È un errore di scrittura
  dell'agente, non un permesso mancante. Il 2026-11-09 torna in quattro repo
  nello stesso giorno, dalle righe di chiusura: `nixos` e `economia`
  sull'ultimo `docs(ciclo)`, `salute` sul `Prossimo:`, `method` col primo
  `git log` degli eventi, rilanciato fra virgolette. La `eval` e la `exec`
  canoniche lo scrivono quotato; i fork non sono riletti. Per la decisione
  «Ricorrenza dopo il recepimento» la proposta è uno strumento, non un'altra
  frase: un comando concesso per nome che stampi l'ultimo commit del giro e
  l'ultimo `Prossimo:`, così la grafia non serve più. Si decide in sessione,
  insieme allo script.
- **Il segnale già canonico.** Per ogni classe ricorrente lo script dice se
  un commit di `method` la segnala già e se l'adottante l'ha recepito, dal
  cursore del marker `i3/allineamento-metodo.md` confrontato con
  `o3/canone.py distanza`. Se il segnale c'è e l'adottante è indietro,
  l'esito è «recepire con `/method`». Un recepimento puntuale senza
  avanzamento del cursore, come `nixos` `a20ab32` per `e88d81f`, il cursore
  non lo vede: lo script deve leggerlo dal marker o dichiararlo come limite.
- **L'esito nel giro.** Il passo 4 del perceive aggiunge la lettura
  dell'output. Una ricorrenza senza segnale canonico diventa una proposta in
  questo task o in quello pertinente, e si chiude in sessione col custode
  (prescrizione `ciclo-autonomo`, punto 7, chiusa il 2026-10-28 e in git):
  il giro non scrive la skill né
  `permessi.json`.

## Decisioni del custode, 2026-10-27

Proposte da `nixos` e approvate dal custode, arrivate via Herdr.

- **N e soglia.** Una classe è ricorrente quando compare in almeno due giri
  distinti, anche di repo diversi, fra gli ultimi dieci di ogni repo.
- **Ricorrenza dopo il recepimento.** Pesa di più una classe che ricorre
  anche dopo che l'adottante ha recepito il segnale canonico: la regola nel
  punto d'uso non basta. La proposta diventa allora un permesso o uno script
  che renda inutile la grafia, non un'altra frase nella skill. Lo script
  distingue quindi tre esiti: segnale canonico assente, segnale non
  recepito (`/method`), segnale recepito e ricorrenza che continua.
- **Più grafie in un comando.** Il comando conta in ogni sua classe: lo
  script resta deterministico, e con una riga per classe il doppio
  conteggio non fa danni. La classe di grafia si legge dal comando negato;
  la classe del diniego (vincolo voluto, lacuna, attrito) e la causa
  accertata restano al perceive (`5de8edb`, `kb/agent-as-user.md`).
- **La mappa dei segnali.** La mappa che va dalla classe al commit di
  `method` che la segnala vive nello script, come costante coperta dai
  test. È canone, non un parametro degli adottanti, e un file di dati
  sarebbe una seconda fonte da tenere allineata. `kb/agent-as-user.md`
  spiega e rimanda allo script.
- **Repo fuori da `deck`.** Si contano solo i repo leggibili, ma l'output
  dichiara quali ha letto, così il limite resta visibile.
- **Il gesto abbandonato.** Resta al passo 4 del perceive, che confronta il
  diniego col tentativo che lo segue: da `tentativi.jsonl` lo script non lo
  vede.

## Fuori da questo task

- La sonda delle grafie con `claude -p` e i settings del giro: è un task
  locale di `nixos` (`nixos` `bcf4b26`), che gestisce host e versione di
  Claude Code. Esiti del 2026-10-28 su 2.1.311 (`nixos` `91f6ef2`, 21
  prove, inoltrati via Herdr): negate graffe, `cd` dentro un composto,
  `$(…)`, `for` e heredoc unito a `&&`; concessi `;` e `&&` fra comandi in
  allow, pipe, redirezioni, heredoc da solo, `-m` ripetuti, graffe e pipe
  fra virgolette. Per lo script: la classe composto vale solo con un pezzo
  non concesso, e l'heredoc conta come classe solo dentro un composto.
- Gli allow `gh issue view` e `gh pr view` per `nixos`: lacuna locale,
  chiusa nel `permessi.json` di `nixos` (`bcf4b26`).

## Stato, 2026-11-12

Costruito in sessione col custode:

- `o3/dinieghi.py` coi test (`tests/test_dinieghi.py`), mappa dei segnali
  compresa, concesso nei permessi del giro e lanciato al passo 4 del
  perceive della skill `eval`, in `metodo` soltanto: il conteggio fra repo
  è il lavoro dell'osservatorio, e negli adottanti leggerebbe i dinieghi di
  `salute` ed `economia` da un giro altrui. Per questo non si prescrive.
  `kb/agent-as-user.md` vi rimanda.
- Prima uscita, sugli ultimi dieci giri di `method`, `nixos`, `salute` ed
  `economia`: `parentesi` in 13 giri e quattro repo, senza segnale;
  `non-concesso` in 4 giri; `fuori-perimetro` in 2, recepita in `method` e
  non in `nixos`. Le parentesi sono quasi tutte le due letture che aprono il
  giro, e la regola quotata delle skill non bastava.
- Da qui `o3/ultimo_giro.py`, la proposta di questo task per la
  «ricorrenza dopo il recepimento»: ultimo giro, `Esiti:` e ultimo
  `Prossimo:` senza grafie da quotare. Lo usano `eval compare` ed
  `exec plan`; la prescrizione [ultimo giro](../o3/ultimo-giro.md) lo porta
  ai sette.
- Limiti dell'uscita, dichiarati dallo script: permessi di oggi e non di
  allora (il `printenv` di `economia` dell'08/11 è concesso oggi), abbinamento
  dei pattern che imita l'harness, giri di `svezia` e `danea2` non letti.
  Le grafie negate da Codex escono col motore, perché le traduce
  l'esecutore.

## Criterio di chiusura

Fatto il 2026-11-12, salvo l'ultima condizione: lo script è in `o3/` coi
test, concesso e letto dal passo 4 del perceive; `kb/agent-as-user.md` vi
rimanda; la prescrizione `ultimo-giro` porta agli adottanti lo strumento
nato dalla prima uscita. Resta che un giro di `method` ne abbia usato
l'output e che le sue due letture d'apertura passino senza dinieghi. Riga del plan, voce in `o2/tasks.md` e questo file si
rimuovono nello stesso commit.

Verifica sul giro schedulato del 2026-11-12 (tentativo `1627c9a5`): il
perceive ha letto l'uscita di `o3/dinieghi.py`, e `o3/ultimo_giro.py` e
`git log --oneline dc6e902..HEAD` sono passati al primo tentativo, senza
dinieghi in tutto il giro. La condizione è soddisfatta. Il giro non chiude
il task per un residuo che tocca uno strumento in `o3/`, fuori dal suo
perimetro: in `SEGNALI` di `o3/dinieghi.py` la classe `parentesi` resta
`None`, quindi l'uscita la dà «segnale assente: proposta in o2/» finché la
classe resta nella finestra di dieci giri, benché lo strumento proposto
(`o3/ultimo_giro.py`, `de3fe56`) esista. Proposta: mapparla su `de3fe56`
col suo test in `tests/test_dinieghi.py`, poi chiudere il task in sessione.

Connessioni:

- [agent-as-user](../kb/agent-as-user.md)
- [ciclo-autonomo](../i3/ciclo-autonomo.md)
