---
data: 2026-06-07
stato: aperto
---

# Skill method-review per riallineare gli adottanti

Progettare una skill base condivisa `method-review`, canonica in `metodo` e
replicata nei repo adottanti, per verificare il drift locale rispetto
all'evoluzione del metodo senza aprire task centrali di propagazione.

Dipende dal completamento del rename strutturale `metodo` → `method`, per
progettare path e marker direttamente sul nome definitivo senza introdurre churn.

La skill si esegue nel repo adottante. Legge i commit di `metodo` successivi
all'ultima revisione registrata, confronta le generalizzazioni portabili con
l'implementazione locale e distingue:

- cambiamenti applicabili direttamente;
- cambiamenti da adattare al dominio;
- cambiamenti non pertinenti;
- divergenze locali intenzionali da preservare;
- problemi locali che richiedono un task nel repo adottante.

Non deve orchestrare modifiche cross-repo dal repository `metodo`, applicare
ciecamente ogni differenza o sostituire `tasks-review`: `method-review` controlla
la relazione adottante-metodo; `tasks-review` supervisiona il lavoro futuro del
dominio.

## Questioni da risolvere

- come registrare in modo versionato e leggibile l'ultimo commit di `metodo`
  revisionato, senza stato host-locale o opaco;
- quali superfici confrontare: README, CLAUDE, AGENTS, porte root, nodi
  metodologici, skill base, strumenti e convenzioni;
- quali controlli possono essere deterministici e quali richiedono giudizio;
- se la skill debba solo proporre modifiche o possa applicarle dopo conferma;
- come gestire modifiche locali legittime alle skill forkate senza sovrascriverle;
- come produrre un esito sintetico: allineato, adattamento necessario, non
  pertinente, task locale aperto;
- come evitare che il marker di revisione dichiari allineamento quando restano
  modifiche pertinenti non applicate;
- **blind spot host-config (dichiarato, non risolvibile dalla skill):** alcune
  regole del metodo si impongono in config fuori dai repo (es. il disable di
  `auto-memory`, versionato in `nixos`, non in ciascun adottante). La skill legge
  il `git log` dei repo e non vede questo strato: deve dichiararlo come limite, non
  certificarlo allineato. Cfr. why.md «La memoria dell'harness: regola portabile a
  L2…».

## Pilota

1. Definire il contratto della skill in `metodo` e il formato del marker
   versionato.
2. Implementare la copia canonica con wrapper Codex.
3. Pilotarla su un solo adottante con drift reale o ricostruito dalla recente
   propagazione README-bussola.
4. Verificare che distingua correttamente canone comune e adattamento locale.
5. Solo dopo il pilota, replicarla negli altri adottanti e aggiornare il nodo
   `skill`.

## Criterio di chiusura

La skill è presente e documentata in `metodo`, validata su un adottante e
replicata nei quattro repo. Ogni esecuzione può determinare in modo verificabile
quali commit del metodo sono stati revisionati e lascia eventuale lavoro futuro
nel `plan.md`/`tasks/` del repo locale, non in quello di `metodo`.
