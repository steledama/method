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

È una coda, non uno storico né un backlog degli adottanti. Contiene solo lavoro
vivo del repository, ordinato per esecuzione. Un task concluso scompare dal plan
e da `o2/`; Git e i fili conservano ciò che merita storia.

## Forma

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
non diventa un secondo diario.

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
  solo.

Ogni `w` e ogni `p` porta inoltre `by:`, la data di riesame (`by: 2026-11-04`,
o il solo mese). Su una `w` che arriva da un canale non letto dal giro è una
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
della chiosa. Il primo interprete è quello di `nixos` (`0a7cb7c`).

## Attese a finestra

`Dip.` dice da cosa dipende un task, non come si comporta il costo del ritardo,
e sono tre comportamenti diversi. L'attesa **piatta** non costa: l'opzione resta
identica. L'attesa **onerosa** costa in modo crescente ma resta aperta e si
recupera pagando — interessi, sanzioni, ravvedimenti. L'attesa **a finestra**
non rende la cosa più cara: può renderla impossibile.

Le prime due sono già governate, perché `## Scadenze` regge tutto ciò che ha una
data. La terza è invisibile per costruzione: la sua caratteristica è
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

Un adottante che implementa il controllo delle scadenze deve far comparire le
righe marcate a ogni esecuzione, senza condizione di distanza, senza contarle
come scadute. È il contratto del controllo: il suo recepimento si verifica nel
codice del fork, non si deduce dalla presenza di questo nodo.

## Tempo e fonti

`## Scadenze` contiene solo date esogene o ricorrenze che possono cambiare l'ordine
della coda, in tre specie. La **prima** è la data esogena: il Mondo la impone e
la coda le si adatta. La **seconda** è l'orologio nostro, e allora la data non
sta qui ma nel `by:` di una `p`. La **terza** è la
ricorrenza di uno scheduler: la riga indica cadenza e configurazione —
la fonte di verità è la config versionata — senza replicare ogni prossima data.
Calendari che non muovono la coda restano nel dominio.

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
