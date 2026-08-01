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

**`bi` è il terzo repo, e il contratto ha pagato al primo contatto.** Il
`method-review` di `bi` (2026-07-29, marker a `b42164c`) ha trovato nel proprio
fork del generatore lo stesso guasto silenzioso: dal 7 luglio, quando il suo plan
è passato all'indice unico, **nessuna** delle undici righe risolveva più al
proprio `o2/` e la vista dei task era vuota da tre settimane. Tre repo su cinque,
stessa dinamica, sempre invisibile agli audit strutturali. Portato il contratto,
ha intercettato subito una divergenza reale che nessuno aveva visto — un task
intitolato «Completare la famiglia…» in `o2/` contro «Completare famiglia…» nel
plan e in due fili `i3/` — poi allineata.

**`nixos` è il quarto, e ha pagato la stessa moneta.** Il suo `method-review`
(2026-07-29, intervallo `6133ace..b42164c`, marker a `b42164c`) ha recepito il
contratto e nell'atto ha scoperto la propria incarnazione del guasto: anche lì
la potatura del footer aveva tolto l'unica chiave, il generatore locale faceva
`continue` in silenzio, e `presentation/tasks.html` era fermo al 10 luglio senza
il task aperto il 20 — **diciannove giorni** con audit, fidelity e `check.sh`
verdi per tutto il periodo. Quattro repo su cinque, stessa dinamica. Il contratto
ha poi intercettato tre righe del plan col titolo divergente dal proprio file
`o2/`, per una delle quali l'indice portava una **terza** variante: la stessa
classe di divergenza trovata in `bi`, e il secondo adottante su due a pagarla al
primo contatto.

**Un vincolo che arriva tardi è anche un rilevatore.** Ratificato il 2026-07-29
dalla valutazione i2→i3 della percezione «il recepimento di un vincolo fa
emergere il drift che era già lì» (2026-07-29, da `nixos`, consumata qui).
`constraint` diceva il vincolo solo in avanti — rende l'azione sbagliata
impossibile o rumorosa — e così si legge come pura prevenzione, il cui valore si
misura in errori che non accadranno. Installarlo dove c'è già storia fa una
seconda cosa: al primo giro non previene, **rivela**, e ciò che rivela è il drift
maturato nel tempo in cui non c'era. Il tempo silenzioso ne è la misura — tre
settimane in `bi`, diciannove giorni in `nixos`, diciassette in `metodo` — ed è
anche la risposta a chi legge il recepimento come costo: quel lavoro non nasce
col vincolo, diventa solo esigibile. Il canone si allunga di una riga in
`constraint`, dove la regola già vive; `view` non cambia, perché il fatto non
riguarda le viste ma i vincoli in generale.

**Il canale del canone ha battuto il battito.** L'inventario delle viste era
stato affidato alla quinta lente di `/adopters-review` dell'11 agosto, e `nixos`
era uno dei due repo che quella lente doveva ancora guardare: ci è arrivato prima
il `method-review` dell'adottante, alla propria cadenza. Non è un difetto del
battito né una ragione per spostare la lente: le due vie hanno soggetti diversi —
il canone che scende, l'audit che guarda — e la ridondanza è precisamente ciò che
ha preso il caso. Conseguenza sullo scope: alla lente 5 dell'11 agosto resta
`economia` sola su questo asse.

Il trigger del watchpoint è quindi scattato, ma la conseguenza **non** è
trascrivere in `view` la forma del contratto. `bi` non è una terza invenzione
convergente: è un port, e la forma vive già in un'implementazione versionata che
gli adottanti forkano (`check_plan_contract` in `o3/presentation.py`). Metterla
anche in prosa sarebbe una seconda rappresentazione dello stesso fatto — l'errore
che questo filo intero denuncia. Il nodo tiene il principio, il codice tiene la
forma (cfr. `skill`: le skill sono interfacce sugli strumenti versionati, non
documentazione).

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

Watchpoint chiuso sul contratto: le invenzioni indipendenti restano due —
`salute` (quadro corporeo) e `metodo` (plan × `o2/`), convergenti su
indicizzazione, coerenza dei valori dichiarati due volte e varianti ammesse
invece che appiattite — e `bi`, `nixos` e `salute` stessa ne sono i
recepimenti, arrivati col normale `method-review` senza bisogno di una
prescrizione `o3/`. `salute` è la quinta istanza della stessa dinamica
(2026-08-01, `e6d6f28`): il suo `parse_plan` era codice morto, importato da
nessun generatore, quindi nulla legava una riga del plan al suo file — il
recepimento l'ha cablato nel generatore della home e il contratto ha rotto la
build al primo giro su una divergenza reale di titolo (H1 di `o2/` contro
riga del plan), il terzo adottante su tre a pagarla al primo contatto. Resta
`economia`: il suo `method-review` del 2026-08-01 ha eseguito i tre
entrypoint trovando le viste **fresche** — l'obbligo di freschezza è a posto —
ma nessun giro ha ancora esercitato il **cablaggio del contratto** nel suo
fork, l'unico asse su cui i tre adottanti hanno pagato al primo contatto.
Resta alla lente 5 del battito di settembre.

**Due obblighi, non uno.** Ratificato il 2026-07-29 dalla valutazione i2→i3 della
percezione «una vista generata può essere stale senza che nulla diverga»
(2026-07-29, da `economia` e `bi`, consumata qui). Una vista derivata deve essere
coerente con le fonti **e** non più vecchia delle fonti. Il contratto copre il
primo obbligo e non può coprire il secondo per costruzione: gira quando gira il
generatore, e il difetto è che il generatore non è più stato eseguito. La home di
`economia` era ferma da cinque giorni e tre commit del proprio register — le
mancava il criterio con cui quel register dice di giudicare ogni scelta — e
`verdict.html` di `bi` era stantia **mentre** una sessione di manutenzione girava
sul repo: è l'argomento più duro contro il presidio riflessivo, perché lì
qualcuno stava attivamente guardando.

**Rigenerare, non descrivere.** La strada che sembrava ovvia — dichiarare le
fonti di ogni vista in un manifesto e confrontare i timestamp — è stata scartata:
il generatore le fonti le conosce già, e un elenco parallelo sarebbe la seconda
rappresentazione che diverge, cioè l'errore che questo filo denuncia. Scartarla
scioglie anche la domanda sul glob: senza manifesto, una vista a fonti nominate e
una che le raccoglie con un pattern si comportano allo stesso modo. Resta
rigenerare, e la determinismo già canonica rende il prezzo quasi nullo — misurato
qui: 1,1 secondi per le quattro viste, e `git status` vuoto quando le fonti non
si sono mosse. Il check i2 del gate `/commit` smette perciò di essere un giudizio
(«è cambiato il significato?») e diventa un gesto: esegui la build, leggi `git
status`, ciò che compare **era** stale. Il giudizio resta solo dove la build non
arriva, cioè su una sintesi `i2/` il cui significato è cambiato davvero.

Onestà sul livello raggiunto: è un check reso meccanico, non una forcing
function. Il vincolo vero sarebbe un hook, e resta fuori per una ragione di
principio e non di pigrizia — richiede installazione host-locale, stato non
versionato dentro un artefatto che si vuole portabile, ed è la via che in `bi` si
era già rotta in silenzio dopo un rename. La vista versionata è quindi un
artefatto con un debito: si versiona perché deve aprirsi dal checkout, e si paga
rigenerandola nell'atto che tocca le fonti.

**Il modo del ritrovamento ha tarato il rimedio.** Nessuna delle due istanze è un
danno subito: una viene da un'ispezione deliberata, l'altra è emersa dentro
un'altra revisione. Un segnale così licenzia il rimedio più economico che
l'avrebbe intercettato — un comando nel gate — e non un manifesto, una classe di
check nuova o un'infrastruttura di hook. La regola è salita a canone in
`method-development`, dove già vive la guardia contro la sovra-ingegnerizzazione:
lì diceva _se_ rispondere, ora dice anche _quanto_.

Watchpoint: se una vista stale passa comunque un commit dopo questa modifica del
gate, il check meccanico non basta e l'escalation è il vincolo vero — a quel
punto il costo dell'installazione host-locale va ridiscusso contro la
portabilità, non dato per perso in partenza. Negli adottanti il debito è
saldato: `bi` l'aveva già pagato una volta, ed `economia` l'ha chiuso col
`method-review` del 2026-08-01 — i tre entrypoint eseguiti nel gate, home e
fotografia già fresche, `git status` vuoto su di esse. Il check meccanico ha
retto al primo giro reale in tre repo su tre.

Il terzo caso non si va a cercare: un caso cercato dimostra che il pattern
esiste, non che la generalizzazione serve, e il dal-basso è la guardia contro la
sovra-ingegnerizzazione. Ma il non-cercare vale per il canone, non per il
runtime: quattro campioni su quattro esaminati, e sul solo `economia` nessuno
ha ancora guardato l'asse del contratto (la freschezza sì, col giro del
2026-08-01) — il costo di una vista che inganna matura in silenzio proprio
dove nessuno guarda. L'inventario «quali viste non sono
generate» perciò non resta appeso a questa riga: è la quinta lente di
`/adopters-review` (superfici e viste), dentro il battito mensile che già esiste
invece che in un atto nuovo. Se fosse restato un rimando in prosa sarebbe stato
lo stesso difetto che questo filo denuncia — una regola al livello riflessivo
invece che nella struttura.
