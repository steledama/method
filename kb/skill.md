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
- `kb [audit|review]`, diagnosi strutturale rapida o revisione semantica
  profonda della conoscenza;
- `commit`, gate prima del filing back nella storia;
- `cycle [autonomo]`, il ciclo congiunto `eval all` → `exec all` → `commit`:
  compone gli archi senza fonderli, in sessione o come ciclo autonomo senza
  custode;
- `method`, allineamento degli adottanti al canone.

## Atomicità: un atto, un contratto

Come un nodo contiene un'idea, una skill compie un atto con un contratto:
input chiaro, esito dichiarato, strumenti di `o3/` sotto per le parti
deterministiche, KB come riferimento. Le skill si compongono in due livelli,
base e composta, e i rami di una composta vivono come file nella sua cartella
(`skill-composition`).

Una skill è una selezione della KB guidata dallo scopo: `kb/kb.md` è l'indice
globale, la skill un indice parziale orientato a un atto. Nella skill restano
obiettivi, vincoli, sequenza, punti di decisione e forma dell'esito; il resto
vive nei nodi, nei register e negli strumenti, e la skill vi rimanda. Il
rimando è condizionale, legato al punto in cui serve («se è dovuto il ramo X,
leggi il nodo Y nella sezione Z»): una lista di letture fisse a ogni run
costerebbe più del testo che sostituisce (`agent-as-user`). Una skill
cresciuta si estrae prima di dividerla: ciò che non è procedura va verso
`kb/`, i register e gli script, e spesso il resto sta in un nucleo breve che
non chiede più divisione.

## Indipendenza dall'harness

Il contenuto di una skill vive in file neutri, markdown leggibile da qualunque
agente; gli harness vi si legano con adattatori sottili e sostituibili. Le
skill seguono la forma condivisa di più harness: una cartella con `SKILL.md`,
`name` e `description` nel frontmatter, file di supporto accanto. Un'opzione
propria di un harness si usa solo come ottimizzazione e la sua assenza non
deve rompere nulla: la struttura funziona anche con un harness che sa solo
leggere file. Legare il metodo a un harness è lock-in, e vale anche per i nomi:
un nome generico può collidere domani con un comando integrato.

## Skill canoniche e stadi

Gli scope-stadio corrispondono agli atomi del ciclo. La procedura completa vive
nelle rispettive `SKILL.md`; il nodo conserva soltanto il modello e i confini.
Dopo un evento del Mondo l'ordine è `eval` → `exec`: prima si aggiorna ciò che è
vero, poi ciò che va fatto. Le supervisioni propongono modifiche a collezioni e
register e attendono conferma del custode.

Ogni stadio di un arco chiude con un esito esplicito, e la chiusura vuota è
legittima. L'esito resta però nella storia: il giro si chiude con un commit che
porta una parola per stadio, `materia` o `vuoto`, anche quando non ha cambiato
file. Senza questa traccia una chiusura vuota non si distingue da uno stadio mai
invocato, e il giudizio sulla divisione in stadi perde la sua sola misura.

Il giro che passa da `exec plan` lascia nello stesso commit anche il suo
punto d'arrivo: il **prossimo task**, confermato o cambiato rispetto a quello
precedente (trailer `Prossimo:`). È lo sbocco della catena del ciclo, nuove
percezioni → interpretazioni → verdetto contro il Goal → dipendenze e
priorità, e la rende verificabile: una conferma è un atto registrato, non un
silenzio, e un cambio di priorità si vede confrontando due giri senza
dipendere dal giudizio dell'agente. `plan=vuoto` con `Prossimo: … (confermato)`
dice che la coda è stata riesaminata e regge.

## Skill di dominio

Una capacità dipendente dal dominio vive nel repository che la usa. Può restare
autonoma oppure diventare scope di `eval` o `exec` quando insiste interamente su
quell'arco. Se l'argomento seleziona rami appartenenti ad archi diversi, resta
autonoma: il nome non deve obbligare il chiamante a dichiarare un arco falso.
Gli scope di dominio non entrano automaticamente nello sweep `all`.

Il nome indica la capacità o l'oggetto mantenuto, non la cadenza. Il ritmo vive
nel plan o in configurazione dichiarativa: una stessa skill può servire più
porzioni di Mondo con cadenze diverse, oppure essere attivata da un evento.
Ritmi diversi non bastano a dividere una capacità; procedure o giudizi diversi
sì.

La directory delle skill è l'inventario eseguibile. `CLAUDE.md` ne offre il
router iniziale e i wrapper di altri harness ne assicurano la discovery senza
duplicare la procedura canonica. Vale per ogni file letto da un harness: è un
binding verso il contenuto, che vive versionato nello stadio che gli spetta
(cfr. `claude`, «File dell'harness»). Ogni skill dichiara scope, limiti,
autorizzazioni ed esito atteso, e preferisce script versionati a logica fragile
riscritta nel prompt.

L'agente rilegge la skill a ogni invocazione e non ricorda la precedente: la
lunghezza è un costo ricorrente, e un nucleo breve con rami letti solo quando
dovuti è la forma adatta. Ogni gesto che la skill richiede deve essere concesso
nel contesto in cui gira; un gesto negato si chiude sul permesso o sullo
strumento, non con un'istruzione che chiede all'agente di adattarsi
(`agent-as-user`).

Una skill portabile può separare protocollo comune e profilo locale. Il primo
definisce procedura, evidenza richiesta e forma dell'esito; il secondo dichiara
fonti, controlli, convenzioni e prove proprie del dominio. Anche il repository
canonico ha un dominio: il suo profilo non diventa implicitamente universale.
I fork restano versionati e si allineano con `method`, confrontando il
protocollo senza sovrascrivere il profilo locale. I criteri concettuali restano
nei nodi, senza essere trasformati in una seconda procedura.

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
- [skill-composition](skill-composition.md)
- [agent-as-user](agent-as-user.md)
