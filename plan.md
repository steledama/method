# Plan

Lo stadio Plan del ciclo di sviluppo: i task aperti, in **ordine di esecuzione**,
con priorità e dipendenze. La conoscenza stabile vive in `kb/`; qui restano solo
i task e il loro stato di pianificazione.

## Task

| #   | Task                                            | Dip. |
| --- | ----------------------------------------------- | ---- |
| 1   | Strato di presentazione trasversale (deck→view) | —    |
| 2   | System image visiva: la home dell'atrio         | #1   |

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
11 S, 4 D, 1 vuoto). Restano i tre task **implementativi**.

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
`prescriptions/`, la storia resta in Git. Restano i due task implementativi: la
**presentazione (#1)**, ora sbloccata — il rename deck→view propaga a costo quasi
nullo perché i riferimenti accidentali sono già ripuliti — e la **home (#2)** dopo
presentazione, che consuma la mappa-sorgente del gate.

## Dettagli task

- [Strato di presentazione trasversale (deck→view)](tasks/strato-presentazione.md)
- [System image visiva: la home dell'atrio](tasks/system-image-visiva.md)
