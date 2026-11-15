---
sintesi: "Le classi non-concesso e fuori-perimetro di o3/dinieghi.py chiedono una proposta da tre giri di method (12, 13 e 15/11) senza esito: decidere se sono lacune da chiudere con un permesso o uno strumento, o vincoli voluti che lo strumento non deve più portare in proposta."
ciclo: dev
decidere: "Le classi non-concesso e fuori-perimetro di o3/dinieghi.py sono lacune da chiudere con permessi o strumenti, o vincoli voluti da togliere dalla richiesta di proposta?"
---

# Dinieghi senza segnale

## Origine

Giro autonomo del 2026-11-15. `python3 o3/dinieghi.py` dà due classi che
chiedono un intervento:

- `non-concesso`, 4 giri fra gli ultimi dieci, in `economia` e `nixos`,
  dall'11 al 15/11: «segnale assente: proposta in o2/»;
- `fuori-perimetro`, 3 giri, in `economia`, `method` e `nixos`, il 13 e il
  14/11: «recepito e ricorre: serve un permesso o uno strumento».

I giri del 12 e 13/11 di `method` le hanno contate senza proporre (corpi di
`c12512c` e `558e437`). Il task sui dinieghi ricorrenti è chiuso dal custode
il 13/11 (`a40d4fb`) con la sola classe `parentesi`. Tre giri senza esito
(`exec plan`, passo 3c): la voce entra qui.

## I dinieghi contati

Letti nelle chiusure dei `tentativi.jsonl` di `method`, `nixos` ed `economia`:

- `non-concesso`, `economia`: `git ls-files` sulle bozze l'11 e il 13/11.
  Il giro del 14/11 ne ha accertato la causa, nessuna regola per
  `git ls-files`, e il custode lo ha risolto in sessione col prompt che usa
  `ls o3` (`economia` `fe90266`, 15/11);
- `non-concesso`, `nixos`: `gh issue list` il 09/11, `git -C` verso `method`
  il 14/11, `gh api repos/NixOS/nixpkgs/commits/nixos-unstable` il 15/11.
  `git -C` è vietato dalla skill `cycle`; le letture `gh` sono il canale
  world di `nixos` e mancano nei suoi permessi del giro;
- `fuori-perimetro`, `method`: Read di `~/nixos/o3/cicli.nix` il 13/11, il
  file che il prompt del giro nomina per il campo `giri`;
- `fuori-perimetro`, `nixos`: Read di
  `~/.local/state/presentazione/nixos.serve` il 14/11.

## Alternative

1. **Vincoli voluti.** `non-concesso` è un'allowlist locale dell'adottante,
   e una lettura fuori perimetro è vietata di proposito (`cycle`, «Avvio»).
   `o3/dinieghi.py` le riporta come fatti, senza chiedere una proposta in
   `method`; le lacune restano ai giri degli adottanti, come ha fatto
   `economia`.
2. **Lacune caso per caso.** Si propongono i permessi mancanti: le letture
   `gh` nel recinto di `nixos`, che `method` non scrive; per `method`, un
   Read di `~/nixos/o3/cicli.nix` in `o3/ciclo/permessi.json`, o il prompt
   che smette di nominarlo.
3. **Misto.** `non-concesso` passa all'adottante (alternativa 1),
   `fuori-perimetro` resta una proposta qui solo quando il prompt del repo
   nomina il file negato.

Motivo per decidere ora: senza una scelta, il giro conta le due classi ogni
giorno e la richiesta di proposta resta senza esito.

## Decisione richiesta

Il custode sceglie fra le tre alternative. Il giro non scrive né
`o3/dinieghi.py` né i permessi.
