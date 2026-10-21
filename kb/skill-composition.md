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

## Le due regole

- una base non chiama altre skill: compie il suo atto e restituisce l'esito.
  Può sempre usare strumenti deterministici: il divieto riguarda le skill;
- una composta non contiene procedura di dominio: decide solo ordine,
  condizioni e passaggio degli esiti.

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
