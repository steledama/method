---
data: 2026-05-23
stato: bozza
---

# CLAUDE

CLAUDE.md è la costituzione operativa del progetto per gli agenti. Risponde alla domanda: come devo agire in questo repo? Contiene regole d'azione, vincoli, permessi, procedure sicure e riferimenti rapidi; non contiene conoscenza stabile del dominio.

La distinzione è essenziale. Se CLAUDE.md spiega come funziona il sistema, diventa documentazione narrativa e compete con la KB. Se invece resta costituzione operativa, può essere caricato spesso senza gonfiare il contesto e senza creare una seconda fonte di verità.

Regole:

- apre con il bootstrap di sessione
- contiene comportamenti consentiti, proibiti o da chiedere
- può elencare comandi quotidiani ad alta frequenza
- rimanda ai nodi KB per architettura, procedure e spiegazioni stabili
- non è fonte di fatti per audit o fedeltà cognitiva
- quando supera il ruolo operativo, il contenuto va trasferito nei nodi tematici

Connessioni:

- [metodo-kb](metodo-kb.md)
- [agents](agents.md)
- [readme](readme.md)
- [struttura-progetto](struttura-progetto.md)
- [skill](skill.md)
