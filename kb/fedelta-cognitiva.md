---
data: 2026-05-16
stato: maturo
---

# Fedeltà cognitiva

La fedeltà cognitiva è la capacità di una knowledge base di restare non solo
formalmente sana, ma anche aderente al sistema reale e facile da ricostruire per
un umano o un LLM. Una KB può avere tutti i link validi e tuttavia essere poco
fedele se conserva storia superata, esempi non più canonici o punti di accesso
che non riflettono più la forma attuale del progetto.

La verifica della fedeltà cognitiva combina tre livelli. Il lint strutturale
controlla la topologia della rete. I controlli anti-drift confrontano pochi fatti
documentati con fonti primarie affidabili. La revisione semantica guidata valuta
ciò che gli script possono solo portare all'attenzione: funzione dei nodi,
chiarezza dei router, rapporto tra presente e storia, nuove frontiere emerse nel
dominio.

## Tre livelli di verifica

| Livello     | Domanda                                            | Esempi                                         |
| ----------- | -------------------------------------------------- | ---------------------------------------------- |
| strutturale | la KB è integra?                                   | link, orfani, README, frontmatter              |
| fattuale    | la KB concorda con le fonti di verità del dominio? | dipende dal dominio — vedi sezione Adattamento |
| semantico   | la KB è ancora una buona interfaccia cognitiva?    | funzione dei nodi, router, confini             |

## Checklist semantica

### Router e punti di ingresso

- un audit strutturale pulito sta nascondendo un README cognitivamente sbagliato?
- README, CLAUDE e mappa descrivono ancora funzioni distinte o si stanno
  duplicando?
- i contenuti condivisi tra progetti sono referenziati come dipendenze
  trans-repo, invece di essere indicizzati come KB locale?

### Funzione documentale

- ogni nodo importante ha ancora una funzione dominante chiara?
- mappa, reference e runbook sono rimasti separati?

### Presente vs storia

- la KB permanente descrive ancora il presente?
- workaround, migrazioni o casi storici appartengono ormai a Git o `why.md`?

### Decisioni e assunzioni

- una decisione che preserva un comportamento storico ("manteniamo il vecchio
  comportamento") registra in `why.md` *su quale assunzione* poggia, non solo
  *cosa* preserva?
- l'assunzione è ancora vera, o il significato dei dati sotto di essa è cambiato
  dall'ultima volta?
- esistono decisioni che vivono solo nel messaggio di commit, prive di un
  appiglio in `why.md` per essere ri-valutate quando il modello evolve?

Una decisione registrata solo nel commit è un'azione nel mondo (`L3`) senza il
ritorno che la rende ri-valutabile: il *gulf of evaluation del ciclo di
sviluppo* (vedi [ciclo-azione](ciclo-azione.md)) resta non attraversato. Il
commit dice "ho preservato X"; il why deve dire "X presuppone Y; se Y cambia,
riaprire" — perché è l'assunzione, non il comportamento, che va ri-controllata
quando il modello dati evolve. Caso reale: `bi`/1018022, dove il ripristino di un
backorder "storico" su prodotti a solo magazzino, dopo che la semantica dei dati
era cambiata, ha prodotto un oversell mesi dopo; l'assunzione viveva nel commit,
non nel why.

### Accessibilità cognitiva

- README permette ancora a un nuovo LLM di entrare dal punto giusto?
- la mappa canonica del progetto consente ancora di ricostruire il sistema reale dall'alto?
- gli intenti operativi principali hanno un router leggibile?

### Aderenza al dominio

- gli esempi documentali derivano ancora da elementi vivi nel progetto?
- sono emersi pattern ricorrenti non ancora rappresentati?
- esistono nodi che parlano di componenti, situazioni o entità non più attive?

### Confini futuri

- sono emersi assi operativi distinti che oggi convivono ma potrebbero divergere
  domani?
- un nodo è ancora semanticamente uno, o lo è solo per inerzia storica?

## Metriche minime

- entità principali del progetto documentate nei punti canonici;
- nessun nodo che descrive elementi rimossi o non più attivi;
- fatti ad alta deriva monitorati contro fonti di verità chiare;
- aree principali collegate a fonti di verità e nodi di approfondimento;
- router del README ancora coerente con gli intenti principali;
- ultima revisione qualitativa significativa registrata nel tempo.

## Adattamento al dominio

Il livello fattuale varia per dominio. Ogni progetto deve definire esplicitamente
le proprie fonti di verità e i propri fatti ad alta deriva prima di attivare
controlli anti-drift.

- **progetti code-based** (es. nixos, bi): il codice sorgente e il filesystem sono
  le fonti primarie; si verificano entità dichiarate nella configurazione (host,
  profili, moduli, script) rispetto a ciò che esiste realmente
- **progetti finanziari o legali** (es. economia): output strutturati e documenti
  autoritativi sono le fonti; si verificano situazioni aperte/chiuse, importi,
  scadenze, accordi — il rischio di drift non è "il codice è cambiato, la
  documentazione no?" ma "la situazione è evoluta, il nodo no?"
- **ogni nuovo dominio**: identificare prima i fatti che cambiano più spesso
  (alta deriva) e le fonti che li rendono verificabili; non estendere i controlli
  oltre ciò che ha una fonte primaria leggibile

## Fonti di verità per i fact check

I fact check automatici devono confrontare documentazione contro fonti primarie
(filesystem, codice, output strutturati, documenti autoritativi), mai contro
altra documentazione. Testare "il numero scritto in un file di istruzioni" contro
"il conteggio reale degli elementi nel codice" è formalmente un check, ma
trasforma il file di istruzioni in una fonte di verità accidentale che va
mantenuta manualmente e si presta a drift. La fonte di verità deve essere unica:
il filesystem, l'output di un manifest dichiarativo, il contenuto di un file di
configurazione o di un documento autorevole.

Quando un fatto strutturale risulta verificabile solo via documentazione, è un
segnale che manca una fonte primaria leggibile, non che la documentazione vada
validata contro se stessa. La soluzione corretta è esporre il fatto come dato
derivato dalla fonte (un conteggio, un inventario, un check di esistenza), non
inserirlo come stringa nella documentazione operativa.

## Limite intenzionale

La fedeltà cognitiva non deve diventare un test fittizio. Gli script verificano
ciò che il dominio rende verificabile; i warning indirizzano l'attenzione; umano e
LLM decidono se un nodo vada rifatto, diviso o lasciato invariato.

Un caso tipico: l'audit può dire 0 errori e 0 avvisi mentre il README resta
cognitivamente infedele, perché indicizza contenuti metodologici condivisi come
se fossero parte della KB locale. Il controllo corretto non è solo "i link
funzionano?", ma "questo punto di ingresso ricostruisce ancora il modello reale
del progetto?". In questi casi lo script può intercettare regressioni note, ma la
skill deve sempre includere una revisione qualitativa di README, CLAUDE e mappa.

## Applicazione nei progetti adottanti

| Progetto   | Situazione attuale                                                                                                                            | Confronto con il metodo                                                                                                                                          |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nixos`    | Implementa il ciclo più completo: inventario da `flake.nix` e filesystem, facts, coverage e fidelity.                                         | Aderenza alta: il dominio dichiarativo consente controlli automatici affidabili senza inventare fonti fittizie.                                                  |
| `bi`       | Ha audit strutturale maturo e una copertura script-nodi; la mappa dichiara che il livello fattuale va ancora progettato su fonti BI primarie. | Caso intermedio: la complessità applicativa richiede selezionare pochi fatti ad alta fiducia prima di automatizzare fidelity.                                    |
| `economia` | Usa facts sulla mappa e fonti JSON/documentali; ha introdotto un controllo README contro il drift del metodo trans-repo.                      | Buon adattamento finanziario-legale: la fedeltà riguarda situazioni aperte, importi, scadenze e documenti, ma anche la coerenza dei punti di ingresso.           |
| `salute`   | Strutturalmente sana; la fedeltà è soprattutto semantica e interpretativa, legata a fonti, diario, pratica e coerenza dei concetti.           | Mostra il limite dei fact check: in una KB riflessiva la revisione qualitativa può essere formalizzata come loop teoria -> pratica -> osservazione -> revisione. |

Il confronto tra teoria e pratica suggerisce una regola più precisa: attivare automatismi di fedeltà solo dove esiste una fonte primaria leggibile e stabile. Dove la fonte è interpretativa o personale, il metodo deve fornire checklist e filing back, non simulare test oggettivi.

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [nodo](nodo.md)
- [strumenti-kb](strumenti-kb.md)
- [fonte-di-verita](fonte-di-verita.md)
- [map](map.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [ciclo-azione](ciclo-azione.md)
