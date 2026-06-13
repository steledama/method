---
data: 2026-06-13
stato: aperto
---

# Chiarire i1/i2 per le fonti elaborate di salute

Il 2026-06-13, in `salute`, la cartella `sources/` (trascrizioni e testi rielaborati
in markdown, versionati) è stata rinominata `perceptions/` — porta `perceptions.md`,
titolo "Percezioni elaborate (i1)" — e i grezzi (`sources/raw/*.txt`) sono stati
spostati fuori dall'artefatto, su Drive (`~/Drive/gdrive-stefano/salute/input/`, non
versionato, condiviso tra host). La motivazione locale: il grezzo è ora pienamente
"mondo esterno" (i1 in senso stretto), e la rielaborazione in markdown — prima
distillazione del segnale — diventerebbe il vero i1 _dentro_ l'artefatto.

## Tensione con `input.md`

`input.md` definisce già i tre stadi:

- i1 — grezzo: percezione del segnale esterno (referto, log, export, documento);
  dove vive: `sources/` (o locale al progetto)
- i2 — distillato: interpretazione e sintesi (nota di lettura, analisi, estratto
  commentato); dove vive: `kb/` in `stato: bozza`
- i3 — formalizzato: nodo KB `stato: maturo` o `verdict.md`

Per questa definizione, i1 è il segnale grezzo (ora corretto: vive fuori
dall'artefatto, su Drive, per `salute`) e i2 è la distillazione — ma i2 "vive in
`kb/` come bozza", non in una cartella propria. Le `perceptions/*.md` di `salute`
sono trascrizioni interamente rielaborate (la skill `elabora-trascrizione` produce
prosa distillata, non solo testo grezzo searchable) — per **natura** sembrano più
vicine a i2 ("nota di lettura, analisi, estratto commentato") che a i1, anche se
**non vivono in `kb/`**.

Questo è diverso dal pattern già documentato in `sources.md` (metodo): lì `sources/`
contiene i1 grezzo + un'estrazione `.txt` 1:1 (stesso contenuto, "i1 in forma
testuale canonica", non un'interpretazione). Le `perceptions/*.md` di `salute` non
sono un'estrazione 1:1: sono già un primo livello di sintesi/selezione (criteri di
inclusione/esclusione, struttura a sezioni, prosa rivista).

## Domande da chiarire

- Le `perceptions/*.md` di `salute` sono i2 "fuori sede" (per natura i2, ma non in
  `kb/` perché il dominio richiede un corpus intermedio tra grezzo e nodi atomici)?
  Se sì, la cartella andrebbe rinominata di conseguenza (`perceptions` → un nome che
  non implichi i1), oppure `input.md` va arricchito per ammettere che i2 possa vivere
  fuori da `kb/` quando il dominio lo richiede (sintesi lunghe, prima di estrarre
  nodi atomici)?
- Oppure: la rielaborazione è legittimamente un i1 "di secondo livello" — un i1 più
  fedele e cercabile del grezzo originale, sullo stesso piano dell'estrazione `.txt`
  di `sources.md` ma con un passo di pulizia/selezione in più data la natura
  (trascrizioni lunghe e ripetitive) — e quindi `perceptions`/i1 è corretto?
- Verificare se altri adottanti (`economia`, `bi`, `nixos`) hanno un pattern
  analogo: un corpus elaborato, versionato, distinto da `kb/`/`data/`, che si pone
  fra il grezzo e i nodi atomici.

## Esito atteso

- Chiarire/arricchire `input.md` con la posizione esatta di un eventuale corpus
  intermedio elaborato (nome di stadio, dove vive, criterio per distinguerlo da i1
  grezzo e da i2-in-kb).
- Allineare `salute/perceptions.md` (e il nome della cartella, se necessario) alla
  definizione chiarita.
- Se emerge un pattern comune, generalizzarlo in `input.md`/`sources.md`; se resta
  locale a `salute`, annotarlo come adattamento di dominio in `confronto-progetti-adottanti`.

Connessioni:

- [input](../kb/input.md)
- [output](../kb/output.md)
- [ciclo-azione](../kb/ciclo-azione.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
