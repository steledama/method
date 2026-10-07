---
stato: maturo
---

# Verdict

I file in `i3/` conservano il verdetto attuale sulle tensioni aperte rispetto ai
goal. Sono il residuo dello stadio Compare: `i3/verdicts.md` li indicizza come
il plan indicizza il lavoro futuro.

Un filo descrive come stanno le cose ora e perché conta. Si aggiorna in place;
non accumula cronache, report rigenerabili o task. Quando il giudizio è stabile
e non resta tensione, file e voce d'indice vengono rimossi solo se non hanno
altre funzioni vive: la storia resta in Git. Un file che custodisce anche un
cursore o un contratto corrente, come `i3/allineamento-metodo.md` negli
adottanti, resta necessario anche con stato `aligned`: si aggiorna il verdetto
senza eliminare il cursore che servirà alla prossima revisione.

Anche un'ipotesi in attesa è una funzione viva: dichiara orizzonte e riscontro
con fonte ed è raggiungibile da `eval` (cfr. `interpret`). Un filo
con criterio, conteggio e data può già presidiarla. Prima di rimuoverlo,
conservare quel presidio in una destinazione esplicita e raggiungibile.
La chiusura operativa non conferma da sola una spiegazione.

Il verdetto non può essere più sicuro del materiale:

- una quantità rilevante dichiara se è misurata, dichiarata da terzi o derivata;
- una quantità derivata non regge da sola una conclusione;
- il materiale prodotto dal progetto — soprattutto il task `o2/`, la
  corrispondenza in uscita e le valutazioni delle fonti — viene letto prima di
  costruire una sintesi più elegante ma meno vera;
- fatti verificabili rimandano a fonti primarie.

## Che cosa è un filo

Compare confronta l'interpretazione con lo scopo: un filo che non dice contro
quale obiettivo si misura non confronta niente. Un file resta in `i3/` solo se
ha tre cose:

- una **tensione aperta**, non una decisione già incisa;
- un **obiettivo** di `goal.md` contro cui la tensione si misura, dichiarato
  nel frontmatter con la sua chiave (`obiettivo: 1`, `S`, più chiavi separate
  da virgola) al livello dell'obiettivo, non del suo indicatore;
- una **condizione di chiusura** che il ciclo può vedere arrivare: una data, un
  battito, un dato che qualcuno raccoglie.

Ciò che non ha le tre cose non è un verdetto, e va dove il suo genere vive:

- la motivazione di una decisione ormai stabile va nel nodo che porta la regola
  e nel messaggio del commit; il filo si chiude;
- un'ipotesi incisa che attende l'uso può restare nel nodo o nella lettura
  pertinente, con orizzonte, riscontro con fonte e raggiungibilità da `eval`:
  il solo `stato: bozza` non ne presidia il riesame;
- il seguito di una prescrizione negli adottanti lo misura l'audit periodico;
- una decisione ancora da prendere è un task.

La **provenienza** del segnale da cui un filo nasce non è il suo obiettivo: un
filo nato da una percezione non misura per questo il canale delle percezioni.
La chiave si verifica contro il register come la colonna `Ob.` del plan, e una
chiave vuota o assente rompe la build della vista.

Ogni filo tratta una sola tensione e ha frontmatter `ciclo: dev|runtime` e
`obiettivo:`. Un cambio di verdetto può modificare priorità o task, oppure proporre una revisione
del Goal; la propagazione è esplicita, non incorporata nel filo.

La skill `eval compare` rivede periodicamente fili, segnali e copertura dei
goal. Il gate `commit` verifica invece se la singola modifica corrente richiede
di aggiornare un verdetto.

Connessioni:

- [compare](compare.md)
- [interpret](interpret.md)
- [goal](goal.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [source-of-truth](source-of-truth.md)
- [git-history](git-history.md)
