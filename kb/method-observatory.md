---
stato: maturo
---

# Method observatory

Il repo metodo non è solo una libreria di nodi portabili: è il punto di
osservazione da cui il metodo viene riletto mentre viene applicato nei progetti
adottanti. La sua funzione meta-cognitiva è raccogliere differenze, convergenze,
attriti e drift tra le implementazioni reali, trasformandoli in conoscenza
metodologica stabile quando il pattern è portabile, o lasciandoli come lavoro
locale quando appartengono al dominio.

Il metodo nasce e si verifica nei progetti concreti. Gli adottanti non sono solo
consumatori del metodo: sono casi sperimentali con vincoli diversi, ed è la
diversità dei vincoli a farne materiale di analisi. Un progetto code-based
espone problemi di fedeltà tecnica e copertura del codice; un progetto ad alta
responsabilità espone problemi di fonti autoritative e dati sensibili; un
progetto riflessivo espone problemi di hub semantici, accessi cognitivi e filing
back; un progetto che pilota software di terzi espone i limiti di un Mondo che
non si lascia interrogare a piacere. L'osservatorio serve a rendere queste
differenze comparabili senza appiattirle; chi sia in territorio in un dato
momento vive nel register `world.md`.

La direzione che l'osservatorio governa è il movimento dal basso (uno dei due di
`method-development`, e quello che protegge dal generalizzare per esigenze
immaginate). Si parte da un'esigenza concreta in un repo adottante, si risolve
lì nel merito, poi si chiede se la soluzione locale contiene una regola
generale. Solo a quel punto il repo adottante modifica `metodo` o produce un
commit nel metodo con la generalizzazione. Gli altri adottanti recepiscono il
canone e le sue eventuali prescrizioni applicando localmente ciò che è
pertinente; `metodo` non apre né ordina i task delle loro code. Il movimento
dall'alto — importare una cornice teorica e verificarla contro i domini reali —
non passa da questo flusso: non genera task negli adottanti, ma rilegge
l'insieme dei loro componenti per nominare ciò che il confronto fa affiorare.

L'unità di analisi non è solo il nodo KB. Vanno confrontati tutti i componenti
della ricetta metodologica:

- README: funzione di bussola (orienta e punta, non immagazzina), qualità dei
  router, puntatori al cruscotto (plan, catalogo, modello, indice-di-dominio
  dove esiste)
- CLAUDE.md e AGENTS.md: chiarezza operativa, separazione tra regole d'azione e
  contenuto di dominio, costo di caricamento
- fili `i3/`: qualità della memoria interpretativa, granularità delle decisioni,
  rapporto con git
- `o1/plan.md` + `o2/`: corrispondenza tra supervisione e dettagli, qualità del
  contesto operativo, presenza di task morti
- nodi KB: quantità, cluster, hub, orfani, formato, link, copertura delle aree
  reali, equilibrio tra mappa, concetto, reference e runbook
- strumenti: comandi comuni, estensioni locali, dipendenze, output
  ricostruibili, confine tra audit strutturale e fedeltà cognitiva
- skill: workflow ricorrenti, differenze locali, duplicazioni, possibilità di
  template o wrapper comuni
- fonti di verità: codice, JSON, documenti autoritativi, mappe, output
  strutturati e dati locali

Il confronto deve produrre quattro tipi di esito:

- generalizzazione metodologica: una differenza locale rivela una regola
  portabile e viene integrata nei nodi di metodo
- estensione strumentale: una duplicazione stabile diventa script, comando,
  skill base o template riusabile
- task locale: un problema resta lavoro autonomo di dominio e va tracciato in
  `o1/plan.md`/`o2/` del repo interessato
- manutenzione propria del metodo: una generalizzazione già emersa richiede
  ristrutturazione, semplificazione, rinomina, documentazione o strumenti
  portabili nel repo `metodo`

La distinzione è cruciale. Il repo metodo non deve diventare un contenitore di
problemi altrui né un orchestratore centralizzato che toglie autonomia ai
progetti. Deve invece funzionare come osservatorio: raccoglie segnali,
interpreta pattern e custodisce generalizzazioni. Le verifiche operative restano
nei repo dove nascono, perché lì vivono fonti, priorità, dipendenze e criteri di
chiusura.

Analisi periodiche:

- inventario componenti: presenza e forma di README, CLAUDE, AGENTS, map,
  `o1/plan.md`, fili `i3/`, `o2/`, strumenti, skill, nodi metodo e nodi dominio
- confronto strumenti: sottocomandi comuni, comandi locali, dipendenze, output,
  compatibilità della superficie base
- confronto skill: scopo, istruzioni, path, formatter, relazione con script
  versionati
- confronto KB: numero nodi, link, orfani, hub, cluster, tipi documentali, nodi
  non indicizzati, accessi cognitivi
- confronto fedeltà: fonti di verità disponibili, fatti verificabili, aree
  scoperte, segnali anti-drift
- confronto operativo: task aperti, voci verdict significative, problemi
  ricorrenti e interventi rimandati ai repo locali

## Protocollo d'ingresso di un adottante

Ammettere un progetto nel territorio è un'operazione dell'osservatorio, non
soltanto l'aggiunta di una voce a `world.md`. Il protocollo resta una checklist
qui, senza skill autonoma: ingressi ripetuti hanno giustificato una forma
stabile, non ancora una nuova automazione.

### 1. Verifica l'adozione locale

- identifica il commit esatto dell'adottante e conserva l'eventuale specimen
  pre-adozione;
- verifica il symlink `method/`, i register `goal.md` e `world.md`, la sezione
  README canonica e il marker `i3/allineamento-metodo.md`;
- leggi dal marker adattamenti intenzionali, limiti di verifica e commit di
  `method` recepito: `aligned` certifica l'allineamento documentale dichiarato,
  non il runtime esterno;
- non correggere la coda locale: task, gradualità e priorità restano
  giurisdizione dell'adottante.

### 2. Fissa una baseline con provenienza

- conta soltanto ciò che la superficie permette di misurare e dichiara il
  metodo: audit, query o conteggio manuale;
- registra almeno nodi KB, sintesi i2, fili i3, task e skill locali quando
  esistono; una quantità manuale non si somma retroattivamente a serie prodotte
  da un audit diverso;
- separa i limiti del checkout dai limiti del sistema vivo: assenza di accesso a
  host, scheduler, servizi o backup resta esplicita e non diventa una
  certificazione negativa;
- se manca storia comparabile, la baseline fondativa sostituisce il delta e il
  primo `/adottanti` valuta se la struttura regge all'uso reale.

### 3. Aggiorna solo le rappresentazioni correnti

- registra nome, profilo e superficie nel register `world.md`;
- cerca nel repository le enumerazioni e i conteggi correnti degli adottanti
  (`rg` propone candidati, non decide): bussola e regole operative, `goal.md`,
  nodi dell'osservatorio e del Mondo, indice/verdetto dell'audit e scadenza del
  prossimo battito;
- classifica ogni occorrenza prima di modificarla: **inventario corrente** da
  aggiornare, **baseline locale** da aggiungere con provenienza, oppure
  **fotografia storica datata** da preservare nel numero e nel perimetro
  originari;
- non riscrivere una fotografia vera soltanto perché contiene «quattro» o
  «cinque»: aggiungi invece la nota che colloca il nuovo ingresso fuori giro.

### 4. Predisponi il primo giro

- aggiungi l'adottante alla prossima finestra `/adottanti` e dichiara quale
  segnale costituirà la sua prima verifica;
- aggiorna il filo `i3/audit-adottanti.md` senza anticipare il cursore mensile:
  l'ingresso è un evento fuori giro, non un audit aggiuntivo;
- rigenera le viste con `o3/build-presentation.sh` e `o3/build-system-image.sh`;
  ciò che cambia era una rappresentazione derivata, non una fonte da correggere
  a mano;
- chiudi con `o3/kb_tools.py audit`, `git diff --check` e una ricerca finale dei
  candidati classificati, dichiarando quelli storici lasciati intenzionalmente
  invariati.

La forma ideale è un ciclo leggero:

1. partire da un problema concreto in un repo adottante
2. risolvere il problema nel merito, con task, verdict e nodi locali
3. distinguere cosa è specifico del dominio da cosa è portabile
4. aggiornare `metodo` solo con la generalizzazione o con uno strumento comune
   già giustificato dall'uso
5. propagare agli altri repo tramite lettura dei commit di `metodo`, non tramite
   task centrali prescrittivi
6. ripetere quando nuovi casi reali confermano, correggono o limitano la
   generalizzazione

Questo ciclo rende il repo metodo un meta-strumento di cognizione sulla
cognizione: non solo documenta come pensare con una KB, ma osserva come le KB
reali evolvono, dove falliscono, dove divergono e quali forme si dimostrano più
robuste.

Le fotografie e le baseline prodotte da questo ciclo appartengono a `i2/`; il
verdetto aggregato corrente appartiene a `i3/`. Il nodo conserva il protocollo,
non i risultati datati né le azioni suggerite ai singoli adottanti.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [method-development](method-development.md)
- [kb-tools](kb-tools.md)
- [project-structure](project-structure.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [knowledge-base](knowledge-base.md)
- [readme](readme.md)
- [claude](claude.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [source-of-truth](source-of-truth.md)
