---
stato: maturo
---

# Method development

Lo sviluppo del metodo — e di ogni knowledge base — procede per due movimenti complementari, non per uno solo. Il movimento dal basso parte da un'esigenza concreta che nasce mentre si risolve un problema in un dominio: si stabilizza localmente e, se generalizzabile, risale a principio portabile. Il movimento dall'alto parte da un inquadramento teorico importato — un gigante, un concetto, una distinzione — che offre la cornice per vedere, nominare e mettere in ordine ciò che dal basso si avverte come disagio ma non si sa inquadrare.

Ciascun movimento ha un fallimento proprio, ed è il fallimento dell'altro a fare da antidoto. Il dal-basso puro è cieco alla propria disorganizzazione strutturale: può generalizzare solo ciò che è già emerso, mai progettare la forma d'insieme, e come dogma tarpa le ali. Il dall'alto puro impone strutture estranee, sovra-ingegnerizza soluzioni per esigenze immaginate e imbriglia il dominio in una cornice che non gli appartiene. Tenere un solo movimento come regola produce o localismo dogmatico o astrazione imposta.

L'antidoto non è scegliere: è l'alternanza e il contraddittorio tra i due. Il corpo avverte il disordine — lo strato viscerale — la teoria lo nomina — lo strato riflessivo; si scende a verificare la cornice contro i domini reali, si risale a correggerla quando non regge. È il ciclo dell'azione di Norman applicato al metodo stesso, una struttura ad anello e non un cricchetto a senso unico: il gulf of evaluation è il movimento dal basso che legge il mondo, il gulf of execution è il movimento dall'alto che vi imprime un'intenzione. Per questo l'enfasi esclusiva sul dal-basso, pur giusta come guardia contro la sovra-ingegnerizzazione, contraddice il gigante che il metodo ha adottato: va tenuta come uno dei due poli, non come la regola.

Una precisazione contro un equivoco: il «dall'alto» di questo nodo è il top-down del **ciclo di sviluppo** del metodo — la cornice teorica importata che dà forma alla pratica. È distinto dal top-down del **ciclo runtime**, in cui `metodo` disegna il proprio output di canone (prescrizioni o3-runtime, convergenze) e gli adottanti lo recepiscono: quel secondo movimento dall'alto, con pari dignità del bottom-up che emerge dagli adottanti, vive in `cognitive-artifact-design` e `development-meta-cycle`. I due top-down non vanno confusi: uno plasma il metodo, l'altro plasma come gli artefatti adottanti dovrebbero diventare.

## Il confine canone↔adottante: dichiara e taci

La propagazione ha un costo che non va pagato a ogni rotazione interna del canone. Quando un nodo cambia nome o si scompone, finché l'adottante replica nei propri file un inventario dei path interni del metodo, ogni rename si propaga come una bonifica diffusa su `CLAUDE.md`, `README.md` e nodi locali dei quattro repo. È coupling alla **struttura interna** del canone, non alla sua **interfaccia**: l'adottante dipende da come il metodo è organizzato oggi, non solo da ciò che gli serve davvero.

La regola che scioglie il nodo è **dichiara e taci**: l'adottante dichiara _una volta_ l'adozione del metodo come insieme, e altrove collega solo ciò da cui il proprio contenuto dipende davvero. Tre gradi di dipendenza, da non confondere:

- **dipendenza generale** — l'adozione del metodo come tale. Si dichiara una sola volta, nella sezione README canonica (`readme`): riferimento + breve descrizione, il symlink `method/`, e i due poli del ciclo del dominio (Goal e World) sotto heading fissi. Il solo nome di nodo assunto stabile come punto d'aggancio è l'hub `cognitive-artifact-design.md`. Questa è l'**interfaccia**: cambia di rado, è il contratto.
- **connessione intenzionale** — un link diretto a un nodo interno che esprime una dipendenza **semantica** o **operativa** reale: un nodo locale che àncora il proprio concetto a un concetto del metodo, una regola o uno strumento locale che rimanda alla propria specifica canonica, un task che usa un nodo come vincolo o contesto necessario. Resta legittima: è un'informazione locale, non un inventario.
- **coupling accidentale** — da rimuovere: inventari diffusi dei nodi del metodo, elenchi orientativi che duplicano l'hub, richiami aggiunti solo per dire genericamente «questa regola viene dal metodo», path interni copiati in più file senza una funzione locale distinta.

La metrica non è «zero link» ma «zero link senza funzione locale». Il confine è lo stesso dei due movimenti: interfaccia stabile sopra, struttura interna volatile sotto, e l'**ultimo miglio** — quali link tenere, riscrivere o rimuovere — deciso nel repo adottante contro il suo stato reale, perché solo lì si vede se un link porta significato o è rumore. La _forma_ uniforme che la dichiarazione prende vive in `readme`: questo nodo dice _perché_ disaccoppiare, `readme` dice _quale forma_.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [action-cycle](action-cycle.md)
- [augmentation-system](augmentation-system.md)
- [development-meta-cycle](development-meta-cycle.md)
- [processing-layers](processing-layers.md)
- [pace-layering](pace-layering.md)
- [plan](plan.md)
- [knowledge-base](knowledge-base.md)
- [readme](readme.md)
- [design-principles](design-principles.md)
