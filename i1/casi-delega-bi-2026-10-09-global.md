---
ciclo: runtime
---

# Casi della delega: giro di `bi` su Global, feed e correzioni

Data: 2026-10-09 · Fonte: `bi` `i1/casi-delega-2026-10-09-global.md` a
`c4e9b84a`, con i commit da `eb333ae5` a `a01e6f53`, letti su `origin`.
Acquisiti nella sessione sul canone del 2026-10-09. Nel repo di origine i
casi restano «da inoltrare» finché il giro locale non li segna «acquisita da
method».

## Contesto

Terzo giro di `bi` del 9 ottobre. Il custode ha autorizzato il push dei
commit di codice dopo i test, deciso l'uscita del fornitore Global e chiesto
di metterne in `bl` le righe rimaste fuori, accettato la vista di controllo
delle correzioni con la sospensione delle modalità di correzione fino alla
sua entrata in esercizio. La vista `CORREZIONI` è in esercizio e la
sospensione è tolta (`a01e6f53`).

## I quattro casi

1. **Premessa del custode smentita dalla scala.** Il mandato diceva Global
   «già in blacklist»; le righe senza `bl` erano 1.090 su 1.090. L'agente ha
   proceduto perché il mandato copriva «quelle che non lo sono» e il fine
   era netto, con fotografia preliminare dei TT, dry-run e rilettura, e ha
   dichiarato lo scarto. Questione dell'adottante: un salto di ordini di
   grandezza rispetto alla premessa va riportato prima dell'atto o dopo?
2. **Secondo ordine evitato restando nel perimetro.** Con `bl`, 373 righe
   Global con `wl1` attivo diventano il paradosso `wl`+`bl`, che lo
   strumento di pulizia risolve togliendo `wl` e quindi togliendo dal
   catalogo i TT di cui Global è l'unica whitelist. L'agente ha scritto solo
   `bl` e avvertito di non lanciare la pulizia. Questione: una regola di
   pulizia generica può trasformare uno stato d'attesa voluto in una
   decisione non presa da nessuno.
3. **Backfill limitato a ciò che le tracce provano.** Le tracce provano 4
   correzioni, rimozioni Axro del 2/10 su link con firma vuota, che il
   backfill marca «manuale» (`casi-delega-bi-2026-10-09-attuazione.md`); le
   1.340 correzioni di categoria passate non hanno precedente, perché la traccia
   si sovrascrive e il backup non salva `categoria_auto`. Questione: una
   traccia che si sovrascrive non è una traccia; la tracciabilità su cui si
   regge la delega va verificata sulla conservazione, non solo sulla
   scrittura.
4. **Push dove il commit è già il rilascio.** Pubblicazione dopo l'intera
   suite verde. Conferma il caso 3 del giro di correzioni: la distinzione
   fra rilascio e pubblicazione dipende dal ruolo dell'host.

## Fatti accanto ai casi

- `feedHealth` lasciava `unknown` un fornitore senza tentativi registrati e
  non lo escludeva mai, anche in `enforce`: è il varco da cui è passato
  Global. La proposta di chiuderlo è in `o2/freschezza-feed-fornitori.md`.
- Il backup granulare non salva `categorizzazione`, `correzione_precedente` e
  `corretto_il`: una riga ricreata dal sync perde la traccia della correzione.
