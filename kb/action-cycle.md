---
data: 2026-05-24
stato: bozza
---

# Action cycle

Modello del rapporto tra utente e sistema secondo Donald Norman, **trasportato nell'agentic loop dell'LLM dentro l'harness**. Non è la voce biografica di Norman — esiste come nodo di dominio in altri progetti adottanti — ma estrae il pattern che rende un sistema usabile e lo trasferisce dal banco di Norman (un umano che agisce su un oggetto) al ciclo che un agente LLM percorre, sessione dopo sessione, dentro un harness: il sistema progettato per chiudere i gulf non è più una caffettiera, è la KB.

Il modello sostiene che ogni interazione produttiva con un sistema passa attraverso sette stadi, divisi in due fasi: esecuzione (formare l'intenzione, pianificarla, specificarla, eseguirla) e valutazione (percepire l'esito, interpretarlo, confrontarlo con l'obiettivo). Lungo entrambe le fasi si aprono distanze cognitive — i due gulf — che il design del sistema deve ridurre. Il metodo eredita questo modello e lo riassegna: l'agente che percorre il ciclo è in primo luogo l'**LLM** (l'umano resta consumatore, soprattutto di o2 — vedi «I due gulf»); il sistema che deve chiudere il ciclo è l'**artefatto versionato**.

Nella cornice di sistema di Engelbart (H-LAM/T, cfr. `augmentation-system`), Norman è la gamba che dà l'**interfaccia col Mondo**: come il sistema rende visibile l'azione possibile, come riceve feedback, come chiude il ciclo. Risolve il «come l'agente agisce» che né Luhmann (produttore solitario di scrittura) né Karpathy (esplorazione e rendering) affrontano. Il resto del nodo è il suo contributo: il ciclo d'azione che il metodo eredita ed estende.

## I sei atti e i due poli

Il modello canonico di Norman procede in sequenza:

- Goal — cosa voglio ottenere
- Plan — come penso di ottenerlo
- Specify — quali azioni concrete servono
- Perform — eseguo l'azione nel mondo
- Perceive — vedo l'esito
- Interpret — capisco cosa significa
- Compare — confronto con il goal iniziale

Nel metodo il ciclo si materializza su due archi simmetrici — output (esecuzione, che scende dalla KB al Mondo) e input (valutazione, che risale dal Mondo alla KB) — con il Goal all'apice e il Mondo in fondo:

- **Plan** → o1 — piano in forma macchina, vicino alla KB
- **Specify** → o2 — vista di decisione per l'umano
- **Perform** → o3 — prescrizione versionata dell'atto
- **Perceive** → i1 — cattura versionata e valenza-neutra del segnale
- **Interpret** → i2 — distillato (nota, sintesi) in `kb/` come nodo bozza
- **Compare** → i3 — conoscenza formalizzata o verdetto; alimenta il prossimo Goal

**Sei atti, due poli.** I sette stadi di Norman non sono dello stesso tipo. Il Goal non è un atto ma uno _stato_ — il punto verso cui si tende; gli altri sei (Plan, Specify, Perform, Perceive, Interpret, Compare) sono _operazioni_. Il metodo rende esplicito ciò che Norman teneva implicito: il secondo polo, il **Mondo**, il fondo verso cui gli atti scendono e da cui risalgono (cfr. `world`). La forma canonica nel metodo è dunque **6 atti + 2 poli**, non sette stadi: sei operazioni che corrono tra Goal (in alto) e Mondo (in basso). I poli non si eseguono, si _costituiscono_ ai bordi — il Goal viene dal motivo (la vita, il committente), il Mondo viene ritagliato dall'infinito per rilevanza guidata dai goal. Ne risultano due triadi speculari, ciascuna stretta attorno a un polo: alta {Compare (i3), Goal, Plan (o1)}, bassa {Perform (o3), Mondo, Perceive (i1)}; in mezzo, alla vita del ciclo, restano i due atti che non toccano nessun polo, Specify (o2) e Interpret (i2). Le due triadi e la vita corrispondono ai tre livelli di elaborazione di Norman — riflessivo in alto, behavioral in mezzo, viscerale al Mondo (cfr. `processing-layers`).

**La KB non è uno stadio.** Né i poli né gli atti _sono_ la KB. La KB è il _system image_ di Norman: il medium attraverso cui gli atti leggono e scrivono, non una stazione del ciclo (cfr. `system-image`). Il ciclo corre tra due poli attraverso due medium persistenti — la KB all'interno, il Mondo all'esterno.

**Lo specchio per altitudine.** I due archi sono speculari, accoppiati per altitudine e non per numero. Il Goal è l'apice; il Mondo è il fondo.

- in basso, alla membrana `world`: **o3 ↔ i1** (Perform ↔ Perceive) —
  prescrizione / cattura, i due riflessi versionati dei due versi;
- in mezzo: **o2 ↔ i2** — vista di decisione / nota interpretata;
- in alto, alla KB: **o1 ↔ i3** — piano strutturato / conoscenza formalizzata.

I numeri sembrano non combaciare (o1 con i3) solo perché contano la distanza dall'inizio dell'arco: l'output scende, l'input risale.

## I due medium e i prodotti del loop

**Le due cerniere hanno la stessa forma:** scrivi-poi-leggi attraverso un medium persistente. Alla cerniera bassa, o3 prescrive l'atto, l'atto modifica `world` e i1 ne cattura un segnale; i due riflessi versionati non sostituiscono il passaggio fisico attraverso la membrana. Il mondo trattiene lo stato nell'intervallo, esattamente come l'artefatto lo trattiene tra i3 e il Goal. La differenza non è nella forma ma nella tenuta: **il mondo persiste da solo, l'artefatto persiste solo se qualcuno lo scrive.** Il mondo si ricorda della mail spedita, della transazione eseguita, del gesto compiuto, che qualcuno lo registri o no; l'artefatto dimentica a meno che l'i3 non depositi l'esito. È il contenuto operativo del principio «una decisione non scritta è una decisione persa» — non un'esortazione morale, ma la conseguenza dell'unico dei due medium che non si mantiene da sé. Per questo l'artefatto ha bisogno di un custode e il mondo no.

**Ciò che l'artefatto trattiene sono i prodotti degli atti.** Ogni atto del ciclo non è solo un'operazione che passa: _deposita un prodotto versionato_, in un luogo proprio dell'atrio — o1 in `plan.md`, o2 in `tasks/`, o3 nei commit e in `prescriptions/`, i1 in `perceptions/`, i2 nei nodi `kb/` e in `interpretations/`, i3 in `verdict.md` (la mappa-sorgente completa è in `action-cycle-matrix`). Anche i poli trattengono stato: il Goal è scritto (`README`, `development-goal`), e il Mondo «remembers by being there». Nessuno stadio del loop è effimero: ciascuno _è_ e _contiene_ il prodotto dell'agire.

**Divisi, aperti, consultabili.** Tenere questi prodotti separati — non collassati in un unico blob né chiusi nella testa di chi ha agito — è il punto in cui il ciclo d'azione tocca la **cognizione condivisa**: il pavimento ontologico (Hutchins/Clark/Norman) vive in `cognitive-system`, qui se ne legge la materializzazione lungo i sei atti. È l'applicazione al loop del «007 principle» di Clark — lascia l'informazione nel mondo e recuperala quando serve, invece di immagazzinarla tutta dentro: il ragionamento del loop non sta nella mente di un agente, sta esternalizzato e separato nei prodotti dell'atrio. Per l'LLM, che riparte da zero a ogni sessione e per cui la KB _è_ il modello mentale (cfr. l'asimmetria umano/LLM in `cognitive-system`), i prodotti separati sono l'unico modo di rientrare nel ciclo senza ricostruirlo da capo; per l'agente umano sono i **punti di controllo**, i punti dove ispezionare il loop e intervenire.

**La separazione è ciò che rende il loop auto-correggibile.** L'arco di input può rileggere i prodotti dell'arco di output e confrontarli con il Goal — Compare (i3) verifica Plan (o1), Interpret (i2) rilegge ciò che è stato prescritto e fatto — solo se quei prodotti esistono distinti e leggibili.

## I due gulf

Norman chiama gulf of execution la distanza tra "so cosa voglio" e "so come farlo col sistema"; gulf of evaluation la distanza tra "il sistema mostra X" e "capisco cosa significa per me". Sono i due punti critici dove il design fallisce o riesce.

Nel metodo i due gulf si traducono così — e l'agente che li attraversa è in primo luogo l'LLM che riprende il lavoro a freddo, sessione dopo sessione:

- o1 (output macchina) riduce il gulf of execution per l'LLM che continua il lavoro tra sessioni: trova subito le scadenze, lo stato, i fatti strutturati, senza dover ricostruire il modello da capo
- o2 (output decisione) riduce entrambi i gulf per l'utente umano: termometro, schema, raccomandazioni leggibili in cinque secondi (execution); feedback chiaro che traduce l'esito in significato (evaluation)
- o3 riduce il gulf of execution prescrivendo l'atto con la precisione
  necessaria; l'azione effettiva accade in `world`
- i1/i2/i3 riducono il gulf of evaluation: catturano il segnale, gli
  attribuiscono significato e lo formalizzano

**Dove il ciclo si rompe.** Il guasto più insidioso non vive nel ciclo runtime ma nel gulf of evaluation del ciclo di sviluppo: una decisione viene eseguita (il commit parte, gulf of execution attraversato) ma la sua _assunzione_ non viene formalizzata e ri-valutata. Quando il significato dei dati su cui poggiava cambia, niente costringe a riaprirla, e l'assunzione stale si materializza mesi dopo come comportamento errato nel mondo. Nel caso `bi`/1018022 un commit di compatibilità ripristinò un comportamento storico ("presente nei backorders ⇒ esiste un fornitore esterno") dopo che il modello dati aveva cambiato significato — la sorgente interna magazzino era entrata nei backorders. La decisione visse nel messaggio di commit, non in `verdict.md`: il gulf of execution fu attraversato, quello di evaluation no, e l'assunzione esplose come oversell quando un cliente comprò due pezzi contro una giacenza di uno. Il presidio di questo guasto è un check di fedeltà cognitiva (cfr. `cognitive-fidelity`).

## Saltare uno stadio: la perdita di controllo

Il modello di Norman non è qui solo descrittivo: è lo **strumento teorico con cui si progetta il metodo** — l'_harness di secondo livello_, non l'infrastruttura tecnica (L1) ma la rappresentazione che la sovrasta (L2 in `cognitive-system`) e che dà forma all'interazione tra agente umano e agente artificiale. Da questa tesi discende un corollario operativo netto: **il loop va percorso intero; saltare uno o più stadi crea danno e fa perdere il controllo — a entrambi gli agenti.**

Non è completezza estetica. Ogni stadio saltato è un prodotto non depositato, e il prodotto mancante rompe la catena della cognizione condivisa proprio dove servirebbe il controllo. L'**agente artificiale** che salta o1/o2 — pianifica e specifica nella propria testa invece che nell'artefatto — agisce su un modello mentale che evapora a fine sessione: alla ripresa non ha appiglio, ricostruisce a caso, drifta. L'**agente umano** che non trova il prodotto di uno stadio perde il suo punto di controllo: non si ispeziona né si corregge ciò che non è stato deposto. Il caso `bi`/1018022 appena visto è esattamente uno stadio saltato — i3: la decisione visse nel commit, non in `verdict.md`, e nessuno dei due agenti poté riaprirla finché l'assunzione stale non esplose nel mondo. È la forma tipica del guasto, non un'eventualità remota.

## Feedforward e feedback

Ciascun atto è il punto in cui un agente si pone una domanda — _quali alternative?_ (Plan), _cosa posso fare ora?_ (Specify), _come?_ (Perform), _cosa è successo?_ (Perceive), _cosa significa?_ (Interpret), _va bene?_ (Compare) — e ogni domanda è un tema di design: il sistema è ben progettato se fornisce l'informazione per rispondervi. I poli tacciono in modo diverso: il Goal ha la sua domanda (_cosa voglio realizzare?_) ma a provenienza aperta (da dove venga il goal Norman non lo dice, è il confine aperto di `goal`); il Mondo non ha domanda, è il terreno muto, la scatola nera che l'annidamento apre.

Il design risponde a queste domande con vincoli, mapping, significanti, modelli concettuali, feedback e visibilità (cfr. `constraint`, `affordance-signifier`, `system-image`). Norman distingue l'informazione per direzione: il **feedforward** risponde alle domande di esecuzione (cosa posso fare, come), il **feedback** a quelle di valutazione (cosa è successo, cosa significa, va bene). Nel metodo i due archi portano esattamente queste due informazioni: l'arco output (o1/o2/o3) è il feedforward che colma il gulf of execution; l'arco input (i1/i2/i3) è il feedback che colma il gulf of evaluation. Il criterio che ne segue, valido per ogni componente del repo: questo file dà l'informazione per rispondere alla domanda del suo stadio?

## Cicli annidati e le quattro dimensioni

Il ciclo d'azione del metodo non è uno solo: sono due, annidati, ciascuno lo specchio simmetrico appena descritto, distinti per _cosa sia il loro Mondo_ in fondo — la realtà per il ciclo runtime, l'artefatto stesso per il ciclo di sviluppo. L'incastro è che il Mondo del ciclo di sviluppo, costruito e modificato dall'o3-sviluppo, _diventa_ la macchina che esegue il ciclo runtime: è il senso in cui il metodo _estende_ Norman invece di applicarlo soltanto — Norman dà il Mondo come scatola nera, il metodo la apre. La trattazione piena (i due Mondi, la cucitura contro l'affiancamento, l'estensione agli adottanti) vive in `nested-cycles`; il Goal che si sdoppia con esso, in `development-goal`.

Riconosciuti specchio e annidamento, ogni elemento del metodo si colloca su quattro dimensioni _ortogonali_: **agente** (umano / LLM), **annidamento** (runtime / sviluppo), **livello** (1 macchina, 2 decisione, 3 Mondo), **lato del cappio** (output / input). Collassarne due — livello e agente — è l'errore che aveva fatto «sparire» o1. La matrice che ne risulta è la lente per confrontare i progetti adottanti, ed è il compito di `action-cycle-matrix`.

## Le quattro proprietà cardine come criteri di qualità per o2

Norman riassume il buon design in quattro proprietà. Diventano direttamente criteri di valutazione per o2 (output decisione):

- **Visibilità** — tutti gli stati attivi sono percepibili a colpo d'occhio nell'overview, niente di rilevante è nascosto
- **Feedback** — dopo ogni evento il sistema mostra l'esito in modo evidente; non serve indagine per sapere cosa è cambiato
- **Mapping** — la disposizione visiva corrisponde alla struttura reale del dominio, non a un ordine convenzionale
- **Constraint** — la struttura del file impedisce di dimenticare le parti che servono insieme (es. raccomandazioni accanto allo stato)

Esempio applicato: nel `quadro/quadro-corporeo.md` di `salute` la visibilità è garantita dalla tabella overview che mostra tutte le aree attive con banda e score; il feedback dal fatto che dopo ogni evento il termometro si aggiorna; il mapping dal colore proporzionato alla banda di allarme; la constraint dalla struttura del file area, che costringe a dichiarare prossimi step e raccomandazioni accanto allo stato.

## Norman come critico del metodo

Provocazione utile: Norman guarderebbe il metodo allo stato precedente lo strato output e direbbe — "hai una KB profondissima e nessuna affordance". Il sapere c'era, ma non invitava all'azione. Le scadenze in un file, le raccomandazioni operative sparse nei nodi `kb/`, lo stato dei controlli mescolato alla cronologia in nodi come `storia-clinica.md`, nessun termometro. Il gulf of execution tra "so che dovrei meditare" e "medito stamattina" enorme, e niente nella KB lo riduceva.

È la critica che Norman fa al design "centrato su sé stesso": un oggetto può essere splendido — la KB lo è — ed essere comunque mal progettato dal punto di vista di chi ci agisce dentro. Lo strato output del metodo nasce dal riconoscere questa lacuna.

Una conseguenza forte di questa critica, che resta come principio di valutazione: **se l'utente non agisce, la KB è mal progettata, non l'utente è pigro**. Lo strato output va dunque valutato sui criteri di Norman, non sulla bellezza dei nodi che già esistono.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_ (1988), edizione italiana _La caffettiera del masochista_; in particolare il capitolo sull'action cycle
- Norman, _Emotional Design_ (2004), _Living with Complexity_ (2010)
- Voce biografica e di dominio: `salute/kb/donald-norman.md` nei progetti adottanti

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [constraint](constraint.md)
- [system-image](system-image.md)
- [processing-layers](processing-layers.md)
- [output](output.md)
- [input](input.md)
- [perceive](perceive.md)
- [interpret](interpret.md)
- [specify](specify.md)
- [perform](perform.md)
- [compare](compare.md)
- [goal](goal.md)
- [development-goal](development-goal.md)
- [world](world.md)
- [nested-cycles](nested-cycles.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [augmentation-system](augmentation-system.md)
- [cognitive-system](cognitive-system.md)
- [karpathy-pattern](karpathy-pattern.md)
- [zettelkasten](zettelkasten.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
