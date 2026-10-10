---
data: 2026-10-10
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# La delega del ciclo vale anche nel checkout servito

## Cosa e perché

Il custode ha deciso il 2026-10-10: dove il checkout è anche una
superficie servita, perché un timer, un cron o uno scheduler ne eseguono o
pubblicano i file, **la delega del ciclo vale come altrove**. Commit, pull
e push del ciclo restano autorizzati; il resoconto dichiara cosa hanno
rilasciato o pubblicato. Le eccezioni sono nominate in `autonomy.md`, e
per applicarle l'agente riconosce host e checkout prima del primo atto
della sessione, pull compreso. Il canone è in
[consent](../kb/consent.md).

Il motivo è nei casi della delega di `bi` e `crm`
([lettura](../i2/casi-delega-adottanti.md)): il commit in esercizio prima
del push, il pull partito prima di riconoscere `svezia`, il commit che
pubblica le viste sospeso per una conferma che il custode ha giudicato
inutile. La regola rovescia il default: si nominano le eccezioni, non ogni
superficie. È già la pratica delle viste su `deck` e la decisione presa da
`crm` il 2026-10-10.

## Ricetta per il /method locale

1. Verificare se un processo esegue o pubblica i file del checkout
   (Task Scheduler, timer utente, cron, `docker compose` che legge la
   configurazione dal checkout, pubblicazione delle viste).
2. Se sì, decidere col custode se serve un'eccezione. Senza eccezioni non
   si scrive nulla di nuovo: vale la regola di partenza. Con un'eccezione,
   `autonomy.md` nomina superficie, atto escluso o condizione che lo
   ammette. Le eccezioni già scritte in `CLAUDE.md` restano valide e si
   raggiungono da `autonomy.md`.
3. Nella bussola (`CLAUDE.md`, `AGENTS.md`), se il repository ha più
   checkout con ruoli diversi, dire come l'agente riconosce host e
   checkout prima del primo atto (per esempio `hostname`).
4. Registrare nel marker il recepimento o l'adattamento motivato.

## Indizi da verificare sul posto

Lettura del 2026-10-10 dai file su `origin`:

- **crm**: `autonomy.md` mette fra gli atti fuori delega ogni atto su
  `svezia` e ne esclude pull, commit e push del ciclo con i loro effetti.
  È già la regola: l'elenco può semplificarsi, senza obbligo.
- **baserow**: `CLAUDE.md` «Pull remoto» tiene su richiesta il pull del
  checkout, perché i timer di backup e freschezza eseguono gli script da
  lì. È un'eccezione già scritta: va confermata o lasciata cadere dal
  custode e resa raggiungibile da `autonomy.md`.
- **bi**: `CLAUDE.md` «Push remoto» ammette il push del codice eseguito dal
  ciclo dopo l'intera suite verde. È una condizione, non un divieto: resta
  come eccezione nominata.
- **danea-auto**: `autonomy.md` ammette il pull su `danea2` solo fuori dagli
  slot del Task Scheduler. Già conforme.
- **nixos**, **salute**, **economia**: su `deck` le viste seguono ogni
  spostamento di `HEAD`; nessuna eccezione nota. Per `nixos` verificare se
  altri host hanno checkout serviti.
