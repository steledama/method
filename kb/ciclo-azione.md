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

Nel metodo KB il ciclo si materializza sul triplo strato di output: ponte, L1/L2/L3.

- esecuzione (Goal → Plan → Specify → Perform): KB → L2 → decisione → L3
- valutazione (Perceive → Interpret → Compare): L3 → nuove fonti → KB → L2 aggiornata → confronto con il goal

Plan e Specify si materializzano in due strati distinti non per due stadi diversi di Norman, ma per due *consumatori* diversi: L1 è la versione macchina (fatti strutturati per l'LLM che continua il lavoro tra sessioni), L2 la versione umana (vista leggibile per la decisione). Non sono due punti del ciclo — sono lo stesso Plan/Specify rivolto ai due agenti che lo portano avanti.

Esempio concreto, dal pilota di salute. Esecuzione: leggi il quadro corporeo, vedi che il termometro su aneurisma è giallo, decidi di rispettare le raccomandazioni, agisci (cammini, mangi meno). Valutazione: la visita di controllo a novembre 2026 produce un nuovo referto, che diventa nuova fonte, che aggiorna `storia-clinica`, che ridipinge il termometro nel quadro.

## I due gulf

Norman chiama gulf of execution la distanza tra "so cosa voglio" e "so come farlo col sistema"; gulf of evaluation la distanza tra "il sistema mostra X" e "capisco cosa significa per me". Sono i due punti critici dove il design fallisce o riesce.

Nel metodo KB i due gulf si traducono così:

- L1 (output macchina) riduce il gulf of execution per l'LLM che continua il lavoro tra sessioni: trova subito le scadenze, lo stato, i fatti strutturati, senza dover ricostruire il modello da capo
- L2 (output decisione) riduce entrambi i gulf per l'utente umano: termometro, schema, raccomandazioni leggibili in cinque secondi (execution); feedback chiaro che traduce l'esito in significato (evaluation)
- L3 è dove l'azione effettivamente accade — il "perform" del ciclo, fuori dal repo, nel mondo

## Cicli annidati: i progetti code-based

Nei progetti basati su codice il ciclo d'azione non è uno solo: ce ne sono due, annidati. Norman descrive un utente che agisce su un artefatto e ne valuta la risposta; ma quando l'artefatto è un sistema software, l'artefatto stesso è il prodotto di un ciclo d'azione precedente.

- **Ciclo di sviluppo**: Goal (serve una capacità) → Plan/Specify (il `todo`, dettagliato) → Perform (il commit). Il suo "mondo" è il codebase; il suo L3 — l'azione nel mondo — *è il codice*.
- **Ciclo runtime**: il codice, eseguito, compie il proprio ciclo. Legge le fonti e produce L1 (artefatto macchina), L2 (vista di decisione), L3 (azione nel mondo reale: un'email, una transazione, un payload pubblicato).

Il codice è insieme il L3 del ciclo di sviluppo e la macchina che esegue il ciclo runtime. Per questo risalire da un output runtime al task che l'ha generato — `output → codice → commit → todo → goal` — non è debug ma attraversamento dell'annidamento: `git-history`, `log` e `todo` sono le fonti di verità che registrano il ciclo di sviluppo di cui ogni artefatto runtime è un fossile.

È il senso in cui il metodo *estende* Norman invece di applicarlo soltanto: Norman dà il Mondo come scatola nera che risponde all'azione; in un progetto code-based il Mondo-che-risponde è a sua volta un artefatto progettato, con una provenienza. Il metodo apre la scatola — ogni sistema è il L3 di un ciclo che lo precede.

**Dove si rompe.** Il guasto più insidioso non vive nel ciclo runtime ma nel gulf of evaluation del ciclo di sviluppo: una decisione viene eseguita (il commit parte, gulf of execution attraversato) ma la sua *assunzione* non viene formalizzata e ri-valutata. Quando il significato dei dati su cui poggiava cambia, niente costringe a riaprirla, e l'assunzione stale si materializza mesi dopo come comportamento errato nel mondo. Nel caso `bi`/1018022 un commit di compatibilità ripristinò un comportamento storico ("presente nei backorders ⇒ esiste un fornitore esterno") dopo che il modello dati aveva cambiato significato — la sorgente interna magazzino era entrata nei backorders. La decisione visse nel messaggio di commit, non in `log.md`: il gulf of execution fu attraversato, quello di evaluation no, e l'assunzione esplose come oversell quando un cliente comprò due pezzi contro una giacenza di uno. Il presidio di questo guasto è un check di fedeltà cognitiva (vedi [fedelta-cognitiva](fedelta-cognitiva.md)).

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

- [affordance-signifier](affordance-signifier.md)
- [system-image](system-image.md)
- [visceral-behavioral-reflective](visceral-behavioral-reflective.md)
- [ponte](ponte.md)
- [pattern-karpathy](pattern-karpathy.md)
- [zettelkasten](zettelkasten.md)
- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
