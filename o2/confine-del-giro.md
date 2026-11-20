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

## Evidenza dell'host

Inoltro della sessione `nixos` del 2026-11-20, su richiesta del custode;
riferita, non riletta qui. In `nixos` su `origin/main`: lettura
`i2/confine-dei-cicli.md` (`bda240d`, aggiornata in `9ebc6f7` e `34865bc`),
filo `i3/confine-dei-cicli.md`, sintesi in `kb/cicli.md` § «Confine di
esecuzione», prove riproducibili con `o3/tools/prova-confine.sh <repo>`
(accessi, conteggi e metadati, nessun segreto letto), attuazione proposta in
`o2/chiudere-le-uscite-del-recinto.md` (`decidere:` al custode).

Prova su `ciclo-method` del 2026-11-20 alle 18:14. Reggono l'accesso diretto
ai file (home, `o3/ciclo` e `.git/hooks` in sola lettura, `rclone.conf` non
scrivibile, Drive in sola lettura) e le maschere `ReadOnly` e `Inaccessible`.
Escono: `systemd-run --user` (unità fuori dal recinto che leggono i
mascherati, scrivono i path in sola lettura e sopravvivono all'arresto),
`niri spawn`, il socket di Herdr, Secret Service col keyring sbloccato, la
chiave SSH senza passphrase con `ssh-agent` carico, la rete;
`~/.claude/skills`, `~/.codex/config.toml` e `method/.claude` scrivibili; una
maschera `-` non vale per un path creato dopo l'avvio; dati e `.env` di
`salute` leggibili. Verdetto di `nixos`: nessun confine dei cicli di `deck`
si può dichiarare pronto, `method` compreso; la delega dei giri non cambia.
Non verificati: host che accettano la chiave, invio effettivo in un pannello
Herdr, lettura effettiva di una voce del keyring, filtro di rete per
un'unità utente, prova con Codex, arresto dei processi usciti dal recinto.

## Che cosa il giro legge degli adottanti locali

Domanda di `nixos`: la misura minima, rendere inaccessibili i checkout che
un giro non usa, escluderebbe `~/salute` dal giro di `method`? Sì, e oggi il
giro lo usa (lettura di `o3/ciclo/prompt.md`, `o3/ciclo/permessi.json` e
`o3/adottanti.py` del 2026-11-20):

- `o3/adottanti.py` gira `git -C ~/salute` in sola lettura per `stato`,
  `log` e `show`; `show` legge solo i file dell'interfaccia col canone
  (`CLAUDE.md`, `AGENTS.md`, `autonomy.md`, marker, prompt e permessi del
  ciclo, skill). Il processo però raggiunge l'intero object store, dati
  compresi;
- i permessi concedono il Read di `salute/i3/allineamento-metodo.md`,
  `*/autonomy.md`, `*/o3/ciclo/prompt.md` e `*/i1/giri/` (tentativi e
  ultimo), e negano `Edit(salute/**)` e i trascritti `salute/i1/giri/giri/**`;
- l'audit mensile (`adottanti.py audit`) ricostruisce le viste di ogni
  adottante da `origin/main` in una cartella temporanea e ne legge i
  conteggi del plan, i nomi delle catture «da inoltrare» e, con
  `commit_gate.py stadi`, skill e path dei trascritti. La build passa per
  il contenuto del repo, non solo per l'interfaccia.

Dal 2026-11-20 `salute` non ha più giri autonomi, quindi tentativi e
trascritti non crescono. Restano marker e interfaccia, che servono a
`/method` e all'obiettivo 2. Escludere il checkout chiede a `method` di
leggerli altrove, per esempio da `origin` su GitHub o da un'esportazione
della sola interfaccia preparata dall'host, oppure di lasciare `salute` fuori
dal perceive del giro e leggerlo solo in sessione. La scelta tocca territorio
e delega del giro: resta al custode, insieme all'attuazione di `nixos`.

## Dipendenze

Segue il lavoro della sessione `nixos` sul recinto di `deck`, che il
contratto rende propedeutico. L'evidenza c'è dal 2026-11-20 (sezione sopra);
la dichiarazione del confine di `method` attende la decisione del custode su
`nixos` `o2/chiudere-le-uscite-del-recinto.md`, perché dichiarare oggi
vorrebbe dire dichiarare un confine che, per l'host, non regge.
