---
data: 2026-06-14
stato: aperto
---

# System image visiva: la home dell'atrio

Aperto in sessione di design 2026-06-14 (cfr. `verdict.md`, filo «Rifondazione
atrio↔azione»), riallineato 2026-06-15. La home è la controparte grafica
dell'atrio testuale dichiarato dall'`ls`: non un dashboard autonomo, ma un
navigatore che usa il modello di Norman per rendere visibili le principali
superfici del ciclo di sviluppo.

## Dipendenza e perimetro

Il task dipende da «Strato di presentazione trasversale (deck→view)» per:

- convenzione `assets/` e `views/`;
- token grafici e primitivi del ciclo;
- `views/tasks.html`, `views/verdict.html` e
  `views/interpretations.html`;
- disciplina «vista derivata, mai seconda fonte»;
- invariante di apertura tramite `file://`.

La home non usa Reveal e non è prodotta dallo stesso motore dei deck. Condivide
con essi asset, linguaggio visivo, sorgenti e convenzioni di build.

La prima versione include Goal, Plan, Specify, Compare, Interpret e World.
Perform e Perceive restano visibili per non falsare il ciclo di Norman, ma sono
attenuati e senza destinazione. `perceptions/` e `prescriptions/` non alimentano
la home e non ne determinano lo stato.

## Modello di navigazione

`index.html` riprende in forma schematica il ciclo «6 atti + 2 poli»:

- **GOAL**, in alto: identità e introduzione ricavate dal `README`;
- arco di esecuzione:
  - **o1 · Plan** — tabella dei task e dipendenze da `plan.md`, seguita dalle
    eventuali scadenze;
  - **o2 · Specify** — ingresso al deck `views/tasks.html`;
  - **o3 · Perform** — card inattiva, senza collegamento;
- arco di valutazione:
  - **i3 · Compare** — ingresso al deck `views/verdict.html`;
  - **i2 · Interpret** — ingresso al deck `views/interpretations.html`;
  - **i1 · Perceive** — card inattiva, senza collegamento;
- **WORLD**, in basso: progetti adottanti e descrizioni ricavati dal `README`.

Le card Plan, Tasks, Verdict e Interpretations sono le quattro superfici
navigabili. Plan è incorporato nella home: la relativa card porta alla sezione
interna che mostra la tabella completa e gli eventuali vincoli successivi.
Tasks, Verdict e Interpretations aprono invece le rispettive viste generate.

Goal e World sono poli informativi, non viste ulteriori. Perform e Perceive
restano nel diagramma come passaggi reali ma, in questa versione, non sono
collegati a `prescriptions/` o `perceptions/`.

## Sorgenti e trasformazioni

- `README.md`:
  - H1 e primo paragrafo sostanziale per Goal;
  - voci della sezione «Progetti adottanti» per World;
- `plan.md`:
  - righe della tabella, ordine e dipendenze;
  - sezione opzionale `Scadenze`;
- configurazione dello strato di presentazione:
  - path delle tre viste generate;
- Git:
  - organizzazione dell'URL remoto quando serve trasformare i link locali agli
    adottanti in link GitHub.

La home non legge il corpo dei task o del verdict: quelle rappresentazioni
appartengono ai deck dedicati.

## Comportamento dei link World

Il generatore supporta remote SSH e HTTPS. Quando `origin` identifica GitHub,
usa la sua organizzazione e il nome dell'adottante letto dal README per
costruire il link remoto. Se `origin` manca, non è GitHub o il dato non è
ricavabile con certezza, conserva il link relativo presente nel README invece
di inventare un URL.

## Implementazione

1. Creare `assets/system-image.css` sopra i token e i primitivi condivisi,
   mantenendo separate le regole specifiche di Reveal.
2. Creare `tools/build_system_image.py`, stdlib-only:
   - parsing strutturale delle sezioni previste di README e plan;
   - escaping di ogni contenuto inserito nell'HTML;
   - rendering del ciclo e della sezione Plan;
   - risoluzione robusta dei link World;
   - errore esplicito quando manca una struttura obbligatoria.
3. Creare `tools/build-system-image.sh` come entrypoint di build e formatting.
4. Generare e versionare `index.html` in root.
5. Aggiornare `tools.md`, README, `project-structure.md` e il verdetto corrente;
   chiudere il task in `plan.md` solo dopo la verifica completa.

## Vincoli

- home statica, offline e senza JavaScript;
- nessun `fetch`, server o build necessari per consultare l'HTML versionato;
- contenuto sempre derivato, mai mantenuto a mano in `index.html`;
- nessun link diretto a fragment di file Markdown;
- layout leggibile anche su schermi stretti;
- modello di Norman completo nella geometria, anche dove una card è inattiva;
- nessuna dipendenza da contenuti presenti in `perceptions/` o
  `prescriptions/`.

## Verifica e criteri di chiusura

- Goal e World coincidono con il README;
- tabella, ordine, dipendenze e scadenze coincidono con `plan.md`;
- i link a Tasks, Verdict e Interpretations aprono gli HTML corretti via
  `file://`;
- Plan porta alla sezione interna corretta;
- Perform e Perceive sono visibili, attenuati e privi di link;
- remote SSH, HTTPS e assente producono fallback corretti;
- caratteri speciali e contenuto Markdown non possono rompere o iniettare HTML;
- la home è utilizzabile su desktop e mobile senza perdere la leggibilità del
  ciclo;
- due generazioni consecutive sono identiche e la rigenerazione lascia il
  working tree pulito.

## Fuori perimetro

- viste per `perceptions/` e `prescriptions/`;
- attivazione di Perform e Perceive;
- terminale, chat o altri componenti serviti da backend;
- duplicazione nella home del contenuto già leggibile nei tre deck.
