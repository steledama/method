---
data: 2026-05-24
stato: bozza
---

# Ciclo di azione

Modello del rapporto tra utente e sistema secondo Donald Norman, distillato come fondamento metodologico per lo strato di output del metodo. Non è la voce biografica di Norman — esiste come nodo di dominio in altri progetti adottanti — ma estrae il pattern che rende un sistema usabile e lo collega al ciclo dell'azione che il metodo deve sostenere.

Il modello sostiene che ogni interazione produttiva con un sistema passa attraverso sette stadi, divisi in due fasi: esecuzione (formare l'intenzione, pianificarla, specificarla, eseguirla) e valutazione (percepire l'esito, interpretarlo, confrontarlo con l'obiettivo). Lungo entrambe le fasi si aprono distanze cognitive — i due gulf — che il design del sistema deve ridurre. Il metodo KB eredita questo modello per progettare lo strato output così che chiuda davvero il ciclo, non solo che lo descriva.

## I tre giganti del metodo

Il metodo si appoggia su tre pilastri che si dividono il lavoro in modo nitido:

| Gigante                     | Cosa ci dà                                                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Luhmann / Zettelkasten      | la disciplina dell'unità atomica — come è fatto il singolo nodo, come si lega ad altri, perché la sintesi non sta nel nodo   |
| Karpathy / LLM KB           | il pattern di manutenzione — chi tiene aggiornato il sistema, come ingest/query/lint, come l'LLM compone la KB               |
| Norman / design dell'azione | l'interfaccia tra KB e mondo — come il sistema rende visibile l'azione possibile, come riceve feedback, come chiude il ciclo |

Karpathy ha risolto il "chi mantiene" del Zettelkasten. Norman risolve il "come l'utente agisce" che né Luhmann né Karpathy affrontano davvero. Luhmann era un produttore solitario di scrittura; Karpathy parla soprattutto di esplorazione e rendering. Nessuno dei due ha pensato esplicitamente al ciclo di azione tra utente e sistema, che è esattamente il problema dello strato L3 e del filing back. Norman entra a colmare questa lacuna.

## I sette stadi del ciclo di azione

Il modello canonico di Norman procede in sequenza:

- Goal — cosa voglio ottenere
- Plan — come penso di ottenerlo
- Specify — quali azioni concrete servono
- Perform — eseguo l'azione nel mondo
- Perceive — vedo l'esito
- Interpret — capisco cosa significa
- Compare — confronto con il goal iniziale

Nel metodo KB il ciclo si materializza sul triplo strato di output ([ponte](ponte.md), L1/L2/L3):

- esecuzione (Goal → Plan → Specify → Perform): KB → L2 → decisione → L3
- valutazione (Perceive → Interpret → Compare): L3 → nuove fonti → KB → L2 aggiornata → confronto con il goal

Esempio concreto, dal pilota di salute. Esecuzione: leggi il quadro corporeo, vedi che il termometro su aneurisma è giallo, decidi di rispettare le raccomandazioni, agisci (cammini, mangi meno). Valutazione: la visita di controllo a novembre 2026 produce un nuovo referto, che diventa nuova fonte, che aggiorna `storia-clinica`, che ridipinge il termometro nel quadro.

## I due gulf

Norman chiama gulf of execution la distanza tra "so cosa voglio" e "so come farlo col sistema"; gulf of evaluation la distanza tra "il sistema mostra X" e "capisco cosa significa per me". Sono i due punti critici dove il design fallisce o riesce.

Nel metodo KB i due gulf si traducono così:

- L1 (output macchina) riduce il gulf of execution per l'LLM che continua il lavoro tra sessioni: trova subito le scadenze, lo stato, i fatti strutturati, senza dover ricostruire il modello da capo
- L2 (output decisione) riduce entrambi i gulf per l'utente umano: termometro, schema, raccomandazioni leggibili in cinque secondi (execution); feedback chiaro che traduce l'esito in significato (evaluation)
- L3 è dove l'azione effettivamente accade — il "perform" del ciclo, fuori dal repo, nel mondo

## Le quattro proprietà cardine come criteri di qualità per L2

Norman riassume il buon design in quattro proprietà. Diventano direttamente criteri di valutazione per lo strato L2 del metodo:

| Norman     | Criterio per L2                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------- |
| Visibilità | tutti gli stati attivi sono percepibili a colpo d'occhio nell'overview, niente di rilevante è nascosto               |
| Feedback   | dopo ogni evento il sistema mostra l'esito in modo evidente; non serve indagine per sapere cosa è cambiato           |
| Mapping    | la disposizione visiva corrisponde alla struttura reale del dominio, non a un ordine convenzionale                   |
| Constraint | la struttura del file impedisce di dimenticare le parti che servono insieme (es. raccomandazioni accanto allo stato) |

Esempio applicato: nel `quadro/quadro-corporeo.md` di `salute` la visibilità è garantita dalla tabella overview che mostra tutte le aree attive con banda e score; il feedback dal fatto che dopo ogni evento il termometro si aggiorna; il mapping dal colore proporzionato alla banda di allarme; la constraint dalla struttura del file area, che costringe a dichiarare prossimi step e raccomandazioni accanto allo stato.

## Norman come critico del metodo

Provocazione utile: Norman guarderebbe il metodo allo stato precedente lo strato output e direbbe — "hai una KB profondissima e nessuna affordance". Il sapere c'era, ma non invitava all'azione. Le scadenze in un file, le raccomandazioni operative sparse nei nodi `kb/`, lo stato dei controlli mescolato alla cronologia in nodi come `storia-clinica.md`, nessun termometro. Il gulf of execution tra "so che dovrei meditare" e "medito stamattina" enorme, e niente nella KB lo riduceva.

È la critica che Norman fa al design "centrato su sé stesso": un oggetto può essere splendido — la KB lo è — ed essere comunque mal progettato dal punto di vista di chi ci agisce dentro. Lo strato output del metodo nasce dal riconoscere questa lacuna.

Una conseguenza forte di questa critica, che resta come principio di valutazione: **se l'utente non agisce, la KB è mal progettata, non l'utente è pigro**. Lo strato output va dunque valutato sui criteri di Norman, non sulla bellezza dei nodi che già esistono.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_ (1988), edizione italiana _La caffettiera del masochista_; in particolare il capitolo sull'action cycle
- Norman, _Emotional Design_ (2004), _Living with Complexity_ (2010)
- Voce biografica e di dominio: `salute/kb/donald-norman.md` nei progetti adottanti

Connessioni:

- [ponte](ponte.md)
- [pattern-karpathy](pattern-karpathy.md)
- [zettelkasten](zettelkasten.md)
- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
