---
stato: bozza
---

# Development goal

Il polo Goal del **ciclo di sviluppo** (Goal-dev, cfr. `development-meta-cycle`) non è solo contenuto di dominio: condivide **dimensioni comuni a tutti gli artefatti**, e ogni progetto _fotografa_ — più che «definisce» — la propria **posizione auspicata** lungo quelle dimensioni. Il dominio non determina le dimensioni: determina la **gradualità** scelta su ciascuna. È la generalizzazione che mancava al polo, e la cui assenza lo teneva sotto-articolato — la cella Goal-dev declassata a D in `action-cycle-matrix`, mescolata col Goal runtime perché il contenuto dev-specifico non era formulato da nessuna parte.

## Perché le dimensioni guardano il runtime

La cucitura tra runtime cycle e development meta-cycle spiega la natura di questo polo: poiché il **Mondo-dev è la macchina del runtime** (`development-meta-cycle`), gli obiettivi del ciclo di sviluppo sono in larga parte **desiderata sulla forma del ciclo runtime**. Il Goal-dev è dunque il luogo dove vivono le richieste su come il runtime debba comportarsi — il che spiega perché «portabilità» suoni di runtime pur essendo _voluta dallo_ sviluppo.

Da qui si scioglie lo split lasciato provvisorio dal gate. Il **Goal-runtime** raccoglie gli obiettivi _costitutivi_ del runtime — ciò per cui l'artefatto in opera esiste (per `salute`, stare bene; per `metodo`, portabilità, indipendenza dal modello, adattabilità, autocorrezione, rigore delle fonti, pavimento teorico). Il **Goal-dev** raccoglie la _posizione auspicata_ lungo le dimensioni comuni: non _cosa_ il runtime persegue, ma _con quale forma_ lo persegue. I due poli sono entrambi rivolti al runtime — è la cucitura a renderli tali — ma uno tiene lo scopo, l'altro la forma; ed è la forma il contenuto dev-specifico che il polo Goal-dev articola.

## Le dimensioni comuni

Tre dimensioni candidate, emerse dalla riflessione sui cinque artefatti e da raffinare con l'uso — non un'ontologia chiusa:

- **attrito / fluidità** — quanto il ciclo scorre senza gulf of execution o di evaluation; quanto poco l'artefatto frappone tra intenzione e atto, e tra esito e significato.
- **autonomia dell'umano** — umano _in-the-loop_ (dentro ogni iterazione) contro _on-the-loop_ (a supervisione); è lo stesso spettro di delegabilità di `goal` (motivo codificabile contro motivo non esternalizzabile).
- **temporalità del loop** — se il ciclo runtime sia un loop o un atto episodico, e con quale cadenza.

Le tre paiono raggrupparsi in **due famiglie**, da verificare: la **chiusura/attrito** del ciclo (i golfi) e l'**autonomia/automazione** (la posizione dell'umano insieme alla temporalità). La prima misura quanto il ciclo è liscio; la seconda quanto può girare senza la mano umana dentro ogni giro.

## Define contro photograph: il golfo a scala macro

Il polo Goal è la **posizione auspicata** — il punto-bersaglio nello spazio delle dimensioni, dove l'artefatto _vuole_ stare. Il riempimento del ciclo nella matrice (`action-cycle-matrix`) è la **fotografia dello stato attuale**. La **distanza** tra i due è il gulf of execution a scala macro che il ciclo di sviluppo lavora a chiudere: non la distanza di un singolo atto, ma quella dell'intero artefatto dalla forma che si è dato come bersaglio. Il Goal-dev dichiara dove si vuole essere, la matrice fotografa dove si è, e lo sviluppo è il lavoro che accorcia quella distanza.

## Il punto asintotico: l'artefatto invisibile

Le due famiglie hanno un punto di fuga comune. Un artefatto che matura tende a:
coda dev → **vuota** (nessun task una-tantum: la macchina ha la forma giusta e
non chiede interventi), runtime → **ricorrente e schedulato** (il battito va da
solo, umano _on-the-loop_). Il telos è l'**artefatto invisibile** — fa
funzionare i suoi goal senza disturbare — eco di Weiser («le tecnologie più
profonde sono quelle che scompaiono», 1991) e dello strumento trasparente.

Due precisazioni lo tengono onesto. È un **asintoto, non un bersaglio
obbligato**: la gradualità resta di dominio — dove il Goal-runtime vuole l'umano
dentro il giro per costituzione (`salute`: il motivo non è esternalizzabile),
l'invisibilità si declina come attrito zero della macchina, non come assenza
dell'umano. E misura la **macchina**, non lo scopo: un artefatto invisibile con
goal sbagliati è solo un errore che gira da solo.

La sua firma è leggibile nel plan dell'adottante: la **composizione delle code**
— la tabella dev che si svuota, il battito ricorrente in `## Scadenze` o nella
config versionata dello scheduler (cfr. `plan`, `skill`) — è la fotografia della
distanza dal telos. È la metrica candidata per il protocollo runtime-o1 di
`metodo` (l'audit periodico misura la maturità, non prescrive la coda).

## Fotografie per artefatto

Le posizioni auspicate dei cinque sull'asse autonomia/temporalità — la gradualità è di dominio, le dimensioni no:

- `salute`: loop quotidiano, umano profondamente _in-the-loop_ — il motivo non è esternalizzabile, la supervisione è permanente.
- `bi`: sync schedulato, umano _on-the-loop_ (monitoraggio) — il più automatizzabile dei cinque.
- `nixos`: episodico, set-and-review — non un loop a cadenza fissa.
- `economia`: decisioni episodiche, umano _in-the-loop_ — poste alte, supervisione richiesta.
- `metodo`: event-driven sul segnale dell'adottante, umano _in-the-loop_.

Riempire la posizione auspicata _di ciascun adottante_ resta lavoro suo: `metodo` dà le dimensioni comuni, non la fotografia altrui. La fotografia ha ora una **casa dichiarata**: la sezione «Goal di sviluppo» del register root `goal.md` dell'adottante (cfr. `goal`) — la prima istanza è nata in `bi` insieme al register stesso. È teoria dall'alto, ancorata a un disagio reale (la cella Goal-dev mal-filed) e tenuta dalla guardia dal-basso contro la sovra-ingegnerizzazione (`method-development`): le dimensioni restano candidate finché l'uso non le conferma.

Connessioni:

- [goal](goal.md)
- [action-cycle](action-cycle.md)
- [development-meta-cycle](development-meta-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [method-development](method-development.md)
- [plan](plan.md)
- [skill](skill.md)
- [world](world.md)
