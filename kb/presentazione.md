---
data: 2026-06-09
stato: bozza
---

# Presentazione

Il componente che rende lo strato output navigabile e lo pubblica nel mondo: l'o2 reso in forma percepibile e il suo o3, la pubblicazione. È distinto da `output`, che porta il concetto dei livelli o1/o2/o3: questo nodo è il runbook portabile — come la presentazione si costruisce, da dove si genera e come raggiunge il mondo senza che il percorso resti nella testa di chi l'ha configurato. La sua istanza per repo è la cartella `presentations/` e il register `presentations.md`.

La presentazione non è l'unica forma dell'o2. La forma segue la domanda (Karpathy): una pagina markdown, una tabella di confronto, un deck di slide, un grafico, un canvas sono tutte forme legittime, da scegliere secondo cosa l'output deve far decidere. Il deck è la forma-default per la sintesi che si scorre; questo nodo ne fissa il pattern, non lo impone come unica forma.

## Sorgente unica in markdown

Un solo file markdown per presentazione è la sorgente versionabile, e da lì si generano tutti gli output: documento leggibile su GitHub, deck web, PDF. Non si tiene un file-documento più un file-slide separati: due copie divergono, e il drift tra loro è esattamente ciò che la fonte unica evita. Il deck rende lo stesso markdown (Reveal con `data-markdown`, separatore di slide sui titoli di sezione); il PDF esce dall'export del deck, non da una seconda catena. Il prezzo da accettare è che il contenuto-slide vuole essere conciso: le sezioni prosa-pesanti si asciugano, il dettaglio resta nei nodi che la presentazione comprime.

## Build senza dipendenze

Il deck carica il framework da CDN e non introduce build step né dipendenze installate (il caso `bi`: `presentations/index.html` con Reveal da CDN, markdown come sorgente e diagrammi strutturali resi con Mermaid). Lo strumento del deck è uniforme tra i repo — è il «nome uniforme, carattere nel contenuto» di `output`: il dominio non cambia il tool, cambia il registro. Un deck riflessivo-analitico (diagrammi che fanno affiorare contraddizioni, come la sintesi del metodo su sé stesso) e uno viscerale-emotivo (un'infografica che muove all'azione, come serve a `salute`) usano lo stesso motore e si distinguono nel contenuto, secondo i tre livelli di Norman (cfr. `visceral-behavioral-reflective`).

## Pubblicazione: servire, non copiare a mano, dietro un confine, versionato

L'o2 vive in-repo; l'o3 è renderlo raggiungibile. Tre vincoli, tutti appresi sul campo:

- **Servito dalla sorgente, per un percorso versionato.** Ciò che è pubblicato deve derivare dal repo per un percorso che si aggiorna da sé a ogni `git pull` — un symlink, o una copia eseguita da uno script versionato, o un'unità dichiarativa nel repo di infrastruttura. Una copia a mano, o un hook in `.git/hooks/`, è un passo che vive fuori dall'artefatto: non si versiona, non è sotto gli occhi di nessuno, e si perde o si rompe in silenzio.
- **Dietro un confine di rete.** Una presentazione si espone solo su rete privata (LAN/VPN), mai su WAN: una pagina statica su WAN attira brute-force e scanner. È una lezione già pagata, registrata in `nixos/why.md`.
- **Il percorso di pubblicazione è versionato nel repo di infrastruttura.** Non nella memoria di chi ha fatto il deploy. È «una decisione non scritta è persa» applicata all'o3.

**Il caso `bi` come monito.** `nixos` serve `/var/www/presentazione` con un endpoint HTTP statico su rete privata, e il repo `bi` è git-pullato a notte su entrambi i server del paio. Il deploy c'era — un hook `post-merge`/`post-commit` che copiava la cartella della presentazione in quella servita — ma viveva in `.git/hooks/`, che non si versiona: non era nel system image, esisteva solo su quei due dischi. Quando la cartella è stata rinominata (`presentazione`→`presentations`), l'hook ha continuato a cercare il vecchio nome, ha smesso di matchare e ha smesso di copiare, in silenzio. La presentazione servita è rimasta congelata a mesi prima, identica al repo solo finché il contenuto non cambiava. Un rename ha rotto il deploy, e nessuno ha potuto collegare le due cose perché il deploy non era sotto gli occhi di nessuno. È l'assunzione stale del caso `bi/1018022` (cfr. `ciclo-azione`, `fedelta-cognitiva`), qui sull'o3: il presidio è scrivere il deploy nel repo — una riga nello script versionato che già fa il pull, o un'unità dichiarativa in `nixos` — mai in un hook locale. La forma del fix è locale ai repo `bi`/`nixos`; il principio — il deploy va versionato — è di metodo.

Connessioni:

- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [visceral-behavioral-reflective](visceral-behavioral-reflective.md)
- [pattern-karpathy](pattern-karpathy.md)
- [struttura-progetto](struttura-progetto.md)
- [why](why.md)
