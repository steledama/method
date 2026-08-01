---
description: Il braccio di esecuzione del ciclo — exec [plan|specify|perform|all] — coda e priorità del plan, qualità interna dei task o2, supervisione della collezione o3 e atti coperti da autorizzazione
user-invocable: true
---

Compi il braccio di esecuzione del ciclo, nell'ordine degli stadi:
`plan` → `specify` → `perform`. L'argomento seleziona lo stadio, il default è
`all` (la sequenza intera). Ogni stadio invocato restituisce un esito
esplicito e può **chiudere in una riga** quando non ha materia («coda
coerente, nessun intervento»): la chiusura vuota è esito legittimo, non un
passo saltato.

È la skill simmetrica di `eval`: questa tiene onesta l'esecuzione, quella la
valutazione; il register `goal.md` è la cerniera che entrambe controllano da
versanti opposti. Usala a inizio sessione quando bisogna scegliere cosa
affrontare, e a fine sessione quando decisioni metodologiche,
generalizzazioni emerse dagli adottanti o ristrutturazioni di nodi possono
aver cambiato priorità, dipendenze o completezza dei task. Dopo eventi del
mondo gira per **ultima** nel protocollo post-evento (`eval` → `exec`): le
priorità si rivalutano su verdetti freschi, non stantii. Questa è la copia
canonica della skill: gli adottanti la forkano e la parametrizzano sui propri
segnali di dominio.

**Gate comune, proponi-poi-applica**: le modifiche a collezioni e register si
applicano solo dopo conferma del custode, e il gate prevale
sull'autorizzazione generica delle bussole — quella copertura è per il lavoro
ordinario di sessione, non per l'auto-applicazione degli esiti di una
supervisione. Fa eccezione solo l'atto che l'autorizzazione dello scope già
copre (cfr. `perform`).

## `plan` — la coda

**1. Raccogli il contesto corrente**

Esegui in parallelo:

```bash
git diff HEAD
git status --short
git log --oneline -5
```

Leggi `o1/plan.md`, il register `goal.md`, i fili recenti in `i3/` e i file
`o2/` necessari per capire i task aperti. Se l'obiettivo è solo un health
check, puoi limitarti ai titoli/frontmatter dei file `o2/`.

Cerca gli **handoff pendenti**: gli «impatti sul piano» di un `eval compare`
appena girato e le catture i1 con impatti o1 non ancora consumate. Sono
input, non comandi: consumali con giudizio e dichiara le divergenze (es. una
dipendenza che resta `world` anche se l'attesa puntuale è sciolta).

**2. Verifica la consistenza o1↔o2 col generatore**

Il contratto plan×`o2/` lo verifica il generatore: esegui
`o3/build-presentation.sh` e interpretane l'esito — a contratto violato esce
con l'elenco degli errori (riga del plan senza file `o2/`, voce di
`o2/tasks.md` senza file, file non indicizzato, colonna `Ob.` vuota,
frontmatter senza `sintesi`). Non reimplementare il matching a mano. Resta al
giudizio ciò che il generatore non copre:

- le prescrizioni `o3/` collegate a lavoro chiuso non restano in collezione —
  il dettaglio è giurisdizione di `perform`, qui basta il rimando
- task chiusi da un commit, una propagazione completata o un nodo creato non
  restano aperti
- `o1/plan.md` resta povero: il `metodo` non è una backlog board per gli
  adottanti (cfr. `kb/plan.md`), i suoi task sono rari e riguardano solo
  questo repo
- **direzione task→obiettivo**: ogni task serve un obiettivo dichiarato nel
  register `goal.md` (un task senza obiettivo è un candidato al taglio); il
  «lavoro corrente» citato nel register corrisponde a righe vive del plan. La
  direzione opposta (obiettivo→segnale/filo) è di `eval compare`
- `## Scadenze` e finestre tattiche: battiti in arrivo, righe scadute o
  consumate

**3. Rivaluta stato, dipendenze e priorità**

Individua eventi che possono spostare priorità o creare/rimuovere dipendenze,
che nel `metodo` hanno natura propria:

- una generalizzazione si è stabilizzata in un repo adottante -> può diventare
  nodo, skill base, strumento comune o criterio di revisione qui
- rinomina o spostamento di un nodo -> richiede aggiornare i link nei
  `CLAUDE.md` e `README.md` di tutti gli adottanti collegati
- nuova fonte (`i1`) ingerita o cornice teorica importata -> può aprire nodi
  bozza o ristrutturazioni
- drift tra `i2/` e i nodi -> può aprire un task di riallineamento o2
- scadenza di una fotografia dell'osservatorio cross-repo

**3b. Lettura strategica delle mosse**

L'igiene (passi 2-3) dice se la coda è coerente; non se una mossa **vada
fatta**. Per ogni mossa nostra che la review raccomanderebbe, interroga tre
lenti — e se una si accende, la mossa può **nascere come `pause`** invece che
come prossimo task:

- **mandato/canale** — la mossa scavalca un agente o un canale con mandato?
  Nel `metodo`: scrivere diretto nei file di un adottante invece di lasciare
  che il suo `method-review` tiri il canone scavalca la membrana («agisci
  attraverso, ratifica»).
- **sequenza/informazione** — un uso o una conversazione imminente darebbe un
  _read_ prima di muoverci? Nel `metodo`: l'uso reale di un adottante darebbe
  l'evidenza prima di incidere il canone («evidenza prima della struttura»).
- **effetti di secondo ordine** — la mossa rompe un consumatore a valle o
  cambia gli incentivi di una controparte? Nel `metodo`: un rename o un
  refactor di un nodo che rompe un generatore o un link negli adottanti.

È la versione **plan-time** del check i3 che `/commit` fa a commit-time:
stesso invariante, momento diverso. La ricchezza multi-attore (incentivi,
canali neutrali, tempismo di una negoziazione) vive nei fork degli adottanti
come adattamento di dominio; qui resta l'invariante.

**4. Proponi le modifiche e il prossimo task**

Presenta al custode, come elenco, le modifiche proposte — una voce per task,
con azione (aggiungi/modifica/rimuovi), priorità e motivo:

- **<task>** — <azione>; priorità <…>; <motivo>

Se non ci sono modifiche da proporre, dillo esplicitamente. Chiudi indicando
il task consigliato per la sessione corrente, motivandolo con urgenza,
dipendenze e costo/opportunità. Applica a `o1/plan.md` e `o2/` solo dopo
conferma (gate comune).

**5. Chiudi con l'handoff inverso «verdetti da rivalutare»**

Task i cui fatti, visti dal versante esecuzione, smentiscono o incrinano un
filo `i3/`. Se il protocollo post-evento è stato rispettato l'elenco è
normalmente **vuoto** — il vuoto è il segnale che la verità è passata per
prima, non un fallimento. Se non è vuoto, segnalalo al custode: il movimento
di ritorno è l'eccezione che va giustificata, non un secondo giro automatico.

## `specify` — la qualità interna dei task

Confine netto verso `plan`: `plan` guarda la corrispondenza e l'ordine delle
righe (il piano come coda, generatore incluso), `specify` la qualità interna
dei file `o2/` — la corrispondenza non si verifica due volte. Per ogni file
`o2/` vivo (o per quelli toccati di recente, se il giro è leggero):

- ogni task sostanziale ha il suo file: un task che vive solo come riga del
  plan e sta accumulando contesto è un file `o2/` mancante
- il frontmatter è completo: `sintesi` (la verifica dura la fa il generatore)
  e la facet `ciclo`, letta dal Mondo su cui il task insiste
- i diari di sessione si potano a chiusura: il file porta lo stato corrente
  del lavoro, non il log delle sessioni
- le **quattro proprietà cardine** come criteri di qualità (cfr.
  `kb/specify.md`): la specifica rende visibile ciò che il perform dovrà
  fare (visibilità), dichiara come si saprà che ha funzionato (feedback),
  mappa i concetti del task sulle risorse reali (mapping), e scrive i vincoli
  che impediscono l'atto sbagliato (constraint)

Esito: quali file sono a posto, quali hanno un difetto e quale, o la chiusura
in una riga.

## `perform` — l'atto e la sua collezione

Due piani, secondo autorizzazione:

- **La supervisione della collezione `o3/`**: tiene solo il vivo — le
  prescrizioni consumate (atto compiuto, o recepite da tutti gli adottanti)
  si potano insieme alla loro voce in `o3/prescriptions.md` (cfr.
  `kb/perform.md`, «Chiusura del ciclo di vita»); gli strumenti registrati
  sono ancora eseguibili (gli entrypoint girano); i runbook di propagazione
  riflettono il canone corrente, non uno stadio superato.
- **L'atto stesso**: quando è locale, reversibile e già autorizzato, si
  compie davvero; quando tocca il Mondo o richiede nuova autorità, si produce
  o si valida la prescrizione e ci si ferma al confine. In `metodo` il Mondo
  runtime sono gli adottanti: l'atto tipico è la prescrizione, e a compierla
  è il `method-review` dell'adottante — o3 prescrive, l'adottante ratifica.

Esito: stato della collezione (prescrizioni vive e loro freschezza, strumenti
verificati), atti compiuti o predisposti, o la chiusura in una riga.

## Note operative

- Mantieni i titoli brevi e coerenti con la tabella esistente
- La colonna `Dip.` deve riflettere dipendenze reali, non preferenze d'ordine
- I task completati si rimuovono da `o1/plan.md` e `o2/`; lo storico resta in
  git, nei fili `i3/` e nei nodi aggiornati
- Dopo la revisione, suggerisci `/commit` per chiudere la sessione quando ci
  sono modifiche da fissare
