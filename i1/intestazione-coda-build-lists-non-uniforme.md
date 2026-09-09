---
ciclo: dev
---

# Segnale: `build_lists.py` assume `## Contenuti` come nome fisso della coda, ma un'intestazione fissa non regge in un repo dove lo stesso nome ha già un altro significato

Data: 2026-09-09 · Fonte: bi — `o3/prescriptions.md`, `i2/interpretations.md`,
`i1/perceptions.md`, nel recepire il commit `2891892`
(`o3/build_lists.py`)

## Il segnale

`build_lists.py` legge, per ogni pagina configurata, il blocco puntato sotto
l'intestazione `## Contenuti` di un indice di collezione e lo rende come coda
di item aperti — la stessa forma di `o2/tasks.md`. L'intestazione è una
costante fissa nel modulo (`_CONTENUTI`), non un parametro per pagina.

In `bi` `## Contenuti` non ha semantica uniforme fra le collezioni: in
`o2/tasks.md` è davvero una coda di task aperti (stesso pattern del
canonico), ma in `o3/prescriptions.md` e in `i2/interpretations.md` la stessa
intestazione introduce una panoramica strutturale statica della collezione —
pochi bullet stabili, non un elenco che cresce e si svuota. Applicare il
generatore così com'è a `o3/prescriptions.md` avrebbe reso una vista
fuorviante (i bullet strutturali presentati come prescrizioni aperte).
`i1/perceptions.md` di `bi`, all'opposto, non ha affatto un'intestazione
`## Contenuti` — l'avrebbe fatto uscire con `SystemExit` — ma ha una sezione
`## Catture versionate` che è, semanticamente, esattamente la coda che il
generatore assume (una cattura resta finché non è interpretata, poi si
elimina — lo stesso ciclo di `perceive.md`), solo sotto un nome diverso
perché `## Contenuti` in quel file è già preso da una sezione diversa e
strutturale (`## Substrato runtime i1`).

## L'attrito osservato

`bi` ha risolto localmente parametrizzando l'intestazione della coda per
pagina nel proprio fork (`PAGES` porta un quarto campo, il nome della
sezione, invece della costante fissa) e applicando il generatore solo a
`i1/perceptions.md → ## Catture versionate`; `o3/prescriptions.md` resta
fuori, senza vista generata (nessun contenuto versionato "prescrizione
ancora da eseguire" distinto dagli strumenti stabili che il suo
`## Contenuti` già elenca).

**Aggiornamento, stesso giorno.** Il primo giro sopra trattava ancora "coda di
item aperti" come l'unica domanda legittima per queste pagine — la stessa
lente che il segnale gemello `presentazione-domanda-e-pubblico-non-dichiarati.md`
(`nixos`) nomina esplicitamente. Applicata quella lente fino in fondo, `bi` ha
poi esteso `PAGES` da un'intestazione singola a una **lista di sezioni per
pagina**: `prescriptions.html` ora rende `## Contenuti` di
`o3/prescriptions.md` (la panoramica strutturale, non una coda — coerente con
la card home «prescrizioni, strumenti e gli esecutori del runtime di
dominio»); `perceptions.html` rende sia `## Substrato runtime i1` sia
`## Catture versionate`, struttura stabile e coda aperta nella stessa pagina,
nell'ordine della fonte. Riportato qui perché è dato empirico utile al
giudizio del custode su entrambi i segnali — non una generalizzazione: resta
un solo adottante che ha implementato questa via, una delle più elencate in
`presentazione-domanda-e-pubblico-non-dichiarati.md`, non necessariamente la
giusta per `metodo` o per `nixos`.

Resta aperta la domanda più ampia: `## Contenuti` come nome fisso per "la
coda di item aperti di uno stadio" è un'assunzione valida perché finora
`method` stesso è l'unico adottante che l'ha esercitata con questo
generatore, o il contratto giusto è già "un'intestazione dichiarata dal
generatore per pagina" — nel qual caso converrebbe parametrizzarla anche nel
canonico, non solo nel fork.

## Perché non è generalizzato qui

Il caso è uno solo (`bi`, due collezioni sullo stesso generatore). Non basta
a distinguere se l'ipotesi giusta sia "il nome fisso resta valido, `bi` è
un'eccezione locale" oppure "l'intestazione va sempre parametrizzata nel
canonico" — serve un secondo adottante con lo stesso attrito prima di
generalizzare. Nessun verdetto qui: i1 è valenza-neutro.
