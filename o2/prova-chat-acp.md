---
sintesi: "Provare se una chat che parla ACP con Claude Code, dentro un repo del metodo, si comporta come il terminale: istruzioni del repo, skill, permessi, memoria spenta, commit col gate. È la prova minima che decide la direzione propria dell'ingresso."
ciclo: dev
---

# Prova di una chat ACP

## Origine

Nasce il 2026-11-14 dal task
[integrazione-runtime](integrazione-runtime.md), sezione «Ingresso: viste e
chat». Fra i due esiti possibili, il custode vede una direzione propria: un
SQLite derivato, un rendering in tempo reale da markdown a HTML e una chat
che sostituisce il terminale nelle sessioni dirette con l'harness, con repo
e git sempre come base. La chat parlerebbe con l'harness via ACP (Agent
Client Protocol, `agentclientprotocol.com`), il protocollo con cui Buzz
pilota Claude Code (`claude-agent-acp`), Codex (`codex-acp`) e Hermes
(`hermes-acp`). Tutto il resto della direzione ha senso solo se questa prova
riesce; per questo sta in un task suo.

## La domanda

Una sessione di Claude Code aperta via ACP nella cartella di un repo del
metodo si comporta come la stessa sessione nel terminale? In concreto, per
ciascun punto, sì o no provato:

1. carica `CLAUDE.md` del repo e quello globale del custode;
2. vede le skill di `.claude/skills/` e le invoca come comandi, compreso
   `/cycle`, che compone le altre;
3. applica le impostazioni e i permessi del repo, e le richieste di permesso
   arrivano alla chat come messaggi ACP a cui si risponde;
4. rispetta la memoria automatica spenta (`CLAUDE_CODE_DISABLE_AUTO_MEMORY`)
   e non scrive memorie fuori dal repo;
5. fa un commit con `/commit`, passando dal gate, con i trailer giusti;
6. lascia le trascrizioni dove le lascia oggi, come registro.

Il punto 1 non è scontato: un adattatore costruito sull'Agent SDK potrebbe
non caricare le impostazioni del progetto senza un'opzione esplicita. Va
letto nella documentazione dell'adattatore e poi provato.

Se i sei punti tornano, si ripete la prova con Codex via `codex-acp`
(`AGENTS.md`, `.codex/skills/`).

## Letto prima della prova

Lettura del 2026-11-14: la specifica su `agentclientprotocol.com`
(trasporti, inizializzazione, sessioni, turno di prompt, chiamate di
strumenti, file system, terminali, autenticazione) e il codice di
`agentclientprotocol/claude-agent-acp` alla versione 0.107.0 (commit
`b1c1987` del 14/11). È lettura, non prova.

- **Trasporto**: JSON-RPC 2.0 sullo standard input e output, un messaggio
  per riga; parla per primo il client, con `initialize` (`protocolVersion:
1`), poi `session/new` con la cartella assoluta e `session/prompt`. Le
  risposte arrivano come notifiche `session/update` (testo, chiamate di
  strumenti, piano); le richieste di permesso come `session/request_permission`,
  a cui il client risponde con un'opzione (`allow_once`, `reject_once` e le
  varianti «sempre»).
- **Punto 1, istruzioni del repo**: l'adattatore apre la sessione con
  `settingSources: ["user", "project", "local"]` (`src/v1/acp-agent.ts`,
  `src/v2/agent.ts`), cioè impostazioni dell'utente, del progetto e locali; il
  prompt di sistema resta quello di Claude Code, e i `CLAUDE.md` caricati da
  quelle fonti restano anche se il client lo sostituisce
  (`src/client-system-prompt.ts`). Il dubbio del punto 1 è sciolto sulla
  carta; resta da provare.
- **Punto 2, skill**: comandi personalizzati e skill sono supportati
  (README e CHANGELOG); da provare `/cycle`.
- **Punto 3, permessi**: la sessione parte in modo `auto` se disponibile,
  altrimenti `default`, e rispetta il `defaultMode` delle impostazioni, tranne
  i modi più permissivi dichiarati da file del repo, che filtra
  (`src/session-mode.ts`, `src/settings.ts`). Se le regole `deny` di
  `.claude/settings.json` reggano va provato.
- **Accesso**: riusa il login di Claude Code sull'host, abbonamento o
  console, senza una chiave API dedicata (`src/auth-methods.ts`).
- **Avvio**: `npx -y @agentclientprotocol/claude-agent-acp`, Node 22 o
  superiore. Su `deck` ci sono Node 24.21.0 e Claude Code 2.1.321.

## Fuori dalla prova

- l'interfaccia: basta un client minimo, senza pagine né stile;
- il database SQLite e il rendering in tempo reale;
- il coordinamento fra sessioni: Herdr non vede le sessioni aperte dalla
  chat, e dove stia il coordinamento si decide dopo (cfr. il task
  d'origine).

## Passi

1. Host e repository decisi dal custode il 2026-11-14: `deck`, e come
   repository la prima istanza del [coordinatore di gruppi](coordinatore-di-gruppi.md),
   casa, che coordina `nixos`, `salute` ed `economia`. La prova serve così
   anche da primo passo dell'istanza. L'adattatore si lancia con `npx`,
   senza toccare la configurazione di NixOS finché è una prova. Casa creata
   il 2026-11-14 in `~/casa` (commit `107f89b`, solo locale): struttura del
   metodo, `CLAUDE.md`, le skill forkate dal canone e il gate di commit, senza
   giri autonomi né letture dei repo del gruppo.
2. Leggere la specifica di ACP e la documentazione di `claude-agent-acp`:
   avvio, apertura di una sessione con una cartella, prompt, aggiornamenti,
   richieste di permesso, impostazioni caricate.
3. Scrivere il client minimo: Python, sola libreria standard, JSON-RPC sullo
   standard input e output dell'adattatore, nella scratchpad della sessione
   e non in `o3/` finché è una prova. In alternativa un client esistente.
4. Eseguire i sei punti e annotare per ciascuno l'esito e la prova.
5. Riportare l'esito nel task d'origine, sezione «Ingresso: viste e chat».

## Criterio di chiusura

I sei punti hanno un esito provato, l'esito è riportato nel task d'origine
e il custode ha deciso se aprire un task di sviluppo della chat.

## Legami

- [integrazione-runtime](integrazione-runtime.md): la direzione propria e
  la mappa degli strati;
- [session-messaging](../kb/session-messaging.md): il coordinamento di oggi,
  con Herdr;
- [view](../kb/view.md) e [view-publishing](../kb/view-publishing.md): le
  viste derivate e la pubblicazione da commit, che la chat non cambia.
