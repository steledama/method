---
ciclo: runtime
---

# I casi della delega: dove la delega del ciclo incontra il dominio

La prima lettura dei casi della delega arrivati dagli adottanti dopo la
ratifica di `delega-ciclo` (2026-10-09). Il materiale sono le catture `i1/`
acquisite fino al 2026-10-10: quattro giri di `bi` del 9 ottobre, il primo
ciclo di `crm` su `svezia` e il terzo giro del backup di `baserow`. I
casi dei primi giri autonomi di `bi` (2026-10-17) e di `baserow`
(2026-10-16, inoltrati il 2026-10-19) e quello di `danea-auto` del
2026-10-15, inoltrato il 2026-10-19, sono letti a parte, sotto, e non
entrano nei conteggi.
`nixos`, `economia` e `salute` non hanno inoltrato casi; `salute` lo
dichiara nel proprio indice `i1/`. L'assenza
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

## Nel giro autonomo: il testo del giro chiede ciò che il recinto nega

Quattro casi in due adottanti, tutti al primo giro autonomo: in `bi` il
bootstrap chiede di rileggere il marker di ruolo e `ciclo.json` ne nega la
lettura ([cattura](../i1/casi-delega-bi-2026-10-17.md)); in `baserow` il
prompt elencava `ls -l backup/` che l'allowlist negava, la skill canonica
chiedeva il pull d'avvio che prompt e register riservavano al custode, e un
filtro in pipe è stato negato a pezzi
([cattura](../i1/casi-delega-baserow-2026-10-16.md)). Accanto, senza caso
inoltrato, il primo giro di `method` ha avuto letture motivate dal prompt e
negate dal perimetro (`o2/pilota-ciclo-autonomo.md`). In ogni caso l'agente
ha preso il diniego come confine e l'ha dichiarato; il costo è stato in turni
e in letture perse, non in atti fuori delega. Le correzioni sono tutte
locali e a mano: togliere dal prompt, concedere in `ciclo.json`, dichiarare
nel prompt l'elenco che `ciclo.json` già contiene. Interpretazione di questa
lettura: due testi scritti a mano dello stesso perimetro divergono al primo
giro, e il primo giro di prova è oggi il solo confronto. Dal 2026-10-19
`tentativi.jsonl` conta i `dinieghi` per giro (`nixos` `60c2314`), una misura
della divergenza leggibile senza trascritto. Il custode ha deciso il 2026-10-19 due
correzioni del canone: la prescrizione `ciclo-autonomo` (chiusa il 2026-10-28)
chiede i comandi del prompt alla lettera in `ciclo.json` e un giro di prova
senza dinieghi su di essi prima del gradino 1; la skill `cycle` salta il pull
d'avvio dove `autonomy.md` lo riserva al custode.

## Temi di un solo adottante, in attesa

- **Un atto del giro su un secondo host** (`baserow`,
  [cattura](../i1/casi-delega-baserow-2026-10-16.md), fatti accanto): dal
  2026-10-19 il giro allinea il checkout dello standby dopo il push, con
  guardie sul posto (marker di ruolo assente, working tree pulito) e verifica
  dell'hash. Anche lo standby è un checkout servito: il pull rilascia lì gli
  script del controllo di freschezza. Nessun esercizio ancora; per il canone
  resta un caso singolo.

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
- **Chi riconosce l'host nel giro autonomo** (`bi`, primo giro autonomo,
  [cattura](../i1/casi-delega-bi-2026-10-17.md)): il bootstrap locale chiede
  di rileggere il marker di ruolo che l'unità impone già con
  `ConditionPathExists`; il permesso del giro nega la lettura, l'agente non
  aggira il diniego, deduce il ruolo da `hostname` e prompt e lo dichiara.
  Tocca l'ipotesi sotto: nel giro autonomo il riconoscimento prima del primo
  atto può stare nell'unità e non nell'agente. Secondo la cattura `crm` e
  `baserow` hanno la stessa condizione senza ripeterla nel bootstrap.
- **Un atto delegato per il guasto davanti al suo precursore**
  (`danea-auto`, [cattura](../i1/casi-delega-danea-auto-2026-10-15.md)):
  la delega copre la chiusura di LibreOffice «incastrato»; con un degrado
  misurato dal precursore l'atto era lo stesso e la condizione no. L'agente
  ha chiesto raccomandando la chiusura e ha proseguito il resto del ciclo;
  il custode ha scelto la chiusura. L'adottante propone un'ipotesi (copre,
  se l'atto è identico, fuori slot e con soglia scritta in uno strumento),
  non una regola. Il riscontro sull'utilità della prevenzione è locale e
  aperto fino al 27/10 circa; per il canone resta un caso singolo, in
  linea con [consent](../kb/consent.md): chiedere sul confine, poi allargare
  il criterio coi casi.

## Ipotesi in attesa

- **Ipotesi**: nel checkout servito basta la delega del ciclo con le
  eccezioni nominate, purché host e checkout si riconoscano prima del primo
  atto. Il custode l'ha resa canone il 2026-10-10
  ([consent](../kb/consent.md)), recepito dai sette lo stesso giorno.
  Eccezioni nominate: pull su richiesta in `baserow`; push del codice a
  suite verde in `bi`; pull fuori dagli slot in `danea-auto`; push su
  richiesta in `nixos` solo se un ciclo automatico eseguisse dal checkout.
  **Orizzonte**: l'audit `/adottanti` del 2026-11-01. **Riscontro**: i
  casi inoltrati entro quella data e le eccezioni scritte nei sette
  `autonomy.md` su `origin`. La smentisce un atto del ciclo su un checkout
  servito che il custode giudica da riservare senza che un'eccezione lo
  nominasse; la rafforza un mese di cicli senza casi di quel tipo.
- I temi di un solo adottante si riesaminano allo stesso audit; senza un
  secondo adottante restano adattamenti locali.
