---
title: "Cognizione condivisa"
subtitle:
  "Framework metodologico e osservatorio cross-repo per la progettazione di
  artefatti di supporto alla cognizione condivisa tra uomo e modelli di
  intelligenza artificiale tramite knowledge base (KB) e superfici versionate
  del ciclo d'azione"
author: "Stefano Pompa · stefano.pompa@gmail.com · github.com/steledama/method"
date: "2026.07.05"
ciclo: dev
---

## LLM, harness, artefatto {.img data-background-image="../i2/llm-harness-method.png" data-background-size="contain" data-background-color="#fef9e6"}

## Artefatto, sistema, metodo {.img data-background-image="../i2/artifact-system-method.png" data-background-size="contain" data-background-color="#fef9e6"}

## Il ciclo dell'azione (Norman) {.img data-background-image="../i2/action-cycle-norman.png" data-background-size="contain" data-background-color="#fefaea"}

## Dal ciclo di Norman al metodo

- i poli non si eseguono: lo **scopo** motiva, il **mondo** è ritagliato per
  rilevanza guidata dallo scopo
- sei atti, sei superfici versionate: piani, compiti, prescrizioni · percezioni,
  interpretazioni, confronti
- a ogni stadio l'umano ispeziona e l'LLM rientra senza ricostruire: più
  trasparenza, più controllo
- il riflessivo da solo non muove, il viscerale da solo è cieco: i livelli si
  servono a vicenda

## La rilettura del metodo {.img data-background-image="../i2/action-cycle-method.png" data-background-size="contain" data-background-color="#fefbea"}

## Leggere il ciclo

- i1 cattura, i2 interpreta, i3 giudica rispetto al Goal: la valenza entra nel
  confronto
- il Mondo dipende dal ciclo: dominio nel runtime, artefatto nello sviluppo; può
  avere una propria storia Git
- un compito ha risultato e condizioni concrete; non coincide automaticamente
  con un'operazione di Leontiev
- la KB informa la comprensione insieme a richiesta, strumenti e segnali; il
  system image comprende l'intero artefatto

## Runtime cycle and development meta-cycle

- the runtime cycle is the main loop: the artifact acts on the domain and reads
  back its response
- the development meta-cycle shapes the machine that makes runtime possible
- dev is not a second loop beside runtime: it is the reflective loop above it
- portability is a quality of the runtime machine, not a replacement for the
  domain

## Runtime cycle / development meta-cycle {.img data-background-image="../i2/development-meta-cycle.png" data-background-size="contain" data-background-color="#fcf6e3"}

## Sviluppo del metodo {.img data-background-image="../i2/method-development-loop.png" data-background-size="contain" data-background-color="#fdf8e5"}

## Artefatto, KB, mondo {.img data-background-image="../i2/artifact-kb-world.png" data-background-size="contain" data-background-color="#fef9e6"}

## Una lente sul livello viscerale: `o3 <-> i1` {.hero}

Le prescrizioni preparano l'azione.

Le percezioni catturano il segnale del mondo.

Qui il ciclo aggancia il reale.

## Una lente sul livello comportamentale: `o2 <-> i2` {.hero}

Le interpretazioni **rivelano**, i compiti **risolvono**.

Quando una soluzione diventa stabile, sedimenta nei nodi della KB.

La KB, insieme ai dati del mondo, orienta nuove interpretazioni.

## Una lente sul livello riflessivo: `o1 <-> i3` {.hero}

I confronti rivelano tensioni, priorità e drift.

I piani risolvono orientando il lavoro futuro.

Qui il ciclo decide che cosa conta e dove andare.

## Tre livelli, una KB {.hero}

Il viscerale aggancia il mondo.

Il comportamentale trasforma segnali in lavoro.

Il riflessivo governa senso e direzione.

La KB trattiene ciò che deve sopravvivere al singolo giro.

## Verificare la maturità

- una coda vuota e un battito automatico sono indizi: servono esiti runtime e
  segnali aggiornati
- attendere o rinunciare può essere una decisione informata; l'inazione da sola
  non prova un difetto
- funzione e contenuto guidano la collocazione; ritmi diversi aiutano a separare
  responsabilità
- le fonti sostengono le attribuzioni; analogie e ipotesi del metodo restano
  dichiarate come tali

## Separazioni utili

- conoscenza stabile nella **KB**
- segnali, interpretazioni e verdetti distinti
- piano sintetico e specifiche operative separate
- task consumabili distinti dalle skill permanenti
- storia affidata a **Git**, non accumulata nei documenti
- strumenti deterministici separati dal giudizio
- **Goal** e **Mondo** espliciti come confini
- sviluppo dell’artefatto distinto dal suo uso nel dominio

## Conclusioni {.hero}

Umano e agente collaborano attraverso un **artefatto persistente** che conserva
conoscenza, lavoro, giudizi e capacità in forme diverse, permettendo al ciclo di
continuare tra sessioni senza affidarsi alla memoria della chat.

Questo metodo è la mia risposta attuale a questa esigenza: non l’unica
possibile, ma quella che sto mettendo alla prova e che propongo alla
discussione.
