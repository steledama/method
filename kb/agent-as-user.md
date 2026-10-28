---
stato: bozza
---

# Agent as user

L'agente è un utilizzatore a pieno titolo dello strumento, quanto il lettore
umano. Usa skill, prompt, `CLAUDE.md`, permessi dell'harness, script, codici di
uscita e messaggi d'errore come il custode usa viste e nodi: sono la sua parte
del system image. I criteri di design di Norman, affordance, signifier,
vincolo e feedback, si applicano anche a lui, e non solo agli artefatti letti
dall'umano. Progettare l'artefatto significa progettare anche la superficie su
cui l'agente agisce, con la stessa cura e con criteri di revisione propri.

## Le specificità dell'agente

L'agente non è un lettore umano più veloce. Quattro tratti cambiano il design:

- rilegge tutto a ogni run: ogni riga di una skill o di un prompt si paga a
  ogni invocazione, non una volta sola. Una skill lunga è un costo ricorrente;
  la forma adatta è un nucleo breve con i rami in file separati, letti solo
  quando il ramo è dovuto. Anche l'elenco delle skill si paga: ogni skill
  disponibile porta la sua descrizione in ogni sessione, usata o no;
- non ricorda fra le sessioni: ciò che impara in un giro non c'è nel giro
  successivo. Una lezione dura solo se diventa struttura, cioè uno strumento,
  un permesso, uno schema o un test. Un'istruzione scritta va riletta per
  sempre e funziona solo se viene letta e seguita ogni volta;
- paga ogni diniego in turni: un comando negato costa almeno un giro di
  tentativo e ripiego, e un comando composto con un solo pezzo non concesso è
  negato per intero;
- nel giro senza custode nessuno risponde: i segnali devono bastare senza
  chiedere, e un'ambiguità si risolve con un'inferenza o con una rinuncia.

Un segnale reso solo per l'occhio umano è muto per l'agente che legge testo.
Il colore, il grigio attenuato di un suggerimento, la posizione su uno schermo
spariscono nella forma testuale: un suggerimento dell'harness nel campo di
input si confonde allora con un messaggio scritto e non inviato. Il segnale
va cercato nella forma che lo conserva, per esempio i codici ANSI di un
terminale, oppure reso esplicito; dove non lo si percepisce vale la lettura
prudente (`session-messaging`).

## Il diniego è una percezione

Un diniego dei permessi è il feedback che l'agente riceve dallo strumento, nel
senso di Norman: dice che l'azione tentata non è ammessa. Per l'artefatto è
una percezione del ciclo, non un incidente da assorbire. Ogni diniego si
classifica in uno di tre modi:

- vincolo voluto: il guardrail ha funzionato, l'azione era davvero da
  impedire. Il vincolo resta; al più si migliora il feedback, con un messaggio
  più chiaro o un segnale nel punto d'uso che fa risparmiare il turno;
- lacuna: il gesto era legittimo e lo strumento non l'ha previsto. Si allarga
  il permesso o si dà uno strumento dedicato, consentito, che compie il gesto
  in modo sicuro;
- attrito dell'harness: il gesto era legittimo, ma il deny viene dalla
  grammatica dei permessi dell'harness, non da una regola del repository, e
  nessun allow lo apre. Il caso è la brace expansion, che Claude Code in
  modalità `dontAsk` nega anche quando il comando è negli allow. Non è un
  vincolo voluto, perché non protegge niente, né una lacuna chiudibile sul
  permesso. Si registra col suo costo in turni: se il rilancio riesce al
  primo tentativo il feedback del diniego basta; se ricorre, un segnale nel
  punto d'uso è legittimo, perché dietro c'è un vincolo vero, oppure lo
  strumento dedicato rende superflua la grafia che l'harness ferma.

La classe dipende dal contesto, non dal comando. L'affordance è una relazione
tra agente e artefatto, e lo stesso deny può essere vincolo in un contesto e
lacuna in un altro. Un atto sul Mondo negato nel giro, dove nessuno lo vede
prima che accada, può essere il gesto legittimo di una sessione col custode.
La classificazione si fa quindi per contesto d'uso: sessione col custode,
giro autonomo, agente esecutore.

La classe poggia su una causa accertata, non intuita. Il deny scatta su una
grafia, e la grafia che l'agente crede di aver usato non è sempre quella che
ha fermato il comando: il riscontro è il tentativo riuscito che segue, e la
differenza fra il comando negato e quello passato isola la causa. Il caso è
il giro di nixos del 2026-10-22: un diniego registrato come «`cd` composto,
errore dell'agente» su un comando senza `cd`, nello stesso giro in cui un
`cd … &&` era passato; il rilancio riuscito scioglieva nei path la brace
expansion `{eval,exec,…}` e toglieva il `cat` finale, che è negli allow. La
prova isolata coi soli allow `wc *` e `cat *` (Claude Code 2.1.303,
`dontAsk`) ha negato i due comandi con le graffe e lasciato passare gli
altri, con o senza `&& cat`: la causa è la brace, un attrito dell'harness.
Una classe data su una causa
intuita scrive nel task una diagnosi falsa, che il giro dopo legge come
fatto.

Un gesto abbandonato non ha un tentativo riuscito da cui leggere la causa:
l'agente prende il diniego e rinuncia. Se il gesto era legittimo, la perdita
non è il turno ma la percezione che il gesto avrebbe dato, e il diniego vale
come lacuna probabile, con la causa come ipotesi dichiarata, finché una
prova isolata non la accerta: nel giro seguente, che ne lancia i pezzi uno
per volta, o in sessione col custode. Il caso è il giro di nixos del
2026-10-24: `home-manager generations | head -2; cd … && jq …` negato e mai
riprovato, mentre la home di `deck` era indietro di un commit e nessun altro
strumento del giro poteva vederlo.

Anche il resoconto del giro classifica con queste tre classi, con la causa
accertata o l'ipotesi. Un'etichetta fuori classe, come «errori miei», arriva
al giro seguente già scritta e prende il posto della diagnosi: la
percezione la rilegge come ipotesi e riclassifica sulla trascrizione.

## Il cartello

Una lacuna non si chiude mai con un cartello nella skill che chiede all'agente
di adattarsi. Sarebbe la scritta SPINGERE sulla porta: il segnale compensa un
design che non comunica da sé, e per un lettore senza memoria è il caso
peggiore, perché si paga a ogni run e regge solo finché viene letto e seguito.
Il confine è netto. Una riga che annuncia un vincolo voluto, nel punto in cui
il gesto si compie, è un signifier legittimo: fa risparmiare un turno e ha
dietro un vincolo vero che regge anche se la riga non viene letta. Un divieto
scritto senza un vincolo dietro, o un'istruzione che chiede di aggirare un
gesto legittimo negato, è un cartello e indica una lacuna da chiudere sullo
strumento.

## Criteri di revisione

Per skill, prompt, permessi e script:

- ogni gesto che la skill o il prompt richiedono è concesso nel contesto in
  cui la skill gira?
- ogni divieto scritto ha dietro un vincolo vero, o copre una lacuna?
- il deny presidia il gesto o solo una sua grafia? Se una forma equivalente
  passa, il deny costa dinieghi senza proteggere ed è un cartello travestito
  da vincolo: si toglie, e il presidio va dove il gesto si decide. Il caso è
  lo staging intero, negato come `git add -A` e concesso come `git add` di
  una cartella; il controllo vero è il confronto di `git status` prima dello
  staging;
- i dinieghi registrati sono classificati, e ciascuno è chiuso sul vincolo o
  sullo strumento?
- quanto pesa la skill a ogni run, e quali rami possono vivere in file letti
  solo quando servono?
- un gesto ricorrente e fragile, come una scrittura composta su un registro,
  ha uno script dedicato con nome e uscita che ne segnalano la funzione?
- il feedback di un vincolo voluto dice all'agente cosa fare invece?
- uno strumento che emette un orario lo dà nell'ora locale in cui si
  scrivono resoconti e commit, da sola o accanto all'UTC? La `Z` finale è un
  segnale che l'agente perde: il giro di `salute` del 2026-10-28 ha letto un
  `modified_at` in UTC come ora locale e ha scritto le 2:00 al posto delle
  3:00. La correzione sta nell'output dello strumento, non in un'istruzione
  che chiede di convertire.

La revisione appartiene a chi progetta l'artefatto, in sessione col custode
quando tocca permessi o prescrizioni del giro. Il giro senza custode percepisce
e propone; non allarga da sé il proprio perimetro.

## Riferimenti

- Donald Norman, _The Design of Everyday Things_, Revised and Expanded Edition
  (Basic Books, 2013), Cap. 1 «The Psychopathology of Everyday Things»: la
  porta che ha bisogno di un'etichetta per essere usata come segnale di un
  design che non comunica; signifier e feedback. Cap. 4 «Knowing What to Do:
  Constraints, Discoverability, and Feedback». Provenienza e limite della
  copia locale nel register `world.md`.

Connessioni:

- [affordance-signifier](affordance-signifier.md)
- [constraint](constraint.md)
- [agent](agent.md)
- [skill](skill.md)
- [claude](claude.md)
- [perceive](perceive.md)
- [system-image](system-image.md)
- [cognitive-system](cognitive-system.md)
- [skill-composition](skill-composition.md)
- [session-messaging](session-messaging.md)
