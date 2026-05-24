---
data: 2026-05-24
stato: bozza
---

# Ponte

Lo strato di output del metodo: il livello che traduce la conoscenza accumulata nella KB in azione possibile nel mondo. È distinto dalla KB perché ospita sintesi, viste, dashboard — tutto ciò che il purismo zettelkastiano vieta dentro al nodo atomico e che il pattern Karpathy chiede di produrre. Il nome riprende la sua funzione: collegare due rive — la teoria accumulata e la pratica nel mondo — che senza di lui restano separate.

Lo strato output esiste perché il KB possa restare puro. È la sua condizione di possibilità, non un'aggiunta opzionale. Senza, la pressione di sintesi finisce dentro ai nodi (caso paradigmatico: `salute/kb/storia-clinica.md`, diventato di fatto un mini-dashboard improprio), violando l'atomicità che è il principio fondante dello Zettelkasten.

## La risoluzione del conflitto Zettelkasten/Karpathy

Il metodo si appoggia su due pilastri storici con una tensione mai nominata. Lo Zettelkasten storico — Luhmann ha scritto 70 libri e 400 articoli usando le sue carte come motore di scrittura — non nega l'output, ma lo colloca _fuori_ dall'archivio. Le carte sono atomiche, una idea per carta. Non ci sono carte di sintesi né viste d'insieme. La sintesi accade quando scrivi il libro, fuori dal Zettelkasten.

Karpathy, al contrario, mette la sintesi _dentro_ al wiki. Il suo pattern include esplicitamente summary pages, entity pages, concept pages, comparisons — mantenute dall'LLM. Il wiki contiene sia atomi che aggregati, perché la manutenzione è automatica e a basso costo.

Le due posizioni collidono se si pretende di averle entrambe nello stesso spazio. La risoluzione del metodo è strutturale: il KB resta zettelkastiano puro, lo strato ponte ospita le sintesi karpathiane. La sintesi acquista un posto legittimo che non viola l'atomicità dei nodi.

## I tre livelli dell'output

L'output universale del metodo ha tre livelli, distinti per audience, forma e collocazione:

| Livello               | Audience                      | Forma                                            | Dove vive                 |
| --------------------- | ----------------------------- | ------------------------------------------------ | ------------------------- |
| L1 — output macchina  | LLM, sistema, automazione     | JSON, dati strutturati, `.nix` compilato         | nel repo                  |
| L2 — output decisione | umano (utente, collaboratori) | schemi, diagrammi, slides, termometri            | nel repo                  |
| L3 — output azione    | mondo                         | email, parole dette, transazioni, gesti corporei | fuori dal repo, nel mondo |

Tre osservazioni importanti.

L3 è dove l'output produce effetti reali. Tutto il resto è strumentale. Le email che mandi spostano davvero i soldi, le parole dette al medico cambiano davvero il percorso clinico, il gesto dello yoga cambia davvero il corpo.

L3 ritorna come fonte. Le email diventano paper trail, le visite diventano referti, lo yoga diventa diario. Il ciclo si chiude e la KB cresce. Questa è la generalizzazione del "filing back" di Karpathy: non solo le query buone tornano nella KB, ma l'azione nel mondo produce nuove fonti che il sistema integra.

L1 e L2 hanno funzioni diverse e dovrebbero essere distinguibili. L1 è ottimizzato per l'LLM che continua il lavoro tra sessioni; L2 per l'utente umano che decide o condivide. Confonderli è una trappola: un JSON denso è inutile per la decisione umana, un'infografica colorata è inefficiente per l'LLM.

## Il ciclo che si chiude attraverso l'azione

C'è una cosa che il metodo non aveva mai detto esplicitamente: la KB è strumentale all'azione, non è il fine. Le carte di Luhmann erano strumentali alla scrittura; il nostro KB è strumentale a decidere e agire bene nel mondo.

Il loop teoria → pratica → osservazione → revisione del nodo locale `salute/kb/verifica-nel-vivere` diventa la formalizzazione universale del ciclo: ogni progetto adottante chiude L3 con il ritorno delle fonti, anche quando il dominio è tecnico (`nixos`) o finanziario (`economia`).

## Stato dei progetti adottanti

Ogni progetto adottante ha già implementato uno strato output, anche senza nominarlo. La promozione a componente universale del metodo (sessione 2026-05-24) registra solo quello che esiste già:

| Progetto   | L1                                                          | L2                                                         | L3                                                                  |
| ---------- | ----------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| `nixos`    | `.nix` in `home/`, `hosts/`, `modules/` (forte)             | testo descrittivo in `kb/` (debole, no diagrammi)          | sistema in esecuzione, deploy, switch (forte)                       |
| `bi`       | scripts notturni (forte)                                    | `presentazione/` Reveal.js (forte)                         | decisioni business, riunioni (forte)                                |
| `economia` | `output/json/` (forte)                                      | `output/report*.md` tabelle (medio)                        | email amministratori, riunioni famigliari (forte)                   |
| `salute`   | implicito sparso (scadenze, cronologia in `storia-clinica`) | `quadro/` con termometro e file per area (pilota in bozza) | yoga, controlli, alimentazione, conversazioni mediche (medio-forte) |

Pattern emergente: dove L2 è forte, il progetto serve decisioni condivise con altri (`bi`); dove L2 è debole, la KB resta personale e introspettiva, e fatica a generare azione coordinata.

## Dichiarazione minima dello strato output

Ogni progetto adottante dovrebbe dichiarare esplicitamente il proprio strato output nella mappa o nel README locale. La dichiarazione minima non impone una directory uguale per tutti, ma rende verificabile il circuito:

```markdown
## Strato output

- L1 macchina:
- L2 decisione:
- L3 azione:
- Fonte di ritorno:
- Criterio di aggiornamento:
```

La dichiarazione serve a evitare l'ambiguità più comune: chiamare output una sintesi che non produce azione. L1 e L2 sono output intermedi; lo strato è completo solo se dichiara come L3 produce una fonte di ritorno e come quella fonte aggiorna KB, task, scadenze o nuove viste.

## Forma locale, funzione universale

Il nome dello strato resta locale e segue il dominio:

- `salute` lo chiama `quadro/` — vista clinica corporea
- `bi` lo ha già come `presentazione/` — slide deck per stakeholder
- `economia` lo ha già come `output/` — report json e markdown
- `nixos` lo ha già come `home/`, `hosts/`, `modules/` — l'output è la configurazione stessa che gira sul sistema

La funzione è la stessa: tradurre conoscenza in azione possibile. Il nome locale è scelta di dominio, non drift dal metodo. Ogni progetto adottante dichiara esplicitamente la sua forma per L1, L2, L3; livelli assenti vanno nominati come assenti, non lasciati impliciti.

## Segnale di maturità

Uno strato output maturo lascia traccia di cicli completi: L2 rende visibile una decisione, L3 produce un'azione nel mondo, l'azione genera una fonte e la fonte ritorna nella KB o nel quadro operativo. Il criterio empirico minimo per validare un pilota è osservare almeno 2-3 cicli completi, non soltanto la presenza di file ben formattati.

## Criteri di qualità

Lo strato ponte va valutato sui criteri di Norman descritti in [ciclo-azione](ciclo-azione.md): visibilità, feedback, mapping, constraint. La bellezza dei nodi della KB non basta. Se l'utente non agisce, il ponte è mal progettato.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [pattern-karpathy](pattern-karpathy.md)
- [zettelkasten](zettelkasten.md)
- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [struttura-progetto](struttura-progetto.md)
