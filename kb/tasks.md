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

`ciclo` vale `dev` o `runtime`. Non esiste `stato`: l'esistenza del file indica
che il task è aperto; priorità e dipendenza vivono nel plan. Il corpo descrive lo
stato corrente del lavoro, non accumula diari di sessione.

Alla chiusura, contenuti stabili e decisioni risalgono nella KB o nei fili; riga,
indice e file vengono rimossi insieme. Prima di eliminare copie operative nel
Mondo si verifica che abbiano perso significato autonomo e che esistano target e
autorità espliciti.

Nel repository `metodo` entrano solo task di custodia del metodo. Le verifiche
puntuali di un adottante nascono nel suo `o2/` e tornano qui soltanto quando
producono una regola portabile.

La skill `exec specify` valuta la qualità interna dei task; `exec plan` ne
controlla presenza, ordine e dipendenze.

Connessioni:

- [plan](plan.md)
- [specify](specify.md)
- [perform](perform.md)
- [verdict](verdict.md)
- [world](world.md)
- [knowledge-base](knowledge-base.md)
