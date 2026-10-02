---
stato: bozza
---

# Presentation

La superficie presentativa dell'artefatto: dove le viste derivate vengono rese,
aperte e condivise. Se `view` tiene la disciplina della derivazione — a quali
obblighi una vista risponde — questo nodo tiene la sua **materializzazione**: il
formato che si apre senza attrezzatura, la build che lo produce e il modo in cui
raggiunge un lettore che non ha il checkout.

La cartella `presentation/` è la casa di questa superficie: le viste generate e
gli asset condivisi. Non è una collezione-stadio e non ha indice proprio — è
rappresentazione derivata, e la sua fonte vive sempre altrove.

## Compartimento stagno

`presentation/` si apre e si serve da sola: nessun URL emesso esce dalla
cartella. Un link a una fonte (`../goal.md`, `../o2/…`) diventa la sua
etichetta; restano link le ancore, i file della cartella e gli URL con schema.
Il legame che una vista deve conservare si porta dentro: la chiave `Ob.` del
plan apre la legenda degli obiettivi, una slide della vista con i titoli letti
da `goal.md`. Le immagini di una vista hanno la fonte nella loro collezione (le
tavole delle Interpretazioni in `i2/`) e la build le copia in
`presentation/assets/`: la dipendenza resta nel verso della derivazione, e git
salva una volta sola i file identici. Il builder rompe se un'immagine manca o
un URL esce dalla cartella: è il «derivata implica verificata» di
`view` applicato al confine.

## HTML apribile direttamente

Il formato operativo minimo è un HTML versionato con path relativi, apribile con
doppio click o `xdg-open` sul file. Non deve richiedere build, deploy, servizi
permanenti o `fetch` di file locali, che i browser bloccano sotto `file://`.

Reveal può essere caricato da CDN senza introdurre dipendenze installate. L'HTML
si apre via `file://`; la connessione Internet serve solo a caricare il
framework, non a servire i file locali. Se serve uso offline, Reveal va
vendorizzato in `presentation/assets/`. La home statica non usa Reveal. Ha un
CSS proprio (`system-image.css`) condiviso tra i fork adottanti, ma il contratto
è minimale: token, base e sole classi emesse dal builder della home. Le viste
Reveal hanno un solo CSS canonico, `deck.css`, uguale in ogni repo: base pulita
sul tema `white`, titoli con barra d'accento, cover, slide `hero` e tavola,
tabella del plan. Le classi di dominio (diagrammi, componenti di un deck
specifico) vivono in un CSS locale del repo, dichiarato in `CSS_LOCALI` di
`o3/presentation/project.py`.

## Identità del progetto

Le presentazioni dei progetti sono uniformi: a distinguerle sono solo la
**sigla** nei titoli delle viste («Method Plan», «BI Piano», nella lingua del
repo) e un **colore d'accento** unico per progetto, che vale per viste, liste e
home. Lo stile a sketch è stato abbandonato perché troppo confidenziale per una
superficie che deve passare da un repo all'altro senza attrito. Sigla, lingua,
accento e sorgente del deck — un Markdown in `DECK`, oppure un builder di
dominio in `DECK_BUILDER` quando il deck si genera dai dati del repo — si
dichiarano in un solo file,
`o3/presentation/project.py`; la build scrive l'accento in
`presentation/assets/theme.css`.

La home resta minimale, pura affordance di navigazione, senza modalità
dev/runtime. Se la lente dev/runtime servirà, entrerà come filtro nelle singole
viste, che già mostrano la colonna `Ciclo`; finché l'uso non la chiede, resta
rimandata.

## Grafica nativa e build minima

Le view usano HTML e CSS nativi per layout, diagrammi e componenti visivi; SVG
inline è disponibile quando serve controllo geometrico più preciso. Motori di
diagrammi come Mermaid introducono parser, vincoli di layout e dipendenze
runtime sproporzionati rispetto al vantaggio in presentazioni curate: non fanno
parte del pattern di default.

La build è versionata in `o3/presentation/`, con lo **stesso path in ogni
repo**: chi passa da un progetto all'altro, umano o agente, non deve scoprire
dove stanno i builder, e le skill citano un solo comando. L'entrypoint è unico,
`python3 o3/presentation/build.py`: rigenera tutte le viste, la home e gli
asset, e chiude col presidio del compartimento stagno. È Python e non shell
perché deve girare anche sugli host Windows. Gli script restano privi di
dipendenze installate oltre a Pandoc e Prettier; gli asset comuni vivono in
`presentation/assets/`. Due generazioni consecutive devono produrre lo
stesso output: il determinismo è ciò che rende la rigenerazione un gesto
meccanico invece di una decisione.

## Apertura locale e condivisione on-demand

Il default è aprire il file localmente:

```bash
xdg-open presentation/<vista>.html
```

Per aprirla da un altro PC della LAN, lo stesso comando in ogni repo e su ogni
sistema (su Windows `py o3\presentation\serve.py`):

```bash
python3 o3/presentation/serve.py
```

Il server usa solo la libreria standard e serve la sola cartella
`presentation/`, che è chiusa su se stessa: niente dotfile, niente elenchi di
cartella. Stampa gli URL raggiungibili, ascolta per default sulla porta 8765
(`--port`, `--bind` per cambiarla o restringerla) e si chiude con Ctrl-C.

Il server non tocca il firewall. Da un altro dispositivo la porta deve essere
ammessa per la sola rete privata: sugli host con firewall dichiarativo la
regola vive nella loro configurazione, e finché il server non gira sulla porta
non ascolta nessuno; su Windows la prima esecuzione apre il prompt del
firewall.

## Vincolo conservato

Una vista autonoma non giustifica un servizio permanente senza consumatori
reali. Hook host-local e copie servite separatamente dal checkout possono
rompersi in silenzio dopo un rename; apertura locale e condivisione on-demand
mantengono invece sorgente e resa nello stesso artefatto. La condizione di
revisione è un bisogno reale di disponibilità continua o accesso remoto, non la
sola possibilità tecnica di mantenere un servizio.

Connessioni:

- [view](view.md)
- [output](output.md)
- [project-structure](project-structure.md)
- [constraint](constraint.md)
- [processing-layers](processing-layers.md)
- [affordance-signifier](affordance-signifier.md)
