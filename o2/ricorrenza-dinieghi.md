---
sintesi: "Un diniego che ricorre nei giri autonomi, anche fra repo diversi, diventa una proposta in o2: lo conta uno script per classe di grafia, e prima di proporre una regola nuova si verifica se c'è un segnale canonico che l'adottante non ha recepito."
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
- **Il segnale già canonico.** Per ogni classe ricorrente lo script dice se
  un commit di `method` la segnala già e se l'adottante l'ha recepito, dal
  cursore del marker `i3/allineamento-metodo.md` confrontato con
  `o3/canone.py distanza`. Se il segnale c'è e l'adottante è indietro,
  l'esito è «recepire con `/method`».
- **L'esito nel giro.** Il passo 4 del perceive aggiunge la lettura
  dell'output. Una ricorrenza senza segnale canonico diventa una proposta in
  questo task o in quello pertinente, e si chiude in sessione col custode
  (`o3/ciclo-autonomo.md`, ricetta, punto 7): il giro non scrive la skill né
  `permessi.json`.

## Domande aperte

- **N e soglia.** Quanti giri si guardano, e quante ricorrenze fanno un
  segnale? La proposta di partenza è almeno due giri, anche di repo diversi,
  negli ultimi dieci per repo.
- **Classe e causa.** La classe di grafia si legge dal comando negato, la
  causa accertata viene dal tentativo riuscito che lo segue (`5de8edb`,
  `kb/agent-as-user.md`). Lo script conta la grafia; la classe del diniego
  (vincolo voluto, lacuna, attrito) resta al perceive. Un comando con più
  grafie, come un `for` composto con `python3 -c`, conta in ogni classe o
  in una sola?
- **La mappa dei segnali.** Quale classe è già segnalata da quale commit di
  `method`, e dove vive questa mappa: nello script, in `kb/agent-as-user.md`
  o in un file di dati in `o3/`?
- **Repo fuori da `deck`.** I `tentativi.jsonl` di `svezia` e Windows non
  sono leggibili da `deck` (`i3/ciclo-autonomo.md`): la ricorrenza fra repo
  conta solo quelli serviti dallo stesso host?
- **Il gesto abbandonato.** Lo script vede solo i dinieghi, non i gesti
  abbandonati dopo un diniego, che sono la perdita vera
  (`kb/agent-as-user.md`). Basta, o serve un segnale anche per quelli?

## Fuori da questo task

- La sonda delle grafie con `claude -p` e i settings del giro: è un task
  locale di `nixos`, che gestisce host e versione di Claude Code.
- Gli allow `gh issue view` e `gh pr view` per `nixos`: sono una lacuna
  locale, da chiudere in sessione sul `permessi.json` di `nixos`.

## Criterio di chiusura

Lo script è in `o3/` coi test, concesso nel `permessi.json` di `method`,
letto dal passo 4 del perceive nella skill `eval`. La ricetta di
`o3/ciclo-autonomo.md` lo prescrive agli adottanti. Un giro di `method` ne ha
usato l'output. Riga del plan, voce in `o2/tasks.md` e questo file si
rimuovono nello stesso commit.

Connessioni:

- [pilota-ciclo-autonomo](pilota-ciclo-autonomo.md)
- [agent-as-user](../kb/agent-as-user.md)
- [ciclo-autonomo](../i3/ciclo-autonomo.md)
