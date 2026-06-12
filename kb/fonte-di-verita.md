---
data: 2026-05-23
stato: bozza
---

# Fonte di verità

Una fonte di verità è ciò contro cui si verifica ciò che la KB dice. Risponde alla domanda: contro che cosa verifico ciò che la KB dice? Può essere codice, configurazione, JSON, documento autoritativo, database, output strutturato o mappa mantenuta manualmente.

La fonte di verità impedisce alla KB di diventare una descrizione plausibile ma disancorata. Nei progetti code-based può coincidere con file tecnici; nei progetti finanziari con documenti e JSON compilati; nei progetti riflessivi con fonti testuali, corpus elaborati o scelte interpretative dichiarate.

Regole:

- deve essere esplicita quando un fatto ha alta deriva
- deve essere distinta dalla sintesi interpretativa della KB
- può essere tecnica, documentale o umana a seconda del dominio
- va collegata dalle mappe e dai nodi ad alta responsabilità
- alimenta i controlli di fedeltà cognitiva
- non tutti i nodi richiedono la stessa intensità di verifica

## Applicazione nei progetti adottanti

- **`nixos`** — fonti di verità attuali: `flake.nix`, host, moduli Nix, profili Home Manager, filesystem. Confronto con il metodo: caso più verificabile — le fonti sono dichiarative e leggibili dagli script.
- **`bi`** — fonti di verità attuali: script, moduli JS, configurazioni, Baserow, WooCommerce, Danea, Google Sheets e output intermedi. Confronto con il metodo: dominio più complesso — bisogna distinguere fonti tecniche locali da sistemi esterni non sempre esportabili.
- **`economia`** — fonti di verità attuali: documenti grezzi, output JSON compilati, `stato.md`, `scadenze.md`, nodi entità e mappa. Confronto con il metodo: caso non-code ad alta responsabilità — la fonte autoritativa per analisi è `output/json/`, non la narrazione della KB.
- **`salute`** — fonti di verità attuali: fonti testuali elaborate, fonti raw, nodi concettuali, diario e pratica personale. Confronto con il metodo: la fonte di verità è meno meccanica — conta la tracciabilità interpretativa più che il fact check automatico.

Il confronto impedisce una generalizzazione troppo tecnica. "Fonte di verità" non significa sempre codice: può essere un JSON prodotto da parser, una tabella esterna, un documento legale, una fonte testuale o una scelta interpretativa dichiarata. La regola comune è esplicitare il livello di fiducia e non verificare documentazione contro altra documentazione.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [map](map.md)
- [strumenti-kb](strumenti-kb.md)
- [knowledge-base](knowledge-base.md)
