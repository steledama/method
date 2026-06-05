# Fonti grezze (i1)

Questa cartella è il primo pilota dello **strato input**: i segnali grezzi (i1) che,
attraverso elaborazione (i2), diventano conoscenza formalizzata nei nodi (i3).
Cfr. [ingest-norman](../todo/ingest-norman.md) e
[rifondazione-input-output](../todo/rifondazione-input-output.md).

I file binari **non sono versionati** (vedi `.gitignore`): sono sotto copyright e il repo
è pubblico. Versionato è solo questo manifest, che registra la *provenienza* delle fonti —
quale edizione esatta ha alimentato quale concetto. È la base dei `## Riferimenti` nei nodi
(fedeltà alle fonti: quale libro per quale idea).

Accanto a ogni binario può vivere una sua estrazione testuale `.txt` (resa leggibile con
`pandoc`/`pdftotext`): è la superficie di lavoro per l'ingest, ciò su cui si grep-pa e si
verificano le citazioni. **Non è un i2**: nessuna interpretazione, stesso contenuto del
binario — è i1 in forma testuale canonica, e per copyright è ignorata esattamente come il
binario (anzi a maggior ragione, essendo testo pieno e cercabile). Le uniche porzioni
versionate restano le citazioni brevi dentro i `## Riferimenti` dei nodi. I `.txt` si
rigenerano dai binari:

```
pandoc -f epub -t plain "<file>.epub" -o "<file>.txt"   # per gli EPUB
pdftotext "<file>.pdf" "<file>.txt"                      # per i PDF
```

## Fonti presenti

| Fonte | Edizione | Formato | ISBN | Note |
| --- | --- | --- | --- | --- |
| *The Design of Everyday Things* | Revised and Expanded, 2013 | EPUB | 978-0465050659 | Fonte canonica per `ciclo-azione`. L'ed. 2013 è quella che **aggiunge** affordance e signifier rispetto all'orig. 1988. Scelto l'EPUB (testo nativo riflowabile) come miglior i1 per la distillazione. |
| *Emotional Design — Why We Love (or Hate) Everyday Things* | 2004 | PDF | 978-0465051366 | Citata in `ciclo-azione`; copia unica, strato testo verificato. |
| *Things That Make Us Smart* — Cap. 3 «The Power of Representation» | 1993 | PDF (estratto) | 978-0201626957 | Fonte per `artefatto-cognitivo`. Capitolo disponibile; testo estratto con pdftotext (`representation.txt`) e GLM-OCR (`representation-glm-ocr.txt`, con indicatori di pagina — qualità superiore). L'intero volume non è ancora reperito. |

### Scelta delle copie (2026-06-05)

Per DOET erano arrivate quattro copie. Tenuta solo l'**EPUB 2013** perché:
- è l'edizione che contiene i concetti che servono (affordance/signifier, aggiunti nel 2013);
- l'EPUB ha testo nativo, qualità superiore al PDF per l'estrazione (i1→i2).

Scartate: l'ed. 2002 (superata, priva di signifier), una scansione da 23 MB senza strato
testo (inservibile), e il PDF 2013 (ridondante con l'EPUB).

## Gap noto

- *Things That Make Us Smart* (1993, ISBN 978-0201626957) — il **Cap. 3 «The Power of
  Representation»** è ora disponibile come PDF (`representation.pdf`) e distillato in
  `kb/artefatto-cognitivo.md` (bozza). Il volume completo (in particolare i capitoli su
  cognizione distribuita e sugli artefatti esperienziali vs riflessivi negli altri contesti)
  non è ancora reperito.
