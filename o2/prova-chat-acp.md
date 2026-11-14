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
   senza toccare la configurazione di NixOS finché è una prova.
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
