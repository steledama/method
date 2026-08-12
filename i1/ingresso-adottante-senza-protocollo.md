---
ciclo: dev
---

# Segnale: l'ingresso di un adottante nel territorio non ha protocollo

Data: 2026-08-12 · Fonte: `metodo` stesso — ingresso di `crm` come quinto
adottante (commit `b9d01b5`), con un sesto (`danea-auto`) in valutazione lo
stesso giorno

## Il segnale

L'ingresso di `crm` nel territorio è costato una bonifica a mano su **nove
file** di `metodo`, sparsi su tutti e tre gli strati dell'artefatto: i due
register dei poli (`world.md` la voce e il conteggio, `goal.md` la fotografia
dell'obiettivo 2), la bussola e l'ingresso operativo (`README.md` in tre punti,
`CLAUDE.md`), quattro nodi `kb/` (`world`, `readme`, `adopter-comparison`,
`kb.md`), il plan (`o1/plan.md`, la riga di `## Scadenze`). Più due viste
rigenerate, di cui una era **stale** e lo si è scoperto solo perché il gate di
`/commit` esegue le build.

Nessuna procedura copre questa sequenza. Esiste `/adottanti` per il battito
mensile su un territorio **dato**, esiste `method` per il canale col canone di
un adottante **già dentro**, esiste `/commit` come gate. Il passaggio
«un artefatto diventa parte del territorio» non ha né skill né checklist: si
ricostruisce a memoria ogni volta, e ciò che si dimentica non rompe nulla —
resta solo un conteggio che mente.

Due fatti collaterali che il giro ha prodotto, e che sono la ragione per cui il
costo non è visibile a posteriori:

- il grosso della bonifica erano **conteggi in prosa** («i quattro adottanti»,
  «comune ai cinque repo»). Quattro occorrenze durevoli sono state rese
  count-free nello stesso giro, ma la distinzione tra conteggio durevole (da
  eliminare) e conteggio datato (da conservare come fotografia: le fonti dei
  recepimenti, gli snapshot di `adopter-comparison`, la sintesi
  `baricentro-kb-adottanti`) è stata fatta caso per caso, a giudizio;
- la voce nuova in `world.md` era formalmente divergente dalle quattro sorelle
  (nome maiuscolo, nessun link al remoto che pure esisteva) e la difformità è
  emersa **dalla vista rigenerata**, non dalla lettura del register: la home la
  rendeva come unico elemento non cliccabile della lista.

## Perché è catturato

Un solo ingresso è un caso, e il canone non si muove su un caso (cfr.
`registro-perpetuo-vs-cattura-singola`, `criterio-world-substrato`,
`de-cablaggio-binomio-due-agenti`: stesso pattern di attesa). Ma il secondo caso
è **annunciato** — `danea-auto` è in valutazione per il sesto ingresso — e a
quel punto la domanda non sarà più «quanti sono» ma «perché l'ingresso non ha
una procedura». La cattura esiste perché a quel giro il costo di questo giro
sia leggibile senza ricostruirlo dal `git log`: nove file, tre strati, una vista
stale scoperta per caso.

Valenza-neutro: qui non si giudica se serva una skill, un nodo, una riga di
checklist in `/commit` o nulla. Quella valutazione è i2→i3 al secondo segnale.

## Cosa resta fuori

La classificazione di `danea-auto` come specimen del test esterno — con la sua
convergenza indipendente datata, il limite di contaminazione dal custode e lo
stato pre-adozione `fb83c0d` — non è materia di questa cattura: vive nel filo
[maturazione-nodi-fondativi](../i3/maturazione-nodi-fondativi.md), dove il
falsificatore era già atteso. Un fatto per segnale.
