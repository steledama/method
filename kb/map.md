---
data: 2026-06-06
stato: bozza
---

# Map

La mappa è il **register dell'indice-di-dominio**: il file che risponde alla domanda _com'è fatto il territorio reale di questo progetto?_ Collega entità, fonti di verità, flussi, responsabilità, aree e nodi di approfondimento. Non elenca tutto: rende visibile il modello del sistema reale e lo lega ai nodi che lo spiegano. La sua istanza è il register root `map.md`, una **porta-collezione** aperta on-demand (come `kb.md`) — _non_ la bussola d'ingresso, che è il README, e _non_ un file-ciclo del bootstrap.

Per un LLM la mappa è un dispositivo cognitivo potente: senza, l'agente ricostruisce il territorio da nomi file e link; con una buona mappa capisce subito quali elementi sono centrali, quali fonti verificano i fatti e quali nodi aprire per un intervento.

Esiste **dove il dominio ha un territorio da indicizzare** (host, conti, sistemi, entità). Dove il dominio è astratto non serve: in `metodo` non c'è `map.md`, perché il suo territorio runtime — i progetti adottanti — è indicizzato dall'osservatorio e non da una mappa, mentre il modello vive nei nodi e in `presentations/`.

Distinzione netta da `kb.md`: `kb.md` indicizza i **nodi della KB** (cosa è scritto), `map.md` indicizza il **territorio del dominio** (cos'è il mondo) e lo lega ai nodi. Sono due register diversi, entrambi porte-collezione.

Regole:

- è un register root `map.md`, porta-collezione aperta on-demand; coppia register/concetto con questo nodo `kb/map.md`
- **nome uniforme `map.md`** in tutti i repo che ne hanno bisogno (supera il drift `project-map.md` / `mappa-progetto.md`)
- collega sistema reale, fonti di verità e nodi; non sostituisce il catalogo dei nodi (`kb.md`)
- non diventa storico né lista di task
- può essere diversa per domini tecnici, finanziari o riflessivi
- include lo strato output come dimensione esplicita: dove vivono o1, o2, o3 nel progetto e come il ciclo di azione ritorna alla KB come nuova fonte; senza questa dimensione la mappa descrive solo l'accumulo di conoscenza, non il ciclo completo

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                  | Confronto con il metodo                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `nixos`    | indice host, profili home, macro-aree, fonti Nix e nodi (da uniformare a `map.md` root).            | Esempio forte di indice-territorio code-based: trasforma filesystem e configurazione in modello leggibile.        |
| `bi`       | indice sistemi, flussi dati, script, moduli, fonti tecniche e task strutturali (da uniformare).     | Indice necessario per alta complessità applicativa; riduce la dipendenza da CLAUDE e README.                      |
| `economia` | indice conti, investimenti, immobili, persone, successioni, dati e nodi (da uniformare a `map.md`). | Buon adattamento non-code: rende verificabile il ponte tra entità reali, output dati e KB.                        |
| `salute`   | indice assi concettuali, fonti, pratica, diario e percorsi (da uniformare a `map.md`).              | Conferma che una KB riflessiva ha bisogno di un indice meno tecnico: assi, fonti, pratica, diario invece di host. |

Il confronto mostra che la mappa è il componente più adattabile del metodo: nei repo tecnici indicizza codice e flussi, in `economia` entità e dati, in `salute` assi concettuali e pratica. Due punti ormai fissati: l'istanza vive in **root** come register (`map.md`), porta-collezione on-demand, con nome uniforme; e **non** è la bussola — l'orientamento d'ingresso è il README, che alla mappa _punta_.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [readme](readme.md)
- [indice](indice.md)
- [fonte-di-verita](fonte-di-verita.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [struttura-progetto](struttura-progetto.md)
