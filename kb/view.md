---
data: 2026-06-09
stato: bozza
---

# View

La view è una rappresentazione navigabile e derivata: rende leggibile una sorgente
del progetto senza diventare una seconda fonte di verità. È la cerniera o2/i2 del
metodo (cfr. `action-cycle`, sezione i2 micro/macro): o2 quando orienta una
decisione, i2 quando viene letta per attribuire significato a ciò che sintetizza.

Il deck Reveal è una forma concreta di view, adatta a una sintesi che si scorre.
Non è l'unica forma possibile. La forma segue la domanda (Karpathy): pagina
markdown, tabella di confronto, deck di slide, grafico, canvas e home statica sono
forme alternative, scelte secondo cosa devono far capire o decidere.

## Vista derivata, mai seconda fonte

Una view versionata deve poter essere aperta direttamente dal checkout, ma il suo
contenuto non si mantiene a mano se esiste una sorgente canonica. La sorgente resta
nel file-ciclo o nella collezione-stadio; la view cambia la forma di lettura.

Nel repo `metodo` le viste generate vivono in `views/`:

- `views/interpretations.html` deriva da `interpretations/metodo-in-sintesi.md`;
- `views/tasks.html` deriva da `plan.md` e dai file in `tasks/`;
- `views/verdict.html` deriva da `verdict.md`;
- `index.html`, quando presente, deriva da `README.md`, `plan.md` e dalla
  configurazione delle viste.

Le sorgenti rimangono pure: `interpretations/`, `tasks/`, `plan.md` e
`verdict.md` non incorporano HTML generato.

## HTML apribile direttamente

Il formato operativo minimo è un HTML versionato con path relativi, apribile con
doppio click o `xdg-open views/interpretations.html`. Non deve richiedere build,
deploy, servizi permanenti o `fetch` di file locali, che i browser bloccano sotto
`file://`.

Reveal può essere caricato da CDN senza introdurre dipendenze installate. L'HTML si
apre via `file://`; la connessione Internet serve solo a caricare il framework, non
a servire i file locali. Se serve uso offline, Reveal va vendorizzato in `assets/`.
La home statica non usa Reveal, ma condivide token, palette e primitivi grafici.

## Grafica nativa e build minima

Le view usano HTML e CSS nativi per layout, diagrammi e componenti visivi; SVG
inline è disponibile quando serve controllo geometrico più preciso. Motori di
diagrammi come Mermaid introducono parser, vincoli di layout e dipendenze runtime
sproporzionati rispetto al vantaggio in presentazioni curate: non fanno parte del
pattern di default.

La build è versionata in `tools/build-presentation.sh`: usa Pandoc/Reveal per le
viste a slide, `tools/build_views.py` per le sorgenti derivate e gli asset comuni in
`assets/`. Due generazioni consecutive devono produrre lo stesso output.

## Apertura locale e condivisione on-demand

Il default è aprire il file localmente:

```bash
xdg-open views/interpretations.html
```

Solo per condividerlo temporaneamente con un altro dispositivo sulla stessa LAN/VPN:

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory views
```

`http.server` non modifica il firewall. Sullo stesso host `localhost:8000`
funziona senza aprire porte; da un altro dispositivo la porta TCP scelta deve essere
ammessa dal firewall per la sola subnet o interfaccia privata necessaria. Terminata
la condivisione, si chiude il processo e si rimuove l'eventuale regola temporanea.

## Provenienza bottom-up

Il pattern è emerso in `bi`. Una prima soluzione serviva il deck permanentemente da
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
