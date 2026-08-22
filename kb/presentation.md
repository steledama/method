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

## HTML apribile direttamente

Il formato operativo minimo è un HTML versionato con path relativi, apribile con
doppio click o `xdg-open` sul file. Non deve richiedere build, deploy, servizi
permanenti o `fetch` di file locali, che i browser bloccano sotto `file://`.

Reveal può essere caricato da CDN senza introdurre dipendenze installate. L'HTML
si apre via `file://`; la connessione Internet serve solo a caricare il
framework, non a servire i file locali. Se serve uso offline, Reveal va
vendorizzato in `presentation/assets/`. La home statica non usa Reveal. Ha un
CSS proprio (`system-image.css`) condiviso tra i fork adottanti, ma il contratto
è minimale: token, base e sole classi emesse dal builder della home. Le classi
delle viste Reveal restano nel loro CSS.

## Grafica nativa e build minima

Le view usano HTML e CSS nativi per layout, diagrammi e componenti visivi; SVG
inline è disponibile quando serve controllo geometrico più preciso. Motori di
diagrammi come Mermaid introducono parser, vincoli di layout e dipendenze
runtime sproporzionati rispetto al vantaggio in presentazioni curate: non fanno
parte del pattern di default.

La build è versionata in entrypoint dedicati nella collezione `o3/`, uno per
famiglia di vista, registrati nel suo indice insieme agli altri esecutori. Gli
script restano privi di dipendenze installate quando possibile; gli asset comuni
vivono in `presentation/assets/`. Due generazioni consecutive devono produrre lo
stesso output: il determinismo è ciò che rende la rigenerazione un gesto
meccanico invece di una decisione.

## Apertura locale e condivisione on-demand

Il default è aprire il file localmente:

```bash
xdg-open presentation/<vista>.html
```

Solo per condividerlo temporaneamente con un altro dispositivo sulla stessa
LAN/VPN:

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory presentation
```

`http.server` non modifica il firewall. Sullo stesso host `localhost:8000`
funziona senza aprire porte; da un altro dispositivo la porta TCP scelta deve
essere ammessa dal firewall per la sola subnet o interfaccia privata necessaria.
Terminata la condivisione, si chiude il processo e si rimuove l'eventuale regola
temporanea.

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
