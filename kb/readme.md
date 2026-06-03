---
data: 2026-05-23
stato: bozza
---

# README

README.md è il bootstrap principale del progetto. Risponde alla domanda: dove sono e da dove parto? Deve permettere a un umano o a un LLM di capire rapidamente scopo, stato, task aperti e accessi alla KB senza leggere l'intero repository.

README.md ha una doppia audience. Per l'umano è la porta d'ingresso leggibile; per l'LLM è il primo compressore del contesto. Per questo deve essere sintetico ma semantico: non solo elenco di file, ma orientamento al dominio, priorità operative e indice dei nodi.

Funzioni:

- descrivere nome, dominio e scopo del progetto
- dichiarare principi o approccio locale
- mostrare i task aperti e le priorità correnti
- puntare alla mappa canonica quando esiste
- contenere l'indice statico dei nodi
- elencare molto brevemente gli strumenti disponibili, rimandando a CLAUDE per
  l'uso operativo e ai nodi per il dettaglio
- distinguere metodo portabile e specificità locali

Nei progetti adottanti, il README deve dichiarare il metodo condiviso come
dipendenza trans-repo quando i nodi metodologici arrivano via symlink
(`metodo/ -> ../metodo/kb`). Non deve indicizzare quei nodi uno per uno come se
fossero conoscenza locale del dominio: il lettore deve capire cosa appartiene al
metodo portabile e cosa appartiene al progetto.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                                                                                                  | Confronto con il metodo                                                                                                                                                                |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | README sintetico e molto orientativo: host, principi, task, documentazione, router "capire il progetto in 5 minuti" e catalogo completo.                                                            | È il caso più vicino alla funzione ideale di bootstrap: orienta senza diventare manuale completo e rimanda alla mappa canonica.                                                        |
| `bi`       | README ampio ma funzionale: struttura, comandi, repo collegati, skill, task e indice per cluster applicativi.                                                                                       | Funziona come router operativo e catalogo; il rischio è la crescita insieme alla complessità del dominio, ma la mappa aiuta a non trasformarlo in spiegazione totale.                  |
| `economia` | README combina orientamento, task urgenti, indice KB, struttura, privacy e pointer agli strumenti; la sezione metodo dichiara il repo trans-repo invece di indicizzare i singoli nodi metodologici. | Buon adattamento a un dominio ad alta responsabilità: il bootstrap deve includere stato corrente e scadenze, purché conoscenza stabile e metodo condiviso restino nei luoghi canonici. |
| `salute`   | README lungo e narrativo, ora con pointer espliciti a `mappa-progetto`, `principi-salute` e `verifica-nel-vivere`.                                                                                  | Resta efficace come ingresso storico e umano; la mappa autonoma riduce il rischio che il README debba spiegare anche il modello del dominio.                                           |

Il confronto chiarisce che il README non deve avere una lunghezza unica. Deve però preservare la funzione: ingresso, orientamento e indice. Quando inizia a contenere spiegazioni di dominio o teoria del metodo, il contenuto va spostato nei nodi e il README deve restare un router.

La stessa regola vale per gli strumenti: il README li rende visibili con una lista breve — quali esistono e dove approfondirli — non con procedure, flag o troubleshooting. È il primo livello della tripartizione README orienta · CLAUDE istruisce · KB approfondisce, dettagliata in `strumenti-kb`.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [indice](indice.md)
- [task-aperti](task-aperti.md)
- [mappa](mappa.md)
- [claude](claude.md)
- [struttura-progetto](struttura-progetto.md)
- [strumenti-kb](strumenti-kb.md)
