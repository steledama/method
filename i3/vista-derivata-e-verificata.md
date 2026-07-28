---
ciclo: dev
---

# Una vista è derivata solo se verificata: il generatore legge le fonti come contratto

Aperto (2026-07-28) dalla valutazione i2→i3 della percezione di `salute` («una
vista derivata mantenuta a mano può invertire l'effetto che cerca», catturata il
2026-07-28, consumata da questo filo).

**Il canone non mancava: mancava il vincolo.** `view` diceva già «vista derivata,
mai seconda fonte» e che il contenuto non si mantiene a mano se esiste una
sorgente canonica. Il deck di `salute` violava una regola già scritta, e nessun
controllo se ne accorgeva: la regola viveva al livello riflessivo — ricordarsi di
aggiornare — e non nella struttura. È la seconda incarnazione della lezione già
incisa in `constraint` col deploy rotto dal rename in `bi`: là nulla forzava
«servito = repo», qui nulla forza «vista = fonte». Ciò che si aggiunge al nodo
non è la regola ma la sua esigibilità: **derivata senza verificata è mezza
garanzia**. Un generatore che trasforma una sola sorgente non può divergere;
quando le sorgenti sono più d'una e possono contraddirsi, o le legge come un
contratto e rompe la build, o produce comunque un output plausibile e falso.

**`metodo` ha la stessa patologia, e se l'è inflitta potando.**
`presentation/tasks.html` è un mazzo **vuoto** dall'11 luglio (commit `25a92d1`):
tre slide → zero, con due task aperti nel plan. Il footer `## Dettagli task`
rimosso quel giorno era un secondo indice per il lettore umano — potarlo era
giusto — ma era anche l'**unica chiave** con cui `o3/presentation.py` legava una
riga del plan al suo file `o2/`. Rimossa la chiave, `build_views.py` fa
`if not row.source: continue` e la vista si svuota in silenzio: diciassette
giorni, mentre l'audit strutturale continuava a riportare 0 problemi su 197
nodi.

Riparato lo stesso giorno, e la riparazione ha precisato il difetto. Non era il
`continue` in sé: il canone ammette una riga di plan senza dettaglio `o2/` («il
file serve _quando serve contesto_», `tasks`), quindi la vista ora la rende con
i soli dati della tabella invece di saltarla. Il difetto era che **nessuno
guardava dall'altra parte**: un file `o2/` che nessuna riga risolve è la
divergenza vera, e ora rompe la build per nome. La risoluzione passa dall'indice
unico `o2/tasks.md` — la chiave che il canone aveva già eletto quando ha abolito
il footer — e il contratto verifica quattro cose: ogni file indicizzato esiste,
ogni file esistente è indicizzato, ogni file è legato a una riga e a una sola, e
il `ciclo` dichiarato nel plan coincide col frontmatter del dettaglio. Verificato
iniettando le quattro violazioni, e sullo stato reale dell'11 luglio: col
generatore nuovo quel plan rende le sue quattro slide invece di zero.

Il reperto corregge anche il verdetto precedente: «potare è fondere, non
cancellare» chiedeva quale copia portasse il fatto più fresco. Qui il contenuto
era fuso correttamente — il fatto viveva già in `o2/tasks.md` — e la potatura ha
rotto lo stesso, perché la copia rimossa aveva un **secondo lettore**, una
macchina. Fondere guarda ai lettori, non solo al contenuto (riga estesa al passo
4 di `verdicts-review`, dove l'atto vive).

**Il drift colpisce il fatto più fresco.** Una vista a mano non degrada in modo
uniforme: diverge dove la sorgente si muove, cioè dove conta. In `salute` l'unico
aggiornamento sostanziale del mese — un esame ritirato su indicazione medica — è
esattamente ciò che il deck non aveva recepito, e per sedici giorni ha continuato
a invitare a chiederlo: il danno non è l'incompletezza ma l'**inversione**. In
`metodo` la vista si è svuotata nell'atto stesso in cui il plan cambiava forma.
Conseguenza operativa: verificare una vista a campione sul contenuto vecchio è il
test sbagliato — si controlla contro l'ultima modifica della fonte.

**Non serve una classe di controllo nuova.** Gli audit strutturali non
attraversano il confine tra una vista e ciò da cui deriva, ed è giusto così: un
generatore che rompe la build **è** già quel controllo, e arriva prima
(`constraint`: il vincolo rende l'azione sbagliata rumorosa, il check riflessivo
può saltare). La domanda utile non è chi controlla le viste, ma **quali viste non
sono ancora generate** e, tra quelle generate, quali derivano da più fonti senza
verificarle. In `metodo` le quattro viste di `presentation/` sono tutte generate;
`tasks.html` è l'unica a fonti multiple (tabella del plan × file `o2/`) ed è
appunto quella che ha ceduto. La home è a sorgente-per-sezione — collega le
collezioni, non le rende — e sull'unico input che legge davvero, l'H1 del
`README`, rompeva già: non può divergere, e la riga di `view` che la diceva
derivata dal plan è stata corretta.

**Il costo del drift ordina, non classifica.** Su `salute` una vista stale
invitava a un esame che un medico aveva ritirato; su altri domini sarebbe rumore.
L'asimmetria non produce due regole né una tassonomia di viste per danno: la
regola resta una — una vista si genera, e se ha più fonti le verifica — mentre il
costo di dominio decide l'**ordine** in cui le viste ancora a mano vengono
convertite.

**La difformità di una fonte può essere un secondo significato.** Il parser di
`salute` è inciampato su un file-area su otto che dichiarava una `Riapertura`
invece della coppia `Prossima azione`/`Entro`: normalizzarlo alla forma
maggioritaria avrebbe distrutto la distinzione tra area _dormiente_, che aspetta
un trigger, e _attiva_, che aspetta una data — la stessa che `plan` fa tra una
scadenza e una pausa con condizione di risveglio. Il contratto ammette entrambe
le forme invece di imporne una. È «fondere, non cancellare» su un secondo asse:
là copia contro copia, qui schema contro fonte. Due assi diversi, la stessa
assunzione implicita — che il difforme sia il difettoso. Resta nominato qui e
nella forma view-specifica in `view`; se compare un terzo asse, sale a nodo
proprio.

**Il filo non ha bisogno di un campo nuovo.** La domanda era se un filo che
valuta un artefatto composto — fonte più superficie che la rende — debba
dichiarare quale dei due sta misurando. No: un verdetto è sulla fonte di verità,
e una superficie che può essere falsa della propria fonte è un difetto della
superficie, non una dimensione mancante del filo. Generata e verificata la vista,
la distinzione collassa. Si riaprirebbe solo per una superficie che **non si può**
generare — fuori dal repo, mantenuta da altri: caso oggi non presente in nessuno
dei quattro.

Watchpoint: i campioni di generatore-contratto sono due — `salute` (quadro
corporeo) e `metodo` (plan × `o2/`) — e convergono sulle stesse tre verifiche:
indicizzazione, coerenza dei valori dichiarati due volte, varianti ammesse
invece che appiattite. Convergenza non ancora sufficiente a incidere in `view` la
forma del contratto oltre l'elenco di esempi: serve il terzo, e nessuna
prescrizione `o3/` parte prima — la modifica è puntuale e viaggia col normale
`method-review`.

Il terzo caso non si va a cercare: un caso cercato dimostra che il pattern
esiste, non che la generalizzazione serve, e il dal-basso è la guardia contro la
sovra-ingegnerizzazione. Ma il non-cercare vale per il canone, non per il
runtime: due campioni su due esaminati — `nixos`, `bi` ed `economia` non li ha
guardati nessuno su questo asse — e il costo di una vista che inganna matura in
silenzio proprio dove nessuno guarda. L'inventario «quali viste non sono
generate» perciò non resta appeso a questa riga: è la quinta lente di
`/adopters-review` (superfici e viste), dentro il battito mensile che già esiste
invece che in un atto nuovo. Se fosse restato un rimando in prosa sarebbe stato
lo stesso difetto che questo filo denuncia — una regola al livello riflessivo
invece che nella struttura.
