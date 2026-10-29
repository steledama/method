---
sintesi: "Affinare la `w` del plan sul modo in cui si riconosce il risveglio (sonda deterministica, arrivo in un canale, termine di riesame) con campi della chiosa e senza lettere nuove, e scrivere che un'attesa tenuta dal custode è una `p`. Analisi sull'uso nei sei adottanti e proposta di canone da discutere col custode."
ciclo: runtime
decidere: "Se incidere in `kb/plan.md` la forma del risveglio delle `w` (`sonda:`, `arrivo:`, `entro:`) e la precisazione che il custode sta dentro il «noi» delle `p`."
---

# Riconoscimento del risveglio delle attese

## Origine

Il 2026-10-29 la sessione `nixos` su `norvegia` inoltra via Herdr, su
richiesta del custode, una domanda di metodo. In `nixos` il prospetto di
`/manutenzione` (`o3/scripts/maintenance-due.sh`) prende tutte le righe del
plan con `w<n>` e mostra ogni giorno come «mai controllato» anche le attese
che nessuno script può interrogare. Il giro autonomo del 29/10 ne ha fatto
un task (`nixos` `o2/maintenance-due-attese-non-upstream.md`, alternativa
raccomandata: un prefisso `upstream:` letto dallo script).

La posizione del custode: la divisione fra `w` (la mossa è esterna
all'artefatto) e `p` (la teniamo noi) regge, e non serve una categoria
«custode». Un'attesa tenuta dal custode, dall'agente o da entrambi è una `p`,
perché la cognizione è condivisa. L'agente fa bene a chiedere un
ripensamento se una `p` non gli torna, e a stare fermo se gli torna. La
domanda è se affinare la `w` sul modo in cui si riconosce il risveglio, e non
su chi tiene il tempo. Il requisito centrale: l'arrivo non deve sfuggire.

## Il canone oggi

`kb/plan.md` dice che «la lettera dice chi tiene il tempo — il mondo o noi»,
che la lettera si decide da chi fa la prossima mossa e che ogni `w` nomina il
segnale che la riapre, «osservabile nei segnali che il giro raccoglie». Il
passo 3 di `exec plan` scioglie la riga quando il segnale compare fra le
catture. Restano due lacune:

- il «noi» non dice se il custode ne fa parte, e i domini lo leggono in modi
  diversi;
- il segnale è testo libero: niente dice come si riconosce, e niente copre il
  caso in cui arriva da un canale che il giro non legge.

## Uso nei domini

Letture del 2026-10-29: `nixos` `c4fbebda`, `bi` `79113b1b` (origin),
`danea-auto` `065e18a` (origin), `baserow` `9a1bdca`, `economia` `e9636c5` e
`salute` `8d6e5ca` (su `deck`). `crm` è dismesso.

- **nixos**: 5 `w` e nessuna `p`. La chiosa porta un prefisso di natura
  (`upstream:`, `custode:`, `Mondo:`). `w3` e `w4` sono sondabili: lo stato
  di una issue GitHub, la versione 8.6.0 o successiva di naps2 in
  `nixos-unstable`. `w2` e `w5` sono marcate `custode:`, e per il criterio
  del custode sono delle `p`. `w1` (`Mondo:`) aspetta un giro in cui un ramo
  risulti dovuto secondo le cadenze di `i1/manutenzione.json`, con «primo
  atteso il 2026-11-01». È un'occorrenza reale che valida il codice, quindi
  una `w`, e il suo segnale si legge in modo deterministico nel registro dei
  giri.
- **danea-auto**: 4 `w` e 3 `p`. È la forma più matura: «**Riapre:** `<segnale>`,
  o in mancanza `<data>`». `w3`, `w4` e `w6` si riconoscono in modo
  deterministico su log locali (un ritentativo `^+s`, l'`ATTENZIONE` di
  `stats.ps1`, la riga `ERRORE FATALE`, un `Ctrl+P` fallito), con un termine
  (06/11, marzo 2027). `w5` aspetta un'occorrenza del guasto. La legenda
  scrive già «una `p` non è pronta: la mossa spetta alla sessione col
  custode», che è la posizione del custode.
- **economia**: 8 `w` e 1 `p`, tutte attese di un arrivo (risposte,
  documenti, un accredito, la CU) da canali diversi: Gmail, WhatsApp,
  telefonata, estratto conto «al ciclo finanze». `w1` ha come risveglio
  «l'ok di Stefano sul testo»: è una `p`. `w3` nomina canali che il giro non
  legge (WhatsApp, la telefonata). `w7` («attesa in gennaio 2027») porta un
  termine. La legenda ha il termine come principio senza data: «se il
  silenzio supera il tattico, sollecitare».
- **bi**: 3 `w` e 3 `p`. Le `w` aspettano arrivi: un fornitore candidato, il
  codice e gli accessi da Alessio, una decisione di Alessio e Luigi. `w2` è
  in parte sondabile (migrazione fatta: repo `abbinamenti`, modulo in
  `nixos`). `p1` «attende la decisione commerciale» su GM: se la decisione
  spetta a Luigi e non al custode, per il criterio è una `w`. Lo valuta la
  sessione `bi`.
- **salute**: una `w`, la seduta del 3/11. È un evento esterno con una data,
  e il suo esito arriva solo dal resoconto del custode nel diario o in
  sessione.
- **baserow**: nessuna attesa aperta.

In tutto 21 `w` e 7 `p`. Delle `w`, 6 sono sondabili (`nixos` w1, w3, w4;
`danea-auto` w3, w4, w6) e 12 aspettano un arrivo. Le altre 3 sono tenute
dal custode (`nixos` w2, w5; `economia` w1) e per il criterio sono delle `p`.

## Analisi

**La divisione w/p regge, col custode dentro il «noi».** È coerente con la
cognizione condivisa, e `danea-auto` la pratica già. Ha una conseguenza
operativa: nel giro senza custode una `p` tenuta dal custode non è pronta. Il
giro non la tocca, e la nomina nella riga `Attenzione:` solo se ha una
ragione per chiederne il ripensamento. Classificarla `w` ha due costi: falsa
il prospetto degli script (`nixos`) e manda il giro a cercare nel Mondo un
segnale che nasce in sessione. Per le attese composite, come `nixos` w2
(finestra concordata _o_ prima promozione reale di uno standby), la lettera
segue la prima mossa attesa. L'evento del Mondo resta nella chiosa come
risveglio alternativo.

**Il modo di riconoscimento è la distinzione che lavora.** Ce ne sono due,
più una rete di sicurezza.

- **Sonda**: un comando o un URL con una condizione booleana, valutabile
  senza il modello. Costa una chiamata a ogni cadenza, e oltre la cadenza
  non può sfuggire. La esegue uno strumento versionato, e il modello ne
  legge solo l'esito.
- **Arrivo**: il segnale arriva da sé in un canale (una sessione, il diario,
  un'email, un log, un giro). Riconoscerlo vuol dire confrontare i fatti in
  ingresso con le `w` aperte, che è lavoro di `perceive`. Può sfuggire in due
  modi: il canale non è letto dal giro (telefonata, WhatsApp, una seduta),
  oppure è letto ma nessuno fa il confronto. Il secondo si ripara dando a
  `perceive` l'elenco delle `w` ad arrivo col loro canale. Il primo no: se il
  canale passa per il custode, è il custode a portare il fatto, e il giro non
  può accorgersene da solo.
- **Termine**: non è un terzo modo ma la rete sotto gli altri due. È una data
  oltre la quale il silenzio diventa il segnale: si sollecita, si
  riclassifica o si chiede al custode. È quello che garantisce che l'arrivo
  non sfugga quando il canale non è leggibile. `danea-auto` lo usa già («o in
  mancanza il 06/11»); `economia` lo ha come principio.

Il requisito del custode si traduce così in una regola verificabile: **ogni
`w` ha una sonda, oppure un arrivo in un canale che il giro legge, oppure un
termine.** Una `w` senza nessuno dei tre può sfuggire, ed è un rilievo per
`exec plan`. Quando il canale non è letto dal giro, compreso il caso «lo
riferisce il custode», il termine diventa necessario.

**Efficienza.** Gli script prendono solo le righe con una sonda, quindi non
mostrano più «mai controllato» su attese senza niente da interrogare (in
`nixos`, il 29/10, erano 3 righe su 15). Non serve neanche un'euristica sul
prefisso: la sonda c'è o non c'è, e l'alternativa A del task `nixos` diventa
un caso particolare del canone. Una sonda eseguita dallo script del dominio
costa al giro un solo comando già concesso, invece di una forma nuova per
ogni attesa. È la stessa economia di permessi che cerca
[ricorrenza-dinieghi](ricorrenza-dinieghi.md). `perceive` riceve un elenco
breve di `w` ad arrivo col loro canale e cerca in modo mirato (per esempio
il mittente atteso in Gmail), senza rileggere la legenda. I termini entrano
nel controllo delle scadenze come righe di riesame, senza contare come
scadenze.

**Analisi.** La forma rende leggibile la composizione delle attese di ogni
dominio. `nixos` e `danea-auto` hanno attese tecniche, in gran parte
sondabili e quindi delegabili al giro. `economia` e `bi` hanno attese
relazionali ad arrivo, spesso da canali che solo il custode vede. Questo
informa la delega: dove la quota di attese «riferite dal custode» è alta, il
giro senza custode ha poco da sciogliere da solo, e i termini sono il suo
presidio.

## Campo nella chiosa o lettere nuove

Le lettere nuove (per esempio `ws`/`wa`, o un simbolo come il `!`) non
convengono, per tre ragioni:

- la lettera dice chi muove, mentre il modo di riconoscimento è un attributo
  della condizione di risveglio, che vive già nella chiosa;
- moltiplicare le forme dell'indice rompe l'indirizzo breve e la sua
  riassegnazione in ordine di tabella;
- un secondo simbolo appeso contenderebbe al `!` la rarità che lo fa
  funzionare.

Le lettere attuali reggono la traduzione (`w` per _wait_, `p` per _pause_). Un
campo con parola chiave si traduce uno a uno: `sonda:` → `probe:`, `arrivo:` →
`arrival:`, `entro:` → `by:`. La raccomandazione è il campo.

## Proposta di canone

Da discutere col custode. In `kb/plan.md`, sezione «Forma»:

1. **Il «noi» delle `p` è il custode con l'agente.** Un'attesa tenuta dal
   custode, dall'agente o da entrambi è una `p`: la cognizione è condivisa.
   L'agente chiede un ripensamento quando una `p` non gli torna, altrimenti
   sta fermo. Nel giro senza custode una `p` non è pronta.
2. **Il risveglio di una `w` dichiara come si riconosce**, in una di due
   forme, più un termine:

   - `sonda:` un controllo deterministico, cioè una cosa da interrogare e una
     condizione, che uno strumento valuta senza il modello. Esempio, `nixos`
     w4: `sonda: naps2 ≥ 8.6.0 in nixos-unstable`;
   - `arrivo:` il fatto atteso e il canale da cui arriva (email, diario,
     sessione, un log, un giro). Esempio, `salute` w1: `arrivo: esito della
seduta, riferito dal custode nel diario o in sessione · entro:
2026-11-04`;
   - `entro:` la data di riesame, necessaria quando il canale non è letto
     dal giro e facoltativa altrimenti.

   Il canone fissa il contratto della sonda (deterministica, booleana,
   senza il modello) e non la sua sintassi. Il vocabolario (issue, versione
   in nixpkgs, riga di log) e la sua valutazione appartengono allo strumento
   locale: dichiara e taci (`kb/method-development.md`).

3. **Contratto degli strumenti.** Uno script che controlla le attese prende
   solo le `w` con `sonda:`. I termini `entro:` entrano nel controllo delle
   scadenze. `perceive` confronta i fatti in ingresso con le `w` ad
   `arrivo:`. `exec plan` segnala come rilievo le `w` senza sonda, senza
   canale letto dal giro e senza termine.
4. **Il `!` resta ortogonale**: dice quanto costa l'attesa, non come si
   riconosce il risveglio.

Toccati, oltre al nodo: il passo 3 di `exec plan` (rilievo sulle `w` che
possono sfuggire) e il `perceive` di `eval` (confronto con le `w` ad arrivo).

## Questioni per il custode

1. Il termine `entro:` va reso obbligatorio quando il canale non è letto dal
   giro, o resta sempre facoltativo?
2. Dove vive la sonda eseguibile? Nella chiosa (una sola rappresentazione,
   ma un comando dentro il plan) o nella config dell'adottante insieme alla
   cadenza, come `i1/manutenzione.json` in `nixos`, con la chiosa che la
   nomina. Raccomandazione: la condizione leggibile nella chiosa,
   l'implementazione nello strumento, la cadenza in config.
3. Le parole chiave: `sonda`/`arrivo`/`entro` (`probe`/`arrival`/`by`), o
   altre.
4. Recepimento: basta il nodo, letto via symlink e allineato da ciascun
   `/method`, oppure serve una prescrizione `o3/` per gli strumenti che
   controllano le attese, come per il contratto del `!`? Raccomandazione:
   solo il nodo, finché un secondo adottante non ha uno script del genere.

## Conseguenze per i domini

Le recepiscono le loro sessioni. Qui restano come materiale del confronto.

- `nixos`: w2 e w5 diventano `p`; w1, w3 e w4 dichiarano la sonda. Il task
  `maintenance-due-attese-non-upstream` si risolve con l'alternativa A
  riformulata: lo script legge la sonda e non un prefisso.
- `economia`: w1 diventa `p`; le `w` con canali non letti dal giro (w3, w4)
  prendono un termine.
- `bi`: va verificato di chi è la decisione in `p1`; w2 ha una sonda
  parziale.
- `salute`: w1 è un arrivo per tramite del custode, con termine.
- `danea-auto`: «Riapre: …, o in mancanza `<data>`» è già la forma, al più da
  rinominare.
- `baserow`: niente.

## Chiusura

Alla decisione del custode: se accolta, si aggiornano `kb/plan.md` e le
skill `exec` ed `eval`, e riga del plan, voce in `o2/tasks.md` e questo file
si rimuovono nello stesso commit. Se respinta, il task si chiude con la
ragione nel commit.

Connessioni:

- [plan](../kb/plan.md)
- [attese-a-finestra](../i2/attese-a-finestra.md)
- [ricorrenza-dinieghi](ricorrenza-dinieghi.md)
