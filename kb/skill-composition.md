---
stato: bozza
---

# Skill composition

La KB è orizzontale: i nodi si collegano senza gerarchia. Le skill invece
agiscono, e per ciò che agisce la composizione è naturale: un atto più ampio si
compie coordinando atti più semplici. Il metodo tiene la composizione su due
livelli con due regole, senza imporre i livelli per decreto: un terzo livello
compare solo se una composta compone altre composte, e allora si vede.

## Le tre forme

- skill composta: in elenco, con descrizione; decide quali atti compiere, in
  che ordine e a quali condizioni;
- skill base: compie un atto con il suo contratto, è invocabile anche da sola
  e sta in elenco con una descrizione brevissima;
- ramo: un file nella cartella della composta, letto solo quando il ramo è
  dovuto; non è invocabile e non sta in elenco.

Il ramo è la risposta portabile al costo dell'elenco: nessun harness lo vede
come skill, e ogni harness che legge file lo raggiunge. Una parte che serve
quasi sempre dalla composta è un ramo, non una base. Un harness può offrire di
tenere una base in elenco col solo nome: si usa come ottimizzazione
facoltativa, non come il modo in cui il metodo nasconde le basi (`skill`,
«Indipendenza dall'harness»).

Anche una base può tenere file accanto: è un supporto, la parte del proprio
atto letta solo quando serve, per esempio su un solo scope. Non è un ramo e
non rompe la prima regola, perché non porta un altro atto: resta dentro il
contratto della base, che ne risponde come del suo SKILL.md. Il criterio di
scelta è il contratto, non il file:

- il testo prosegue l'atto della base su una condizione: supporto della base;
- il testo è un atto che serve solo alla composta: ramo della composta;
- il testo è un atto con un contratto proprio, utile da solo o a più
  composte: base.

Una base con supporti condizionali resta base: non diventa una composta di
secondo livello né chiede un terzo livello `cycle → base → supporto`.

## Le due regole

- una base non chiama altre skill: compie il suo atto e restituisce l'esito.
  Può sempre usare strumenti deterministici: il divieto riguarda le skill;
- una composta non contiene procedura di dominio: decide solo ordine,
  condizioni e passaggio degli esiti.

Una composta dichiara nel frontmatter le skill che compone, nel campo
`metadata` della specifica Agent Skills (`compone: eval exec commit`). La
composizione si legge allora senza inferirla dal testo, dove un nome può
comparire anche per escluderlo; il guardiano la segue a cascata e la
confronta con le chiamate scritte in SKILL.md e nei file accanto, segnalando
la composta che chiama skill non dichiarate e la base che chiama altre skill.
Quando una base ha bisogno di un'altra skill non la chiama: restituisce
l'handoff nel proprio esito («l'esito lo segnala per `/exec plan`»), e chi
compone o il custode decide. Le menzioni senza verbo restano candidati da
classificare: descrivono il contratto o sono rinvii da riscrivere come handoff. Un harness che non conosce
il campo lo ignora senza rompere nulla.

Il canone ne è l'istanza. `cycle` è la composta: compone `eval all`,
`exec all` e `commit`, e passa a `commit` gli esiti per stadio che diventano
trailer. `eval` ed `exec` sono basi: chiudono col proprio esito e la proposta
di commit, e il commit lo compie `commit` quando lo chiede il custode o la
composta. `commit` è una base anch'essa, dal working tree a un commit
verificato e pubblicato; il suo nucleo deterministico è uno strumento.

## Argomenti o skill separate

Se i rami condividono la procedura bastano gli argomenti di una skill sola,
come gli stadi di `eval`. Se condividono poco sono basi separate, o rami di
una composta. Una skill che divide per argomento atti con contratti diversi è
un ombrello travestito da atomo: l'asse giusto è l'atto, e l'oggetto su cui
l'atto si compie può essere l'argomento.

## Il costo dell'elenco

Ogni skill in elenco porta la sua descrizione nel contesto di ogni sessione,
anche quando non viene usata (`agent-as-user`). Spezzare una skill riduce
quanto l'agente legge per run; moltiplicare le skill allunga ciò che legge
sempre. L'atomicità si bilancia quindi con descrizioni brevissime e con i
rami, che non costano nulla finché non servono.

## Misura

L'abilità di un artefatto si misura su quanto riesce a isolare nuclei atomici
e semplici che si coordinano verso i goal del dominio. Indicatori osservabili:

- nuclei atomici e loro riuso: una base usata da più composte;
- dinieghi per giro;
- peso medio letto per run;
- quota di righe che sono rimandi a `kb/` e a `o3/`;
- crescita delle copie di una skill canonica rispetto al canone.

Il numero di nuclei non è un obiettivo in sé: si legge insieme al riuso e al
peso, perché più skill costano più elenco.

Connessioni:

- [skill](skill.md)
- [agent-as-user](agent-as-user.md)
- [node](node.md)
- [connection](connection.md)
- [tasks](tasks.md)
