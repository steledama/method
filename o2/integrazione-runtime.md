---
sintesi: "Studiare se il metodo può girare sopra Hermes Agent o OpenClaw, che danno installazione, chat e pianificazione già pronte, invece di costruire un ingresso proprio. Letta il 2026-11-13 la documentazione ufficiale dei due sulle sei domande: nessuna incompatibilità sulla carta, Hermes si adatta meglio. Resta la prova su un repository di prova, poi la scelta del custode."
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
di partenza per Hermes. Due esiti lo interessano entrambi:

- se l'integrazione regge, l'adozione passa da un runtime che molti hanno già;
- se non regge, lo studio ha comunque chiarito che cosa serve a un ingresso
  proprio.

## Principio fermo

Sotto c'è un repository markdown, che è il motore; l'interfaccia è la
presentazione. Vale per tutte e due le vie, ed è il criterio con cui si
giudica un'integrazione: se per girare su un runtime la memoria deve uscire
dal repo, non è un'integrazione ma una sostituzione.

## Esito della lettura della documentazione

Lettura del 2026-11-13 della documentazione ufficiale
(`hermes-agent.nousresearch.com/docs`, `docs.openclaw.ai`), fatta da due
agenti di lettura con citazioni e indirizzi delle pagine. Limiti: alcune
pagine lunghe sono state lette solo in parte o in riassunto; le pagine di
Hermes su plugin, installazione su Windows e modelli locali non sono state
lette; nessuno dei due è stato installato. Tutto ciò che segue è letto, non
provato.

### Licenza e linguaggio

Dati di GitHub del 2026-11-13:

- **Hermes Agent** (`NousResearch/hermes-agent`): licenza MIT; Python 71%,
  TypeScript 25%; nato a luglio 2025, circa 263.000 stelle, sviluppo attivo.
  Lo mantiene Nous Research, un'azienda.
- **OpenClaw** (`openclaw/openclaw`): licenza MIT; TypeScript 89%, più Swift e
  Kotlin per le app; nato a novembre 2025, circa 394.000 stelle, sviluppo
  attivo. La documentazione lo dice sviluppato dalla OpenClaw Foundation, un
  ente senza scopo di lucro.

Lettura: sono entrambi open source con una licenza che permette di usarli,
modificarli e ridistribuirli, anche dentro un prodotto. Gli strumenti del
metodo (`o3/`) sono in Python, come il nucleo di Hermes: un plugin o
un'estensione del cruscotto si scriverebbe nel linguaggio che il repo usa già,
mentre con OpenClaw servirebbe TypeScript.

### 1. Dove vive la memoria

- **Hermes**: `MEMORY.md` e `USER.md` in `~/.hermes/memories/`, per profilo e
  non per progetto, con limiti stretti (2.200 e 1.375 caratteri). Si spengono
  del tutto con `memory.memory_enabled: false` e
  `memory.user_profile_enabled: false`; la revisione in background che salva
  memorie e skill si spegne con `auxiliary.background_review.enabled: false`.
  Lo storico delle sessioni resta in un database SQLite, senza interruttore
  documentato. Non c'è modo documentato di portare la memoria in una cartella
  del repo.
- **OpenClaw**: la memoria è markdown nello spazio di lavoro, e lo spazio di
  lavoro si può puntare su un repository git esistente
  (`agents.entries.<id>.workspace`). Lo scarico automatico prima della
  compattazione e la promozione automatica in `MEMORY.md` si spengono. Porta
  però nel repo i propri file: `SOUL.md`, `IDENTITY.md`, `USER.md`,
  `MEMORY.md`, note giornaliere. L'indice di ricerca sta in un SQLite fuori
  dallo spazio di lavoro.

Lettura: con Hermes vale la stessa mossa già fatta con Claude Code, spegnere
la memoria del runtime e lasciare il repo come unica memoria. OpenClaw è più
vicino nella forma, ma mette nella root file suoi che concorrono con bussola,
`goal.md` e `world.md`.

### 2. File di contesto del progetto

- **Hermes**: carica un solo tipo di file, il primo che trova fra
  `.hermes.md`, `AGENTS.override.md`, `AGENTS.md`, `CLAUDE.md`,
  `.cursorrules`. In un repo git unisce gli `AGENTS.md` dalla root alla
  cartella di lavoro. Tetto di almeno 20.000 caratteri. Controlla i file
  contro l'iniezione di istruzioni e può bloccarne uno. `SOUL.md` è globale,
  non del progetto.
- **OpenClaw**: inietta `AGENTS.md` a ogni sessione, con tetto di 20.000
  caratteri per file e 60.000 in totale. `CLAUDE.md` e `README.md` non
  risultano caricati.

Lettura: l'aggancio è `AGENTS.md`, che i repo del metodo hanno già (540
caratteri, rimanda a bussola e `CLAUDE.md`). Con entrambi `CLAUDE.md` non
entra da solo: l'agente lo legge perché `AGENTS.md` glielo dice, come oggi con
Codex.

### 3. Skill

- **Entrambi** seguono lo standard agentskills.io: una cartella con
  `SKILL.md`, `name` e `description` obbligatori nel frontmatter, ogni skill
  disponibile come comando `/nome`.
- **Hermes**: carica le skill del progetto da `<root>/.hermes/skills/` e
  `<root>/.agents/skills/`, solo dopo `hermes skills trust`. Le considera del
  repo: la manutenzione autonoma non le modifica mai e le skill nuove create
  dall'agente vanno altrove. Si possono aggiungere cartelle esterne
  (`skills.external_dirs`). La creazione autonoma si può sottoporre ad
  approvazione (`skills.write_approval: true`); un interruttore che la vieta
  del tutto non è stato trovato.
- **OpenClaw**: carica da `<workspace>/skills` e `<workspace>/.agents/skills`
  con precedenza su tutto il resto. Un'officina delle skill lascia che
  l'agente salvi e aggiorni le proprie; se tocca anche quelle dello spazio di
  lavoro non è documentato.

Lettura: le skill canoniche in `.claude/skills/` non hanno `name` nel
frontmatter, quindi serve un wrapper, come quello che c'è già per Codex in
`.codex/skills/`. Una sola cartella `.agents/skills/` di wrapper servirebbe
tutti e due i runtime. Hermes dà la garanzia che serve al canone: le skill del
repo non vengono riscritte dall'agente.

### 4. Ciclo autonomo

- **Hermes**: i lavori pianificati girano in una sessione nuova, con
  `--workdir` (la cartella del repo, da cui carica `AGENTS.md`) e `--skill`
  (la skill da invocare). Il risultato si può lasciare in un file locale.
  Senza persona presente i comandi pericolosi sono negati
  (`approvals.cron_mode: deny`). Serve il gateway acceso. Le definizioni
  stanno in `~/.hermes/cron/jobs.json`, fuori dal repo. Esiste un modo senza
  interfaccia (`hermes -z`).
- **OpenClaw**: le automazioni girano nel gateway e stanno nel suo database.
  Il carico è un messaggio, un comando o uno script; una skill come carico
  non è documentata. C'è `openclaw agent exec "<prompt>" --cwd ./repo --json`,
  senza gateway, con codici d'uscita 0, 1 e 2, pensato per pianificatori
  esterni. Senza una superficie di approvazione collegata le richieste sono
  negate.

Lettura: il lavoro pianificato di Hermes corrisponde quasi uno a uno al giro
di oggi (`--workdir <repo> --skill cycle`). Il comando senza gateway di
OpenClaw si aggancerebbe invece al lanciatore esistente. In entrambi la
definizione del giro vive fuori dal repo: serve un passo che la ricavi dalle
ricorrenze del plan, come oggi fanno le unità di NixOS.

### 5. Delega

- **Nessuno dei due** ha un file di permessi per progetto, né una regola sui
  commit git.
- **Hermes**: approvazione dei comandi `smart`, `manual` oppure `off`; un
  elenco di divieti che vale sempre (`approvals.deny`, per esempio
  `git push --force*`); una radice fuori dalla quale non si scrive
  (`HERMES_WRITE_SAFE_ROOT`), che però il terminale può aggirare; esecuzione
  in contenitore.
- **OpenClaw**: permessi per agente nel file globale `openclaw.json` (strumenti
  ammessi e vietati, sandbox, scrittura solo nello spazio di lavoro). La
  sicurezza dell'esecuzione sull'host è `full` per impostazione predefinita.
  La documentazione dichiara che non è un confine di sicurezza fra utenti
  ostili.

Lettura: `autonomy.md`, i punti riservati al custode, i trailer dei commit e
`o3/commit_gate.py` non hanno un equivalente in nessuno dei due. Restano del
metodo, e sono ciò che il metodo aggiunge. Il runtime applica i permessi
tecnici; il repo dichiara la delega.

### 6. Interfaccia

- **Hermes**: cruscotto web locale (`hermes dashboard`, porta 9119) con stato,
  chat, configurazione, sessioni, log, lavori pianificati, skill. L'indice
  della documentazione dice che i plugin possono aggiungere schede e rotte al
  cruscotto; la pagina dei plugin non è stata letta. App desktop per Windows,
  macOS e Linux. Installazione nativa su Windows da PowerShell; la scheda di
  chat del cruscotto su Windows richiede WSL2. Server compatibile con le API
  di OpenAI e integrazione con gli editor.
- **OpenClaw**: interfaccia di controllo web con chat, configurazione,
  automazioni, approvazioni, skill. App nativa per Windows che installa una
  propria distribuzione WSL. Plugin per canali, strumenti e comandi; pagine
  aggiunte all'interfaccia da un plugin non trovate.

Lettura: installer per Windows, chat e gestione dei giri esistono già in
entrambi. Le pagine per goal, world, plan ed esiti dei cicli sarebbero, con
Hermes, un plugin del cruscotto invece di un sito da costruire.

### 7. Che cosa aggiunge il metodo

Il 2026-11-13 il custode precisa che, nelle sue intenzioni, ciò che
caratterizza il progetto è il modello di Norman: i sei stadi del ciclo
d'azione, più Goal e World. Le mancanze elencate sotto ne sono conseguenze,
non un elenco di funzioni.

Letti con quel modello, i due runtime coprono l'arco di esecuzione (ricevono
una richiesta, pianificano, agiscono) dentro la sessione, senza lasciarne
traccia per stadio. L'arco di valutazione è sottile: il ciclo di
apprendimento di Hermes valuta come l'agente ha lavorato, per salvare memorie
e skill, non se il Mondo si è avvicinato all'obiettivo. Goal e World non
esistono come oggetti persistenti.

Il modello sta un livello sopra il runtime: gli stadi sono collezioni del
repo e due skill, e al runtime si chiede solo di eseguire skill e pianificare
giri. Per questo l'integrazione è possibile con entrambi. Due attenzioni:

- il ciclo di apprendimento di Hermes è un secondo ciclo, nascosto e fuori dal
  repo. Corrisponde al meta-ciclo di sviluppo del metodo, ma senza versione:
  va spento o messo sotto approvazione, perché a migliorare l'artefatto sia il
  ciclo del metodo;
- senza un'interfaccia che mostri gli stadi, per chi usa il runtime il metodo
  si riduce a un pacchetto di skill. Il plugin del cruscotto che mostra Goal,
  World e i sei stadi non è un accessorio: è ciò che rende visibile il
  modello.

Nessuno dei due ha: obiettivi scritti contro cui misurare, un braccio di
valutazione con verdetti e provenienza, una delega dichiarata con il
resoconto di ciò che l'agente ha deciso da solo, un canone che si propaga fra
più repository. La loro memoria è una nota libera (in Hermes, 2.200
caratteri).

Prima formulazione, da discutere: «dà all'agente che usi già un obiettivo
scritto, una memoria strutturata nel repository e il resoconto di ciò che ha
deciso da solo».

## Valutazione dell'agente

Sulla carta nessuno dei due è incompatibile. Hermes si adatta meglio, per
quattro motivi letti nella documentazione: tratta le skill del progetto come
proprietà del repo, pianifica un giro con cartella e skill, la sua memoria si
spegne, il suo cruscotto si estende. OpenClaw è più vicino nella forma, ma
porta nel repo i propri file d'identità e memoria e ha il profilo di sicurezza
più aperto.

Punti che solo la prova può chiarire:

- se il controllo di Hermes contro l'iniezione blocca `AGENTS.md` o le skill;
- se le skill reggono senza lo strumento Skill di Claude Code, in particolare
  `/cycle` che compone `eval`, `exec` e `commit`;
- come si comportano con un modello diverso da Claude;
- il costo: con Hermes i modelli Anthropic richiedono una chiave API, oppure
  un piano Max con crediti aggiuntivi; il piano Pro non basta.

## La via alternativa: ingresso proprio

Idea del custode, da riprendere se la prova trova incompatibilità o se il
runtime copre solo una parte:

- un installer per Windows;
- alcune pagine web di configurazione: goal, world, task, plan, strumenti;
- un cruscotto con gli esiti dei cicli e le scadenze;
- una chat nelle pagine per parlare con l'agente;
- la configurazione del repository sottostante.

Punti da tenere presenti:

- installer, chat e pianificazione esistono già in Hermes e OpenClaw (cfr.
  punto 6): costruirli da capo ha senso solo se la prova dice che non si
  possono usare;
- le viste di oggi (`view/`) sono generate dal repo e sono di sola lettura.
  Pagine che configurano scrivono nel repo: serve decidere chi fa il commit e
  con quale dichiarazione di autonomia;
- un'interfaccia abbassa il costo d'installazione, non quello di capire il
  metodo (lessico, nodi, collezioni): quello si abbassa con la bussola e con
  un primo giro guidato.

## Passi

1. ~~leggere la documentazione ufficiale dei due sulle sei domande~~ fatto il
   2026-11-13;
2. leggere le pagine di Hermes rimaste: plugin del cruscotto, installazione
   su Windows, modelli locali;
3. provare Hermes su un repository di prova con la struttura del metodo:
   wrapper in `.agents/skills/`, memoria spenta, un giro di `eval` e uno di
   `exec`, poi un giro pianificato; annotare che cosa si rompe;
4. scrivere l'esito per domanda, distinguendo il provato dal letto;
5. portare al custode la scelta: integrazione, ingresso proprio, o tutte e
   due con un ordine.

L'installazione di un runtime su un host e la prova su un adottante sono atti
da chiedere al custode: il passo 3 si fa su un repository di prova.

## Legami

- [nome-del-progetto](nome-del-progetto.md): il nome si sceglie sapendo se il
  progetto si presenta da solo o come strato sopra un runtime;
- [traduzione-inglese](traduzione-inglese.md): un'integrazione pubblica
  richiede l'inglese;
- la prescrizione [strumenti dal canone](../o3/strumenti-dal-canone.md) e
  [pubblicazione-decisa-dal-repo](pubblicazione-decisa-dal-repo.md): riducono
  già la dipendenza dallo strato host.

## Criterio di chiusura

Le sei domande hanno una risposta provata, o dichiarata come solo letta, e il
custode ha deciso la via; i task che ne seguono sono aperti nel plan.

## Fonti

Hermes Agent:

- [Memoria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
- [File di contesto](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- [Skill](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Lavori pianificati](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- [Sicurezza](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Cruscotto web](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
- [Fornitori di modelli](https://hermes-agent.nousresearch.com/docs/integrations/providers)

OpenClaw:

- [Spazio di lavoro dell'agente](https://docs.openclaw.ai/concepts/agent-workspace.md)
- [Memoria](https://docs.openclaw.ai/concepts/memory.md)
- [Skill](https://docs.openclaw.ai/tools/skills.md)
- [Automazioni](https://docs.openclaw.ai/automation/cron-jobs/how-it-works.md)
- [Comando `agent`](https://docs.openclaw.ai/cli/agent.md)
- [Sicurezza](https://docs.openclaw.ai/gateway/security.md)
- [Approvazioni dell'esecuzione](https://docs.openclaw.ai/tools/exec-approvals.md)
- [Interfaccia di controllo](https://docs.openclaw.ai/web/control-ui.md)
- [Windows](https://docs.openclaw.ai/platforms/windows.md)
