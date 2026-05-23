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

## Applicazione nei progetti adottanti

| Progetto | Situazione attuale | Confronto con il metodo |
| -------- | ------------------ | ----------------------- |
| `nixos` | 37 nodi indicizzati, 7 cluster, nessun nodo mancante dal README. | Indice compatto e completo, adatto a un codebase con macro-aree tecniche ben delimitate. |
| `bi` | 78 nodi indicizzati, 11 cluster, nessun nodo mancante. | Indice molto granulare; funziona perché cluster e mappa separano catalogo e modello del dominio. |
| `economia` | 44 nodi indicizzati, 4 cluster, nessun nodo mancante. | Indice leggibile, ma l'audit segnala un cluster isolato nella zona strumenti/servizi esterni. |
| `salute` | 193 nodi indicizzati, 8 cluster, nessun nodo mancante. | Indice esteso ma necessario per una KB concettuale ampia; il rischio è che il README diventi anche mappa. |

La pratica conferma la distinzione: l'indice può essere lungo, ma deve restare catalogo. Nei progetti grandi serve una mappa autonoma per evitare che le descrizioni dei cluster diventino l'unico modello del dominio.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [mappa](mappa.md)
- [nodo](nodo.md)
- [strumenti-kb](strumenti-kb.md)
