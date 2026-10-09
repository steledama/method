---
ciclo: runtime
---

# Casi della delega: giro di correzioni di `bi`

Data: 2026-10-09 · Fonte: `bi` `i1/casi-delega-2026-10-09-correzioni.md` a
`4867d68c`, commit ancora non pubblicato, letto via SSH nel checkout di
`svezia`; criterio allargato a `4e7d0df2` su `origin`. Acquisiti nella
sessione sul canone del 2026-10-09. Nel repo di origine i casi restano «da
inoltrare» finché il giro locale non li segna «acquisita da method».

## Contesto

Giro di correzioni dopo il primo ciclo con scritture delegate
(`casi-delega-bi-2026-10-09.md`). Il custode ha allargato
`scritture-skill-delegate` alle modalità di correzione e revisione delle due
skill, a condizione che le correzioni siano tracciabili, e ha chiesto una
vista Baserow di controllo. Le righe di seconda scelta vanno collegate al TT
con `bl` sulla riga del fornitore. Cinque commit: tre pubblicati, due locali
perché uno tocca codice in `o3/`.

## I quattro casi

1. **Mandato incollato eseguito senza conferma.** Stessa forma del caso 1
   del primo giro, solo testo incollato senza una riga del custode. Questa
   volta l'agente ha proceduto dichiarandolo in apertura, perché il testo
   citava commit, file e proposte della sessione. Questione dell'adottante:
   la provenienza verificabile dal contesto può sostituire la conferma?
2. **Presidio citato dal criterio ma non ancora esistente.** La vista di
   controllo richiede due campi (valore e firma precedenti, data ordinabile)
   e uno strumento che crea viste: l'agente ha scritto la proposta in
   `o2/vista-controllo-correzioni.md` invece di una vista parziale. Fino
   all'accettazione la tracciabilità promessa dal register è più debole di
   quella dichiarata. Questione: una delega regge se cita un presidio che
   non esiste ancora?
3. **Criterio di skill che richiede codice dell'esecutore.** Per scrivere
   `bl` l'agente ha esteso `valida-corrispondenze.js` con test, ha
   committato senza push, come vuole la regola sul codice in `o3/`, e ha
   usato la versione locale per le 5 scritture. La sessione lavora nel
   checkout di produzione, dove il ciclo notturno fa `git pull --ff-only`.
   Questione: lì il rilascio effettivo è il commit e il push ne diventa la
   pubblicazione; il confine «push = rilascio» presume che il codice viva
   altrove.
4. **Effetto di secondo ordine di link corretti.** Le 20 righe Global
   rilette sono corrette nell'identità, ma il feed Global è fermo al 9
   giugno: i link portano sui TT disponibilità di quattro mesi prima.
   Questione: la verifica dell'atto guarda la riga; il secondo ordine
   richiede di guardare il consumatore.

## Fatti accanto ai casi

- Il custode ha deciso lo stesso giorno di cancellare Global come
  fornitore: è già in blacklist, non manda feed e non si adegua ai flussi.
- Il `git pull --ff-only` dei cron si ferma se `origin` avanza mentre il
  checkout di produzione ha commit non pubblicati.
