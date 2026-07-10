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

Claim falsificabile: la perdita è **strutturale, non accidentale** — si addensa sui
nodi-strumento con sezioni per-adottante, dove stabilizzazione locale e modifica del
canone collassano nello stesso atto; se ricapita, dovrebbe ricapitare lì. Stato: la
riga `kb-tools` è ratificata come generalizzata (l'**oggetto-prova** della cucitura);
il nodo dedicato resta **in riserva** — un solo episodio non fa struttura.
L'enforcement è **dichiarato, non presidiato**: l'unico presidio è l'agente adottante
che si accorge e si ferma (come `bi`); il buco — un write-through che passa
inosservato — è tracciato dal task `enforcement-cucitura-canone` (`bozza`, trattenuto
`pause`). Un secondo arco bottom-up — la riforma della forma di `plan.md` da
`economia`+`bi` — è nel frattempo passato per il **canale-perception** (i1→i2/i3),
confermando che la gamba runtime→dev funziona senza mettere alla prova il presidio
specifico del write-through.
