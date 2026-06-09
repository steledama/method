# Presentazioni

Porta-collezione di `presentations/` nell'atrio di root: lo strato output o2/o3 del repo — le
viste sintetiche che non possono stare in `kb/` senza violare l'atomicità zettelkastiana (la
sintesi vive qui, non nei nodi; cfr. [output](kb/output.md)). Si vede a colpo d'occhio, si
legge e si distribuisce on-demand.

## presentations/

- [metodo-in-sintesi](presentations/metodo-in-sintesi.md) — la sintesi illustrata del metodo:
  dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo dell'azione come
  specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al processo (anatomia,
  sviluppo, routing). Cristallizza lo stadio Compare del ciclo di sviluppo.

Il `.md` è la fonte unica; `index.html` lo rende come deck Reveal.js (caricato da CDN,
diagrammi Mermaid inclusi). Il deck carica il markdown via `fetch`, quindi si apre servendo
la cartella — `cd presentations && python3 -m http.server`, poi `localhost:8000` — non con un
doppio-clic su `file://`. Il PDF (o3) per stampa/distribuzione esce dall'export del deck
(apertura con `?print-pdf` e stampa, oppure `decktape`), non da `md2pdf`, e non è versionato.
