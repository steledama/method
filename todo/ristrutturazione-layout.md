---
data: 2026-06-06
stato: aperto
---

# Ristrutturazione del layout — disegno unico, migrazione atomica

Documento di disegno della riorganizzazione del top level del repo (e dei 4 adottanti). Consolida
e sostituisce `rinomina-log-why`. Regola di lavoro: **niente file di contenuto si tocca finché il
disegno non è approvato**; poi una sola migrazione lo realizza sui 5 repo in un colpo, per pagare
la propagazione una volta sola.

## Principio guida (la triade — da fissare in [[struttura-progetto]] dentro la migrazione)

1. **Root = artefatti bootstrap-essenziali di livello-progetto.** Letti per capire *il tutto*, a
   prescindere dalla pace: README (Goal + mappa), CLAUDE/AGENTS (regole), `why` (memoria di
   valutazione che chiude il ciclo dell'azione).
2. **Cartelle = collezioni di unità atomiche, ognuna con un solo file-meta** che le indicizza o
   ordina. È l'«eccezione che conferma la regola» dentro la cartella.
3. **La pace è criterio di compagnia, non di profondità.** Decide cosa non fondere in un solo file,
   non a che livello del filesystem sta. Quando altezza nel ciclo e pace confliggono (caso `why`:
   alta ma veloce), l'altezza decide la collocazione, la pace decide che resti un file separato.

Conseguenza: l'altezza nel filesystem segue l'altezza nel ciclo di Norman + il costo di bootstrap,
non la stabilità. Sostituisce la vecchia intuizione «più in alto = più stabile», già demolita da
[[pace-layering]].

## Layout target

```
README.md      orientamento + motivazioni/principi (Goal) + MAPPA inline (il modello);
               punta a kb/ (catalogo) e tasks/ (lista). NON contiene più indice né task-board.
CLAUDE.md      regole operative
AGENTS.md      wrapper agent-agnostico
why.md         (ex log.md) memoria interpretativa append-only; entry con chiave = la decisione,
               data come metadato, commit citabile inline come puntatore (mai come spina dorsale)
kb/            i nodi (unità atomiche) + UN file-meta = il catalogo dei nodi
tasks/         (ex todo/) i dettagli dei task + UN file-meta = la lista prioritizzata (deps incluse)
scripts/       invariato
.claude/skills/, .codex/skills/   invariati
```

## Cosa cambia, voce per voce

- **README**: esce l'indice dei nodi, esce la tabella task; entra (o si linka) la mappa. Resta lo
  strato lento: identità, principi, mappa, progetti adottanti, come collegare un progetto.
- **`log.md` → `why.md`**: rinomina + nuovo modello di entry (vedi [[git-history]], che già dice
  «il git log dice cosa, log dice perché»: il nome ora coincide con la funzione).
- **`todo/` → `tasks/`**: allinea la cartella al vocabolario del metodo (`task-aperti`,
  `revisione-tasks`, «Tasks aperti»). Giustificato anche perché ora ospita la lista-Plan, non solo
  i dettagli «da fare».
- **catalogo dei nodi**: dal README a un file-meta dentro `kb/`.
- **lista dei task**: dal README a un file-meta dentro `tasks/`; il README la *punta*, la skill
  `revisione-tasks` la legge a inizio sessione.

## Micro-decisioni aperte (da chiudere su carta prima della migrazione)

- **M1 — nome del file-meta in kb/.** Collisione: il nodo-concetto è già `kb/indice.md`. L'istanza
  non può chiamarsi così. Proposta: istanza = `kb/catalogo.md` (il nodo `indice` la chiama già
  «catalogo»), il concetto resta `kb/indice.md`. Il file-meta non è un nodo: niente frontmatter di
  nodo, e va escluso dall'audit di `kb_tools.py` (per nome o con prefisso `_`).
- **M2 — nome del file-meta in tasks/.** Proposta: `tasks/aperti.md` (coerente col nodo-concetto
  `task-aperti`). Alternativa `tasks/lista.md`.
- **M3 — i nodi-concetto seguono le rinomine delle istanze?** Principio proposto: **un nodo-concetto
  si rinomina solo se il suo nome diventa fuorviante dopo la rinomina dell'istanza.** Casi:
  `kb/log.md` → diventa fuorviante (descrive `why.md`): rinominare, ma a `kb/why.md` per findability
  o a `kb/memoria-interpretativa.md` per purismo tipo/istanza? `kb/todo.md` → descrive la cartella
  ora `tasks/`: rinominare a `kb/tasks.md`? `kb/mappa.md`, `kb/indice.md`, `kb/task-aperti.md`
  restano (sono concetti, non istanze).
- **M4 — tooling.** `scripts/kb_tools.py`: `append_log()`/`log_path`/header `# log.md`/flag
  `--append-log` → `--append-why`; esclusione del file-meta `kb/` dall'audit nodi; aggiornare la
  skill `audit-kb` di ogni progetto che invoca il flag.

## Piano di migrazione (atomico, una volta sola sui 5 repo)

1. approvare disegno + M1–M4 su carta;
2. nel repo `metodo`: rinomine file, riscrittura referenze (~40 in `metodo`), mappa nel README,
   indice e lista nelle cartelle, triade in [[struttura-progetto]], aggiornamento `kb_tools.py` e
   skill, diagrammi della presentazione;
3. nei 4 adottanti **nello stesso passaggio**: i nodi condivisi si propagano via symlink, ma istanze
   root (`log.md`→`why.md`, cartella `todo/`→`tasks/`) e referenze in CLAUDE/README vanno rifatte a
   mano (caso «cambio nome/path di nodo» del `CLAUDE.md`); preservare la distinzione
   why/`diario.md`/`stato.md`;
4. verifica: `kb_tools.py audit` su ogni repo + grep di `log\.md` e `todo/` residui su tutti e 5;
5. **prima entry di `why.md`**: il perché dell'intero ridisegno del layout — la fondazione del file
   scritta nel file che il ridisegno ha ribattezzato.
