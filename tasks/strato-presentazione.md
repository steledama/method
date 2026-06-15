---
data: 2026-06-15
stato: aperto
---

# Strato di presentazione trasversale (deck → view)

Aperto in sessione di design 2026-06-15, allargando lo scope della system image
visiva (cfr. `verdict.md`, filo «Rifondazione atrio↔azione»). Il nodo `deck`
confonde oggi il concetto generale — una vista navigabile derivata — con una sua
forma concreta, il deck Reveal delle interpretazioni. Il task separa i due
livelli e costruisce uno strato di presentazione trasversale alle sorgenti.

## Decisioni

- **`view` è il concetto generale**: artefatto navigabile e derivato che rende
  leggibile una sorgente senza diventare una seconda fonte di verità.
- **`deck` resta una forma concreta di view**: una sequenza Reveal adatta a
  sintesi che si scorrono. Le occorrenze semantiche di «deck» non vanno
  sostituite meccanicamente.
- `kb/deck.md` viene rinominato `kb/view.md` e ampliato dal solo deck delle
  interpretazioni alle viste generate del progetto.
- `interpretations/`, `tasks/`, `plan.md` e `verdict.md` restano sorgenti pure;
  nessun HTML generato vive nelle collezioni o nei file-ciclo.
- gli HTML generati restano versionati per conservare l'affordance `file://`
  dal checkout.

## Struttura risultante

- `assets/` — risorse condivise dello strato:
  - token grafici e palette senza dipendenze da Reveal;
  - primitivi per diagrammi, card e ciclo di Norman;
  - adattatore Reveal, separato dagli stili condivisi;
- `views/interpretations.html` — deck esistente, derivato da
  `interpretations/metodo-in-sintesi.md`;
- `views/tasks.html` — deck dei task aperti, derivato da `plan.md` e `tasks/`;
- `views/verdict.html` — deck dei fili aperti, derivato da `verdict.md`;
- `index.html` — home statica della system image, realizzata dal task
  «System image visiva».

`views/` è una nuova specie nell'atrio: contiene presentazioni generate,
distinte sia dalle sorgenti sia dai cataloghi e file-ciclo. `assets/` è la
macchina condivisa che le rende coerenti.

## Vista Tasks

`views/tasks.html` è il gemello sul lato Specify del deck Interpretations:
trasforma la coda operativa in una superficie scorribile senza duplicarne la
supervisione.

- una slide per ogni task sostanziale, nello stesso ordine di `plan.md`;
- titolo dal relativo H1;
- `data`, `stato` e `sintesi` dal frontmatter;
- posizione, dipendenze ed eventuale contesto di scadenza da `plan.md`;
- link relativo al file `tasks/*.md` come sorgente di dettaglio.

Il frontmatter canonico dei task viene esteso con una sintesi autoriale,
obbligatoria e autosufficiente:

```yaml
---
data: YYYY-MM-DD
stato: aperto
sintesi: "Risultato atteso del task in una frase breve."
---
```

`sintesi` descrive il risultato atteso, non replica il titolo né registra
priorità o dipendenze. Data di ultima modifica e altre informazioni ricavabili
da Git non entrano nel frontmatter. Il task aggiorna `kb/tasks.md`, i controlli
strutturali e tutti i task aperti alla nuova forma.

Le righe semplici di `plan.md` prive di un file in `tasks/` non generano una
slide autonoma: restano visibili nella vista Plan della home.

## Vista Verdict

`views/verdict.html` deriva direttamente da `verdict.md`:

- ogni sezione `##` diventa una slide;
- titolo e corpo completo della sezione restano insieme;
- il preambolo del file può diventare una slide introduttiva;
- l'ordine delle slide coincide con l'ordine dei fili nel file.

Il deck non introduce sintesi manuali: `verdict.md` resta l'unica sorgente e la
vista ne cambia solo la forma di lettura.

## Pipeline e asset

Le tre viste usano una pipeline comune Pandoc/Reveal e lo stesso adattatore
grafico. La sorgente Interpretations passa direttamente a Pandoc; Tasks richiede
un generatore stdlib-only che combina frontmatter e `plan.md` in Markdown
derivato; Verdict usa le sezioni Markdown già presenti.

L'attuale `interpretations/reveal.css` va scomposto:

- token e primitivi realmente condivisibili, senza prefisso `.reveal`;
- regole specifiche del rendering Reveal;
- stile della home, aggiunto dal task successivo.

Reveal resta inizialmente su CDN. Il vendoring in `assets/` è ammesso quando
diventa necessario l'uso offline dei deck, ma non è requisito di questo task.

## Vincoli

- apertura via `file://` senza build preventiva, server o `fetch` di file
  locali;
- viste derivate, mai seconda fonte;
- path relativi validi dalla nuova collocazione in `views/`;
- HTML deterministico e versionato;
- nessun rename lessicale indiscriminato di «deck» in prosa;
- la home non viene realizzata in questo task.

## Implementazione

1. Rinominare e riscrivere `kb/deck.md` come `kb/view.md`; aggiornare `kb.md`.
2. Aggiornare `kb/tasks.md` e gli strumenti per il campo `sintesi`; migrare i
   task aperti.
3. Formalizzare in `project-structure.md` `assets/`, `views/` e la separazione
   tra sorgenti e presentazioni generate.
4. Creare lo split CSS condiviso/Reveal e spostare fuori da
   `interpretations/` gli asset presentativi.
5. Consolidare la build delle viste e generare i tre HTML in `views/`.
6. Aggiornare README, regole operative, `tools.md`, indici delle collezioni e
   sorgente Interpretations ai nuovi path.
7. Cercare globalmente backlink e riferimenti a `deck.md`,
   `interpretations/index.html` e `interpretations/reveal.css`; classificare
   ogni occorrenza prima di aggiornarla.
8. Propagare il rename agli adottanti dopo il task di disaccoppiamento,
   modificando solo le connessioni intenzionali rimaste.

## Verifica e criteri di chiusura

- ogni task sostanziale aperto possiede una `sintesi` valida;
- ordine, dipendenze e scadenze nella vista Tasks coincidono con `plan.md`;
- ogni sezione `##` di `verdict.md` produce una slide completa;
- Interpretations continua a renderizzare senza regressioni;
- le tre viste si aprono direttamente via `file://` e i link relativi
  funzionano;
- ricerca globale e audit non trovano backlink rotti o vecchi path;
- due generazioni consecutive producono gli stessi file;
- rigenerare tutte le viste su un checkout aggiornato lascia il working tree
  invariato.

## Fuori perimetro

- la home `index.html`, affidata al task «System image visiva»;
- `perceptions/` e `prescriptions/` come viste o destinazioni navigabili;
- una finestra-terminale o qualunque interfaccia che richieda un backend;
- il vendoring immediato di Reveal.
