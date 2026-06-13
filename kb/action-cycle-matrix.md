---
data: 2026-06-09
stato: bozza
---

# Action cycle matrix

Strumento di verifica sul campo della teoria del ciclo di azione: applica gli otto elementi del ciclo — sei atti più due poli, cfr. `action-cycle` — a ciascuno dei cinque artefatti (`nixos`, `bi`, `economia`, `salute` e `metodo` stesso) per mettere alla prova l'ipotesi della simmetria invece di darla per scontata. Non è una mappa che illustra la teoria: è un test che può falsificarla. Nasce dalla domanda aperta — la simmetria a otto elementi è una struttura reale che affina lo strumento, o una forzatura elegante che piega la realtà all'esigenza teorica?

> **IL RISCHIO È LA COMPLICITÀ CON SÉ STESSI.** Una matrice che parte cercando simmetria la trova sempre: la ragione motivata fabbrica corrispondenze su misura. Questo strumento vale solo se ogni casella riceve un verdetto onesto con una riga di giustificazione, e solo se «forzato» è un esito _gradito_, non un fallimento da smussare. Se a fine verifica le caselle forzate o vuote restano molte, l'ipotesi della simmetria è sbagliata e va abbandonata, non difesa. Lo strumento serve a uccidere la teoria se lo merita, non a incoronarla.

## Scala di verdetto

- **S — solido**: l'elemento esiste nell'artefatto, ben formato e riconoscibile senza forzature.
- **D — debole**: esiste ma è sotto-sviluppato, implicito o sparso.
- **F — forzato**: l'accostamento regge solo piegando la realtà alla teoria; è il verdetto che falsifica.
- **? — da verificare**: non ancora ispezionato sul campo nel repo. Non un giudizio, un debito.

## La matrice — primo passaggio

Riempito solo dove esiste grounding diretto (`output.md`, `goal.md`, `world.md`, ispezione delle `interpretations/`); il resto è marcato `?` per onestà, non per cautela.

- **Goal (polo)** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Plan · o1** — `nixos`: S; `bi`: S; `economia`: S; `salute`: D; `metodo`: S
- **Specify · o2** — `nixos`: D; `bi`: S; `economia`: D; `salute`: D; `metodo`: D
- **Perform · o3** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Perceive · i1** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S
- **Interpret · i2** — `nixos`: D; `bi`: S; `economia`: D; `salute`: D; `metodo`: D
- **Compare · i3** — `nixos`: D; `bi`: S; `economia`: S; `salute`: D; `metodo`: S
- **Mondo (polo)** — `nixos`: S; `bi`: S; `economia`: S; `salute`: S; `metodo`: S

Conteggio: 29 S, 11 D, 0 ?, 0 F (dopo aver riempito i2/i3 — vedi sotto).

## Cosa dice il primo passaggio (lettura spietata)

Il conteggio sembra confortante. Non lo è, e leggerlo come una vittoria sarebbe esattamente la complicità contro cui avverte il riquadro.

- **Venti dei ventinove S sono quasi tautologici.** Le quattro righe-bordo — Goal, Perform (o3), Perceive (i1), Mondo — sono solide _perché le abbiamo definite noi_ per ciascun artefatto in `goal.md` e `world.md`. Un elemento che combacia perché l'abbiamo ritagliato su misura non è prova della simmetria: è la simmetria messa lì a mano. Vanno scontate.
- **Tolti i bordi, l'interno è in larga parte debole.** Plan (4 S, 1 D), Specify/o2 (1 S, 4 D), Interpret/i2 (1 S, 4 D), Compare/i3 (3 S, 2 D). i2 e i3, prima vuote, sono ora riempite mappando su artefatti che _esistono davvero_ — la sintesi (i2) e `verdict.md` (i3) — non per relabeling: è teoria che regge il test sull'arco di input. Ma il risultato non è un trionfo di simmetria, è una diagnosi: l'interno è debole, e la debolezza è la stessa ovunque — la rappresentazione (o2/i2) e la disciplina del verdetto (i3).
- **Lo zero forzati ha ora un significato diverso.** Riempite i2 e i3, nessuna casella ha richiesto di piegare la realtà: il modello ha mappato su artefatti reali (sintesi, `verdict.md`). È un risultato — il ciclo è descrittivamente adeguato a questa classe di repo — ma resta provvisorio per una ragione circolare: questi repo li abbiamo già plasmati col metodo. Il vero test esterno è un repo costruito _senza_ il metodo: il ciclo vi mapperebbe ancora? Finché non lo proviamo, lo zero-forzati è incoraggiante, non conclusivo. Il primo `F` onesto, quando arriverà, varrà più di tutti gli `S`.
- **`o2` è la colonna-spia.** Debole in quattro artefatti su cinque (solo `bi` con Reveal.js la salva). È lo strato di rappresentazione/decisione: la conferma che il collo di bottiglia di tutti gli artefatti è la vista che dovrebbe generare azione. È la stessa diagnosi della stasi di `salute`, l'unico artefatto debole su _entrambi_ o1 e o2 — quasi tutto l'arco di output assente, eppure o3 «medio»: agisce per intuizione senza che l'artefatto lo sostenga, che è il profilo del loop a vuoto.
- **`metodo` non è stato segnato tutto-S di proposito.** Un artefatto che dà il massimo a sé stesso si sta adulando. Anche così sta in alto, e proprio per questo merita la revisione esterna più dura, non la più indulgente.

## Protocollo di riempimento

I verdetti deboli e quelli riempiti per ragionamento si verificano sul campo, non a tavolino qui. Il luogo della verifica è la prima slide di ciascun artefatto — il suo autoritratto attraverso i sei atti e i due poli, applicati al proprio dominio: dove l'accostamento è debole o forzato, tanto meglio, costringe a guardare l'artefatto in modo analitico. `metodo` non orchestra questo lavoro nei repo adottanti (cfr. `adopter-comparison`): ogni repo riempie la propria colonna, e il verdetto risale qui come fotografia aggregata. Le righe i2/i3 sono ora riempite per ragionamento (mappano su artefatti reali); questo nodo resta `bozza` finché la verifica esterna repo-per-repo non le conferma — o le smentisce.

Connessioni:

- [action-cycle](action-cycle.md)
- [world](world.md)
- [goal](goal.md)
- [output](output.md)
- [system-image](system-image.md)
- [adopter-comparison](adopter-comparison.md)
- [cognitive-fidelity](cognitive-fidelity.md)
