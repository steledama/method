# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                                            | Dip. |
| --- | --------------------------------------------------------------- | ---- |
| 1   | Cicli annidati: modello dei poli (i3) + diagramma rifatto       | —    |
| 2   | Frecce del ciclo d'azione visibili (home + deck)                | —    |
| 3   | Slide «Sviluppo del metodo»: bottom-up → generalizza → top-down | —    |
| 4   | Coerenza slide post system-image + rimozione «Approfondimento»  | 1    |
| 5   | Protocollo runtime-o1 (audit periodico top-down)                | —    |

Apertura 2026-06-22: una **revisione i2-macro dello strato di presentazione**. Il
deck (`interpretations/metodo-in-sintesi.md`) è l'i2-macro del metodo su sé stesso;
riletto alla luce del task system-image (il _system image_ è l'artefatto, non la
KB), slide e home non rappresentano più fedelmente il modello. **Disciplina**
(cfr. il deck stesso e `cognitive-fidelity`): il deck rivela, i nodi risolvono —
ciò che è **modello** si chiude prima nei nodi (i3), poi il deck si **ri-deriva**;
ciò che è **resa** (CSS, layout) si corregge nello strato `view`. È il percorso
i2 → i3 → o1 che, oltre a ripulire la presentazione, rifila come o1 il gap
strutturale runtime-o1 (task 5).

Note di rotta:

- **Task 1** porta una decisione di modello aperta: `nested-cycles` oggi dice
  **4 poli** (una coppia Goal/Mondo per ciclo, l'artefatto = fondo-dev _e_ macchina
  del runtime), mentre il diagramma andrebbe verso **3 poli impilati** (Goal ·
  Artefatto · World). Va sciolta nel nodo (i3) prima di ridisegnare. Il nodo già
  **vieta** la rappresentazione a due colonne alla pari (§«La cucitura, non
  l'affiancamento») che il deck attuale usa, e impone di mostrare la cucitura.
- **Task 5** è il gap che il filo «cicli annidati» di `verdict.md` portava come
  TODO appeso a un gate chiuso: l'arco top-down è scoccato una volta (prescrizione
  baricentro → `method-review` → recepimento) ma manca il protocollo d'audit
  periodico. Dipende dalla maturazione dell'osservatorio (i2/o2-runtime, oggi una
  sola istanza); la lama è audit ≠ micromanagement della coda adottante.

Il **gate dei cicli annidati è chiuso** (ratificato a freddo, 2026-06-21, cfr.
`verdict.md` e `kb/action-cycle-matrix.md`): l'annidamento regge — due cicli
genuini, con l'interno runtime **nascente** (l'osservatorio sugli adottanti è
i2/o2-runtime, una sola istanza; runtime-o1 il gap top-down, scoccato una volta
ma senza protocollo d'audit). La mappa-sorgente dei 16 elementi è prodotta e
ri-sorgentata a freddo: è ciò che la presentazione e la home consumano.

La **chirurgia dei giganti** è **chiusa** (2026-06-21): il nodo nuovo
`augmentation-system` (la cornice H-LAM/T di Engelbart) è scritto, gli hub
`action-cycle`, `karpathy-pattern`, `cognitive-system`, `cognitive-artifact`,
`processing-layers`, `affordance-signifier`, `knowledge-base`,
`cognitive-artifact-design`, `nested-cycles`, `zettelkasten`, `method-development`
e il `README` sono allineati in una passata sola — Engelbart come cornice di
sistema che contiene i giganti, Karpathy ricondotto a istanza, il pavimento
Hutchins/Clark/Norman promosso, la revisione di «non orchestra» incisa. Audit
pulito (48 nodi, 0 link rotti). Resta aperta solo la maturazione `bozza→maturo`
dei nodi fondativi, che attende l'uso reale (cfr. `verdict.md`, «Maturazione dei
nodi fondativi»).

Il **fronte fondativo è chiuso**: la chirurgia dei giganti e il **Goal di sviluppo**
(nodo `development-goal`, 2026-06-21) hanno articolato il polo Goal-dev — dimensioni
comuni e posizione auspicata — sciogliendo lo split Goal-dev/Goal-runtime lasciato
provvisorio dal gate; la cella Goal-dev risale da D a S in `action-cycle-matrix` (ora
11 S, 4 D, 1 vuoto).

**Guardrail**, da non perdere: teoria-prima valeva _in quella fase_, non come regola
permanente. Il dal-basso resta la guardia contro la sovra-ingegnerizzazione
(`method-development`), e l'implementazione resta il _falsificatore_ della teoria
(`action-cycle-matrix`); ora che le fondamenta sono posate l'implementazione torna a
fare da prova.

Sul fronte implementativo: il **disaccoppiamento è chiuso** (2026-06-21). Il
principio «dichiara e taci» è inciso in `method-development` (il confine
canone↔adottante: dipendenza generale / intenzionale / accidentale); la sezione
README canonica è formalizzata in `kb/readme.md` (heading fissi `## Metodo` ·
`### Goal` · `### World`, World esplicito mai euristico) ed esposta da tutti e
cinque i README. Il round 1 della propagazione è **recepito dai quattro
adottanti** via il loro `method-review` (`nixos`, `bi`, poi `salute` in `dcb08dc`
e `economia` in `22e22ca`); la prescrizione esaurita è rimossa da
`prescriptions/`, la storia resta in Git. Lo **strato di presentazione** è
chiuso: `deck` è stato scisso in `view`, `assets/` e `views/` sono materializzati,
le viste `interpretations`, `tasks` e `verdict` sono generate e versionate. Anche la
**home della system image** è chiusa: `index.html` è generato, statico, offline e
consuma README, Plan e le viste. Il cluster implementativo aperto dal gate è
esaurito.

Il **task fondativo-terminologico è chiuso** (2026-06-22): il _system image_ è
unificato sull'**artefatto** — la KB ne è il nucleo di conoscenza formalizzata, non
il sinonimo. La tesi ratificata rovescia la metà «KB-come-system-image-trasversale»
della vecchia dottrina dei «due framework»: è l'artefatto a essere il medium interno
trasversale ai tre livelli, la KB la sua regione alta/formalizzata (riceve solo
i2/i3; gli altri stadi depositano fuori da `kb/`). Verifica a supporto della tesi.
Propagato in una passata: i tre titolari (`system-image`, `cognitive-system`,
`action-cycle`), la cautela (`knowledge-base`, `output`, `input`) e i cinque emersi
dal grep (`processing-layers`, `project-structure`, `kb-content-typology`,
`cognitive-artifact-design`, `karpathy-pattern`), più la coda `index`. Gli archi del
ciclo tornano a correre tra Goal e Mondo (non «dalla/alla KB»). Audit pulito (49
nodi, 0 link rotti).

## Dettagli task

- [Cicli annidati: modello dei poli + diagramma](tasks/cicli-annidati-modello.md) — task 1
- [Revisione i2 della presentazione](tasks/presentazione-i2.md) — task 2, 3, 4
- [Protocollo runtime-o1](tasks/protocollo-runtime-o1.md) — task 5
