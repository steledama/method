---
data: 2026-05-24
stato: aperto
---

# Superficie portabile kb_tools.py: comandi avanzati

`nixos` ha i comandi `inventory`, `facts`, `coverage`, `fidelity` che verificano il legame tra KB e sistema reale. `bi` ha `script_missing_docs` e `script_docs_count`. `economia` ha `facts` sulla mappa. La versione portabile del metodo ha solo i comandi base.

## Azione

- confrontare le implementazioni di `facts` e `fidelity` tra nixos ed economia: c'è una struttura comune separabile dalla fonte di verità specifica?
- identificare la parte domain-agnostic (struttura del controllo, livelli errore/avviso/info) dalla parte domain-specific (fonti di verità, entità)
- decidere se aggiungere stub/template per `facts` e `fidelity` nel `scripts/kb_tools.py` portabile, in modo che ogni progetto li sovrascriva invece di crearli da zero

## Criterio di chiusura

`kb/strumenti-kb.md` aggiornato con la decisione. Se si aggiunge lo stub al portabile, aprire task separato per l'implementazione.
