---
data: 2026-05-23
stato: maturo
---

# Osservatorio metodo

Il repo metodo non è solo una libreria di nodi portabili: è il punto di osservazione da cui il metodo viene riletto mentre viene applicato nei progetti adottanti. La sua funzione meta-cognitiva è raccogliere differenze, convergenze, attriti e drift tra le implementazioni reali, trasformandoli in conoscenza metodologica stabile o in task locali per i singoli repository.

Il metodo nasce e si verifica nei progetti concreti. `nixos`, `bi`, `economia` e `salute` non sono solo consumatori del metodo: sono casi sperimentali con vincoli diversi. Un progetto code-based espone problemi di fedeltà tecnica e copertura del codice; un progetto finanziario espone problemi di fonti autoritative e dati sensibili; un progetto riflessivo espone problemi di hub semantici, accessi cognitivi e filing back. L'osservatorio serve a rendere queste differenze comparabili senza appiattirle.

L'unità di analisi non è solo il nodo KB. Vanno confrontati tutti i componenti della ricetta metodologica:

- README: funzione di bootstrap, qualità dei router, indice statico, task aperti, relazione con la mappa di progetto
- CLAUDE.md e AGENTS.md: chiarezza operativa, separazione tra regole d'azione e contenuto di dominio, costo di caricamento
- log.md: qualità della memoria interpretativa, granularità delle decisioni, rapporto con git
- todo/: corrispondenza con README, qualità del contesto operativo, presenza di task morti
- nodi KB: quantità, cluster, hub, orfani, formato, link, copertura delle aree reali, equilibrio tra mappa, concetto, reference e runbook
- strumenti: comandi comuni, estensioni locali, dipendenze, output ricostruibili, confine tra audit strutturale e fedeltà cognitiva
- skill: workflow ricorrenti, differenze locali, duplicazioni, possibilità di template o wrapper comuni
- fonti di verità: codice, JSON, documenti autoritativi, mappe, output strutturati e dati locali

Il confronto deve produrre tre tipi di esito:

- generalizzazione metodologica: una differenza locale rivela una regola portabile e viene integrata nei nodi di metodo
- estensione strumentale: una duplicazione stabile diventa script, comando, skill base o template riusabile
- task locale: un problema riguarda un singolo repo e va riportato nel suo `todo/`, non assorbito nel metodo generale

La distinzione è cruciale. Il repo metodo non deve diventare un contenitore di problemi altrui né un orchestratore centralizzato che toglie autonomia ai progetti. Deve invece funzionare come osservatorio: raccoglie segnali, interpreta pattern, propone interventi e rimanda l'azione al livello giusto.

Analisi periodiche:

- inventario componenti: presenza e forma di README, CLAUDE, AGENTS, log, todo, scripts, skill, nodi metodo e nodi dominio
- confronto strumenti: sottocomandi comuni, comandi locali, dipendenze, output, compatibilità della superficie base
- confronto skill: scopo, istruzioni, path, formatter, relazione con script versionati
- confronto KB: numero nodi, link, orfani, hub, cluster, tipi documentali, nodi non indicizzati, accessi cognitivi
- confronto fedeltà: fonti di verità disponibili, fatti verificabili, aree scoperte, segnali anti-drift
- confronto operativo: task aperti, log significativi, problemi ricorrenti e interventi rimandati ai repo locali

La forma ideale è un ciclo leggero:

1. raccogliere dati deterministici dai repo adottanti
2. generare un report comparativo nel repo metodo
3. interpretare il report in una voce di log o in un nodo stabile
4. aggiornare il metodo se emerge una generalizzazione
5. aprire task nei repo locali quando il problema è specifico
6. ripetere periodicamente o dopo sessioni strutturali importanti

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

- [metodo-kb](metodo-kb.md)
- [strumenti-kb](strumenti-kb.md)
- [struttura-progetto](struttura-progetto.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [knowledge-base](knowledge-base.md)
- [readme](readme.md)
- [claude](claude.md)
- [agents](agents.md)
- [task-aperti](task-aperti.md)
- [todo](todo.md)
- [log](log.md)
- [git-history](git-history.md)
- [skill](skill.md)
- [fonte-di-verita](fonte-di-verita.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
