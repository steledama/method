---
sintesi: "Una chat nel sito di gruppo che apre sessioni ACP con Claude Code o con Codex nella cartella di un repo del gruppo: messaggi, chiamate di strumenti e approvazioni col diff, con il governo del repo invariato. Primo lavoro eseguibile del coordinatore di gruppi."
ciclo: dev
---

# Chat del coordinatore

## Origine

Aperto dal custode il 2026-11-14, dopo la prova di una chat ACP in `casa`
(task chiuso lo stesso giorno, in git). È il primo lavoro eseguibile del
[coordinatore di gruppi](coordinatore-di-gruppi.md): dal sito del gruppo si
lavora in chat con gli agenti, al posto del terminale, e il repo resta la
base. Il quadro, cioè la mappa degli strati e i due esiti possibili, sta in
[integrazione-runtime](integrazione-runtime.md), «Ingresso: viste e chat».

## Punto di partenza

Il client della prova, [`o3/chat/prova_acp.py`](../o3/chat/prova_acp.py):
Python con la sola libreria standard, lancia un adattatore ACP, apre una
sessione in una cartella, manda prompt e risponde alle richieste di permesso.

Che cosa la prova ha mostrato, in `casa` su `deck`, con
`claude-agent-acp` 0.107.0 e `codex-acp` 2.6.0:

- **Claude Code** carica i `CLAUDE.md` del repo e globale, vede e carica le
  skill, rispetta le regole `deny` di `.claude/settings.json`, non scrive
  memoria, fa un commit col gate con `/commit`. In modo `default` le
  scritture arrivano al client come `session/request_permission`, con
  strumento, input e diff; un rifiuto ferma l'agente senza effetti.
- **Codex** carica l'`AGENTS.md` del repo e legge da sé i file a cui
  rimanda, vede le skill come `$commit` e le carica dal wrapper, fa un commit
  col gate. In `read-only` una scrittura arriva come richiesta di permesso; il
  rifiuto chiude il turno.
- **Lo stesso client** ha lavorato con tutti e due senza cambiare riga.
- Le trascrizioni restano dove le lascia ciascun harness, come registro.

Non provato: un `/cycle` intero, che aspetta la parametrizzazione delle
skill di `casa`.

## Risultato atteso

Nel sito del gruppo, una pagina di chat da cui il custode:

- sceglie un repo del gruppo e un harness, e apre una sessione nella sua
  cartella;
- scrive e legge i messaggi man mano che arrivano;
- vede le chiamate di strumenti e il piano dell'agente;
- risponde alle richieste di permesso con un pulsante, vedendo il diff;
- cambia il modo di permesso fra quelli che l'harness dichiara.

Le viste del repo si aggiornano dal suo working tree e dai suoi commit, come
oggi.

## Vincoli

- **Il governo non cambia.** La chat parla con l'harness e non lo
  sostituisce: le modifiche le fa l'agente, i commit passano da `/commit` col
  gate e i trailer, i permessi restano quelli del repo e dell'harness.
- **Nessuna nuova fonte.** La chat non tiene memoria propria; le
  trascrizioni sono dell'harness. Un ricordo ad accesso dichiarato è materia
  del coordinatore («La memoria»), non di questo task.
- **Libreria standard**, come `o3/view/`, perché giri anche su Windows. Il
  codice vive nel canone, in `o3/chat/`, e ogni sito di gruppo lo usa senza
  copiarlo.
- **Accesso.** Chi raggiunge la chat può far agire un agente sui repo del
  gruppo con l'abbonamento del custode. Il primo rilascio ascolta solo su
  `localhost`; esporla sulle reti private, come le viste, richiede prima
  un'autenticazione, decisione del custode.

## Due differenze dell'harness da risolvere

- **Dove stanno i divieti.** Le regole `deny` di `.claude/settings.json`
  valgono solo per Claude Code; Codex ha sandbox, approvazioni e regole di
  esecuzione proprie (l'opzione `accept_execpolicy_amendment` della prova lo
  mostra). Va deciso se il repo dichiara i divieti in un posto solo, da cui si
  ricavano le regole di ciascun harness, o se la chat mostra quale protezione
  vale per l'harness scelto.
- **I modi di permesso.** Claude Code dichiara `default`, `acceptEdits`,
  `plan`, `auto`, `bypassPermissions`; Codex `read-only`, `workspace-write`,
  `agent`, `agent-full-access`. La proposta dell'agente: la chat mostra i
  modi che l'adattatore dichiara in `session/new` (`availableModes`), senza
  inventare una corrispondenza fra harness.

Fuori dalla chat, la memoria di Codex su `deck`: trovata attiva il
2026-11-14 e spenta lo stesso giorno da `nixos` (`ed43f24`, modulo
`o3/modules/home/codex.nix`), con `features.memories`,
`memories.generate_memories` e `memories.use_memories` a `false` in
`~/.codex/config.toml`. Il custode ha poi rimosso
`~/.codex/memories/` e `memories_1.sqlite`, che non contenevano nulla di
durevole.

## Passi

1. ~~Un server minimo per `casa`, su `localhost`~~ fatto il 2026-11-20:
   `o3/chat/serve.py --istanza ~/casa`, porta 8100, con `acp.py` e
   `chat.html`. Eventi in Server-Sent Events, permessi in attesa del
   custode col diff, modi dichiarati dall'adattatore, interruzione e
   chiusura; presidi su `Host` e `Origin` contro le pagine di altri siti.
   Provato dal vivo con `claude-agent-acp` 0.107.0 in `casa`: sessione,
   modi, risposta in streaming, `end_turn`.
2. ~~La scelta del repo e dell'harness~~ fatto il 2026-11-20: l'istanza e i
   membri di `## Membri` con un checkout accanto all'istanza.
3. Le due differenze dell'harness.
4. Il rapporto col sito delle viste: per ora due servizi, perché le viste
   stanno sulle reti private senza autenticazione e la chat resta su
   loopback; si uniscono dopo il passo 5. Il codice sta già accanto, nel
   canone.
5. L'accesso: autenticazione, poi l'esposizione sulle reti private.
6. Un `/cycle` intero da chat, dopo la parametrizzazione delle skill di
   `casa`.

Il coordinamento fra sessioni resta aperto: Herdr non vede le sessioni
aperte dalla chat (cfr. il task d'origine).

## Criterio di chiusura

Il custode lavora da chat in un repo del gruppo di casa con tutti e due gli
harness, approvazioni comprese, e un `/cycle` intero è passato da lì. Ciò
che si è imparato su ACP risale in un nodo `kb/`.

## Legami

- [coordinatore-di-gruppi](coordinatore-di-gruppi.md): il quadro e le
  istanze;
- [integrazione-runtime](integrazione-runtime.md): mappa degli strati e
  confronto;
- [view-publishing](../kb/view-publishing.md): come si servono le viste,
  e il confine delle reti private.
