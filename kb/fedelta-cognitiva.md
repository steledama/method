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

| Livello     | Domanda                                              | Esempi                                               |
| ----------- | ---------------------------------------------------- | ---------------------------------------------------- |
| strutturale | la KB è integra?                                     | link, orfani, README, frontmatter                    |
| fattuale    | la KB concorda con le fonti di verità del dominio?   | dipende dal dominio — vedi sezione Adattamento       |
| semantico   | la KB è ancora una buona interfaccia cognitiva?      | funzione dei nodi, router, confini                   |

## Checklist semantica

### Funzione documentale

- ogni nodo importante ha ancora una funzione dominante chiara?
- mappa, reference e runbook sono rimasti separati?

### Presente vs storia

- la KB permanente descrive ancora il presente?
- workaround, migrazioni o casi storici appartengono ormai a Git o `log.md`?

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

Connessioni:

- [metodo-kb](metodo-kb.md)
- [knowledge-base](knowledge-base.md)
- [nodo](nodo.md)
- [strumenti-kb](strumenti-kb.md)
- [fonte-di-verita](fonte-di-verita.md)
- [mappa](mappa.md)
