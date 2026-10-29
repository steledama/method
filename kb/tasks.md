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
l'artefatto o porta a termine un affare del dominio, e chiede decisioni,
approfondimenti o chiarimenti che si prendono col custode.

Il giro senza custode pianifica i task ma non li esegue. Una notizia nuova, come
una risposta, un dato o un verdetto, si traduce nella pianificazione: il giro
corregge un'informazione del task, ne aggiorna la specifica, ne cambia priorità
e dipendenze, chiude un'attesa o un task consumato, ne crea uno nuovo o ne
cancella uno superato. Se arriva per mail la risposta del notaio sulla vendita
di un immobile, il giro aggiorna la specifica del task di vendita e chiude
l'attesa, ma non risponde al notaio. L'implementazione, lo sviluppo e gli atti
sul Mondo che il task prepara restano alla sessione col custode, salvo quelli
che il register di autonomia assegna al giro.

A muovere la pianificazione è un verdetto che una notizia ha mosso
(`action-cycle`, «Risalire prima di scendere»). Un plan fermo senza notizie nuove è
l'equilibrio, non una lacuna. Un'osservazione che il dato del dominio conserva
già non è una notizia da annotare nel task (`source-of-truth`,
`pace-layering`). Una scelta che spetta al custode nasce nel task col campo
`decidere:`.

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
- [action-cycle](action-cycle.md)
