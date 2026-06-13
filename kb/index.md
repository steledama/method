---
data: 2026-06-06
stato: bozza
---

# Index

L'indice risponde alla domanda: quali nodi esistono e come li trovo? È un catalogo statico della KB, organizzato in modo da rendere i nodi scansionabili per cluster, area o intenzione. La sua istanza è il register `kb.md`, la **porta-collezione** di `kb/` nell'atrio di root: si vede a colpo d'occhio ma si consulta on-demand, non a ogni sessione. Vale la scissione visibilità ≠ caricamento (project-structure): sta in root _come porta_, non perché letto al bootstrap — a differenza di `plan`, che è un file-ciclo letto sempre. Il README non lo incorpora: lo punta.

La policy linguistica separa identità e contenuto: register, filename e H1 sono
inglesi; la prosa concettuale resta italiana. `kb.md` è l'artefatto vivo che
cataloga la collezione, mentre `kb/index.md` ne documenta la funzione.

L'indice non è una mappa. L'indice elenca e orienta; la mappa spiega come il dominio si tiene insieme. Confondere i due produce README troppo lunghi o mappe ridotte a cataloghi. La distinzione è preziosa per l'LLM perché separa recupero rapido e comprensione strutturale.

Regole:

- vive come register `kb.md`, porta-collezione in root, aperta on-demand
- il README lo punta, non lo duplica
- deve contenere tutti i nodi stabili indicizzati
- può essere organizzato per cluster o intenzione
- deve restare più catalogo che spiegazione
- non sostituisce la mappa del dominio (map)
- va verificato con strumenti deterministici quando possibile
- indicizza la KB locale del progetto; contenuti trans-repo consumati via symlink
  vanno dichiarati come dipendenza, non mescolati al catalogo locale

## Applicazione nei progetti adottanti

- **`nixos`** — situazione attuale: indice compatto, pochi cluster tecnici ben delimitati, nessun nodo mancante. Confronto con il metodo: adatto a un codebase con macro-aree tecniche nette.
- **`bi`** — situazione attuale: indice molto granulare con molti cluster. Confronto con il metodo: funziona perché cluster e mappa separano catalogo e modello del dominio.
- **`economia`** — situazione attuale: indice locale che referenzia i nodi metodologici condivisi come repo trans-repo via symlink. Confronto con il metodo: indice più fedele — separa catalogo della KB di dominio e metodo condiviso, così non confonde dipendenza e contenuto locale.
- **`salute`** — situazione attuale: indice esteso per una KB concettuale ampia. Confronto con il metodo: necessario al dominio riflessivo; il rischio è che diventi anche mappa.

I conteggi aggiornati (nodi, cluster) vivono in adopter-comparison. La pratica conferma la distinzione: l'indice può essere lungo, ma deve restare catalogo. Nei progetti grandi serve una mappa autonoma per evitare che le descrizioni dei cluster diventino l'unico modello del dominio.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [readme](readme.md)
- [map](map.md)
- [node](node.md)
- [kb-tools](kb-tools.md)
