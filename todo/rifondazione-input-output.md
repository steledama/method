---
data: 2026-06-04
stato: aperto
---

# Rifondazione input/output del metodo

Task rifondativo: introduce la simmetria input/output come struttura portante del metodo,
completa l'analogia con Norman, e aggiorna tutta la nomenclatura conseguente.

## Motivazione

Il metodo ha sviluppato finora solo il lato esecuzione del ciclo di Norman: la KB produce
output strutturati (L1/L2/L3) che sfociano in azione nel mondo. Il lato valutazione — come
il mondo ritorna nella KB — era descritto ma non formalizzato in strati simmetrici.

Tre problemi concreti:

1. **"Ponte"** è una metafora che richiede spiegazione. "Output" è autoesplicativo, si
   accoppia naturalmente con "input" e non perde nulla del significato originale.

2. **L1/L2/L3** è nomenclatura arbitraria. Con i due lati del ciclo esplicitati, la
   simmetria **o1/o2/o3** (output) e **i1/i2/i3** (input) rende evidente la struttura
   bidirezionale senza aggiungere concetti nuovi.

3. **L'analogia con Norman era parziale.** Norman descrive esattamente due archi
   complementari: Gulf of Execution (da goal ad azione nel mondo) e Gulf of Evaluation
   (da percezione del mondo a valutazione). Il metodo usava Norman solo per criticare
   il design dello strato output, non per fondare la struttura intera. La revisione
   chiude questa asimmetria.

## Base empirica: il pattern di input esiste già nei repo adottanti

La formalizzazione in i1/i2/i3 non è introdotta per simmetria teorica: il problema
dell'organizzazione degli ingest è emerso dall'uso reale, in particolare in `economia`
e `salute`, i due repo con le fonti esterne più dense e eterogenee.

| Progetto   | Esempi concreti di input già incontrati                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------- |
| `economia` | estratti conto, documenti notarili, polizze, comunicazioni del commercialista, delibere condominiali                 |
| `salute`   | referti medici, cartelle cliniche, esami del sangue, relazioni specialistiche                                        |
| `nixos`    | messaggi di errore o alert di sistema, nuove esigenze hardware/software, attese anomale nei rebuild, deprecation notice |
| `bi`       | segnalazioni dei colleghi (a voce o per email), errori nei dati, inefficienze nei processi, richieste di nuove analisi |

Il pattern ricorrente in tutti e quattro: arriva un segnale esterno grezzo (i1) che
richiede elaborazione (i2) prima di poter diventare conoscenza stabile nella KB (i3)
o aprire un task. Finora questo percorso era implicito e non governato — ogni repo
lo gestiva in modo diverso e spesso non lo gestiva affatto.

La formalizzazione è dunque bottom-up: nomina e struttura qualcosa che esiste già,
non impone un modello calato dall'alto.

## Analogia completa con Norman

Il ciclo di Norman a sette stadi si divide in due archi che corrispondono punto per punto
ai due lati del metodo:

**Arco di esecuzione → strati output**

| Norman                  | Metodo                                              |
| ----------------------- | --------------------------------------------------- |
| Goal                    | lettura della KB, decisione formata                 |
| Plan + Specify          | o2 — vista, schema, slide, raccomandazione leggibile |
| Perform                 | o3 — email, parole, transazione, gesto              |

**Arco di valutazione → strati input**

| Norman                  | Metodo                                              |
| ----------------------- | --------------------------------------------------- |
| Perceive                | i1 — segnale grezzo: referto, log, export, documento |
| Interpret               | i2 — elaborazione: sintesi, analisi, nota distillata |
| Compare (→ nuovo Goal)  | i3 — conoscenza formalizzata: nodo KB, fonte di verità |

Il ciclo si chiude quando o3 (azione nel mondo) genera nuovi i1 (segnali grezzi), che
attraverso i2 diventano i3, che alimentano la prossima esecuzione. Questo è esattamente
il "filing back" di Karpathy, ora fondato strutturalmente e non solo descritto.

**Conseguenza importante**: i due gulf di Norman mappano direttamente sui due lati:
- Gulf of Execution = distanza tra i3 (sapere nella KB) e o3 (azione nel mondo) → ridotto
  da o2 che rende il sapere azionabile
- Gulf of Evaluation = distanza tra i1 (segnale grezzo) e i3 (comprensione formalizzata) →
  ridotto da i2 che interpreta e filtra

## Formulazione fondativa: i tre giganti rispetto alla KB

I tre giganti non sono equivalenti rispetto alla KB — ognuno abita un livello diverso
del metodo:

- **Luhmann è la KB** — il Zettelkasten *è* una KB; nodi atomici, atomicità, struttura emergente
- **Karpathy governa la KB** — ingest, query, lint, filing back; il processo che la mantiene viva
- **Norman connette la KB al mondo** — il ciclo di azione tra conoscenza e azione, tra mondo e conoscenza

Questa formulazione è più precisa dell'attuale "si dividono il lavoro in modo nitido":
è vera ma non dice *dove* ognuno lavora rispetto alla KB. La nuova formulazione chiarisce
anche perché Norman è il gigante che giustifica sia lo strato output (esecuzione) sia lo
strato input (valutazione) — è l'unico dei tre che guarda fuori dalla KB verso il mondo.

Da usare come apertura del nodo sui tre giganti durante la riscrittura.

## Chiave di lettura possibile: il metodo come estensione di Norman

Norman dà per scontati due elementi ai confini del suo ciclo: il **Goal** (che motiva
l'azione) e il **Mondo** (che risponde all'azione). I sette stadi vivono in mezzo — ma
né l'origine del Goal né la natura del Mondo vengono spiegati. Sono i confini del modello,
non il suo contenuto.

Il metodo potrebbe essere letto come un'estensione di Norman verso i suoi due estremi
irrisolti:

- **Sul Goal**: la KB non è solo uno strumento per eseguire meglio — è il luogo dove i
  goal si formano, si raffinano, si mettono in discussione. Norman dà il Goal come input
  del ciclo; il metodo mostra come si costruisce attraverso la conoscenza accumulata.

- **Sul Mondo**: lo strato input (i1/i2/i3) governa come il mondo entra nel sistema —
  non subire passivamente i segnali grezzi ma avere un processo per trasformarli in
  conoscenza. Norman tratta il Mondo come una scatola nera che risponde; il metodo lo
  apre.

In questa lettura il metodo non è un'applicazione di Norman ma un'**estensione** verso
i suoi due estremi lasciati aperti: cosa c'è prima del Goal, e cosa c'è dopo il Mondo.

Questa chiave di lettura è aperta: va verificata durante la riscrittura dei nodi e
potrebbe rivelarsi una forzatura oppure il contributo concettuale più originale del
metodo rispetto alle sue fonti.

## Nota terminologica: "KB" come sineddoche del metodo

Nel task e nei nodi esistenti "KB" viene spesso usata come sineddoche del metodo intero
— la parte per il tutto. La KB in senso stretto è solo i nodi in `kb/`: la conoscenza
accumulata e formalizzata. Il metodo comprende anche la struttura di progetto, il ciclo
operativo, gli strati input/output, gli strumenti, le regole d'azione.

La sineddoche è comoda e in parte giustificata — la KB è il nucleo identitario del
sistema e dà il nome al metodo. Ma crea ambiguità reale: "la KB governa il Goal" e
"il metodo governa il Goal" dicono cose diverse, e la differenza conta specialmente
nella chiave di lettura normaniana.

Durante la riscrittura dei nodi in inglese vale la pena usare "the method" quando si
intende il sistema intero, e "the KB" solo quando si intende specificamente i nodi
di conoscenza. Non una correzione meccanica a posteriori — una consapevolezza da
mantenere mentre si scrive.

## Fuori scope: lo scorporo concettuale (2026-06-05)

Le sessioni 04-06 e 05-06 hanno alzato la quota oltre la rinomina i/o. Per non gonfiare
questo task — che resta focalizzato sulla *struttura input/output* — i concetti di quota
superiore si scorporano in un task dedicato (`todo/artefatto-cognitivo.md`): tripartizione
artefatto cognitivo / sistema cognitivo / metodo, ciclo d'azione a *due agenti* (umano + LLM
che condividono il system image), gerarchia del Goal (motivo → goal → operazione), stack
L0/L1/L2. Sono un asse diverso — *cosa è* l'oggetto — dal *come funziona* la struttura i/o.

Cerniera: `ciclo-azione` è toccato da entrambi i task (qui per la conversione L→o/i, là per
la riscrittura a due agenti). Coordinare: le due modifiche al nodo vanno fatte nella stessa
passata, non in due sweep separati.

Già fatto in questa sessione (in nomenclatura `L`, in attesa di conversione i/o):
`ciclo-azione` ha la sezione "Cicli annidati" e l'affinamento o1/o2 (stesso Plan/Specify, due
consumatori); `fedelta-cognitiva` ha il check "Decisioni e assunzioni". La conversione L→o/i
li spazza insieme al resto.

## Scope delle modifiche

### 1. Rinominare `kb/ponte.md` → `kb/output.md`

Contenuto da riscrivere quasi integralmente:
- Titolo: "Output" (non "Ponte")
- Sezione "risoluzione conflitto Zettelkasten/Karpathy": invariata nel contenuto, aggiornare
  il termine "strato ponte" → "strato output"
- Sezione "tre livelli": rinominare L1/L2/L3 → o1/o2/o3 nelle intestazioni e nel testo
- Aggiungere sezione "strato input" con i1/i2/i3 come specchio simmetrico
- Aggiornare la tabella "dichiarazione minima" per includere entrambi i lati
- Aggiornare connessioni: `[ciclo-azione](ciclo-azione.md)` resta, rimuovere
  autoriflessioni sul nome "ponte"

### 2. Aggiornare `kb/ciclo-azione.md`

- Sezione "I sette stadi": aggiornare la mappatura esecuzione/valutazione con la nuova
  nomenclatura o1/o2/o3 e i1/i2/i3
- Sezione "I due gulf": esplicitare che Gulf of Execution = output side, Gulf of Evaluation
  = input side
- Aggiungere tabella sinottica completa del ciclo bidirezionale
- Aggiornare l'esempio di `salute` con la nomenclatura nuova

### 3. Aggiornare `kb/metodo-kb.md`

- Sostituire tutti i riferimenti a "ponte", "strato ponte", "L1/L2/L3" con la nuova
  nomenclatura
- Aggiungere strato input nella ricetta metodologica, se già presente come concetto
  implicito ("filing back", "fonti")

### 4. Aggiornare `kb/struttura-progetto.md`

- Sostituire "strato output (ponte)" con "strato output" ovunque
- Aggiungere strato input come componente della struttura di progetto (opzionale o
  obbligatorio? da decidere durante l'implementazione)

### 5. Aggiornare `presentazione/metodo-in-sintesi.md`

I cinque diagrammi mermaid vanno aggiornati:
- Diagramma "ciclo che si chiude": aggiungere strato input con i1/i2/i3 come ramo
  simmetrico, e aggiornare L1/L2/L3 → o1/o2/o3
- Diagramma "dove vive cosa": aggiornare "strato output (ponte)" → "strato output"
- Diagramma "anatomia di un progetto": aggiornare "strato output (ponte)" → "strato output"
- Rigenarare il PDF dopo le modifiche

### 6. Aggiornare `README.md`

- Sezione "Funzioni del repo": "strato output (ponte)" → "strato output"
- Sezione "Nodi": entry di `ponte` → rinominare in `output`, aggiornare descrizione
- Aggiornare il riferimento `[ponte](kb/ponte.md)` con `[output](kb/output.md)`

### 7. Aggiornare tutti i nodi che linkano `ponte.md`

Fare un grep per `ponte.md` e `\bponte\b` in tutta la `kb/` e aggiornare i link nelle
sezioni Connessioni. Candidati: `ciclo-azione.md`, `metodo-kb.md`, `struttura-progetto.md`,
`knowledge-base.md`, `confronto-progetti-adottanti.md`.

### 8. Propagazione ai progetti adottanti

I progetti adottanti leggono i nodi via symlink: vedono automaticamente tutte le
modifiche ai nodi. Non è necessario aggiornamento manuale dei contenuti.

Tuttavia verificare se qualche progetto adottante:
- ha un nodo locale che linka `metodo/ponte.md` per nome — aggiornare il link
- usa esplicitamente la terminologia "L1/L2/L3" o "strato ponte" nei propri nodi locali
  — segnalare ma non imporre il cambio (è scelta locale)

Progetti adottanti: `nixos`, `bi`, `economia`, `salute`.

## Decisioni risolte (2026-06-05)

1. **Nomenclatura dei due lati → `input/output` (+ sigle `i1..i3` / `o1..o3`).**
   Scartata `esecuzione/valutazione` benché fedele a Norman. Ragioni: le sigle i/o derivano
   dalle iniziali e sono *sistematiche* (due regole, sei sigle derivabili), mentre i
   nomi-stadio di Norman vanno memorizzati uno a uno; in inglese *execution* ed *evaluation*
   collidono sulla `e`; e la circolarità del ciclo (Norman è opportunistico — può partire dal
   goal o dallo stimolo/affordance) toglie ogni "ordine corretto", lasciando intatto solo il
   significato *direzionale* di input/output (dentro/fuori dal sistema), invariante rispetto
   al punto d'innesco. I nomi-stadio di Norman (perceive/interpret/compare,
   plan/specify/perform) **non** diventano etichette degli strati — sono atti cognitivi, gli
   strati sono artefatti (il referto non "percepisce", è il percepito): entrano come *glossa*
   d'insegnamento accanto alla sigla, non al suo posto.

2. **Lingua → inglese.** Tradurre con cura nodo per nodo durante la riscrittura, mai
   meccanicamente a posteriori (la profondità concettuale è stata costruita in italiano).
   Motivazioni: repo pubblico; l'inglese è già la lingua del dominio tecnico (git, KB, LLM,
   frontmatter); fedeltà alle fonti (i tre giganti vivono nell'accademia anglofona).
   Conseguenza operativa: usare "the method" per il sistema intero e "the KB" solo per i nodi
   di conoscenza (cfr. nota sulla sineddoche).

## Decisioni ancora aperte

1. **Dove vivono le fonti grezze (i1) nel repo?** — *decisione cardine, da sciogliere col
   dogfooding, non a scrivania.* Il repo non ha `fonti/`. Posare *un* i1 reale (il segnale
   `bi`/1018022 o un estratto di Norman, cfr. `ingest-norman`) e farlo passare per i1→i2→i3
   prima di scrivere la sezione "strato input" di `output.md`. Bottom-up.

2. **Strato input obbligatorio o opzionale nella struttura di progetto?** Alcuni progetti
   hanno fonti grezze dense (economia, salute), altri quasi solo input intenzionale (nixos).
   Propensione: dichiarazione obbligatoria, anche se i1 è vuoto o implicito.

3. **Nomi locali per i1/i2/i3?** Come per l'output (`salute` chiama l'output "quadro/"): la
   struttura usa i1/i2/i3, i nomi locali sono liberi.

4. **Dove dichiarare lo strato input nei progetti adottanti?** Mappa, README, file dedicato?
   La dichiarazione minima di `ponte.md` riguardava l'output; va estesa simmetricamente.

## Sequenza suggerita

**Prima dello sweep** (deciso 2026-06-05): (a) questo consolidamento del task; (b) dogfood di
*un* i1 reale per fissare la struttura fisica dell'input (decisione aperta #1). Solo dopo:

1. Creare `kb/output.md` con il nuovo contenuto (non rinominare subito `ponte.md` —
   scrivere prima il nodo nuovo, poi eliminare il vecchio)
2. Aggiornare `kb/ciclo-azione.md` con la mappatura completa
3. Aggiornare `kb/metodo-kb.md` e `kb/struttura-progetto.md`
4. Aggiornare connessioni in tutti i nodi che linkano `ponte.md`
5. Eliminare `kb/ponte.md`
6. Aggiornare `README.md`
7. Aggiornare `presentazione/metodo-in-sintesi.md` e rigenerare il PDF
8. Verificare grep residui di "ponte" e "L1/L2/L3" nell'intero repo
9. Segnalare ai progetti adottanti (opzionale, via log o commit message)

## Connessioni

- [ponte](../kb/ponte.md)
- [ciclo-azione](../kb/ciclo-azione.md)
- [metodo-kb](../kb/metodo-kb.md)
- [struttura-progetto](../kb/struttura-progetto.md)
