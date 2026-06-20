---
data: 2026-06-20
stato: bozza
---

# KB content typology

Il contenuto di una knowledge base non è omogeneo. Ogni nodo denota qualcosa, e ciò che denota lo colloca su un polo del ciclo d'azione: il Goal in alto, il Mondo in basso, la macchina in mezzo. Distinguere _a cosa serve_ la KB — il canale tra agenti che non si parlano, la sua funzione di system image — da _di cosa parla_ — il suo contenuto — scioglie una confusione ricorrente: i due assi sono ortogonali, e la KB è il system image (funzione) il cui contenuto è un modello dei poli del ciclo (denotazione). Questa tipologia guarda il secondo asse.

Le tre regioni del contenuto rispondono a tre domande diverse sul mondo. Il contenuto di tipo **ought** (Goal) dice dove l'artefatto vorrebbe andare: concetti, valori, obiettivi. Il contenuto di tipo **is** (Mondo runtime) dice com'è la realtà del dominio su cui l'artefatto agisce: persone, conti, host, fornitori, il corpo. Il contenuto di tipo **macchina** (Mondo di sviluppo) dice com'è fatto l'artefatto stesso: architetture, script, schemi. La macchina è la cucitura tra i due cicli annidati — è il Mondo del ciclo di sviluppo e insieme la macchina che esegue il runtime — perciò descriverla è ancora rappresentare un mondo, solo l'altro.

La distribuzione del contenuto di una KB tra queste regioni è il suo **baricentro**, e il baricentro è una diagnosi. Un ciclo d'azione calcola uno scarto solo se possiede entrambi i poli: un is contro cui misurare un ought. Una KB tutta-ought ha il polo alto gonfio e il polo basso vuoto, quindi non ha su cosa mordere e non genera azione; una KB tutta-is descrive la realtà ma non sa verso cosa orientarla. Leggere il baricentro mostra quale arco del ciclo l'artefatto affama, prima e meglio di qualunque lint formale.

Le tre regioni:

- **ought (Goal)** — concetti, valori, obiettivi; il riferimento valoriale. È legittimamente assente quando il motivo è codificabile e non richiede articolazione.
- **is (Mondo runtime)** — la realtà del dominio filtrata dai goal; il modello del mondo su cui l'artefatto agisce.
- **macchina (Mondo di sviluppo)** — com'è fatto l'artefatto; è il caso più letterale di system image alla Norman, l'artefatto che si documenta da sé per il prossimo agente. È legittimamente assente o sottile quando la macchina dell'artefatto è il tooling condiviso (il metodo via symlink, le regole operative) e non codice di dominio proprio: gemella simmetrica dell'esenzione-ought.

Le due tensioni, dove la tripletta si tende e va tenuta esplicita invece di lisciata:

- **la macchina si sdoppia** — descrivere la struttura dell'artefatto (architetture, schemi) non è la stessa cosa che prescrivere l'atto sul Mondo (procedure, pratiche, runbook). Il secondo è contenuto o3, un repertorio d'atto sceso verso la membrana, non descrizione del Mondo di sviluppo. La regione macchina va letta come «il come», con due facce: la struttura e l'atto.
- **le sorgenti fuori posto** — maestri e fonti promossi a nodo non sono un polo del ciclo: sono fonti di verità che canonicamente vivono nel register e nel Mondo, non come nodi. La loro presenza nel corpo della KB è un'anomalia strutturale, spesso sintomo dello stesso sbilanciamento di una KB che accumula chi-l'ha-detto invece di cosa-è-vero.

Il baricentro non prescrive una distribuzione corretta unica: ciò che è sano dipende dal dominio e dal grado di delegabilità del goal. Prescrive una sola cosa — che entrambi i poli siano presenti dove il ciclo deve chiudersi. Un dominio a goal codificabile può vivere senza nodi-ought, e un dominio la cui macchina è il tooling condiviso senza nodi-macchina; ma nessun dominio che debba generare azione può vivere senza il polo is contro cui l'ought si misura.

Esempi per artefatto, come baricentri distinti sullo stesso ciclo:

- baricentro **is**: una KB di gestione patrimoniale fatta quasi solo di persone, conti, immobili e successioni — la realtà vista con gli occhiali del dominio, più un solo nodo-obiettivi.
- baricentro **macchina e atto**: una KB di configurazione di sistemi fatta di pattern, servizi e procedure di ripristino, con una fetta di Mondo (rete, host) e nessun nodo-valore, perché il goal è codificabile.
- baricentro **macchina↔is**: una KB di business intelligence che attraversa script e architettura da un lato e fornitori e cataloghi reali dall'altro — lo span più largo, e l'artefatto che esegue meglio.
- baricentro **ought**: una KB di benessere personale fatta quasi solo di concetti filosofici e maestri, con l'is del corpo ridotto a margine — il polo basso affamato, e l'artefatto che non genera azione. È il segnale che il baricentro va corretto, non il sintomo di un utente pigro.

L'ultimo caso mostra il modo più insidioso in cui il baricentro mente: un segnale del Mondo può essere catturato e mai interpretato in un nodo, restando una riga sepolta in una cronologia invece di diventare la casa su cui il ciclo agisce. Il polo is allora esiste sulla carta ma non nel ciclo, e l'artefatto resta cieco proprio sull'allerta più importante.

Connessioni:

- [knowledge-base](knowledge-base.md)
- [system-image](system-image.md)
- [nested-cycles](nested-cycles.md)
- [goal](goal.md)
- [world](world.md)
- [processing-layers](processing-layers.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [cognitive-fidelity](cognitive-fidelity.md)
