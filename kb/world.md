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

- **`world` vs i1** — il grezzo non versionato sta nel Mondo; la cattura
  versionata e filtrata per rilevanza sta in `i1/`. Le fonti autorevoli (libri,
  documenti) vivono su una superficie non versionata, spesso Drive, fuori
  dall'artefatto: sono Mondo — fonte di verità, non i1; ne diventano i1 solo
  quando un'elaborazione le cattura. Di esse l'artefatto versiona solo la
  **provenienza**, nella sezione fonti del register `world.md`: un register che
  indicizza il Mondo è legittimo, mentre la superficie fisica non ha manifest
  (cfr. «Il register `world.md`»).
- **i1 vs i2** — il confine è l'ingresso della valenza e dell'interpretazione,
  non la fedeltà della copia. Estrazione lossless e distillazione lossy ma
  valenza-neutra possono essere entrambe i1.
- **o2 vs o3** — o2 è una superficie di decisione; o3 è una prescrizione
  versionata dell'atto. L'atto realizzato sta in `world`.

In Norman il Mondo è la scatola nera che risponde all'azione: il ciclo descrive
come l'utente agisce sull'artefatto e ne valuta la risposta, ma il Mondo resta
dato, non aperto. Il metodo estende Norman proprio su questo punto. La relazione
tra runtime cycle e development meta-cycle sdoppia il Mondo: il _Mondo runtime_
è la realtà su cui l'artefatto agisce (un'email inviata, una transazione, un
payload pubblicato, un gesto corporeo); il _Mondo di sviluppo_ è l'artefatto
stesso, su cui si agisce con un commit e di cui si percepisce la risposta come
lint, audit, test, errore. Ogni sistema runtime è il Mondo di un meta-ciclo di
sviluppo che lo precede: non l'o3, ma l'artefatto risultante dall'o3. Il metodo
apre così la scatola nera che Norman lasciava chiusa.

Il Mondo è l'elemento più specifico al dominio dell'intero ciclo. La meccanica è
invariante; ciò che cambia è di che cosa è fatto `world` e quali atti e segnali
lo attraversano. Il Mondo porta fatti favorevoli o sfavorevoli, ma non è la
sorgente della loro valenza: la valenza entra quando l'artefatto interpreta e
confronta quei fatti con un Goal.

## Il criterio del significato senza artefatto

I tre confini lasciano aperto un caso: il contenuto non versionato che
l'artefatto tocca è membrana `world` o substrato interno di uno stadio? Il
discriminante operativo è il **test del significato senza artefatto**:

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

Il test vale anche alla chiusura di un task: una copia operativa prodotta per
l'atto può restare su una superficie del Mondo pur avendo perso significato
autonomo. Quando una collezione si chiede «questo contenuto è mio o del mondo?»
applica lo stesso criterio. Il test classifica, non autorizza: riconoscere una
copia consumata non conferisce il permesso di cancellarla dal Mondo (cfr.
`tasks`, `consent`).

## Materializzazione fisica

La membrana fisica non ha un nome di path canonico. Il nome canonico identifica
il **polo** (`world.md`); le superfici concrete si chiamano per ciò che sono
(`gdrive/`, `client/`, mount, sync, sistema esterno) e sono dichiarate nel
register. Questo evita la collisione tra il register `world.md` e un symlink
root `world/`, che in sessione sembra un pezzo del canone invece di una
superficie host-local. La superficie resta gitignorata e senza manifest: il
contenuto è Mondo, non collezione dell'artefatto.

La membrana può avere **più superfici fisiche** per lo stesso adottante — la
cartella sincronizzata, un mount Drive per gli asset, un sistema esterno in
esercizio — purché **dichiarate** nel register `world.md`: è la dichiarazione a
tenere onesta la system image, non l'unicità del supporto. Il medium resta una
decisione tecnica reversibile; se una superficie degrada, il fallback è un altro
supporto world, non il ritorno a substrato.

Il contratto del register root che rende indirizzabile questo polo vive in
`world-register`; qui resta il modello del Mondo e della sua membrana.

## Configurazioni ricorrenti della cerniera bassa

Alcune forme ricorrenti di come la cerniera si distribuisce tra `world`, o3 e
i1, non l'inventario del territorio (che vive nel register `world.md`):

- **dominio riflessivo o personale** — nel Mondo stanno il corpo, le pratiche,
  gli incontri e i documenti originali; o3 predispone promemoria e canovacci; i1
  cattura percezioni e trascrizioni solo quando serve durata. Il grezzo è
  abbondante e quasi mai va versionato.
- **configurazione dichiarativa** — nel Mondo stanno host, reti, dischi e
  sistema in esecuzione; o3 è la configurazione o la procedura pronta al deploy;
  i1 raccoglie log ed errori quando il grezzo non è già persistente altrove. Qui
  il riflesso i1 è raro proprio perché il Mondo trattiene lo stato da sé.
- **integrazione di sistemi esterni** — nel Mondo stanno controparti, gestionali
  e servizi in esercizio, che rispondono con i propri tempi e non si lasciano
  interrogare a piacere; o3 è il payload o il runbook predisposto; i1 cattura
  export, risposte ed esiti per l'elaborazione. È la configurazione in cui la
  cattura i1 pesa di più, perché la fonte può non restare accessibile.

Le tre non esauriscono lo spettro e un adottante può starne a cavallo. Ciò che
resta invariante è la meccanica: l'atto e il grezzo nel Mondo, i due riflessi
versionati on-demand.

Connessioni:

- [action-cycle](action-cycle.md)
- [world-register](world-register.md)
- [goal](goal.md)
- [output](output.md)
- [input](input.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [affordance-signifier](affordance-signifier.md)
- [source-of-truth](source-of-truth.md)
- [readme](readme.md)
- [method-observatory](method-observatory.md)
- [method-development](method-development.md)
- [project-structure](project-structure.md)
- [processing-layers](processing-layers.md)
