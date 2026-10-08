---
data: 2026-10-05
stato: attiva
ciclo: runtime
target: danea-auto
---

# Rendere raggiungibili le ipotesi in attesa senza presidio

## Cosa e perché

La regola ratificata è: **ogni ipotesi in attesa dichiara orizzonte e
riscontro con fonte, ed è raggiungibile da `eval`**. Vive in
[interpret](../kb/interpret.md), [verdict](../kb/verdict.md) e nello scope
`interpret` della [skill canonica](../.claude/skills/eval/SKILL.md).
La [prova](../i2/presidio-ipotesi-adottanti.md) non giustifica facet `tipo`,
contenitori separati o un presidio nuovo per tutti gli adottanti.

L'intervento serve dove un'ipotesi in attesa non ha già un presidio. Una
collezione senza ipotesi è legittima, come in `baserow`; un filo con criterio,
conteggio e data, come in `nixos`, soddisfa già la regola. La lettura dei nodi
arriva via `method/`; il fork della skill richiede recepimento locale.

## Stato

Recepita da sei destinatari su sette, verificato nei marker e nei file su
`origin` il 2026-10-07: `nixos`, `bi`, `economia`, `salute`, `crm` e
`baserow` a `35a08d5`, ciascuno con l'esito nel marker. Il seguito sul deck
di `nixos` è chiuso: la lettura causale vive in `i2/ipotesi-boot-server.md`,
raggiunta dal filo `affidabilita-boot-server`. Resta `danea-auto`, a
`a344f64`, osservato senza sollecitazione fino al riesame dal 2026-10-13.
Il rinvio è voluto: dal 2026-10-08 il suo marker può avanzare con una riga
neutra che rimanda il recepimento alla sollecitazione di `metodo`, senza
nominare ipotesi né filo; la sollecitazione parte dalla scadenza del plan a
osservazione chiusa. Recepirla prima del giro misurato contaminerebbe
l'osservazione.

## Ricetta per il /method locale

1. Rileggere la regola e adeguare lo scope `interpret` della skill locale:
   riesaminare le ipotesi raggiungibili anche senza nuovi eventi, seguendo
   indici, fili e scadenze del progetto. Correggere l'eventuale rinvio al
   solo `stato` del nodo in `compare`.
2. Dove il presidio manca, dichiarare l'orizzonte (data, evento o battito),
   il riscontro atteso e la fonte; renderli raggiungibili dal giro `eval`.
   Preservare i presidi già sufficienti e i contratti runtime di dominio.
   Dati mancanti o data di riesame trascorsa non risolvono l'ipotesi.
3. Prima di potare un filo che custodisce un'ipotesi in attesa, conservarne
   il presidio in una destinazione esplicita. La chiusura operativa non
   dimostra una causa.
4. Registrare nel marker locale il recepimento o l'adattamento motivato.
   I giudizi sul dominio e le azioni restano del custode dell'adottante.

## Indizi da verificare sul posto

Fotografie della prova del 2026-10-05, da confrontare con i file correnti:

- **economia**, a `84cefbc`: `i2/angolo-nostradamus.md`, profezie 8, 5 e 6.
  Cercare la risposta di Orsi del 13/08, i bonifici del 13/08 e 18/08 e i
  riscontri parziali sulla partecipazione di Carlo, confrontandoli con
  formulazione e criterio originari. «Corroborata» per P8, «mista» per P5 e
  «falsificata» per P6 erano risposte attese della prova, non giudizi sul
  dominio reale: li decide `economia`. L'evento che falsificava P6 era
  costruito, così come la rettifica della fonte di P7; non sono fatti
  avvenuti da importare. Verificare orizzonte, fonte e raggiungibilità delle
  ipotesi ancora in attesa senza copiarne gli esiti sperimentali.
- **nixos**, a `6262067`: il filo `i3/affidabilita-boot-server.md` ha già
  criterio, conteggio e data. Verificare i reboot del 05/10 in
  `i1/manutenzione.json`, raccordare il conteggio con
  `o2/investigate-server-boot-recurrence.md` e dichiarare se un guasto lo
  azzera; il totale corretto lo decide `nixos` sulle sue fonti. La data
  anticipata e la rettifica sul boot di `svezia` erano costruite per la
  prova. Rivedere inoltre la sezione «Affidabilità del boot dei server» del
  deck: conservare il racconto dell'artefatto in `presentation/` e dare una
  casa raggiungibile alla lettura causale, in i2 se necessario, mantenendo
  il presidio già funzionante nel filo. Questo è il seguito sul contenuto
  del deck trasferito da `migrazione-viste`.
- **danea-auto**: il canone osserva senza sollecitarla la scadenza già
  prevista nel filo LibreOffice. L'osservazione e i limiti di attribuzione
  in caso di recepimento anticipato vivono nella
  [lettura della prova](../i2/presidio-ipotesi-adottanti.md#osservazione-aperta-danea-auto).
- **bi, salute, crm, baserow**: distinguere ipotesi in attesa, letture
  esplorative, domande e verifiche operative. Nessuna creazione obbligata di
  ipotesi o file; nessun frontmatter imposto a prodotti JSON o script.

## Verifica e chiusura

Il `/method` locale verifica sui file che ogni ipotesi in attesa incontrata
abbia orizzonte, riscontro con fonte e un percorso effettivamente letto da
`eval`; dichiara anche il caso senza ipotesi e i presidi già sufficienti.
Il battito `/adottanti` controlla marker e file su `origin`, compreso il
seguito sul deck di `nixos`. La prescrizione resta fino al recepimento dei
sette e alla chiusura di quel seguito, senza governarne le code locali.
