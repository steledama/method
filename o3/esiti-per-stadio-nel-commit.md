---
data: 2026-09-24
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto
---

# Ogni giro di `eval` ed `exec` lascia l'esito per stadio nel commit

## Cosa e perché

La clausola di uscita della tripartizione `eval`/`exec` giudica la divisione
in stadi soprattutto sugli **esiti nulli**: uno stadio che chiude vuoto in
tutti i repository per tre giri direbbe che la divisione è «troppo». Il
battito del 2026-09-24 ha mostrato che questa misura non esiste: un esito
vuoto viene restituito solo in conversazione e non lascia traccia, così un
giro senza materia è indistinguibile da un giro mai fatto
(`i3/skill-per-arco-tripartito.md`, verdetto del 2026-09-24).

Il canone (`kb/skill.md`) ora chiede che l'esito resti nella storia. Nessun
file nuovo: il log è git.

## Ricetta di recepimento

1. Nei fork locali di `.claude/skills/eval/SKILL.md` e `exec/SKILL.md`, dopo la
   regola della chiusura in una riga, aggiungi la registrazione dell'esito
   nel commit che chiude il giro:
   `Esiti: <stadio>=materia|vuoto ...`, una voce per ogni stadio invocato.
   Preserva le parametrizzazioni di dominio.
2. Gli **scope di dominio** montati sulle canoniche (`eval trascrizione` in
   `salute`, `eval finanze|posta|registrazioni` in `economia`) registrano lo
   stadio canonico a cui appartengono, per esempio
   `Esiti: perceive=materia`, oppure tutti e tre per `finanze`, che attraversa
   l'arco. Così il conteggio resta confrontabile fra repository.
3. Un giro senza file cambiati si committa con `git commit --allow-empty` e lo
   stesso trailer. Nel fork di `/commit`, se la regola «una riga» è ancora
   presente, aggiungi l'eccezione per il trailer `Esiti:`.
4. Le skill di dominio **autonome** (`manutenzione` in `nixos`; `ordini`,
   `categorizzazione`, `tassonomia` in `bi`) non sono coinvolte: non sono
   stadi della tripartizione.
5. Registra il recepimento nel marker `i3/allineamento-metodo.md`.

## Verifica

`git log --since=<data> --format='%(trailers:key=Esiti,valueonly)'` restituisce
una riga per giro. Il battito `/adottanti` del 2026-11-01 la usa per contare
gli esiti per stadio e per repository. Un repository senza nessuna riga dopo
il recepimento non ha fatto giri, oppure non registra: la distinzione si fa
leggendo il resto del `git log`.
