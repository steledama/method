---
sintesi: "Un server su richiesta, identico in ogni repo, per aprire la presentazione dagli altri PC della LAN: o3/presentation/serve.py, Python senza dipendenze esterne, perché danea-auto gira su Windows e un comando di host via nixos lo escluderebbe. Pubblica solo presentation/, chiusa su se stessa."
ciclo: dev
---

# Server LAN della presentazione

Quarto task della ristrutturazione della presentazione (2026-10-02). Dipende da
[presentazione-autonoma-e-uniforme](presentazione-autonoma-e-uniforme.md):
servire solo `presentation/` ha senso quando nessun link esce dalla cartella.

## Decisioni del custode (2026-10-02)

- **Script per repo, non comando di host.** Un comando installato da
  `nixos` sarebbe più elegante, ma la piattaforma di `danea-auto` è Windows,
  quindi lo script deve essere multipiattaforma: Python, solo libreria
  standard.
- **Si pubblica solo `presentation/`**, la superficie minima. La cartella
  è chiusa su se stessa e la rende possibile il task precedente.
- **Su richiesta:** si avvia, si usa, si chiude con Ctrl-C. Non è un
  servizio permanente, e il «Vincolo conservato» di `kb/presentation.md`
  resta intatto.

## Forma

- **Path di canone**: `o3/presentation/serve.py`, identico nei sei repo
  (decisione del custode, cfr.
  [presentazione-autonoma-e-uniforme](presentazione-autonoma-e-uniforme.md)).
  Il comando è `python3 o3/presentation/serve.py`, su Windows
  `py o3\presentation\serve.py`. La fonte resta in `o3/`, e `presentation/`
  resta fatta di file generati più gli asset.
- **Comportamento:** ascolta su `0.0.0.0` (con `--bind` per restringere),
  usa una porta fissa poco comune (per esempio 8765, con `--port` per
  cambiarla), stampa gli URL raggiungibili sulla LAN, serve solo file sotto
  `presentation/` e rifiuta i dotfile.

## Firewall

- Per i PC della LAN la porta deve essere aperta sull'host che serve.
- Su `svezia` e `deck` (NixOS) il firewall è dichiarativo. La via proposta
  è aprire la porta in modo dichiarativo, solo verso la LAN, nel repo
  `nixos`: finché lo script non gira, sulla porta non ascolta nessuno.
  L'atto spetta a `nixos` e gli arriva come segnale, non lo scrive `metodo`.
- Su Windows (`danea2`) la prima esecuzione apre il prompt del firewall:
  va documentato, non automatizzato.

## Canone da toccare

- `kb/presentation.md`, sezione «Apertura locale e condivisione on-demand»:
  il comando uniforme prende il posto di `python3 -m http.server`.

## Criterio di chiusura

Da un altro PC della LAN si apre `metodo` all'URL stampato dallo script, con
viste e navigazione funzionanti. Lo stesso comando parte senza modifiche su
Linux e su Windows.
