---
stato: bozza
---

# KB content typology

Il contenuto di una knowledge base non è omogeneo. Ogni nodo denota qualcosa, e
ciò che denota lo colloca in una regione del ciclo d'azione: il Goal in alto, il
Mondo in basso, la macchina in mezzo oppure la norma che ne governa la
costruzione. Distinguere _a cosa serve_ la KB — il canale tra agenti che non si
parlano, il suo ruolo nel system image — da _di cosa parla_ — il suo contenuto —
scioglie una confusione ricorrente: i due assi sono ortogonali, e la KB è il
nucleo formalizzato del system image (funzione) il cui contenuto è un modello
dei poli del ciclo e dei vincoli della sua macchina (denotazione). Questa
tipologia guarda il secondo asse.

Le quattro regioni del contenuto rispondono a quattro domande diverse. Il
contenuto di tipo **ought** (Goal) dice dove l'artefatto vorrebbe andare:
concetti, valori, obiettivi. Il contenuto di tipo **is** (Mondo runtime) dice
com'è la realtà del dominio su cui l'artefatto agisce: persone, conti, host,
fornitori, il corpo. Il contenuto di tipo **macchina** (Mondo di sviluppo) dice
com'è fatto l'artefatto stesso: architetture, script, schemi. Il contenuto di
tipo **norma della macchina** dice invece come l'artefatto deve essere costruito
o mantenuto: invarianti, convenzioni e principi d'ingegneria. La macchina è la
cucitura tra runtime cycle e development meta-cycle — è il Mondo del ciclo di
sviluppo e insieme la macchina che esegue il runtime — ma descriverla e
prescriverne la forma restano atti denotativi distinti.

La distribuzione del contenuto di una KB tra queste regioni è il suo
**baricentro**: un indizio per orientare la diagnosi. Per valutare un esito
servono un riferimento desiderato e uno stato osservato, ma entrambi possono
vivere fuori dalla KB: nei register, nei dati, nelle sintesi i2 o nelle fonti
interrogate dal ciclo. Una regione poco rappresentata nei nodi è una domanda di
copertura, non la prova che un polo manchi all'artefatto.

La verifica attraversa quindi l'intero ciclo: dove si legge il riferimento, dove
si osserva lo stato, chi li confronta e quale decisione ne segue. La
composizione della KB da sola non misura efficacia, autonomia o qualità delle
azioni.

Le quattro regioni:

- **ought (Goal)** — concetti, valori, obiettivi; il riferimento valoriale. È
  legittimamente assente quando il motivo è codificabile e non richiede
  articolazione.
- **is (Mondo runtime)** — la realtà del dominio filtrata dai goal; il modello
  del mondo su cui l'artefatto agisce.
- **macchina (Mondo di sviluppo)** — com'è fatto l'artefatto; è il caso più
  letterale di system image alla Norman, l'artefatto che si documenta da sé per
  il prossimo agente. È legittimamente assente o sottile quando la macchina
  dell'artefatto è il tooling condiviso (il metodo via symlink, le regole
  operative) e non codice di dominio proprio: gemella simmetrica
  dell'esenzione-ought.
- **norma della macchina** — come l'artefatto deve essere costruito e mantenuto:
  principi d'ingegneria, invarianti di struttura, contratti dei componenti e
  motivazioni delle alternative scartate. Non è Goal: prescrive la macchina, non
  il motivo o il valore del dominio. Non è macchina: dice _come deve essere_,
  non _com'è_.

Due forme laterali vanno tenute esplicite invece di lisciate dentro le quattro
regioni:

- **il repertorio d'atto** — prescrivere l'atto sul Mondo (procedure, pratiche,
  runbook) non è descrivere la macchina né prescriverne la forma. È contenuto o3
  sceso verso la membrana: il _come si agisce_, distinto dal _com'è fatta_ la
  macchina e dal _come deve essere costruita_.
- **le sorgenti fuori posto** — maestri e fonti promossi a nodo non sono un polo
  del ciclo: sono fonti di verità che canonicamente vivono nel register e nel
  Mondo, non come nodi. La loro presenza nel corpo della KB è un'anomalia
  strutturale, spesso sintomo dello stesso sbilanciamento di una KB che accumula
  chi-l'ha-detto invece di cosa-è-vero.

Il baricentro non prescrive una distribuzione corretta unica: ciò che è sano
dipende dal dominio e dal grado di delegabilità del goal. Prescrive una sola
cosa — che entrambi i poli siano presenti dove il ciclo deve chiudersi. Un
dominio a goal codificabile può vivere senza nodi-ought, e un dominio la cui
macchina è il tooling condiviso senza nodi-macchina; ma nessun dominio che debba
generare azione può vivere senza il polo is contro cui l'ought si misura.

Configurazioni possibili:

- una KB patrimoniale può avere baricentro **is**, mentre gli obiettivi sono
  articolati nel register Goal;
- una KB di sistemi può concentrarsi su **macchina e norma**, con procedure vive
  in o3 e stato osservato nel runtime;
- una KB di integrazione può attraversare **macchina e is**, senza che questa
  ampiezza provi da sola una maggiore efficacia;
- una KB personale può avere baricentro **ought**: occorre verificare che
  pratica e condizioni reali siano leggibili nelle superfici del ciclo prima di
  proporre nuovi nodi.

Un segnale catturato ma mai interpretato può lasciare il ciclo privo di
informazione utilizzabile. Il rimedio può essere una sintesi i2, un confronto i3
o conoscenza durevole nella KB: dipende dalla funzione e dalla durata, non
esiste un obbligo di trasformare ogni segnale in nodo. Le fotografie datate e i
confronti degli adottanti vivono in `i2/`, i loro giudizi correnti in `i3/`.

Connessioni:

- [knowledge-base](knowledge-base.md)
- [system-image](system-image.md)
- [development-meta-cycle](development-meta-cycle.md)
- [goal](goal.md)
- [world](world.md)
- [processing-layers](processing-layers.md)
- [action-cycle-matrix](action-cycle-matrix.md)
- [cognitive-fidelity](cognitive-fidelity.md)
