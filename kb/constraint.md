---
data: 2026-06-09
stato: bozza
---

# Constraint

Una limitazione progettata che riduce le azioni possibili a quelle valide. Norman lo elenca tra i meccanismi con cui il design risponde alle domande dell'utente — accanto a mapping, significanti, modelli concettuali, feedback e visibilità — ed è ciò che nei progetti si chiama spesso _guardrail_. La sua forza sta nel livello a cui opera: dove un check riflessivo (ricordarsi di fare X) può saltare, il vincolo rende l'azione sbagliata impossibile, oppure rumorosa. Non chiede attenzione: la rende superflua.

Norman distingue quattro tipi. I vincoli _fisici_ limitano per geometria (un pezzo entra in un solo verso). I _culturali_ poggiano su convenzioni condivise. I _semantici_ derivano dal significato della situazione. I _logici_ escludono per deduzione le alternative impossibili. Le _forcing function_ sono il caso forte: impediscono di proseguire finché un passo necessario non è compiuto.

Nel metodo il vincolo è un componente che si _progetta e si costruisce_, non un criterio con cui si valuta — per questo ha un nodo proprio, distinto dalle proprietà valutative (visibilità, feedback, mapping). Le sue incarnazioni ricorrono cross-progetto: i guardrail sulla freschezza degli input; la configurazione dichiarativa che rende irrappresentabili gli stati invalidi; gli schemi e i test che rifiutano dati malformati; l'audit di `kb_tools` e il gate del commit, che bloccano prima di fissare; i check di fedeltà cognitiva, che sono vincoli contro il drift di significato.

Il vincolo è il presidio strutturale che regge quando il livello riflessivo cede. Nei tre livelli di Norman il check «ricordarsi di» vive in alto, dove l'attenzione è scarsa e intermittente; il vincolo vive sotto, nella struttura, e non dipende dal ricordo. È la lezione del deploy della presentazione rotto da un rename: mancava un vincolo — niente forzava «servito = repo» — così il guasto è stato silenzioso. Un vincolo (un symlink che lega servito e sorgente, un test che fallisce, uno schema) lo avrebbe reso impossibile o rumoroso. La regola di progetto che ne segue: dove un errore conta, non affidarsi alla memoria di un agente, ma costruire il vincolo che lo intercetta.

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [action-cycle](action-cycle.md)
- [processing-layers](processing-layers.md)
- [cognitive-fidelity](cognitive-fidelity.md)
- [system-image](system-image.md)
- [view](view.md)
