---
stato: maturo
---

# Plan

Il plan è la supervisione corrente del lavoro futuro: risponde a «cosa facciamo
adesso?». La sua istanza è `o1/plan.md`; i dettagli sostanziali vivono nei file
`o2/`, indicizzati una sola volta da `o2/tasks.md`.

Questo nodo tiene **due funzioni deliberatamente fuse**: l'atomo o1 del ciclo —
scegliere la direzione, il primo atto dell'arco di esecuzione — e la sua unica
materializzazione, la coda `o1/plan.md`. Altrove il metodo le separa (`compare`
e `verdict`, `specify` e `tasks`), perché lì l'atomo ha più di una
materializzazione. Per o1 non ne esiste una seconda: il piano è la coda, e
sdoppiarlo produrrebbe un nodo-atomo senza contenuto proprio. Se un giorno una
seconda forma del Plan emerge, la separazione diventa dovuta.

Il nodo si legge a strati. «Forma» basta a un plan fatto di soli task pronti
o in sequenza. «Risveglio» e «Attese a finestra» servono quando una riga
aspetta qualcosa, `w` o `p`. «Ricorrenze» e «Controllo di scadenze e
ricorrenze» servono quando una riga torna o porta una data. «Tempo e fonti»
dice quale data va in quale sezione.

È una coda, non uno storico né un backlog degli adottanti. Contiene solo lavoro
vivo del repository, ordinato per esecuzione. Un task concluso scompare dal plan
e da `o2/`; Git e i fili conservano ciò che merita storia.

## Forma

Il plan apre con `## Direzione`, prima di `## Task`: due o tre frasi che
dichiarano la fase operativa del repository e la rotta verso il traguardo.
In un repository in sviluppo nominano il traguardo che organizza i task;
in uno a regime dichiarano il peso prevalente delle ricorrenze e gli
eventuali fronti di sviluppo ancora vivi. È una sintesi locale del lavoro,
non una copia del motivo stabile di `goal.md` o della bussola del README.

La fase si dichiara in prosa, senza un attributo a valori chiusi: quantità
di task e ricorrenze sono indizi, non una prova automatica di maturità.
`exec plan` confronta la direzione con Goal, fili e coda a ogni giro. La
riscrive quando cambiano traguardo, fase o rotta, non a ogni avanzamento.
Date di stato, percentuali, prossimi passi e resoconti appartengono alla
tabella, a `o2/` o ai fili `i3/`. Il generatore può verificarne forma e
posizione; la freschezza del significato resta al giro.

La tabella canonica usa `Ciclo · Ob. · Task · Dip.`:

- `Ciclo`: `dev` o `runtime`, secondo il mondo su cui insiste il task;
- `Ob.`: numero dell'obiettivo servito in `goal.md`, oppure `S` per il Goal di
  sviluppo; non può essere vuoto;
- `Task`: titolo unico usato anche nei riferimenti e nell'indice `o2/tasks.md`;
- `Dip.`: `—` se pronto, `↳ <titolo>` se sequenziato dopo un altro task, `w<n>`
  se la prossima mossa è esterna, `p<n>` se la tratteniamo noi.

L'ordine delle righe, insieme alle dipendenze, esprime la priorità: non servono
numeri identificativi o una colonna apposita. Un fatto vive in una sola
rappresentazione; eventuali dettagli stanno in `o2/`, non in nuove colonne.

Attese e pause portano un indice (`w1`, `p2`) che le lega a una legenda breve
sotto la tabella: la lettera dice chi tiene il tempo — il mondo o noi — e il
numero è l'indirizzo della chiosa. L'indice è dell'attesa, non della riga:
nasce col primo numero libero della sua lettera e resta invariato finché
l'attesa vive, comunque la riga si sposti nella tabella; chiusa l'attesa, il
numero torna libero (con `p1`, `p2`, `p4` occupati la prossima pausa è `p3`).
Un'attesa che cambia lettera prende il primo libero della nuova. Così un
riferimento in un commit o fra sessioni resta vero finché l'attesa è aperta,
mentre rinumerare in ordine di tabella cambierebbe nome a righe intatte. La
legenda segue l'ordine dei numeri, dichiara causa e condizione di risveglio e
non diventa un secondo diario. Indici e chiose si corrispondono: una chiosa
senza la riga che porti il suo indice in `Dip.` è il resto di un'attesa
chiusa o di un task uscito dal plan, e va tolta. Un indice senza chiosa è
un'attesa senza causa. Le due cose le segnala `build.py --check`.

La lettera si decide da chi fa la prossima mossa, non da quanto lavoro resta.
Un task col codice applicato che aspetta un'occorrenza reale per validarsi è
`w`, anche se poi toccherà a noi verificarla: tenerlo `p` lo lascia in testa
e i giri lo confermano come prossimo senza che ci sia una mossa da fare. Per
questo ogni `w` nomina il **segnale** che lo riapre e come lo si riconosce
(«Risveglio»). Il giro lo cerca; se lo trova, la dipendenza si scioglie, la
riga risale fra le pronte e il `Prossimo:` cambia con quel segnale per causa.

Il «noi» delle `p` è il custode con l'agente: un'attesa tenuta dal custode,
dall'agente o da entrambi è una `p`, perché la cognizione è condivisa. Nel giro
senza custode una `p` non è pronta. L'agente chiede un ripensamento quando una
`p` non gli torna, altrimenti sta fermo. Un'attesa composita prende la lettera
della prima mossa attesa, e il risveglio alternativo resta nella chiosa.

## Risveglio

La chiosa di una `w` dichiara come si riconosce il risveglio, in una di due
forme:

- `probe:` un controllo deterministico, cioè una cosa da interrogare e una
  condizione, che uno strumento valuta senza il modello
  (`probe: nixpkgs naps2 >= 8.6.0`). Oltre la cadenza dello strumento l'arrivo
  non può sfuggire;
- `arrival:` il fatto atteso e il canale da cui arriva: email, diario,
  sessione, un log, un giro (`arrival: esito della seduta, via diario o
sessione`). Il giro lo riconosce confrontando i fatti in ingresso con le `w`
  ad arrivo. Se il canale passa per il custode, il giro non può accorgersene da
  solo. Se invece il giro non legge il canale perché gli manca un permesso o
  uno strumento, come una casella di posta in cui scrive bozze ma non legge le
  risposte, la cecità è una lacuna da proporre (`agent-as-user`), non un
  `by:` da rinnovare.

Un arrivo può coprire l'attesa solo in parte. Quando la `w` aspetta la
risposta a una nostra richiesta, chi riconosce l'arrivo ne confronta il
contenuto con ciò che la richiesta chiedeva, letto dal messaggio inviato o
dalla chiosa, che per questo lo tiene raggiungibile. Ogni parte non coperta
esce in modo esplicito: resta nell'`arrival:` della `w`, diventa una mossa
nostra (una `p` o un `decidere:`) oppure cade col motivo scritto. Nel giro
senza custode l'arrivo parziale va anche nella riga `Attenzione:`. Una
risposta che scioglie l'attesa senza questo confronto toglie dal radar
proprio le domande rimaste aperte, spesso le sostanziali (giro di
`economia`, 2026-11-06: a una richiesta in tre punti il notaio risponde col
solo elenco dei documenti, l'attesa si chiude e i due punti sostanziali li
recupera il custode il giorno dopo).

Ogni `w` e ogni `p` porta inoltre `by:`, la data di riesame (`by: 2026-11-04`,
o il solo mese, che vale come il suo ultimo giorno). Su una `w` che arriva da un canale non letto dal giro è una
scadenza di sollecito: oltre la data il silenzio è il segnale. Altrimenti è un
riesame di pertinenza, perché la sonda garantisce che l'arrivo non sfugga, non
che aspettarlo abbia ancora senso. Su una `p` è la data entro cui ci chiediamo
se la teniamo ancora, e la domanda può investire il task intero.

Scaduto il termine gli esiti sono tre: sollecitare (per una `p`, riprendere),
riclassificare, oppure rinnovare il `by:` col motivo nella chiosa. Il rinnovo
senza motivo è il rinvio rituale che il termine serve a impedire. Nel giro senza
custode il sollecito è un atto verso l'esterno e la ripresa di una `p` spetta
alla sessione: il giro nomina la riga scaduta nella riga `Attenzione:`.

I termini non sono scadenze: non stanno in `## Scadenze` e non contano come
scadute, ma entrano nel controllo delle scadenze come righe di riesame. Il `!`
resta ortogonale: dice quanto costa l'attesa, non come si riconosce il
risveglio.

Il canone fissa il contratto della sonda (deterministica, booleana, senza il
modello) e non la sua sintassi. La condizione vive nella chiosa, scritta nel
vocabolario chiuso dello strumento che la valuta: i tipi che conosce, come una
issue, una versione in un repository di pacchetti, una riga di log.
L'interprete vive in `o3/`, la cadenza nella config dell'adottante. Così la
sonda nasce e muore con la sua attesa, e una riga del plan non diventa mai un
comando: lo strumento esegue solo i tipi che conosce, e il giro autonomo resta
col permesso dello strumento. Uno strumento che controlla le attese prende solo
le `w` con `probe:` e fa comparire le righe col `by:` passato.

Un'attesa che nessun tipo del vocabolario sa interrogare dichiara `arrival:` e
la riconosce `perceive`: un tipo nuovo entra nello strumento solo quando il caso
si ripete. La legenda è prosa, e il formatter può andare a capo dentro una
condizione: chi estrae `probe:` e `by:` unisce prima le righe di continuazione
della chiosa.

## Attese a finestra

`Dip.` dice da cosa dipende un task, non come si comporta il costo del ritardo,
e sono tre comportamenti diversi. L'attesa **piatta** non costa: l'opzione resta
identica. L'attesa **onerosa** costa in modo crescente ma resta aperta e si
recupera pagando — interessi, sanzioni, ravvedimenti. L'attesa **a finestra**
non rende la cosa più cara: può renderla impossibile.

Le prime due sono già governate, perché `## Scadenze` e `## Ricorrenze` reggono
tutto ciò che ha una data. La terza è invisibile per costruzione: la sua caratteristica è
precisamente di non averne una — una capacità di agire che può venir meno, una
controparte che può uscire di scena, un fatto altrui non databile. Nessun
controllo che ragioni per distanza temporale la troverà.

Per questo l'indice può portare un `!` appeso (`w2!`): l'opzione può chiudersi e
non riaprire. Significa **deperibile, non urgente**, e la distinzione va tenuta
ferma perché inverte la lettura normale della coda: una finestra può avere mesi
davanti e meritare comunque presidio, mentre una scadenza già passata può
legittimamente restare in attesa.

Si marca ciò la cui chiusura **non ha una data calcolabile** e su cui non c'è
ancora una mossa in agenda. Se una data esiste — una prescrizione, un termine di
decadenza — il posto è `## Scadenze`, e marcarla qui diluirebbe il segnale: la
rarità è ciò che lo fa funzionare.

Vale anche il verso opposto, ed è l'esito che il marcatore deve provocare:
appena si mette in agenda l'azione che presidia la finestra, **la data
sostituisce il marcatore**, che si toglie. Il `!` serve finché si aspetta, e
smettere di aspettare è il modo giusto di farlo sparire. Un piano in cui non
compare perché ogni finestra è stata messa in agenda è un piano sano, non un
piano che ha dimenticato il meccanismo.

La chiosa di un `!` dichiara due cose oltre a causa e risveglio: **cosa chiude
la finestra** e **cosa resta se si chiude**. Il secondo campo è quello che
conta. Scrivere il ripiego col suo costo trasforma un'ansia in una decisione: si
può scegliere di rischiare una finestra, non si può sceglierlo senza sapere cosa
c'è dopo.

Il controllo delle scadenze (`o3/scadenze.py`, cfr. «Controllo di scadenze e
ricorrenze») fa comparire le
righe marcate a ogni esecuzione, senza condizione di distanza, senza contarle
come scadute.

## Ricorrenze

Un task si chiude e scompare, una ricorrenza compiuta si riscrive con la data
successiva. È questo il criterio: la riga che, fatta la cosa, tornerebbe non è
un task né una scadenza e sta in `## Ricorrenze`, la sezione del plan che segue
la tabella dei task. Vale per un timer quotidiano, un controllo mensile o un
adempimento annuale, con l'orologio nostro o del Mondo.

Altrove costa in due modi. Come `p` eterna è un task che dichiara di non
chiudersi e occupa la coda (la prova annuale del seed di `nixos`). Come task
rifatto a ogni occorrenza sparisce fra una e l'altra (chiuso il 730 del 2026,
nel plan di `economia` non restava niente che ricordasse il successivo).

```markdown
| Prossima         | Cadenza    | Esecutore | Ob. | Ricorrenza                  |
| ---------------- | ---------- | --------- | --- | --------------------------- |
| config           | quotidiano | scheduler | 1   | [Ciclo autonomo](procedura) |
| 2027-11          | annuale    | sessione  | 2   | [Prova del seed](procedura) |
| 2027-03          | annuale    | task      | 1   | [Redditi](procedura)        |
| entro 2027-08-10 | annuale    | sessione  | 1   | [RC auto](procedura)        |
```

Un repo col ciclo autonomo lo dichiara nella prima riga, perché chi consulta il
plan veda subito cosa gira da solo. La riga non riporta l'orario: la fonte di
verità è la config dello scheduler, spesso fuori dall'artefatto, e una copia
andrebbe tenuta sincronizzata. L'ora effettiva la dicono i log dei giri.

- `Prossima` è la prossima mossa, non l'evento: un giorno o il solo mese, che
  vale come il suo ultimo giorno. La data nuda è un orologio nostro, `entro` un
  termine imposto dal Mondo, `config` dice che l'orologio è di uno scheduler:
  la fonte di verità è la config versionata e la riga non replica ogni prossima
  data. Un marcatore di data indicativa non serve, e non va introdotto: la
  grafia `~` di `economia`, riscritta in `\~` nel file, ha nascosto al controllo
  le righe che la portavano;
- `Cadenza` è una di `quotidiano`, `settimanale`, `mensile`, `trimestrale`,
  `semestrale`, `annuale`, `biennale`. Una nuova entra quando il caso si
  presenta, perché il controllo deve saperla convertire in un intervallo;
- `Esecutore` dice chi chiude l'occorrenza: `scheduler`, `giro`, `sessione`
  (il «noi» delle `p`, custode con agente) o `task`. Descrive e non autorizza:
  il permesso sta nel register di autonomia, e una riga del plan non diventa
  mai un comando. Se il giro compie solo una parte dell'occorrenza, l'esecutore
  resta chi la chiude;
- `Ob.` vale come nella tabella dei task e non può essere vuoto: una ricorrenza
  non finisce mai da sola, quindi è quella che ha più bisogno di dichiarare a
  cosa serve;
- `Ricorrenza` è il titolo con il link alla procedura: una riga senza procedura
  è un rilievo, come un `entro` senza task.

La tabella non accoglie prosa. La procedura sta dove starebbe comunque, in una
skill, in `o3/` o in un nodo `kb/`, mai in `o2/`, che è fatto di lavoro che
finisce. La procedura dichiara anche dove va la traccia di un'occorrenza
compiuta, di norma `i1/` o il filo che la consuma. Quando le porzioni di Mondo
si moltiplicano, come i rami di una manutenzione, le cadenze per entità stanno
in configurazione dichiarativa accanto alla skill e il plan tiene una riga sola.

Avanzare `Prossima` è l'atto che chiude l'occorrenza, nello stesso commit della
sua traccia. L'ultimo esito quindi non serve in riga: una data passata significa
non fatta, senza dover distinguere fra una cosa saltata e una riga dimenticata.

`Esecutore` distingue anche le ricorrenze che si esauriscono in una sessione da
quelle con mosse preparatorie. Se l'occorrenza chiede attese o decisioni oltre
una sessione, come i redditi, è `task`: `Prossima` è il giorno in cui si
comincia e a quella data `exec plan` apre un task ordinario, che si chiude e
scompare come ogni altro. Il termine di quella occorrenza va in `## Scadenze`
col suo task, come ogni appuntamento fissato per un'occorrenza. La riga avanza
all'apertura del task, perché da lì a sorvegliare sono il task e la scadenza.
Una riga `task` non porta quindi `entro`.

`exec plan` apre i task delle righe `task`, e nel giro senza custode nomina in
`Attenzione:` le righe `sessione` dovute. Le righe `giro` le compie `exec
perform`, se il register di autonomia glielo assegna. Una ricorrenza non è
candidata al `Prossimo:`, che resta dei task. `eval compare` giudica quelle
saltate più volte e quelle che da molte occorrenze non producono niente,
candidate a una cadenza più bassa o al taglio: il riesame di pertinenza è
l'occorrenza stessa, quindi la riga non porta un `by:`.

La sezione è una seconda tabella del plan: il parser di un fork che legge ogni
tabella come tabella dei task va adeguato prima di aggiungerla. La forma la
verifica `build.py --check`.

## Controllo di scadenze e ricorrenze

Il controllo è uno strumento del canone, `o3/scadenze.py`, che un adottante
lancia dal proprio repo col checkout di `method`, come il gate di `/commit`:
uno strumento per repo finirebbe per leggere la stessa grammatica in modi
diversi, come è successo al `by:` col solo mese. Il profilo locale
`o3/scadenze.toml` è opzionale e riguarda solo la forma delle righe di
`## Scadenze`: formati di data oltre a quello ISO e marcatori di riga chiusa.
Stati, codice di uscita e divieto di scarti silenziosi non si configurano. Gli
strumenti locali restano alle voci di dominio, come i rami di una manutenzione.

Il controllo unisce le due sezioni in una sola catena cronologica e dà a ogni
riga di `## Ricorrenze` uno stato: `dovuta` dalla data raggiunta, `saltata`
quando è passata anche la data più una cadenza, cioè quando è andata persa
un'occorrenza intera, col numero delle occorrenze perse. Lì solo un `entro`
passato conta come scaduta: l'orologio nostro passato si stampa senza toccare
il codice di uscita, come un `by:`. In `## Scadenze` ogni data passata conta
come scaduta, perché la sezione tiene solo date imposte dal Mondo; un
appuntamento passato si toglie dal plan. Le righe `config` non hanno data da
confrontare: se un giro manca lo dicono i log dello scheduler, che sono un
canale di `perceive`.

Una data nostra che deve restare visibile sta nel `by:`, non in `## Scadenze`:
un `by:` entro la finestra di 45 giorni entra nella catena come riesame in
arrivo, senza contare come scadenza e senza toccare il codice di uscita. Se
conta il giorno, il `by:` lo porta scritto: col solo mese vale l'ultimo.

È un segnale, non un gate: esce con 1 se c'è una scaduta, con 2 se non riesce a
leggere plan o profilo, e non entra nei controlli del commit. Lo lanciano
`exec plan` ed `eval compare`.

Il controllo non scarta mai in silenzio. Ogni voce di `## Scadenze` o di
`## Ricorrenze` è una data interpretata o un rilievo di forma, col testo della
riga, che come gli altri rilievi non tocca il codice di uscita. È la classe del
guasto di `economia`, dove 8 righe erano invisibili senza alcun segnale
(2026-11-08). Una voce di `## Scadenze` comincia con la data, ISO e col giorno o
il solo mese, eventualmente in grassetto e preceduta da `entro`, e la separa dal
testo un `—` o un `→`.

## Tempo e fonti

`## Scadenze` contiene solo date una tantum che possono cambiare l'ordine della
coda. Se la data la impone il Mondo sta qui, e la coda le si adatta. Se
l'orologio è nostro la data non sta qui ma nel `by:` di una `p`. Se la data
torna è una ricorrenza, e sta in `## Ricorrenze`. Calendari che non muovono la
coda restano nel dominio, ricorrenti o no.

Una scadenza che chiede una mossa nostra prima della data, come prenotare,
procurarsi o rinnovare un documento o preparare un invio, ha un task che la
prepara. Una riga «entro…» di `## Scadenze` senza task è lavoro non tracciato.
Le scadenze
vicine si leggono come catena: ogni passo deve ricevere in tempo ciò che gli
serve dal precedente. Se il dominio rispecchia `## Scadenze` su un'altra
superficie, come un calendario, il confronto va in entrambe le direzioni: ogni
evento ha la sua riga e ogni riga datata ha il suo evento. Il confronto
distingue anche l'impegno fissato dalla data obiettivo o dal promemoria.
Confrontare in un solo verso lascia passare una data obiettivo segnata come
appuntamento.

La cadenza e la composizione della coda sono indizi della forma del runtime, da
leggere insieme a esiti e copertura dei segnali (`development-goal`). Una
tabella dev vuota non prova da sola la maturità dell'artefatto, e una coda ferma
non prova da sola un problema: un `Prossimo:` confermato per molti giri, con
esiti runtime sani, è l'equilibrio che il telos dell'artefatto invisibile cerca
(`development-goal`, `tasks`).

Un ingest semplice può restare una riga del plan; `## Fonti da elaborare` tiene
eventuali path lunghi. Quando servono decisioni, vincoli o più passaggi, nasce
un file `o2/`.

La skill `exec plan` controlla coerenza, priorità e rapporto task→obiettivo, e
chiude col prossimo task, confermato o cambiato, nel trailer `Prossimo:` del
commit (`skill`); il generatore verifica il contratto tra tabella, indice e
file `o2/`.

Connessioni:

- [tasks](tasks.md)
- [development-goal](development-goal.md)
- [goal](goal.md)
- [verdict](verdict.md)
- [action-cycle](action-cycle.md)
- [constraint](constraint.md)
- [view](view.md)
