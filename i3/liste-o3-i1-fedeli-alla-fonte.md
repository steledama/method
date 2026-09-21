---
ciclo: dev
---

# Le viste a elenco o3/i1 sono fedeli alla struttura della fonte, non a un nome di intestazione

Aperto il 2026-09-09 dalla valutazione i2→i3 di due percezioni consumate qui:
`bi` («`build_lists.py` assume `## Contenuti` come nome fisso della coda, ma
un'intestazione fissa non regge in un repo dove lo stesso nome ha già un
altro significato») e `nixos` («la presentazione eredita la domanda di i1 per
analogia strutturale, ma nessuno ha mai dichiarato a quale domanda e a quale
pubblico ogni pagina deve rispondere»). Stesso giorno, stesso generatore,
stesso commit d'origine (`2891892`): due repo indipendenti su due assi
diversi della stessa rottura — il contratto della vista era un nome di
intestazione (`## Contenuti`), non la struttura markdown della fonte. In `bi`
il nome ha due significati diversi fra collezioni dello stesso repo; in
`nixos`, e mascherato nel canone stesso, la card o3 promette «strumenti» che
il generatore non ha mai reso, perché guardava solo il primo blocco puntato
sotto quel nome — `## Strumenti` restava fuori da `prescriptions.html` anche
in `metodo`.

## Il contratto nuovo

`o3/build_lists.py` rende l'intero corpo Markdown tramite Pandoc, già richiesto
dalla build Reveal. La parametrizzazione `PAGES` conserva sorgente, prefisso dei
link e titolo; il titolo iniziale della fonte è sostituito da quello di pagina.
Le intestazioni editoriali non sono una whitelist. Sottotitoli, liste annidate
e numerate e codice conservano la propria struttura: la lettura di tutte le
sezioni H2 da sola non bastava, perché il parser di blocchi piatti appiattiva
padri e figli e rendeva i sottotitoli come prosa.

Il ribasamento dei link e delle immagini Markdown avviene sull'AST prima della
resa HTML, preservando query, frammenti e URL assoluti. Il codice letterale non
è riscritto. L'HTML grezzo incorporato, inclusi i suoi URL, resta responsabilità
della fonte. Il formato è il Markdown di Pandoc usato dalla build Reveal.

Il contratto di `kb/view.md` distingue intestazioni editoriali libere e chiavi
nominali esplicitamente dichiarate da uno schema. La fedeltà richiede di
preservare le relazioni nella fonte, non soltanto tutte le parole. Le prove in
`tests/test_build_lists.py` presidiano annidamenti, ordine delle sezioni,
sottotitoli, liste numerate, codice e destinazioni dei link; il doppio giro di
build verifica il determinismo sulle fonti reali.

## Watchpoint aperto: fedeltà completa vs. lente del lettore-abitante

Renderizzare per intero include anche la prosa storica che oggi vive, senza
intestazione propria, subito dopo il blocco puntato di `## Contenuti` in
`i1/perceptions.md` e `o3/prescriptions.md` — il generatore non decide più
cosa sia «storia», quindi non la esclude più. Le due pagine sono oggi più
lunghe e mescolano il registro «coda aperta» (lettore-abitante, cfr. il
segnale nixos su domanda/pubblico) con quello narrativo (lettore-ospite,
cronaca dei fili chiusi). La causa è a monte, non nel generatore: `i1` e `o3`
dichiarano già che «la storia resta in git» ma la tengono comunque in prosa
nel corpo del file. Non prunata qui — è una decisione editoriale sul
contenuto delle collezioni, non sullo strumento, e resta al custode: se `i1`
e `o3` smettessero di portare la cronaca inline (coerenti con la propria
regola già scritta), il problema si scioglie da sé, senza altro codice — ma
è materiale nuovo, non lo stesso filo, e non blocca la chiusura del verdetto
sopra.

Misura: obiettivo 1 del goal («Custodire un canone coerente e fedele alle
fonti»). Propagazione agli adottanti in `o3/liste-o3-i1-fedeli-alla-fonte.md`.
