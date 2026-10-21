---
sintesi: "Canone delle skill fissato (skill, skill-composition, agent-as-user) e prescritto agli adottanti; restano il guardiano, il gate deterministico di /commit, la prova di .agents/skills e la rinomina unica per atto."
ciclo: dev
---

# Progettazione delle skill

## Origine

Segnalazione della sessione `nixos`, 2026-10-21, con le risposte del custode
costruite in quella sessione. Forma approvata in sessione: atomicità per atto
e contratto, composta, base e ramo, due regole senza eccezioni, indipendenza
dall'harness come criterio. Prescrizione agli adottanti in
[o3/progettazione-skill.md](../o3/progettazione-skill.md); l'ordine della
revisione per repo vive in
[agente-come-utilizzatore.md](agente-come-utilizzatore.md).

## Da fare in method

1. **Guardiano:** fatto il 2026-10-21. `o3/skill_tools.py` (`audit`,
   `classifica`) con test, avviato da `/kb audit` tramite il profilo; la parte
   qualitativa è la sezione «Skill» di `/kb review`. Prima uscita su `method`:
   `ruff format` scritto in `/commit` e non concesso nel giro (vincolo voluto:
   il giro non modifica `o3/`), `git -C` ed `echo rc=$?` in `/cycle` come
   segnali di vincoli veri. Limite: l'estrazione dei comandi è euristica e
   non vede i divieti scritti senza le parole del cartello.
2. **Gate deterministico di `/commit`:** formatter, controlli,
   `build.py --check`, audit KB quando cambia `kb/` e verifica dei trailer in
   uno script di `o3/`, con un profilo locale per i formatter degli
   adottanti; lanciabile anche da un hook git. In `/commit` restano filing
   back, messaggio e `Autonomia`.
3. **Prova di `.agents/skills/`:** la cartella della specifica Agent Skills
   è letta da pi 1.3.0 (documentato) e compare in Codex 0.163 e in Claude
   Code 2.1.303. Se una prova reale conferma che i tre la caricano, il
   contenuto può viverci e i wrapper per harness si riducono.
4. **Rinomina unica per atto**, quando la composizione si è stabilizzata:
   due skill, una quantitativa e una qualitativa, con l'oggetto come
   argomento (`kb|skill`), al posto di `/kb audit|review`, che divide per
   argomento due atti con contratti diversi. Alias di due righe per i nomi
   vecchi finché servono. Nomi da decidere allora: inglese per le canoniche,
   nessun verbo generico (`review`, `audit`), collisioni verificate harness per
   harness. In Claude Code 2.1.303 risultano integrati fra gli altri `plan`,
   `goal`, `security-review` e una voce `exec` da verificare contro la
   skill omonima.

## Criterio di chiusura

Punti 1-4 chiusi o ricondotti a task propri. Riga del plan, voce in
`o2/tasks.md` e questo file si rimuovono nello stesso commit.

Connessioni:

- [skill](../kb/skill.md)
- [skill-composition](../kb/skill-composition.md)
- [agent-as-user](../kb/agent-as-user.md)
- [kb-tools](../kb/kb-tools.md)
