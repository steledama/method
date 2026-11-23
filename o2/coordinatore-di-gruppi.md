---
sintesi: "Il metodo diventa un coordinatore di gruppi di artefatti: ogni repo è un artefatto cognitivo, un gruppo (casa, lavoro) si governa da un unico sito che rende il markdown dei suoi repo e permette di lavorare in chat con gli agenti, agnostico rispetto all'harness e al sistema operativo. La memoria si apre con un ricordo SQLite fuori da git ad accesso dichiarato. Goal ratificato e prime due istanze decise il 2026-11-14: casa, che nasce come repository della prova ACP, e tt."
ciclo: dev
---

# Coordinatore di gruppi

## Origine

Direzione posta dal custode il 2026-11-14, a valle del confronto fra
`method`, Hermes, OpenClaw e Buzz ([integrazione-runtime](integrazione-runtime.md))
e della prova di una chat ACP (task chiuso il 2026-11-14, in git). Se dopo la prova il
metodo ha senso di esistere, prende un nome
([nome-del-progetto](nome-del-progetto.md)) e diventa un coordinatore di
repo:

- ogni repo è un artefatto cognitivo, e il metodo è a sua volta un artefatto
  che ne coordina altri;
- un gruppo è il metodo più uno o più repo, e si gestisce da un unico sito
  web. Il metodo parte da solo, e i repo gli si aggiungono;
- il metodo governa, coordina, monitora e aggiorna il funzionamento degli
  artefatti del gruppo;
- ogni artefatto è agnostico rispetto all'harness e al sistema operativo;
- non un sito per artefatto ma uno per gruppo. Dal sito si legge in HTML il
  markdown dei repo e si lavora in chat con gli agenti; le pagine seguono sia
  le modifiche fatte in chat col custode sia le azioni dei giri autonomi
  sul markdown.

I gruppi di oggi sono due, separati e distinti:

- **casa**: `nixos`, `salute`, `economia`;
- **lavoro**: `nixos-lavoro`, `danea-auto` (Windows), `baserow`, `bi`, e
  `abbinatore`, entrato il 2026-11-16.

Nella mappa degli strati del task d'origine, il coordinatore occupa
coordinazione e ingresso, dove il metodo oggi è debole, e lascia fermi
memoria e governo, dove è forte. L'harness resta esterno, raggiunto via ACP.

## Che cosa cambia rispetto a oggi

- **Da osservatore a coordinatore.** Oggi `world.md` tratta gli adottanti
  come il Mondo che `method` osserva, e il canone arriva loro via symlink.
- **Un sito per gruppo.** Oggi ogni repo ha la sua porta e il suo
  `serve.py` (sei viste fra `deck` e `svezia`, più `danea2`); diventerebbero
  due siti, casa e lavoro.
- **Il sito è anche il posto dove si lavora.** Oggi la vista è di sola
  lettura e la chat è il terminale.

## Il sito di gruppo

Precisato dal custode il 2026-11-20:

- **i membri si dichiarano nel `world.md` dell'istanza**: è il registro da
  cui la build del sito ricava quali viste e presentazioni rendere, non solo
  un elenco da leggere: la sezione `## Membri` del contratto
  (`kb/view-publishing.md`, «Sito di gruppo»), oggi nel `world.md` di
  `nixos` per casa e di `nixos-lavoro` per il lavoro;
- **l'istanza è membro del proprio sito**: la home elenca l'istanza e i
  membri, ciascuno con la sua vista e la sua presentazione. Nel caso minimo,
  un'istanza senza membri, il sito rende solo l'istanza stessa;
- **un servizio per host, non per repo**: su `deck` il sito di casa
  sostituisce le viste di `nixos`, `salute` ed `economia`
  (`deck:8002`–`8004`); dal 2026-11-23 lo serve `nixos`, senza la pagina
  di `casa`. Cambiano il registro
  `o3/presentations.nix` di `nixos`, il servizio per repo di
  `kb/view-publishing.md` e gli indirizzi in `world.md`;
- **il canone resta fuori dal gruppo**: `method` non è membro di casa;
  la sua vista (`deck:8001`) resta finché un punto successivo non ne decide la
  sorte.

## Punti da chiarire

1. **Canone e coordinatore di gruppo: deciso il 2026-11-14.** «Casa e
   lavoro condividono strumenti, hanno governi distinti» (presentazione di
   `nixos`): se `method` coordinasse anche il gruppo lavoro, lo stato di quel
   gruppo finirebbe nel repo personale del custode. Il canone resta uno e
   condiviso (nodi e codice, `method`); ogni gruppo ha un coordinatore, un
   repository istanza con il proprio stato, che adotta il canone come oggi
   gli adottanti. È la distinzione fra `method` e gli adottanti, spostata di
   un livello. Le istanze decise dal custode:
   - **casa**, su `deck`, coordina `nixos`, `salute` ed `economia`; nasce
     come repository della prova ACP;
   - **tt**, per il lavoro, coordina `nixos-lavoro`, `danea-auto`,
     `baserow`, `bi` e l'`abbinatore`; si apre se l'istanza casa regge.

   **Rivisto il 2026-11-23.** Il custode sente il repository istanza come un
   onere in più: `casa` tiene poco di suo (i membri nel `world.md`, una
   delega di sola lettura, un task), mentre il codice di sito e chat vive nel
   canone e il servizio in `nixos`. Il coordinatore non è più un repo
   apposito ma un membro del gruppo eletto a coordinarlo:
   - **casa** è coordinata da `nixos`, che dichiara i membri nel proprio
     `world.md`; il repository `casa` si cancella del tutto, cancellato su
     GitHub il 2026-11-23: il custode non vuole repo morti per poche righe
     di storia, e la prova ACP resta raccontata nei task di `method`;
   - **lavoro** è coordinato da `nixos-lavoro`, con lo stesso schema:
     l'istanza `tt` non si crea;
   - **il codice di sito e chat resta nel canone** (`o3/view/`,
     `o3/chat/`): è generico e serve a tutti i gruppi; il coordinatore tiene
     solo membri, delega, coda e il servizio sull'host;
   - **`method` non coordina nessun gruppo**: perderebbe la generalità del
     canone, e lo stato del gruppo lavoro finirebbe nel repo personale del
     custode, il motivo della decisione del 2026-11-14;
   - **`nixos` torna privato**: un coordinatore percepisce i membri e ne
     scrive sintesi, verdetti e task, e `salute` ed `economia` sono privati.
     Coordinare «alla cieca» da un repo pubblico, senza mai scrivere del
     contenuto dei membri, è stato scartato perché poggia sulla sola
     disciplina dei giri. `nixos-lavoro` è già privato.

   Il gruppo lavoro adotta anche il sito di gruppo (custode, 2026-11-23), in
   un secondo tempo: `nixos-lavoro` ha già i membri nel proprio `world.md`
   (`e108c29`), resta il servizio su `svezia`.

2. **Il sito di lavoro deve raggiungere `danea2`.** Un sito su `svezia` che
   fa lavorare anche `danea-auto` parla con un harness su Windows. ACP passa
   su standard input e output, quindi in linea di principio anche via ssh;
   l'agnosticismo rispetto al sistema operativo va provato. I ponti di Buzz
   per Claude Code e Codex su Windows non ci sono.
3. **Decisioni che cambiano.** Il 2026-11-13 il custode ha annullato una
   seconda vista di `method` su `svezia`, per non avere una copia che resta
   indietro ([diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md),
   «Origine»). Con un sito per gruppo il checkout di `method` sull'host di
   lavoro è il motore di quel sito, non una copia della vista: la
   preoccupazione si scioglie, ma la decisione va riaperta in modo
   esplicito. Cambiano anche `kb/view-publishing.md` (servizio per repo) e il
   ruolo di `world.md`; `/adottanti` è ritirato il 2026-11-23, e gli
   strumenti passano al coordinatore
   ([strumenti-del-coordinatore](strumenti-del-coordinatore.md)).

## La memoria

Il custode la considera aperta: oggi il metodo la chiude, e probabilmente è
una mancanza. La regola di `CLAUDE.md` («Memoria») è nata contro la memoria
dell'harness: opaca, legata all'host, senza governo. Un SQLite del metodo è
un'altra cosa, se resta governato.

Proposta del custode: un SQLite fuori da git, a cui si decide se si può
accedere in autonomia nel ciclo autonomo, nel ciclo interattivo, o in
nessuno dei due.

Distinzione proposta dall'agente:

- **memoria**: conoscenza, decisioni, verdetti. Resta nel repo, versionata;
- **ricordo**: gli episodi, cioè conversazioni, giri, tentativi, dinieghi.
  Va nell'SQLite. In parte esiste già, sparso fra le trascrizioni degli
  harness e i `tentativi.jsonl` dei giri.

Condizioni perché il ricordo non diventi la seconda memoria criticata in
Hermes e in Buzz:

- **l'accesso si dichiara nella delega**: i tre modi stanno in
  `autonomy.md`, versionati; il contenuto no;
- **si parte da «nessuno» e si sale per gradini**, come ogni delega del
  giro;
- **ciò che conta risale nel repo**: il ricordo non è mai l'unico posto di
  una decisione, e il gate di `/commit` è il punto in cui risale, come nel
  filing back;
- **provenienza**: una decisione presa usando un ricordo lo cita nel
  resoconto;
- **un ricordo per gruppo, non per host**.

Cambiare la regola di `CLAUDE.md` è una modifica del canone e la decide il
custode, quando questa sezione sarà matura.

## Goal

Ratificato dal custode il 2026-11-14: il Goal di sviluppo di `goal.md` ora
parla di gruppi di artefatti al posto di «un ciclo autonomo di runtime in
ogni repo».

## Dipendenze

- [chat-del-coordinatore](chat-del-coordinatore.md): il primo lavoro
  eseguibile, la chat dal sito, che parte dalla prova ACP riuscita;
- [nome-del-progetto](nome-del-progetto.md): il coordinatore prende un nome;
- [integrazione-runtime](integrazione-runtime.md): la scelta della via;
- [diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md): la
  pubblicazione delle viste trova qui una risposta parziale.

## Passi

1. ~~Ratificare il Goal~~ fatto il 2026-11-14.
2. ~~Decidere canone e coordinatore di gruppo~~ fatto il 2026-11-14: istanze
   casa e tt.
3. ~~Creare l'istanza casa~~ fatto il 2026-11-14: `~/casa` su `deck`,
   commit `107f89b`; dal 2026-11-20 ha il remote privato `steledama/casa`.
   Non è ancora nel `world.md` di `method`, perché entrarvi la metterebbe
   sotto `/adottanti` prima che abbia una delega sui repo del gruppo.
   Superato il 2026-11-23 (punto 1, «Rivisto»): `casa` si cancella.
4. ~~Passare il coordinamento a `nixos`~~, dopo la revisione del 2026-11-23:
   `nixos` reso privato; in `nixos` la sezione dei membri nel `world.md`, la
   delega di lettura su `salute` ed `economia` e il task delle skill di
   `casa`; il sito su `deck:8002` senza la pagina di `casa`; in `method`
   `world.md` e `kb/view-publishing.md`; `steledama/casa` cancellato e il checkout
   `~/casa` tolto. Fatto tutto il 2026-11-23: `nixos` `afd5e8d` (membri,
   delega `gruppo-in-lettura`, task delle skill, sito e chat da `~/nixos`). I passi in `nixos` e su `casa` sono atti di quei
   repo o di un'autorizzazione esplicita del custode.
5. Dividere il task in lavori eseguibili: il sito di gruppo è fatto il
   2026-11-20 (task chiuso, in git: casa su `deck:8002`, contratto in
   `kb/view-publishing.md`, «Sito di gruppo»), la chat
   [chat-del-coordinatore](chat-del-coordinatore.md); resta il ricordo
   (l'istanza tt non si crea dal 2026-11-23).

## Criterio di chiusura

I tre punti da chiarire hanno una decisione, il coordinamento di casa è
passato a `nixos`, e il lavoro è diviso in task eseguibili nel plan.
