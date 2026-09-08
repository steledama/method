---
stato: bozza
---

# Development goal

Il polo Goal del **ciclo di sviluppo** (Goal-dev) descrive la forma auspicata
dell'artefatto. Il metodo propone dimensioni candidate comuni — attrito,
autonomia e temporalità — lungo cui ogni progetto dichiara la propria posizione
desiderata. L'uso deve verificarne applicabilità e sufficienza: il dominio
sceglie la gradualità e può mostrare che una dimensione manca o che una di
quelle proposte non discrimina casi utili.

## Perché le dimensioni guardano il runtime

La cucitura tra runtime cycle e development meta-cycle spiega la natura di
questo polo: poiché il **Mondo-dev è la macchina del runtime**
(`development-meta-cycle`), gli obiettivi del ciclo di sviluppo sono in larga
parte **desiderata sulla forma del ciclo runtime**. Il Goal-dev è dunque il
luogo dove vivono le richieste su come il runtime debba comportarsi — il che
spiega perché «portabilità» suoni di runtime pur essendo _voluta dallo_
sviluppo.

Il **Goal-runtime** raccoglie gli obiettivi _costitutivi_ del runtime — ciò per
cui l'artefatto in opera esiste. Il **Goal-dev** raccoglie la _posizione
auspicata_ lungo le dimensioni comuni: non _cosa_ il runtime persegue, ma _con
quale forma_ lo persegue. I due poli sono entrambi rivolti al runtime — è la
cucitura a renderli tali — ma uno tiene lo scopo, l'altro la forma; ed è la
forma il contenuto dev-specifico che il polo Goal-dev articola.

## Le dimensioni candidate

Tre dimensioni candidate emerse dal confronto tra adottanti — non un'ontologia
chiusa. Lo stato `bozza` del nodo segnala precisamente che l'uso deve ancora
confermare se siano sufficienti e se le due famiglie proposte sotto reggano:

- **attrito / fluidità** — quanto il ciclo scorre senza gulf of execution o di
  evaluation; quanto poco l'artefatto frappone tra intenzione e atto, e tra
  esito e significato.
- **autonomia dell'umano** — umano _in-the-loop_ (dentro ogni iterazione) contro
  _on-the-loop_ (a supervisione); è lo stesso spettro di delegabilità di `goal`
  (motivo codificabile contro motivo non esternalizzabile).
- **temporalità del loop** — se il ciclo runtime sia un loop o un atto
  episodico, e con quale cadenza.

Le tre paiono raggrupparsi in **due famiglie**, da verificare: la
**chiusura/attrito** del ciclo (i golfi) e l'**autonomia/automazione** (la
posizione dell'umano insieme alla temporalità). La prima misura quanto il ciclo
è liscio; la seconda quanto può girare senza la mano umana dentro ogni giro.

## Define contro photograph: il golfo a scala macro

Il polo Goal è la **posizione auspicata** — il punto-bersaglio nello spazio
delle dimensioni, dove l'artefatto _vuole_ stare. Il riempimento del ciclo nella
matrice (`action-cycle-matrix`) è la **fotografia dello stato attuale**. La
**distanza** tra i due è il gulf of execution a scala macro che il ciclo di
sviluppo lavora a chiudere: non la distanza di un singolo atto, ma quella
dell'intero artefatto dalla forma che si è dato come bersaglio. Il Goal-dev
dichiara dove si vuole essere, la matrice fotografa dove si è, e lo sviluppo è
il lavoro che accorcia quella distanza.

## Il punto asintotico: l'artefatto invisibile

Per un runtime delegabile, il metodo propone un punto di fuga: meno lavoro dev
correttivo e un battito che richiede meno interventi manuali. È il telos
candidato dell'**artefatto invisibile** — sostiene i goal senza aggiungere
attrito — accostato all'idea di Weiser delle tecnologie che si integrano nella
pratica fino a sottrarsi all'attenzione (1991).

Due precisazioni lo tengono onesto. È un **asintoto, non un bersaglio
obbligato**: la gradualità resta di dominio — dove il Goal-runtime vuole l'umano
dentro il giro perché il motivo non è esternalizzabile, l'invisibilità si
declina come attrito zero della macchina, non come assenza dell'umano. E misura
la **macchina**, non lo scopo: un artefatto invisibile con goal sbagliati è solo
un errore che gira da solo.

La **composizione delle code** è un indizio candidato: tabella dev che si svuota
e runtime ricorrente possono segnalare minore attrito. Non bastano a misurare la
maturità. Una coda vuota può anche indicare abbandono o problemi non percepiti;
un nuovo task dev può essere la risposta sana a un dominio che cambia. La
lettura va accompagnata da esiti runtime, segnali aggiornati e copertura degli
obiettivi. Cadenza e scheduler sono fonti del battito, non prove della sua
efficacia (`plan`, `skill`).

## Gradualità di dominio e casa della fotografia

Le posizioni auspicate si confrontano lungo le dimensioni candidate, senza
forzare il dominio ad adottare una forma unica. Due contrasti ne mostrano l'uso.
Dove il motivo non è esternalizzabile la supervisione è permanente per
costituzione — il loop è quotidiano e l'umano resta profondamente _in-the-loop_.
Dove il motivo è codificabile l'umano si sposta _on-the-loop_ e sorveglia un
battito schedulato che gira da solo. Tra i due estremi stanno i cicli episodici,
che non hanno cadenza fissa ma si aprono su un evento: un set-and-review di
configurazione, una decisione a posta alta, il segnale di un adottante.

Riempire la posizione auspicata _di ciascun adottante_ resta lavoro suo:
`metodo` propone le dimensioni comuni, non la fotografia altrui — tenerne qui un
elenco sarebbe la seconda rappresentazione che deriva in silenzio. La fotografia
ha una **casa dichiarata**: la sezione «Goal di sviluppo» del register root
`goal.md` dell'adottante (cfr. `goal-register`). Le dimensioni restano candidate
finché l'uso nei domini non ne conferma sufficienza e confini.

## Riferimenti

- Mark Weiser, «The Computer for the 21st Century» (1991), apertura della bozza
  d'autore dopo l'editing di _Scientific American_, disponibile nella copia
  ospitata da UC Irvine. Sostiene l'idea di tecnologie integrate nella pratica
  fino a sottrarsi all'attenzione; l'applicazione a code e cicli del metodo è
  una proposta locale. Provenienza nel register `world.md`.

Connessioni:

- [goal](goal.md)
- [goal-register](goal-register.md)
- [action-cycle](action-cycle.md)
- [development-meta-cycle](development-meta-cycle.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [method-development](method-development.md)
- [plan](plan.md)
- [skill](skill.md)
- [world](world.md)
