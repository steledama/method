# Fonti

**Register** di provenienza nell'atrio di root — non un catalogo né una collezione
interna: il manifest di **provenienza delle fonti-mondo autorevoli**, quale edizione esatta
ha alimentato quale concetto. È materiale di `world`, non dello strato input: la
fonte di verità (`source-of-truth`) contro cui si verifica ciò che i nodi
affermano, che vive **fuori** dall'artefatto. Sibling di `map.md`: entrambi
indicizzano il territorio esterno, non una cartella interna. Diventa i1
(`perceptions/`) solo se un'elaborazione ne cattura una porzione versionata;
finché resta grezzo non elaborato, è Mondo. La rifondazione input/output è
documentata in [verdict.md](verdict.md).

I binari vivono in `world` (su Drive, via il symlink `world/`, gitignorati):
grezzo esterno persistente, fuori dall'artefatto. Non per questo diventano i1. Si
versiona una cattura del Perceive (in `perceptions/`) solo quando il grezzo è
effimero o quando precisione, revisione e durata richiedono un riflesso stabile.
Le percezioni di `salute` possono richiederlo; i libri di `method`, già
persistenti e sotto copyright, no — di loro resta versionata solo la provenienza,
qui sotto.

I file binari **non sono versionati** (vedi `.gitignore`): sono sotto copyright e il repo
è pubblico. Versionato è solo questo manifest, che registra la _provenienza_ delle fonti —
quale edizione esatta ha alimentato quale concetto. È la base dei `## Riferimenti` nei nodi
(fedeltà alle fonti: quale libro per quale idea).

Accanto a ogni binario può vivere una sua estrazione testuale `.txt` (resa
leggibile con `pandoc`/`pdftotext`): è la superficie di lavoro per l'ingest, ciò
su cui si grep-pa e si verificano le citazioni. Non è i2, perché non contiene
interpretazione; nel metodo non è neppure i1, perché resta ignorata insieme al
grezzo persistente nel `world` degenere. Sarebbe i1 se venisse selezionata e
versionata come cattura necessaria del Perceive. Le uniche porzioni versionate
restano le citazioni brevi dentro i `## Riferimenti` dei nodi. I `.txt` si
rigenerano dai binari:

```
pandoc -f epub -t plain "<file>.epub" -o "<file>.txt"   # per gli EPUB
pdftotext "<file>.pdf" "<file>.txt"                      # per i PDF
```

## Fonti presenti

- **The Design of Everyday Things** — Revised and Expanded, 2013, EPUB, ISBN 978-0465050659.
  Fonte canonica per `action-cycle`. L'ed. 2013 è quella che **aggiunge** affordance e
  signifier rispetto all'orig. 1988. Scelto l'EPUB (testo nativo riflowabile) come miglior
  i1 per la distillazione.
- **Emotional Design — Why We Love (or Hate) Everyday Things** — 2004, PDF, ISBN
  978-0465051366. Citata in `action-cycle`; copia unica, strato testo verificato.
- **Things That Make Us Smart** — Cap. 3 «The Power of Representation», 1993, PDF
  (estratto), ISBN 978-0201626957. Fonte per `cognitive-artifact`. Capitolo disponibile;
  testo estratto con pdftotext (`representation.txt`) e GLM-OCR
  (`representation-glm-ocr.txt`, con indicatori di pagina — qualità superiore). L'intero
  volume non è ancora reperito.
- **The Extended Mind** — Andy Clark & David J. Chalmers, _Analysis_ 58(1):7-19, 1998,
  DOI 10.1111/1467-8284.00096. Fonte primaria del task «mente estesa». Testo d'autore
  completo: pagina HTML di Chalmers (`consc.net/papers/extended.html`) e PDF nel
  repository istituzionale di Edinburgh (ERA, `1842/1312`, 22 pp.) — quest'ultimo è l'i1
  scelto. Copia legale ma sotto copyright Oxford/Wiley e persistente: solo provenienza
  qui, niente cattura in `perceptions/` (come i libri di Norman). Distillazione i2/i3 da
  fare e destinazione da decidere dopo la lettura (cfr. `tasks/fonti-mente-estesa.md`); il
  nodo non va scritto prima dell'i1 reale. Nota di fedeltà: la pagina d'autore riporta una
  paginazione diversa (58:10-23, da reprint); la citazione canonica del journal è 7-19.
- **Augmenting Human Intellect: A Conceptual Framework** — Douglas C. Engelbart, Summary
  Report **AFOSR-3223**, SRI Project No. 3578, Contract AF 49(638)-1024, preparato per il
  Director of Information Sciences, Air Force Office of Scientific Research; Stanford Research
  Institute, Menlo Park, **ottobre 1962**. Ripubblicato in forma ridotta come «A Conceptual
  Framework for the Augmentation of Man's Intellect» in _Vistas in Information Handling_
  (Howerton & Weeks eds., Spartan Books, 1963, pp. 1-29). Fonte primaria del task Engelbart e
  della ristrutturazione dei giganti (cfr. `verdict.md`, filo «I giganti ristrutturati»).
  Report governativo/SRI, pubblicato liberamente dal Doug Engelbart Institute; procurato da
  Internet Archive (`1962-engelbart-AHI-framework`) in EPUB a scansione (166 MB, immagini di
  pagina con strato OCR) e PDF (9 MB). Confronto fatto: il PDF via `pdftotext` (sia `-layout`
  sia raw) è mangiato (spaziatura spezzata, passi mancanti); l'OCR dell'EPUB estratto dai `<p>`
  è prosa pulita ed è la **superficie di lavoro** scelta (`1962-engelbart-AHI-framework.txt`),
  GLM-OCR non necessario. Cita per **sezione**, non per pagina, vista la qualità OCR. Solo
  provenienza versionata qui, niente cattura in `perceptions/`. **i1 letto integralmente (Sez.
  I-IV)**: cornice H-LAM/T, synergism, ipotesi Neo-Whorfiana, bootstrap «Tools Developed vs
  Tools Used»; la Sez. III (memex di Bush, il sistema di schede edge-notched di Engelbart, il
  dialogo «Joe», team cooperation) conferma sul testo primario che la cornice contiene già nodi
  atomici con link tipizzati e provenienza, la mossa di ingest/distillazione i1→i2, un loop di
  valutazione e la cooperazione collaborativa.

### Scelta delle copie (2026-06-05)

Per DOET erano arrivate quattro copie. Tenuta solo l'**EPUB 2013** perché:

- è l'edizione che contiene i concetti che servono (affordance/signifier, aggiunti nel 2013);
- l'EPUB ha testo nativo, qualità superiore al PDF per l'estrazione (i1→i2).

Scartate: l'ed. 2002 (superata, priva di signifier), una scansione da 23 MB senza strato
testo (inservibile), e il PDF 2013 (ridondante con l'EPUB).

## Gap noto

- _Things That Make Us Smart_ (1993, ISBN 978-0201626957) — il **Cap. 3 «The Power of
  Representation»** è ora disponibile come PDF (`representation.pdf`) e distillato in
  `kb/cognitive-artifact.md` (bozza). Il volume completo (in particolare i capitoli su
  cognizione distribuita e sugli artefatti esperienziali vs riflessivi negli altri contesti)
  non è ancora reperito.
