---
description: Il braccio di valutazione del ciclo — eval [perceive|interpret|compare|all] — raccolta del grezzo dal Mondo, sintesi i2 con provenienza e cascata, verdetto dei fili i3 contro goal.md e bonifica del plan
user-invocable: true
---

Compi il braccio di valutazione del ciclo, nell'ordine degli stadi:
`perceive` → `interpret` → `compare`. L'argomento seleziona lo stadio, il
default è `all` (la sequenza intera). Ogni stadio invocato restituisce un
esito esplicito e può **chiudere in una riga** quando non ha materia («nessun
segnale nuovo»): la chiusura vuota è esito legittimo, non un passo saltato.

È la skill simmetrica di `exec`: questa tiene onesta la valutazione, quella
l'esecuzione; il register `goal.md` è la cerniera che entrambe controllano da
versanti opposti. Usala quando un giro del ciclo produce esiti (una
propagazione recepita, una percezione valutata, un verdetto ratificato), a
inizio sessione strategica, o quando fili e note sembrano crescere senza
controllo. Dopo eventi del mondo vale il **protocollo post-evento**:
`eval` → `exec` — la verità prima delle priorità (pilota `economia`,
2026-07-12). Questa è la copia canonica della skill: gli adottanti la forkano
e la parametrizzano sui propri segnali di dominio.

**Gate comune, proponi-poi-applica**: le modifiche a collezioni e register si
applicano solo dopo conferma del custode, e il gate prevale
sull'autorizzazione generica delle bussole — quella copertura è per il lavoro
ordinario di sessione, non per l'auto-applicazione degli esiti di una
supervisione.

## `perceive` — raccogliere il grezzo

Valenza-neutro: qui si registra, non si giudica. Il confine i1→i2 è
l'ingresso della valenza, e anticiparlo è il difetto che lo stadio esiste per
impedire.

1. Raccogli ciò che arriva dal Mondo. In `metodo` i canali sono: i marker
   `i3/allineamento-metodo.md` degli adottanti (dai checkout dichiarati nel
   territorio di `world.md`, superfici ssh remote comprese), gli esiti già
   prodotti da `kb` (che resta capacità diagnostica trasversale: la sua
   diagnosi si acquisisce come segnale, non si esegue
   implicitamente da qui), i segnali che il custode porta da un altro repo.
2. Cattura in `i1/` (item più voce in `i1/perceptions.md`) **solo** ciò che è
   effimero o che per precisione e durata chiede un riflesso stabile (cfr.
   `kb/perceive.md`): il grezzo persistente resta fuori, raggiungibile dalla
   sua fonte.
3. Esito: cosa è entrato, cosa è stato catturato e perché, cosa resta fuori.

## `interpret` — distillare in sintesi

Orientato dai goal sulla rilevanza, neutro sulla valenza (cfr. `kb/goal.md`).
Tre obblighi sulle sintesi `i2/`:

- **Provenienza delle quantità** (cfr. `kb/verdict.md`): un numero che entra
  in una sintesi dichiara se è misurato, dichiarato da terzi o derivato da
  dichiarazioni. Una quantità derivata non fa da architrave.
- **Cascata all'indietro**: quando un claim cambia o cade, cerca le sintesi
  `i2/` che lo usavano e correggile — prima i riferimenti espliciti, poi i
  candidati semantici da verificare. Il riconoscimento di ogni dipendenza
  implicita non si promette: ciò che non è stato verificato si dichiara.
- **Materiale di casa prima**: il file `o2/`, la corrispondenza in uscita, la
  valutazione di credibilità già scritta nella KB sono fonti primarie, non
  contesto.

Esito: quali sintesi sono nate o cambiate, contro quale materiale sono state
verificate, quali affermazioni restano non verificate e sono dichiarate tali.

## `compare` — il verdetto contro il Goal

**1. Raccogli il contesto corrente**

Leggi `goal.md`, `i3/verdicts.md` e ogni filo `i3/*.md`; poi `o1/plan.md` e
`git log --oneline -15` per gli eventi dall'ultima revisione. I segnali reali
sono gli esiti di `perceive` e `interpret` di questo giro, l'audit
(`o3/kb_tools.py audit`), i marker `i3/allineamento-metodo.md` degli
adottanti (dai checkout dichiarati nel territorio di `world.md`) e le
percezioni `i1/` non ancora valutate.

**2. Cinque domande per ogni filo**

- **È ancora vero?** Confronta il verdetto col segnale reale (audit, marker,
  nodo), non con la memoria. Un filo che contraddice il suo segnale va
  aggiornato in place prima di ogni altra cosa. Fra i segnali c'è il **file
  `o2/` che alimenta il filo**: `exec plan` guarda plan↔`o2/`, questo stadio
  guarda filo↔segnali, e filo↔`o2/` non è di nessun altro — è spesso la
  registrazione più fresca e più cauta, e il filo che è più ottimista del
  proprio task ha già in casa la propria smentita (`kb/verdict.md`).
- **È più sicuro del suo materiale?** Sul filo che suona meglio degli altri
  — più elegante, più quantificato, più favorevole — fai un passo in più, non
  uno in meno: le quantità che reggono la tesi portano la provenienza (misurata
  / dichiarata da terzi / derivata da dichiarazioni)? Ciò che il progetto ha
  prodotto **di suo** (posta in uscita, valutazione della fonte già in KB) è
  stato guardato? Una tesi che cade se cade una cifra derivata non è un
  verdetto: è una congettura da retrocedere.
- **È ancora aperto?** Verdetto stabile e nessuna tensione → il filo si chiude:
  file rimosso, voce tolta da `i3/verdicts.md`, storia in git.
- **È ancora _un_ filo?** Se è cresciuto multi-tema, proponi lo split; ogni
  filo tiene una tensione sola.
- **È stato, non log?** Pota paragrafi storici e sequenze datate: la cronologia
  è il git history del file, non il suo corpo.

**3. Copertura bidirezionale con `goal.md`**

- Ogni obiettivo del register ha un **segnale vivo** (filo, audit, marker) e —
  se c'è tensione aperta — un filo che la tiene. Un obiettivo senza segnale è
  un buco di misura da dichiarare nel register, non da nascondere.
- Ogni filo dichiara **quale obiettivo misura** (annotazione `misura:` nella
  voce di `i3/verdicts.md`). Un filo che non misura nessun obiettivo è
  materiale da triage: o rivela un obiettivo mancante nel register (proponilo),
  o non è un verdetto.
- Segnali orfani (percezioni `i1/` che nessun filo valuta, marker che nessuno
  legge) vanno fatti emergere.

**4. Bonifica del plan (e dei task)**

Il plan è coda pura: tabella, dipendenze, legenda. Note e «cause» che sono
narrativa di stato del mondo (debrief, letture, posizioni, fondazioni
consegnate) migrano nel filo pertinente — o nel task `o2/` se sono contesto
operativo di esecuzione. Stessa lente sui task `o2/`: i diari di sessione si
potano a chiusura. È il gemello del passo «igiene» di `exec plan`, guardato
dal versante opposto.

Migrare è **fondere, non cancellare**: prima di potare una copia, stabilisci
quale delle due porta il fatto più fresco. L'assunzione naturale — la copia è
stale, la destinazione è vera — non regge sempre: nella potatura di `economia`
(2026-07-28) in due casi su otto era il plan a portare il fatto più recente, e
potare alla cieca avrebbe distrutto informazione.

Fondere guarda anche ai **lettori**, non solo al contenuto: chiedersi chi altro
legge la copia che stai rimuovendo, macchine incluse. In `metodo` il footer
`## Dettagli task` era un secondo indice per l'umano ma l'unica chiave con cui il
generatore risolveva una riga del plan al suo `o2/`: potato il footer, la vista
dei task è rimasta vuota per diciassette giorni senza che nulla rompesse
(`i3/vista-derivata-e-verificata.md`).

**5. Formazione goal (modo due dell'i3)**

Input esogeni che non chiudono loop noti ma ne aprono di nuovi (una percezione
da un adottante che non rientra in nessun obiettivo, una cornice teorica
importata) → proponi il filo nuovo o il ritocco al register. Sempre in
proposta: decidere cosa conta è del custode umano (`kb/goal.md`).

**6. Proponi, poi applica**

Presenta le modifiche come elenco — una voce per filo/obiettivo, con azione
(aggiorna/chiudi/split/crea, migra dal plan) e motivo. Se non c'è nulla da
proporre, dillo esplicitamente. Applica a `i3/`, `goal.md` e `o1/plan.md` solo
dopo conferma del custode (gate comune); chiudi suggerendo `/commit`.

**7. Handoff «impatti sul piano»**

Elenco puntato, non eseguito: ogni verdetto cambiato in questo giro che
implica modifiche a `o1/plan.md`/`o2/` (priorità, attese sciolte, scadenze,
task superati), come input per l'`exec plan` a valle. L'handoff è input,
non comando: lo scope ricevente conserva il giudizio e dichiara le
divergenze. Se non c'è nulla da passare, dillo esplicitamente.

## Note operative

- I fili chiusi si rimuovono, non si archiviano: la storia resta in git.
- L'annotazione `misura:` vive nell'indice `i3/verdicts.md`, non nel
  frontmatter dei fili (il frontmatter tiene solo la facet `ciclo`).
- La valutazione non cambia mai un segnale (audit, marker): se il segnale è
  sbagliato, il fix è un task, non un ritocco al verdetto.
- Aggiornamenti del register `goal.md` in questa sede sono fotografie
  (obiettivo a regime, buco di misura dichiarato), non nuovi obiettivi: quelli
  li porta il custode.
