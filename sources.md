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
- **Things That Make Us Smart: Defending Human Attributes in the Age of the Machine** — Don
  Norman, originale **1993** (Addison-Wesley, ISBN 978-0201626957). **Volume integrale ora
  reperito** nella riedizione **Diversion Books, dicembre 2014** (ISBN 978-1-62681-537-7),
  EPUB **testo nativo pulito** (parse `pandoc`, niente OCR), superficie di lavoro `TTMUS.txt`.
  Il volume integrale rende obsoleto il vecchio estratto del solo Cap. 3 (`representation.*`, di
  uno stato precedente di `world/`, non presente in questa cartella). Fonte di `cognitive-artifact` (Cap. 3
  «The Power of Representation», già distillato) e, da distillare, del pavimento ontologico:
  **Cap. 6 «Distributed Cognition»** (la trattazione di Norman, accanto a Hutchins/Clark) e i
  capitoli su cognizione esperienziale vs riflessiva (Cap. 2, 5). Citare per **capitolo**, non
  per pagina (la paginazione della riedizione 2014 differisce dall'originale 1993). Solo
  provenienza qui, niente cattura in `perceptions/`.
- **How Buildings Learn: What Happens After They're Built** — Stewart Brand, originale **1994**
  (Viking Penguin), Penguin Books **1995**, EPUB con testo nativo, ISBN 978-1-101-56264-2,
  superficie di lavoro `HowBuildingsLearn.txt` generata con `pandoc`. Fonte di
  `pace-layering` per la traduzione operativa di Duffy: Brand riprende i quattro strati di
  Frank Duffy e li espande nei sei "S" general-purpose (Site, Structure, Skin, Services,
  Space plan, Stuff), poi collega la gerarchia degli strati al rapporto slow/fast: gli strati
  lenti vincolano quelli veloci, mentre i cambiamenti veloci possono risalire e farsi assorbire
  dagli strati lenti quando diventano ricorrenti. **Cap. 2 «Shearing Layers» distillato in
  `kb/pace-layering.md`**; Brand basta come fonte operativa per l'uso metodologico, mentre Duffy
  primario resta un approfondimento filologico non bloccante. Citare per **capitolo/sezione**,
  non per pagina, perché la superficie di lavoro deriva dall'EPUB.
- **The Clock of the Long Now: Time and Responsibility** — Stewart Brand, **1999**, Basic Books,
  A Member of the Perseus Books Group, eISBN 978-0-786-72292-1, EPUB con testo nativo, superficie
  di lavoro `ClockLongNow.txt` generata con `pandoc`. Fonte di `pace-layering` per la
  generalizzazione civilizzazionale: nel capitolo **«The Order of Civilization»** Brand formula
  la scala Fashion/art, Commerce, Infrastructure, Governance, Culture, Nature e la dinamica
  "fast learns, slow remembers / fast proposes, slow disposes". Distillato in
  `kb/pace-layering.md`; citare per **capitolo/sezione**, non per pagina.
- **The Extended Mind** — Andy Clark & David J. Chalmers, _Analysis_ 58(1):7-19, 1998,
  DOI 10.1111/1467-8284.00096. Fonte primaria del task «mente estesa». Testo d'autore
  completo: pagina HTML di Chalmers (`consc.net/papers/extended.html`) e PDF nel
  repository istituzionale di Edinburgh (ERA, `1842/1312`, 22 pp.) — quest'ultimo è l'i1
  scelto. Copia legale ma sotto copyright Oxford/Wiley e persistente: solo provenienza
  qui, niente cattura in `perceptions/` (come i libri di Norman). **i3 scritto** nella
  chirurgia coordinata dei nodi (2026-06-21): pavimento ontologico in `kb/cognitive-system.md`
  (active externalism, parity, scaffolding, 007, mente-come-controllore, criterio scaffold
  action-oriented). Nota di fedeltà: la pagina d'autore riporta una
  paginazione diversa (58:10-23, da reprint); la citazione canonica del journal è 7-19.
- **Being There: Putting Brain, Body, and World Together Again** — Andy Clark, A Bradford
  Book / The MIT Press, **1997** (second printing 1997), ISBN 0-262-03240-6, LCCN 96-11817.
  Companion di _The Extended Mind_ per il task «mente estesa»: il paper copre belief/memoria
  (Otto), questo libro copre embodiment e **scaffolding** — è la fonte del claim «artefatto
  come corpo/ambiente ingegnerizzato» che da sola _The Extended Mind_ non regge. Procurato in
  PDF con **strato di testo nativo** (pulito), superficie di lavoro `BeingThere.txt`; niente
  OCR né cattura in `perceptions/`, solo provenienza qui. Nota di fedeltà: il nome del file
  riporta «1998» (probabile paperback), ma l'edizione è la 1997 — citare 1997. **i1 letto e
  i3 scritto**: lo scaffolding e il «007 principle» sono distillati nel pavimento ontologico
  di `kb/cognitive-system.md`.
- **Augmenting Human Intellect: A Conceptual Framework** — Douglas C. Engelbart, Summary
  Report **AFOSR-3223**, SRI Project No. 3578, Contract AF 49(638)-1024, preparato per il
  Director of Information Sciences, Air Force Office of Scientific Research; Stanford Research
  Institute, Menlo Park, **ottobre 1962**. Ripubblicato in forma ridotta come «A Conceptual
  Framework for the Augmentation of Man's Intellect» in _Vistas in Information Handling_
  (Howerton & Weeks eds., Spartan Books, 1963, pp. 1-29). Fonte primaria del task Engelbart e
  della ristrutturazione dei giganti, distillata nel nodo `kb/augmentation-system.md`.
  Report governativo/SRI, pubblicato liberamente dal Doug Engelbart Institute; procurato da
  Internet Archive (`1962-engelbart-AHI-framework`) in EPUB a scansione (166 MB, immagini di
  pagina con strato OCR) e PDF (9 MB). Confronto fatto: il PDF via `pdftotext` (sia `-layout`
  sia raw) è mangiato (spaziatura spezzata, passi mancanti); l'OCR dell'EPUB estratto dai `<p>`
  è prosa pulita ed è la **superficie di lavoro** scelta (`1962-engelbart-AHI-framework.txt`),
  GLM-OCR non necessario. Il **PDF è stato rimosso** perché scadente: restano EPUB + txt. Cita
  per **sezione**, non per pagina, vista la qualità OCR. Solo provenienza versionata qui, niente
  cattura in `perceptions/`. **i1 letto integralmente (Sez. I-IV)**: cornice H-LAM/T, synergism,
  ipotesi Neo-Whorfiana, bootstrap «Tools Developed vs Tools Used»; la Sez. III (memex di Bush,
  il sistema di schede edge-notched di Engelbart, il dialogo «Joe», team cooperation) conferma
  sul testo primario che la cornice contiene già nodi atomici con link tipizzati e provenienza,
  la mossa di ingest/distillazione i1→i2, un loop di valutazione e la cooperazione collaborativa.
- **Cognition in the Wild** — Edwin Hutchins, A Bradford Book / The MIT Press, **1995**. Fonte
  del **pavimento ontologico** (cognizione distribuita) che `cognitive-system` già cita;
  procurata per saldare il debito «citato-non-sourced» prima della chirurgia dei giganti. PDF
  con strato OCR (scansione), superficie `Hutchins.txt`; qualità **media** (artefatti tipo
  «suong»→strong, «Corn~ute»→compute, parole fuse) — usabile per sourcing per concetto/capitolo,
  GLM-OCR non necessario, ma ogni citazione verbatim va verificata sulla scansione. Pagina-titolo
  OCR-garbled: ISBN/printing non verificati dall'OCR (citare 1995, MIT Press). **i1 di sourcing
  fatto**: la tesi (cognizione come processo culturale/sociale; unità di analisi oltre la pelle;
  il team di navigazione come sistema cognitivo e computazionale), la definizione di «cognition
  in the wild» (habitat naturale vs laboratorio «in captivity», un'ecologia del pensiero), la
  propagazione dello stato rappresentazionale tra media, e la sintesi del cap. 9 (non scambiare
  le proprietà del sistema socioculturale per quelle della mente individuale) — esattamente il
  punto che Clark cita (Hutchins 1995 cap. 9). Solo provenienza qui, niente cattura in
  `perceptions/`.
- **Activity, Consciousness, and Personality** — A. N. Leont'ev, traduzione inglese **1978**
  (orig. russo _Деятельность. Сознание. Личность_, 1975). Fonte di `goal` per la **gerarchia
  attività / azione / operazione** (azione ↔ goal, attività ↔ motivo, operazione ↔ condizioni).
  Procurato da **marxists.org** (libero e legale), EPUB **testo nativo pulito** (parse `pandoc`,
  niente OCR), superficie di lavoro `Leontiev-ACP.txt`, ToC integrale. La sezione-chiave è **§3.5
  «The General Structure of Activity»**. Citare per **sezione** (la traduzione marxists.org può
  differire dall'edizione a stampa Prentice-Hall/Progress 1978). Solo provenienza qui, niente
  cattura in `perceptions/`. **§3.5 sorzata in `kb/goal.md`**: confermata la distinzione
  attività/motivo, azione/goal o scopo cosciente, operazione/condizioni.

### Scelta delle copie (2026-06-05)

Per DOET erano arrivate quattro copie. Tenuta solo l'**EPUB 2013** perché:

- è l'edizione che contiene i concetti che servono (affordance/signifier, aggiunti nel 2013);
- l'EPUB ha testo nativo, qualità superiore al PDF per l'estrazione (i1→i2).

Scartate: l'ed. 2002 (superata, priva di signifier), una scansione da 23 MB senza strato
testo (inservibile), e il PDF 2013 (ridondante con l'EPUB).

## Gap noto

Nessun debito di **fonte** fondativo resta aperto: frame (Engelbart), pavimento
(Hutchins/Clark/Norman) e `goal` (Leontiev) sono tutti reperiti. Restano due lavori di
**distillazione** (non di fonte), tracciati altrove:

- _Things That Make Us Smart_ (Norman 1993) — volume integrale reperito; Cap. 2 e 6 **i3
  scritto** (2026-06-21): Cap. 2 (esperienziale/riflessivo, radice dei tre livelli) in
  `kb/cognitive-artifact.md` e `kb/processing-layers.md`; Cap. 6 (cognizione distribuita di
  Norman) in `kb/cognitive-system.md`. Cap. 3 già in `kb/cognitive-artifact.md`; Cap. 5 e altri opzionali.
- _Activity, Consciousness, and Personality_ (Leont'ev 1978) — §3.5 sorzata in `kb/goal.md`;
  resta solo l'eventuale distillazione ulteriore se nascerà da uso reale del nodo.
