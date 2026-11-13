---
sintesi: "Studiare se il metodo può girare sopra Hermes Agent o OpenClaw, che darebbero installazione, chat e pianificazione già pronte, invece di costruire un ingresso proprio. Lo studio obbliga a dire che cosa il metodo aggiunge agli esistenti; se emerge incompatibilità, resta la via di un ingresso proprio con interfaccia web sopra il repo markdown. Si parte da Hermes."
ciclo: dev
---

# Integrazione con un runtime esistente

## Origine

Il 2026-11-13, discutendo il nome, emerge il posizionamento: Hermes Agent e
OpenClaw sono programmi che si installano e tengono memoria e pianificazione
nel proprio runtime; il metodo è una forma di repository con memoria e governo
in file versionati. Il punto debole è l'ingresso: oggi adottare vuol dire
symlink, fork delle skill e uno strato host legato a NixOS.

Il custode propone di studiare un'integrazione con uno dei due, con preferenza
di partenza per Hermes, non ancora approfondita. Due esiti lo interessano
entrambi:

- se l'integrazione regge, l'adozione passa da un runtime che molti hanno già;
- se non regge, lo studio ha comunque chiarito che cosa serve a un ingresso
  proprio.

## Principio fermo

Sotto c'è un repository markdown, che è il motore; l'interfaccia è la
presentazione. Vale per tutte e due le vie, ed è il criterio con cui si
giudica un'integrazione: se per girare su un runtime la memoria deve uscire
dal repo, non è un'integrazione ma una sostituzione.

## Che cosa si sa già

Da una prima ricerca web del 2026-11-13, su documentazione ufficiale e guide
di terzi; nessuno dei due è stato installato né provato.

**Hermes Agent** (Nous Research):

- tutto vive in una cartella personale, `~/.hermes`: `SOUL.md` per la
  persona, `MEMORY.md` e `USER.md` per la memoria;
- le skill sono memoria procedurale che l'agente crea e migliora da solo;
- legge file di contesto del progetto, fra cui `AGENTS.md`; non è chiaro come
  li trova e con quale precedenza;
- si installa su Windows in modo nativo, da PowerShell, e ha un installer
  desktop;
- non è emerso se ha un cruscotto web.

**OpenClaw**:

- lavora in uno spazio di file markdown, `~/.openclaw/workspace`:
  `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `USER.md`, `MEMORY.md` e note
  giornaliere;
- lo spazio di lavoro nasce già come repository git se git è installato, e
  si sposta clonandolo;
- le skill si caricano da una cartella dello spazio di lavoro;
- ha un battito periodico (`HEARTBEAT.md`) e una pianificazione a orario;
- la sicurezza è il punto più contestato: una fonte conta 138 CVE fra
  febbraio e aprile 2026;
- installazione su Windows e interfaccia di controllo non verificate.

Entrambi leggono `AGENTS.md`, che i repo del metodo hanno già per Codex. A una
prima lettura OpenClaw è più vicino nella forma (spazio di lavoro markdown in
git), Hermes nell'ingresso (installer per Windows). È una lettura da
verificare, non un esito.

## Domande dello studio

1. **Dove vive la memoria.** Il runtime può lavorare con il repo del progetto
   come unica memoria, o ne tiene una propria che entra in concorrenza? Qui il
   metodo spegne la memoria dell'harness (`CLAUDE.md`, «Memoria»): vale lo
   stesso vincolo.
2. **Skill.** Le skill del metodo (`eval`, `exec`, `cycle`, `kb`, `commit`)
   si caricano così come sono, con un wrapper, o vanno riscritte? Un runtime
   che modifica le skill da solo è compatibile con skill versionate nel
   canone?
3. **Ciclo autonomo.** La pianificazione del runtime può sostituire il
   lanciatore e le unità di NixOS, mantenendo perimetro, resoconto e riga
   `Attenzione:`?
4. **Delega.** Come si traducono `autonomy.md`, i punti riservati al custode
   e i trailer dei commit in un runtime che ha un proprio modello di permessi?
5. **Interfaccia.** Che cosa offre già il runtime per configurare e
   controllare, e che cosa resterebbe da costruire per goal, world, plan e
   scadenze?
6. **Che cosa aggiunge il metodo.** Detto in una riga, per chi usa già quel
   runtime. Se non si riesce a dirlo, è il risultato più importante dello
   studio.

## La via alternativa: ingresso proprio

Idea del custode, da riprendere se lo studio trova incompatibilità o se il
runtime copre solo una parte:

- un installer per Windows;
- alcune pagine web di configurazione: goal, world, task, plan, strumenti;
- un cruscotto con gli esiti dei cicli e le scadenze;
- una chat nelle pagine per parlare con l'agente;
- la configurazione del repository sottostante.

Punti da tenere presenti:

- installer, chat e pianificazione sono ciò che Hermes e OpenClaw offrono
  già: costruirli da capo ha senso solo se lo studio dice che non si possono
  usare;
- le viste di oggi (`view/`) sono generate dal repo e sono di sola lettura.
  Pagine che configurano scrivono nel repo: serve decidere chi fa il commit e
  con quale dichiarazione di autonomia;
- un'interfaccia abbassa il costo d'installazione, non quello di capire il
  metodo (lessico, nodi, collezioni): quello si abbassa con la bussola e con
  un primo giro guidato.

## Passi

1. leggere la documentazione ufficiale di Hermes sulle sei domande, poi
   quella di OpenClaw per confronto;
2. provare Hermes su un repository di prova con la struttura del metodo: un
   giro di `eval` e uno di `exec`, annotando che cosa si rompe;
3. scrivere l'esito per domanda, con ciò che è verificato e ciò che è solo
   letto;
4. portare al custode la scelta: integrazione, ingresso proprio, o tutte e
   due con un ordine.

L'installazione di un runtime su un host e la prova su un adottante sono atti
da chiedere al custode: il passo 2 si fa su un repository di prova.

## Legami

- [nome-del-progetto](nome-del-progetto.md): il nome si sceglie sapendo se il
  progetto si presenta da solo o come strato sopra un runtime;
- [traduzione-inglese](traduzione-inglese.md): un'integrazione pubblica
  richiede l'inglese;
- [strumenti-dal-canone](strumenti-dal-canone.md) e
  [pubblicazione-decisa-dal-repo](pubblicazione-decisa-dal-repo.md): riducono
  già la dipendenza dallo strato host.

## Criterio di chiusura

Le sei domande hanno una risposta con la sua provenienza, e il custode ha
deciso la via; i task che ne seguono sono aperti nel plan.

## Fonti

- [Documentazione di Hermes Agent](https://hermes-agent.nousresearch.com/docs)
- [Mer.vin, la cartella `.hermes`](https://mer.vin/2026/05/hermes-agent-dot-hermes-folder-layout-soul-secrets-memory-skills/)
- [Documentazione di OpenClaw, lo spazio di lavoro dell'agente](https://docs.openclaw.ai/concepts/agent-workspace.md)
- [Stack Junkie, i file dello spazio di lavoro di OpenClaw](https://www.stack-junkie.com/blog/openclaw-workspace-architecture)
- [Toolradar, OpenClaw e Hermes Agent a confronto](https://toolradar.com/blog/openclaw-vs-hermes-agent)
