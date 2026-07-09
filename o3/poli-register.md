---
data: 2026-07-09
stato: attiva
ciclo: runtime
target: economia (pilot), bi, salute, nixos
---

# I poli del ciclo come register: `goal.md` e `world.md` arrivano agli adottanti

## Cosa e perché

Con la ratifica dei poli-register (2026-07-09, filo
`i3/poli-register-goal-world.md`) il canone descrive un atrio che nessun
adottante ha ancora per intero: i **register di root sono i due poli del
ciclo** — `goal.md` (il nord) gemello di `world.md` (il territorio) — e la
classe supera `map.md` e `sources.md`, entrambi assorbiti da `world.md`. Il
polo Goal esce dal README, che torna bussola pura; la home ricava i poli
dall'**intro dei register**, non più dalle sezioni `### Goal`/`### World`.
Insieme ai register arriva il **quartetto di review**: `plan-review` (rinomina
di `tasks-review`) e `verdicts-review` (nuova), la coppia simmetrica che
controlla la cerniera `goal.md` dai due versanti.

Il perché operativo è nato dal basso, in `bi`: i fili i3 dicevano «perché
conta» ma non «rispetto a quale obiettivo»; il plan ordinava per urgenza, non
per obiettivo servito; i loop delegati chiedevano un ancoraggio senza un posto
a cui agganciarlo; e nessuno rivedeva mai l'insieme dei fili, così la narrativa
di stato colava nel plan. Cfr. `goal` («Il register `goal.md`»), `world` («Il
register `world.md`», «Il criterio del significato senza artefatto»), `skill`
(quartetto), `readme` (sezione canonica), `project-structure` (classe
register), `verdict` (i due presìdi, annotazione `misura:`).

## La ricetta (nel lessico del metodo)

1. **Il register `goal.md` — il passo-cuore, e il suo contenuto lo porta il
   custode.** Crea `goal.md` in root (niente frontmatter, come ogni register):
   l'**intro** (dall'H1 al primo H2) è il motivo in sintesi — è ciò che la home
   renderà, quindi visione del polo, non membrana né pipeline; poi gli
   obiettivi di livello azione (albero basso, un livello), ognuno con i due
   aggetti — **segnali** che lo misurano (fili `i3/`, report, viste) e **lavoro
   corrente** che lo serve (righe di `o1/plan.md`, per titolo); una sezione
   «Goal di sviluppo» con la posizione auspicata sulle dimensioni comuni
   (`development-goal`); una sezione di disciplina col **custode umano
   dichiarato**. Un obiettivo a regime (segnali vivi, lavoro assente) resta
   visibile: è informazione. La prescrizione dà la forma; **il nord lo scrive
   il custode**, non l'agente — l'agente propone una bozza dai materiali
   esistenti (README §Goal, nodi di razionale, stato) e la fa ratificare.
2. **`map.md` → `world.md` — la fusione del polo basso.** L'indice-territorio
   locale (qualunque nome porti oggi: `map.md`, `mappa-progetto.md`, …) diventa
   la sezione **territorio** del nuovo register `world.md`; `sources.md`, dove
   esiste, ne diventa la sezione **fonti** (provenienza: quale edizione regge
   quale nodo); le **superfici della membrana** si dichiarano una volta
   (symlink o mount descrittivi — `gdrive/`, `client/`, sync, sistemi esterni —
   non un nome obbligato `world/`). L'**intro** è la visione del Mondo che
   l'artefatto tiene
   (tipicamente l'ex `### World` del README). La dimensione interna dell'ex
   mappa («dove vivono o1, o2, o3») non migra: è superata dall'atrio, che si
   auto-dichiara. Il criterio per i casi dubbi (membrana o substrato?) è il
   **test del significato senza artefatto** (`world`).
3. **README asciugato.** La sezione canonica diventa il solo `## Metodo`:
   dichiarazione di adozione, symlink `method/`, hub
   `cognitive-artifact-design.md`, puntatori ai due register. Via `### Goal` e
   `### World`; la legenda dell'atrio aggiorna la classe register
   (`goal.md`/`world.md` al posto di `map.md`/`sources.md`). Il README
   conserva l'identità in una riga: chi entra capisce perché il repo esiste
   senza aprire nulla.
4. **Builder della home.** Risincronizza il fork dall'`o3/` del metodo:
   `register_intro` (H1 → primo H2, in `presentation.py`) sostituisce
   `canonical_readme_section`; i due poli si leggono da `goal.md`/`world.md`
   invece che dal README. Il contratto di resa non cambia: builder stupido e
   fedele, markdown → HTML senza card né euristiche. Poi rigenera.
5. **Skill: il quartetto.** Rinomina `tasks-review` → `plan-review`
   (directory, frontmatter, wrapper Codex) e aggiungi la lente task→obiettivo
   verso `goal.md`; forka `verdicts-review` dal canonico (quattro domande per
   filo, copertura bidirezionale, bonifica del plan, formazione-goal in
   proposta) parametrizzandola sui segnali del dominio; aggiorna i riferimenti
   in `commit` e `method-review` locali. `bi` ha già la coppia: per lei questo
   passo è solo verifica di allineamento col canonico.
6. **Bussole e link al canone.** `CLAUDE.md`/`AGENTS.md`: register dei poli al
   posto dei vecchi register, quartetto nella lista skill. I riferimenti a
   `method/map.md` e `method/sources.md` sono **rotti per costruzione** (nodi
   eliminati dal canone): puntano ora a `method/world.md` e `method/goal.md`.
   L'annotazione `misura:` nelle voci di `i3/verdicts.md` (quale obiettivo del
   register il filo misura) è facoltativa ma raccomandata al primo giro.
7. **Verifica e chiusura.** `kb_tools.py audit` pulito, home e viste
   rigenerate, e il **primo giro della coppia**: `/plan-review` (ogni task
   serve un obiettivo del register?) e `/verdicts-review` (ogni obiettivo ha un
   segnale vivo? la narrativa di stato migra dal plan ai fili?). La migrazione
   chiude solo col commit locale (gate `/commit`); il marker `method-review.md`
   avanza dopo.

## Touchpoint per-repo (indizi da verificare in loco, non ordini)

- **`economia` — pilota recepito** (`74c56c6`, 2026-07-09; marker
  `method-review.md` a `3609404`): banco più severo superato. Il recepimento ha
  creato `goal.md`, fuso `map.md` in `world.md`, asciugato README/home,
  installato `plan-review`/`verdicts-review` anche nei wrapper Codex e rimosso
  `tasks-review`. Il primo giro della coppia ha inciso `misura:` in
  `i3/verdicts.md`: il plan resta coda e motivazione operativa delle attese,
  mentre la valutazione stabile passa ai fili. `scadenze.md` resta calendario
  di dominio: non è materia di questa prescrizione.
- **`bi`** — a metà strada, è l'**origine**: `goal.md`, `plan-review` e
  `verdicts-review` nati lì (`52b2b600`). Restano i passi 2-4 e 6: fondere
  `map.md` in `world.md` dichiarando le **due superfici** (client Syncthing +
  mount Drive foto, dal criterio world/substrato), asciugare il README,
  risincronizzare il builder. Il suo `goal.md` cita `map.md` come gemello:
  aggiornare il puntatore a `world.md`.
- **`salute`** — recepimento pieno; la mappa semantica (assi concettuali,
  fonti, pratica, diario) diventa la sezione territorio. `sources.md` era
  assente per divergenza dichiarata: `world.md` nasce con la sezione fonti solo
  se il custode decide di riassorbire quella divergenza — non è un obbligo del
  runbook. Il motivo («stare bene, equilibrio corpo-mente») è il meno
  esternalizzabile dei quattro: la disciplina del custode qui è il punto, non
  un dettaglio.
- **`nixos`** — recepimento pieno; l'indice host/profili/moduli diventa la
  sezione territorio. Il Goal porta i **due goal in tensione** (minimalismo vs
  affidabilità multi-host): il register li mostra entrambi coi rispettivi
  segnali (deriva dal minimalismo, replicabilità degli host) — la tensione è
  informazione, non un difetto da risolvere nel file.

## Ordine e chiusura

Pilot su `economia` completato: i suoi cocci sono incisi in questo runbook
prima degli altri recepimenti (come i cocci di `nixos` ed `economia` nella
prescrizione dell'atrio). Proseguire con `bi` (completamento), `salute` e
`nixos`. La prescrizione resta attiva finché i quattro non l'hanno recepita via
il proprio `method-review`; recepita da tutti, si rimuove dalla collezione e
chiude con lei il task di tracciamento (`o2/propagazione-poli-register.md`). La
storia resta in git.
