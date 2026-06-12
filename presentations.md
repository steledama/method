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

`index.html` è generato dalla sorgente markdown con
`tools/build-presentation.sh`, rende la sintesi come deck Reveal.js (caricato da
CDN) ed è apribile direttamente dal checkout. Diagrammi e componenti visivi
sono HTML/CSS nativi, con SVG inline disponibile per geometrie che lo
richiedono: nessun motore grafico JavaScript interviene a runtime. Il server
Python è solo un'opzione di condivisione temporanea su LAN/VPN:
`python3 -m http.server 8000 --bind 0.0.0.0 --directory presentations`; per
client remoti la porta deve essere ammessa dal firewall sulla sola rete privata.
Il PDF per stampa/distribuzione esce dall'export del deck e non è versionato.
