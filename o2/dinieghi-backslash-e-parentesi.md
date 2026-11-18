---
sintesi: "o3/dinieghi.py chiede dal giro del 16/11 una proposta su due classi: backslash, senza segnale canonico, in due giri di method; parentesi, recepita da nixos e ricorsa il 16/11. Decidere se segnalarle nella skill cycle, chiuderle con uno strumento o lasciarle come attrito contato."
ciclo: dev
decidere: "Le classi backslash (senza segnale) e parentesi (ricorsa in nixos dopo il recepimento) si chiudono con una riga in cycle, con uno strumento, o restano attrito contato?"
---

# Dinieghi: backslash e parentesi

## Origine

Giro autonomo del 2026-11-16. `python3 o3/dinieghi.py` dà due classi che
chiedono una proposta in `o2/` (`eval`, `perceive`, passo 4):

- `backslash`, 2 giri fra gli ultimi dieci, entrambi di `method`, il 09 e il
  15/11: «segnale assente: proposta in o2/». Al conteggio del giro del 15/11 il
  caso era uno solo, perché la chiusura di quel giro si scrive dopo;
- `parentesi`, recepita con `ultimo_giro.py` (`de3fe56`), ricorre in `nixos`
  il 16/11: «recepito e ricorre: serve un permesso o uno strumento».

Il task sulle classi `non-concesso` e `fuori-perimetro` è chiuso dal custode
il 15/11 (`59f97f2`) e non copre queste due.

## I dinieghi contati

Letti nelle chiusure di `i1/giri/tentativi.jsonl` di `method` e `nixos`:

- `backslash`, `method`: `git log --format=%h\ %ad\ %s …` nel giro del
  09/11 e `git log --format=%h\ %ad\ %s%n%b --date=short -2 -- …` in quello
  del 15/11. Causa accertata dal giro del 15/11 (corpo di `fbcd776`): lo
  stesso comando con il formato fra virgolette è passato. Attrito
  dell'harness, un turno per volta;
- `parentesi`, `nixos`: `git log --since='7 days ago' --grep=^docs(ciclo)
--format='%h %ad%n%b' --date=short` nel giro del 16/11, con la parentesi
  fuori dalle virgolette. Il segnale `de3fe56` è uno strumento di `method`,
  `o3/ultimo_giro.py`, che legge l'ultimo giro e non i corpi della
  settimana richiesti da `exec plan`. La congettura del 16/11
  sull'apertura del giro è smentita dal comando stesso; riesame e
  interpretazione stanno nel filo [ciclo autonomo](../i3/ciclo-autonomo.md).

## Al giro del 18/11

`o3/dinieghi.py` non chiede più una proposta per nessuna delle due:
`backslash` non compare, perché il giro del 09/11 è uscito dagli ultimi
dieci di `method` e resta il solo 15/11; `parentesi` è «recepito dopo e
senza ricorrenze in method, nixos, salute: in osservazione». La decisione
resta aperta, ma oggi coincide nei fatti con l'alternativa 3; un nuovo caso
di una delle due classi la riporta allo stato del 16/11.

## Alternative

1. **Una riga in `cycle`.** «Avvio» elenca già graffe, `for`, `$(…)`,
   heredoc: si aggiungono il backslash fuori dalle virgolette e la parentesi
   non quotata, con la forma che passa (argomento fra virgolette). È una
   modifica alla skill canonica, quindi proposta; arriva agli adottanti col
   loro `/method`.
2. **Uno strumento.** `ultimo_giro.py` copre già l'apertura; per eliminare
   il comando contato serve una lettura dei corpi dei giri della settimana,
   non solo degli eventi dall'ultimo giro. Un eventuale strumento deve
   conservare quella finestra e i corpi, con formato fisso, e avere un
   comando concesso nel fork dell'adottante. La correzione discende dal
   riesame nel filo ciclo autonomo, non cambia la priorità della proposta.
3. **Attrito contato.** Le due classi restano nel conteggio di
   `o3/dinieghi.py` senza proposta: costano un turno e il tentativo seguente
   riesce. Allora `SEGNALI` le marca come attrito noto, perché il giro non
   le riporti ogni giorno.

Motivo per decidere ora: senza una scelta, il giro le conta ogni giorno e la
richiesta di proposta resta senza esito, come per le due classi chiuse il
15/11.

## Decisione richiesta

Il custode sceglie fra le tre alternative, anche combinate (1 per
`backslash`, 2 per `parentesi`). Il giro non scrive né skill, né
`o3/dinieghi.py`, né permessi.
