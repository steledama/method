---
ciclo: runtime
---

# Segnale: il giro di `method` del 2026-10-20 contro il suo prompt

Data: 2026-10-20 · Fonte: giro autonomo di `method` (partenza alle 07:17,
`i1/giri/tentativi.jsonl`), esito dei comandi riportato dall'harness;
`tentativi.jsonl` di `nixos` in `~/nixos/i1/giri/`

## Il segnale

Due righe del prompt `o3/ciclo/prompt.md` non reggono nell'esercizio.

- **Fetch dei repo di `svezia`.** Il prompt chiede
  `git -C /home/stele/<repo> fetch --quiet origin` per `bi`, `crm`,
  `baserow` e `danea-auto`. I permessi lo concedono, ma tutti e quattro
  falliscono con `error: impossibile aprire '.git/FETCH_HEAD': File system in
sola lettura` (codice 255): nel recinto dell'unità i checkout degli altri
  repo sono in sola lettura, e il fetch deve scrivere in `.git/`. È il primo
  giro che esegue la riga, aggiunta il 2026-10-19: il giro del 19 si era
  fermato per la sessione aperta. `git show origin/main:…` funziona, ma
  legge l'`origin` noto al checkout, non quello di oggi. Anche `git log` su
  quei checkout è negato.
- **Orario di `nixos`.** Il prompt mette il giro di `method` «un'ora dopo
  `nixos`», cioè alle 14:00. `tentativi.jsonl` di `nixos` mostra invece le
  partenze schedulate del 2026-10-19 e del 2026-10-20 alle 04:30. Il
  2026-10-19 il giro è riuscito, con commit e push. Il 2026-10-20 si è
  fermato perché c'era una sessione aperta, e poi è ripartito alle 07:17,
  insieme a quello di `method`: fuori orario, avviati a mano dal custode
  (confermato in sessione il 2026-10-20). Il commit che ha spostato l'orario non è
  verificato: la lettura di `nixos` `o3/cicli.nix` è negata nel giro.

## Cosa resta fuori

I marker di `svezia` letti da `origin` noto (`bi` a `8b61b63`, `baserow` a
`735d7f7`, `crm` a `70a5825`, `danea-auto` a `d8a88e7`) non dicono se quei
repo hanno pubblicato commit dopo l'ultimo fetch fatto in sessione. Il giro
non ne deduce uno stato.

## Stato del seguito

Proposta al custode in `o2/pilota-ciclo-autonomo.md`, «Andamento»: il prompt
e il recinto vanno corretti in `o3/ciclo/` e in `nixos`, fuori dal giro.
Deciso il 2026-10-20 in sessione: fetch in un passo dell'unità prima del
giro (alternativa 3), prompt corretto anche sull'orario.
