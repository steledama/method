---
stato: maturo
---

# Skill

Una skill è una capacità ricorrente resa invocabile dall'agente. Contiene la
procedura operativa e usa strumenti versionati per le parti deterministiche; non
duplica la conoscenza stabile dei nodi. A differenza di un task, non si consuma
quando viene eseguita.

Le skill canoniche del metodo sono:

- `eval [perceive|interpret|compare|all]`, arco di valutazione;
- `exec [plan|specify|perform|all]`, arco di esecuzione;
- `kb`, diagnosi strutturale e semantica della conoscenza;
- `commit`, gate prima del filing back nella storia;
- `method`, allineamento degli adottanti al canone.

Gli scope-stadio corrispondono agli atomi del ciclo. La procedura completa vive
nelle rispettive `SKILL.md`; il nodo conserva soltanto il modello e i confini.
Dopo un evento del Mondo l'ordine è `eval` → `exec`: prima si aggiorna ciò che è
vero, poi ciò che va fatto. Le supervisioni propongono modifiche a collezioni e
register e attendono conferma del custode.

## Skill di dominio

Una capacità dipendente dal dominio vive nel repository che la usa. Può restare
autonoma oppure diventare scope di `eval` o `exec` quando insiste interamente su
quell'arco. Se l'argomento seleziona rami appartenenti ad archi diversi, resta
autonoma: il nome non deve obbligare il chiamante a dichiarare un arco falso.
Gli scope di dominio non entrano automaticamente nello sweep `all`.

Il nome indica la capacità o l'oggetto mantenuto, non la cadenza. Il ritmo vive
nel plan o in configurazione dichiarativa: una stessa skill può servire più
porzioni di Mondo con battiti diversi, oppure essere attivata da un evento.
Ritmi diversi non bastano a dividere una capacità; procedure o giudizi diversi
sì.

La directory delle skill è l'inventario eseguibile. `CLAUDE.md` ne offre il
router iniziale e i wrapper di altri harness ne assicurano la discovery senza
duplicare la procedura canonica. Ogni skill dichiara scope, limiti,
autorizzazioni ed esito atteso, e preferisce script versionati a logica fragile
riscritta nel prompt.

Connessioni:

- [perceive](perceive.md)
- [interpret](interpret.md)
- [compare](compare.md)
- [plan](plan.md)
- [specify](specify.md)
- [perform](perform.md)
- [goal](goal.md)
- [tasks](tasks.md)
- [kb-tools](kb-tools.md)
- [claude](claude.md)
