---
stato: bozza
---

# Presentation

La presentazione è il **racconto curato dell'artefatto**: un solo deck che
spiega com'è fatto il progetto e perché, a chi lo incontra senza percorrerne le
collezioni. È scritta, non derivata. Se una vista (`view`) traduce una fonte
senza diventarne una seconda, la presentazione è essa stessa una fonte: un
argomento composto, con un ordine, delle tavole e delle omissioni scelte.

## Distinta dalle viste e dall'interpretazione

Due confusioni da tenere fuori.

- **Non è una vista.** Una vista si rigenera e la sua freschezza è un gesto
  meccanico; il deck si scrive, e la sua freschezza è un giudizio: quando
  cambia ciò che racconta, va riletto. Per questo non vive in `view/`, dove
  tutto è generato, ma in `presentation/`: la sorgente `presentation.md` e
  le tavole accanto. La build la rende in `view/presentation.html` e la home
  la linka come voce a sé.
- **Non è uno stadio.** Il racconto dell'artefatto non interpreta i segnali del
  Mondo: tenerlo in `i2/` mescola la superficie curata con le letture che
  attendono riscontro, e fa sembrare interpretazione ciò che è esposizione.
  `i2/` resta alle sintesi che interpretano i segnali.

## Fedeltà alle fonti

Il deck comprime: ogni slide sceglie una tensione e ne tace altre. La
compressione è legittima finché ciò che afferma resta riconducibile a una fonte
del repo — un nodo, una sintesi, un register — e non introduce tesi che il
canone non regge. Una tavola che semplifica un concetto deve semplificarlo
nella direzione del nodo, non in quella più raccontabile (`verdict`, «Il
verdetto non può essere più sicuro del materiale»). Il deck non sostituisce le
fonti: chi vuole il dettaglio apre le pagine.

Negli adottanti il deck può essere generato dai dati del repo da un builder di
dominio (`DECK_BUILDER` in `o3/view/project.py`), invece che scritto in
Markdown (`DECK`). In quel caso conserva la funzione che ha nel dominio: se
porta anche una lettura del Mondo, quella lettura non scompare cambiando
cartella, e il confine fra racconto dell'artefatto e interpretazione si decide
nel repo.

## Forma

Reveal, caricato da CDN senza dipendenze installate: l'HTML si apre via
`file://` e la rete serve solo al framework; per l'uso offline Reveal si
vendorizza. Il deck ha un CSS canonico, `deck.css`, uguale in ogni repo — base
pulita sul tema `white`, titoli con barra d'accento, cover, slide `hero` e
tavola —; le classi di dominio vivono in un CSS locale dichiarato in
`CSS_LOCALI`. Le tavole si citano come `assets/<nome>`, hanno la fonte accanto
al deck e la build le copia in `view/assets/`; una tavola che manca rompe la
build.

HTML e CSS nativi bastano per layout e componenti; SVG inline quando serve
controllo geometrico. Motori di diagrammi come Mermaid introducono parser e
dipendenze runtime sproporzionati per un racconto curato e non fanno parte del
pattern di default. Il PDF per stampa o distribuzione esce dall'export del deck
e non si versiona.

Connessioni:

- [view](view.md)
- [output](output.md)
- [interpret](interpret.md)
- [verdict](verdict.md)
- [project-structure](project-structure.md)
- [processing-layers](processing-layers.md)
- [affordance-signifier](affordance-signifier.md)
