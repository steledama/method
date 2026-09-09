---
ciclo: dev
---

# Segnale: l'elenco o3 eredita la domanda di i1 per analogia strutturale, ma nessuno ha mai chiesto a quale domanda la card o3 della home deve rispondere

Data: 2026-09-09 · Fonte: nixos — `presentation/index.html` (slot o3),
`presentation/prescriptions.html`, `o3/prescriptions.md`, generati da
`o3/build_lists.py` (canone `2891892`); riscontro anche nell'artefatto di
`metodo` stesso (vedi sotto)

## Il segnale

`kb/view.md` fissa il criterio: «la forma segue la domanda» — elenco, tabella,
slide, canvas sono forme alternative scelte secondo cosa una pagina deve far
capire o decidere, non intercambiabili per convenienza implementativa. Quando
`build_lists.py` è stato esteso da `i1/perceptions.md` a `o3/prescriptions.md`
"per lo stesso pattern" (il commit `2891892` lo dice: «stesso pattern già
portato per `tasks.html`»), l'estensione ha portato la _forma_ — elenco
puntato della coda sotto `## Contenuti` — senza riportare la _domanda_ a cui
quella forma risponde in i1 («cosa è arrivato dal Mondo e non ho ancora
interpretato?»), e senza chiedersi se sia la domanda che la card o3 della home
pone.

In `nixos` non lo è. La card o3 di `presentation/index.html` ha didascalia
«Dichiarazione runtime e strumenti deterministici del Perform» — non
«prescrizioni narrative ancora da eseguire». Chi legge quella didascalia e
clicca si aspetta la mappa di cosa _è_ lo stadio o3 in questo artefatto (host,
moduli, skill, strumenti — la sostanza dichiarata in `## Dichiarazione
runtime`/`## Strumenti`/`## Skill` dello stesso file sorgente), non la coda di
ciò che _resta da fare_. Riceve invece «Nessun elemento aperto.» — corretto
rispetto alla domanda di i1, sbagliato rispetto alla domanda che la propria
card ha posto.

**Lo stesso scarto esiste in `metodo`, solo mascherato.** La card o3 della
home canonica recita «Prescrizioni **ed esecutori deterministici** del
metodo», ma `prescriptions.html` — generato dallo stesso `build_lists.py` —
rende solo il blocco `## Contenuti` (oggi 4 prescrizioni aperte verso gli
adottanti); la sezione `## Strumenti` che la card cita esplicitamente
(`kb_tools.py`, `build_views.py`, `build_lists.py`, `build_system_image.py`...)
non compare mai nella vista. Non si nota perché la coda non è vuota — ma il
meccanismo che produce lo scarto è identico, ed è nell'artefatto canonico
stesso, non in un adattamento locale di un adottante.

## A cosa serve la presentazione, e per chi

`kb/cognitive-artifact.md` / `kb/system-image.md`: l'artefatto è l'unico
canale attraverso cui due menti che non si parlano — il custode nel tempo, e
chi si avvicina per la prima volta — costruiscono comprensione. «Quando il
system image è incoerente, incompleto o contraddittorio, l'utente non riesce a
usare il sistema.» `presentation/` è il punto di massima esposizione di questo
principio: è la superficie che un lettore _senza contesto pregresso_ incontra
per primo, prima di aver aperto un solo nodo KB (`kb/presentation.md`: «un
lettore che non ha il checkout»). Le sue pagine non possono assumere il
lettore-abitante — chi già sa che «prescrizioni», in questo progetto, significa
solo la coda narrativa; devono valere anche per il lettore-ospite, per cui la
didascalia della card è l'unica promessa disponibile.

Né `kb/view.md` né `kb/presentation.md` dichiarano, oggi, un pubblico o una
domanda per pagina. `view.md` tiene la disciplina della derivazione (a quali
obblighi una vista risponde una volta scelta la forma) e afferma il principio
generale «la forma segue la domanda»; `presentation.md` tiene la
materializzazione (formato, build, modo in cui raggiunge il lettore). Nessuno
dei due è il luogo dove la domanda-per-pagina — e il suo pubblico — si
registrano esplicitamente prima di scegliere la forma. La domanda che questo
segnale solleva non è «il parsing di `## Contenuti` è corretto?» (lo è, per la
domanda di i1) ma: **la presentazione ha un pubblico dichiarato e una domanda
dichiarata per ciascuna delle sue pagine, o li eredita per analogia strutturale
dalla pagina precedente?** Oggi la seconda. `index.html` sembra scritto per il
lettore-ospite (didascalie che spiegano cosa _è_ ogni stadio); le viste-elenco
sono scritte per il lettore-abitante (cosa resta _aperto_, la stessa lente di
un backlog). Le due lenti sono entrambe legittime — ma sono diverse, e finché
la scelta resta implicita, ogni pagina generata "per lo stesso pattern"
rischia di riportare la lente sbagliata, come qui, due volte, in due
artefatti diversi.

## Perché tenuto separato da `intestazione-coda-build-lists-non-uniforme.md`

`bi` ha aperto oggi stesso, sullo stesso generatore, un segnale imparentato:
il nome fisso `## Contenuti` non è un contratto uniforme fra collezioni (coda
vera in `o2/tasks.md`, panoramica strutturale statica in
`o3/prescriptions.md`/`i2/interpretations.md` di `bi`), e propone di
parametrizzare il nome della sezione per pagina. Non lo fondo qui come secondo
caso dello stesso attrito perché opera un livello sotto e resta valido anche
se questo si risolve: parametrizzare il nome della sezione risponde a _dove_
si legge la coda, non a _quale domanda_ la pagina generata deve rispondere né
_per chi_. Applicato il fix di `bi`, la card o3 di `nixos` e di `metodo`
continuerebbero a promettere più di quanto l'elenco puntato — qualunque sia il
nome della sua sezione sorgente — possa mai mostrare. Sono attriti imparentati
(stesso generatore, stesso giorno, stessa estensione `2891892`) ma non lo
stesso attrito: fonderli rischia di far passare il secondo (parametrizzazione
del nome) per soluzione anche del primo (domanda e pubblico dichiarati), che
nessun fix di parsing tocca.

## Perché non è generalizzato qui

Un solo adottante ha scritto questo segnale (nixos), ma la sua seconda
istanza — non dichiarata da nessuno finora — è già visibile nell'artefatto
canonico stesso. Non è chiaro se la soluzione sia: dichiarare pubblico e
domanda per pagina in `view.md` o `presentation.md`; comporre, per le card che
promettono più della coda, una vista che unisca coda aperta e mappa
strutturale; oppure ridurre la promessa delle card (`o3` in entrambi gli
artefatti) a ciò che l'elenco può davvero mantenere. Nessun verdetto qui — i1
è valenza-neutro: la scelta fra queste vie, e se generalizzare subito visto
che il canone stesso già la esibisce, è i2→i3, giudizio del custode.
