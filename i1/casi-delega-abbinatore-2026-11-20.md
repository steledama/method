---
ciclo: runtime
---

# Casi della delega: il passaggio dell'abbinatore a `svezia`

Data: 2026-11-20 · Fonte: `abbinatore` `i1/casi-delega-2026-11-20.md` a
`4038a16`, letto nel checkout `~/abbinatore`, e l'inoltro della sessione
`abbinatore` via Herdr su richiesta del custode. Situazioni, comportamenti e
riscontri sono dichiarati dall'agente dell'adottante; la sessione `bi` e il
custode compaiono come riportati. Nel repo di origine i casi restano «da
inoltrare» finché non risultano acquisiti da `method`.

## Contesto

Passaggio dell'abbinatore da AWS a `svezia`, condotto in sessione interattiva
dal custode con le sessioni `bi` e `nixos` collegate via Herdr. Primo
inoltro di casi della delega da `abbinatore`, adottante dal 2026-11-16.

## Caso 1: una verifica parziale presentata come completa

**Il caso.** Prima del via libera a `bi` su `ABBINATORE_EXPORT_DIR`
(decisione riservata del custode), l'agente confronta i file del 9/11 su
ttadmin.it con l'export generato dal dump. Legge le prime righe del diff,
conta 19 righe cambiate e riferisce che «le 19 righe aggiungono solo
PC 311 W». `bi` rifà il confronto per articolo: 11 righe su 19 aggiungono
anche altri modelli, fino a 27. Il custode sospende il via libera; l'agente
incrocia i 19 articoli col Registro attività e trova per ognuno l'abbinamento
o la copia dell'11/11 coerente; solo allora il via libera parte. Nessun atto
prodotto dall'errore.

**Questione dell'adottante.** «Solo», «tutte», «nessuna» su un confronto
letto a campione sono generalizzazioni: `interpret` potrebbe trattarle come
tratta i «quindi».

**Fatti accanto al caso.**

- [interpret](../kb/interpret.md) cerca già dalla forma «una generalizzazione
  da pochi casi scritti come fatti», ma solo «in ciò che un giro scrive o
  tocca»: task, fili, messaggi di commit. L'affermazione del caso è un
  riferito in chat al custode e a un'altra sessione, fuori da quella
  superficie e fuori da un giro.
- L'intercettazione è venuta da un controllo incrociato di un'altra
  sessione, non da una regola: un caso solo.

## Caso 2: due sessioni Herdr che si aspettano a vicenda

**Il caso.** `bi` invia via Herdr un messaggio all'abbinatore, chiede la
risposta «in fondo al pannello» e resta in `herdr agent wait` sul pannello
dell'abbinatore. L'abbinatore, per non inserirsi a metà del turno di `bi`,
aspetta con `herdr agent wait` che `bi` torni inattivo. Stallo di alcuni
minuti, sciolto dal custode («temo che vi stiate aspettando a vicenda»):
l'abbinatore chiude il turno con la risposta in fondo al proprio pannello,
che `bi` legge. Scartato l'invio comunque: avrebbe accodato il messaggio a un
testo del custode già nel campo di `bi`.

**Questione dell'adottante.** In
[session-messaging](../kb/session-messaging.md): prima di attendere un
destinatario `working`, leggerne il pannello; se aspetta proprio il mittente,
la risposta va lasciata nel proprio pannello e il turno chiuso.

**Fatti accanto al caso.**

- Il protocollo locale di `session-messaging` non nomina il destinatario
  `working`: tratta l'inattivo (`--wait --until working`) e il `blocked`.
  L'attesa dell'inattività è una scelta dell'agente, non una regola scritta.
- La risposta «in fondo al pannello» è già la forma del canale fra host
  («Sessione su un altro host»), dove la sessione remota non può inviare:
  `bi` l'ha usata fra due sessioni locali, e il nodo non dice che vale anche
  lì.
- Primo stallo riportato sul canale: un caso solo.
