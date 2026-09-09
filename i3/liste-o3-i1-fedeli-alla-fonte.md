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

`o3/build_lists.py` renderizza ora, nell'ordine della fonte, l'intro (il
corpo prima della prima `##`) e ogni sezione `##` per intero — paragrafi e
liste, senza selezionare quale sezione conti e quale no. La parametrizzazione
per pagina (`PAGES`) resta solo su sorgente/prefisso-link/titolo, mai su quali
intestazioni includere: una sezione conta per la sua forma (intestazione +
blocco), non per il suo nome. Verificato sui due casi reali: `prescriptions.html`
rende ora anche `## Strumenti` (chiude lo scarto nixos, mascherato anche nel
canone); una fonte con nomi di sezione propri come quella di `bi` renderizza
comunque per intero, senza bisogno di whitelist locale. `presentation.py`
normalizza i link relativi (`posixpath.normpath`) — necessario perché
l'intro, a differenza dei soli item della coda, porta link scritti relativi
alla fonte in punti diversi del file.

`kb/view.md` guadagna il principio in prosa («Il contratto è strutturale, non
nominale»): una collezione-stadio è vicina al Mondo (Perceive/Perform, livello
istintuale di Norman) ed è normale che ogni repo la strutturi a modo proprio;
il generatore condiviso non deve imporre il proprio lessico a chi lo usa
(`method-development`, «il confine canone↔adottante: dichiara e taci»).

Verificato: audit strutturale verde (48 nodi), viste rigenerate
deterministicamente (`git status` stabile a doppia rigenerazione di
`build-presentation.sh`), link relativi corretti.

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
