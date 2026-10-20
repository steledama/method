---
stato: bozza
---

# Interpret (i2)

Interpret trasforma il segnale catturato in significato senza ancora fissare il
verdetto. Produce note e sintesi che dichiarano fonti, assunzioni e incertezza.
La rilevanza è guidata dai goal; la valenza resta sospesa per evitare che la
sintesi diventi persuasione.

`i2/` raccoglie sintesi multi-nodo che interpretano i segnali; il racconto
curato dell'artefatto vive in `presentation/` (`presentation`). Un nodo KB in stato
`bozza` può invece ospitare un concetto ancora in maturazione. Il passaggio a
`compare` richiede giudizio: nessuna interpretazione diventa conoscenza stabile
automaticamente.

Ogni ipotesi in attesa dichiara **orizzonte e riscontro con fonte**, ed è
raggiungibile da `eval`. L'orizzonte può essere una data, un evento o una
ricorrenza di riesame; il riscontro dichiara cosa osservare e dove verificarlo,
anche quando non è ancora disponibile. Il riesame resta dovuto anche senza
nuovi segnali; una data trascorsa non risolve da sola l'ipotesi.

Si aggiunge il presidio dove manca. Un filo con criterio, conteggio e data
può già soddisfare la regola; non servono facet, contenitori separati o
ipotesi da produrre in ogni collezione. Una collezione senza ipotesi è
legittima. Lo stato di maturità di un nodo non sostituisce il presidio di
una sua ipotesi ancora in attesa.

Le ipotesi più insidiose sono quelle **non dichiarate**: un «perché», un
«quindi», una previsione o una generalizzazione da pochi casi scritti come
fatti, dentro un task, un filo o un messaggio di commit. Si cercano dalla
forma, non dall'introspezione, in ciò che un giro scrive o tocca: la forma
segnala il candidato, la prova è se l'affermazione va oltre i dati. Un
«quindi» che è aritmetica su misure è una derivazione e dichiara solo la
provenienza; una spiegazione causale, un'attesa sul futuro o una conclusione
che aggiunge un'assunzione è un'ipotesi, e va nel presidio con affermazione,
provenienza, cosa la smentirebbe e orizzonte. Un task può rimandare a
un'ipotesi ma non ospitarla: il riesame di `interpret` non lo rilegge. Quando cade si cita la
formulazione e la si segna smentita, senza riscriverla in silenzio: la
smentita è informazione sul modello, non solo sul dato. Il caso tipo è una
tesi causale scritta in un task come spiegazione ovvia e smentita dal dato
del giro successivo, senza che nessuno dei due giri la registrasse come
interpretazione.

Connessioni:

- [input](input.md)
- [perceive](perceive.md)
- [compare](compare.md)
- [goal](goal.md)
- [source-of-truth](source-of-truth.md)
- [presentation](presentation.md)
