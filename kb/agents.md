---
data: 2026-05-23
stato: bozza
---

# AGENTS

AGENTS.md è il wrapper agent-agnostico del progetto. Risponde alla domanda: dove trovo le istruzioni operative condivise tra agenti? La sua funzione non è spiegare il dominio né duplicare regole operative, ma indicare con il minimo attrito il percorso di bootstrap che qualunque agente deve seguire.

AGENTS.md esiste perché agenti diversi cercano convenzioni diverse. Un progetto può essere usato da Claude, Codex o altri strumenti; il wrapper impedisce che ogni agente abbia un ingresso divergente. La costituzione operativa resta in CLAUDE.md o nei file equivalenti locali; AGENTS.md è il ponte comune.

Regole:

- deve essere breve
- deve esplicitare l'ordine di lettura a inizio sessione
- deve rimandare a README.md e CLAUDE.md
- non deve contenere regole operative divergenti
- non deve contenere conoscenza di dominio
- quando cambia il bootstrap del progetto, va aggiornato insieme a CLAUDE.md

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                                      | Confronto con il metodo                                                                                                                |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | wrapper breve con ordine esplicito README → mappa → CLAUDE → nodo.                                                                      | È il modello più chiaro: breve, agent-agnostico e coerente con il bootstrap reale.                                                     |
| `bi`       | wrapper minimale.                                                                                                                       | Aderisce alla brevità, ma potrebbe esplicitare meglio l'ordine completo di lettura come fa `nixos`.                                    |
| `economia` | wrapper minimale.                                                                                                                       | Funziona come ponte, ma il bootstrap effettivo include anche `stato.md`, `scadenze.md` e mappa; AGENTS potrebbe renderlo più visibile. |
| `salute`   | wrapper minimale; il bootstrap locale ora passa da README verso `mappa-progetto`, `principi-salute` e `verifica-nel-vivere`.            | Adeguato come wrapper; potrebbe esplicitare il percorso completo se il costo di scoperta torna alto.                                   |

Il confronto conferma che AGENTS deve restare piccolo. La differenza da osservare non è la quantità di contenuto, ma la precisione del percorso di bootstrap: quando il progetto ha file locali obbligatori (`stato.md`, `scadenze.md`, mappa), il wrapper deve indirizzarli senza duplicare regole operative.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [claude](claude.md)
- [readme](readme.md)
- [struttura-progetto](struttura-progetto.md)
