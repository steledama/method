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
2. **Gate deterministico di `/commit`:** fatto il 2026-10-21.
   `o3/commit_gate.py` (`prima`, `dopo [--giro]`) col profilo locale
   `o3/commit_gate.toml`; `/commit` e `/cycle` lo lanciano, i permessi del
   giro lo concedono. Lanciabile anche da un hook git, non ancora installato.
   Verificato sullo storico: `dopo --giro` passa sull'ultimo giro (`8030882`).
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

5. **Stadi di una base in file accanto:** proposta di `nixos` del
   2026-10-24, nel confronto autorizzato dal custode (`o2/design-agent-as-user.md`
   e `i1/agent-task-orientation-20261024.md` di `nixos`). Il caso è rivedere
   un task già scelto: `exec` va letta per intero, ma serve solo `specify`.
   La forma è un ingresso comune breve, con gate, esiti e trailer, e
   `plan`, `specify` e `perform` in file accanto, letti solo se lo stadio è
   dovuto. Le regole restano in una sola copia e non nasce nessuna skill
   nuova. Il prototipo è nel solo fork, non ancora collaudato su sessioni
   nuove. Riscontro dato a `nixos`:
   - si estrae prima di dividere (`kb/skill.md`, punti 4-6 di
     `o3/progettazione-skill.md`): `plan` pesa circa 120 righe e il passo 3b
     è soprattutto conoscenza;
   - la revisione di un task singolo è `specify` con l'oggetto come
     argomento, `exec specify <task>`. Il canone legge `specify` come una
     rassegna di tutti i file `o2/`, e un instradamento per intento scritto in
     prosa non dà lo stesso risultato con ogni agente;
   - la divisione si prova con la stessa partizione che si proporrebbe al
     canone. Se la prova regge sulle tre richieste («rivediamo questo task»,
     «qual è il prossimo task?», `/exec all`), il canone la recepisce, anche
     per `eval`. Altrimenti ogni recezione con `/method` diventa un'unione a
     mano.
     Questione per il canone, chiusa il 2026-10-25 su rilievo di `salute`:
     `skill-composition` distingue il supporto condizionale di una base,
     parte del suo atto letta su uno scope, dal ramo della composta; una base
     con supporti resta base, senza terzo livello.
     Limite segnalato da `nixos`: il guardiano contava le righe dei file
     accanto ma ne ignorava comandi, divieti, chiamate e trailer. Chiuso il
     2026-10-24: `skill_tools.py` legge anche i rami e li etichetta
     `skill/file:riga`, con un test che lo copre. La forma resta da
     consolidare dopo la prova del fork.
     Rilievi di `salute` (bfaf406), chiusi il 2026-10-25: le chiamate fra
     skill si cercano con più verbi (anche «usare») nella riga o nella
     precedente, e le menzioni senza verbo escono come candidati; comandi e
     divieti si censiscono anche in `CLAUDE.md`, `AGENTS.md` e prompt del
     giro; un divieto di sessione retto solo dai deny del giro è segnalato.
     Lo stesso falso negativo c'era nel canone (`commit` e `method`
     chiamavano `/exec plan`): ora restituiscono un handoff.

## Criterio di chiusura

Punti 1-5 chiusi o ricondotti a task propri. Riga del plan, voce in
`o2/tasks.md` e questo file si rimuovono nello stesso commit.

Connessioni:

- [skill](../kb/skill.md)
- [skill-composition](../kb/skill-composition.md)
- [agent-as-user](../kb/agent-as-user.md)
- [kb-tools](../kb/kb-tools.md)
