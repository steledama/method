---
data: 2026-05-22
stato: aperto
---

# Valutazione strumenti, skills e KB cross-repo

## Contesto

La Fase A del task `metodo-repo-centralizzato` ha centralizzato i 10 nodi
metodologici in `~/metodo/kb/` con symlink da ogni progetto. Restano fuori
perimetro tre categorie di elementi che trascendono i singoli progetti e che
potrebbero beneficiare di centralizzazione analoga: la CLI Google Workspace,
gli script di audit KB e le skills Claude Code.

La decisione di escluderli dalla Fase A è stata deliberata: hanno dipendenze
tecniche (runtime, parametrizzazione, meccanismi di aggiornamento) che
richiedono analisi separata. Questo task non apre una fase di implementazione:
serve a osservare l'evoluzione dei progetti e a preparare una valutazione più
solida prima di centralizzare strumenti o cambiare struttura ai repository.

## Orientamento prudente

Per il momento la linea guida è conservativa:

- non spostare strumenti runtime in `~/metodo` finché le varianti locali non
  sono state confrontate su più sessioni reali;
- non cambiare il symlink `metodo/ → ../metodo/kb` senza una motivazione
  cross-repo chiara;
- distinguere sempre tra pattern metodologico portabile e implementazione
  specifica di progetto;
- trattare eventuali rinomini delle cartelle `kb/` come decisione
  architetturale separata, perché impattano link, script, README, skill e uso in
  Obsidian.

## Candidati

### Google Workspace CLI (`gog`/`gws`)

Installata a livello sistema via nixos (`pkgs-ai`), usata operativamente in
economia e salute. Documentata oggi in `nixos/kb/google-workspace-cli.md`
nonostante sia rilevante per più progetti.

Ipotesi da valutare: nodo architetturale cross-repo in `~/metodo/kb/` che
descriva il pattern di utilizzo (auth per-host, comandi principali, note
cross-progetto), con il runbook di setup che resta nel progetto che installa e
configura i tool. Nel caso attuale il runbook operativo resta in `nixos/kb/`,
perché l'installazione avviene via NixOS/home-manager.

### KB audit scripts (`kb_tools.py`)

Ogni progetto ha una versione propria dell'audit script con sottocomandi
parzialmente diversi (nixos ha `inventory`, `facts`, `coverage`, `fidelity`;
bi e altri hanno versioni più semplici). Il pattern è comune; i dettagli
sono specifici del dominio.

- **Opzione A futura**: script canonico in `~/metodo/tools/` che i progetti
  adattano con fork leggeri — fonte unica per la logica comune, varianti
  esplicite.
- **Opzione B conservativa**: solo nodo metodologico in `~/metodo/kb/` che
  descrive il pattern; gli script restano indipendenti per progetto.
- **Opzione C intermedia**: libreria minima o template in `~/metodo/tools/`,
  con entry point locali che mantengono la logica di dominio.

La scelta predefinita resta l'Opzione B finché non emerge duplicazione reale e
stabile. `~/metodo` oggi è volutamente semplice e quasi solo markdown:
aggiungere runtime Python crea ownership, versionamento e coordinamento
cross-repo.

### Skills Claude Code

`audit-kb` e `commit` sono simili tra nixos, bi, economia, salute, ma non vanno
considerate automaticamente identiche. Cambiano formatter disponibili, scope dei
commit, controlli anti-drift, path locali e responsabilità di dominio.

Ipotesi da valutare: skill base in `~/metodo/skills/` e skill locali sottili che
aggiungono configurazione e controlli specifici. Una centralizzazione completa
con symlink diretti è da rimandare finché non è chiaro quali differenze siano
superficiali e quali strutturali.

### Naming delle cartelle KB

La Fase A ha lasciato nei progetti cartelle locali chiamate genericamente `kb/`.
Con l'introduzione di `~/metodo` come primo progetto cross-repo, questo nome
generico può diventare ambiguo in due contesti:

- nelle conversazioni e nelle analisi cross-repo, dove non è sempre immediato
  capire se un nodo appartenga a nixos, salute, economia, bi o metodo;
- in Obsidian, dove vault o cartelle chiamate tutte `kb` si distinguono solo
  dopo l'apertura.

Ipotesi da valutare: rinominare le cartelle di dominio in `kb-nixos/`,
`kb-salute/`, `kb-economia/`, `kb-bi/`, mantenendo `~/metodo/kb/` per i nodi
metodologici. Il beneficio sarebbe una maggiore chiarezza nominale cross-repo;
il costo sarebbe una migrazione ampia di link, script, README, skill, istruzioni
operative e abitudini di navigazione.

Per ora questa è solo una domanda di architettura. Non va implementata dentro
questa fase senza una valutazione dedicata e senza verificare quanto gli script
assumano il path `kb/`.

## Valutazione preliminare richiesta

Prima di qualsiasi implementazione, raccogliere almeno:

- confronto tra sottocomandi comuni e specifici dei quattro `scripts/kb_tools.py`;
- confronto tra skill `audit-kb` e `commit` nei quattro progetti;
- mappa dei riferimenti hardcoded a `kb/`, `metodo/`, `.claude/skills/` e
  `.codex/skills/`;
- impatto di un eventuale rinomino `kb/` sugli indici README, sui link Markdown,
  sugli audit e su Obsidian;
- casi reali emersi nello sviluppo dei progetti in cui la duplicazione degli
  strumenti ha creato costo o drift.

## Domande aperte

1. **Symlink scope**: se metodo cresce con `tools/` e `skills/`, il symlink
   corrente `metodo/ → ../metodo/kb` non basta. Occorrerà puntare `metodo/`
   all'intero repo `../metodo`, o usare symlink separati per sotto-cartella? La
   scelta impatta tutti i progetti già collegati.

2. **Ownership di kb_tools.py**: il repo metodo è oggi solo markdown, senza
   dipendenze di runtime. Aggiungere `tools/` con Python rompe questa
   semplicità e crea un punto di aggiornamento che richiede coordinamento. Vale
   la pena?

3. **Skills parametrizzate vs. varianti**: le differenze tra le versioni locali
   di `commit` e `audit-kb` sono superficiali (nomi formatter, path locali) o
   strutturali? Verificare prima di decidere se centralizzare o lasciare
   indipendenti.

4. **Naming KB locali**: il nome generico `kb/` è ancora il tradeoff migliore
   ora che esiste `~/metodo`, o conviene rendere esplicito il dominio nel nome
   della cartella (`kb-nixos/`, `kb-salute/`, `kb-economia/`, `kb-bi/`)? Quanto
   costa la migrazione rispetto al vantaggio cognitivo e all'uso in Obsidian?

5. **Principi specifici di salute**: salute non ha `design-principles.md`
   adattato al dominio (la sezione universale di `metodo/design-principles.md`
   è disponibile, ma mancano i principi specifici del progetto). Da scrivere
   come task separato in `~/salute`.

## Decisioni già prese

- Il symlink `metodo/ → ../metodo/kb` punta alla sotto-cartella `kb/`, non alla
  root: gli agenti vedono solo i nodi, non i file operativi del meta-repo.
  Qualsiasi estensione di metodo che aggiunga `tools/` o `skills/` dovrà
  riconsiderare questa scelta per tutti i progetti già collegati.
- Il nodo `google-workspace-cli.md` resta in nixos fino a decisione esplicita:
  l'installazione avviene lì e il runbook è nixos-specifico.
- Rinominare `kb/` → `kb-nixos/` etc. resta fuori scope implementativo di questa
  fase, ma diventa una domanda esplicita da valutare perché incide sulla
  chiarezza cross-repo e sull'uso in Obsidian.
