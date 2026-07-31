---
sintesi: "Ritagliare il quartetto lungo il modello: `plan-review` e `verdicts-review` diventano `execute` ed `evaluate`, con i tre stadi del proprio arco come scope (`plan|specify|perform`, `perceive|interpret|compare`). Le procedure esistenti non si buttano, si rifilano sotto il loro stadio; si guadagna la casa per i1, i2 e o3, oggi scoperti. Pilota `metodo`, poi prescrizione o3 per i quattro."
ciclo: dev
---

# Skill per arco: `evaluate` ed `execute` tripartite

Verdetto e razionale nel filo
[`i3/skill-per-arco-tripartito.md`](../i3/skill-per-arco-tripartito.md); qui la
forma concreta e la sequenza di lavoro.

## Il canovaccio di `evaluate [perceive|interpret|compare|all]`

Il braccio di valutazione, nell'ordine del ciclo. Default `all`; ogni stadio può
essere invocato da solo, e ogni stadio può **chiudere in una riga** quando non ha
materia («nessun segnale nuovo»): la chiusura vuota è esito legittimo, non un
passo saltato.

**`perceive`** — raccogliere il grezzo dal Mondo, **valenza-neutro**. In `metodo`:
i marker `method-review.md` dei quattro adottanti, gli esiti già prodotti da
`kb-review`, i segnali che il custode porta da un altro repo. Negli adottanti:
posta, log, output di strumenti, documenti arrivati. `evaluate perceive` può
acquisire una diagnosi di `kb-review`, ma non la esegue implicitamente:
`kb-review` resta la capacità diagnostica dell'ala trasversale, fuori dai due
archi. Si cattura in `i1/` **solo** ciò che è effimero o che per precisione e
durata chiede un riflesso stabile
(`kb/perceive.md`): il grezzo persistente resta fuori. Nessuna valutazione qui —
il confine i1→i2 è l'ingresso della valenza, e anticiparlo è il difetto che lo
stadio esiste per impedire. Esito: cosa è entrato, cosa è stato catturato e
perché, cosa resta fuori.

**`interpret`** — distillare il grezzo in sintesi, **orientati dai goal sulla
rilevanza e neutri sulla valenza** (`kb/goal.md`). È lo stadio che oggi non ha
casa, e i suoi tre obblighi vengono dritti dai segnali appena valutati:

- **la provenienza delle quantità** (`kb/verdict.md`): un numero che entra in una
  sintesi dichiara se è misurato, dichiarato da terzi o derivato da
  dichiarazioni. Una quantità derivata non fa da architrave;
- **la cascata all'indietro**: quando un claim cambia o cade, le sintesi `i2/`
  che lo usavano si cercano e si correggono. La skill individua riferimenti
  espliciti e candidati semantici da verificare, senza promettere di riconoscere
  automaticamente ogni dipendenza implicita. È il buco che ha lasciato propagare
  la cifra dei «400 €/mese» in un'analisi e nella sua classifica di priorità dopo
  che era stata smentita;
- **il materiale di casa prima**: il file `o2/`, la corrispondenza in uscita, la
  valutazione di credibilità già scritta nella KB sono fonti primarie, non
  contesto.

Esito: quali sintesi sono nate o cambiate, contro quale materiale sono state
verificate, quali affermazioni restano non verificate e sono dichiarate tali.

**`compare`** — il verdetto contro il Goal: è la procedura attuale di
`verdicts-review`, rifilata sotto il suo stadio. Le cinque domande per ogni filo
(è ancora vero rispetto al segnale, incluso il file `o2/`? è più sicuro del suo
materiale? è ancora aperto? è ancora _un_ filo? è stato, non log?), la copertura
bidirezionale col register `goal.md`, la formazione-goal sugli input esogeni
**sempre in proposta al custode**, la bonifica del plan dalla narrativa di stato,
e l'handoff «impatti sul piano» verso `execute`.

## Il canovaccio di `execute [plan|specify|perform|all]`

**`plan`** — la coda: drift `o1/plan.md`↔`o2/`, ordine e priorità, dipendenze
reali (non preferenze d'ordine), direzione task→obiettivo letta dalla colonna
`Ob.`, `## Scadenze` e finestre tattiche, task consigliato per la sessione. È il
cuore dell'attuale `plan-review`.

**`specify`** — i dettagli: ogni task sostanziale ha il suo file, il frontmatter
è completo (`sintesi`, `ciclo`), il contratto plan×`o2/` regge (lo verifica il
generatore, non l'agente), i diari di sessione si potano a chiusura. Qui vivono
le **quattro proprietà cardine** come criteri di qualità dell'o2 — visibilità,
feedback, mapping, constraint (`kb/specify.md`) — che oggi nessuna skill
controlla mai.

**`perform`** — predisporre o compiere l'atto, secondo autorizzazione. Nel
canone: la collezione `o3/` tiene solo il vivo (prescrizioni consumate potate,
`kb/perform.md`), gli strumenti registrati sono ancora eseguibili, i runbook di
propagazione riflettono il canone corrente. Quando l'atto è locale, reversibile
e già autorizzato, `execute perform` lo compie davvero; quando tocca il Mondo o
richiede nuova autorità, produce o valida la prescrizione e si ferma al confine.
Un dominio **può** montare qui i propri atti come scope (`execute aggiornamento`
in `nixos`, `execute categorie` in `bi`), con la scelta del ramo guidata da
giorno, host e scadenze e le cadenze in config dichiarativa per entità: è
ammesso, non prescritto — il confine di autorizzazione segue le risorse dello
scope, non la skill.

## Cosa tocca

- **Skill**: `.claude/skills/evaluate/`, `.claude/skills/execute/` e i wrapper
  `.codex/skills/` corrispondenti; rimozione di `plan-review` e
  `verdicts-review` **dopo** che il contenuto è stato rifilato, non prima.
- **`kb/skill.md`**: è la riscrittura più profonda — «Base ufficiale», la coppia
  simmetrica di supervisione, la regola dei nomi (che passa da «l'indice che
  tiene onesto» a «l'arco del modello», con la ragione del cambio), il
  protocollo post-evento (che cita le skill per nome), «Applicazione nei repo del
  metodo».
- **Nodi che citano le due skill per nome**: `kb/plan.md`, `kb/goal.md`,
  `kb/verdict.md`, `kb/perceive.md`, `kb/interpret.md`, `kb/compare.md`,
  `kb/specify.md`, `kb/perform.md` — da verificare con un grep, non a memoria.
  Gli atomi degli stadi guadagnano il rimando alla propria fetta di skill.
- **Bussole**: `README.md` e `CLAUDE.md` di `metodo` (l'elenco commentato delle
  skill), e negli adottanti gli stessi due file più le righe `## Scadenze` che
  citano le skill per nome.
- **`i1/perceptions.md`, `i2/interpretations.md`, `o3/prescriptions.md`**: i tre
  indici finora senza guardiano guadagnano il rimando allo stadio che li
  mantiene.

## Sequenza

1. riscrivere `kb/skill.md` col taglio nuovo (il canone prima delle skill: le
   skill sono interfacce sul canone, non la sua sede);
2. scrivere `evaluate` ed `execute` in `metodo`, rifilando le procedure esistenti
   e aggiungendo i tre stadi scoperti; wrapper Codex;
3. prima del pilota, fissare l'ipotesi su `adopters-review`: resta skill di
   dominio distinta e produce materiale che `evaluate perceive` può acquisire;
   l'assorbimento è una variante da rivalutare solo dopo l'uso, non
   un'ambiguità dell'interfaccia da pilotare;
4. **pilotare su `metodo`** i due archi end-to-end su almeno un evento reale;
   ogni scope restituisce un esito esplicito, anche nullo, e il filo registra
   attriti, sovrapposizioni e passaggi che non hanno cambiato l'artefatto
   _prima_ di propagare;
5. aggiornare nodi e bussole; emettere la prescrizione `o3/` per i quattro,
   col pilota-adottante scelto lì (candidato `nixos`, che ha già il multi-scope
   collaudato e la skill di dominio più matura da montare eventualmente su
   `perform`);
6. alla chiusura, aprire il task di rivalutazione `pause` con la condizione di
   risveglio della clausola di uscita (filo `i3/`).

## Criterio di chiusura

Le due skill esistono in `metodo` e sono state invocate end-to-end su almeno un
evento reale; ogni scope ha restituito un esito esplicito, anche nullo, e il
filo registra attriti, sovrapposizioni e passaggi che non hanno cambiato
l'artefatto. Il canone in `kb/skill.md` è inciso e la prescrizione per i quattro
è aperta. Il recepimento degli adottanti **non** è parte di questo task: è loro
coda, e si misura col battito mensile.
