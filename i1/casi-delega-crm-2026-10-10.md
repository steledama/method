---
ciclo: runtime
---

# Casi della delega: primo ciclo di `crm` sul checkout di `svezia`

Data: 2026-10-10 · Fonte: `crm` `i1/casi-delega-2026-10-10.md` a
`ca59b1e`, con le decisioni del custode a `2f2c582` e `e396bc8`, letti su
`origin`. Acquisiti nel giro di `method` del 2026-10-10. Nel repo di origine
i casi restano «da inoltrare» finché il giro locale non li segna «acquisita
da method».

## Contesto

Primo ciclo congiunto `eval → exec → commit` delegato del CRM, avviato dal
custode nel checkout `/home/sviluppo/crm` su `svezia` a `e0dad24`. Su quel
host gira `presentazione-crm-pubblicazione.timer`, che ogni cinque minuti
pubblica l'`HEAD` del checkout sulla porta 8002. Nella stessa sessione il
custode ha tolto le due eccezioni di `svezia`: rilascio e pubblicazione
seguono pull e commit con push del ciclo.

## I due casi

1. **Pull prima di riconoscere l'host.** Il bootstrap ha eseguito
   `git pull --ff-only` sul CRM e sul checkout di `method`, e solo dopo
   `hostname` ha restituito `svezia`, dove il pull era su richiesta. Entrambi
   i pull erano no-op. L'agente l'ha dichiarato come errore di
   ricostruzione; il custode l'ha giudicato corretto e ha tolto l'eccezione.
   Questione dell'adottante: una regola che dipende dal checkout regge solo
   se il bootstrap fa riconoscere il checkout prima del primo atto.
2. **Il commit del ciclo pubblica le viste di produzione.** `ciclo-delegato`
   include commit e push; gli atti fuori delega includevano ogni atto su
   `svezia`, pubblicazione compresa. L'agente ha completato gli stadi fino a
   `specify`, ha fermato `perform` e ha sospeso il commit per chiedere. Il
   custode ha autorizzato l'atto e poi cambiato il criterio. Questione: la
   delega del ciclo presuppone un checkout di sviluppo; ipotesi
   dell'adottante, non regola: `autonomy.md` dichiara in quali checkout vale
   la delega.

## Fatti accanto ai casi

- L'indizio di `pull-autonomo` per `crm` chiedeva di verificare che il
  servizio non leggesse file dal checkout; non nominava il timer delle
  viste, che rende il commit una pubblicazione.
- In entrambi i casi la conferma richiesta si è rivelata inutile per
  dichiarazione del custode, nella stessa sessione.
