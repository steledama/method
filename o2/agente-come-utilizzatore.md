---
sintesi: "Il canone tratta l'agente come utilizzatore a pieno titolo (kb/agent-as-user.md); resta la revisione di method e degli adottanti, dominio per dominio: dinieghi classificati, cartelli censiti, skill a nucleo breve, permessi allineati ai gesti richiesti."
ciclo: dev
---

# Agente come utilizzatore

## Origine

Segnalazione della sessione `nixos` su `deck`, inoltrata via Herdr il
2026-10-21 su richiesta del custode, con priorità primaria. Il custode ha
approvato in sessione la forma: nodo nuovo `kb/agent-as-user.md`, rimandi in
`affordance-signifier`, `constraint`, `claude`, `skill`, `perceive` e nel punto
8 di `o3/ciclo-autonomo.md`, revisione degli adottanti via `/method` con un
task `o2/` per repo. Il caso di partenza e il modello del task locale sono in
`nixos` `o2/design-agent-as-user.md` (giro del 2026-10-21, `5da4549`).

## Revisione per repo

Ogni repo apre un task `o2/` proprio, quando `/method` recepisce il nodo, e
controlla quattro cose:

- dinieghi storici di `i1/giri/tentativi.jsonl` classificati, per contesto,
  come vincolo voluto o lacuna; ogni lacuna chiusa su permesso o strumento;
- censimento dei cartelli in skill, prompt e `CLAUDE.md` («non usare», «non è
  concesso», «è negato»): vincolo da tenere col suo deny, oppure lacuna;
- peso delle skill rilette a ogni run e rami che possono vivere in file
  separati;
- permessi confrontati coi gesti richiesti, separando sessione e giro.

Ordine, dall'evidenza raccolta il 2026-10-21 dai log locali di `deck`:

1. `method`: 12 dinieghi in due giri (2026-10-20, 07:20 e 15:03).
   Classificazione:
   - lacuna, dieci: letture di storia e interfaccia degli adottanti
     (`git -C <adottante> log|show`, `grep` su `CLAUDE.md`, `tail` del
     reflog, `ls` fuori dalla cartella). Chiusa il 2026-10-21 in sessione
     col custode con `o3/adottanti.py` (`stato`, `log`, `show`), di sola
     lettura e consentito nel giro e in sessione; tolti dagli allow i
     quattro `git -C … show origin/main:i3/allineamento-metodo.md`, ora
     coperti da `show`. `show` legge solo l'interfaccia col canone: il resto
     del dominio degli adottanti resta un vincolo voluto, segnalato
     dall'uscita dello script;
   - vincolo voluto, due: `grep` e `Read` di `o3/cicli.nix` di `nixos` per
     l'orario dei timer. Il prompt indica già la fonte nel perimetro, le
     righe `partenza` di `tentativi.jsonl`.

   Resta da verificare sul primo giro dopo il pull: nessun diniego di
   lettura sugli adottanti. Poi il censimento delle skill canoniche (`eval`
   245 righe, `exec` 235) e dei cartelli.

2. `nixos`: pilota in corso, task `o2/design-agent-as-user.md`.
3. `salute`: 10 dinieghi in tre giri; `eval` 415 righe.
4. `economia`: 3 dinieghi in due giri; `eval` 676 righe.
5. `bi`: 2141 righe di skill in totale; log dei giri su `svezia`.
6. Gli altri adottanti.

## Misura

L'audit `/adottanti` del 2026-11-01 aggiunge per repo due segnali di distanza:
dinieghi-lacuna per giro e righe di skill rilette a ogni run.

## Criterio di chiusura

Ogni adottante ha recepito il nodo nel marker e ha chiuso o ricondotto a task
propri le quattro voci; `method` ha chiuso la propria lacuna di lettura. Riga
del plan, voce in `o2/tasks.md` e questo file si rimuovono nello stesso commit.

Connessioni:

- [agent-as-user](../kb/agent-as-user.md)
- [ciclo-autonomo](../o3/ciclo-autonomo.md)
- [audit-adottanti](../i3/audit-adottanti.md)
