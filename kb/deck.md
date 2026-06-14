---
data: 2026-06-09
stato: bozza
---

# Deck

Il componente che rende le interpretazioni navigabili: il deck-tool è una
**cerniera** (cfr. `action-cycle`, sezione i2 micro/macro). In ogni dominio la
stessa superficie è o2 quando viene prodotta come vista di decisione e substrato
i2 quando viene letta per attribuire significato alla sintesi; cambia il
contenuto interpretato, non il ruolo tra repository. È distinto da `output`, che
porta il concetto dei livelli o1/o2/o3 e i1/i2/i3: questo nodo è il runbook
portabile — come il deck si costruisce, si apre e raggiunge
eventualmente un altro dispositivo. La sua istanza per repo è la cartella
`interpretations/`, con indice interno `interpretations/interpretations.md`.

Il deck non è l'unica forma dell'interpretazione. La forma segue la domanda
(Karpathy): una pagina markdown, una tabella di confronto, un deck di slide, un
grafico, un canvas sono tutte forme legittime, da scegliere secondo cosa
l'output deve far decidere o interpretare. Il deck è la forma-default per la
sintesi che si scorre; questo nodo ne fissa il pattern, non lo impone come unica
forma.

## HTML Reveal apribile direttamente

Il formato operativo minimo è `interpretations/index.html`: un deck Reveal
versionato, con path relativi, apribile direttamente dal checkout con doppio
click o `xdg-open interpretations/index.html`. Non deve richiedere build, deploy,
servizi permanenti o `fetch` di file locali, che i browser bloccano sotto
`file://`.

I file markdown possono restare sorgenti di dettaglio o materiale da cui si
distilla il deck, ma il deck non deve duplicarli integralmente: comprime
ciò che serve alla decisione e rimanda ai nodi per il dettaglio. Quando un deck
è generato meccanicamente da un `.md`, il comando di generazione deve essere
versionato; altrimenti l'HTML è esso stesso la sorgente presentativa. Il PDF
esce dall'export del deck, non da un secondo artefatto mantenuto a mano.

## Grafica nativa e build minima

Il deck usa HTML e CSS nativi per layout, diagrammi e componenti visivi; SVG
inline è disponibile quando serve controllo geometrico più preciso. Motori di
diagrammi come Mermaid introducono un parser, vincoli di layout e una dipendenza
runtime sproporzionati rispetto al vantaggio in presentazioni curate: non fanno
parte del pattern di default. Un'eccezione è giustificata solo per grafici
tecnici numerosi, standardizzati e realmente più manutenibili come testo.

Reveal può essere caricato da CDN senza introdurre dipendenze installate.
L'HTML si apre via `file://`; la connessione Internet serve solo a caricare il
framework, non a servire i file locali. Se serve uso offline, Reveal va
vendorizzato dentro `interpretations/`. Il contenuto e i diagrammi restano
comunque HTML/CSS/SVG del progetto e non dipendono da JavaScript di rendering.

Lo strumento del deck è uniforme tra i repo — è il «nome uniforme, carattere
nel contenuto» di `output`: il dominio non cambia il tool, cambia il registro.
Un deck riflessivo-analitico e uno viscerale-emotivo usano lo stesso motore e si
distinguono nel contenuto, secondo i tre livelli di Norman (cfr.
`processing-layers`).

## Apertura locale e condivisione on-demand

Il default è aprire il file localmente:

```bash
xdg-open interpretations/index.html
```

Solo per condividerlo temporaneamente con un altro dispositivo sulla stessa
LAN/VPN:

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory interpretations
```

`http.server` non modifica il firewall. Sullo stesso host `localhost:8000`
funziona senza aprire porte; da un altro dispositivo la porta TCP scelta deve
essere ammessa dal firewall per la sola subnet o interfaccia privata necessaria.
Su NixOS questo richiede una regola dichiarativa e un rebuild; non va aperta la
porta globalmente né esposta su WAN. Terminata la condivisione, si chiude il
processo e si rimuove l'eventuale regola temporanea.

## Provenienza bottom-up

Il pattern è emerso in `bi`. Una prima soluzione serviva il deck
permanentemente da due server e lo copiava con hook Git locali non versionati.
Il rename `presentazione/` → `presentations/` (poi → `interpretations/`) ha rotto gli hook in silenzio. La
soluzione finale non è stata rendere più complesso il deploy, ma eliminare un
servizio senza consumatori reali: l'HTML era già autonomo e apribile dal
checkout. Il commit `bi/ab8c6b5b` ha fissato apertura locale + `http.server`
on-demand; `nixos/d8da967` ha rimosso servizio e porta 8085. La generalizzazione
portabile è: **file locale per default, rete solo quando serve davvero**.

Connessioni:

- [output](output.md)
- [action-cycle](action-cycle.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [processing-layers](processing-layers.md)
- [karpathy-pattern](karpathy-pattern.md)
- [project-structure](project-structure.md)
- [verdict](verdict.md)
