# log.md

Registro interpretativo delle sessioni significative. Il git log dice cosa è cambiato; questo file dice perché conta.

---

## 2026-06-04 — Rifondazione: salto di quota concettuale (artefatto cognitivo)

Sessione di dialogo concettuale, ancora **pre-implementazione** (si seziona prima di
agire). Il task `rifondazione-input-output` è salito di quota: non più "rinominare e
chiudere la simmetria", ma rispondere alla domanda di fondo — *cosa è* l'oggetto che
stiamo costruendo. La risposta riordina tutto il resto e andrà a riscrivere il task.

**Tripartizione (tre parole, tre cose).** Si scioglie la sineddoche "KB = metodo"
distinguendo:
1. *Artefatto cognitivo* (Norman stretto, *Cognitive Artifacts* 1991: dispositivo
   rappresentazionale esterno) = la rappresentazione che si progetta e che persiste —
   KB + strato output + strato input + struttura. È ciò che il metodo coltiva. **È
   portabile**: sopravvive al cambio di modello o di harness.
2. *Sistema cognitivo* (Hutchins, cognizione distribuita) = artefatto + umano + LLM +
   harness, accoppiati. È *dove la cognizione accade davvero*. Non è portabile (contiene
   agenti specifici) e non si progetta come oggetto: emerge dall'uso.
3. *Metodo* = la pratica (il "come") con cui si coltiva l'artefatto perché il sistema
   performi.

**Argomento decisivo per la definizione artefatto-centrica**: la tesi del progetto
("harness portabile, vendor-neutro") è dicibile *solo* se l'artefatto è la
rappresentazione e non il sistema d'interazione. La definizione sistema-centrica toglie
la parola "portabile". L'utente — laureato in interazione uomo-macchina, tradizione
ergonomia cognitiva / cognizione distribuita — tende per formazione a pensare "sistema";
si è convenuto di tenere *entrambi* i concetti ma con nomi distinti, per non perdere ciò
che quella tradizione coglie (la cognizione vive nell'accoppiamento) senza rinunciare
alla portabilità.

**Stack a livelli.** L0 modello → L1 harness tecnico (Claude Code/Codex, sostituibile)
→ L2 = il metodo come *harness cognitivo* portabile e leggibile dall'umano. Norman vive
a L2 (design dell'interazione: visibilità, feedback, mapping, constraint), non a L1
(meccanismo). `agents.md` e i wrapper `.codex` sono già la cucitura L1↔L2.

**L0 è un agente, non un artefatto.** La novità — *l'artefatto che legge* — regge solo
tenendo distinti artefatto (KB) e agente (LLM). Tesi originale che estende Norman: Norman
scriveva per artefatti passivi; qui l'artefatto è letto e rielaborato da una seconda
mente. Il ciclo d'azione va riscritto per due agenti che condividono lo stesso system
image. Conseguenza che chiude un buco: o1 (output macchina) non manca dalla mappatura di
Norman — è il ciclo applicato al secondo agente. Asimmetria dei modelli mentali: per
l'umano la KB è impalcatura esterna a un modello che già possiede; per l'LLM la KB *è*
il modello mentale (riparte da zero ogni sessione).

**Il Goal come confine aperto di Norman.** Il metodo traccia i task (Plan/Specify) ma non
i Goal (il perché). `goal` / `task` / `todo` sono tre *altitudini*, non sinonimi —
disciplinabili con la gerarchia dell'activity theory: motivo (attività) → goal (azione) →
operazione (task). Architettura: i3 (input formalizzato) ha *due* destinazioni, la KB e
la revisione dei goal — è il Compare→nuovo Goal di Norman. Decisione: **non** rinominare
`todo/`→`goals/` (nasconderebbe il concetto e mentirebbe sul contenuto attuale); scrivere
il *nodo* sul Goal e lasciare emergere l'apparato quando il lavoro lo richiede.

**Struttura nodi propensa (taglio B + cerniera)**: `artefatto-cognitivo`,
`sistema-cognitivo` (cerniera, dove vive l'asimmetria dei modelli mentali), nodo `goal` /
gerarchia dell'azione; `ciclo-azione` riscritto come ciclo a due agenti.

**Decisioni che superano l'entry precedente**: la lingua del repo è **inglese** (non più
"aperta"). Servono *più libri di Norman*, non solo DOET: "cognitive artifact" e cognizione
distribuita vengono da *Things That Make Us Smart* (1993). L'ingest dei libri di Norman
diventa un **task separato** (`todo/ingest-norman.md`), candidato a essere il primo pilota
reale dello strato input.

**Forma del ciclo: due cerniere, non uno specchio** (scioglie il filo del "mirror").
La struttura di Norman non è uno specchio (i3 ↔ o1) ma un *cappio con due cerniere*. Il
Goal è l'apice (sta sopra entrambi i gulf), il Mondo è il fondo; l'esecuzione (Q2 Plan,
Q3 Specify = o2 → Q4 Perform = o3) è la discesa, la valutazione (Q5 Perceive = i1 → Q6
Interpret = i2 → Q7 Compare = i3) è la risalita. Le due cerniere:
- **Mondo** (Q4→Q5): o3 agisce, i1 percepisce — stesso luogo, due versi: *simmetrico*.
- **KB** (Q7→Q1): l'apice. i3 *scrive* l'esito nella KB; il Goal *legge* l'intenzione
  dalla KB. Scrivi-poi-leggi, non riflesso. L'asimmetria al confine KB è **feature**: la
  KB è la memoria persistente dove il ciclo si chiude.
o1 non sta su questo arco — vive sul ciclo del *secondo agente* (l'LLM che legge la KB
per agire), che ha un proprio lato-input macchina (audit, lint, errori, test). Due cicli,
uno per agente, stessa KB all'apice. Va disegnato così in `ciclo-azione` e nel mermaid
"ciclo che si chiude" (sostituisce le due colonne speculari). Cautela di fedeltà sul Goal:
la KB *informa e raffina* il Goal, non lo *genera* — il Goal nasce all'incrocio motivo
(da sopra) + KB; è l'estensione di Norman "sul Goal".

**Gradiente di autonomia e passaggio di consegne** (concetto nuovo, forse il più
originale). Il repo versionato è la *traccia* di un passaggio di consegne graduale
umano→LLM: git registra la delega progressiva mentre l'harness di guardrail e
autocorrezioni si accumula. Traiettoria human-in → human-*on* (controllo supervisorio,
Sheridan) → human-out, dove la fase "on" è la più insidiosa — *ironie dell'automazione*
(Bainbridge 1983): le skill si atrofizzano e la ripresa del controllo è richiesta proprio
quando è più difficile. L'autonomia non è uno slider unico ma un *profilo per stadio del
ciclo* (livelli di automazione, Parasuraman/Sheridan) e dipende da **quanto del motivo è
esternalizzabile nell'artefatto**. Gradiente sui quattro repo: `nixos` (motivo
codificabile → autonomia alta) → `bi`/`economia` (media, gate umani obbligatori) →
`salute` (motivo non esternalizzabile → supervisione permanente). Il README di ogni
progetto dovrebbe dichiarare scopi generali + grado di autonomia attuale/aspirato.
Conseguenza che ribalta l'obiezione bottom-up sul lato input: **il lato valutazione
(i1→i2→i3) è il meccanismo di sicurezza che rende possibile l'uscita dell'umano dal
loop** — non simmetria teorica ma load-bearing. o2 non sparisce con la fine dei PDF: si
trasforma in *spiegazione resa su richiesta*, perché per le decisioni ad alta posta
l'umano deve *capire* (formarsi un modello mentale), non solo interrogare — altrimenti
perde la capacità di valutare. (Fonti: il "flusso" è di Csikszentmihalyi, Norman lo
adotta.)

**Due principi dell'arco di input (dal caso economia, bottom-up).**
1. *i2 goal-guidato sulla rilevanza, neutro sulla valenza.* I goal scelgono legittimamente
   cosa mostrare, granularità, confronti (rilevanza), mai il verdetto buono/cattivo
   (valenza), che è compito di i3. Test: due persone con goal di valenza opposta devono
   produrre lo *stesso* i2 e dissentire solo a i3; se i2 differisce già nel giudizio,
   l'artefatto non ospita una valutazione, riflette il bias. i2 = rappresentazione
   condivisa e contestabile; i3 = dove avviene il contrasto (cruciale nel multi-stakeholder,
   es. conti personale/comune di due partner in `economia`). Pattern già presente in
   `salute/quadro`: i numeri = i2, il termometro/colore = i3. Un i2 goal-saturo distrugge
   il gulf of evaluation e annulla la funzione di sicurezza dell'arco di input — l'artefatto
   non può più portare cattive notizie.
2. *L'arco di input è più ampio dell'arco di valutazione di Norman.* i1 ha due sorgenti:
   feedback (risposta a o3, chiude un goal esistente, Norman puro) ed esogeno (il mondo
   agisce da sé — busta paga, normativa, alert — apre spesso un goal nuovo). Quindi i3 ha
   due modi: verdetto (Compare contro goal esistente) e triage/formazione-goal (per
   l'esogeno). Conseguenza autonomia: *delega la chiusura di loop noti, tieni l'umano per
   l'apertura di loop nuovi* (il triage dell'esogeno = decidere cosa conta = formazione del
   goal, la cosa meno esternalizzabile; eco di Bainbridge). Il metodo apre il confine-Mondo
   (il mondo non solo risponde, agisce) come apre il confine-Goal: estensione di Norman a
   entrambi gli estremi.

**Metodo di sviluppo del metodo (concordato).** Validare i concetti teorici calandoli
bottom-up nei quattro domini, ognuno banco di prova di una parte diversa: `economia`
(multi-stakeholder, irreversibilità, valenza), `salute` (motivo non esternalizzabile,
corpo), `nixos` (autonomia alta, determinismo, feedback-heavy, poco esogeno), `bi`
(decisioni condivise, input esogeno dai colleghi). `nixos` e `bi` sono quasi opposti
sull'asse feedback/esogeno — il confronto valida la criticità 2. Più si cala la parte poco
chiara in un dominio, più si illumina l'intero.

**Anti-dogma per costruzione.** Ciò che va "scritto nella pietra" non sono i verdetti
(output di i3, sempre revisionabili) ma i *meccanismi di autocorrezione* (i2 neutro sulla
valenza, input come intake del mondo): sono ciò che tiene l'artefatto capace di smentire i
propri goal e di ascoltare il mondo che agisce. La pietra è l'impegno a restare corrigibili,
non le conclusioni. Mappa sulla distinzione che il repo già ha: metodo/nodi stabili (pietra)
vs goal/valutazioni revisionabili (fluido).

**Fili ancora da sezionare** prima di riscrivere il task: il sottoscoping dei file da
aggiornare (`pattern-karpathy`, `knowledge-base`, `mappa` sono riscritture concettuali,
non solo link); lo stato bozza/maturo e la dipendenza con `salute/quadro/` tracciata in
`confronto-progetti-adottanti`; la trappola del grep ("ponte" è anche metafora viva in
`agents.md`, `mappa.md` e nei `project-map` dei repo adottanti — non sostituire ciecamente).

**Nota di metodo (dogfooding su me stesso)**: in questa sessione avevo salvato gli appunti
concettuali nello store di memoria dell'harness (`~/.claude/`). È l'anti-pattern
dell'artefatto portabile — host-locale, opaco, non versionato. Rimossi; la regola "la
memoria del progetto vive versionata nel repo" è ora in `CLAUDE.md` (sezione `## Memoria`),
e questi appunti vivono qui, dove dovevano stare.

---

## 2026-06-04 — Rifondazione input/output: pianificazione e formulazioni fondative

Sessione di pianificazione metodologica con tre prodotti concreti: frontmatter PDF,
strategia di condivisione con Luigi, task rifondativo aperto.

**Firma PDF**: aggiunto frontmatter YAML a `presentazione/metodo-in-sintesi.md`
(title, subtitle, author, date). Il template LaTeX esistente in `nixos/modules/home/md2pdf.nix`
gestisce già `\maketitle` condizionale — nodi senza frontmatter non sono influenzati.

**Strategia GitHub aziendale**: definiti tre livelli di accesso (metodo pubblico,
`bi` in sola lettura ai colleghi, nixos/salute/economia privati). Redatta email a Luigi
per invitarlo a creare un account GitHub personale — solo il primo passo, senza condividere
il metodo finché non dà un segnale concreto di interesse reale.

**Task rifondativo** `todo/rifondazione-input-output.md`: il task più denso aperto finora
in questo repo. Tre questioni operative (rename ponte→output, L1/L2/L3→o1/o2/o3, lingua
italiano→inglese) e una ristrutturazione concettuale profonda. Le formulazioni fondative
emerse durante la sessione, da usare come apertura dei nodi riscritti:

*I tre giganti rispetto alla KB*: Luhmann è la KB — Karpathy governa la KB — Norman
connette la KB al mondo. Più preciso dell'attuale "si dividono il lavoro in modo nitido":
dice dove ognuno lavora, non solo cosa porta.

*Il metodo come estensione di Norman*: Norman dà per scontati due elementi ai confini
del ciclo — il Goal e il Mondo. Il metodo interviene su entrambi: la KB è il luogo dove
i goal si formano (non sono dati); lo strato input governa come il Mondo entra nel sistema
(non è una scatola nera). Il metodo non applica Norman: lo estende verso i suoi estremi
irrisolti.

*KB come sineddoche del metodo*: "KB" viene usata spesso quando si intende il sistema
intero. La KB in senso stretto è solo i nodi in `kb/`. Durante la riscrittura in inglese:
"the method" per il sistema intero, "the KB" solo per i nodi di conoscenza.

*Base empirica degli strati input*: il pattern di ingest non governato esiste già nei
quattro repo — estratti conto e referti in `economia` e `salute`, errori e alert in
`nixos`, segnalazioni dei colleghi in `bi`. La formalizzazione i1/i2/i3 è bottom-up.

Tre decisioni aperte nel task: nomenclatura (input/output vs esecuzione/valutazione),
lingua (italiano vs inglese, propensione per l'inglese per fedeltà cognitiva alle fonti),
strato input come componente obbligatorio o opzionale.

---

## 2026-06-03 — Revisione qualitativa profonda dei nodi e strato output del metodo

Revisione semantica di tutti i 25 nodi, oltre il lint strutturale (sempre pulito).
Diagnosi: KB matura e coerente, ma sovradimensionata e ridondante rispetto al suo
stesso scopo (portabilità, basso costo di comprensione). Ironia di fondo: il
metodo predica fonte-unica-di-verità e "la sintesi vive nel ponte perché la KB
resti pura", ma violava entrambe le regole su sé stesso. Intervento in quattro
passaggi, un commit ciascuno.

Pass 1 — dati cross-repo centralizzati in `confronto-progetti-adottanti`. I
conteggi per repo (nodi, link, righe CLAUDE, task, audit datati) erano duplicati
e già stantii in `strumenti-kb`, `indice`, `task-aperti`, `claude`, `agents`:
mini-fotografie sparse che nessuno risincronizzava. Tolti i numeri fragili,
lasciata la lezione qualitativa.

Pass 2 — de-duplicati i blocchi concettuali ripetuti, con case canoniche: tre
giganti → `ciclo-azione`, L1/L2/L3 e conflitto Zettelkasten/Karpathy → `ponte`,
esposizione strumenti → `strumenti-kb`, quattro proprietà di Norman →
`ciclo-azione`. Altrove: ruolo proprio del nodo + rimando, niente
ri-derivazione. Applicata fonte-unica anche ai concetti, non solo ai dati.

Pass 3 — `struttura-progetto` (146→112 righe) ripeteva liste di regole con nodo
dedicato (`Regole AGENTS/CLAUDE/todo`, `Sezioni README`). Keep/relocate/remove:
bullet unici spostati in `claude`, liste sostituite da pointer. Il nodo resta
overview dei pilastri; i criteri di revisione vivono nei nodi-casa. Nessun nodo
rimosso: `agents` e `git-history` restano sottili ma con funzione distinta, e lo
stato `bozza` lo segnala onestamente.

Pass 4 — creato il primo strato output del repo `metodo`:
`presentazione/metodo-in-sintesi.md`, cinque diagrammi Mermaid (tre giganti,
ciclo dell'azione, anatomia del progetto, sviluppo bottom-up, routing dei
contenuti). Dogfooding: il metodo applica il proprio principio `ponte` a sé
stesso — la sintesi vive nello strato output, non in un nodo `kb/`. Il file
dichiara anche L1/L2/L3 del repo metodo. Era l'L2 mancante: il metodo descriveva
sé stesso solo a parole, senza una vista a colpo d'occhio.

---

## 2026-06-03 — Seconda fotografia dell'osservatorio

Rinfrescato `confronto-progetti-adottanti` dopo che la prima fotografia (2026-05-23)
era invecchiata di 11 giorni mentre i repo adottanti continuavano a muoversi.
La rilettura è funzione di osservatorio (lettura dei repo), non orchestrazione,
quindi coerente col flusso bottom-up.

Cosa è cambiato dai dati reali: `economia` è cresciuta (51→55 nodi, 184→198 link)
e ha audit pulito — i "segnali strutturali da correggere" del vecchio nodo erano
ormai falsi; `bi` ha chiuso due task (todo 9→7) restando stabile a 84 nodi;
`nixos` e `salute` invariati nei numeri. Aggiornate le tre tabelle del nodo
(stato, dati strutturali, azioni suggerite) e marcate come completate le azioni
ormai concluse (bi CLAUDE, salute mappa, economia audit).

Due osservazioni metodologiche registrate nel nodo. Primo: i 10 file accentati di
`salute` (`realtà.md`, `qualità.md`, …) sono un default strumentale che non aderisce
al dominio, non un drift — la regola "niente accenti nei nomi" è convenzione tecnica
che una KB riflessiva italiana può legittimamente non seguire; resta decisione locale.
Secondo: `ponte` e `ciclo-azione` sono ancora `stato: bozza` per scelta, non per
dimenticanza — la promozione a maturo è un filing back atteso dal pilota
`salute/quadro/` quando produrrà 2-3 cicli L2→L3→fonte→KB documentati.

Conferma operativa: l'osservatorio si ricostruisce a mano in poche query
(`kb_tools.py audit` per repo), quindi un report cross-repo automatico resta non
necessario finché il costo non cresce — niente task preventivo, in linea bottom-up.

---

## 2026-06-01 — Formalizzazione sviluppo bottom-up del metodo

Formalizzato nei nodi centrali il principio emerso dalla revisione dei task:
lo sviluppo del metodo è bottom-up. Una modifica metodologica nasce da
un'esigenza concreta in un repo adottante, viene risolta lì nel merito, poi viene
riportata in `metodo` solo se produce una generalizzazione portabile. Gli altri
repo adottanti recepiscono la modifica leggendo i commit del metodo e applicando
localmente ciò che è pertinente.

Aggiornati `metodo-kb`, `osservatorio-metodo`, `task-aperti`, `todo` e README.
La conseguenza operativa è che `metodo/todo/` non è una backlog board
cross-repo: i task qui devono riguardare il metodo stesso, la sua presentazione,
la coerenza dei nodi, strumenti comuni già giustificati o generalizzazioni
emerse dall'uso reale.

---

## 2026-06-01 — Chiusura task residui e triade skill ufficiale

Chiusi gli ultimi due task aperti in `metodo`. Il task `Confronto skill
audit-kb e commit cross-repo` è stato assorbito nella formalizzazione della
triade ufficiale `audit-kb` / `revisione-tasks` / `commit` in `kb/skill.md`: non
serve mantenere un task separato di confronto perché i quattro repo adottanti
espongono già la triade con parametrizzazioni locali.

Chiuso anche `Superficie portabile kb_tools.py: comandi avanzati` senza
implementazione centrale. I comandi avanzati come `facts`, `fidelity`,
`coverage` e `inventory` restano locali finché un bisogno concreto in un repo
adottante non produce una generalizzazione bottom-up. Il repo `metodo` non
mantiene più task preventivi su strumenti nati in un singolo repo.

Il README ora registra nessun task aperto. Questa è la forma desiderata per il
repo `metodo`: entrare qui raramente, per ristrutturare, semplificare o custodire
generalizzazioni già emerse dai repo adottanti.

---

## 2026-06-01 — Skill revisione-tasks applicata ai repo adottanti

Chiuso il task `Portabilità skill revisione-tasks` applicando subito il pattern
a tutti i repo adottanti. `economia` resta il caso originario; `nixos`, `bi` e
`salute` hanno ora una skill `.claude/skills/revisione-tasks` con wrapper Codex
corrispondente, discovery in README e riga operativa in CLAUDE.md.

La decisione metodologica è che la funzione è comune, ma la skill vive locale:
ogni repo deve rivedere task, priorità e dipendenze rispetto ai propri segnali
concreti. `kb/skill.md` registra quindi la triade comune `audit-kb` /
`revisione-tasks` / `commit`, senza introdurre un task centrale top-down.

---

## 2026-06-01 — Task file locali di dominio spostato in economia

Spostato il task `Formalizza pattern file-dominio` dal repo `metodo` al repo
`economia`, dove ora vive come `todo/file-locali-dominio.md`. Il criterio sui
componenti locali di dominio deve nascere dall'uso concreto di `stato.md`,
`scadenze.md` e `diario.md`; `metodo/kb/struttura-progetto.md` riceverà solo il
filing back se il pattern si dimostra portabile.

Questa chiusura segue la stessa regola bottom-up adottata per `salute/quadro/`:
il repo adottante produce l'evidenza, il repo metodo custodisce la
generalizzazione.

---

## 2026-06-01 — Task pilota quadro spostato in salute

Spostato il task `Osservazioni dal pilota salute/quadro/` dal repo `metodo` al
repo `salute`, dove ora vive come `todo/osservazioni-quadro-pilota.md`. La
verifica richiede uso reale del quadro, raccolta di cicli L2 -> L3 -> fonte ->
KB -> quadro e osservazione delle decisioni locali; tenerla in `metodo` la
rendeva un controllo top-down su un repo adottante.

In `metodo` resta solo la destinazione del filing back: `kb/ponte.md` dovrà
essere aggiornato se dal pilota di `salute` emergeranno criteri portabili sullo
strato output. Questa chiusura rafforza la regola operativa bottom-up: il repo
adottante produce l'evidenza, il repo metodo custodisce la generalizzazione.

---

## 2026-06-01 — Chiusura task README narrativo salute

Chiuso il task centrale `README narrativo di salute: quando è accettabile?`
senza lavorarlo da `metodo`. Il task era formulato come verifica top-down sul
README di un repo adottante; secondo la direzione bottom-up emersa nella
revisione dei task, una revisione del README di `salute` deve nascere dentro
`salute` da un problema concreto di bootstrap, orientamento o drift.

Se da quel lavoro locale emerge un criterio generalizzabile sulla narratività
dei README in domini riflessivi, il filing back corretto sarà aggiornare
`kb/readme.md` in `metodo` dal repo adottante, non mantenere qui un task di
controllo preventivo su `salute`.

---

## 2026-06-01 — Chiusura regress check CLAUDE.md BI

Chiuso il task `Regress check CLAUDE.md bi` dopo verifica della storia locale
di `../bi`. Il commit `b195b8ff` (`docs(kb): compatta CLAUDE e chiudi task
metodo`) ha eliminato il task locale `todo/revisione-claude-md.md`, rimosso la
riga dal README di BI e registrato in `log.md` la riduzione di `CLAUDE.md` da
manuale esteso a costituzione operativa. Il commit successivo `a78091c1` ha
aggiunto solo la tabella operativa degli strumenti propagata da `~/metodo`, non
un ritorno alla documentazione narrativa di dominio.

Il criterio quantitativo indicato nel task centrale (`~100 righe`) era troppo
rigido rispetto al caso reale: già dopo la chiusura locale BI `CLAUDE.md` era a
162 righe, e oggi è a 187 per effetto della tabella strumenti. La soglia utile
resta qualitativa: `CLAUDE.md` non deve tornare manuale parallelo alla KB.

---

## 2026-05-29 — Filing back da economia: audit pulito non basta

La revisione di `economia` ha mostrato un drift non rilevato dall'audit
strutturale: il README indicizzava nodi metodologici condivisi come se fossero
contenuto locale, pur avendo link validi e audit 0/0/0. Il metodo viene chiarito:
i progetti adottanti devono dichiarare il repo `metodo` come dipendenza
trans-repo e tenere separati indice locale, mappa del dominio e contenuto
metodologico condiviso.

Aggiornati `fedelta-cognitiva`, `skill`, `readme` e `indice`: `audit-kb` fotografa
lo stato e deve includere una revisione qualitativa di README/CLAUDE/mappa;
`commit` è il gate più capillare per prevenire drift, perché impone il filing
back prima che una modifica venga fissata nella storia.

La stessa sessione ha chiarito anche la regola di esposizione degli strumenti:
devono essere scopribili nel README, operativi in CLAUDE.md e approfonditi nei
nodi. Questa tripartizione aumenta la consapevolezza dell'LLM senza trasformare
README o CLAUDE in manuali duplicati.

---

## 2026-05-24 — Rafforzamento operativo dello strato output

Il pilota `salute/quadro/` ha chiarito un criterio che mancava al nodo `ponte`: uno strato output non è maturo quando ha file ben formattati, ma quando lascia traccia di cicli completi L2→L3→fonte→KB→quadro. Aggiornato `kb/ponte.md` con la dichiarazione minima dello strato output (L1 macchina, L2 decisione, L3 azione, fonte di ritorno, criterio di aggiornamento) e con il segnale empirico di maturità: osservare almeno 2-3 cicli completi.

Aggiornato il task `salute-quadro-pilota` per trasformarlo da osservazione passiva del pilota a verifica attiva: registro azioni, prossime decisioni, fonti prodotte e ritorno nel quadro. La maturazione del metodo passa ora dall'uso reale di `salute/quadro/azioni.md`.

---

## 2026-05-24 — Creazione di `ponte` e `ciclo-azione`: tre giganti riconosciuti

Promossi al meta i due nodi previsti dal task `ponte-teoria-pratica`. `ponte.md` formalizza lo strato output del metodo: i tre livelli L1 macchina, L2 decisione umana, L3 azione nel mondo; la risoluzione del conflitto Zettelkasten/Karpathy (la sintesi vive nello strato output, non nei nodi); il ciclo che si chiude attraverso l'azione; lo stato dei quattro progetti adottanti.

`ciclo-azione.md` distilla il modello del ciclo di azione di Donald Norman: i sette stadi (Goal → Plan → Specify → Perform → Perceive → Interpret → Compare), i due gulf (execution, evaluation) come metriche delle distanze cognitive, le quattro proprietà cardine (visibilità, feedback, mapping, constraint) come criteri di qualità per L2. Introduce Norman come terzo gigante del metodo accanto a Luhmann (atomicità del nodo) e Karpathy (manutenzione LLM).

Aggiornati i README di `metodo` e di `salute` per citare i tre giganti. Aggiornato `confronto-progetti-adottanti.md` per registrare la promozione dello strato output da "componente locale aggiuntivo" a "componente universale con forme locali". Filing back: il file `salute/quadro/quadro-corporeo.md` linka ora i due nuovi nodi metodologici (dal locale verso il meta), pattern che diventa parte del metodo stesso.

Una formulazione che resta come fondamento: lo strato output esiste perché il KB possa restare puro. È la sua condizione di possibilità, non un'aggiunta opzionale.

Provocazione utile da Norman, ripresa nel nodo `ciclo-azione`: se l'utente non agisce, la KB è mal progettata, non l'utente è pigro. Lo strato output va dunque valutato sui criteri di Norman, non sulla bellezza dei nodi.

I due nodi sono in stato bozza. Maturazione attesa con l'uso reale del pilota in `salute`.

---

## 2026-05-24 — Strato output e terzo gigante Norman

Sessione cross-repo nata in `salute` con ricadute meta importanti. La riflessione ha riconosciuto una funzione cognitiva universale del metodo finora implicita: lo strato di OUTPUT, distinto dalla KB. Tre formulazioni stabilizzate.

Prima: il conflitto Zettelkasten/Karpathy sulla sintesi (atomicità vs pagine di sintesi nel wiki) si risolve separando KB e output. La sintesi vive nello strato output, non nei nodi. **Lo strato output esiste perché il KB possa restare puro.** Risolve anche pressioni attualmente visibili in alcuni nodi (es. `salute/kb/storia-clinica.md`, diventato di fatto un dashboard improprio).

Seconda: l'output universale ha tre livelli. L1 — macchina (JSON, dati strutturati, `.nix`), L2 — decisione umana (schemi, diagrammi, slides, termometri), L3 — azione nel mondo (email, parole dette, gesti corporei, transazioni). L3 ritorna come fonte chiudendo il ciclo. Stato attuale dei quattro progetti adottanti:

- `nixos`: L1 forte (`home/`, `hosts/`, `modules/`), L2 debole (architettura solo come testo in `kb/`), L3 forte (sistema in esecuzione)
- `bi`: forte su tutti i livelli (scripts notturni + `presentazione/` Reveal.js + decisioni business)
- `economia`: L1 forte (`output/json/`), L2 medio (`output/report*.md` solo tabelle), L3 forte (email, riunioni famigliari)
- `salute`: L1 implicito sparso, L2 assente (l'SVG su Drive era un proto-output fuori repo), L3 medio-forte

Pattern emergente: dove L2 è forte (`bi`) il progetto serve decisioni condivise con altri; dove è debole resta personale e introspettivo, e fatica a generare azione coordinata.

Terza: Donald Norman è il terzo gigante del metodo accanto a Luhmann e Karpathy. Il modello dei sette stadi e i due gulf (execution, evaluation) descrivono precisamente come L1/L2 servono L3. Le quattro proprietà cardine (visibilità, feedback, mapping, constraint) diventano criteri di qualità per L2. Provocazione utile: una KB con poche affordance e nessun feedback è mal progettata, non è la persona pigra.

Decisione: pilota prima in `salute/quadro/`, formalizzazione meta dopo. Aperto il task gemello `ponte-teoria-pratica` in `todo/`, con dipendenza esplicita dal pilota di salute. I due nodi che nasceranno in `kb/` sono `ponte.md` (lo strato, risoluzione Zettelkasten/Karpathy, tre livelli, ciclo chiuso) e `ciclo-azione.md` (distillazione metodologica di Norman, gemello formale di `pattern-karpathy.md`, non biografia). Aggiornamenti collaterali previsti: `confronto-progetti-adottanti.md` per promuovere l'output da "componente locale" a universale, e `metodo-kb.md` per citare i tre giganti.

---

## 2026-05-24 — Osservatorio salute chiuso

Chiuso il task `osservatorio-salute`: nel repo `salute` sono stati creati
`kb/mappa-progetto.md`, `kb/principi-salute.md` e
`kb/verifica-nel-vivere.md`, con aggiornamento di README, CLAUDE e log locali.

Il caso conferma tre regole metodologiche. Primo: le verifiche cross-repo
restano nel repo `metodo`, ma quando producono contenuto di dominio diventano
task locali. Secondo: per KB riflessive la mappa non deve simulare una mappa
tecnica; deve collegare assi concettuali, fonti, pratica e diario. Terzo:
README-only è accettabile per ingest semplici, mentre interventi strutturali o
serie di nodi richiedono `todo/` finché non vengono stabilizzati in nodi.

## 2026-05-22 — Fondazione del repo

Creato il repo `~/metodo` come fonte unica di verità per i nodi metodologici,
consolidando le versioni sparse in nixos, bi, economia e salute.

La versione nixos era la più evoluta su tutti i nodi. Il diff ha rilevato tre
contributi non banali dagli altri repo:

- `struttura-progetto`: da economia, aggiunta la nozione di "README come
  artefatto a doppia audience" e "revisione-tasks come chiusura sessione"
- `strumenti-kb`: da economia, aggiunto il dettaglio "tre livelli
  (errore/avviso/info)" nell'output di audit
- `fedelta-cognitiva`: generalizzato il livello fattuale per renderlo
  domain-agnostic; aggiunta sezione "Adattamento al dominio" con economia come
  esempio di adattamento al dominio legale/finanziario

`design-principles.md` è stato scritto ex novo unificando i due approcci
divergenti di nixos (ingegneria del codice) e bi (affidabilità dei sistemi
dati) in un documento stratificato: principi universali + principi code-based +
principi specifici di progetto nel README locale.

I nodi zettelkasten, connessione e pattern-karpathy erano identici in tutti i
repo: copiati verbatim.

Fase A.2 (symlink + pulizia locale) e Fase B (strumenti cross-repo) restano
task aperti in `~/nixos/todo/metodo-repo-centralizzato.md`.

---

## 2026-05-23 — Metodo KB come hub della ricetta metodologica

Riorganizzato `kb/metodo-kb.md` per eliminare la ripetizione tra componenti
portabili, skeleton minimo e prompt di creazione. L'inventario ora compare una
sola volta come "Ricetta metodologica"; le altre sezioni descrivono creazione,
criteri di separazione e varianti osservate nei progetti adottanti.

La revisione conferma che non serve ancora creare un nodo autonomo per ogni
componente: `nodo`, `struttura-progetto` e `strumenti-kb` sono gia separati
perche hanno regole proprie, mentre README, CLAUDE, AGENTS, log e todo restano
componenti strutturali descritti dall'hub finche non accumulano semantica
riusabile piu ampia.

Aggiunto `AGENTS.md` al repo metodo per allineare il repository alla propria
ricetta minima: wrapper breve, ordine di lettura esplicito, nessuna duplicazione
delle regole operative.

Aggiunto `scripts/kb_tools.py` come backend portabile: comandi base per audit,
backlink, orfani, README, migrazione e termini candidati; comandi generici
`inventory` e `coverage` per progetti code-based. I controlli di fedelta
specifici di dominio restano estensioni locali nei progetti adottanti.

Formalizzata la funzione del repo metodo come osservatorio cross-repo in
`kb/osservatorio-metodo.md`. Il repo non conserva solo il metodo generale, ma
osserva periodicamente come il metodo viene incarnato nei progetti adottanti:
README, CLAUDE, AGENTS, log, todo, nodi, strumenti, skill, fonti di verita e
salute complessiva delle KB. Il task cross-repo esistente e stato ampliato come
prima implementazione operativa dell'osservatorio.

Aggiornato il README con il titolo `Metodo KB` e con l'inquadramento a doppia
funzione: metodo portabile e osservatorio cross-repo. L'apertura ora esplicita
che le differenze tra progetti sono materiale di analisi per decidere cosa
generalizzare, cosa lasciare locale e cosa trasformare in task operativo.

Espanso `kb/metodo-kb.md` con un indice cognitivo del metodo e creati nodi
bozza per tutti i componenti della ricetta che non avevano ancora un nodo
autonomo: AGENTS, CLAUDE, README, indice, task aperti, mappa, todo, log, git
history, skill e fonte di verita. La scelta rende esplicito che il metodo e un
work in progress pratico: i componenti non maturi possono essere descritti,
collegati, confrontati tra repo e fatti maturare nel tempo.

---

## 2026-05-24 — Revisione task come funzione strutturale di sessione

Generalizzata l'intuizione emersa da `economia`: la revisione dei task non e
solo un adattamento locale per scadenze e pratiche aperte, ma una funzione
strutturale del metodo. Le sessioni LLM pianificano, analizzano e implementano
lavoro attraverso task espliciti; se README e `todo/` driftano, la sessione
parte da una supervisione falsa.

Aggiornati i nodi `task-aperti`, `claude`, `skill` e `struttura-progetto` per
distinguere tra funzione obbligatoria e implementazione locale: ogni progetto
deve avere un controllo leggero dei task nel bootstrap operativo; una skill
dedicata `revisione-tasks` diventa opportuna quando i task sono numerosi,
dipendono da fonti/scadenze esterne o il drift produce costo reale di sessione.

Formalizzata anche la governance dei task metodologici cross-repo: vivono nel
repo `metodo` e di norma hanno precedenza sui task di progetto. Anche quando
targettano un singolo repository, restano centrali finche il motivo del lavoro e
metodologico; un task locale nasce solo quando l'intervento diventa autonomo di
dominio. Di conseguenza la verifica su `nixos`, `bi` e `salute` resta nel task
cross-repo centrale con matrice per repository, mentre `economia` resta il caso
guida gia allineato.

La coda metodologica e stata poi divisa in task centrali specifici per repo:
`osservatorio-bi`, `osservatorio-economia`, `osservatorio-nixos` e
`osservatorio-salute`. Il vecchio task unico di valutazione cross-repo e stato
rimosso per rendere le priorita ordinabili per target senza duplicare lavoro nei
repo adottanti.
