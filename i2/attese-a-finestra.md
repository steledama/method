---
ciclo: runtime
---

# Il marcatore delle attese a finestra non è mai stato esercitato

Dal 2026-08-22 `kb/plan.md` distingue tre comportamenti dell'attesa: piatta,
onerosa e **a finestra**, quella che non incarisce ma può chiudere
l'opzione. Per renderla visibile l'indice di dipendenza porta un `!`
(`w2!`): deperibile, non urgente. Il filo che la presidiava si è chiuso
nella potatura `5ea8204` del 2026-10-02 e la regola è rimasta nel nodo, che è
`stato: maturo` per le sue altre funzioni. Non è rimasta invece la verifica
che il filo attendeva: il primo caso reale che eserciti il marcatore.

## Misura

Il 2026-10-05, sulla storia di `o1/plan.md` dei sette adottanti, nessun
commit introduce un indice nella forma `w<n>!` o `p<n>!` (ricerca `git log
-G'[wp][0-9]+!'`). In sei settimane il marcatore non è comparso una volta.

## Letture possibili

- nei domini attuali non ci sono attese a finestra senza data e senza mossa
  in agenda: la regola è corretta e semplicemente rara, come il nodo prevede
  («la rarità è ciò che lo fa funzionare»);
- le attese a finestra ci sono, ma chi scrive il plan non le riconosce come
  tali: finiscono in `## Scadenze` con una data inventata, oppure restano
  senza presidio.

Il conteggio non distingue le due letture. Le distingue la rilettura delle
dipendenze `w<n>` aperte negli adottanti, chiedendo per ciascuna se la sua
chiusura ha una data calcolabile e che cosa resta se l'opzione si chiude.
`economia` è il candidato naturale: controparti e decadenze sono il suo
dominio.

## Che cosa ne dipende

La maturità di `kb/plan.md` non dice nulla su questa parte del nodo. Finché
manca un caso reale, la distinzione deperibile/urgente è un'ipotesi incisa,
non una regola provata sotto pressione. Il riesame spetta al battito
`/adottanti` o a un segnale i1 da un adottante che incontri una finestra.
