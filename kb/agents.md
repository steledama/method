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

Connessioni:

- [metodo-kb](metodo-kb.md)
- [claude](claude.md)
- [readme](readme.md)
- [struttura-progetto](struttura-progetto.md)
