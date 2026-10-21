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

## File dell'harness

I file che l'harness cerca in `.claude/` sono binding, non sede del contenuto.
Prompt e permessi del ciclo autonomo sono prescrizioni dell'atto e vivono in
`o3/ciclo/`, versionati e leggibili da ogni harness; `.claude/settings.json`
resta dov'è perché l'harness della sessione lo legge solo da lì. Un'opzione
propria di un harness si usa solo come ottimizzazione: la sua assenza non deve
rompere nulla (`skill`, «Indipendenza dall'harness»).

`.claude/settings.local.json` è un'area di transito, non versionata e legata
all'host. Periodicamente ciò che è durevole si promuove in `settings.json` e il
resto si scarta. Il giro autonomo eredita gli allow di `settings.json`: una
promozione allarga anche il perimetro senza custode, quindi si promuove solo ciò
che il giro può fare da solo.

## Criteri di revisione

- ogni regola cambia davvero un'azione dell'agente?
- descrizioni e razionali consultabili on-demand possono migrare in KB?
- comandi rari o completi possono vivere in un nodo o nello `--help`?
- README, Goal o World sono duplicati?
- i guardrail necessari prima di un atto rischioso sono ancora visibili?
- ogni divieto scritto ha dietro un vincolo vero, e ogni gesto richiesto è
  concesso nel contesto in cui l'agente lo compie (`agent-as-user`)?

CLAUDE è il livello operativo della divisione «README orienta · CLAUDE istruisce
· KB approfondisce». Non è una fonte di fatti per audit o fedeltà cognitiva.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [readme](readme.md)
- [project-structure](project-structure.md)
- [skill](skill.md)
- [kb-tools](kb-tools.md)
- [agent-as-user](agent-as-user.md)
