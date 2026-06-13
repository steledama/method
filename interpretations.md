# Interpretazioni

Porta-collezione di `interpretations/` nell'atrio di root: lo stadio i2 (Interpret) del
ciclo di sviluppo — le sintesi visive che rendono co-presenti le tensioni tra i nodi e
aggiornano il modello mentale di chi mantiene il metodo (cfr. [output](kb/output.md),
[ciclo-azione](kb/ciclo-azione.md), [system-image](kb/system-image.md)). Non possono
stare in `kb/` senza violare l'atomicità zettelkastiana: la sintesi vive qui, non nei
nodi. Si vede a colpo d'occhio, si legge e si distribuisce on-demand.

## interpretations/

- [metodo-in-sintesi](interpretations/metodo-in-sintesi.md) — la sintesi illustrata del
  metodo: dall'ontologia (artefatto/sistema/metodo) alla meccanica (tre giganti, ciclo
  dell'azione come specchio simmetrico, cicli annidati, le quattro dimensioni, goal) al
  processo (anatomia, sviluppo, routing). Ogni sezione è un'interpretazione: rivela una
  tensione altrimenti invisibile da dentro i singoli nodi.

`index.html` è l'indice generato della collezione — prodotto dalla sorgente markdown con
`tools/build-presentation.sh`, rende le interpretazioni come deck Reveal.js (caricato da
CDN) ed è apribile direttamente dal checkout. Diagrammi e componenti visivi sono HTML/CSS
nativi, con SVG inline disponibile per geometrie che lo richiedono: nessun motore grafico
JavaScript interviene a runtime. Il server Python è solo un'opzione di condivisione
temporanea su LAN/VPN: `python3 -m http.server 8000 --bind 0.0.0.0 --directory
interpretations`; per client remoti la porta deve essere ammessa dal firewall sulla sola
rete privata. Il PDF per stampa/distribuzione esce dall'export del deck e non è
versionato.
