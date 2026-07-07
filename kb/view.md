---
stato: bozza
---

# View

La view è una rappresentazione navigabile e derivata: rende leggibile una sorgente
del progetto senza diventare una seconda fonte di verità. È la cerniera o2/i2 del
metodo (cfr. `action-cycle`, sezione i2 micro/macro): o2 quando orienta una
decisione, i2 quando viene letta per attribuire significato a ciò che sintetizza.

La vista Reveal a slide è una forma concreta di view, adatta a una sintesi che si scorre.
Non è l'unica forma possibile. La forma segue la domanda (Karpathy): pagina
markdown, tabella di confronto, presentazione a slide, grafico, canvas e home statica sono
forme alternative, scelte secondo cosa devono far capire o decidere.

## Vista derivata, mai seconda fonte

Una view versionata deve poter essere aperta direttamente dal checkout, ma il suo
contenuto non si mantiene a mano se esiste una sorgente canonica. La sorgente resta
nel file-ciclo o nella collezione-stadio; la view cambia la forma di lettura.

Nel repo `metodo` le viste generate vivono in `presentation/`:

- `presentation/interpretations.html` deriva da `i2/metodo-in-sintesi.md`;
- `presentation/tasks.html` deriva da `o1/plan.md` e dai file in `o2/`;
- `presentation/verdict.html` deriva dai fili in `i3/`;
- `presentation/index.html` deriva da `README.md`, `o1/plan.md` e dalla configurazione delle viste.

Le sorgenti rimangono pure: `i2/`, `o2/`, `o1/plan.md` e `i3/` non incorporano HTML generato.

## HTML apribile direttamente

Il formato operativo minimo è un HTML versionato con path relativi, apribile con
doppio click o `xdg-open presentation/interpretations.html`. Non deve richiedere build,
deploy, servizi permanenti o `fetch` di file locali, che i browser bloccano sotto
`file://`.

Reveal può essere caricato da CDN senza introdurre dipendenze installate. L'HTML si
apre via `file://`; la connessione Internet serve solo a caricare il framework, non
a servire i file locali. Se serve uso offline, Reveal va vendorizzato in `presentation/assets/`.
La home statica non usa Reveal. Ha un CSS proprio (`system-image.css`) condiviso
tra i fork adottanti, ma il contratto è minimale: token, base e sole classi
emesse dal builder della home. Le classi delle viste Reveal restano nel loro CSS.

## Grafica nativa e build minima

Le view usano HTML e CSS nativi per layout, diagrammi e componenti visivi; SVG
inline è disponibile quando serve controllo geometrico più preciso. Motori di
diagrammi come Mermaid introducono parser, vincoli di layout e dipendenze runtime
sproporzionati rispetto al vantaggio in presentazioni curate: non fanno parte del
pattern di default.

La build è versionata in due entrypoint: `o3/build-presentation.sh` usa
Pandoc/Reveal per le viste a slide e `o3/build-system-image.sh` genera la home
statica. Gli script Python in `o3/` restano stdlib-only; gli asset comuni vivono
in `presentation/assets/`. Due generazioni consecutive devono produrre lo stesso output.

## Apertura locale e condivisione on-demand

Il default è aprire il file localmente:

```bash
xdg-open presentation/interpretations.html
```

Solo per condividerlo temporaneamente con un altro dispositivo sulla stessa LAN/VPN:

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory presentation
```

`http.server` non modifica il firewall. Sullo stesso host `localhost:8000`
funziona senza aprire porte; da un altro dispositivo la porta TCP scelta deve essere
ammessa dal firewall per la sola subnet o interfaccia privata necessaria. Terminata
la condivisione, si chiude il processo e si rimuove l'eventuale regola temporanea.

## Provenienza bottom-up

Il pattern è emerso in `bi`. Una prima soluzione serviva la vista a slide permanentemente da
due server e lo copiava con hook Git locali non versionati. Il rename
`presentazione/` → `presentations/` (poi → `interpretations/`) ha rotto gli hook in
silenzio. La soluzione finale non è stata rendere più complesso il deploy, ma
eliminare un servizio senza consumatori reali: l'HTML era già autonomo e apribile
dal checkout. Il commit `bi/ab8c6b5b` ha fissato apertura locale + `http.server`
on-demand; `nixos/d8da967` ha rimosso servizio e porta 8085.

Connessioni:

- [output](output.md)
- [action-cycle](action-cycle.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [processing-layers](processing-layers.md)
- [karpathy-pattern](karpathy-pattern.md)
- [project-structure](project-structure.md)
- [verdict](verdict.md)
