---
ciclo: runtime
---

# Segnale: le verifiche differite di `bi`, ipotesi in attesa nate in sessione

Data: 2026-10-23 · Fonte: inoltro della sessione `bi` via Herdr, su richiesta
del custode; `bi` `3177d46b` e `b8ef7257` letti su `origin`

## Il segnale

In sessione col custode `bi` corregge un difetto: i prodotti Danea fuori XML
perdevano la quantità in arrivo sul sito (`3177d46b`). Sistema anche due SKU
nei dati. L'esito si vede solo il mattino dopo, con il notturno, il push del
catalogo delle 06:30 e l'audit post-push. A quell'ora la sessione è chiusa e
lavora il giro autonomo delle 07:30. Il custode voleva un posto dove lasciare
al giro le verifiche nate in sessione.

`bi` non aggiunge nulla a prompt, skill o permessi. Crea
`i2/verifiche-differite.md`, indicizzato in `i2/interpretations.md`, che
`eval` raggiunge già dall'indice i2 al passo delle ipotesi in attesa
(`b8ef7257`). Ogni voce ha questo contratto:

- **Attesa**: l'affermazione, con l'origine (sessione, commit);
- **Da**: la data dalla quale il riscontro esiste; prima non si valuta;
- **Riscontro**: comandi eseguibili dal giro autonomo dentro la sua
  allowlist, uno per chiamata;
- **Conferma** e **smentita**;
- **Se smentita**: dove va il seguito (task `o2/`, proposta, riga
  `Attenzione:`).

Il giro che valuta una voce ne riporta l'esito nel resoconto e la toglie: la
storia resta in git. Una voce scaduta da più di tre giorni senza riscontro va
nella riga `Attenzione:`. La prima voce vale dal 2026-10-24: `qtaArrivo` nel
backorder per i prodotti collegati a Danea e drift chiuso su
`meta._quantita_in_arrivo` di `1001124` e `1012175`.

## La lettura dell'adottante

Giudizio del custode, riferito dalla sessione `bi`: è un buon contributo.
È la prima volta che i2 ospita qualcosa con una funzione operativa chiara e
ricorrente, mentre lo stadio fatica ancora a trovare il suo ruolo. Una
verifica differita è l'ipotesi in attesa di [interpret](../kb/interpret.md)
(attesa sul futuro, orizzonte, riscontro con fonte, cosa la smentirebbe), ma
nata in sessione e di vita breve. Fa da ponte fra la sessione col custode e
il ciclo autonomo: la sessione forma l'ipotesi, il giro la verifica e la
chiude.

## La prova in corso

Il giro di `bi` del 2026-10-24 riceve la voce solo attraverso il contratto
esistente di `eval`, senza istruzioni aggiunte al prompt del ciclo.

- Se la raggiunge e la chiude da solo, basta nominare il caso nel metodo.
- Se la ignora, serve un aggancio esplicito in `eval` o in `/cycle`.

L'esito sarà nel resoconto e nel commit del giro di `bi`, e la sessione `bi`
lo inoltrerà. In mancanza dell'inoltro, il riscontro sta nel commit di giro
di `bi` del 24/10: trailer `Esiti:` e diff di `i2/verifiche-differite.md`.
È la misura che [presidio-ipotesi-adottanti](../i2/presidio-ipotesi-adottanti.md)
lasciava aperta: il caso di `danea-auto` provava che un giro fa emergere
un'ipotesi già scritta con data e criterio, non che un giro ne riconosca una
non dichiarata. Qui l'ipotesi è dichiarata, ma in un contenitore nuovo che
nessuna istruzione nomina.

## Le domande dell'adottante

Non sono richieste di modifica immediata.

1. Nominare in `kb/interpret.md`, e forse nei passi perceive e interpret di
   `eval`, la verifica differita come specie di ipotesi in attesa, con il
   contratto minimo sopra.
2. Presidio come file agenda unico per adottante (la scelta di `bi`: facile
   da riempire per la sessione e da svuotare per il giro), o come voce nella
   sintesi i2 pertinente.
3. Se `/cycle` e il suo resoconto debbano dichiarare le verifiche differite
   valutate (oggi lo chiede solo il file).
4. La relazione con `## Scadenze` del plan, che segna un orologio nostro e
   quindi la condizione di risveglio di un `pause`, per non avere due
   agende.

Un solo adottante, una sola voce. Accanto c'è il caso `bi` del 19–20/10, in
[giri-ipotesi-implicite](giri-ipotesi-implicite-e-prossimo-task-2026-10-20.md):
una tesi causale nata e caduta in due giri con `interpret=vuoto`, cioè
un'ipotesi rimasta senza contenitore.
