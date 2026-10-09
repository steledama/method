---
ciclo: runtime
---

# Casi della delega: giro di attuazione di `bi` dopo Global

Data: 2026-10-09 · Fonte: `bi` `i1/casi-delega-2026-10-09-attuazione.md` a
`e110e9d0`, con `e236d661`, `0c676918` e `92722e8e`, letti su `origin`; schede
in `i1/rimozioni-axro-2026-10-02.md` ed elenco in
`i1/fonti-alternative-global-2026-10-09.md`. Acquisiti nella sessione sul
canone del 2026-10-09. Nel repo di origine i casi restano «da inoltrare»
finché il giro locale non li segna «acquisita da method».

## Contesto

Quarto giro di `bi` del 9 ottobre: alternativa B per l'uscita di Global,
ricerca di fonti alternative per i TT rimasti scoperti, chiusura del varco
`unknown` di `feedHealth`, backup esteso ai campi di correzione con
ripristino di prova isolato, schede delle quattro rimozioni Axro per la
revisione del custode.

## I due casi

1. **Una fonte trovata non basta a ripristinare la disponibilità.** Sui 62
   TT esaminati l'agente ha scritto tre nuovi link Biuromax certi ma senza
   stock e due scarti; nessun TT ha recuperato disponibilità. Due TT hanno
   già stock Axro ma `wl2` solo da Global, che il criterio delegato non
   autorizza a scrivere. Questione dell'adottante: una richiesta di recupero
   va verificata sull'esito del consumatore, distinguendo nuova relazione,
   stock e autorizzazione di dataset.
2. **Il marcatore «manuale» non identifica l'operatore.** Le quattro
   rimozioni Axro hanno `correzione_precedente` con firma «manuale», ma le
   preimmagini conservano una firma vuota: «manuale» è il marcatore
   ricostruito dal backfill per una decisione non firmata, non l'identità né
   la data di chi l'aveva presa. Questione: distinguere il fatto conservato
   dal marcatore convenzionale di provenienza quando si prepara la revisione
   umana.

## Fatti accanto ai casi

- Le schede mostrano per tutte e quattro un toner originale collegato a un
  tamburo o a un TT di altra natura, con il TT toner originale assente.
- Il ripristino di prova recupera i tre campi di traccia su una riga
  ricreata con ID diverso; `crea-campi-correzione.js` è versionato in
  `o3/utility/`.
