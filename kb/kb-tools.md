---
stato: maturo
---

# KB tools

Gli strumenti KB rendono deterministici i controlli ripetitivi: parsing dei
link, backlink, catalogo, frontmatter, formato e copertura. Non decidono quali
concetti siano veri o utili. Lo script produce evidenze; umano e LLM le
interpretano e modificano la conoscenza.

`o3/kb_tools.py` offre una superficie portabile usata dalla skill `kb`:

- `audit [--format markdown|json]`: report strutturale completo; i link sono
  verificati anche fuori dall'inventario dei nodi — register dei poli, bussola,
  regole e indici delle collezioni — perché un riferimento a un filo rimosso
  resterebbe altrimenti invisibile;
- `backlinks NODE`, `orphans`: topologia della rete;
- `readme`, `migration`: catalogo e convenzioni documentali;
- `facets`: attributi di dominio dichiarati nel frontmatter;
- `terms`: candidati terminologici da valutare, non nuovi nodi automatici;
- `inventory`, `coverage`: inventario e copertura per progetti con codice.

Il nucleo comune resta indipendente dal dominio. Un adottante può aggiungere
controlli `facts` o `fidelity` quando dispone di fonti primarie leggibili, e può
dichiarare facet locali tramite `EXTENDED_FACETS`. Le estensioni preservano i
comandi base, così skill e audit comparativi possono usare la stessa interfaccia.

La documentazione segue una sola gerarchia: README rende lo strumento
rintracciabile, CLAUDE indica quando usarlo, i nodi ne definiscono capacità e
limiti, mentre gli indici delle collezioni registrano prescrizioni ed esecutori
concreti. Per questo `coverage` considera README, KB e indici di collezione:
richiedere un nodo per ogni modulo interno trasformerebbe la KB in un inventario
della macchina già custodito da `o3/prescriptions.md`. Ripetere ovunque
procedure, opzioni e file crea drift.

Regole d'uso:

- preferire lo script versionato a parser improvvisati in sessione;
- mantenere separati audit strutturale e revisione semantica;
- confrontare i fatti con fonti primarie, mai con altra documentazione;
- conservare nei fili solo il cambiamento di giudizio prodotto dall'audit, non
  il report rigenerabile;
- tenere le estensioni locali e, quando possibile, prive di dipendenze esterne.

Lo scope intenzionale è la struttura della KB e dei documenti supportati. La
qualità delle decisioni, dei router e delle prescrizioni resta una valutazione
qualitativa (`cognitive-fidelity`).

Connessioni:

- [knowledge-base](knowledge-base.md)
- [node](node.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [source-of-truth](source-of-truth.md)
- [method-observatory](method-observatory.md)
