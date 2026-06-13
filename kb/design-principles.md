---
data: 2026-05-24
stato: maturo
---

# Principi Guida

Principi che governano l'architettura e lo sviluppo dei progetti che adottano il metodo KB. I principi universali si applicano a qualsiasi progetto indipendentemente dal dominio; i principi code-based si applicano ai progetti con codebase attiva. Ogni progetto può aggiungere principi specifici nel proprio README — deviazioni dai principi universali vanno motivate in `verdict.md`.

## Principi universali

Applicabili a tutti i progetti: nixos, bi, economia, salute e futuri.

### Minimalismo

Nessun nodo morto, nessun dato duplicato non governato, nessuna funzionalità inutilizzata. Se qualcosa non è attivo o rilevante, non esiste nel repository. Applicato anche alla documentazione: un nodo che descrive un elemento rimosso va eliminato o aggiornato.

### Fonte unica di verità

Ogni dato, regola o configurazione vive in un posto solo. I duplicati sono fonte di drift: quando lo stesso fatto è scritto in due posti, uno divergerà inevitabilmente. Se una duplicazione è necessaria per ragioni tecniche, il nodo secondario deve indicare esplicitamente quale sia la fonte canonica.

### Tracciabilità

Le decisioni significative si registrano in `verdict.md` con motivazione esplicita. Nessuna scelta architetturale importante resta implicita o distribuita nei commit. La tracciabilità riguarda il perché, non il cosa: il cosa è già nel codice, nei dati e nei nodi.

### Esplicito su implicito

Le dichiarazioni visibili sono preferite alle assunzioni nascoste. Ciò che potrebbe rimanere tacito — una dipendenza, una restrizione, una scelta di design — va reso leggibile. Il costo di esplicitare è basso; il costo di dover ricostruire un'assunzione implicita dopo mesi può essere alto.

## Principi per progetti code-based

Applicabili a nixos, bi e altri progetti con codebase attiva.

### Riproducibilità

Il sistema è ricostruibile da zero a partire dal repository. Le dipendenze sono fissate in modo verificabile (lock file, dichiarazioni esplicite). Zero configurazioni manuali fuori dal repository.

### Modularità

Ogni funzionalità in un'unità separata con responsabilità chiara. La logica comune viene estratta, non duplicata. Se due componenti condividono logica, va estratta prima che la duplicazione crei divergenza.

### Idempotenza

Le operazioni possono essere rieseguite sugli stessi dati senza effetti collaterali inattesi. In caso di errore o interruzione, è possibile ripartire senza dover prima ripulire uno stato parziale.

## Principi specifici di progetto

Ogni progetto porta i propri principi specifici nel README o in un nodo locale puntato dal README. La distinzione tra principi universali e principi locali va resa esplicita: il lettore deve poter capire a colpo d'occhio cosa appartiene al metodo condiviso e cosa è scelta del singolo progetto.

Esempi di principi specifici adottati nei progetti correnti:

- **nixos**: Home Manager standalone (timeline sistema/utente disaccoppiate), Explicit Unfree (nessun software non-libero entra silenziosamente), Hardware-Specific (moduli hardware corrispondono all'hardware reale)
- **bi**: Sincronizzazione graduale / Eventual consistency (gli aggiornamenti si propagano gradualmente con meccanismi di riprova), Isolamento degli errori / Graceful degradation (un errore su un elemento non blocca l'intero processo), Tracciabilità operativa (ogni elaborazione automatica produce un log strutturato con riepilogo via email)
- **salute**: teoria verificata nella pratica, corpo e mente come unico campo, fonti come mappe, diario come materiale grezzo per filing back

## Principi per lo strato output

Applicabili a tutti i progetti con uno strato output esplicito. Derivano dai criteri di Norman — visibilità, feedback, mapping, constraint — definiti come checklist di revisione in `ciclo-azione` e `output`. Vanno usati come criteri di revisione, non come target estetici.

Il principio cardine resta: se l'utente non agisce, lo strato output è mal progettato — non l'utente è pigro. Questi principi si valutano sul comportamento reale, non sulla qualità dei nodi sottostanti.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [struttura-progetto](struttura-progetto.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [consenso](consenso.md)
