---
ciclo: runtime
---

# I casi della delega: dove la delega del ciclo incontra il dominio

La prima lettura dei casi della delega arrivati dagli adottanti dopo la
ratifica di `delega-ciclo` (2026-10-09). Il materiale sono le catture `i1/`
acquisite fino al 2026-10-10: quattro giri di `bi` del 9 ottobre, il primo
ciclo di `crm` su `svezia` e il terzo giro del backup di `baserow`.
`nixos`, `economia`, `salute` e `danea-auto` non hanno inoltrato casi;
`salute` e `danea-auto` lo dichiarano nei propri indici `i1/`. L'assenza
non è un esito: la skill chiede di non produrre casi per completare il giro.

## Provenienza

I conteggi sono misurati qui sulle catture: 18 casi, 15 di `bi`, 2 di
`crm`, 1 di `baserow`. Situazioni, comportamenti e questioni sono dichiarati
dagli agenti degli adottanti; i riscontri del custode sono dichiarazioni
riportate dagli stessi adottanti. Il raggruppamento sotto è
un'interpretazione di questa lettura, non una classificazione degli
adottanti. Tre quinti dei casi vengono da un solo repository in un solo
giorno, con il dominio a più alta densità di scritture delegate.

## Due temi attraversano più di un adottante

**Il checkout è anche una superficie servita.** Quattro casi in due
adottanti: in `bi` il checkout di produzione esegue il codice al commit,
prima del push (giro di correzioni, caso 3; giro su Global, caso 4); in
`crm` il timer delle viste pubblica l'`HEAD` di `svezia`, così il commit
del ciclo diventa una pubblicazione, e il pull di inizio sessione è partito
prima di riconoscere l'host (casi 1 e 2). Senza caso, la stessa condizione
è dichiarata in `baserow`, che tiene su richiesta il pull del checkout
perché i timer eseguono gli script da lì (`5fc585c`), e in `danea-auto`,
dove il Task Scheduler legge il working tree. Il passo 3 della prescrizione
chiusa `pull-autonomo` prevedeva il residuo e lasciava la scelta al
custode; le scelte sono state tre diverse (rilascio che segue il pull in
`crm`, pull su richiesta in `baserow`, push del codice a suite verde in
`bi`), e questo conferma che la decisione è di dominio. Il punto non
coperto è a monte della scelta: riconoscere il checkout prima del primo
atto. L'indizio di `pull-autonomo` per `crm` non nominava il timer delle
viste. Su `deck` le viste di `method`, `nixos`, `salute` ed `economia`
seguono già ogni spostamento di `HEAD`, secondo il contratto di
[view](../kb/view.md), e non hanno prodotto casi: in `crm` l'attrito è
nato perché il register locale escludeva la pubblicazione mentre la delega
includeva il commit che la produce.

**Le conferme richieste si rivelano inutili.** Quattro casi in due
adottanti: in `bi` una conferma su un mandato incollato è arrivata senza
modifiche (primo giro, caso 1) e la volta dopo l'agente ha proceduto
dichiarandolo (giro di correzioni, caso 1); in `crm` entrambe le conferme
sono state giudicate inutili dal custode, che ha subito allargato il
criterio. È il movimento previsto da [consent](../kb/consent.md), «i
criteri partono severi e si allentano coi casi». Non è ancora controprova:
nessuno dei diciotto casi riporta un'autonomia rivelatasi sbagliata con
danno. Gli errori dichiarati sono due: il dry-run concatenato alla
scrittura in `bi`, senza difformità alla rilettura, e il pull di `crm`,
che il custode ha giudicato corretto.

## Temi di un solo adottante, in attesa

- **Tracciabilità e secondo ordine** (`bi`, cinque casi): la verifica
  dell'atto guarda la riga, mentre l'effetto sta nel consumatore; una
  traccia che si sovrascrive non è una traccia; un marcatore ricostruito
  non identifica l'operatore. Sale se un secondo adottante con scritture
  delegate lo incontra.
- **Chi ha deciso cosa** (`bi`, primo giro, caso 2): un commit
  `concordato` che contiene dettagli scelti dall'agente.
- **Criterio di smentita riscritto dopo il dato** (`baserow`): l'agente
  ha evitato sia la smentita alla lettera sia la conferma dal meccanismo
  inferito, ha conservato il criterio vecchio e ha portato la riscrittura
  al custode. Tocca la regola minima del presidio in
  [interpret](../kb/interpret.md) ed è un riscontro di segno favorevole per il
  filo [verdetto più sicuro del materiale](../i3/verdetto-piu-sicuro-del-materiale.md);
  per il canone resta un caso singolo.

## Ipotesi in attesa

- **Ipotesi**: la delega del ciclo presuppone che il checkout non sia una
  superficie servita; dove lo è, il bootstrap deve farlo riconoscere prima
  del primo atto e `autonomy.md` deve nominare quella superficie. La
  proposta di canone è in
  [`o2/delega-nel-checkout-servito.md`](../o2/delega-nel-checkout-servito.md).
  **Orizzonte**: il battito `/adottanti` del 2026-11-01. **Riscontro**: i
  casi inoltrati entro quella data e i bootstrap dei sette letti su
  `origin`. La rafforza un altro caso di atto non riconosciuto su un
  checkout servito; la indebolisce un mese di cicli senza casi su quella
  superficie.
- I temi di un solo adottante si riesaminano allo stesso battito; senza un
  secondo adottante restano adattamenti locali.
