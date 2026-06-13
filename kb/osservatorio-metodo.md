---
data: 2026-05-23
stato: maturo
---

# Osservatorio metodo

Il repo metodo non è solo una libreria di nodi portabili: è il punto di osservazione da cui il metodo viene riletto mentre viene applicato nei progetti adottanti. La sua funzione meta-cognitiva è raccogliere differenze, convergenze, attriti e drift tra le implementazioni reali, trasformandoli in conoscenza metodologica stabile quando il pattern è portabile, o lasciandoli come lavoro locale quando appartengono al dominio.

Il metodo nasce e si verifica nei progetti concreti. `nixos`, `bi`, `economia` e `salute` non sono solo consumatori del metodo: sono casi sperimentali con vincoli diversi. Un progetto code-based espone problemi di fedeltà tecnica e copertura del codice; un progetto finanziario espone problemi di fonti autoritative e dati sensibili; un progetto riflessivo espone problemi di hub semantici, accessi cognitivi e filing back. L'osservatorio serve a rendere queste differenze comparabili senza appiattirle.

La direzione che l'osservatorio governa è il movimento dal basso (uno dei due di `sviluppo-metodo`, e quello che protegge dal generalizzare per esigenze immaginate). Si parte da un'esigenza concreta in un repo adottante, si risolve lì nel merito, poi si chiede se la soluzione locale contiene una regola generale. Solo a quel punto il repo adottante modifica `metodo` o produce un commit nel metodo con la generalizzazione. Gli altri repo adottanti non ricevono ordini da `metodo`: leggono i commit del metodo e applicano localmente ciò che è pertinente. Il movimento dall'alto — importare una cornice teorica e verificarla contro i domini reali — non passa da questo flusso: non genera task negli adottanti, ma rilegge l'insieme dei loro componenti per nominare ciò che il confronto fa affiorare.

L'unità di analisi non è solo il nodo KB. Vanno confrontati tutti i componenti della ricetta metodologica:

- README: funzione di bussola (orienta e punta, non immagazzina), qualità dei router, puntatori al cruscotto (plan, catalogo, modello, indice-di-dominio dove esiste)
- CLAUDE.md e AGENTS.md: chiarezza operativa, separazione tra regole d'azione e contenuto di dominio, costo di caricamento
- verdict.md: qualità della memoria interpretativa, granularità delle decisioni, rapporto con git
- tasks/: corrispondenza con `plan.md`, qualità del contesto operativo, presenza di task morti
- nodi KB: quantità, cluster, hub, orfani, formato, link, copertura delle aree reali, equilibrio tra mappa, concetto, reference e runbook
- strumenti: comandi comuni, estensioni locali, dipendenze, output ricostruibili, confine tra audit strutturale e fedeltà cognitiva
- skill: workflow ricorrenti, differenze locali, duplicazioni, possibilità di template o wrapper comuni
- fonti di verità: codice, JSON, documenti autoritativi, mappe, output strutturati e dati locali

Il confronto deve produrre tre tipi di esito:

- generalizzazione metodologica: una differenza locale rivela una regola portabile e viene integrata nei nodi di metodo
- estensione strumentale: una duplicazione stabile diventa script, comando, skill base o template riusabile
- task locale: un problema resta lavoro autonomo di dominio e va tracciato nel `tasks/` del repo interessato
- manutenzione propria del metodo: una generalizzazione già emersa richiede ristrutturazione, semplificazione, rinomina, documentazione o strumenti portabili nel repo `metodo`

La distinzione è cruciale. Il repo metodo non deve diventare un contenitore di problemi altrui né un orchestratore centralizzato che toglie autonomia ai progetti. Deve invece funzionare come osservatorio: raccoglie segnali, interpreta pattern e custodisce generalizzazioni. Le verifiche operative restano nei repo dove nascono, perché lì vivono fonti, priorità, dipendenze e criteri di chiusura.

Analisi periodiche:

- inventario componenti: presenza e forma di README, CLAUDE, AGENTS, map, plan, verdict, tasks, scripts, skill, nodi metodo e nodi dominio
- confronto strumenti: sottocomandi comuni, comandi locali, dipendenze, output, compatibilità della superficie base
- confronto skill: scopo, istruzioni, path, formatter, relazione con script versionati
- confronto KB: numero nodi, link, orfani, hub, cluster, tipi documentali, nodi non indicizzati, accessi cognitivi
- confronto fedeltà: fonti di verità disponibili, fatti verificabili, aree scoperte, segnali anti-drift
- confronto operativo: task aperti, voci verdict significative, problemi ricorrenti e interventi rimandati ai repo locali

La forma ideale è un ciclo leggero:

1. partire da un problema concreto in un repo adottante
2. risolvere il problema nel merito, con task, verdict e nodi locali
3. distinguere cosa è specifico del dominio da cosa è portabile
4. aggiornare `metodo` solo con la generalizzazione o con uno strumento comune già giustificato dall'uso
5. propagare agli altri repo tramite lettura dei commit di `metodo`, non tramite task centrali prescrittivi
6. ripetere quando nuovi casi reali confermano, correggono o limitano la generalizzazione

Questo ciclo rende il repo metodo un meta-strumento di cognizione sulla cognizione: non solo documenta come pensare con una KB, ma osserva come le KB reali evolvono, dove falliscono, dove divergono e quali forme si dimostrano più robuste.

## Prima fotografia cross-repo

La fotografia del 2026-05-23 è sintetizzata nel nodo `confronto-progetti-adottanti`. Il principio adottato è distribuire il confronto: la sintesi tira le somme, mentre i nodi dei singoli componenti contengono la situazione concreta dei quattro progetti e il confronto tra teoria e applicazione pratica.

Questa forma evita due errori opposti. Il README resta leggero e non diventa report analitico; il confronto non resta però confinato in un documento isolato, perché ogni componente del metodo accumula i propri esempi reali.

Esito metodologico iniziale:

- `nixos` è il riferimento per strumenti anti-drift code-based;
- `bi` è il caso guida per chiarire il confine tra `CLAUDE.md`, nodi KB e strumenti locali;
- `economia` è il caso guida per fonti autoritative, stato corrente e scadenze;
- `salute` è il caso guida per KB concettuali, filing back e mappa non tecnica.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [sviluppo-metodo](sviluppo-metodo.md)
- [strumenti-kb](strumenti-kb.md)
- [struttura-progetto](struttura-progetto.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [knowledge-base](knowledge-base.md)
- [readme](readme.md)
- [claude](claude.md)
- [agents](agents.md)
- [plan](plan.md)
- [tasks](tasks.md)
- [verdict](verdict.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [fonte-di-verita](fonte-di-verita.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
