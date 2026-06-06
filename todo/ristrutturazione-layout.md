---
data: 2026-06-06
stato: aperto
---

# Ristrutturazione del layout — disegno unico, migrazione atomica

Documento di disegno della riorganizzazione del top level del repo (e dei 4 adottanti). Consolida
e sostituisce `rinomina-log-why`. Regola di lavoro: **niente file di contenuto si tocca finché il
disegno non è approvato**; poi una sola migrazione lo realizza sui 5 repo in un colpo, per pagare
la propagazione una volta sola.

## Policy linguistica (fissata il 2026-06-06)

Il repo migra all'inglese per gradi: **forma in inglese, contenuto in italiano** finché il metodo
non cristallizza, poi inglese integrale. Forma = cartelle, file pilastro, file-meta, nomi
strutturali. Contenuto = i nodi e la prosa di dominio. Conseguenza-segnale utile: l'inglese marca
l'artefatto strutturale *vivo*, l'italiano la *documentazione* concettuale (es. `kb/index.md` vivo
vs `kb/indice.md` nodo-concetto). Aggiunge `presentazione/ → presentation/` allo sweep.

## Principio guida — la triade (da fissare in [[struttura-progetto]] dentro la migrazione)

1. **Root = artefatti bootstrap-essenziali di livello-progetto**, letti per capire *il tutto* a
   prescindere dalla pace. Il root è il **cruscotto del ciclo di sviluppo** (quello che agisce
   sull'artefatto, non sul mondo): README (Goal), `map`
   (modello), `plan` (Plan: prossime azioni), CLAUDE/AGENTS (regole), `why` (memoria di valutazione).
   `plan` e `why` stanno in root pur essendo veloci: la loro **altezza nel ciclo vince sulla pace**.
2. **Cartelle = collezioni di unità atomiche.** Una cartella ha un file-meta *dentro di sé* solo se
   il suo catalogo si consulta on-demand (`kb/index.md`). Se il meta si legge a ogni sessione, sale
   in root (è il caso di `plan`, meta-istanza dei task, sollevato dall'altezza).
3. **Pace = criterio di compagnia, non di profondità.** Decide cosa non fondere in un solo file.
   Quando altezza e pace confliggono, l'altezza decide la collocazione, la pace decide che resti un
   file separato.
4. **Root estensibile (dal basso).** Il set universale (README/map/plan/CLAUDE/AGENTS/why) è un
   *pavimento, non un soffitto*: un dominio aggiunge i propri file bootstrap-essenziali — economia
   `stato.md`/`scadenze.md`, salute `scadenze.md`/`diario.md` — con lo stesso criterio di altezza.

Sostituisce «più in alto = più stabile», già demolita da [[pace-layering]]. Il principio stesso è
applicazione di [[sviluppo-metodo]]: cornice dall'alto (Norman) verificata dal basso (le root reali).

**Nota — il cruscotto è il ciclo di *sviluppo*, e non è simmetrico a sette caselle.** `plan` è il
Plan dello sviluppo, **non** o1 (il Plan del runtime): distinzione da fissare in [[struttura-progetto]]
per non creare una contraddizione `plan`/o1 tra nodi. Il lato esecuzione sono *intenzioni scritte*
(Goal/Plan → file a root); il lato valutazione sono *operazioni* (audit, [[fedelta-cognitiva]]) il
cui residuo rientra in `why` e nei nodi. Il Compare (i3 in [[ciclo-azione]]) non vuole un
`compare.md`: quando si cristallizza è l'**o2/termometro** (quadro, stato.md, la presentazione) nello
strato output — vista generata, non intenzione.

## Verifica dal basso (root dei 4 progetti, 2026-06-06)

La triade regge contro i progetti reali e ne esce arricchita (il punto 4 è emerso proprio qui):
- universali presenti ovunque: README, CLAUDE, AGENTS, log(→why), kb/, scripts/, todo/(→tasks/);
- **strato output**, già nominato dal metodo, con nome locale: `output/` (economia), `quadro/`
  (salute), `presentazione/` (bi, metodo) — è l'o-layer, né pilastro né collezione kb;
- **file bootstrap di dominio in root**: `stato.md`, `scadenze.md`, `diario.md` — esigenze dal
  basso, inquadrate dal punto 4 come estensioni domain-specific;
- il **"mondo" del dominio** (nixos: home/hosts/modules; economia: src/data/config; bi: src/test) è
  ciò su cui il ciclo agisce: fuori dalla competenza-layout del metodo;
- da guardare a parte: `memory/` in economia (possibile residuo dello store harness, anti-pattern
  per il suo stesso CLAUDE).

## Layout target (metodo)

```
ROOT  — cruscotto del ciclo dell'azione, letto a ogni sessione
  README.md   Goal: identità, principi, motivazioni; punta a map.md e kb/
  map.md      il modello del dominio (vista o2, separata dal README per tenerlo conciso)
  plan.md     Plan: i task aperti prioritizzati con dipendenze (ex tabella README / task-aperti)
  CLAUDE.md   regole operative
  AGENTS.md   wrapper agent-agnostico
  why.md      (ex log.md) memoria del perché, append-only
  + (nei domini) file bootstrap locali: stato.md, scadenze.md, diario.md, ...
kb/    nodi (unità atomiche) + index.md (catalogo, consultato on-demand)
tasks/ (ex todo/) i dettagli operativi dei task (stadio Specify), indicizzati da plan.md
scripts/ · presentation/ (ex presentazione/) · .claude/skills/ · .codex/skills/
```

## Cosa cambia, voce per voce

- **README**: esce l'indice dei nodi, esce la tabella task; resta lo strato lento (identità,
  principi, progetti adottanti, come collegare) e *punta* a `map.md`, `plan.md`, `kb/index.md`.
- **mappa**: artefatto root separato `map.md` (vista o2, non inline, per tenere conciso il README
  auto-caricato). Mantiene il passo di bootstrap `README → map → CLAUDE → nodo` già nel metodo.
- **lista task → `plan.md` in root**: la meta-istanza dei task sale dall'altezza del ciclo (Plan,
  primo file letto a sessione). `tasks/` resta solo i dettagli.
- **`log.md` → `why.md`**: rinomina + nuovo modello di entry (chiave = la decisione, data come
  metadato, commit citabile inline come puntatore).
- **`todo/` → `tasks/`**: allinea al vocabolario del metodo.
- **`presentazione/` → `presentation/`**: policy linguistica.
- **catalogo dei nodi → `kb/index.md`** dentro la cartella (on-demand).

## Micro-decisioni

- **M1 — `kb/index.md`** (register, inglese-vivo); il nodo-concetto resta `kb/indice.md` (italiano,
  doc): la coesistenza è il significante vivo/doc della policy linguistica. *Ratificato il 2026-06-06.*
- **M2 — risolta**: niente file-meta in `tasks/`; la lista-Plan sale in root come `plan.md`.
- **M3 — ratificato**: nome del nodo = nome del file; `why` non `memoria-interpretativa`. Dove
  l'istanza è root (`why.md`, `map.md`, `plan.md`) il nodo-concetto può condividere il nome inglese
  (path diverso): `log`→`why`, `mappa`→`map`, `task-aperti`→`plan`. Da rifinire in migrazione.
- **M4 — ratificato**: `--append-log` → `--append-why`, esclusione del file-meta dall'audit nodi,
  aggiornamento skill `audit-kb`.

## Piano di migrazione (atomico, una volta sola sui 5 repo)

1. (fatto) disegno approvato, M1–M4 e nomi ratificati il 2026-06-06;
2. nel repo `metodo`: rinomine file/cartelle, riscrittura referenze (~40), `map.md` e `plan.md` in
   root, `kb/index.md`, triade in [[struttura-progetto]], `kb_tools.py` e skill, diagrammi della
   presentazione;
3. nei 4 adottanti **nello stesso passaggio**: i nodi condivisi si propagano via symlink, ma
   istanze root (`log.md`→`why.md`, `todo/`→`tasks/`, lista→`plan.md`) e referenze in CLAUDE/README
   vanno rifatte a mano (caso «cambio nome/path di nodo» del `CLAUDE.md`); preservare la distinzione
   why/`diario.md`/`stato.md`/`scadenze.md`;
4. verifica: `kb_tools.py audit` su ogni repo + grep di `log\.md` e `todo/` residui sui 5 repo;
5. **prima entry di `why.md`**: il perché dell'intero ridisegno del layout — la fondazione del file
   scritta nel file che il ridisegno ha ribattezzato.

## Stato

Disegno chiuso il 2026-06-06: M1–M4, `plan.md` e i nomi sono ratificati. Il task è ora puramente
esecutivo — la prossima sessione esegue la migrazione atomica seguendo il piano qui sopra.
