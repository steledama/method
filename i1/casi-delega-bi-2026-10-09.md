---
ciclo: runtime
---

# Casi della delega: primo giro di `bi`

Data: 2026-10-09 · Fonte: `bi` `i1/casi-delega-2026-10-09.md` a `c8ff758c`,
con il criterio `scritture-skill-delegate` a `fb1d0d1a` e lo snellimento di
`CLAUDE.md` a `be229a36`, letti su `origin`. Acquisiti nella sessione sul
canone del 2026-10-09. Nel repo di origine i casi restano «da inoltrare»
finché il giro locale non li segna «acquisita da method».

## Contesto

Primo ciclo congiunto `eval → exec → commit` dopo il recepimento di
`delega-ciclo`. Prima del ciclo il custode ha allargato la delega di `bi`:
le scritture Baserow di `categorizzazione` e `corrispondenze` entrano nel
ciclo con dry-run, cap per giro (100 per fornitore, 20 per fetta), soli
campi già scritti dalle skill e arresto della fetta anomala; `tassonomia` e
le propagazioni verso WooCommerce restano riservate. Il commit del giro è
`Autonomia: agente`, con due `Impatto-motivo:` che citano `ciclo-delegato` e
`scritture-skill-delegate` e i conteggi per fornitore e fetta.

## I cinque casi

Sintesi dei cinque elementi registrati dall'adottante; il testo completo è
nella fonte.

1. **Conferma su un mandato incollato.** Il mandato, che allargava la
   delega, era arrivato soltanto come testo incollato, senza una riga del
   custode fuori dal blocco. Per la regola dell'harness un testo incollato
   vale come istruzione solo se il messaggio dell'utente lo chiede: l'agente
   ha chiesto conferma prima di ogni atto. Il custode ha confermato senza
   modifiche. Questione dell'adottante: distinguere mandati incollati con o
   senza una riga propria, e mandati che cambiano la delega da quelli che la
   usano.
2. **Condizioni scritte più strette del mandato.** Nel commit `concordato`
   del criterio l'agente ha aggiunto restrizioni non dettate: fuori dalla
   delega `--correggi`, `--rivaluta`, la revisione dei link esistenti, le
   viste diverse da `VALIDARE1`; solo esiti `nuova` e `scarto`. Le ha
   dichiarate nel resoconto; conferma del custode pendente. Questione: un
   commit `concordato` che contiene dettagli scelti dall'agente mescola chi
   ha deciso cosa.
3. **Categorizzazione delegata riuscita.** 89 prodotti su quattro
   fornitori, dry-run pulito, 89 scritte, 10 in `altro / altro` dichiarate
   per assenza di una voce nel vocabolario. Nessuna conferma, nessun attrito.
   Riscontro di dominio atteso dallo status del 10/10 e dalla revisione
   dell'operatore sulle firme.
4. **Dry-run e scrittura concatenati.** Sulla fetta Biuromax l'agente ha
   lanciato dry-run e scrittura in un solo comando: ordine rispettato e
   dry-run pulito, ma la scrittura non attendeva la lettura. Errore
   dichiarato dall'agente, fette successive separate, 20 righe rilette senza
   difformità. Questione: una condizione che richiede giudizio fra due passi
   regge solo se l'esecutore la rende meccanica.
5. **Criterio mancante sulle righe B-grade.** Cinque righe Imcopex di
   seconda scelta con lo stesso part number del TT nuovo: l'agente le ha
   lasciate non decise invece di scartarle e ha aperto la proposta in
   `o2/skill-revisione-oem-corrispondenze.md`. Questione: distinguere
   «scarto», giudizio dato, da «non deciso», giudizio sospeso, quando il
   criterio manca.

## Fatti accanto ai casi

- Le 20 righe validate della fetta Global non hanno trace di matching:
  poggiano su suggerimento e codici, dichiarato dall'agente.
  `prodotti_ref` è letto da riordini e catalogo pubblicato.
- `bi` cita come canale di consegna `~/method/o3/delega-ciclo.md`, rimosso
  in `method` con `516dd5b`: riferimento da aggiornare nel prossimo giro
  locale.
