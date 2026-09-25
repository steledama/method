---
ciclo: runtime
---

# Segnale: `aligned` nel marker certifica il recepimento di prescrizioni aperte che nessuno ha verificato

Data: 2026-09-24, integrato il 2026-09-25 · Fonte: battito `/adottanti`
(terzo, arretrato dal 2026-09-01) — marker `i3/allineamento-metodo.md` di
`bi`, `economia`, `crm`; rilettura dei sei dopo i `/method` del 2026-09-25

## Il segnale

La prescrizione `o3/semplificazione-lessico-struttura.md` (nata 2026-08-21)
chiede di togliere `atrio`, `ali` e `stanze` da README, CLAUDE e marker, e di
registrare nel marker le differenze conservate con la loro funzione locale.
Il 2026-09-24, dopo più giri `/method` conclusi con `status: aligned`, il
lessico è ancora in uso vivo in tre repository e nessun marker lo dichiara
come divergenza:

- `bi` — `README.md` («le due ali attraversano il ciclo», «### La legenda
  dell'atrio», «**ali trasversali**»), `CLAUDE.md` («le ali `kb/` e…»,
  «bootstrap (atrio)»); marker `aligned` a `8150997`, rivisto il 2026-09-21;
  il gap era già stato visto il 2026-08-22 e segnalato nel filo
  `audit-adottanti`;
- `crm` — `README.md` («La root è l'atrio dell'artefatto») e la sezione
  `## Bootstrap e atrio` del proprio marker; `aligned` a `5b5e344`, rivisto il
  2026-09-08;
- `economia` — `CLAUDE.md` («le ali trasversali e i register»); `aligned` a
  `8150997`, rivisto il 2026-09-21. Non era stato letto il 2026-08-22.

## Perché non è un caso singolo

Il filo `i3/audit-adottanti.md` teneva l'episodio del 2026-08-22 come
watchpoint, non come filo, perché la guardia dal-basso di
`method-development` chiede un secondo segnale prima di generalizzare. Ora il
secondo segnale c'è, e non è la ripetizione dello stesso: in `bi` il gap è
sopravvissuto a due `/method` successivi alla sua segnalazione; `economia` è
un terzo repository; `crm` lo porta addirittura nel titolo di una sezione del
marker che dichiara `aligned`. Il gap è documentale, cioè proprio ciò che
`aligned` pretende di coprire, non il runtime esterno che
`method-observatory` esclude già.

## Il giro del 2026-09-25

Il giorno dopo la cattura tutti e sei gli adottanti hanno girato `/method`
fino a `eb3f400`, tutti `aligned`. Letti nei file, fuori dai nodi in
symlink, i tre repository del segnale si separano:

- `crm` (`2034b26`) ed `economia` (`d9ecd89`) recepiscono la prescrizione
  e lo nominano nel soggetto del commit («lessico semplificato», «e
  lessico»);
- `salute`, che il lessico non l'aveva, scrive nel marker che le
  prescrizioni aperte del canone «sono state rilette nei file, non solo nel
  delta»;
- `bi` (`afa4702d`) passa `aligned` a `eb3f400` col lessico ancora vivo in
  `README.md`, `CLAUDE.md` e `i2/bi-in-sintesi.md` («la root è l'atrio»). Il
  marker non nomina né la prescrizione né una divergenza: è il terzo
  `/method` che la attraversa senza vederla.

La differenza non sta nel canone ricevuto, che è lo stesso commit per
tutti, ma in cosa ha letto il giro: chi ha riletto le prescrizioni aperte
le ha chiuse, e chi ha letto solo il delta dei commit no. Nessuna skill
chiede la rilettura. `salute` la dichiara come scelta del giro, non come
passo del proprio fork. Restano residui di una frase negli indici
`o3/prescriptions.md` di `nixos` e `crm`, invisibili per lo stesso motivo.

## La domanda da valutare

Il `/method` dell'adottante legge i commit di `method` successivi al proprio
cursore. Una prescrizione nata **prima** del cursore e rimasta aperta esce
dal suo orizzonte: il marker avanza e `aligned` passa a coprirla senza che
nessuno l'abbia riletta. La domanda per i2→i3: `/method` deve **verificare**,
a ogni giro, il recepimento delle prescrizioni ancora aperte in `o3/`
(elencate in `o3/prescriptions.md`), e non soltanto il delta dei commit?
Oppure `aligned` va ristretto in modo esplicito a «delta dei commit
recepito»? Non si decide qui.
