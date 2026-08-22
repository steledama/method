---
stato: bozza
---

# View

La view è una rappresentazione navigabile e derivata: rende leggibile una
sorgente del progetto senza diventare una seconda fonte di verità. È la cerniera
o2/i2 del metodo (cfr. `action-cycle`): o2 quando orienta una decisione, i2
quando viene letta per attribuire significato a ciò che sintetizza.

La forma segue la domanda (Karpathy): pagina markdown, tabella di confronto,
presentazione a slide, grafico, canvas e home statica sono forme alternative,
scelte secondo cosa devono far capire o decidere. La vista a slide è adatta a
una sintesi che si scorre, non è l'unica forma possibile. Questo nodo tiene la
**disciplina della derivazione** — a quali obblighi una vista risponde; il
formato che si apre, la build che lo produce e il modo in cui raggiunge un
lettore vivono in `presentation`.

## Vista derivata, mai seconda fonte

Una view versionata deve poter essere aperta direttamente dal checkout, ma il
suo contenuto non si mantiene a mano se esiste una sorgente canonica. La
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
deterministica: se le fonti non sono cambiate l'output è identico e `git status`
non mostra niente. Da qui il gesto meccanico del gate `/commit` — si esegue la
build e si legge `git status`: una vista che compare modificata **era** stale, e
la sua rigenerazione entra nel commit. Non è più una domanda di giudizio.

Una vista versionata è dunque un artefatto con un debito: la si versiona perché
deve aprirsi dal checkout senza build, e si paga l'obbligo di rigenerarla
nell'atto stesso che tocca le sue fonti. Un hook che lo faccia da sé resta
fuori: richiede installazione host-locale, cioè stato non versionato dentro un
artefatto che si vuole portabile — la stessa via che qui si era già rotta in
silenzio dopo un rename.

Connessioni:

- [presentation](presentation.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
- [constraint](constraint.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [processing-layers](processing-layers.md)
- [karpathy-pattern](karpathy-pattern.md)
- [verdict](verdict.md)
