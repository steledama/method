---
sintesi: "Il repo è oggi un esperimento per una persona sola che governa più repo propri con un metodo uniforme. Che cosa cambia, nella pubblicazione delle viste e nell'osservazione degli adottanti, se il metodo si diffonde oltre il custode unico? Trasformato il 2026-11-13 dal task sulla pubblicazione decisa dal repo; niente da implementare, in pausa fino al riesame del ciclo autonomo."
ciclo: dev
---

# Diffusione oltre il custode unico

## Origine

Fino al 2026-11-13 questo task era «Pubblicazione decisa dal repo»: il repo
dichiara dove si pubblica, l'host tiene una porta sola con uno smistatore
davanti a un servitore per repo e un elenco dei checkout ammessi (proposta
di `nixos` del 2026-10-31, adottata dal custode l'8/11). Quel disegno è
abbandonato e resta in git, con la valutazione punto per punto.

Il 2026-11-13 il custode lo ha ripensato in sessione, partendo dal bisogno
di mostrare la vista di `method` in ufficio. Una seconda vista su `svezia`
sarebbe rimasta indietro rispetto a quella di `deck`, o avrebbe chiesto un
clone separato: la richiesta a `nixos-lavoro` è stata annullata prima di
ogni modifica. La vista resta una, su `deck:8001`, raggiungibile da
`norvegia` via VPN; per l'ufficio basta un inoltro temporaneo da
`norvegia`, atto di `nixos-lavoro` quando servirà.

## La domanda

Il metodo oggi presuppone un custode solo, sette repo quasi tutti locali e
host che lui stesso configura. Che cosa va ripensato se chi lo adotta è
qualcuno che il custode non conosce, con i propri host e i propri repo?

Due superfici lo mostrano già:

- **la pubblicazione delle viste**: oggi è l'host a dire chi serve cosa
  (`kb/view-publishing.md`, «Servizio sulle reti private»);
- **l'osservazione degli adottanti**: `/adottanti` e `o3/adottanti.py`
  leggono un elenco chiuso in `world.md`, via checkout locali e `ssh`.

## Emerso il 2026-11-13

- La pubblicazione è una scelta di chi tiene il checkout: lavorare in modo
  snello sul solo testo, oppure servire la vista, comoda per gli umani ma
  con un carico di build e di servizio.
- Un elenco di host versionato nel repo non regge alla scala: chi clona ha
  i propri host, e i nomi scritti dentro per lui non significano niente.
  Resta l'interruttore locale al checkout, che però è stato non versionato:
  va deciso come renderlo leggibile, per esempio dichiarato dalla resa.
- L'esclusività dell'host esiste contro le rese a versioni diverse. Ogni
  resa parte già da un commit pulito e dichiara il commit che serve: se la
  regola dell'host unico serva ancora è da decidere qui, non prima. Fino ad
  allora il canone resta com'è.
- I ruoli production e standby di `nixos-lavoro`, su cui poggiava
  l'evidenza del vecchio task, non esistono più: `svezia` è il server,
  `norvegia` la postazione di sviluppo.
- L'audit degli adottanti presuppone che il custode possa leggere ogni
  repo. Con adottanti sconosciuti l'osservatorio cambia natura o sparisce.

## Dipendenze

La risposta dipende da [integrazione-runtime](integrazione-runtime.md): se
il metodo gira sopra un runtime esistente, pubblicazione e osservazione
possono diventare materia sua. Si lega anche a
[nome-del-progetto](nome-del-progetto.md) e a
[traduzione-inglese](traduzione-inglese.md).

## Criterio di chiusura

Il custode decide se la diffusione è uno scopo del progetto. Se sì, il task
si divide in lavori eseguibili sulle due superfici; se no, si rimuove con
la riga del plan e la voce in `o2/tasks.md`.

Connessioni:

- [view-publishing](../kb/view-publishing.md)
- [method-observatory](../kb/method-observatory.md)
