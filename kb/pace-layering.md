---
stato: maturo
---

# Pace layering

Pace layering è il principio per cui un sistema complesso e durevole non cambia tutto alla stessa velocità: è composto da strati con frequenze di cambiamento diverse, e la sua salute nasce dall'accoppiamento tra strati lenti e strati veloci, non dal bloccare il cambiamento. Gli strati lenti danno stabilità, continuità e memoria; gli strati veloci danno innovazione, adattamento e apprendimento. Un sistema sano lascia che gli strati veloci sperimentino e che gli strati lenti assorbano solo ciò che ha retto la prova, mantenendo i due accoppiati ma disaccoppiati nel ritmo.

Il principio chiarisce un criterio che il metodo usava in forma debole sotto il nome di "conoscenza stabile". "Stabile" non è una proprietà assoluta: niente in una KB viva è immutabile, perché il metodo stesso è in evoluzione continua. Stabile è un grado, non uno stato — una frequenza di cambiamento più bassa rispetto ad altri componenti. Una knowledge base non ha uno strato eterno e uno volatile: ha un gradiente. La mappa del dominio e la struttura del progetto cambiano lentamente; i nodi cambiano a frequenza media; il plan, i dettagli operativi e il verdict cambiano a ogni sessione. Collocare bene un artefatto significa riconoscerne la velocità, non la sua importanza: un componente lento e uno veloce vanno tenuti in posti diversi anche quando parlano della stessa cosa.

Da qui il criterio operativo che mancava per decidere dove vive una cosa. Mettere un artefatto veloce dentro uno strato lento, o un artefatto lento dentro uno strato veloce, genera attrito: un catalogo che cambia a ogni sessione non appartiene allo stesso luogo di un nodo concettuale che cambia una volta al mese. Lo sviluppo bottom-up del metodo è pace layering in azione: gli strati veloci propongono il cambiamento mentre si risolve un problema concreto in un repo adottante, gli strati lenti lo dispongono attraverso il filing back solo quando è diventato una generalizzazione portabile. Gli strati veloci imparano, gli strati lenti ricordano.

Brand fonda il caso architettonico sul lavoro di Frank Duffy: un edificio non è una cosa unica, ma una sovrapposizione di componenti con longevità diversa. Duffy distingue Shell, Services, Scenery e Set; Brand li traduce ed espande nei sei strati Site, Structure, Skin, Services, Space plan e Stuff. Il punto trasferibile non è la lista edilizia in sé, ma la relazione tra ritmi: Site e Structure sono lenti e vincolanti, Stuff e Space plan sono veloci e sperimentali, Services e Skin stanno nel mezzo. Quando gli strati sono troppo incollati, i lenti bloccano il flusso dei veloci e i veloci lacerano i lenti con cambiamenti continui. Un artefatto adattivo lascia quindi "slippage" tra strati: abbastanza connessione da funzionare come sistema, abbastanza separazione da permettere a ogni strato di cambiare alla propria frequenza.

La dinamica è bidirezionale. Gli strati lenti dominano il comportamento ordinario del sistema: vincolano ciò che gli strati veloci possono fare. Ma gli strati veloci sono il luogo della variazione e della prova; quando una variazione veloce si ripete abbastanza, può risalire e trasformare uno strato più lento. In _The Clock of the Long Now_, Brand generalizza questa grammatica alla civiltà: fashion/art, commerce, infrastructure, governance, culture, nature. Gli strati veloci innovano e imparano; quelli lenti stabilizzano, ricordano e impongono continuità. Nel metodo questo distingue bene esperimento, adozione e filing back: il lavoro di sessione e i repo adottanti propongono; il metodo portabile dispone solo dopo che un cambiamento ha mostrato tenuta oltre il caso locale.

Fonti:

- Frank Duffy, architetto, origine dell'idea che un edificio sia una sovrapposizione di strati a diversa longevità ("shearing layers")
- Stewart Brand, _How Buildings Learn: What Happens After They're Built_ (1994), cap. 2 "Shearing Layers": espande Duffy nei sei strati Site, Structure, Skin, Services, Space plan, Stuff; formula il vincolo dei lenti sui veloci, la risalita dei veloci nei lenti e l'imperativo progettuale di lasciare slittamento tra sistemi a passo diverso
- Stewart Brand, _The Clock of the Long Now_ (1999), cap. "The Order of Civilization": generalizza il concetto alla civiltà come scala Fashion/art, Commerce, Infrastructure, Governance, Culture, Nature e condensa la dinamica in "fast learns, slow remembers" e "fast proposes, slow disposes"

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [project-structure](project-structure.md)
- [knowledge-base](knowledge-base.md)
- [design-principles](design-principles.md)
- [plan](plan.md)
- [verdict](verdict.md)
