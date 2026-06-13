# Fonti grezze

Porta-collezione di `sources/` nell'atrio di root: il manifest dello **strato input**.
La cartella `sources/` tiene copie di lavoro non versionate delle fonti che
alimentano i1 e, attraverso elaborazione (i2), diventano conoscenza formalizzata
nei nodi (i3). La rifondazione input/output è documentata in
[verdict.md](verdict.md).

I binari sono un caso degenere di `world`: il grezzo non sta fuori dal checkout,
ma siede in una cartella gitignorata. Non per questo diventa i1. Si versiona una
cattura del Perceive solo quando il grezzo è effimero o quando precisione,
revisione e durata richiedono un riflesso stabile. Le percezioni di `salute`
possono richiederlo; i libri di `method`, già persistenti e sotto copyright, no.

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
