---
ciclo: runtime
---

# Revisione coordinata del bootstrap di un adottante

Prescrizione da eseguire nel singolo repository tramite `/method`. Non impone
un template e non autorizza `metodo` a scrivere nel repo adottante: porta il
contratto comune fino al confine e lascia al dominio l'ultimo miglio.

## Perimetro

Leggere insieme, nell'ordine di bootstrap effettivo:

1. `README.md`;
2. `CLAUDE.md`;
3. intro e articolazione di `goal.md`;
4. intro e articolazione di `world.md`;
5. nodo canonico `method/world.md` e gli altri nodi metodologici collegati
   intenzionalmente dai quattro file.

Usare come materiale comparativo `method/../i2/bootstrap-adottanti.md` quando
il checkout consente di raggiungerlo; le osservazioni per-repo sono indizi da
verificare sullo stato locale, non ordini testuali.

## Contratto comune

### README — orienta

- identità e scopo sono comprensibili senza aprire altri file;
- il primo contenuto sostanziale rende Mondo, poste e percorsi nel linguaggio
  del dominio;
- Goal, World, cruscotto, catalogo e regole operative sono raggiungibili;
- la sezione `## Metodo` dichiara una volta dipendenza, symlink, hub stabile e
  register dei poli;
- teoria estesa, inventario completo, procedure e troubleshooting non
  competono con la funzione di bussola.

### CLAUDE — istruisce

- contiene ciò che deve essere presente **prima dell'azione**: autorizzazioni,
  vincoli, pericoli, ambiente e convenzioni operative;
- sposta nei nodi reference, razionali e conoscenza consultabile on-demand;
- non ricostruisce il catalogo del metodo né duplica estesamente il README;
- conserva guardrail ad alta posta anche quando rendono il file più lungo.

### Goal — rende il nord

- l'intro dall'H1 al primo H2 è la visione della direzione, non una spiegazione
  del register o del ciclo;
- obiettivi, segnali e lavoro corrente concordano col README e col plan;
- la compressione dell'intro non cancella tensioni costitutive del dominio.

### World — rende il territorio

- l'intro dall'H1 al primo H2 dice di che cosa è fatto il Mondo rilevante;
- superfici, fonti, pipeline e dettaglio territoriale vivono nelle sezioni
  on-demand;
- entità e assi concordano col Goal e con il dominio presentato nel README;
- `world.md` locale applica il nodo canonico `method/world.md`, non lo duplica.

## Controllo trasversale

Verificare esplicitamente:

- contraddizioni fra identità, assi, stato, Goal e World;
- lo stesso dettaglio ripetuto in più file senza lettori distinti;
- contenuto rimosso dal README ma riversato senza criterio in CLAUDE;
- link interni al metodo privi di una dipendenza semantica o operativa locale;
- intro dei register che la home amplificherebbe come metadocumentazione o
  modello eccessivamente esteso.

## Esito locale

Applicare soltanto le modifiche giustificate dal dominio. Nel marker
`i3/allineamento-metodo.md` registrare:

- file revisionati e commit del canone usato;
- modifiche applicate;
- differenze conservate con motivazione di dominio;
- eventuali tensioni nuove da far risalire come segnale i1 a `metodo`.

Rigenerare e verificare la home se rende le intro di Goal e World. Un esito
senza modifiche è legittimo quando il quartetto soddisfa già il contratto.
