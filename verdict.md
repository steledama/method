# verdict.md

Il verdetto attuale del progetto, per filo/area aperta — non un log. Il git log dice
_cosa_ è cambiato; questo file dice _come stanno le cose ora_ su ciascun filo
concettuale aperto, e _perché conta_. Specchio di `plan.md` sul lato valutazione:
`plan.md` fotografa i task aperti (o1), `verdict.md` i verdetti aperti (i3). Forma e
disciplina canoniche in [`kb/verdict.md`](kb/verdict.md).

Ogni gruppo `##` è un filo aperto; il corpo è lo **stato attuale**, aggiornato in
place, non una sequenza di entry datate (la cronologia di un filo è il git history di
questo file stesso). Quando un filo si chiude — verdetto stabile, nessuna tensione
aperta — il gruppo si rimuove: la storia resta in git. Il commit citato inline è il
puntatore alla storia verificabile.

---

## De-cablaggio del binomio «due agenti»: la seconda metà resta bottom-up

Il metodo è nato descrivendo due agenti — l'umano e un singolo LLM — e su quel binomio
aveva cablato la sua asimmetria in più nodi come se fosse _la_ struttura. Il nodo
`agent` lo ha riconosciuto per ciò che è: il **caso saliente** di una popolazione di
agenti più ampia (Norman: «person, animal, or machine»; la categoria macchina è un
gradiente, non un punto — un LLM di frontiera che pianifica e un agente locale che
esegue non sono lo stesso lettore sulla stessa KB). La prima metà è fatta, e
**additiva**: ammorbiditi `system-image`, `cognitive-system`, `knowledge-base`
togliendo al binomio lo statuto di struttura unica, senza cancellare il caso umano/LLM
— resta vero _come caso_, ed è l'unico in uso a valle (i nodi viaggiano per symlink).
La seconda metà — maturazione di `agent`, biforcazione di o1 per capacità dell'agente,
asse fiducia/privacy, divisione per stadio del ciclo — resta **deliberatamente non
scritta**: attende che un secondo livello di agente entri nell'uso reale. Scriverla ora
sarebbe inventare struttura prima dell'evidenza, l'opposto di come il metodo si
sviluppa.

## Maturazione dei nodi fondativi e debiti di fonte

La rifondazione ontologica (artefatto/sistema/metodo) e l'arco di input (i1/i2/i3)
hanno dato al metodo il vocabolario che gli mancava — cosa _è_ l'oggetto che coltiva,
cosa _vuole_ chi lo usa — ma i nodi che lo reggono sono ancora `bozza`, in attesa della
maturazione `bozza→maturo` dall'uso reale: `cognitive-artifact`, `cognitive-system`,
`goal`, `output`, `agent`, e i nodi i2 fondati su Norman (`affordance-signifier`,
`system-image`, `processing-layers`). Due debiti di fonte li tengono zoppi
sul lato fedeltà (i3): _Things That Make Us Smart_ (Norman 1993, fonte di «artefatto
cognitivo» e cognizione distribuita) è distillato solo nel Cap. 3
(`sources/representation.pdf`), il volume completo non è reperito; Hutchins (per
`cognitive-system`) e Leontiev (per `goal`) sono citati nei Riferimenti ma non vivono
in `sources/`. L'ingest delle fonti mancanti è tracciato in `plan` (mente estesa,
pace-layering). La matrice 4D del ciclo, infine, è un falsificatore costruito sulle
definizioni del metodo stesso: il suo esito «zero forzati» resta **provvisorio finché
non lo si testa su un repo nato senza il metodo**.

## Il lato-input appena rifondato: verdict come i3, interpretations come i2-macro

Il fronte più fresco (commit `dd5c2e7` + questa sessione): due artefatti del ciclo di
sviluppo hanno appena preso forma sul lato valutazione. **`verdict.md` è il residuo
scritto dell'i3** (Compare) — da log datato append-only a stato corrente per filo
aggiornato in place; disciplina ora canonica in `kb/verdict.md`, e questa migrazione ne
è la prima istanza reale (ciò che ha portato il nodo a `maturo`). **`interpretations/`
è i2-macro**: la sintesi periodica che rilegge l'intero artefatto e rivela tensioni
non-locali tra nodi. Il pilot su `economia` ha corretto la distinzione troppo rigida
tra i repo: la stessa superficie è o2 quando viene prodotta come vista di decisione e
substrato i2 quando viene letta; selezione e rappresentazione dei dati sono già
interpretazione orientata dai goal. La porta canonica è quindi `interpretations/`
ovunque, con il carattere nel contenuto. La propagazione ora ha un protocollo:
`method-review` usa un marker SHA versionato e lascia il lavoro pertinente nel repo
adottante. `economia` è il primo pilot committato; `nixos` è il secondo, committato
in `5d076ae`, e conferma il carve-out per output di altra natura ontologica
(configurazione Nix runtime, nessuna porta `interpretations/` vuota). La
propagazione è conclusa nei quattro adottanti: `economia` in `4c633b8`, `nixos`
in `5d076ae`, `bi` in `48f9e2cc`, `salute` in `bc1eaef`. Il caso BI conferma che
l'uniformità del protocollo non deve
interferire con opzioni applicative omonime: `--append-note` resta dominio,
`--append-why` era infrastruttura di audit. Il caso salute conferma che privacy,
diario, scadenze, fonti e skill di ingest sono adattamenti di contenuto e
workflow, non eccezioni alla struttura comune. _Ri-derivazione del deck_: chiusa.
Il deck è stato ri-derivato — esprime il framing i2-micro/macro e ha ricevuto un
restage viscerale che applica `processing-layers` a sé stesso. La slide che diagnostica
«un o2 solo riflessivo non muove» era resa in registro puramente riflessivo: il deck
commetteva il peccato che descrive. Ora contrasto, gerarchia e tre slide-eroe (con
l'accento caldo che lega il viscerale alla membrana `world`) portano la sintesi fino al
viscerale; il colpo «Attractive things work better» segue la slide della stasi, così il
deck _performa_ la lezione invece di solo enunciarla. La disciplina del nodo `deck`
(HTML/CSS nativi, build unica `pandoc`+`prettier`) è rimasta intatta.
