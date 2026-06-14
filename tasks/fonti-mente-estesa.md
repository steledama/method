---
data: 2026-06-07
stato: aperto
---

# Fonti e filone della mente estesa (Andy Clark)

Aperto il 2026-06-07 per non perdere un filone teorico emerso a margine del ridisegno
della root (atrio / system image). Il filone potrebbe fare da **pavimento** filosofico al
metodo — e va vagliata l'ipotesi forte che riconfiguri o sostituisca il ruolo di Karpathy
fra i giganti (Karpathy sul tema ha un post; Clark ha una tradizione). Decisione **non**
presa: qui si tiene il filo, non si conclude.

## Il filone in breve

Tre posizioni sulla cognizione, e come mappano sulla scelta di layout appena fatta:

- **Tradizionale — teatro interiore**: la mente riceve input, ne costruisce una
  rappresentazione interna, ragiona su quella. È la Filosofia A della root: si _carica_ la
  KB nel contesto, poi si agisce.
- **Andy Clark — mente estesa / incarnata**: la mente non rappresenta il mondo, lo _abita
  e lo manipola_; il confine mente/mondo si dissolve. È la Filosofia B: non si carica
  l'inventario, lo si _attraversa_ — l'affordance è nella struttura, non in un documento da
  internalizzare. La propensione per B è, filosoficamente, una propensione per Clark.
- **Donald Norman — cognizione distribuita** (già adottato): la mente si estende nel mondo
  attraverso artefatti, che restano distinguibili ma collaborano. Più funzionale, meno
  radicale di Clark.

Il metodo cita già Hutchins (_Cognition in the Wild_) in [[cognitive-system]]: **Clark è il
fratello mancante** della stessa famiglia (cognizione estesa/distribuita).

## La torsione che rende il filone originale (Hinton)

La provocazione di Hinton: l'IA sfida tutte e tre le posizioni perché produce comportamento
intelligente **senza corpo e senza ambiente**. L'LLM non _abita_ il filesystem come un agente
incarnato abita lo spazio — riceve token. Per l'LLM "agire attraverso senza rappresentare" è
in parte falso: per attraversare la porta `kb.md` deve comunque leggerla (caricarla); non può
«sapere come sedersi senza un'immagine della sedia», ha solo immagini. Quindi l'embodiment di
B è **reale per l'umano, parziale/aspirazionale per l'LLM** — il che ricade esattamente
sull'asimmetria già nei nodi ([[system-image]]): per l'umano la KB è impalcatura a un modello
già posseduto; per l'LLM la KB _è_ il modello.

Sintesi candidata (vale un nodo, una volta sourcata): Hinton dice che l'IA manca di corpo e
mondo; **la risposta del metodo è che l'artefatto versionato _è_ il corpo/ambiente
ingegnerizzato che diamo all'LLM senza corpo** — il sostrato esterno persistente che gli dà un
"mondo" stabile in cui agire tra una sessione e l'altra. È l'upgrade filosofico
dell'intuizione sull'asimmetria degli agenti.

## Lavoro

- procurare le fonti primarie (`world`, su Drive; provenienza nel register `sources.md`) (non costruire dal sentito dire):
  Clark & Chalmers, _The Extended Mind_ (1998, _Analysis_ 58); Clark, _Being There_ (1997);
  Clark, _Supersizing the Mind_ (2008);
- distillare i2 con provenienza esatta (edizione, capitolo); decidere la destinazione
  bottom-up: estendere [[cognitive-system]] / [[system-image]] / [[cognitive-artifact]]
  oppure aprire un nodo proprio `mente-estesa`;
- vagliare l'ipotesi forte sui giganti: Clark come quarto gigante, o ridefinizione del posto
  di Karpathy. Da decidere solo dopo aver letto le fonti, non ora;
- portare a i3 la sintesi "artefatto come corpo/ambiente ingegnerizzato dell'LLM" nei
  Riferimenti dei nodi toccati.

## Disciplina di fedeltà (vincolo, non nota)

Il filone è nato da un **estratto di seconda mano**: un riassunto AI di una conversazione, che
_confabula davanti agli occhi_ (attribuzioni incerte Feynman/Clark/Brooks, «probabilmente
intendeva…»). È esattamente la citazione di seconda mano da cui [[cognitive-fidelity]] mette in
guardia. **Non scrivere un nodo da quel materiale.** Prima i1 reale, poi i2, poi i3 — l'arco
di input completo, come per [[affordance-signifier]] e [[system-image]].
