---
data: 2026-06-13
stato: bozza
---

# Input

Lo strato input del metodo: il livello che traduce il segnale grezzo del mondo in conoscenza stabile nella KB — l'**arco di valutazione** del ciclo d'azione, che risale dal Mondo alla KB e chiude il ciclo. È il simmetrico dello strato `output` (l'arco di esecuzione, che scende dalla KB al Mondo); la geometria che li accoppia — specchio per altitudine, le due cerniere, i cicli annidati — vive in `ciclo-azione`, non qui.

Lo strato input esiste per una ragione di sicurezza, non di completezza teorica: è il meccanismo per cui l'artefatto può ascoltare il mondo che lo smentisce. Un ciclo con solo output agisce ma non si corregge; è l'arco di input che rende possibile delegare l'azione tenendo l'umano nel loop per ciò che conta (cfr. `goal`, `sistema-cognitivo`).

## I tre stadi dell'input

Il segnale grezzo del mondo ritorna nel sistema e attraversa tre stadi prima di diventare conoscenza stabile:

- **i1 — grezzo** — natura: percezione del segnale esterno; forma: referto, log, export, documento, messaggio; dove vive: `sources/` (o locale al progetto)
- **i2 — distillato** — natura: interpretazione e sintesi; forma: nota di lettura, analisi, estratto commentato; dove vive: `kb/` in `stato: bozza`
- **i3 — formalizzato** — natura: conoscenza stabile o verdetto; forma: nodo KB aggiornato, fonte di verità, input al Goal; dove vive: `kb/` in `stato: maturo`, e `verdict.md` come residuo scritto del Compare

Ogni stadio corrisponde a uno stadio di Norman: i1 = Perceive, i2 = Interpret, i3 = Compare. Il passaggio i2→i3 non è automatico — è il giudizio che decide se un'interpretazione è abbastanza stabile da entrare nella KB. Per questo i2 vive in `kb/` come nodo in `stato: bozza`: la forma è quella del nodo, ma la funzione è ancora di elaborazione. La maturazione `bozza→maturo` è il passaggio i2→i3.

## L'i2 ha bisogno di un substrato

L'i2 (Interpret) non lavora sul grezzo: da centinaia di segnali (i1) non si interpreta nulla. È la **sintesi** — la torta delle spese, il trend, il termometro — il luogo dove l'interpretazione accade. Per questo i2 e o2 sono lo stesso artefatto visto dai due archi (lo specchio o2↔i2): la sintesi è o2 quando la si produce (feedforward, scende), è substrato dell'i2 quando la si legge per interpretare (feedback, risale). La forma segue il dominio: grafica dove i dati sono molti (`economia`, `bi`), testuale dove il dominio è concettuale (`salute`). Vincolo di sicurezza: la sintesi che interpreta dev'essere goal-guidata sulla rilevanza ma neutra sulla valenza, o l'i2 diventa ragionamento motivato e la stessa superficie che dovrebbe far capire finisce per persuadere (cfr. `goal`).

L'i2 ha anche una scala macro: la sintesi periodica che rilegge l'intero artefatto e rivela tensioni non-locali tra nodi, ruolo di `interpretations/` in `method` (cfr. `ciclo-azione`, sezione i2 micro/macro).

## Le due sorgenti di i1, i due modi di i3

L'arco di input del metodo è più ampio dell'arco di valutazione di Norman. i1 ha due sorgenti:

- **feedback** — risposta a un o3, chiude un goal esistente (Norman puro: l'esito dell'azione che si valuta contro l'intenzione);
- **esogeno** — il mondo agisce da sé: busta paga, normativa, alert, referto non sollecitato — e apre spesso un goal _nuovo_.

Per questo i3 ha due modi: **verdetto** (Compare contro un goal esistente, loop noto e delegabile) e **triage/formazione-goal** (per l'esogeno: decidere cosa conta, la cosa meno esternalizzabile — eco di Bainbridge). Il metodo apre così il confine-Mondo come apre il confine-Goal: il mondo non solo risponde, agisce (cfr. `goal`, `mondo`).

Connessioni:

- [output](output.md)
- [ciclo-azione](ciclo-azione.md)
- [goal](goal.md)
- [mondo](mondo.md)
- [knowledge-base](knowledge-base.md)
- [affordance-signifier](affordance-signifier.md)
- [metodo-kb](metodo-kb.md)
