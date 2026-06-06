---
data: 2026-06-06
stato: bozza
---

# Map

La mappa è il nodo che risponde alla domanda: come si tiene insieme questo dominio? Collega entità, fonti di verità, flussi, responsabilità, aree e nodi di approfondimento. Non serve a elencare tutto, ma a rendere visibile il modello del sistema. La sua istanza è il file root `map.md`: vista o2 letta a bootstrap, tenuta concisa e separata dal README (per pace) così che il file di identità non si gonfi.

Per un LLM la mappa è un dispositivo cognitivo fondamentale. Senza mappa, l'agente deve ricostruire il dominio da README, nomi file e link. Con una buona mappa, capisce rapidamente quali elementi sono centrali, quali fonti verificano i fatti e quali nodi aprire per un intervento.

Regole:

- è un file root (`map.md`), nel cruscotto del ciclo, letta come secondo passo del bootstrap (`README → map → CLAUDE → nodo`)
- collega sistema reale, fonti di verità e nodi
- non sostituisce il catalogo completo dei nodi (`kb/index.md`)
- non deve diventare storico o lista di task
- può essere diversa per domini tecnici, finanziari o riflessivi
- include lo strato output come dimensione esplicita: mostra dove vivono o1, o2, o3 nel progetto e come il ciclo di azione ritorna alla KB come nuova fonte; senza questa dimensione la mappa descrive solo l'accumulo di conoscenza, non il ciclo completo

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                   | Confronto con il metodo                                                                                                              |
| ---------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `nixos`    | `kb/project-map.md` collega host, profili home, macro-aree, fonti Nix e nodi.                        | Esempio forte di mappa code-based: trasforma filesystem e configurazione in modello leggibile.                                       |
| `bi`       | `kb/project-map.md` collega sistemi, flussi dati, script, moduli, fonti tecniche e task strutturali. | Mappa necessaria per un dominio ad alta complessità applicativa; riduce la dipendenza da CLAUDE e README.                            |
| `economia` | `kb/mappa-progetto.md` collega conti, investimenti, immobili, persone, successioni, dati e nodi.     | Buon adattamento non-code: la mappa rende verificabile il ponte tra entità reali, Drive/output JSON e KB.                            |
| `salute`   | Ha aggiunto `kb/mappa-progetto.md`, collegata a principi locali e verifica nel vivere.               | Conferma che una KB riflessiva ha bisogno di una mappa meno tecnica: assi concettuali, fonti, pratica, diario e percorsi di accesso. |

Il confronto mostra che la mappa è il componente più adattabile del metodo. Nei repo tecnici mappa codice e flussi; in `economia` mappa entità e dati; in `salute` mappa assi concettuali, fonti, pratiche e diario invece di host o script. La collocazione dell'istanza (root `map.md` nel metodo, `kb/*-map.md` in alcuni adottanti) è essa stessa materia di affinamento: la triade in struttura-progetto la vuole in root, nel cruscotto.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [indice](indice.md)
- [fonte-di-verita](fonte-di-verita.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [struttura-progetto](struttura-progetto.md)
