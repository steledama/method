---
data: 2026-10-03
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto
---

# Presentazioni permanenti sulle reti private

## Cosa e perché

Il custode ha deciso (2026-10-03) che ognuno dei sette progetti abbia un
**host privilegiato** che serve sempre la sua `presentation/`. Così chi sta
nelle reti private vede com'è fatto il progetto e a che punto è, aggiornato
all'ultima sincronizzazione del checkout:

- `deck` (casa): `method` 8001, `nixos` 8002, `salute` 8003, `economia` 8004;
- host di produzione della coppia server (oggi `svezia`): `bi` 8001, `crm` 8002. Il servizio segue il ruolo, non l'hostname;
- `danea2` (Windows): `danea-auto` 8001, configurato a parte.

Accanto ai servizi permanenti, `serve.py` lanciato a mano ascolta sulla porta
**8000** in ogni repo e su ogni host. Le reti ammesse sono solo quelle private
(LAN casa, VPN casa, LAN lavoro), mai la rete pubblica. La porta 8765 è
dismessa ovunque.

La condizione di revisione del vincolo di `method/presentation.md`, «un
bisogno reale di disponibilità continua o accesso remoto», si è verificata.
Il canone ha rivisto il vincolo invece di aggirarlo:
`§ Vincolo conservato` elenca ora le condizioni che rendono legittimo un
servizio permanente. Le principali: consumatori reali, un solo host
privilegiato per progetto, un servizio utente disponibile dopo il riavvio,
solo reti private, nessuna copia separata, assenza leggibile ed esposizione
dichiarata. `serve.py` canonico ha il default 8000.

La decisione vale **senza eccezioni**, anche per i repo con dati personali.

## Ricetta di recepimento

1. **Recepisci il canone** con `/method`: `o3/presentation/serve.py` torna
   identico al canonico (porta 8000, docstring nuova). Ogni menzione locale di
   8765 o di un server «su richiesta» si aggiorna: README, CLAUDE, indice
   `o3/`, note degli strumenti.
2. **Dichiara la decisione** nel proprio `CLAUDE.md` e in
   `i3/allineamento-metodo.md`: l'apertura della presentazione alle reti
   private è una decisione presa dal custode il 2026-10-03. Accanto va lo stato
   del collaudo: porte, reti, host, e cosa è verificato da un client reale e
   cosa no. Dove il repo dice ancora che la decisione spetta al custode o che
   è da decidere, scrivi che è stata decisa. Il collaudo resta dichiarato per
   quello che è.
3. **Registra l'esposizione dei dati** dove il repo tiene i propri vincoli sui
   dati, non solo nella nota di rete. Un server sempre acceso e senza
   autenticazione espone `presentation/` in modo continuo, non più
   occasionale: scrivi cosa finisce nella cartella, chi lo vede e quali dati
   non devono entrarci. Un vincolo locale che contraddice la decisione (per
   esempio «solo `--bind 127.0.0.1`» o «l'agente non lo avvia su altri host»)
   va riscritto in coerenza con la decisione, senza farne un'eccezione locale.
   La protezione sta in ciò che entra nella cartella e nelle reti ammesse.
4. **Indica l'host privilegiato**: host, porta e dove vive la configurazione
   del servizio. Per `deck` e per la coppia server la configurazione vive nel
   repo `nixos`; per `danea2` vive a parte. Le attività residue di
   installazione e collaudo hanno un riferimento operativo esplicito nel repo
   che le esegue: il task `nixos` `o2/serve-project-presentations.md` per gli
   host NixOS, un task locale di `danea-auto` per `danea2`. Il marker
   distingue il recepimento del canone dall'attivazione e dal collaudo del
   servizio e rimanda a quel lavoro.
5. Registra il recepimento nel marker `i3/allineamento-metodo.md`.

## Indizi per repo

Stato letto il 2026-10-03 dai checkout su `deck`. Sono indizi da verificare in
loco, non ordini alla lettera.

- **nixos** — host `deck`, porta 8002.
  - 8765 compare in `README.md`, `o3/prescriptions.md` e
    `i3/allineamento-metodo.md`;
  - il task locale `o2/serve-project-presentations.md` implementa servizi
    utente, firewall, rotte e marker di ruolo per `deck`, `game`, `neve` e la
    coppia server, e dipende da questo recepimento: `nixos` recepisce per
    primo.
- **bi** — host della production (oggi `svezia`), porta 8001, servizio
  dichiarato in `nixos`.
  - 8765 compare in `CLAUDE.md` e in `i3/allineamento-metodo.md`, che
    rimanda l'esposizione a NixOS;
  - per il punto 3: dati aziendali (ordini, fornitori, listini); verifica
    cosa ne arriva nelle viste.
- **economia** — host `deck`, porta 8004, servizio dichiarato in `nixos`.
  - `CLAUDE.md` registra la decisione LAN del 2026-10-02 sulla 8765 e la
    regola «l'agente non lo avvia su altri host né su altre reti»: va
    riscritta con lancio manuale sulla 8000 su ogni host e servizio
    permanente su `deck`;
  - 8765 compare in `o3/tools.md`;
  - `i3/allineamento-metodo.md` dice che il servizio permanente è «da
    decidere» e che il collaudo non è stato fatto da un client reale;
  - per il punto 3: dati patrimoniali, fiscali e legali.
- **salute** — host `deck`, porta 8003, servizio dichiarato in `nixos`.
  - `CLAUDE.md` prescrive `--bind 127.0.0.1` e dice «l'apertura alla LAN la
    decide il custode»: va riscritto con lancio manuale sulla 8000 aperto
    alle reti private e servizio permanente su `deck`;
  - `i3/allineamento-metodo.md § Limiti` dice che il server LAN non è
    collaudato;
  - per il punto 3: dati sanitari personali. Verifica dove il repo tiene le
    regole sui dati (`CLAUDE.md`, `world.md`) e cosa ne passa nelle viste.
- **crm** — host della production (oggi `svezia`), porta 8002, servizio
  dichiarato in `nixos`.
  - 8765 compare in `o3/prescriptions.md`;
  - per il punto 3: dati commerciali di clienti e contatti.
- **danea-auto** — host `danea2`, porta 8001, configurazione a parte.
  - 8765 compare in `o3/prescriptions.md` e in `i3/allineamento-metodo.md`,
    con la regola del firewall `danea-auto presentation (serve.py)` su TCP
    8765, profilo Privato, `LocalSubnet`. La regola va rifatta per 8000 e
    8001 e la 8765 rimossa;
  - su Windows non c'è `systemd --user`: la forma del servizio permanente la
    decide l'agente di `danea-auto` in loco, sull'ambiente reale di
    `danea2`, rispettando le condizioni del nodo. Scelta, motivazione e
    collaudo vivono in un task locale (punto 4).

## Fuori perimetro

La prescrizione non porta la configurazione degli host. Servizi utente,
firewall, rotte e marker di ruolo degli host NixOS vivono nel task `nixos`;
il servizio su `danea2` vive in `danea-auto`.

## Verifica

- `serve.py` locale identico al canonico; `python3 o3/presentation/serve.py`
  senza argomenti stampa URL sulla porta 8000;
- nel repo non restano default, comandi o regole attive sulla 8765;
- il marker `i3/allineamento-metodo.md` registra i punti 1–4, con il
  riferimento operativo delle attività residue. Il battito `/adottanti` lo
  legge e conferma che i file corrispondono.
