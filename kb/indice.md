---
data: 2026-05-23
stato: bozza
---

# Indice

L'indice è la parte del README che risponde alla domanda: quali nodi esistono e come li trovo? È un catalogo statico della KB, organizzato in modo da rendere i nodi scansionabili per cluster, area o intenzione.

L'indice non è una mappa. L'indice elenca e orienta; la mappa spiega come il dominio si tiene insieme. Confondere i due produce README troppo lunghi o mappe ridotte a cataloghi. La distinzione è preziosa per l'LLM perché separa recupero rapido e comprensione strutturale.

Regole:

- vive nel README, non come nodo separato operativo del progetto
- deve contenere tutti i nodi stabili indicizzati
- può essere organizzato per cluster o intenzione
- deve restare più catalogo che spiegazione
- non sostituisce la mappa del dominio
- va verificato con strumenti deterministici quando possibile
- indicizza la KB locale del progetto; contenuti trans-repo consumati via symlink
  vanno dichiarati come dipendenza, non mescolati al catalogo locale

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                            | Confronto con il metodo                                                                                                                               |
| ---------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | indice compatto, pochi cluster tecnici ben delimitati, nessun nodo mancante.                  | Adatto a un codebase con macro-aree tecniche nette.                                                                                                   |
| `bi`       | indice molto granulare con molti cluster.                                                     | Funziona perché cluster e mappa separano catalogo e modello del dominio.                                                                              |
| `economia` | indice locale che referenzia i nodi metodologici condivisi come repo trans-repo via symlink.  | Indice più fedele: separa catalogo della KB di dominio e metodo condiviso, così il README non confonde dipendenza e contenuto locale.                |
| `salute`   | indice esteso per una KB concettuale ampia.                                                   | Necessario al dominio riflessivo; il rischio è che il README diventi anche mappa.                                                                     |

I conteggi aggiornati (nodi, cluster) vivono in `confronto-progetti-adottanti`. La pratica conferma la distinzione: l'indice può essere lungo, ma deve restare catalogo. Nei progetti grandi serve una mappa autonoma per evitare che le descrizioni dei cluster diventino l'unico modello del dominio.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [mappa](mappa.md)
- [nodo](nodo.md)
- [strumenti-kb](strumenti-kb.md)
