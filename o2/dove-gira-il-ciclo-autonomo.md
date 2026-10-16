---
sintesi: "Il ciclo autonomo gira da un timer systemd dichiarato in un unico modulo nixos, con Claude Code non interattivo: un file di decisioni per repo e un meccanismo generico. Costruito e collaudato al gradino 0 su deck e svezia; resta da osservare l'arresto per tempo massimo."
ciclo: dev
---

# Dove gira il ciclo autonomo

Il ciclo autonomo è un giro `eval all` → `exec all` che chiude con un commit e il
push, senza custode.

## Scelta

Decisa dal custode il 2026-10-11.

- **Scheduler**: timer systemd sull'host, dichiarato in `nixos`. Versionato e
  riproducibile, sopravvive ai riavvii, vede checkout, `gdrive` e superfici
  ssh. Scartati `/loop` (vive nella sessione, non versionato) e le routine
  cloud (un clone dal remoto non vede checkout locali né superfici private).
- **Harness**: solo Claude Code, `claude -p`. Il confronto con Codex e pi
  nasceva dal timore di dipendere da un solo fornitore; in questa fase
  complicava senza beneficio. Se servirà cambiare, si valuteranno le opzioni
  di quel momento.
- **Prova**: su repo reali con il servizio reale, non su cloni usa e getta.
  La gradualità sta nei gradini del [pilota](pilota-ciclo-autonomo.md), non in un
  ambiente di prova separato.

## Forma del modulo

Un unico modulo in `nixos`, con le decisioni separate dal meccanismo:

- **File delle decisioni**: per ogni repo host, cadenza, orario, tempo
  massimo e stato (`manuale`: unità presente, avvio solo a mano; `timer`:
  schedulato). Il campo `host` ha un solo valore: «un solo host tiene il
  ciclo autonomo di un repo» vale per costruzione. `danea-auto` vi compare come voce
  dichiarata «fuori nixos (Task Scheduler)», così il quadro resta completo.
- **Meccanismo generico**: su ogni host genera le unità dei soli repo
  assegnati a lui. Tiene in un posto l'invocazione, il tempo massimo
  (`RuntimeMaxSec`), il lock contro sessioni sovrapposte sullo stesso
  checkout, il log dei tentativi e la fonte di stato per la home. Il registro
  di cadenza di `/manutenzione` non è un lock fra sessioni: serve un lock
  locale.

Confine: `nixos` decide **dove e quando**, il repo decide **cosa**. Prompt
del giro, permessi del ciclo autonomo e perimetro degli atti (`autonomy.md`) vivono
nel repo; il modulo invoca senza sapere cosa fa il giro (cfr.
`kb/method-development.md`, «dichiara e taci»). La scelta qui non attiva lo
scheduler: l'attivazione vive in `nixos`.

Due recinti, in quest'ordine (ricognizione di `salute`, 2026-10-11):

- **L'unità** è il recinto vero: percorsi in sola lettura o inaccessibili
  (`ReadOnlyPaths`, `InaccessiblePaths`), lock, tempo massimo. Le regole Bash
  dell'harness non coprono redirect e sottoprocessi.
- **I permessi dell'harness** sono il secondo: un file del solo ciclo autonomo,
  versionato nel repo e passato all'unità con `--settings`, non
  `.claude/settings.json`, che vale anche per le sessioni interattive. Con
  `--setting-sources project` l'unità esclude `settings.local.json` e le
  impostazioni utente, che possono concedere atti non voluti nel ciclo autonomo (in
  `salute` su `deck`, cancellazioni su Drive e calendario).

## Invocazione

Verificato sull'help il 2026-10-11 (Claude Code 2.1.295): `claude -p` con
`--permission-mode dontAsk` (ogni permesso non concesso è negato senza
chiedere), `--no-session-persistence`, `--max-budget-usd`,
`--output-format json`. L'ambiente dell'unità evita i blocchi interattivi:
stdin da `/dev/null`, `GIT_TERMINAL_PROMPT=0`,
`GIT_SSH_COMMAND="ssh -o BatchMode=yes"`, `PAGER=cat`.

Verificato ai gradini 0 di `salute` (2026-10-11) e `crm` (2026-10-15),
cfr. [pilota](pilota-ciclo-autonomo.md): le skill del repo si invocano da
`claude -p`, i permessi negati arrivano alla chiusura e ingialliscono il
semaforo, Claude e il push via ssh si autenticano nell'unità senza agent.
Resta da osservare l'arresto per `RuntimeMaxSec` e la sua traccia nel
journal: nessun giro ha ancora toccato il tempo massimo.

## Vincoli comuni

- Sincronizzazione: la skill `cycle` fa `git pull --ff-only` a working tree
  pulito prima di ogni atto e si ferma se fallisce. Un push rifiutato non si
  forza e rende visibile l'arresto (caso reale in `method` il 2026-10-08).
- Dove un push innesca un rilascio (`bi`), il ciclo autonomo eredita la scelta
  locale: in `bi` il push resta su richiesta quando i commit toccano il
  codice eseguito dal ciclo.

## Arresti e fonte di stato

La proposta operativa deve precisare comportamento e arresto per checkout
sporco, conflitto, timeout, sessioni sovrapposte e push rifiutato, senza
chiedere un consenso interattivo che nel ciclo autonomo non può arrivare.

Definire una fonte dello stato dei tentativi leggibile dalla home: partenza,
chiusura, arresto e mancata partenza rispetto alla cadenza attesa; distinguere
commit creato, push e pubblicazione. Il solo `git log` non misura un tentativo
interrotto prima del commit. `o3/view/publish.py` e il suo `status.json`
misurano la pubblicazione, non l'esecuzione di `eval`/`exec`.

## Chiusura

Modulo dichiarato in `nixos` e collaudato al gradino 0 sui due host,
protocollo dei casi di arresto, contratto della fonte per la home e
prescrizione di attivazione locale per gli adottanti.
