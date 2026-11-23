---
sintesi: "Un ricordo degli episodi del gruppo (conversazioni, cicli, dinieghi) in un SQLite fuori da git, governato dal metodo e ad accesso dichiarato nella delega, distinto dalla memoria versionata nel repo. Oggi la regola di CLAUDE.md lo esclude; cambiarla è una modifica del canone che decide il custode, quando la forma è matura."
ciclo: dev
---

# Ricordo del gruppo

## Origine

Staccato il 2026-11-24 dal task chiuso `coordinatore-di-gruppi` (in git),
sezione «La memoria», quando il resto del quadro era compiuto: il
coordinamento di casa passato a `nixos`, il sito di gruppo fatto, la chat in
[chat-del-coordinatore](chat-del-coordinatore.md).

Il custode considera la memoria aperta: oggi il metodo la chiude, e
probabilmente è una mancanza. La regola di `CLAUDE.md` («Memoria») è nata
contro la memoria dell'harness: opaca, legata all'host, senza governo. Un
SQLite del metodo è un'altra cosa, se resta governato.

## Forma proposta

Proposta del custode: un SQLite fuori da git, a cui si decide se si può
accedere nel ciclo interattivo o in nessun ciclo.

Distinzione proposta dall'agente:

- **memoria**: conoscenza, decisioni, verdetti. Resta nel repo, versionata;
- **ricordo**: gli episodi, cioè conversazioni, cicli, dinieghi. Va
  nell'SQLite. In parte esiste già, sparso fra le trascrizioni degli harness
  e il registro della chat.

## Condizioni

Perché il ricordo non diventi la seconda memoria criticata in Hermes e in
Buzz (studio di integrazione, chiuso il 2026-11-24, in git):

- **derivato, mai fonte**: cancellarlo non deve perdere nulla che il repo
  non sappia ricostruire, salvo il registro degli episodi;
- **l'accesso si dichiara nella delega**: i modi stanno in `autonomy.md`,
  versionati; il contenuto no;
- **si parte da «nessuno» e si sale per gradini**, come ogni delega;
- **ciò che conta risale nel repo**: il ricordo non è mai l'unico posto di
  una decisione, e il gate di `/commit` è il punto in cui risale, come nel
  filing back;
- **provenienza**: una decisione presa usando un ricordo lo cita nel
  resoconto;
- **un ricordo per gruppo, non per host**.

## Passi

1. Raccogliere dagli episodi reali (chat, sessioni, cicli) quali domande il
   ricordo dovrebbe rendere rispondibili, e quali oggi restano senza
   risposta.
2. Proporre schema, sede sull'host del coordinatore e modi d'accesso.
3. Portare al custode la modifica della regola di `CLAUDE.md` («Memoria»).

## Criterio di chiusura

Il custode ha deciso se il ricordo entra nel canone, con quali modi
d'accesso, e la regola di `CLAUDE.md` è aggiornata di conseguenza; oppure ha
deciso di tenerla com'è, col motivo.

Connessioni:

- [chat-del-coordinatore](chat-del-coordinatore.md)
