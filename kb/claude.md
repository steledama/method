---
stato: maturo
---

# CLAUDE

`CLAUDE.md` contiene le regole operative necessarie a un agente prima di agire
nel repository. Risponde a «come devo operare qui?»; la conoscenza stabile del
dominio vive nei nodi.

## Contenuto

- ordine di bootstrap e contesto da leggere;
- autorizzazioni, divieti e azioni che richiedono conferma;
- guardrail di sicurezza e vincoli di dominio;
- ambiente necessario e comandi minimi ad alta frequenza;
- skill disponibili e condizioni d'uso;
- convenzioni che cambiano il modo di modificare il progetto;
- puntatori ai nodi che spiegano architettura e procedure.

Un paragrafo che spiega come funziona stabilmente il sistema appartiene alla KB.
Un paragrafo che deve essere presente prima dell'azione per guidarla o impedire
un danno appartiene a CLAUDE. La lunghezza è solo un segnale: i guardrail ad
alta posta restano anche quando rendono il file esteso.

`AGENTS.md` è un wrapper breve per gli harness che lo cercano: indica `README →
CLAUDE → nodo pertinente` e non duplica regole. Non richiede un nodo concettuale
autonomo.

## Criteri di revisione

- ogni regola cambia davvero un'azione dell'agente?
- descrizioni e razionali consultabili on-demand possono migrare in KB?
- comandi rari o completi possono vivere in un nodo o nello `--help`?
- README, Goal o World sono duplicati?
- i guardrail necessari prima di un atto rischioso sono ancora visibili?

CLAUDE è il livello operativo della divisione «README orienta · CLAUDE istruisce
· KB approfondisce». Non è una fonte di fatti per audit o fedeltà cognitiva.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [readme](readme.md)
- [project-structure](project-structure.md)
- [skill](skill.md)
- [kb-tools](kb-tools.md)
