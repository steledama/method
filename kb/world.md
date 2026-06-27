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
  versionata e filtrata per rilevanza sta in i1 (`perceptions/`). Le fonti
  autorevoli (libri, documenti) vivono su Drive via `world/`, fuori
  dall'artefatto: sono Mondo — fonte di verità, non i1; ne diventano i1 solo
  quando un'elaborazione le cattura. Di esse l'artefatto versiona solo il
  **registro di provenienza** (`sources.md`), che alimenta i3 ed è sibling di
  `map.md`: un register che indicizza il Mondo è legittimo, mentre il
  symlink-membrana `world/` non ha manifest (cfr. «Materializzazione fisica»).
- **i1 vs i2** — il confine è l'ingresso della valenza e dell'interpretazione,
  non la fedeltà della copia. Estrazione lossless e distillazione lossy ma
  valenza-neutra possono essere entrambe i1.
- **o2 vs o3** — o2 è una superficie di decisione; o3 è una prescrizione
  versionata dell'atto. L'atto realizzato sta in `world`.

In Norman il Mondo è la scatola nera che risponde all'azione: il ciclo descrive come l'utente agisce sull'artefatto e ne valuta la risposta, ma il Mondo resta dato, non aperto. Il metodo estende Norman proprio su questo punto. L'annidamento dei cicli sdoppia il Mondo: il _Mondo runtime_ è la realtà su cui l'artefatto agisce (un'email inviata, una transazione, un payload pubblicato, un gesto corporeo); il _Mondo di sviluppo_ è l'artefatto stesso, su cui si agisce con un commit e di cui si percepisce la risposta come lint, audit, test, errore. Ogni sistema runtime è il Mondo di un ciclo di sviluppo che lo precede: non l'o3, ma l'artefatto risultante dall'o3. Il metodo apre così la scatola nera che Norman lasciava chiusa.

Il Mondo è l'elemento più specifico al dominio dell'intero ciclo. La meccanica
è invariante; ciò che cambia è di che cosa è fatto `world` e quali atti e
segnali lo attraversano. Il Mondo porta fatti favorevoli o sfavorevoli, ma non
è la sorgente della loro valenza: la valenza entra quando l'artefatto interpreta
e confronta quei fatti con un Goal.

## Materializzazione fisica

La convenzione uniforme è un symlink `world` nella root del repository verso
la cartella di progetto non versionata, tipicamente su Drive. Il nome non varia
per dominio: il carattere vive nel contenuto. `world/` non ha un manifest e non
è una collezione dell'artefatto; è solo la membrana. Il symlink è host-local e
gitignorato.

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
filing back e la propagazione. La sua materializzazione convenzionale è una
`world/` gitignorata con symlink a `economia`, `salute`, `nixos` e `bi`, duale
del link `method/` con cui gli adottanti leggono i nodi canonici. Quel link è
_inteso_ in lettura, ma **afforda anche la scrittura** (`affordance-signifier`):
un agente che risolve un problema in un adottante può modificare un nodo di
canone attraverso il symlink. È legittimo come atto runtime — vale la cucitura
**«agisci attraverso la membrana, ratifica in `method`»**: l'edit prosegue come
_segnale_, non come canone-di-record, finché non passa per l'i2/i3 di `method`
(cfr. `verdict.md`). Il _Mondo di sviluppo_ sono invece i nodi `kb/` e la loro
coerenza: un commit agisce sui nodi, lint e audit ne percepiscono la risposta.

Connessioni:

- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [output](output.md)
- [input](input.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [affordance-signifier](affordance-signifier.md)
- [adopter-comparison](adopter-comparison.md)
- [method-observatory](method-observatory.md)
- [method-development](method-development.md)
- [project-structure](project-structure.md)
- [processing-layers](processing-layers.md)
