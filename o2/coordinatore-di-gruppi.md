---
sintesi: "Il metodo diventa un coordinatore di gruppi di artefatti: ogni repo è un artefatto cognitivo, un gruppo (casa, lavoro) si governa da un unico sito che rende il markdown dei suoi repo e permette di lavorare in chat con gli agenti, agnostico rispetto all'harness e al sistema operativo. La memoria si apre con un ricordo SQLite fuori da git ad accesso dichiarato."
ciclo: dev
decidere: "Ratificare la modifica proposta al Goal di sviluppo in goal.md (sezione «Proposta per il Goal»)?"
---

# Coordinatore di gruppi

## Origine

Direzione posta dal custode il 2026-11-14, a valle del confronto fra
`method`, Hermes, OpenClaw e Buzz ([integrazione-runtime](integrazione-runtime.md))
e della [prova di una chat ACP](prova-chat-acp.md). Se dopo la prova il
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
  presto `abbinamenti`.

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

## Punti da chiarire

1. **Canone e coordinatore di gruppo.** «Casa e lavoro condividono
   strumenti, hanno governi distinti» (presentazione di `nixos`). Se `method`
   coordinasse anche il gruppo lavoro, lo stato di quel gruppo (membri,
   verdetti, decisioni) finirebbe nel repo personale del custode. Proposta
   dell'agente: distinguere il canone, uno e condiviso (nodi e codice), dal
   coordinatore di gruppo, un'istanza con il proprio stato, una per casa e
   una per lavoro. È la distinzione di oggi fra `method` e gli adottanti,
   spostata di un livello. Resta da decidere dove viva lo stato del
   coordinatore di lavoro.
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
   ruolo di `world.md` e `/adottanti`.

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

## Proposta per il Goal

Il Goal di sviluppo di `goal.md` dice oggi: «governo operativo delegato
all'agente, **in direzione di un ciclo autonomo di runtime in ogni repo**».
Proposta di riformulazione di quel passaggio, da ratificare dal custode:

> governo operativo delegato all'agente, in direzione di **gruppi di
> artefatti**: ogni repo un artefatto cognitivo con il proprio ciclo
> autonomo di runtime, ogni gruppo coordinato dal metodo attraverso un unico
> sito, da cui si leggono i repo del gruppo e si lavora con gli agenti;
> agnostico rispetto all'harness e al sistema operativo

Il resto del Goal (ambito di autonomia dichiarato, tracciabilità, al
custode scopi, territorio e deleghe, basso attrito di lettura) resta com'è.

## Dipendenze

- [prova-chat-acp](prova-chat-acp.md): la chat dal sito presuppone che una
  sessione ACP si comporti come il terminale;
- [nome-del-progetto](nome-del-progetto.md): il coordinatore prende un nome;
- [integrazione-runtime](integrazione-runtime.md): la scelta della via;
- [diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md): la
  pubblicazione delle viste trova qui una risposta parziale.

## Passi

1. Il custode ratifica, o corregge, la proposta per il Goal.
2. Decidere il punto 1, canone e coordinatore di gruppo, prima di ogni
   lavoro sul sito.
3. Dopo la prova ACP, dividere il task in lavori eseguibili: sito di gruppo,
   chat, ricordo.

## Criterio di chiusura

Il Goal è ratificato, i tre punti da chiarire hanno una decisione, e il
lavoro è diviso in task eseguibili nel plan.
