---
ciclo: runtime
---

# Casi della delega: un messaggio lungo fra host e una pubblicazione contro il register

Data: 2026-11-27 · Fonte: `nixos` `i1/messaggio-lungo-fra-host.md` e
`i1/pubblicazione-contro-il-register.md` a `331462c`, letti nel checkout
`~/nixos`, e l'inoltro della sessione `nixos` su `deck` via Herdr su
richiesta del custode. Situazioni, comportamenti e riscontri sono
dichiarati dall'agente dell'adottante. Nel repo di origine i casi restano
«da inoltrare» finché non risultano acquisiti da `method`.

## Caso 1: un contenuto non versionato oltre il limite fra host

**Il caso.** Il custode chiede di passare un file Markdown non versionato,
2162 byte, dalla sessione `nixos` su `deck` a una sessione Codex CLI su
`svezia` aperta in un pannello `ssh` di Herdr. Copiare il file sull'host di
lavoro da `deck` sarebbe stato un atto su un host di lavoro. L'agente divide
il file in quattro parti sotto i 1000 caratteri, intestate «Parte n/4»;
chiede al destinatario di non agire prima dell'ultima e di rispondere solo
«ricevuta n/4». Prima di ogni `Enter` controlla campo vuoto, host e fine
della parte visibile; alla fine confronta lo sha256. Il file arriva integro.
Il conteggio di Codex, 2140, sembrava un errore: erano caratteri contro
byte. La scrittura del file sul destinatario l'ha approvata il custode. Il
caso si è chiuso poi versionando il contenuto.

**Questione dell'adottante.** In
[session-messaging](../kb/session-messaging.md), § «Sessione su un altro
host»: l'invio a parti numerate con conferma per un contenuto non
versionato, e un'impronta sha256 sui byte come verifica finale invece del
conteggio dei caratteri.

**Fatti accanto al caso.**

- Il nodo, a `3dcb08d`, tiene il messaggio sotto i 1000 caratteri e lo fa
  rimandare al contenuto versionato; non tratta il contenuto che versionato
  non è. Il limite viene da un altro invio da `deck` a `svezia`, il
  2026-11-26.
- L'esito finale è il rimando che il nodo già preferisce: le parti numerate
  hanno fatto da ponte, non da forma stabile.
- La verifica per byte non dipende dal contenuto non versionato: vale anche
  per un rimando a un file da confrontare sui due host.
- Un caso solo, dichiarato dall'adottante.

## Caso 2: un atto verso l'esterno autorizzato contro un obiettivo del register

**Il caso.** Il custode chiede di rendere pubblico il repo `nixos` su
GitHub, come fonte unica delle scorciatoie anche per il repo di lavoro.
L'agente controlla la storia (`privacy.py --storia`, 0 riscontri) e, su
conferma esplicita, cambia la visibilità. L'obiettivo 5 di `goal.md` di
`nixos` vuole il repo privato, perché tiene sintesi e verdetti sui membri
del gruppo, e fra i segnali dichiara la visibilità privata. Né il custode né
l'agente l'hanno riletto prima. La contraddizione emerge nello stadio
`compare` del `/cycle`, leggendo `goal.md` per il minimo dello stadio; il
custode sceglie di tornare privato. Il repo resta pubblico dalle 07:24 alle
14:48 (ora locale, `updated_at` di GitHub). Il contenuto sui membri era
infrastrutturale e aggregato; il link pubblico dato a una sessione di lavoro
non è più leggibile. La fonte unica nasce in un repo pubblico separato,
`steledama/sdr`.

**Questione dell'adottante.** Prima di un atto verso l'esterno e difficile
da annullare, anche autorizzato, cercare nel register le clausole che lo
toccano: il consenso su un atto non sostituisce il confronto con il nord
scritto dal custode stesso. Nodi: [consent](../kb/consent.md),
[goal-register](../kb/goal-register.md).

**Fatti accanto al caso.**

- `consent` ha già un gemello sul lato valutazione: prima di affermare un
  fatto, controllarlo alla fonte invece che a memoria. Non nomina il
  register come fonte da rileggere prima di un atto, e il consenso
  dell'atto qui c'era.
- `goal-register` dice che il motivo resta del custode e che gli agenti
  possono proporre uno scostamento. Un atto che contraddice un obiettivo,
  chiesto dal custode, è di fatto uno scostamento non dichiarato come tale.
- L'intercettazione è venuta dal ciclo, dopo l'atto: il `compare` ha fatto
  da rete, non da guardia.
- Un caso solo, dichiarato dall'adottante.
