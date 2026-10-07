---
stato: bozza
---

# View

La view è una rappresentazione navigabile e derivata: rende leggibile una
sorgente del progetto senza diventare una seconda fonte di verità. È la cerniera
o2/i2 del metodo (cfr. `action-cycle`): o2 quando orienta una decisione, i2
quando viene letta per attribuire significato a ciò che sintetizza.

Nel metodo la forma segue la domanda: pagina, tabella di confronto, grafico,
canvas e home statica sono forme alternative, scelte secondo cosa devono far
capire o decidere. Questo nodo tiene la **disciplina della derivazione** — a
quali obblighi una vista risponde — e la sua materializzazione: la cartella
`view/`, le pagine che rendono le fonti, la build che le produce e il modo in
cui raggiungono un lettore. Il racconto curato dell'artefatto, scritto e non
derivato, è un'altra cosa e vive in `presentation`.

## Vista derivata, mai seconda fonte

Una view si genera dalle fonti e il suo contenuto non si mantiene a mano se
esiste una sorgente canonica. La
sorgente resta nel file-ciclo o nella collezione-stadio; la view cambia la forma
di lettura.

Le sorgenti restano pure: le collezioni non incorporano l'HTML generato, e ogni
sezione della vista deriva da una sorgente sola — così nessuna divergenza è
rappresentabile. Quali viste esistano in un repo e da cosa derivino è una
fotografia della sua macchina: vive nell'indice della collezione che le genera,
non qui.

Una vista mantenuta a mano è una seconda fonte di verità travestita, anche
quando si dichiara derivata. Non degrada in modo uniforme: diverge dove la
sorgente si muove, cioè sul fatto più fresco — quello per cui la si apre. Il
danno non è l'incompletezza ma l'**inversione**: continua a proporre l'azione
che la sorgente ha appena ritirato. Ne segue che il test giusto non è un
campione sul contenuto vecchio, ma il confronto con l'ultima modifica della
fonte.

## Derivata implica verificata

Generare non basta quando le sorgenti sono più d'una e possono contraddirsi: il
generatore le legge come un **contratto** ed esce con errore invece di produrre
un output plausibile — un valore dichiarato due volte che diverge, una sorgente
non indicizzata dove l'indice è la chiave, una riga che non risolve al proprio
dettaglio. È una forcing function (`constraint`), e prende il posto del
controllo periodico: gli audit strutturali non attraversano il confine tra una
vista e ciò da cui deriva, quindi la domanda utile non è chi controlla le viste
ma quali viste non sono ancora generate — e, tra quelle generate, quali derivano
da più fonti senza verificarle.

Quando il generatore incontra una sorgente difforme dallo schema maggioritario,
la difformità si legge prima di normalizzarla: può essere un secondo
significato, e allora è il contratto ad ammettere entrambe le forme. Appiattire
la fonte sulla forma prevista dal parser distrugge informazione in silenzio.

## Il contratto è strutturale, non nominale

Gli indici di Perceive e Perform possono avere intestazioni e gerarchie
editoriali diverse secondo il dominio. Un generatore condiviso non deve
selezionare il contenuto in base al lessico del proprio repository: rende
l'intera struttura della fonte nell'ordine dichiarato, conservando anche
sottosezioni e annidamenti. Il contratto distingue queste intestazioni libere
dalle chiavi nominali esplicitamente concordate con un parser, come le colonne
del plan o le sezioni di un register.

Il linguaggio supportato e i suoi limiti devono essere espliciti. Un generatore
può usare un renderer Markdown esistente oppure un sottoinsieme dichiarato;
in quest'ultimo caso rifiuta i costrutti che non sa rendere, invece di
appiattirli in silenzio. Conservare tutte le parole non basta se si perde la
relazione fra un elemento e i suoi sottoelementi. Un'estensione del formato si
verifica su questi rapporti e sui link relativi, senza normalizzare le fonti
per adattarle a un parser incompleto.

## Freschezza: la vista non è più vecchia delle sue fonti

Il contratto verifica la coerenza fra le fonti **quando il generatore gira**, e
per questo non può nulla contro il difetto opposto: il generatore che non è più
stato eseguito. Sono due obblighi distinti della stessa vista — coerente con le
fonti, e non più vecchia delle fonti — e il secondo si soddisfa solo fuori dal
generatore, nell'atto che cambia le fonti.

Il rimedio non è descrivere le fonti di ogni vista in un manifesto leggibile da
uno strumento: il generatore le conosce già, e un elenco parallelo sarebbe la
seconda rappresentazione che diverge — è anche ciò che rende irrilevante la
differenza fra una vista a fonti nominate e una che le raccoglie con un glob. Il
rimedio è **rigenerare**, e il prezzo è quasi nullo perché la generazione è
deterministica.

Rigenerare, però, non chiede di versionare l'output. Una vista versionata
porta un debito: va rigenerata nell'atto stesso che tocca le sue fonti, la sua
storia raddoppia quella delle fonti con HTML derivato, e l'output dipende dal
toolchain dell'host, così un commit fatto altrove porta rumore presentato come
freschezza. E il gesto che doveva pagare il debito non reggeva: in
`economia` un giro `exec` ha cambiato plan e task senza rigenerare, e la vista
versionata, servita sulle reti private, ha continuato a mostrare un task già
ritirato. Le viste perciò **non si versionano**: `view/` è ignorata da git,
si genera dal checkout con la build e si pubblica dall'host privilegiato.
L'obbligo di freschezza non scompare: si sposta dove la vista si legge.

- **In locale** la build rende il working tree, modifiche e file non tracciati
  compresi, e la home lo dichiara come **anteprima**: non attribuisce a nessun
  commit ciò che rende.
- **Nel gate di `/commit`** la build resta una **verifica**: contratti e
  presidio devono passare, ma il suo output non entra nel commit e non
  sostituisce la vista pubblicata.
- **La vista pubblicata** deriva da un commit pulito ed espone quel commit
  («Pubblicazione», sotto): la sua freschezza è la distanza fra la revisione
  servita e il riferimento remoto, misurabile senza aprire una pagina.

La ricostruzione dopo un aggiornamento la fa il servizio dell'host. Non è
l'hook host-locale scartato in passato: quello era stato non dichiarato dentro
il repo, che si rompeva in silenzio dopo un rename; il servizio è
configurazione dichiarata dove l'host tiene la propria (in `metodo`, il repo
`nixos`), con uno stato leggibile, e un suo guasto lascia servita l'ultima
vista buona invece di una vista falsa.

## Pagine 1:1 e perimetro

La vista canonica è la **pagina**: la traduzione 1:1 di un `.md` in HTML, con
la navigazione. «1:1» è fedeltà al contenuto e alla struttura della fonte — il
corpo intero, il frontmatter reso in testa —, non una restrizione della nozione
di vista derivata, che può restare una sintesi o un grafico quando la domanda
lo chiede.

Il perimetro reso è dichiarato: i register `goal.md` e `world.md` e le sei
collezioni del ciclo, indici e item. Restano fuori, per ora in ogni repo, i
nodi `kb/`, README e le istruzioni per gli agenti. Ciò che `.gitignore` tiene
fuori dal repo resta fuori anche da `view/`, i symlink non si seguono e ogni
repo può escludere per pattern ciò che non vuole esporre (`ESCLUSE` in
`o3/view/project.py`): le viste possono essere servite, quindi il perimetro è
anche una decisione sui dati.

Le pagine **ricalcano i path del repo**: `o1/plan.md` diventa
`view/o1/plan.html`. Così la riscrittura dei link è meccanica — un link a una
fonte del perimetro diventa il link alla sua pagina, un link a ciò che non si
rende diventa la sua etichetta — e le immagini citate si copiano accanto alla
pagina allo stesso path relativo. I legami che i contratti verificano si
rendono percorribili: la chiave `Ob.` del plan e l'`obiettivo:` di un filo
portano all'ancora stabile dell'obiettivo in `goal.html` (`ob-1`, `ob-s`),
derivata dalla chiave e non dal titolo; un task del plan porta alla sua
specifica in `o2/`.

La navigazione è comune a ogni pagina: la home, l'indice della collezione e le
voci della collezione come pallini su un filo d'accento, nell'ordine
dell'indice — la sequenza curata, non l'ordine alfabetico. Su schermo stretto
la barra va in orizzontale e le tabelle scorrono da sole.

## Compartimento stagno

`view/` si apre e si serve da sola: nessun URL emesso esce dalla cartella.
Restano link le ancore, i file della cartella e gli URL web o mail; `file:` e i
path di un disco locale non sono esterni e restano etichetta. La cartella è
tutta generata: ciò che la build non produce più si rimuove, così una fonte
cancellata non lascia una pagina orfana. Il builder rompe se un'immagine manca
o un URL esce dalla cartella: è il «derivata implica verificata» applicato al
confine.

## HTML apribile direttamente e build minima

Il formato operativo minimo è un HTML con path relativi, generato dalla build e
apribile con doppio click o `xdg-open view/index.html`. Dopo la build non
richiede deploy, servizi permanenti o `fetch` di file locali, che i browser
bloccano sotto `file://`. Chi non ha il toolchain consulta la vista pubblicata.

La build è versionata in `o3/view/`, con lo **stesso path in ogni repo**:
chi passa da un progetto all'altro, umano o agente, non deve scoprire dove
stanno i builder, e le skill citano un solo comando. L'entrypoint è unico,
`python3 o3/view/build.py`: verifica i contratti fra le fonti, rigenera
pagine, deck, home e asset, e chiude col presidio del compartimento stagno.
Scrive sempre in una cartella temporanea e copia in `view/` solo a esito
riuscito, così un errore tardivo non lascia una vista a metà; `--check`
verifica senza scrivere, `--publish` pubblica (sotto). È Python e non shell perché deve girare anche sugli host Windows; non ha
dipendenze oltre a Pandoc e Prettier. I CSS canonici (`page.css` per le
pagine, `system-image.css` per la home, `deck.css` per il deck) vivono accanto
ai builder e la build li copia in `view/assets/`. Due generazioni consecutive
producono lo stesso output: il determinismo rende la rigenerazione un gesto
meccanico invece di una decisione.

Le viste sono uniformi fra i progetti: a distinguerle sono la **sigla** e un
**colore d'accento** unico per progetto. Sigla, lingua, accento, deck ed
esclusioni si dichiarano in un solo file, `o3/view/project.py`; la build
scrive l'accento in `view/assets/theme.css`. La home resta minimale, pura
affordance di navigazione: i register in sintesi, i sei stadi verso i loro
indici, il deck come voce a sé.

## Servizio sulle reti private

Per aprire l'anteprima da un altro PC delle reti private, lo stesso comando in
ogni repo e su ogni sistema (su Windows `py o3\view\serve.py`):

```bash
python3 o3/view/serve.py
```

Il server usa solo la libreria standard e serve la sola cartella servita,
chiusa su se stessa: niente dotfile, niente elenchi di cartella. Ascolta per
default sulla porta 8000 (`--port`, `--bind`) e si chiude con Ctrl-C. Non tocca
il firewall: da un altro dispositivo la porta deve essere ammessa per le sole
reti private, mai per la rete pubblica.

Un servizio permanente è legittimo alle condizioni che conservano il vincolo
dell'artefatto autonomo:

- **consumatori reali**: persone nelle reti private che consultano lo stato del
  progetto senza il checkout. Senza di loro il servizio non nasce;
- **un solo host privilegiato per progetto**, così non circolano rese di
  checkout a versioni diverse. Se l'host è un ruolo (la produzione di una
  coppia di server), il servizio segue il ruolo;
- **servizio utente**, gestibile da un agente senza privilegi, disponibile dopo
  il riavvio e senza sessione interattiva;
- **solo reti private**: le porte le ammette il firewall dell'host, il server
  non le apre;
- **pubblicazione da commit pulito**, col contratto della sezione seguente, e
  nessuna copia mantenuta a mano: i builder e `serve.py` sono quelli del
  checkout;
- **esposizione dichiarata**: un server sempre acceso e senza autenticazione
  espone le viste in modo continuo. L'adottante lo registra dove tiene i propri
  vincoli sui dati — cosa entra nel perimetro e chi lo vede.

Host, porte, configurazione del servizio e innesco della pubblicazione (dopo un
pull manuale o un aggiornamento automatico) sono materia dell'host, non del
canone.

## Pubblicazione

`python3 o3/view/build.py --publish DIR` pubblica in una cartella dell'host,
fuori dal checkout, e `python3 o3/view/serve.py --publish-root DIR` la serve.
Il contratto è portabile, indipendente dal sistema dell'host:

- **ultima vista buona**: si costruisce in una cartella a parte e si pubblica
  solo l'esito riuscito, con uno scambio atomico anche su Windows. Un errore,
  anche tardivo, lascia servita la versione precedente; una richiesta già
  iniziata finisce sulla versione con cui è partita;
- **fonti pulite**: la vista pubblicata deriva da un commit, esportato senza
  modifiche locali né file non tracciati e costruito coi builder di quel
  commit. Un pull o un edit durante la build non mescolano le revisioni;
- **provenienza**: la home pubblicata espone l'hash del commit costruito e il
  toolchain che l'ha resa, registrati anche in un file accanto all'output;
- **recupero**: all'avvio si pubblica se l'output manca o è arretrato. Più
  richieste concorrenti si serializzano, e l'ultimo commit richiesto viene
  infine pubblicato, anche dopo una build fallita. Senza alcuna versione valida
  il server non parte, dice perché ed esce con un codice proprio; se una
  versione c'è, continua a servirla e rende consultabile l'errore (`/_stato`);
- **verifica distinta dalla freschezza**: un audit controlla separatamente
  build e contratti sulle fonti, revisione servita rispetto al riferimento
  remoto aggiornato, raggiungibilità della porta. Hash uguali non provano un
  rendering corretto; una porta irraggiungibile è «non verificata», non fresca
  per presunzione.

## Transizione

Fino al recepimento della prescrizione, un adottante può ancora versionare
`view/`. Lì vale la regola precedente: il gate di `/commit` esegue la build e
legge `git status`, una vista che compare modificata **era** stale e la sua
rigenerazione entra nel commit; il servizio permanente lancia `serve.py` sul
`view/` del checkout, e un pull aggiorna le viste. Il passaggio si fa per
host: prima si prepara e si collauda la pubblicazione, poi `view/` esce da git.

Più indietro ancora, un adottante può avere la forma che precede la
migrazione delle viste: viste Reveal e liste in `presentation/`, builder in
`o3/presentation/`, deck in `i2/`. Le due forme non convivono nello stesso
repo: la migrazione sposta builder, deck e servizio nello stesso giro.

Connessioni:

- [presentation](presentation.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
- [constraint](constraint.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [processing-layers](processing-layers.md)
- [project-structure](project-structure.md)
- [affordance-signifier](affordance-signifier.md)
- [karpathy-pattern](karpathy-pattern.md)
- [verdict](verdict.md)
- [method-development](method-development.md)
