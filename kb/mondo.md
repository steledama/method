---
data: 2026-06-09
stato: bozza
---

# Mondo

Il fondo del ciclo d'azione: il polo opposto al Goal. Se il Goal è l'apice da cui scende l'esecuzione e a cui risale la valutazione, il Mondo è il luogo in basso dove l'azione produce effetti reali e da cui ritorna il segnale. È la cerniera Mondo del cappio — o3 scrive un effetto (Perform), i1 lo rilegge come segnale (Perceive): il mondo trattiene lo stato nell'intervallo, ed è scrivi-poi-leggi attraverso un medium, non riflesso immediato. La differenza con la cerniera KB non sta nella forma ma nel medium: il mondo persiste da sé, la KB solo se scritta (cfr. `ciclo-azione`). Tutto ciò che l'artefatto percepisce, interpreta e confronta rispetto agli obiettivi entra da qui.

In Norman il Mondo è la scatola nera che risponde all'azione: il ciclo descrive come l'utente agisce sull'artefatto e ne valuta la risposta, ma il Mondo resta dato, non aperto. Il metodo estende Norman proprio su questo punto. L'annidamento dei cicli sdoppia il Mondo: il _Mondo runtime_ è la realtà su cui l'artefatto agisce (un'email inviata, una transazione, un payload pubblicato, un gesto corporeo); il _Mondo di sviluppo_ è l'artefatto stesso, su cui si agisce con un commit e di cui si percepisce la risposta come lint, audit, test, errore. Ogni sistema runtime è l'o3 di un ciclo di sviluppo che lo precede: il metodo apre la scatola nera che Norman lasciava chiusa.

Il Mondo è l'elemento più specifico al dominio dell'intero ciclo. La meccanica — sette stadi, due archi speculari, due cerniere — è invariante tra i progetti adottanti; ciò che cambia è di che cosa è fatto il Mondo e quali segnali ne entrano. Per questo nominare il Mondo di ciascun artefatto è il modo concreto di intercalare lo stesso ciclo astratto su domini diversi: lo stesso schema d'azione, applicato a corpi-e-mente, a conti correnti, a host e reti, a cataloghi fornitori. Il Mondo è anche la sorgente della valenza: le cattive notizie vengono da qui, e l'artefatto è ben progettato solo se riesce a portarle senza filtrarle — è il vincolo che lega il Mondo alla fedeltà cognitiva e alla neutralità di valenza dell'i2.

## Il Mondo nei progetti adottanti

L'elenco nomina, per ciascun artefatto, di cosa è fatto il Mondo e i due versi della cerniera che lo tocca: l'input grezzo (i1) che ne entra per essere percepito e interpretato, e l'azione (o3) che vi ritorna producendo effetti reali. i1 e o3 stanno insieme nello stesso nodo perché o3 non si comprende se non in relazione al Mondo — nasce nell'artefatto e finisce fuori di esso. Gli stadi intermedi (i2/i3 sull'arco di input, o1/o2 su quello di output) vivono nello strato output; il goal contro cui gli input sono confrontati vive nel nodo Goal.

- **`salute`** — di cosa è fatto il Mondo: il corpo, la mente, le visite mediche, le sessioni di yoga e meditazione, i sintomi, gli stati mentali. Input i1: referti delle visite, sintomi percepiti, stati mentali, esiti delle pratiche. Azione o3: sessioni di yoga e meditazione svolte, controlli fatti, scelte alimentari, conversazioni mediche.
- **`economia`** — di cosa è fatto il Mondo: conti correnti, commercialisti, amministratori di condominio, Agenzia delle Entrate, agenti immobiliari. Input i1: movimenti bancari, bollette, solleciti di pagamento, scadenze fiscali, mail degli agenti immobiliari. Azione o3: email inviate, telefonate, incontri preparati e tenuti, transazioni programmate ed eseguite.
- **`nixos`** — di cosa è fatto il Mondo: i 5 PC, le due reti, lo storage su disco, la capacità computazionale dei singoli host. Input i1: bug, messaggi di errore, lentezze e appesantimenti, aggiornamenti disponibili. Azione o3: deploy e switch applicati, sistema in esecuzione, aggiornamenti installati.
- **`bi`** — di cosa è fatto il Mondo: i fornitori, l'abbinatore, i siti e-commerce col plugin ttimport, il gestionale Danea. Input i1: cataloghi dei fornitori, esportazioni dati da Danea, abbinamenti. Azione o3: payload di disponibilità e prezzi pubblicato al plugin, aggiornamenti dell'intero catalogo inviati ai siti.

## Il Mondo del metodo

`metodo` è un meta-artefatto e per questo ha due Mondi distinti, che l'annidamento dei cicli tiene separati. Il suo _Mondo runtime_ sono i progetti adottanti: quando il metodo agisce — un nodo cambia e propaga via symlink o fork — l'effetto atterra lì, e il segnale che ne ritorna come i1 è l'esigenza che emerge dal basso mentre un repo concreto risolve un problema, insieme al drift e alle convergenze che l'osservatorio rileva. Il movimento bottom-up dello sviluppo del metodo è esattamente la percezione di questo Mondo. Il suo _Mondo di sviluppo_ sono invece i nodi `kb/` e la loro coerenza: un commit agisce sui nodi, lint e audit ne percepiscono la risposta. Dire che «il Mondo del metodo sono i nodi `kb/`» nomina solo il secondo e tace il primo; è il Mondo runtime — i progetti adottanti — a dare al metodo il suo motivo.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [goal](goal.md)
- [output](output.md)
- [input](input.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [osservatorio-metodo](osservatorio-metodo.md)
- [sviluppo-metodo](sviluppo-metodo.md)
