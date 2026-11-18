---
sintesi: "Dichiarare per il giro autonomo di method su deck il confine di esecuzione nella forma del contratto di kb/consent.md (15f4d3f): dati, percorsi, rete e credenziali necessari ed esclusi, meccanismo, evidenza sulla configurazione effettiva, condizioni di riesame."
ciclo: dev
---

# Confine del giro

## Origine

Giro autonomo del 2026-11-18. Il custode fissa in `15f4d3f` il contratto
«Delega e confine di esecuzione» ([consent](../kb/consent.md)) e la sua
attuazione nel lanciatore ([engine fallback](../o3/ciclo/fallback.md),
«Execution boundary and portability»), su due riscontri della sessione
`nixos` dichiarati nel commit: un'unità con l'identità dell'utente ha avviato
un'unità utente fuori dal proprio mount namespace e letto un file fittizio
mascherato; `.env.*` espanso all'avvio non vede i file creati dopo. Il
verdetto sta nel filo [ciclo autonomo](../i3/ciclo-autonomo.md), «Confine di
esecuzione».

Il contratto chiede a ogni esecuzione autonoma di rendere espliciti
capacità, meccanismo, evidenza e condizioni di riesame. Per il giro di
`method` oggi ci sono la delega (`autonomy.md`) e i deny di
`o3/ciclo/permessi.json`, che per il contratto non provano l'isolamento;
una dichiarazione del confine non c'è (ricerca su `o3/ciclo/`, `world.md` e
`autonomy.md` del 2026-11-18).

## Che cosa serve

- **Visibilità**: una dichiarazione del confine del giro di `method`, nel
  repo, con i punti del contratto: dati, percorsi, servizi, rete e
  credenziali necessari ed esclusi; meccanismo e ambiente; minacce e limiti
  noti.
- **Mapping**: il meccanismo vive nel modulo `cicli` di `nixos` su `deck`;
  `method` dichiara ciò che il suo giro richiede e rimanda all'evidenza
  dell'host, senza ricopiarla.
- **Feedback**: l'evidenza è riferita alla configurazione effettiva, con le
  prove che il contratto elenca secondo il rischio; un requisito non
  verificato resta dichiarato tale.
- **Vincoli**: il giro non scrive `o3/`, prescrizioni né config dell'host;
  la dichiarazione e le prove si fanno in sessione col custode, dopo il
  lavoro di `nixos` sul recinto.

## Dipendenze

Segue il lavoro della sessione `nixos` sul recinto di `deck`, che il
contratto rende propedeutico. Nessuna attesa formale finché non si sa dove
quel lavoro produrrà l'evidenza.
