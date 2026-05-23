---
data: 2026-05-23
stato: bozza
---

# Mappa

La mappa è il nodo che risponde alla domanda: come si tiene insieme questo dominio? Collega entità, fonti di verità, flussi, responsabilità, aree e nodi di approfondimento. Non serve a elencare tutto, ma a rendere visibile il modello del sistema.

Per un LLM la mappa è un dispositivo cognitivo fondamentale. Senza mappa, l'agente deve ricostruire il dominio da README, nomi file e link. Con una buona mappa, può capire rapidamente quali elementi sono centrali, quali fonti verificano i fatti e quali nodi aprire per un intervento.

Regole:

- vive in kb/ perché descrive conoscenza stabile del dominio
- viene linkata dal README come primo nodo di comprensione
- collega sistema reale, fonti di verità e nodi
- non sostituisce l'indice completo
- non deve diventare storico o lista di task
- può essere diversa per domini tecnici, finanziari o riflessivi

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | `kb/project-map.md` collega host, profili home, macro-aree, fonti Nix e nodi. | Esempio forte di mappa code-based: trasforma filesystem e configurazione in modello leggibile. |
| `bi` | `kb/project-map.md` collega sistemi, flussi dati, script, moduli, fonti tecniche e task strutturali. | Mappa necessaria per un dominio ad alta complessità applicativa; riduce la dipendenza da CLAUDE e README. |
| `economia` | `kb/mappa-progetto.md` collega conti, investimenti, immobili, persone, successioni, dati e nodi. | Buon adattamento non-code: la mappa rende verificabile il ponte tra entità reali, Drive/output JSON e KB. |
| `salute` | Non emerge un nodo mappa autonomo; il README e i cluster svolgono parte della funzione. | È la lacuna più rilevante: una KB riflessiva ha meno fonti tecniche, ma ha comunque bisogno di un modello dei cluster, delle fonti e del loop teoria-pratica. |

Il confronto mostra che la mappa è il componente più adattabile del metodo. Nei repo tecnici mappa codice e flussi; in `economia` mappa entità e dati; in `salute` dovrebbe mappare assi concettuali, fonti e pratiche invece di host o script.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [indice](indice.md)
- [fonte-di-verita](fonte-di-verita.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
