---
stato: maturo
---

# Tasks

`o2/` contiene la specifica dei task aperti che richiedono più contesto della
riga in `o1/plan.md`. Il plan decide cosa viene prima; il file del task rende
visibili risultato atteso, risorse reali, vincoli e verifica di riuscita. È
memoria operativa temporanea, non conoscenza permanente.

Ogni file ha una riga nel plan e una voce nell'unico indice `o2/tasks.md`. Il
generatore verifica questa corrispondenza. Il frontmatter minimo è:

```yaml
---
sintesi: "Risultato atteso in una frase."
ciclo: dev
---
```

`ciclo` vale `dev` o `runtime`. Un task con una proposta in attesa del
custode aggiunge `decidere: "La questione in una frase."`; il campo si toglie
quando il custode decide, e la home della vista elenca i task che lo hanno
(`kb/view.md`). Non esiste `stato`: l'esistenza del file indica
che il task è aperto; priorità e dipendenza vivono nel plan. Il corpo descrive
lo stato corrente del lavoro, non accumula diari di sessione.

Alla chiusura, contenuti stabili e decisioni risalgono nella KB o nei fili;
riga, indice e file vengono rimossi insieme. Prima di eliminare copie operative
nel Mondo si verifica che abbiano perso significato autonomo e che esistano
target e autorità espliciti.

Nel repository `metodo` entrano solo task di custodia del metodo. Le verifiche
puntuali di un adottante nascono nel suo `o2/` e tornano qui soltanto quando
producono una regola portabile.

La skill `exec specify` valuta la qualità interna dei task; `exec plan` ne
controlla presenza, ordine e dipendenze.

## Task e giro

Il giro ricorrente amministra l'artefatto: esegue il runtime, smaltisce le code
ricorrenti del dominio, percepisce e dà i verdetti. Ciò che si ripete
appartiene al giro, non a un task. Il task è straordinario: una tantum, migliora
l'artefatto e chiede decisioni, approfondimenti o chiarimenti che si prendono
col custode. Per questo il giro senza custode non porta avanti i task, nemmeno
specificandoli; il suo `exec specify` resta igiene della forma.

I due movimenti si toccano in due punti: un verdetto sugli input che cambia la
priorità della coda, e un'evidenza del giro, dall'autoanalisi o dai dati della
giornata, che basta a proporre o a cancellare un task. La proposta nasce col
campo `decidere:`. Le singole osservazioni non si accumulano nel task quando il
dato del dominio le conserva già (`source-of-truth`, `pace-layering`).
Un adottante che vuole una delega più larga la dichiara nel proprio register
di autonomia.

Connessioni:

- [plan](plan.md)
- [specify](specify.md)
- [perform](perform.md)
- [verdict](verdict.md)
- [world](world.md)
- [knowledge-base](knowledge-base.md)
- [view](view.md)
- [source-of-truth](source-of-truth.md)
- [pace-layering](pace-layering.md)
