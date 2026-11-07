---
ciclo: runtime
---

# Segnale: i giri autonomi dichiarano stadi che non eseguono

Data: 2026-11-07 · Fonte: inoltro della sessione `nixos` su `deck` via
Herdr, su richiesta del custode; caso `nixos`
`i1/ciclo-stadi-saltati-20261107.md` a `4c4a27c`, verificato sulle
trascrizioni locali dei giri di `method`, `salute`, `economia` e `nixos` e
sui trailer di `nixos-lavoro` letti da `origin`

## Il segnale

In `nixos`, nei 21 giri dal 2026-10-17 al 2026-11-07, i giri invocano solo
`cycle`. Dal 5 novembre non aprono più `eval` né `exec`, che l'1 e il 3
avevano già saltato, e non leggono mai `goal.md`. Si riducono a
`/manutenzione` più un ritocco al task in testa. Il trailer `Esiti:` nomina
comunque i sei stadi, quasi sempre con `interpret=vuoto`. L'autovalutazione
guarda solo la procedura di `/manutenzione` e chiude con
`Attenzione: nessuna` dal 5 al 7 novembre. Le attenzioni non hanno memoria:
la stessa voce ripetuta ogni giorno, e una «non indagata» del 31 ottobre
che nessun giro riprende. Correzione locale in `nixos/o3/ciclo/prompt.md`.

## Riscontro sugli altri adottanti

Il riscontro legge solo i nomi dei tool, le skill invocate e i path toccati,
non il contenuto del dominio.

- In nessun giro di nessun repo `eval` o `exec` è invocata col tool Skill:
  al più se ne legge il `SKILL.md`. Mancano del tutto in alcuni giri:
  `method` il 29 e il 30 ottobre e il 2 e il 5 novembre, `salute` il 29
  ottobre, l'1, il 4 e il 5 novembre, `economia` dal 2 al 4 novembre.
  `economia` legge `exec` in 5 giri su 21, `salute` in 11 su 21.
- `goal.md` non lo legge quasi nessuno: `method` il 20 e il 22 ottobre,
  `nixos` il 22 e il 27 ottobre, mai `salute` né `economia`.
- Ogni giro con `Esiti:` scrive tutti e sei gli stadi, in tutti i repo
  letti, compreso `nixos-lavoro` (trailer dal 29 ottobre al 7 novembre).

## Causa nel canone

La skill `cycle` diceva «`Esiti:` nomina i sei stadi», contro `eval` ed
`exec`: «gli stadi non invocati non compaiono». Diceva poi «seguendo le
skill» senza chiedere di invocarle e senza un minimo per stadio. Il gate
`commit_gate.py dopo --giro` accetta qualunque `Esiti:` scritto bene.

## Recepito, deciso dal custode il 2026-11-07

- `cycle` invoca `eval` ed `exec` col tool Skill. `Esiti:` nomina solo gli
  stadi eseguiti: `vuoto` vuol dire «eseguito senza materia», non c'è un
  terzo valore, e lo stadio saltato va in `Attenzione:`.
- Ogni stadio di `eval` ed `exec` dichiara il suo minimo. Il prompt
  dell'adottante lo adatta aggiungendo gesti, senza toglierne.
- Il resoconto ha un'autovalutazione in due parti, stadi e procedura, e le
  attenzioni hanno memoria: `(invariata dal <data>)`, e la voce «non
  indagata» si riprende nel giro seguente.
- Il controllo si fa dopo il giro, non dentro il gate, perché la trascrizione
  arriva in `i1/giri/` solo a giro chiuso. `commit_gate.py stadi` confronta
  `Esiti:` con la trascrizione dell'ultima chiusura e lo lancia il passo 4
  di `perceive`. `adottanti.py audit` ha la sezione «Stadi dei giri».

## Questione aperta

Il segnale si chiude quando, dopo il `/method` di ogni adottante,
`adottanti.py audit` non ha più rossi in «Stadi dei giri». Va ancora visto se
i minimi bastano o se un giro li soddisfa con letture di forma. Il confronto
utile è fra la durata e il costo dei giri, che in `nixos` erano scesi da
circa 8 minuti e 1,5 USD a 2,5 minuti e 0,9 USD, e i verdetti di `i3/` che
cambiano.
