---
stato: bozza
---

# World

Il fondo del ciclo d'azione: il polo opposto al Goal e la **membrana fisica non
versionata** tra artefatto e realtà. Se il Goal è l'apice da cui scende
l'esecuzione e a cui risale la valutazione, `world` è il luogo in basso dove
l'atto accade e da cui ritorna il segnale grezzo. È sempre presente, anche
quando il repository non ne conserva alcuna copia.

La cerniera bassa ha tre elementi distinti. L'atto e il grezzo stanno in
`world`; o3 e i1 sono i due riflessi versionati che baciano la membrana dal lato
dell'artefatto. o3 prescrive in avanti il Perform; i1 registra all'indietro il
Perceive. Il riflesso non è obbligatorio: si crea **on-demand**, quando l'atto o
il segnale richiede precisione, revisione o durata. Un canovaccio per un
incontro ad alta posta è o3; l'incontro è `world`; una trascrizione ripulita per
un confronto scrupoloso è i1.

La cerniera resta scrivi-poi-leggi attraverso un medium: l'atto modifica il
mondo e il segnale ne rende percepibile lo stato successivo. La differenza con
la cerniera KB non sta nella forma ma nel medium: il mondo persiste da sé, la KB
solo se scritta (cfr. `action-cycle`).

## I tre confini

- **`world` vs i1** — il grezzo non versionato sta in `world`; la cattura
  versionata e filtrata per rilevanza sta in `i1/`. Le fonti
  autorevoli (libri, documenti) vivono su Drive via `world/`, fuori
  dall'artefatto: sono Mondo — fonte di verità, non i1; ne diventano i1 solo
  quando un'elaborazione le cattura. Di esse l'artefatto versiona solo la
  **provenienza**, nella sezione fonti del register `world.md`: un register che
  indicizza il Mondo è legittimo, mentre il symlink-membrana `world/` non ha
  manifest (cfr. «Il register `world.md`»).
- **i1 vs i2** — il confine è l'ingresso della valenza e dell'interpretazione,
  non la fedeltà della copia. Estrazione lossless e distillazione lossy ma
  valenza-neutra possono essere entrambe i1.
- **o2 vs o3** — o2 è una superficie di decisione; o3 è una prescrizione
  versionata dell'atto. L'atto realizzato sta in `world`.

In Norman il Mondo è la scatola nera che risponde all'azione: il ciclo descrive come l'utente agisce sull'artefatto e ne valuta la risposta, ma il Mondo resta dato, non aperto. Il metodo estende Norman proprio su questo punto. La relazione tra runtime cycle e development meta-cycle sdoppia il Mondo: il _Mondo runtime_ è la realtà su cui l'artefatto agisce (un'email inviata, una transazione, un payload pubblicato, un gesto corporeo); il _Mondo di sviluppo_ è l'artefatto stesso, su cui si agisce con un commit e di cui si percepisce la risposta come lint, audit, test, errore. Ogni sistema runtime è il Mondo di un meta-ciclo di sviluppo che lo precede: non l'o3, ma l'artefatto risultante dall'o3. Il metodo apre così la scatola nera che Norman lasciava chiusa.

Il Mondo è l'elemento più specifico al dominio dell'intero ciclo. La meccanica
è invariante; ciò che cambia è di che cosa è fatto `world` e quali atti e
segnali lo attraversano. Il Mondo porta fatti favorevoli o sfavorevoli, ma non
è la sorgente della loro valenza: la valenza entra quando l'artefatto interpreta
e confronta quei fatti con un Goal.

## Il criterio del significato senza artefatto

I tre confini lasciano aperto un caso: il contenuto non versionato che
l'artefatto tocca è membrana `world` o substrato interno di uno stadio? Il
discriminante operativo, emerso in `bi` migrando il substrato runtime fuori
dalla root (2026-07-09), è il **test del significato senza artefatto**:

> se l'artefatto sparisse domani, questo contenuto avrebbe ancora significato
> operativo per il dominio?

Se sì, è Mondo: asset del dominio che l'artefatto legge e serve ma non possiede
(le foto prodotto nominate per SKU restano utili a sito, listini e operatori
anche senza BI). Se no, è substrato dello stadio appropriato o traccia o3: un
report di drift muore senza il ciclo che lo produce e lo legge, un file di
interscambio fra script è i/o interno, uno snapshot superato dal run successivo
è cache. La controprova è costitutiva del test: non promuove tutto a `world` —
un criterio che promuovesse tutto non discriminerebbe nulla.

Un **indicatore corroborante** è _chi scrive_: un attore del mondo che deposita
contenuto (l'operatore che nomina immagini per SKU) compie un atto del mondo,
non una scrittura interna dell'artefatto. L'indicatore non regge da solo come
criterio — l'artefatto stesso scrive legittimamente contenuto-mondo, perché o3
scrive effetti nel mondo (un payload pubblicato è Mondo pur essendo scritto
dall'artefatto) — ma nella direzione «scritto dal mondo → membrana» è forte.

Il criterio è nato su un caso e resta da collaudare oltre il confine
world/substrato: l'estensione per-stadio (ogni collezione che si chiede «questo
contenuto è mio o del mondo?») attende un secondo segnale reale prima di
diventare disciplina (cfr. `method-development`, la guardia dal basso).

## Materializzazione fisica

La convenzione uniforme è un symlink `world` nella root del repository verso
la cartella di progetto non versionata, tipicamente su Drive. Il nome non varia
per dominio: il carattere vive nel contenuto. `world/` non ha un manifest e non
è una collezione dell'artefatto; è solo la membrana. Il symlink è host-local e
gitignorato.

La membrana può avere **più superfici fisiche** per lo stesso adottante — la
cartella sincronizzata, un mount Drive per gli asset, un sistema esterno in
esercizio — purché **dichiarate** nel register `world.md`: è la dichiarazione a
tenere onesta la system image, non l'unicità del supporto. Il medium resta una
decisione tecnica reversibile; se una superficie degrada, il fallback è un
altro supporto world, non il ritorno a substrato.

## Il register `world.md`

Il polo World ha una porta versionata nell'atrio: il **register root
`world.md`**, gemello di `goal.md` (il goal è il nord, il world è il
territorio — cfr. `goal`). È l'indice del Mondo che l'artefatto, con i suoi
goal, ritiene rilevante: non versiona il mondo (che persiste da sé), ne
versiona la _vista_.

Il register **assorbe due file che il canone teneva separati**:

- `map.md` — l'indice-di-dominio (entità, sistemi, flussi, attori legati ai
  nodi) _era già_ un indice del territorio, cioè del Mondo; la sua dimensione
  interna («dove vivono o1, o2, o3») è superata dall'atrio, che si
  auto-dichiara. Ciò che resta di insostituibile è il territorio: vive qui.
- `sources.md` — il registro di provenienza delle fonti-mondo autorevoli
  (`source-of-truth`) era «sibling di `map.md`»: i sibling si fondono nella
  sezione fonti del register del polo, che continua ad alimentare i
  `## Riferimenti` dei nodi (i3).

La forma segue un **contratto machine-readable** condiviso con `goal.md`:
l'**intro** (dall'H1 al primo H2) è il polo in sintesi — di che cosa è fatto il
Mondo di questo artefatto — ed è ciò che la home rende come polo World,
markdown fedele senza euristiche (cfr. `readme`); le sezioni successive sono la
profondità on-demand, tipicamente:

- **superfici della membrana** — dove `world/` punta e quali altre superfici
  fisiche esistono, dichiarate una volta;
- **territorio** — entità, sistemi, fonti di verità e attori, legati ai nodi
  che li spiegano (l'eredità di `map.md`: nei repo tecnici host e flussi, in
  `economia` conti ed entità, in `salute` assi e pratica);
- **fonti** — la provenienza delle fonti-mondo autorevoli: quale edizione regge
  quale nodo (l'eredità di `sources.md`).

Le regole ereditate restano: porta on-demand (non la bussola, che è il README),
non diventa storico né lista di task, non sostituisce il catalogo `kb/kb.md`
(che indicizza i nodi, non il territorio). A differenza di `map.md`, che
esisteva solo «dove il dominio ha un territorio da indicizzare», `world.md` c'è
in ogni repo: ogni artefatto ha un Mondo — varia la taglia del territorio, non
l'esistenza del polo.

## Il Mondo nei progetti adottanti

L'elenco separa ciò che accade nel Mondo dai riflessi versionati.

- **`salute`** — `world`: corpo, mente, visite, pratiche, conversazioni e
  referti originali; o3: promemoria e canovacci; i1: percezioni, referti o
  trascrizioni catturati quando serve durata.
- **`economia`** — `world`: conti, interlocutori, email, telefonate, incontri e
  transazioni; o3: canovacci e messaggi predisposti; i1: export e
  corrispondenza ripulita per analisi.
- **`nixos`** — `world`: host, reti, dischi e sistema in esecuzione; o3:
  configurazione o procedura pronta al deploy; i1: log, errori e stato
  catturati quando il grezzo non è già persistente.
- **`bi`** — `world`: relazione con fornitori e Danea, siti e plugin in
  esercizio; o3: payload o runbook predisposti; i1: cataloghi, export e
  risposte catturati per l'elaborazione.

## Il Mondo del metodo

`metodo` è un meta-artefatto e ha due Mondi distinti. Il _Mondo runtime_ sono i
progetti adottanti: da lì entrano esigenze, drift e convergenze; lì tornano il
filing back e la propagazione. Il register `world.md` di root li indicizza; la
membrana `world/` gitignorata tiene i symlink a `economia`, `salute`, `nixos` e
`bi` — duale del link `method/` con cui gli adottanti leggono i nodi canonici —
e i binari delle fonti autorevoli su Drive. Quel link è
_inteso_ in lettura, ma **afforda anche la scrittura** (`affordance-signifier`):
un agente che risolve un problema in un adottante può modificare un nodo di
canone attraverso il symlink. È legittimo come atto runtime — vale la cucitura
**«agisci attraverso la membrana, ratifica in `method`»**: l'edit prosegue come
_segnale_, non come canone-di-record, finché non passa per l'i2/i3 di `method`
(cfr. i fili `i3/`). Il _Mondo di sviluppo_ sono invece i nodi `kb/` e la loro
coerenza: un commit agisce sui nodi, lint e audit ne percepiscono la risposta.

Connessioni:

- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [output](output.md)
- [input](input.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [affordance-signifier](affordance-signifier.md)
- [source-of-truth](source-of-truth.md)
- [readme](readme.md)
- [adopter-comparison](adopter-comparison.md)
- [method-observatory](method-observatory.md)
- [method-development](method-development.md)
- [project-structure](project-structure.md)
- [processing-layers](processing-layers.md)
