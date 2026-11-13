---
sintesi: "Il fetch.json che il giro di method legge non si rinnova dall'11/11 (id 47567de9) e porta solo i quattro repo di lavoro, senza clone su deck dal 2026-11-12. Da verificare in sessione nel campo fetch di o3/cicli.nix di nixos; poi decidere se il prompt del giro tiene la lettura o la toglie."
ciclo: dev
decidere: "Togliere da o3/ciclo/prompt.md la lettura di fetch.json, se l'unità non fa più il fetch, o riportarla sui checkout locali di deck?"
---

# Fetch del giro di method

## Origine

Il giro del 2026-11-12 ha segnato `fetch.json` come non rinnovato e lo ha
lasciato «non indagato». Il giro del 2026-11-13 lo riprende.

## Fatti

- `~/.local/state/ciclo/method/fetch.json` porta l'id `47567de9`, il
  tentativo a mano dell'11/11 alle 18:21, mentre la partenza del giro del
  13/11 è `a97ef3b7` (15:00:07). I giri del 12 e del 13/11 non lo hanno
  riscritto.
- Elenca `bi`, `baserow`, `danea-auto` e `nixos-lavoro`, cioè i repo che dal
  2026-11-12 non hanno un clone su `deck` (custode, `o3/ciclo/prompt.md`,
  «Adottanti»), e nessuno dei checkout locali (`nixos`, `economia`,
  `salute`).
- Il 2026-11-13 i checkout locali hanno `HEAD` uguale a `origin/main`, con
  commit del giorno fatti su `deck`: per loro l'età di `origin` conta poco.
  Gli altri si leggono con `--ssh`, e lì `origin/main` è quello dell'ultimo
  fetch fatto sul loro host.

## Da verificare

L'ipotesi sulla causa vive nel filo
[ciclo autonomo](../i3/ciclo-autonomo.md), «Copertura». Il passo in
sessione è leggere il campo `fetch` dell'unità `ciclo-method` in
`o3/cicli.nix` di `nixos`: il giro non può, il Read di quel file è fuori dai
suoi permessi.

## Alternative

- **Togliere la lettura**: il prompt non cita più `fetch.json` e dichiara
  l'età di `origin` solo per i repo letti con `--ssh`.
- **Riportarla sui checkout locali**: il campo `fetch` elenca `nixos`,
  `economia` e `salute`, e il prompt resta com'è.

Decisione richiesta al custode: quale delle due, dopo aver letto il campo in
`nixos`.
