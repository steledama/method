---
data: 2026-10-11
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Nella sessione interattiva il momento del commit si concorda

## Cosa e perché

Il custode ha deciso il 2026-10-11: **nella sessione interattiva il
momento del commit si concorda**. Con commit e push delegati, l'agente
tendeva a committare a ogni passaggio, mentre il custode stava ancora
discutendo decisioni aperte ad aggiustamenti, affinamenti e ripensamenti. Il
commit fissa una fotografia; presa troppo presto, a storia pubblicata ogni
ritocco diventa un altro commit. In `metodo` lo mostra la sessione del
2026-10-10/11: una proposta committata e superata venti minuti dopo, e un
commit vuoto per correggere il trailer di quello precedente.

La regola, in [consent](../kb/consent.md) e nel criterio
`momento-del-commit` di [`autonomy.md`](../autonomy.md):

- l'agente propone il commit quando un punto si è fermato;
- lo fa di propria iniziativa, dichiarandolo, solo se un lettore fuori dalla
  sessione ne ha bisogno, come un adottante che recepisce o un'altra
  sessione;
- il ciclo chiesto esplicitamente fino al commit lo include, gli scambi
  successivi no;
- il giro senza custode chiude col proprio commit;
- il push resta una conseguenza del commit, senza conferma.

Il contenuto resta delegato come prima: cambia solo chi sceglie il
momento.

## Ricetta per il /method locale

1. In `autonomy.md`, accanto a `ciclo-delegato`, aggiungere il criterio
   `momento-del-commit` con la data della decisione del custode locale.
2. Nei fork di `eval` ed `exec`, nel gate di chiusura, aggiungere che nella
   sessione interattiva il momento del commit si concorda: il ciclo chiesto
   fino al commit lo include, gli scambi successivi no.
3. **Residui di dominio**: le skill di dominio che committano da sole
   (giri schedulati, registri skill-owned, esecutori che fissano un esito)
   non sono sessioni interattive di discussione. Il custode decide se
   restano fuori dal criterio; la decisione si scrive in `autonomy.md`.
4. Registrare nel marker il recepimento o l'adattamento motivato.

## Indizi da verificare sul posto

Lettura del 2026-10-11 dai file su `origin`:

- **economia**, **crm**: `autonomy.md` dice «chiusura con commit e push»
  dentro `ciclo-delegato`; il criterio nuovo si aggiunge lì accanto.
- **nixos**, **bi**, **economia**, **salute**: i fork di `eval` ed `exec`
  portano la frase canonica «Chiudere gli scope richiesti con i controlli e
  `/commit`», dove si aggiunge la precisazione.
- **crm**, **danea-auto**, **baserow**: la frase non compare nei fork con
  la stessa forma; cercare dove i fork chiudono il giro.
- **nixos**: `/manutenzione` committa e pusha da sola con un lock fra gli
  host; è il caso tipico del passo 3.
- **bi**: `categorizzazione`, `corrispondenze` e `ordini` hanno scritture
  delegate; verificare se committano da sole.
