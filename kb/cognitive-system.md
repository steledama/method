---
stato: bozza
---

# Cognitive system

Unità di analisi proposta da Edwin Hutchins per studiare la cognizione dove
accade davvero: non dentro la testa di un singolo individuo, ma
nell'accoppiamento tra persone, artefatti e ambiente. Un sistema cognitivo
comprende individui, artefatti e le relazioni che li legano in una pratica di
lavoro. La tesi di Hutchins è che la cognizione è _distribuita_ — non solo tra
le persone di un gruppo, ma tra persone e strumenti, tra mente e mondo.

Cosa si distribuisce non è solo l'informazione ma anche i processi:
rappresentazioni e trasformazioni si propagano attraverso agenti e artefatti in
sequenza. Hutchins lo dimostra sulla navigazione navale — tracciare una rotta
non è il lavoro di nessuna mente singola, ma del sistema composto da equipaggio,
grafici, strumenti e procedure condivise. Non è quindi rinchiusa nella mente
individuale: va analizzata nella propagazione delle rappresentazioni attraverso
persone, strumenti e contesto.

Norman converge sulla stessa conclusione, ed è una convergenza interna alla
stessa famiglia UCSD: persona e artefatto formano un sistema le cui capacità
possono superare quelle dell'individuo isolato. In questa lettura l'artefatto è
un componente che trasforma i compiti e le capacità del sistema. In _Things That
Make Us Smart_ (Cap. 6) Norman tratta la cognizione distribuita _citando
Hutchins_: il mondo ricorda per noi trattenendo lo stato — eco diretta della
membrana `world` — e gli errori condivisi nel sistema diventano occasione di
apprendimento rigenerativo.

## Cognizione distribuita e mente estesa

La **mente estesa** di Clark e Chalmers sostiene che, in determinate condizioni
di accoppiamento, processi esterni possano essere parte della cognizione: il
taccuino di Otto illustra il _parity principle_ e l'_active externalism_. Questa
tesi è distinta dall'analisi di Hutchins della propagazione delle
rappresentazioni; il metodo usa entrambe senza trattarle come una dimostrazione
unica o attribuire capacità cognitive a ogni deposito.

In _Being There_, Clark analizza corpo, ambiente e _scaffolding_. Il «007
principle» invita a sfruttare l'informazione disponibile nel mondo invece di
ricostruirla tutta internamente. La critica del modello mentale come archivio
passivo suggerisce al metodo un criterio di progetto: la KB deve sostenere
comprensione e decisioni nella pratica, compresa una scelta motivata di
attendere. La semplice presenza di file o l'assenza di un'azione immediata non
bastano a giudicare l'accoppiamento cognitivo.

## Il sistema cognitivo del metodo

Nel metodo il sistema cognitivo è l'accoppiamento che prende vita a ogni
sessione: artefatto (la KB, lo strato output, lo strato input) + umano + LLM +
harness tecnico. È dove la cognizione del metodo accade. Non è portabile —
emerge dall'uso e viene ricomposto quando cambiano sessione, agenti o harness.

Questo lo distingue dall'artefatto cognitivo, che invece è portabile: il repo
sopravvive al cambio di modello, al cambio di harness, al cambio di utente. Il
metodo coltiva l'artefatto _perché_ il sistema funzioni; ma l'artefatto e il
sistema non sono la stessa cosa.

## L'asimmetria umano / LLM

Il sistema cognitivo del metodo ha un'asimmetria strutturale tra gli agenti che
leggono l'artefatto. Questo nodo tratta l'effetto dell'asimmetria sul sistema;
la popolazione di agenti, i suoi livelli e la divisione del lavoro vivono in
`agent`. Per l'umano l'artefatto è impalcatura esterna a un modello mentale che
possiede già — un promemoria, un ancoraggio. Per l'LLM l'artefatto è il
principale modello persistente: non porta memoria affidabile tra sessioni e
integra il repo con richiesta corrente, strumenti e segnali del Mondo. Lo user's
model di Norman deriva quindi soprattutto dal system image — l'intero artefatto,
di cui la KB è il nucleo formalizzato — ma non coincide letteralmente con esso.

L'asimmetria ha conseguenze di progetto: l'artefatto deve essere
sufficientemente esplicito per ricostruire il contesto di progetto, senza
richiedere la memoria di sessioni precedenti né ripetere ogni conoscenza
generale già disponibile. Non è un equilibrio facile — è la tensione che motiva
lo sdoppiamento dello strato output nelle due rese per l'agente macchina e per
l'agente umano (cfr. `affordance-signifier`), e che richiede che certe cose
(assunzioni, contesto, ragioni di una decisione) siano esplicite nell'artefatto
anche quando l'umano le ricorderebbe.

## Genus e species

Il sistema cognitivo del metodo si struttura su due gerarchie ortogonali da non
sovrapporre.

_(A) Stack di messa-in-opera_ — il sistema cognitivo per sessione: l'agente
(l'LLM), l'infrastruttura (l'harness) e l'artefatto (l'istanza-di-metodo). I tre
livelli non sono tre "artefatti" dello stesso tipo — sono un agente,
un'infrastruttura e una rappresentazione. Chiamarli tutti con lo stesso nome
cancellerebbe la tesi di portabilità, che vive nel distinguere cosa è portabile
(la rappresentazione) da cosa è sostituibile (agente + harness).

_(B) Discendenza degli artefatti_ — genus → species: il metodo è il genere
(pattern d'artefatto portabile), i progetti adottanti sono le specie (lo stesso
pattern applicato a un dominio specifico). Ogni specie è un artefatto cognitivo
con i propri goal e i propri cicli d'azione. Auto-riferimento: `metodo` è un
artefatto cognitivo il cui dominio è "costruire artefatti cognitivi di dominio"
— di secondo ordine, si applica a sé stesso, ed è insieme il genere e una specie
su cui si può lavorare.

Il legame: l'artefatto nello stack (A) non è una cosa sola — è un _tipo_ con
istanze, cioè la gerarchia (B). Questo dà il vocabolario all'osservatorio
cross-repo: il genere è ciò che generalizza, i tratti di specie sono ciò che
resta locale. La domanda "cosa generalizzare, cosa lasciare locale" del README
diventa precisa.

## Tripartizione

I tre concetti — artefatto, sistema, metodo — si dividono il lavoro in modo
netto:

- _artefatto cognitivo_: la rappresentazione esterna progettata e persistente;
  ciò che il metodo coltiva; portabile
- _sistema cognitivo_: l'accoppiamento dinamico tra artefatto, umano e LLM in
  una sessione; dove la cognizione accade; non portabile
- _metodo_: la pratica con cui si coltiva l'artefatto perché il sistema performi

La distinzione è operativa: dire «il metodo è portabile» significa dire
«l'artefatto è portabile» — il sistema cognitivo no, perché dipende dall'agente
e dall'harness disponibili in quel momento. La tesi di vendor-neutrality e di
sopravvivenza al cambio di modello si regge su questa distinzione.

## Riferimenti

- Edwin Hutchins, _Cognition in the Wild_ (MIT Press, 1995) — fonte primaria sul
  sistema cognitivo come unità di analisi (cfr. la sezione fonti di `world.md`,
  qualità OCR media: verificare le citazioni verbatim sulla scansione). Citare
  per capitolo; cap. 9 per la sintesi (non scambiare le proprietà del sistema
  socioculturale per quelle della mente individuale).
- Andy Clark & David J. Chalmers, «The Extended Mind», _Analysis_ 58(1):7-19,
  1998; Andy Clark, _Being There_ (MIT Press, 1997) — pavimento ontologico della
  mente estesa: active externalism, parity, scaffolding, 007 principle,
  mente-come-controllore. Provenienza nella sezione fonti di `world.md`.
- Donald Norman, «Cognitive Artifacts», in J. Carroll (ed.), _Designing
  Interaction_ (Cambridge University Press, 1991) — definizione dell'artefatto
  cognitivo e della persona-più-artefatto come sistema.
- Donald Norman, _Things That Make Us Smart_ (Addison-Wesley, 1993), Cap. 3
  (rappresentazione, cfr. `kb/cognitive-artifact.md`) e Cap. 6 «Distributed
  Cognition» (la cognizione distribuita di Norman stesso, che cita Hutchins).

Connessioni:

- [cognitive-artifact](cognitive-artifact.md)
- [action-cycle](action-cycle.md)
- [augmentation-system](augmentation-system.md)
- [system-image](system-image.md)
- [affordance-signifier](affordance-signifier.md)
- [knowledge-base](knowledge-base.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
- [agent](agent.md)
