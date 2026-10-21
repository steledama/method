---
data: 2026-10-21
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, baserow, danea-auto
---

# Skill e permessi progettati per l'agente utilizzatore

## Cosa e perché

Il custode ha deciso il 2026-10-21, su segnalazione della sessione `nixos`, che
l'agente è un utilizzatore a pieno titolo dello strumento e che le skill si
progettano con lo stesso rigore della KB. Il canone ora lo dice in tre nodi:

- [agent-as-user](../kb/agent-as-user.md): le specificità dell'agente, il
  diniego come percezione da classificare (vincolo voluto o lacuna), il
  divieto del cartello, il deny che presidia il gesto e non una sua grafia;
- [skill](../kb/skill.md): atomicità per atto e contratto, la skill come
  indice condizionale della KB, prima estrarre e poi dividere, indipendenza
  dall'harness;
- [skill-composition](../kb/skill-composition.md): composta, base e ramo;
  una base non chiama altre skill, una composta non contiene procedura di
  dominio; il costo dell'elenco; la misura.

Il segnale che l'ha resa urgente: le copie di `eval` arrivano a 415 righe
(`salute`) e 676 (`economia`) contro le 245 del canone, `/manutenzione` di
`nixos` è cresciuta fino a 1227 righe prima di una potatura verso `o3/`, e i
giri autonomi pagano dinieghi su gesti che il prompt stesso richiede.

## Ricetta per il /method locale

1. **Canone già recepito per symlink, da applicare:**
   - togliere da `.claude/settings.json` i deny su `git add -A*`,
     `--all*`, `git add .` e `git add . *`; restano `-f`/`--force` e gli
     altri deny git (`o3/ciclo-autonomo.md`, punto 7);
   - nella `/commit` locale il cartello «non usare `git add -A`» lascia il
     posto al confronto di `git status` prima dello staging;
   - il gate deterministico di `/commit`: un profilo locale
     `o3/commit_gate.toml` con i formatter e i controlli del repo, e la
     `/commit` locale che lancia `method/../o3/commit_gate.py prima` e
     `dopo` invece di elencare formatter, controlli e rilettura dei trailer;
     `/cycle` usa `dopo --giro`. I comandi vanno anche nei permessi del giro;
   - la `/cycle` locale dichiara nel frontmatter ciò che compone
     (`metadata:` con `compone: eval exec commit`, più le eventuali skill di
     dominio che il giro compone): il guardiano ricava da lì le skill del
     giro;
   - `eval` ed `exec` chiudono col proprio esito e la proposta di commit,
     senza chiamare `/commit`; `/cycle` resta la composta che committa. La
     frase corrispondente di `ciclo-delegato` va riportata nell'`autonomy.md`
     locale.
2. **Dinieghi:** classificare quelli registrati in `i1/giri/tentativi.jsonl`,
   per contesto (sessione, giro), come vincolo voluto o lacuna; chiudere ogni
   lacuna su permesso o strumento, mai con un'istruzione nella skill.
3. **Cartelli:** censire in skill, prompt e `CLAUDE.md` i divieti scritti
   («non usare», «non è concesso», «è negato»): per ognuno, il deny che lo
   regge oppure la lacuna da chiudere.
4. **Mappa delle skill:** per ogni skill locale sopra le dimensioni del
   canone, dividere il testo per sezione in nucleo (obiettivi, vincoli,
   sequenza, decisioni, esito), conoscenza da nodo `kb/`, duplicato di un
   nodo esistente, schema di un registro, logica da script.
5. **Estrarre** prima di dividere: nodi, register e script ricevono ciò che
   non è procedura, e la skill vi rimanda a condizione.
6. **Composizione:** solo dopo l'estrazione, decidere se una skill ombrello
   diventa una composta con basi o con rami. Una base nuova fissa il proprio
   contratto di esito prima di essere scritta; quando più basi servono una
   composta, il contratto comune si fissa prima delle basi.
7. Verificare con i test e `python3 o3/view/build.py --check`, registrare il
   recepimento nel marker; i punti 4-6 possono restare task `o2/` locali
   collegati al plan.

Il guardiano delle skill parte dalla root del repo:
`python3 method/../o3/skill_tools.py audit`, lanciato dal checkout del canone
senza copiarlo. I punti 2-4 partono dalla sua uscita; il profilo locale di
`/kb` (`domain.md`) lo dichiara fra i comandi dell'audit.

## Note per repo, da verificare in loco

- `nixos`: primo adottante. Le parti di `/manutenzione` (ia, home-manager,
  casa, lavoro, docker, world) servono quasi sempre dalla composta, quindi
  probabilmente sono rami; gli script del registro restano strumenti
  condivisi. Task locale `o2/design-agent-as-user.md`.
- `bi`: la gestione del catalogo ha già basi nate dal basso (corrispondenze,
  categorizzazione, tassonomia) e altre quattro nel plan. Fissare il
  contratto di esito comune prima della prossima base.
- `economia` e `salute`: `eval` locale molto sopra il canone; misurare quanta
  parte è profilo di dominio da portare in `kb/`.
