---
stato: maturo
---

# Design principles

Principi che governano l'architettura e lo sviluppo dei progetti che adottano il
cognitive artifact design. I principi universali si applicano a qualsiasi
progetto indipendentemente dal dominio; i principi code-based si applicano ai
progetti con codebase attiva. Ogni progetto può aggiungere principi specifici
nel proprio README — deviazioni dai principi universali vanno motivate nei fili
`i3/`.

## Principi universali

Applicabili a ogni progetto adottante, presente o futuro, qualunque sia il
dominio; il territorio corrente vive nel register `world.md`.

### Minimalismo

Nessun nodo morto, nessun dato duplicato non governato, nessuna funzionalità
inutilizzata. Se qualcosa non è attivo o rilevante, non esiste nel repository.
Applicato anche alla documentazione: un nodo che descrive un elemento rimosso va
eliminato o aggiornato.

### Fonte unica di verità

Ogni dato, regola o configurazione vive in un posto solo. I duplicati sono fonte
di drift: quando lo stesso fatto è scritto in due posti, uno divergerà
inevitabilmente. Se una duplicazione è necessaria per ragioni tecniche, il nodo
secondario deve indicare esplicitamente quale sia la fonte canonica.

### Tracciabilità

Le tensioni e le decisioni ancora aperte vivono nei fili `i3/` con motivazione
esplicita. Quando una decisione è stabilizzata, il vincolo e le condizioni di
revisione risalgono nella KB; il filo può chiudersi. Nessuna scelta importante
resta ricostruibile soltanto attraversando i commit. La tracciabilità riguarda
il perché, non il cosa: il cosa è già nel codice, nei dati e nei nodi.

### Esplicito su implicito

Le dichiarazioni visibili sono preferite alle assunzioni nascoste. Ciò che
potrebbe rimanere tacito — una dipendenza, una restrizione, una scelta di design
— va reso leggibile. Il costo di esplicitare è basso; il costo di dover
ricostruire un'assunzione implicita dopo mesi può essere alto.

## Principi per progetti code-based

Applicabili agli adottanti con una codebase attiva.

### Riproducibilità

Il repository dichiara come ricostruire il sistema e fissa le dipendenze in modo
verificabile (lock file, dichiarazioni esplicite). Segreti, dati e prerequisiti
esterni hanno fonti e procedure di recupero dichiarate. I passaggi manuali
inevitabili sono documentati: la riproducibilità non richiede di versionare
materiale sensibile o sistemi che il progetto non controlla.

### Modularità

Ogni funzionalità in un'unità separata con responsabilità chiara. La logica
comune viene estratta, non duplicata. Se due componenti condividono logica, va
estratta prima che la duplicazione crei divergenza.

### Idempotenza

Le operazioni possono essere rieseguite sugli stessi dati senza effetti
collaterali inattesi. In caso di errore o interruzione, è possibile ripartire
senza dover prima ripulire uno stato parziale.

## Principi specifici di progetto

Ogni progetto porta i propri principi specifici nel README o in un nodo locale
puntato dal README. La distinzione tra principi universali e principi locali va
resa esplicita: il lettore deve poter capire a colpo d'occhio cosa appartiene al
metodo condiviso e cosa è scelta del singolo progetto.

Le configurazioni ricorrenti mostrano la forma senza duplicare gli adottanti: un
progetto dichiarativo può vincolare software e hardware ammessi; una pipeline
può scegliere consistenza eventuale, isolamento degli errori e log strutturati;
un dominio riflessivo può subordinare la teoria alla pratica e trattare il
diario come grezzo per il filing back. I nomi, lo stato e l'incarnazione
corrente di questi principi restano nei repository di dominio.

## Principi per lo strato output

Applicabili a tutti i progetti con uno strato output esplicito. Derivano dai
criteri di Norman — visibilità, feedback, mapping, constraint — definiti come
criteri generali in `action-cycle` e `output`, articolati in `specify`. Vanno
usati come criteri di revisione, non come target estetici.

Quando un'azione desiderata e possibile non avviene, si verifica se lo strato
output renda leggibili alternative, vincoli ed esiti. L'inazione da sola non
prova un difetto: attendere, osservare o rinunciare può essere la scelta
corretta. Il criterio è sostenere una decisione informata e la sua eventuale
esecuzione, da valutare sul comportamento reale.

Connessioni:

- [cognitive-artifact-design](cognitive-artifact-design.md)
- [project-structure](project-structure.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [output](output.md)
- [action-cycle](action-cycle.md)
- [consent](consent.md)
