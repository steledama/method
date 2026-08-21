---
stato: maturo
---

# Verdict

I file in `i3/` conservano il verdetto attuale sulle tensioni aperte rispetto ai
goal. Sono il residuo dello stadio Compare: `i3/verdicts.md` li indicizza come il
plan indicizza il lavoro futuro.

Un filo descrive come stanno le cose ora e perché conta. Si aggiorna in place;
non accumula cronache, report rigenerabili o task. Quando il giudizio è stabile e
non resta tensione, file e voce d'indice vengono rimossi: la storia resta in Git.
Ogni voce dell'indice dichiara con `misura:` quale obiettivo osserva.

Il verdetto non può essere più sicuro del materiale:

- una quantità rilevante dichiara se è misurata, dichiarata da terzi o derivata;
- una quantità derivata non regge da sola una conclusione;
- il materiale prodotto dal progetto — soprattutto il task `o2/`, la
  corrispondenza in uscita e le valutazioni delle fonti — viene letto prima di
  costruire una sintesi più elegante ma meno vera;
- fatti verificabili rimandano a fonti primarie.

Ogni filo tratta una sola tensione e ha frontmatter `ciclo: dev|runtime`. Un
cambio di verdetto può modificare priorità o task, oppure proporre una revisione
del Goal; la propagazione è esplicita, non incorporata nel filo.

La skill `eval compare` rivede periodicamente fili, segnali e copertura dei goal.
Il gate `commit` verifica invece se la singola modifica corrente richiede di
aggiornare un verdetto.

Connessioni:

- [compare](compare.md)
- [goal](goal.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [source-of-truth](source-of-truth.md)
- [git-history](git-history.md)
