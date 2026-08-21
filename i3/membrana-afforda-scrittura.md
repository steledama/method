---
ciclo: runtime
---

# La membrana `method/` afforda scrittura: agisci attraverso, ratifica in `method`

Emerso dal basso da `bi` (2026-06-23): stabilizzando `coverage --check` l'agente ha
modificato il nodo canonico `kb-tools` **via symlink** `method/`, accorgendosi poi che
l'edit non compariva nel diff del proprio commit (cattura i1 «modifica di canone
nata in un adottante», consumata e potata — storia in git). Il canone descriveva il
canale col suo **uso inteso** — gli adottanti «leggono i nodi» — non con la sua
**affordance**: il symlink è read-write, e afforda la scrittura (corretto in
`world.md`). Non è l'agente ad aver sbagliato: è il modello ad aver descritto la
membrana col suo uso inteso invece che con la sua affordance. La disciplina vive in
questo filo e in `world.md` finché un secondo write-through non chieda un atomo
proprio:

> **Agisci attraverso la membrana, ratifica in `method`.** Un agente che, risolvendo un
> problema in un adottante, modifica un nodo di canone via symlink compie un atto runtime
> legittimo: prosegue coi propri commit locali, ma _non committa l'edit di canone_ — lo
> segnala. `method` lo back-filla come perception e lo fa passare per i2/i3; solo allora
> l'edit diventa canone-di-record. **L'orfano non-committato nel working tree di `method`
> è la cucitura che funziona, non che fallisce.**

Il 2026-08-21 il caso si è ripetuto da `salute`: una revisione del suo README ha
lasciato modifiche dirette in tre nodi canonici (`readme`, `project-structure`,
`adopter-comparison`) e il custode ha rilevato a posteriori che non erano passate
da i1. Il secondo episodio allarga il punto di addensamento: non soltanto nodi-
strumento, ma nodi che descrivono lo stesso componente locale che l'agente sta
revisionando. Stabilizzazione locale e generalizzazione collassano nello stesso
atto proprio perché il symlink rende contigui i due piani.

Il claim strutturale è quindi corroborato e la condizione di risveglio del task
`enforcement-cucitura-canone` è avverata. L'enforcement resta per ora umano e
procedurale — questa sessione ha ricostruito i1→i2→i3 prima di ratificare il diff
— ma non può più essere descritto come sufficiente. Il task è attivo e deve
scegliere il presidio minimo capace di segnalare un working tree di `metodo`
modificato durante una sessione adottante prima che l'edit diventi canone-di-
record.
