---
data: 2026-05-24
stato: bozza
---

# Action cycle

Modello del rapporto tra utente e sistema secondo Donald Norman, distillato come fondamento metodologico per lo strato di output del metodo. Non è la voce biografica di Norman — esiste come nodo di dominio in altri progetti adottanti — ma estrae il pattern che rende un sistema usabile e lo collega al ciclo dell'azione che il metodo deve sostenere.

Il modello sostiene che ogni interazione produttiva con un sistema passa attraverso sette stadi, divisi in due fasi: esecuzione (formare l'intenzione, pianificarla, specificarla, eseguirla) e valutazione (percepire l'esito, interpretarlo, confrontarlo con l'obiettivo). Lungo entrambe le fasi si aprono distanze cognitive — i due gulf — che il design del sistema deve ridurre. Il metodo eredita questo modello per progettare l'artefatto così che chiuda davvero il ciclo, non solo che lo descriva.

## Norman dentro la cornice di sistema

Il metodo non si appoggia a tre pilastri pari: si inscrive in una **cornice di sistema** — l'_augmentation system_ di Engelbart (H-LAM/T) — che _contiene_ i giganti invece di affiancarli. La trattazione piena della cornice e di ciò che vi sta dentro e sotto vive in `augmentation-system`; qui basta collocare Norman al suo posto. Dentro la cornice, **Luhmann / Zettelkasten** dà l'unità atomica (il means _Language_): come è fatto il singolo nodo, come si lega, perché la sintesi non sta nel nodo. La gamba di **manutenzione** — chi tiene aggiornato il sistema, ingest/query/lint, come l'LLM compone la KB — è il _Methodology/Training_ engelbartiano, di cui Karpathy è l'**istanza contemporanea**, non un pilastro a sé (cfr. `karpathy-pattern`).

**Norman** è l'**interfaccia col Mondo**: come il sistema rende visibile l'azione possibile, come riceve feedback, come chiude il ciclo. Risolve il "come l'utente agisce" che né Luhmann né Karpathy affrontano — Luhmann era un produttore solitario di scrittura, Karpathy parla di esplorazione e rendering; nessuno dei due ha pensato esplicitamente al ciclo di azione tra utente e sistema, che è esattamente il problema dello strato output e del filing back. Il resto di questo nodo è il contributo di Norman: il ciclo d'azione che il metodo eredita ed estende.

## I sette stadi del ciclo di azione

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

I numeri sembrano non combaciare (o1 con i3) solo perché contano la distanza dall'inizio dell'arco: l'output scende, l'input risale. o1 e o2 non sono lo stesso stadio rivolto a due agenti, come una formulazione precedente diceva: sono due _altitudini_ dell'arco di output. Il loro consumatore (LLM per o1, umano per o2) è una dimensione ortogonale all'altitudine — vedi «Le quattro dimensioni» più sotto.

**Le due cerniere e la loro vera asimmetria.** Le due cerniere hanno la _stessa_
forma: scrivi-poi-leggi attraverso un medium persistente. Alla cerniera bassa,
o3 prescrive l'atto, l'atto modifica `world` e i1 ne cattura un segnale; i due
riflessi versionati non sostituiscono il passaggio fisico attraverso la
membrana. Il mondo trattiene lo stato nell'intervallo, esattamente come la KB lo
trattiene tra i3 e il Goal.

L'asimmetria reale è altrove: **il mondo persiste da solo, la KB persiste solo se qualcuno la scrive.** Il mondo si ricorda della mail spedita, della transazione eseguita, del gesto compiuto, che l'artefatto faccia altro o no; la KB dimentica a meno che l'i3 non depositi l'esito. È il contenuto operativo del principio «una decisione non scritta è una decisione persa» — non un'esortazione morale, ma la conseguenza dell'unico dei due medium che non si mantiene da sé. Per questo la KB ha bisogno di un custode e il mondo no.

## i2 micro e i2 macro: il deck come cerniera

L'atto Interpret (i2) non ha una sola scala. Nel ciclo per-nodo, i2-**micro** è la
singola nota bozza che distilla un i1 — un referto, un export, un segnale — l'istanza
minima descritta sopra (Interpret → nodo bozza in `kb/`). Ma esiste anche un
i2-**macro**: la sintesi periodica che rilegge l'intero artefatto e rivela tensioni
non-locali tra nodi, invisibili da dentro ciascun nodo preso singolarmente. È il ruolo
di `interpretations/`: ogni sezione del deck è un'interpretazione i2-macro, non un nodo
bozza.

Per `method`, il cui Mondo di sviluppo è la KB stessa, il deck rivela dove i nodi
si contraddicono o si completano. Nei progetti adottanti (`bi`, `economia`,
`salute`), la stessa superficie interpreta dati del Mondo runtime secondo i goal.
In entrambi i casi è o2 quando viene prodotta come vista di decisione e substrato
i2 quando viene letta per capire cosa la sintesi significa. La cerniera non è
quindi una differenza di ruolo tra repository, ma il doppio verso dello stesso
artefatto nel ciclo.

Esempio concreto, dal pilota di salute. Esecuzione: leggi il quadro corporeo, vedi che il termometro su aneurisma è giallo, decidi di rispettare le raccomandazioni, agisci (cammini, mangi meno). Valutazione: la visita di controllo a novembre 2026 produce un nuovo referto (i1), che viene distillato in una nota (i2), che aggiorna `storia-clinica` (i3), che ridipinge il termometro nel quadro (→ nuovo Goal).

## I due gulf

Norman chiama gulf of execution la distanza tra "so cosa voglio" e "so come farlo col sistema"; gulf of evaluation la distanza tra "il sistema mostra X" e "capisco cosa significa per me". Sono i due punti critici dove il design fallisce o riesce.

Nel metodo i due gulf si traducono così:

- o1 (output macchina) riduce il gulf of execution per l'LLM che continua il lavoro tra sessioni: trova subito le scadenze, lo stato, i fatti strutturati, senza dover ricostruire il modello da capo
- o2 (output decisione) riduce entrambi i gulf per l'utente umano: termometro, schema, raccomandazioni leggibili in cinque secondi (execution); feedback chiaro che traduce l'esito in significato (evaluation)
- o3 riduce il gulf of execution prescrivendo l'atto con la precisione
  necessaria; l'azione effettiva accade in `world`
- i1/i2/i3 riducono il gulf of evaluation: catturano il segnale, gli
  attribuiscono significato e lo formalizzano

## Le sette domande, feedforward e feedback

Ciascuno dei sette stadi è il punto in cui un agente si pone una domanda, e ogni domanda è un tema di design: il sistema è ben progettato se fornisce l'informazione per rispondervi.

- Goal — cosa voglio realizzare?
- Plan — quali sono le alternative?
- Specify — cosa posso fare ora?
- Perform — come lo faccio?
- Perceive — cosa è successo?
- Interpret — cosa significa?
- Compare — va bene?

Il Mondo, ottavo elemento del metodo, non ha domanda: è il terreno muto. Anche i due poli tacciono in modo diverso — il Goal ha la sua domanda ma a provenienza aperta (da dove venga il goal Norman non lo dice, è il confine aperto di `goal`), il Mondo tace del tutto (è la scatola nera che l'annidamento apre).

Il design risponde a queste domande con vincoli, mapping, significanti, modelli concettuali, feedback e visibilità (cfr. `constraint`, `affordance-signifier`, `system-image`). Norman distingue l'informazione per direzione: il **feedforward** risponde alle domande di esecuzione (cosa posso fare, come), il **feedback** a quelle di valutazione (cosa è successo, cosa significa, va bene). Nel metodo i due archi portano esattamente queste due informazioni: l'arco output (o1/o2/o3) è il feedforward che colma il gulf of execution; l'arco input (i1/i2/i3) è il feedback che colma il gulf of evaluation. Il criterio che ne segue, valido per ogni componente del repo: questo file dà l'informazione per rispondere alla domanda del suo stadio?

## Cicli annidati: due specchi, due Mondi

Il ciclo d'azione del metodo non è uno solo: sono due, annidati, ciascuno lo
specchio simmetrico appena descritto, distinti per _cosa sia il loro Mondo_ in
fondo — la realtà per il ciclo runtime, l'artefatto stesso per il ciclo di
sviluppo. L'incastro è che il Mondo del ciclo di sviluppo, cioè l'artefatto
costruito e modificato dall'o3-sviluppo, diventa la macchina che esegue il ciclo
runtime: l'artefatto versionato è ciò che poi opera nel runtime. È il senso in cui il metodo
_estende_ Norman invece di applicarlo soltanto — Norman dà il Mondo come scatola
nera, il metodo la apre. La trattazione piena — i due Mondi e i due poli, la
cucitura contro l'affiancamento, la ricaduta sull'atrio, l'estensione agli
adottanti — vive nel nodo dedicato `nested-cycles`.

## Le quattro dimensioni di un elemento del metodo

Una volta riconosciuti specchio e annidamento, ogni elemento del metodo si colloca su quattro dimensioni _ortogonali_ — e l'errore di collassarne due (livello e agente) è ciò che aveva fatto «sparire» o1:

1. **agente** — umano oppure LLM (il modello, non l'harness)
2. **annidamento** — ciclo runtime (agisce sul mondo) oppure ciclo di sviluppo (agisce sull'artefatto)
3. **livello** — 1 (macchina, vicino alla KB), 2 (decisione), 3 (al Mondo)
4. **lato del cappio** — output (esecuzione, discesa) oppure input (valutazione, risalita)

La matrice che ne risulta è la lente per confrontare i progetti adottanti: per ogni dominio si legge cosa è sviluppato, cosa manca perché non serve (es. `nixos` ha poco esogeno sul lato input runtime), e cosa manca ma servirebbe. Sostituisce sia il taglio rigido «stadi divisi per agente» sia la fotografia piatta dello stato dei progetti.

**Dove si rompe.** Il guasto più insidioso non vive nel ciclo runtime ma nel gulf of evaluation del ciclo di sviluppo: una decisione viene eseguita (il commit parte, gulf of execution attraversato) ma la sua _assunzione_ non viene formalizzata e ri-valutata. Quando il significato dei dati su cui poggiava cambia, niente costringe a riaprirla, e l'assunzione stale si materializza mesi dopo come comportamento errato nel mondo. Nel caso `bi`/1018022 un commit di compatibilità ripristinò un comportamento storico ("presente nei backorders ⇒ esiste un fornitore esterno") dopo che il modello dati aveva cambiato significato — la sorgente interna magazzino era entrata nei backorders. La decisione visse nel messaggio di commit, non in `verdict.md`: il gulf of execution fu attraversato, quello di evaluation no, e l'assunzione esplose come oversell quando un cliente comprò due pezzi contro una giacenza di uno. Il presidio di questo guasto è un check di fedeltà cognitiva (cfr. `cognitive-fidelity`).

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
- [world](world.md)
- [nested-cycles](nested-cycles.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [augmentation-system](augmentation-system.md)
- [karpathy-pattern](karpathy-pattern.md)
- [zettelkasten](zettelkasten.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [knowledge-base](knowledge-base.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
