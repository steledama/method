---
ciclo: dev
---

# Le skill si tagliano per arco, non per indice: `eval` ed `exec` tripartite come il modello

Deciso il 2026-07-31 (custode). Il quartetto operativo si ritaglia lungo il
modello di Norman invece che lungo la storia della sua crescita: `plan-review` e
`verdicts-review` diventano **`exec`** ed **`eval`**, ciascuna con i tre
stadi del proprio arco dichiarati e invocabili come scope. Il lavoro vive nel
task «Skill per arco: `eval` ed `exec` tripartite» (`o2/`); qui resta il
verdetto e la clausola di uscita.

**Il movimento è dall'alto, ed è legittimo.** Non è il caso «costruire per un
futuro immaginato» che il dal-basso presidia: `method-development` dichiara i due
movimenti in alternanza e dà al dall'alto pari dignità proprio nella funzione di
**importare la cornice che dà forma a un disagio che dal basso si sente ma non si
sa inquadrare**. Il disagio c'era, in due segnali indipendenti: `verdicts-review`
cresceva per accrescimento (quattro domande, poi cinque, più la bonifica del plan
e due handoff), e la valutazione della percezione «il verdetto è più sicuro del
materiale» ha mostrato che le tesi sbagliate **propagano in `i2/` e nessuno le
insegue** (`verdetto-piu-sicuro-del-materiale`). La cornice che inquadra entrambi
è il ciclo di Norman applicato alla lettera.

**La diagnosi: il nome nominava uno stadio, il corpo ne faceva tre.** La regola
vigente — ogni review porta il nome dell'indice che tiene onesto (`plan-review` :
`o1/plan.md`, `verdicts-review` : `i3/verdicts.md`) — era vera quando la skill
teneva onesto _un_ indice. Non lo è più: `plan-review` copre o1 e o2 (più un
presidio leggero su o3), `verdicts-review` copre i3 e già una parte di i1 (i
segnali orfani). E gli stadi che si sono degradati — **i1, i2, o3** — sono
esattamente quelli che nessun nome nominava. Non è coincidenza: ciò che il
signifier non dichiara è ciò che nessuno mantiene. È la stessa diagnosi della
rinomina `tasks-review`→`plan-review`, applicata un livello più su.

**Il taglio: due capacità, sei scope.** Non sei skill separate — l'arco vale come
sequenza, e il protocollo post-evento (percezione → verdetto → piano) è già
canone: spezzarlo in sei decisioni di invocazione lo dissolverebbe. Vale invece
il pattern multi-scope già collaudato (`aggiorna ia|casa|lavoro|docker|all` in
`nixos`, `ordini <fornitore>` in `bi`), con la regola di fissione intatta — si
spezza se diverge la capacità, mai per ritmo:

- `eval [perceive|interpret|compare|all]`
- `exec [plan|specify|perform|all]`

Conferma che il taglio è quello vero: **l'argomento di scope è il nome
dell'atomo, che è il nome dell'indice della collezione** (`eval interpret` →
`kb/interpret.md` → `i2/interpretations.md`). Nessuna nomenclatura nuova da
inventare — modello, cartelle, nodi e skill si chiamano già allo stesso modo.

**I nomi digitati sono `eval` ed `exec`** (custode, 2026-08-01). Le canoniche
portano l'arco del modello in inglese — il telos è portare il metodo intero,
KB compresa, in inglese — nella forma abbreviata che la mano digita ogni
giorno; Evaluate/Execute sopravvivono solo come nomi degli archi nel canone,
mai come nome della skill. Gli scope-stadio restano per esteso (la catena
atomo→indice non si abbrevia); gli scope di dominio restano nel vocabolario
del loro Mondo (`exec aggiorna`, `eval posta`).

**Il quartetto resta un quartetto**, ritagliato: due archi (`eval`,
`exec`), un'ala (`kb-review`, che sta fuori dai due archi perché `kb/` è
un'ala trasversale al ciclo), un gate (`commit`). Il conteggio non cresce, cresce
la copertura.

**Cambia la natura, e va detto.** Il canone dichiara oggi che il quartetto
distingue diagnosi, supervisione e prevenzione. Le due skill nuove sono **verbi
dell'atto**, non review: `eval perceive` raccoglie i marker, la posta e i
log, non ispeziona `i1/`. Nulla della supervisione si perde però: «è ancora vero
rispetto al segnale?» **è** la domanda di Compare, e l'igiene della coda **è**
Plan. Le procedure esistenti non si buttano, si rifilano sotto il loro stadio, e
si guadagna il posto per ciò che oggi non ha casa (i1, i2, o3).

**Perché la tripartizione non è pedanteria.** I tre episodi di
`verdetto-piu-sicuro-del-materiale` non erano errori di giudizio: erano **passi
non separati**. Chi ha scritto la tesi sulla coincidenza è andato dal materiale
grezzo alla conclusione in un movimento solo — non c'è stato un i2 esplicito,
quindi non c'era niente da rivedere. Separare gli stadi rende **ispezionabile**
un passaggio che altrimenti avviene dentro la testa (o dentro il contesto del
modello) e non lascia traccia. Il costo è scrivere di più; il ricavo è che
l'artefatto può correggersi da solo, ed è la differenza tra metodo e
improvvisazione.

## Le due gambe deboli, dichiarate

**`exec perform` non è simmetrico a `eval perceive`.** Sul braccio di
valutazione i tre stadi lavorano tutti su collezioni dell'artefatto; sul braccio
di esecuzione il terzo stadio tocca il Mondo (`aggiorna` fa switch su host
reali, `categorizza` scrive su PROD). Il canone (ratifica del custode,
2026-08-01) dà a `exec perform` due piani: la **supervisione della
collezione o3** — prescrizioni consumate potate, strumenti dichiarati ancora
eseguibili — e **l'atto stesso quando l'autorizzazione già lo copre**: l'atto
locale, reversibile e autorizzato lo compie davvero; ciò che tocca il Mondo
senza autorità produce o valida la prescrizione e si ferma al confine. Non è
un'estensione teorica: `aggiorna ia` in `nixos` già esegue, committa e pusha in
autonomia per regola del suo `CLAUDE.md` — il confine di autorizzazione segue
le risorse dello scope, non la skill.

**Il montaggio degli scope di dominio è un'ipotesi direzionata, non ancora
canone.** La
ricognizione della flotta (2026-08-01, dettaglio nel task `o2/`) mostra che le
skill di dominio non sono atti da appendere a `perform`: si distribuiscono sui
sei stadi (`aggiorna` è valutazione per tre rami su quattro, `ordini` è
l'intero arco exec a runtime, `finanze-review` ed `elabora-trascrizione`
insistono sull'arco eval, e i canali i1 di `economia` — `posta`,
`registrazioni` — sono `eval perceive` puro). La ricognizione giustifica il
pilota, non ancora l'incisione: il primo canone porta soltanto i sei
scope-stadio; ogni skill di dominio viene poi provata come possibile argomento
delle due canoniche attraverso il `method-review` dell'adottante. Il pilota può
assorbirla, dividerla fra i due archi o mantenerla autonoma. Ordine ratificato
dal custode (2026-08-01): **`nixos` → `salute` → `economia` → `bi`**, dal caso
multi-scope già collaudato a quello più complesso e delicato.

**`eval perceive` può essere il vuoto rituale.** Dove la percezione è
event-driven, una skill che chiede «è arrivata posta?» quando la posta _è_ il
trigger è cerimonia. Due rimedi, entrambi già canonici: uno stadio deve poter
**chiudere in una riga** («nessun segnale nuovo»), col precedente dell'handoff
vuoto che è segnale di buon funzionamento e non fallimento; e in `metodo` lo
scope ha un lavoro vero — raccogliere i marker `method-review.md` dei quattro,
che sono letteralmente la posta in arrivo di questo repo. Deciso nel task:
`adopters-review` resta skill di dominio distinta e produce materiale che
`eval perceive` acquisisce; l'assorbimento è una variante da rivalutare
solo dopo l'uso.

## La clausola di uscita, dichiarata prima di partire

Il rischio dichiarato dal custode è il barocco: una divisione che moltiplica
scritture, token ed energie per azioni che verrebbero naturali tutte insieme. La
scommessa è che la rigidità paghi in qualità autocorrettiva, e i tre episodi
danno la misura del prezzo dell'alternativa. Ma la scommessa si rivaluta, e la
condizione si scrive **ora** perché fra tre mesi non dipenda da chi si ricorda di
averla promessa:

- **quando**: alla chiusura del task nasce un task di rivalutazione `pause`, con
  risveglio al **terzo battito mensile `/adopters-review`** successivo al
  recepimento dai quattro;
- **sintomi che direbbero «troppo»**: uno stadio che chiude vuoto in _tutti_ i
  repo per tre giri; un'invocazione che nessuno fa se non per disciplina; il
  tempo dell'arco che cresce senza che cambi nulla nel verdetto o nella coda;
- **sintomi che direbbero «ha pagato»**: un errore intercettato dallo stadio che
  prima non esisteva (una sintesi i2 corretta perché il claim è caduto, un
  segnale i1 che sarebbe rimasto orfano, una prescrizione o3 consumata potata);
- **cosa si snellisce per primo**, se si snellisce: gli scope, non gli stadi —
  si accorpa l'invocazione, non si smette di distinguere i passi.

Primo pilota: **`metodo` stesso**, che ha entrambi i cicli ed è il repo dove
l'errore costa meno; prova i sei scope canonici, non il montaggio di dominio.
**Il primo giro end-to-end è compiuto** (2026-08-01, skill montate in `metodo`
al posto della coppia): sei esiti espliciti — due sostanziosi (`perceive`,
`compare`), quattro nulli o quasi, primo punto della serie che la clausola di
uscita osserva. L'attrito emerso: la dicitura «via `world/`» ereditata
verbatim da `verdicts-review` era stale rispetto alla membrana reale (il
register dichiara checkout nel territorio, nessun symlink root — corretta
nella skill), e il territorio non dichiarava le superfici per host: sanato
nel register con i checkout e il doppio salto `ssh norvegia` → `ssh deck`
(custode, 2026-08-01), che ha permesso di completare la raccolta dei quattro
marker nello stesso giro. Le
conferme: l'ordine ha pagato al primo giro — `eval compare` ha intercettato
due fotografie stale di `goal.md` (prescrizione aperta non registrata,
«nessun fronte aperto» con un fronte vivo) prima che `exec plan`
ripianificasse su un register falso; nessuna sovrapposizione dannosa fra
`compare` e `plan`, che leggono le stesse fonti da versanti opposti. Il
secondo collaudo candidato è il battito `/adopters-review` del 2026-08-11,
con la posta vera degli adottanti, prima dell'incisione.
Il canone è inciso (2026-08-01: `kb/skill.md` a `stato: maturo`, consumatori
migrati) e la propagazione è emessa: `o3/skill-per-arco.md`, che porta la
rifilatura per i quattro e, dentro, il montaggio delle skill locali come
esperimento sequenziale — solo gli esiti provati risalgono a canone. Chi
recepisce la rifilatura chiude anche l'arretrato della quinta domanda.

Conseguenza già registrata: la «cascata verso i2» proposta come toppa a una riga
in `verdetto-piu-sicuro-del-materiale` decade come mossa autonoma — diventa il
contenuto dello stadio `eval interpret`.
