---
ciclo: dev
---

# Il marcatore delle attese a finestra nel plan

Inciso in `kb/plan.md` (2026-08-22): `Dip.` descrive da cosa dipende un task,
non come si comporta il costo del ritardo, e i comportamenti sono tre. L'attesa
**piatta** non costa, l'attesa **onerosa** costa in modo crescente ma resta
recuperabile, l'attesa **a finestra** non incarisce — può chiudere l'opzione. Le
prime due erano già governate da `## Scadenze`; la terza era invisibile per
costruzione, perché la sua caratteristica è di non avere una data calcolabile
su cui un controllo per distanza temporale possa allertare.

Il canone aggiunge un `!` appeso all'indice (`w2!`): **deperibile, non
urgente** — distinzione che inverte la lettura normale della coda, perché una
finestra con mesi davanti può meritare presidio più di una scadenza già
passata. Si marca solo ciò la cui chiusura non ha ancora una data e su cui non
c'è ancora una mossa in agenda; appena l'azione entra in agenda, la data
sostituisce il marcatore, che si toglie — un plan senza `!` perché ogni
finestra è presidiata è sano, non smemorato. La chiosa dichiara causa,
risveglio, cosa chiude la finestra e **cosa resta se si chiude**: è il secondo
campo a trasformare l'ansia in una decisione dichiarata.

Contestualmente rinominati gli indici di dipendenza esterna: `world`/`pause`
diventano `w<n>`/`p<n>` (lettera = chi tiene il tempo, numero = indirizzo della
legenda, riassegnato a ogni revisione). `o1/plan.md` è stato migrato nello
stesso commit (`pause [a]` → `p1`).

Verdetto corrente: canone inciso, nessuna istanza reale ha ancora prodotto un
`!` (l'unica attesa aperta in `o1/plan.md`, la rivalutazione skill-per-arco, ha
una data nota ed è quindi un `pause` semplice, non una finestra). Il filo resta
aperto fino al primo caso reale che eserciti il marcatore — verifica se la
distinzione deperibile/urgente regge sotto pressione e se il controllo scadenze
dell'adottante (che deve stampare le righe marcate senza condizione di
distanza) è stato recepito.
