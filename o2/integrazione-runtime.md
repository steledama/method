---
sintesi: "Studiare se il metodo può girare sopra Hermes Agent o OpenClaw, che danno installazione, chat e pianificazione già pronte, invece di costruire un ingresso proprio. Letta il 2026-11-13 la documentazione ufficiale dei due sulle sei domande: nessuna incompatibilità sulla carta, Hermes si adatta meglio. Il 2026-11-14 la relazione di ciascuno col repo git, Buzz di Block fra i candidati e quattordici fattori per confrontare le quattro soluzioni. Resta la prova su un repository di prova, poi la scelta del custode."
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

## Relazione col repo

Approfondimento del 2026-11-14, chiesto dal custode prima di ogni prova:
che relazione ha ciascun runtime con un repository git. Mandare il contesto
a un modello non distingue i tre scenari, è uguale in tutti; li distingue che
cosa resta fuori dal repo e se torna nelle decisioni dell'agente. Anche oggi
non tutto sta in git: Claude Code tiene le trascrizioni in
`~/.claude/projects/` e i giri i tentativi in `~/.local/state/ciclo/`, ma sono
registri che l'agente non rilegge. Un archivio fuori dal repo è accettabile
finché resta un registro; diventa una seconda memoria quando l'agente lo
interroga per decidere.

### I tre scenari

- **Oggi, method con Claude Code o Codex**: il repo è il soggetto, l'harness
  uno strumento senza memoria propria (memoria automatica spenta). Nel repo
  vivono memoria, skill, delega e permessi del giro; fuori i registri e il
  calendario dei giri, versionato però nel repo `nixos`.
- **Hermes**: il soggetto è l'agente, con la sua casa in `~/.hermes`, e il
  repo è un luogo dove va a lavorare. Le skill del progetto restano del repo;
  fuori restano memoria del profilo, storico delle sessioni, skill create
  dall'agente, giri pianificati, permessi e plugin del cruscotto.
- **OpenClaw**: l'agente abita il repo, perché lo spazio di lavoro si punta
  su un repo git. La memoria è markdown nel repo e finirebbe in git, ma con
  una forma propria che concorre con `i3/`, `kb/` e `o2/`; l'indice SQLite
  fuori è ricavato dal markdown, una cache e non una fonte. Automazioni e
  permessi stanno nel gateway e in `openclaw.json`.

Con Hermes il nodo è che cosa resta fuori dal repo, con OpenClaw che cosa
entra nel repo senza passare dal metodo.

### Hermes: lo storico delle sessioni

Letto nella documentazione, pagine «Sessions», «Memory», «Tools» e
«Configuration» (questa solo in parte):

- ogni sessione, da riga di comando, interfaccia o gateway, finisce intera in
  `~/.hermes/state.db`, un SQLite per profilo con ricerca a testo pieno:
  messaggi, chiamate di strumenti e risultati, prompt di sistema, cartella di
  lavoro;
- non risulta un modo per spegnere quella scrittura né per spostare il file
  in una cartella del progetto; la cartella dipende da `HERMES_HOME`, ma la
  documentazione lo lascia intendere senza dirlo;
- l'agente lo interroga con lo strumento `session_search`, a sua scelta e non
  in automatico; il prompt lo invita a usarlo «prima di chiedere all'utente
  di ripetersi». Il contenuto entra nel contesto solo come risultato della
  chiamata;
- lo strumento è un insieme a sé (`session_search`), e gli insiemi si
  tolgono con `agent.disabled_toolsets`. Che toglierlo così funzioni è una
  deduzione: la documentazione non lo dice;
- la memoria e lo storico sono per profilo, non per progetto: un profilo che
  lavora su più repo li ricorda tutti insieme, e la cartella di lavoro è solo
  un filtro.

Lettura: con `session_search` tolto, `state.db` torna un registro come le
trascrizioni di Claude Code; con lo strumento acceso è una memoria fra
sessioni, e fra repo, fuori da git. Un profilo per repo terrebbe separati i
repo, al prezzo di un profilo da configurare per adottante.

### Hermes: il ciclo di apprendimento

Letto nelle pagine «Skills», «Memory» e «Curator»:

- per impostazione predefinita l'agente scrive skill liberamente: durante il
  turno con `skill_manage`, quando ha trovato un flusso da ripetere o è stato
  corretto, e in una revisione in background che parte all'incirca ogni dieci
  turni;
- la stessa revisione scrive anche in `MEMORY.md` e `USER.md`;
- le skill nuove vanno in `~/.hermes/skills/`, dove l'agente può modificare
  o cancellare qualsiasi skill;
- `auxiliary.background_review.enabled: false` spegne la revisione, per le
  skill e per la memoria; `skills.write_approval: true` e
  `memory.write_approval: true` mettono le scritture in attesa di
  approvazione. Un divieto completo non c'è: il più vicino è bloccare le
  skill una per una con `hermes curator lock`;
- le skill del progetto (`.hermes/skills/`, `.agents/skills/`) non le tocca
  il curatore, e l'elenco di ciò che la revisione può riscrivere non le
  nomina. Se possa farlo `skill_manage` durante il turno resta aperto.

Lettura: la configurazione minima per il metodo spegne la revisione e mette
in approvazione le scritture rimaste. Un'approvazione però chiede una persona
presente: in un giro senza custode le scritture in attesa si accumulano.

### Hermes: i plugin del cruscotto

Letto nella pagina «Extending the dashboard»: un plugin aggiunge schede con
un manifest, un file JavaScript e, se serve, rotte FastAPI in Python che
girano dentro il cruscotto. Vive in `~/.hermes/plugins/<nome>/`; i plugin
nella cartella del progetto non li carica il gateway. Se un plugin possa
leggere i file di un repo non è documentato. Lettura: il plugin che mostra
Goal, World e i sei stadi starebbe fuori dagli adottanti, ma potrebbe vivere
nel canone e arrivare con un symlink, come gli strumenti di `o3/`.

### Buzz

Aggiunto dal custode il 2026-11-14 (`github.com/block/buzz`). Letti il
README e parte di `ARCHITECTURE.md` e `VISION_AGENT.md`:

- è uno strato diverso dagli altri due: uno spazio di lavoro su un relay
  Nostr che si installa in proprio, dove persone e agenti stanno negli stessi
  canali («Agents are members, not bots»). Fa da cornice a Goose, Codex e
  Claude Code, che restano gli agenti;
- lo mantiene Block, con licenza Apache-2.0, in Rust; circa 37.000 stelle.
  Il README lo dichiara non finito;
- lo stato sta in Postgres: messaggi, canali, flussi, audit, come eventi
  firmati in un registro unico. Il repo git è una cosa che Buzz ospita
  (patch e annunci di repo come eventi, un backend git), non la memoria
  dell'agente;
- skill `SKILL.md` caricate dal runtime non risultano; ci sono gli strumenti
  MCP. I flussi YAML partono da messaggi, reazioni, orari o webhook; le
  approvazioni nei flussi non sono ancora collegate;
- i permessi seguono l'identità dell'agente e i canali, non il progetto.

Lettura: Buzz non sostituisce Claude Code, lo mette in una stanza con altre
persone e altri agenti. Come runtime del metodo non si adatta, perché la
memoria è Postgres e non il repo. Tocca piuttosto
[diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md), cioè
più persone attorno agli stessi repo, e il canale fra sessioni che oggi passa
da Herdr ([session-messaging](../kb/session-messaging.md)).

Il custode lo mette fra i candidati il 2026-11-14. Seconda lettura, lo stesso
giorno: `VISION.md`, `VISION_PROJECTS.md`, i README di `buzz-acp`,
`buzz-agent` e `buzz-app`, e in `docs/` le pagine su database, agenti
remoti, git su object storage e menzioni dai flussi.

- **Come fa girare Claude Code**: `buzz-acp` ascolta i messaggi del canale
  che menzionano l'agente, li raccoglie in un solo prompt per canale e lo
  passa all'agente; la risposta l'agente la scrive nel canale con la CLI di
  Buzz. Claude Code gira tramite l'Agent SDK e chiede una chiave API.
  L'agente lavora in `~/.buzz` per impostazione predefinita; se la cartella
  si possa fissare per agente o per progetto, e se Claude Code vi legga
  `CLAUDE.md` e le skill come in un terminale, non è documentato. Risponde
  solo al proprietario, finché non lo si allarga.
- **Progetti**: un progetto è un evento che elenca dei repo e un canale («A
  project points at repos. That's all it does»), oggi solo progettato.
- **Git**: il relay ospita repo propri, con oggetti in object storage e un
  hook che applica una politica ai push; i commit degli agenti sono firmati
  con la loro chiave. Le protezioni dei rami sono progettate, non fatte; uno
  specchio verso GitHub non risulta.
- **Flussi**: un flusso a orario non lancia un agente in una cartella, può
  solo scrivere un messaggio che lo menziona. Le approvazioni nei flussi oggi
  falliscono.
- **Persone**: ruoli Owner, Admin, Member, Guest e Bot, e l'appartenenza al
  canale come unico confine. Un registro di audit a catena di hash per
  comunità.
- **Installazione**: Postgres, Redis e MinIO, con un compose; app desktop per
  macOS, Windows e Linux, ma i ponti per Claude Code e Codex solo su macOS e
  Linux. Build di anteprima, nessun canale stabile.

Lettura: Buzz sta un livello sopra l'harness, come il metodo, ma su un altro
asse: il metodo dà forma al repo, Buzz mette in relazione persone e agenti.
In linea di principio si compongono, con Claude Code che lavora nel repo del
metodo e riceve i messaggi da un canale. La domanda che decide è quella
lasciata aperta: se l'agente di Buzz può lavorare in una cartella scelta,
con il comportamento nativo dell'harness.

Terza lettura, il 2026-11-14, nel codice: `block/buzz-app` al commit
`4a87b5c` del 13/11 (`docs/agents.md`, `docs/agent-memories.md`,
`src/features/agent-harness/base_prompt.md`,
`src/bundled/claude-code/claude.ts` e `runtime.ts`,
`src/features/solo/workspace.ts`) e `block/buzz` al `5780bd7`
(`crates/buzz-acp`).

- **La cartella di lavoro** è per agente e si configura; il valore
  predefinito è `~/.buzz`, lo stesso per Claude Code, Codex, Goose e Pi,
  quindi senza scelta tutti gli agenti di un utente condividono una
  cartella. Il prompt base vi impone una forma: `RESEARCH/`, `PLANS/`,
  `GUIDES/`, `WORK_LOGS/`, `OUTBOX/`, `REPOS/` per i checkout, `.scratch/`,
  e un `AGENTS.md` con gli agenti attivi e i loro ruoli. È una cartella di
  file, non un repo git: i repo stanno dentro `REPOS/`.
- **Nei repo** l'agente legge i checkout esistenti e modifica in un worktree
  nuovo; nella modalità «solo» le cartelle di progetto sono di sola lettura e
  i worktree nascono da `origin/<ramo>`. Prima di pianificare legge
  `AGENTS.md` del repo, come vincolo di progetto.
- **La risposta alla domanda che decide è sì, con condizioni.** Un plugin può
  dare a una conversazione la sua cartella
  (`ctx.agents.assignConversationFolder`); la sessione parte lì e l'harness
  carica la configurazione del repo, per Claude Code «`CLAUDE.md`,
  `.mcp.json`, skill, hook e impostazioni». La cartella si fissa una volta,
  vale solo sul dispositivo che fa girare l'agente, e solo per Claude Code e
  Codex. Anche la cartella di lavoro dell'agente si può puntare sul repo.
- **Permessi**: nel lancio ordinario Claude Code parte con
  `--permission-mode bypassPermissions`, cioè senza chiedere conferme. Se i
  divieti del giro reggano in quel modo va provato. Nel modo protetto
  l'agente gira in un contenimento e non carica la configurazione del repo.
- **Una memoria propria, fuori da git.** Ogni agente ha una memoria `core`
  iniettata a inizio sessione e una memoria «fredda» (`mem_get`, `mem_set`),
  salvate come eventi cifrati sul relay e leggibili dal proprietario. Il
  prompt base chiede all'agente di tenerci identità, lezioni e obiettivi «fra
  le sessioni», con la fonte di ogni riga, e di non cambiarla senza il
  permesso del proprietario. È lo stesso nodo di Hermes, con in più un prompt
  che la incoraggia; un interruttore non risulta.
- **Hermes dentro Buzz**: `docs/hermes-agent-research.md` (5/10) classifica
  Hermes come harness esterno lanciabile da Buzz. Le due soluzioni si
  compongono anche fra loro.

### Self-hosting e community

Domanda del custode del 2026-11-14: la versione che si installa in proprio
aggiunge comunque uno strato sui dati? Per Buzz una community è lo spazio di
lavoro che si raggiunge da un indirizzo: installato in proprio, un relay
ospita una community; esiste anche un'installazione ospitata per più
community, con gli stessi confini logici.

Installarlo in proprio decide chi custodisce i dati, non dove stanno.
Messaggi, flussi, memoria degli agenti e audit restano in Postgres e
nell'object storage del relay, accanto al repo e non dentro: nessun terzo li
vede oltre al fornitore del modello, ma non sono versionati col repo. Per il
principio fermo conta il secondo punto. I messaggi dei canali sono un
registro, come le trascrizioni di oggi, e non preoccupano; la memoria `core`
e quella fredda sono memoria, e vanno spente o tenute vuote perché a
ricordare sia il repo.

## Confronto fra le quattro soluzioni

Fattori proposti il 2026-11-14 per mettere a confronto `method` (oggi, con
Claude Code o Codex), Hermes, OpenClaw e Buzz. Le quattro non stanno allo
stesso livello, e il primo fattore lo dice; gli altri seguono il principio
fermo (memoria, governo) e il modello di Norman (ciclo), poi scala e
ingresso. Ogni voce dice com'è oggi, per quanto letto; nulla è provato.

### 0. Livello

- **method**: una forma del repo con skill e strumenti; sta sopra un harness
  esistente.
- **Hermes**, **OpenClaw**: un agente completo, che prende il posto
  dell'harness.
- **Buzz**: uno spazio di lavoro che fa da cornice agli harness (Goose,
  Codex, Claude Code) e ha anche un agente proprio.

### A. Memoria

**1. Fonte della memoria**, ciò che l'agente rilegge per decidere.

- **method**: il repo markdown, unica memoria.
- **Hermes**: `MEMORY.md` e `USER.md` del profilo, fuori dal repo,
  spegnibili.
- **OpenClaw**: markdown nello spazio di lavoro, quindi nel repo.
- **Buzz**: per l'harness, il repo se la cartella è il repo; in più la
  memoria `core` e fredda dell'agente sul relay, che il prompt base
  incoraggia.

**2. Richiamo fra sessioni**, l'archivio delle conversazioni e se l'agente
lo interroga.

- **method**: trascrizioni dell'harness, non rilette.
- **Hermes**: `state.db` per profilo, senza interruttore; `session_search` a
  scelta dell'agente, da togliere come insieme di strumenti (dedotto).
- **OpenClaw**: SQLite per agente, senza interruttore; `sessions_search`
  restringibile con `tools.sessions.visibility` o negabile per agente.
- **Buzz**: ogni messaggio è un evento firmato in Postgres, con ricerca a
  testo pieno; il canale stesso è l'archivio.

**3. Apprendimento autonomo**, procedure che l'agente cambia da sé fuori
versione.

- **method**: nessuno; il metodo cambia col proprio ciclo, in git.
- **Hermes**: acceso di serie (skill e memoria); spegnibile la revisione,
  il resto solo in approvazione.
- **OpenClaw**: officina delle skill e «dreaming» accesi di serie, entrambi
  spegnibili; le skill imparate stanno fuori dal repo.
- **Buzz**: guidato dal prompt: le lezioni da un errore vanno in `core`,
  previo permesso del proprietario; nessuna officina di skill trovata.

**4. Forma imposta al repo**, file del runtime che entrano nel repo.

- **method**: la forma è il metodo stesso.
- **Hermes**: nessuna; legge `AGENTS.md` e le skill del progetto.
- **OpenClaw**: file d'identità e note giornaliere; la semina si spegne con
  `skipBootstrap: true`, le note giornaliere no.
- **Buzz**: nessuna nel repo, una nella cartella di lavoro (`RESEARCH/`,
  `PLANS/`, `WORK_LOGS/` e le altre); i repo che ospita stanno nel suo
  object storage.

### B. Governo

**5. Delega e permessi**, dove stanno e se viaggiano col repo.

- **method**: `autonomy.md` e `o3/ciclo/permessi.json`, versionati per repo.
- **Hermes**: configurazione globale del profilo; elenco di divieti,
  contenitore.
- **OpenClaw**: `openclaw.json` globale, strumenti negabili per agente;
  lo spazio di lavoro non è una sandbox.
- **Buzz**: identità dell'agente, appartenenza ai canali, quattordici
  ambiti; Claude Code parte senza conferme (`bypassPermissions`), oppure in
  un contenimento senza la configurazione del repo.

**6. Commit e resoconto**, chi fissa le modifiche e con quale
dichiarazione.

- **method**: `/commit` col gate, trailer di autonomia, impatto ed esiti.
- **Hermes**: nessuna regola sui commit.
- **OpenClaw**: nessun commit automatico; «seguono le tue istruzioni».
- **Buzz**: commit firmati con la chiave dell'agente, politica sui push del
  relay, audit a catena di hash; nessuna dichiarazione di chi ha deciso.

**7. Ciclo autonomo**, chi lo avvia e dove sta la definizione.

- **method**: unità di NixOS (in `nixos`) e lanciatore canonico.
- **Hermes**: lavori pianificati con cartella e skill, in
  `~/.hermes/cron/`.
- **OpenClaw**: automazioni nel gateway, oppure `agent exec --cwd` da un
  pianificatore esterno.
- **Buzz**: flussi a orario che possono solo menzionare un agente in un
  canale.

### C. Ciclo

**8. Goal, World e arco di valutazione**.

- **method**: oggetti persistenti, i sei stadi come collezioni, verdetti con
  provenienza.
- **Hermes**, **OpenClaw**: assenti; la revisione valuta come ha lavorato
  l'agente, non il Mondo.
- **Buzz**: assenti; i flussi reagiscono a eventi.

### D. Scala

**9. Più repo**, l'unità di lavoro e la lettura d'insieme.

- **method**: un repo per adottante, canone via symlink, `/adottanti` li
  legge insieme.
- **Hermes**: un profilo per tanti repo, con memoria in comune; un profilo
  per repo per separarli.
- **OpenClaw**: un agente per spazio di lavoro in un solo gateway,
  instradati per canale e interlocutore.
- **Buzz**: un progetto raggruppa più repo (progettato); una cartella per
  agente o per conversazione, `REPOS/` per i checkout.

**10. Più persone**.

- **method**: un custode; Herdr fra le sessioni.
- **Hermes**: un utente per profilo.
- **OpenClaw**: più persone sullo stesso agente via canali; chi lo usa può
  fargli fare tutto ciò che può fare.
- **Buzz**: il suo punto di forza: ruoli, canali condivisi, agenti come
  membri.

### E. Ingresso

**11. Interfaccia**.

- **method**: terminale e viste generate di sola lettura.
- **Hermes**: cruscotto web estendibile con plugin, app desktop.
- **OpenClaw**: interfaccia di controllo web, canali di chat.
- **Buzz**: app desktop e mobile, canali.

**12. Installazione e piattaforme**.

- **method**: symlink, fork delle skill, strato host su NixOS.
- **Hermes**: installazione nativa anche su Windows; la chat del cruscotto
  lì chiede WSL2.
- **OpenClaw**: app per Windows che installa una propria distribuzione WSL.
- **Buzz**: relay con Postgres, Redis e MinIO; ponti per Claude Code e Codex
  solo su macOS e Linux.

**13. Modelli e costo**.

- **method**: quello dell'harness; oggi Claude Code in abbonamento e Codex.
- **Hermes**: chiave API Anthropic o piano Max con crediti aggiuntivi.
- **OpenClaw**: chiave API, oppure Claude Code (`claude -p`) come motore,
  indicato come via ammessa; su che cosa si paghi non è detto.
- **Buzz**: chiave API per l'agente proprio e per il ponte a Claude Code;
  l'app desktop accede da browser.

**14. Maturità e governo del progetto**.

- **method**: GPL-3.0 per il codice e CC BY-SA 4.0 per i testi, un custode,
  sperimentale.
- **Hermes**: MIT, Nous Research, circa 263.000 stelle.
- **OpenClaw**: MIT, OpenClaw Foundation, circa 394.000 stelle.
- **Buzz**: Apache-2.0, Block, circa 37.000 stelle; dichiarato non finito.

### Che cosa dice il confronto

I fattori 1–8 sono quelli su cui un'integrazione si gioca: dicono se la
memoria e il governo restano nel repo. I fattori 9–14 dicono quanto costa
entrare e quanto lontano si arriva. Hermes e OpenClaw si confrontano col
metodo come alternativa all'harness; Buzz come strato che gli sta accanto,
e per lui contano soprattutto i fattori 7, 9 e 10.

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
2. leggere le pagine di Hermes rimaste: installazione su Windows, modelli
   locali; plugin del cruscotto, storico delle sessioni e ciclo di
   apprendimento letti il 2026-11-14;
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
- gli strumenti lanciati dal canone ([kb-tools](../kb/kb-tools.md)) riducono
  già la dipendenza dallo strato host;
- [diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md): la
  risposta su pubblicazione e osservazione degli adottanti dipende da qui.

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
- [Sessioni](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
- [Strumenti](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
- [Configurazione](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Curatore](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)
- [Estendere il cruscotto](https://hermes-agent.nousresearch.com/docs/user-guide/features/extending-the-dashboard)

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

Buzz:

- [README](https://github.com/block/buzz)
- [Architettura](https://github.com/block/buzz/blob/main/ARCHITECTURE.md)
- [Visione dell'agente](https://github.com/block/buzz/blob/main/VISION_AGENT.md)
- [Visione](https://github.com/block/buzz/blob/main/VISION.md)
- [Progetti](https://github.com/block/buzz/blob/main/VISION_PROJECTS.md)
- [Agenti remoti](https://github.com/block/buzz/blob/main/docs/remote-agents.md)
- [Git su object storage](https://github.com/block/buzz/blob/main/docs/git-on-object-storage.md)
- [buzz-acp](https://github.com/block/buzz/blob/main/crates/buzz-acp/README.md)
- [App desktop](https://github.com/block/buzz-app)
- [Agenti dell'app](https://github.com/block/buzz-app/blob/main/docs/agents.md)
- [Memorie degli agenti](https://github.com/block/buzz-app/blob/main/docs/agent-memories.md)
- [Prompt base degli agenti](https://github.com/block/buzz-app/blob/main/src/features/agent-harness/base_prompt.md)
- [Ricerca su Hermes](https://github.com/block/buzz-app/blob/main/docs/hermes-agent-research.md)

OpenClaw, seconda lettura del 2026-11-14:

- [Più agenti](https://docs.openclaw.ai/concepts/multi-agent)
- [Sessioni](https://docs.openclaw.ai/concepts/session)
- [Ricerca nelle sessioni](https://docs.openclaw.ai/concepts/session-search)
- [Più utenti](https://docs.openclaw.ai/concepts/multi-user)
- [Officina delle skill](https://docs.openclaw.ai/tools/skill-workshop)
- [Fornitori di modelli](https://docs.openclaw.ai/concepts/model-providers)
