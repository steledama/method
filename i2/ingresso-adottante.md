---
ciclo: runtime
---

# Entrare nel territorio è un'operazione del metodo

Il 2026-08-12 sono entrati due adottanti opposti. `crm` era un artefatto
fondativo, ancora senza runtime: l'adozione ha preceduto il codice e non ha
richiesto adattamenti. `danea-auto` era invece un artefatto produttivo cresciuto
senza il canone: lo specimen pre-adozione è `fb83c0d`, le automazioni GUI sono
vive su Windows, la conoscenza locale era già sostanziale e alcuni limiti di
verifica runtime non sono superabili dal checkout Linux. L'adozione è stata
fissata nel commit locale `57ef8a6` e il marker è `aligned` a `c6939d6`.

La differenza di dominio non ha cambiato il lavoro nel repository canonico. In
entrambi i casi l'ingresso ha richiesto di ritrovare a mano le rappresentazioni
del territorio: voce e conteggio in `world.md`, bussola e register Goal, nodi che
descrivono il Mondo e gli adottanti, scadenza del battito, filo dell'audit e
viste derivate. Il primo giro su `crm` aveva già misurato **nove file** toccati e
una vista stale; quantità misurata sul diff `b9d01b5`. Il secondo giro conferma
la dispersione ma aggiunge il bisogno di distinguere tre fotografie:

- l'inventario corrente del metodo, che passa a sei adottanti;
- la baseline locale dell'adottante, che per `danea-auto` conserva divergenze
  intenzionali e limiti di verifica live;
- le fotografie storiche, i cui conteggi a quattro o cinque non vanno riscritti.

Il pattern non è quindi «aggiungere una riga». È un'operazione di ammissione
che attraversa register, sintesi e ciclo, e deve preservare la provenienza dei
conteggi. Una checklist meccanica può trovare occorrenze e rigenerare viste, ma
non può decidere se un numero è corrente o storico, né quali differenze locali
siano adattamenti legittimi. Il protocollo deve perciò restare leggero e
supervisionato: inventario deterministico, giudizio esplicito sulle fotografie,
marker verificato e baseline rinviata al primo `/adottanti` quando manca un
giro comparabile.

## Collaudo prospettico: `baserow`

Il protocollo è poi diventato la prescrizione `o3/ingresso-adottante.md`, e
il terzo ingresso, `baserow` il 2026-10-05, è stato il primo fuori dai due
casi che l'avevano generata. Ha retto: il task di ingresso ha classificato
in anticipo i candidati in inventario corrente, baseline e fotografie da
preservare, e l'ingresso è partito solo quando il marker locale era
`aligned`. Ha richiesto una sola correzione, che ora sta nella prescrizione
(`f44b6c0`): la scelta di un accento delle viste non confondibile con quelli
già registrati, nata da un primo colore troppo vicino a quello di `salute`.
La prima verifica nell'uso è il battito `/adottanti` del 2026-11-01.

## Materiale verificato

- `metodo` commit `b9d01b5`, ingresso di `crm` e relativa cattura i1;
- `danea-auto` commit `57ef8a6`, marker `i3/allineamento-metodo.md`, register,
  plan e catalogo locali;
- `metodo` a `c6939d6`, inclusi `world.md`, `goal.md`, `adopter-comparison`,
  `audit-adottanti` e la scadenza del battito.

Non sono stati verificati il runtime Windows, Task Scheduler, Danea,
LibreOffice, backup o Google Drive: sono limiti della baseline locale, non del
fatto metodologico qui interpretato.
