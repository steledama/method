# verdict.md

Il verdetto attuale del progetto, per filo/area aperta — non un log. Il git log dice
_cosa_ è cambiato; questo file dice _come stanno le cose ora_ su ciascun filo
concettuale aperto, e _perché conta_. Specchio di `plan.md` sul lato valutazione:
`plan.md` fotografa i task aperti (o1), `verdict.md` i verdetti aperti (i3). Forma e
disciplina canoniche in [`kb/verdict.md`](kb/verdict.md).

Ogni gruppo `##` è un filo aperto; il corpo è lo **stato attuale**, aggiornato in
place, non una sequenza di entry datate (la cronologia di un filo è il git history di
questo file stesso). Quando un filo si chiude — verdetto stabile, nessuna tensione
aperta — il gruppo si rimuove: la storia resta in git. Il commit citato inline è il
puntatore alla storia verificabile.

---

## De-cablaggio del binomio «due agenti»: la seconda metà resta bottom-up

Il metodo era nato descrivendo due agenti — l'umano e un singolo LLM — e su quel
binomio aveva cablato la sua asimmetria come se fosse _la_ struttura. La prima metà
della correzione è fatta, e **additiva**: il nodo `agent` riconosce il binomio come
**caso saliente** di una popolazione più ampia (Norman: «person, animal, or machine»;
la categoria macchina è un gradiente, non un punto), e `system-image`,
`cognitive-system`, `knowledge-base` sono ammorbiditi senza cancellare il caso
umano/LLM — resta vero _come caso_, ed è l'unico in uso a valle. La seconda metà —
maturazione di `agent`, biforcazione di o1 per capacità dell'agente, asse
fiducia/privacy, divisione per stadio del ciclo — resta **deliberatamente non
scritta**: attende che un secondo livello di agente entri nell'uso reale. Scriverla
ora sarebbe inventare struttura prima dell'evidenza, l'opposto di come il metodo si
sviluppa.

## Maturazione dei nodi fondativi e falsificatori in attesa di uso reale

La rifondazione ontologica (artefatto/sistema/metodo) e l'arco di input hanno dato al
metodo il vocabolario che gli mancava e **nessun debito di fonte resta aperto**:
Leontiev (per `goal`), Hutchins e il filone mente-estesa (Clark) per
`cognitive-system`, e _Things That Make Us Smart_ (Norman 1993) sono reperiti, sorzati
e distillati nelle destinazioni i3 — chirurgia del 2026-06-21, incluso il nodo nuovo
`augmentation-system` (la cornice H-LAM/T che li contiene). Restano aperti solo i
verdetti che **attendono l'uso reale**:

- la maturazione `bozza→maturo` dei nodi fondativi: `cognitive-artifact`,
  `cognitive-system`, `goal`, `output`, `agent`, `affordance-signifier`,
  `system-image`, `processing-layers`;
- `kb-content-typology` (`bozza`): ha retto contro lo stato reale di `salute`
  (validazione parziale — i quattro adottanti sono plasmati dal metodo); il test
  esterno vero resta un repo nato senza;
- l'esito «zero forzati» della matrice del ciclo (`action-cycle-matrix`), provvisorio
  finché non testato su un repo nato senza il metodo;
- il check `[FACET]`/`EXTENDED_FACETS` in `kb_tools` (meccanismo di estensione del
  frontmatter col criterio dei quattro requisiti, inciso in `kb/node.md`): chiuso sul
  lato `method`, attende come falsificatore-da-implementazione il primo giro reale di
  un adottante (`nixos` Fase 4 con `mondo:` required, `economia` con `tipo:`
  opzionale).

## La home a 16 slot: tensione con `action-cycle-matrix` e propagazione aperta

Il cluster di presentazione è esaurito (deck→`view`, `assets/`+`views/`
materializzati, home rifatta 2026-06-30 come matrice annidata a 16 slot con switch
dev/runtime; motore condiviso in `tools/build_system_image.py`, gli adottanti forkano
la sola CONFIG). Due code aperte:

- **Tensione col nodo `action-cycle-matrix`**: il nodo tiene il frame a 16 celle come
  dogfooding di solo `metodo` (adottanti al ciclo singolo) e una scala a cinque valori
  col «vuoto legittimamente assente»; la home adotta invece il frame a 16 per tutti e
  una regola **binaria** acceso/dimesso che non rende la scala analitica. Da
  riconciliare: o la home è solo affordance di navigazione (la scala resta lo
  strumento del nodo, distinto), oppure la scelta «16 per tutti» risale nel nodo.
- **Propagazione agli adottanti** (forkare motore + CONFIG): canale o3-runtime, non
  ancora pianificato.

Fili parcheggiati dello stesso fronte: la colonna di `plan` per classificare i task su
due assi ortogonali — ciclo (sviluppo/runtime) × natura (metodologico/merito); l'omologia
esplicita tools=o3-sviluppo / scripts=o3-runtime / skill=prescrizioni narrative;
l'eventuale uniformità totale degli indici col suo costo (rinomina del nodo `index`,
split del catalogo `tools`). Fuori orizzonte, deliberatamente: i task come slide
navigabili e la finestra-terminale per dialogare col modello (rompe l'invariante
`file://`, sarà classe e nodo a sé). Il gap **runtime-o1** — il protocollo d'audit
periodico top-down — è un task in `plan.md`, non più un TODO di questo filo.

## La membrana `method/` afforda scrittura: agisci attraverso, ratifica in `method`

Emerso dal basso da `bi` (2026-06-23): stabilizzando `coverage --check` l'agente ha
modificato il nodo canonico `kb-tools` **via symlink** `method/`, accorgendosi poi che
l'edit non compariva nel diff del proprio commit (cattura i1 in
`perceptions/modifica-di-canone-nata-in-un-adottante.md`). Il canone descriveva il
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
