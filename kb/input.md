---
data: 2026-06-13
stato: bozza
---

# Input

Nota-struttura dello strato input del metodo: l'**arco di valutazione** del ciclo d'azione, che risale dal Mondo al Goal e chiude il ciclo. Non descrive i singoli stadi — vivono come atomi: `perceive` (i1), `interpret` (i2), `compare` (i3) — ma indicizza l'arco e tiene le tensioni che corrono _tra_ gli stadi e che nessun atomo possiede da solo. È il simmetrico dello strato `output` (l'arco di esecuzione); la geometria che li accoppia — specchio per altitudine, le due cerniere, i cicli annidati — vive in `action-cycle`.

Lo strato input esiste per una ragione di sicurezza, non di completezza teorica: è il meccanismo per cui l'artefatto può ascoltare il mondo che lo smentisce. Un ciclo con solo output agisce ma non si corregge; è l'arco di input che rende possibile delegare l'azione tenendo l'umano nel loop per ciò che conta (cfr. `goal`, `cognitive-system`).

## I tre atomi dell'arco

Il segnale grezzo del mondo ritorna nel sistema e attraversa tre stadi prima di diventare conoscenza stabile, ciascuno un atomo:

- **`perceive` (i1)** — cattura versionata e valenza-neutra del Perceive; vive in `perceptions/`;
- **`interpret` (i2)** — distillato e sintesi, dove l'interpretazione accade; nodo `kb/` in `stato: bozza`, collezione `interpretations/`;
- **`compare` (i3)** — conoscenza formalizzata o verdetto; nodo `kb/` `maturo` e `verdict.md`.

Ogni stadio corrisponde a uno stadio di Norman: i1 = Perceive, i2 = Interpret, i3 = Compare.

## Le due sorgenti di i1, i due modi di i3

La tensione che attraversa l'arco intero: l'arco di input del metodo è **più ampio** dell'arco di valutazione di Norman. i1 ha due sorgenti — **feedback** (risposta a un o3, chiude un goal esistente: Norman puro) ed **esogeno** (il mondo agisce da sé: busta paga, normativa, alert, referto non sollecitato, e apre spesso un goal _nuovo_). Da qui i due modi di i3, verdetto e triage/formazione-goal (cfr. `compare`): è la sorgente che decide il modo. Il metodo apre così il confine-Mondo come apre il confine-Goal (cfr. `world`, `goal`).

## Lo specchio con l'output

i2 e o2 sono lo stesso artefatto visto dai due archi: la sintesi è o2 quando la si produce (feedforward, scende) ed è substrato dell'i2 quando la si legge per interpretare (feedback, risale). I tre specchi per altitudine — o3↔i1, o2↔i2, o1↔i3 — corrispondono ai tre livelli di elaborazione e si sviluppano in `processing-layers`, non qui.

Connessioni:

- [output](output.md)
- [perceive](perceive.md)
- [interpret](interpret.md)
- [compare](compare.md)
- [action-cycle](action-cycle.md)
- [goal](goal.md)
- [world](world.md)
- [knowledge-base](knowledge-base.md)
- [processing-layers](processing-layers.md)
- [cognitive-artifact-design](cognitive-artifact-design.md)
