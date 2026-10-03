---
sintesi: "Il canone della presentazione ammette un servizio permanente per progetto su un host privilegiato, solo su reti private, e porta il lancio manuale di serve.py sulla porta 8000; una prescrizione o3 lo porta ai sei adottanti, che dichiarano la decisione del custode, l'esposizione continua dei dati e il proprio host. 8765 esce dal canone."
ciclo: runtime
---

# Presentazioni permanenti sulle reti private

## Decisione del custode (2026-10-03)

La decisione è presa: qui si specifica come entra nel canone e come arriva
agli adottanti, non se farlo.

1. **Presentazioni permanenti.** Ognuno dei sette progetti ha un solo host
   privilegiato che serve sempre la sua `presentation/`. Chi sta nelle reti
   private vede com'è fatto il progetto e a che punto è, aggiornato
   all'ultima sincronizzazione del checkout:
   - `deck` (casa): `method` 8001, `nixos` 8002, `salute` 8003,
     `economia` 8004;
   - host di produzione della coppia server (oggi `svezia`): `bi` 8001,
     `crm` 8002. Il servizio segue il ruolo, non l'hostname;
   - `danea2` (Windows): `danea-auto` 8001, configurato a parte.
2. **Lancio manuale.** `python3 o3/presentation/serve.py` senza argomenti
   ascolta sulla porta **8000** (oggi 8765), in ogni repo e su ogni host, ed è
   raggiungibile dalle stesse reti private. Esempio: si lavora su `game` al
   repo `nixos` e lo si consulta da un altro PC senza aggiornarlo su `deck`.
3. **Reti.** Solo reti private: LAN casa, VPN casa, LAN lavoro. Mai la rete
   pubblica. Il server non tocca il firewall: le porte le ammette ogni host
   nella propria configurazione (NixOS in modo dichiarativo, Windows dal
   prompt del firewall o con una regola). La porta 8765 va dismessa ovunque.
4. **Forma del servizio permanente.** È un servizio utente (`systemd --user`
   sugli host NixOS, gestibile da un agente senza `sudo`) che lancia lo
   stesso `serve.py` canonico del checkout con `--port`. Non esiste una copia
   servita separatamente: il server legge i file su disco, quindi un pull
   aggiorna la presentazione senza riavvii. La rigenerazione resta compito di
   `build.py`. Il servizio è disponibile dopo il riavvio dell'host e senza
   una sessione interattiva aperta. Se manca il checkout o l'indice, resta
   fermo con una diagnosi leggibile, senza cicli di riavvio. Al cambio di
   ruolo production resta attivo un solo servizio permanente per progetto,
   sul nuovo host di produzione.

La condizione di revisione di `kb/presentation.md § Vincolo conservato`
(«un bisogno reale di disponibilità continua o accesso remoto») è
soddisfatta. Il vincolo va **rivisto** e il task non deve aggirarlo con
un'eccezione locale.

## Passo 1 — Cambio di canone in `method`

- `o3/presentation/serve.py`:
  - `PORT = 8000`;
  - la docstring e la `description` di argparse non dicono più «su
    richiesta» e «non è un servizio permanente» in assoluto: lo stesso
    script serve il lancio manuale e il servizio permanente con `--port`;
  - il comportamento con `presentation/index.html` assente (oggi
    `SystemExit` con messaggio) resta leggibile anche sotto un service
    manager: un'uscita con errore e un messaggio sullo stderr, senza
    traceback.
- `kb/presentation.md`:
  - **§ Vincolo conservato** riscritto con i requisiti che rendono legittimo
    un servizio permanente:
    - consumatori reali: persone nelle reti private che consultano lo stato
      del progetto senza avere il checkout;
    - un solo host serve permanentemente ciascun progetto; le sessioni
      manuali possono servire temporaneamente altri checkout. Se l'host è
      un ruolo (la production della coppia), il servizio segue il ruolo e
      al cambio resta attivo solo sul nuovo host di produzione;
    - un servizio utente, non di sistema, gestibile senza privilegi;
    - disponibilità dopo il riavvio dell'host e senza una sessione
      interattiva aperta;
    - solo reti private, ammesse dal firewall dell'host. Il server non apre
      porte;
    - nessuna copia servita separatamente: si serve il checkout con lo
      stesso `serve.py` canonico, così sorgente e resa restano nello stesso
      artefatto (è la ragione originaria del vincolo, e resta);
    - un checkout o un `presentation/index.html` mancante fa saltare il
      servizio in modo leggibile, senza cicli di riavvio;
    - il servizio permanente espone i dati con continuità: l'adottante lo
      registra fra i propri vincoli sui dati.
  - **§ Apertura locale e condivisione on-demand**: porta 8000 al posto di
    8765, il lancio manuale accanto al servizio permanente, titolo da
    rivedere se «on-demand» non descrive più l'intera sezione;
  - **§ HTML apribile direttamente**: la frase «non deve richiedere […]
    servizi permanenti» resta vera, perché l'HTML si apre comunque da
    `file://`. Va riletta perché non sembri contraddire il vincolo rivisto.
- Gli altri punti del canone che citano 8765, «su richiesta» o «on-demand»
  riferiti al server. Il grep del 2026-10-03 trova:
  - `o3/prescriptions.md`, voce `serve.py` (righe 70-71);
  - `kb/kb.md`, riga del catalogo di `presentation` («apertura locale e
    condivisione on-demand»);
  - `presentation/prescriptions.html`, rigenerata da `build.py`.

  Al passo si ripete il grep (`8765`, `su richiesta`, `on-demand`,
  `servizio permanente`, `serve.py`) su tutto il repo, `.claude/skills/`
  compreso: questo elenco è una fotografia e non sostituisce il grep.

- `method` è anch'esso uno dei sette progetti, servito da `deck` sulla 8001:
  il suo host privilegiato va dichiarato dove il repo tiene l'orientamento
  operativo, probabilmente la voce `presentation/` del `README.md`. La
  configurazione del servizio vive in `nixos`.

## Passo 2 — Prescrizione `o3/` per gli adottanti

Una prescrizione nuova in `o3/`, indicizzata in `o3/prescriptions.md`, con
`target: nixos, bi, economia, salute, crm, danea-auto`. Va scritta nel
lessico del metodo, come «cosa e perché» più una ricetta. I touchpoint per
repo sono indizi da verificare in loco (`o3/prescriptions.md § Divisione del
lavoro`). Ogni adottante:

- **a) recepisce** `serve.py` e il nodo `presentation` via `/method`: lo
  `serve.py` locale torna identico al canonico, e ogni menzione locale di
  8765 o del server «su richiesta» si aggiorna;
- **b) dichiara la decisione** nel proprio `CLAUDE.md` e in
  `i3/allineamento-metodo.md`: l'apertura della presentazione alle reti
  private è una decisione presa dal custode (2026-10-03). Accanto va lo stato
  del collaudo: porte, reti, host, e cosa è verificato da un client reale e
  cosa no. Dove oggi c'è scritto che la decisione spetta ancora al custode o
  che non è collaudata, va scritto che è stata decisa. Il collaudo resta
  dichiarato per quello che è;
- **c) registra il cambio di esposizione dei dati**: anche se la rete resta
  privata, un server sempre acceso espone il contenuto di `presentation/` in
  modo continuo, non più occasionale, e senza autenticazione. Va scritto dove
  il repo tiene i propri vincoli sui dati, non solo nella nota di rete:
  cosa finisce in `presentation/`, chi lo vede, quali dati non devono
  entrarci. La decisione vale **senza eccezioni**, anche per i repo con
  dati personali (`economia`, `salute`): un vincolo locale che la
  contraddice (per esempio «solo `--bind 127.0.0.1`» o «l'agente non lo
  avvia su altri host») va riscritto in coerenza con la decisione. Non resta
  in contraddizione e non diventa un'eccezione locale. La protezione dei dati
  sta in ciò che entra in `presentation/` e nelle reti ammesse, non in un
  server più chiuso di quello degli altri repo;
- **d) indica l'host privilegiato**: host, porta e dove vive la
  configurazione del servizio (`nixos` per `deck` e per la coppia server,
  configurazione a parte per `danea2`). Le attività residue di installazione
  e collaudo hanno un riferimento operativo esplicito nel repo che le
  esegue: il task di `nixos` per gli host NixOS, un task locale di
  `danea-auto` per `danea2`. Il marker distingue il recepimento del canone
  dall'attivazione e dal collaudo del servizio e rimanda a quel lavoro.

Indizi per repo (stato letto il 2026-10-03 dai checkout su `deck`):

- **nixos** — host `deck`, porta 8002.
  - 8765 compare in `README.md` (riga 65), `o3/prescriptions.md` (righe
    92-93), `i3/allineamento-metodo.md` (righe 65 e 87);
  - il punto d) coincide col task locale `o2/serve-project-presentations.md`,
    che porta anche servizi, firewall e rotte (vedi sotto).
- **bi** — host della production (oggi `svezia`), porta 8001.
  - 8765 compare in `CLAUDE.md` (righe 189-190) e in
    `i3/allineamento-metodo.md` (righe 40-44), che rimanda l'esposizione a
    NixOS;
  - per il punto c): `bi` tratta dati aziendali (ordini, fornitori, listini);
    va verificato cosa ne arriva nelle viste.
- **economia** — host `deck`, porta 8004.
  - `CLAUDE.md` (righe 177-183) registra già la decisione LAN del
    2026-10-02 sulla 8765 e la regola «l'agente non lo avvia su altri host né
    su altre reti»; la regola va riscritta senza eccezioni: lancio manuale
    sulla 8000 su ogni host e servizio permanente su `deck`, come gli altri
    repo;
  - in `o3/tools.md` (righe 60-61) 8765 va aggiornata;
  - `i3/allineamento-metodo.md` dice «un servizio permanente sull'host di
    riferimento è da decidere» (righe 61-64) e dichiara un collaudo senza
    client reale (riga 97);
  - per il punto c): dati patrimoniali, fiscali e legali.
- **salute** — host `deck`, porta 8003.
  - `CLAUDE.md` (righe 58-60) prescrive `--bind 127.0.0.1` e dice
    «l'apertura alla LAN la decide il custode»: va riscritto senza
    eccezioni, con lancio manuale sulla 8000 aperto alle reti private e
    servizio permanente su `deck`, come gli altri repo;
  - `i3/allineamento-metodo.md § Limiti` (righe 90-93) dice che il server LAN
    non è collaudato;
  - per il punto c): dati sanitari personali. Va verificato dove il repo
    tiene le regole sui dati (`CLAUDE.md`, `world.md`: per esempio la regola
    sulle misure di peso dichiarata dal custode) e cosa ne passa nelle viste
    generate.
- **crm** — host della production (oggi `svezia`), porta 8002.
  - 8765 compare in `o3/prescriptions.md` (righe 258-259);
    `i3/allineamento-metodo.md` (riga 38) dice «verificato in locale»;
  - per il punto c): dati commerciali di clienti e contatti.
- **danea-auto** — host `danea2`, porta 8001, configurazione a parte.
  - 8765 compare in `o3/prescriptions.md` (righe 23-25 e 38-39) e in
    `i3/allineamento-metodo.md` (righe 63-65), con la regola del firewall
    `danea-auto presentation (serve.py)` su TCP 8765, profilo Privato,
    `LocalSubnet`;
  - la regola va rifatta per 8000 e 8001 e la 8765 rimossa;
  - la forma del servizio permanente su Windows (non c'è `systemd --user`)
    la decide l'agente di `danea-auto` in loco, sulla base dell'ambiente
    reale di `danea2`. Deve rispettare i requisiti del nodo: servizio a
    livello utente, stesso `serve.py` del checkout, salto leggibile se manca
    l'indice. Scelta e motivazione si dichiarano nel repo, al punto d).

La prescrizione non contiene la configurazione degli host: dichiara cosa ogni
adottante scrive di sé e rimanda a `nixos` per `deck` e la coppia server.

## Ordine e dipendenze

1. Passo 1 in `method`: canone e `serve.py`.
2. Passo 2 in `method`: la prescrizione.
3. `/method` negli adottanti. `nixos` per primo, perché il suo task
   «Servire in modo permanente le presentazioni dei progetti»
   (`o2/serve-project-presentations.md` nel repo `nixos`) dipende dal
   recepimento di questo canone. È il **consumatore** di questo task, e
   servizi utente, firewall, rotte statiche e marker di ruolo vivono lì:
   qui non si duplicano. Gli altri adottanti recepiscono nei loro giri;
   l'agente di `danea-auto` sceglie e configura il servizio su `danea2` in
   loco.

## Verifica

- la ricerca di `8765` sul canone (`kb/`, `o3/`, `.claude/skills/`,
  `README.md`, `CLAUDE.md`, `presentation/`) non trova default, comandi
  operativi o regole attive che usino la vecchia porta. Sono ammesse le
  menzioni della migrazione, comprese quelle del task nelle viste generate
  e le istruzioni di dismissione nella prescrizione;
- `python3 o3/presentation/serve.py` senza argomenti stampa URL sulla porta
  8000; `--port 8001` funziona; con `presentation/index.html` assente esce
  con errore e messaggio, senza traceback;
- `python3 o3/presentation/build.py` passa; `python3 o3/kb_tools.py audit`
  non segnala regressioni sul nodo;
- per ogni adottante, il marker `i3/allineamento-metodo.md` registra il
  recepimento con i quattro punti a)–d). Il battito `/adottanti` lo legge
  e conferma che i file corrispondono, comprese le attività residue e i loro
  riferimenti operativi;
- i task di installazione e collaudo negli adottanti verificano la
  disponibilità dopo riavvio e senza sessione interattiva, l'arresto
  leggibile senza cicli di riavvio quando manca il checkout o l'indice e,
  per la coppia server, l'unicità del servizio permanente dopo il cambio di
  ruolo production. Le soluzioni tecniche e le evidenze vivono in `nixos`
  e in `danea-auto`.

## Criterio di chiusura

- Canone aggiornato: `serve.py` con default 8000, `kb/presentation.md` col
  vincolo rivisto, nessun uso operativo attivo di 8765 nel canone; restano
  ammesse le menzioni della migrazione.
- Prescrizione recepita da tutti e sei gli adottanti, con i punti a)–d)
  verificati e ogni attività residua di installazione e collaudo collegata
  al lavoro operativo nel repo responsabile. Questa chiusura certifica la
  propagazione del canone; attivazione e collaudo si chiudono nei task degli
  adottanti, con le rispettive evidenze. A quel punto la prescrizione esce
  dalla collezione e dall'indice di `o3/` secondo la regola della collezione.
- Alla chiusura, la riga in `o1/plan.md`, la voce in `o2/tasks.md` e questo
  file si rimuovono nello stesso commit. Le decisioni stabili sono già nel
  nodo `presentation`.

Connessioni:

- [presentation](../kb/presentation.md)
- [constraint](../kb/constraint.md)
- [perform](../kb/perform.md)
- [prescriptions](../o3/prescriptions.md)
