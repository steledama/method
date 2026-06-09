---
data: 2026-06-09
stato: bozza
---

# Matrice del ciclo di azione

Strumento di verifica sul campo della teoria del ciclo di azione: applica gli otto elementi del ciclo — sei atti più due poli, cfr. `ciclo-azione` — a ciascuno dei cinque artefatti (`nixos`, `bi`, `economia`, `salute` e `metodo` stesso) per mettere alla prova l'ipotesi della simmetria invece di darla per scontata. Non è una mappa che illustra la teoria: è un test che può falsificarla. Nasce dalla domanda aperta — la simmetria a otto elementi è una struttura reale che affina lo strumento, o una forzatura elegante che piega la realtà all'esigenza teorica?

> **IL RISCHIO È LA COMPLICITÀ CON SÉ STESSI.** Una matrice che parte cercando simmetria la trova sempre: la ragione motivata fabbrica corrispondenze su misura. Questo strumento vale solo se ogni casella riceve un verdetto onesto con una riga di giustificazione, e solo se «forzato» è un esito _gradito_, non un fallimento da smussare. Se a fine verifica le caselle forzate o vuote restano molte, l'ipotesi della simmetria è sbagliata e va abbandonata, non difesa. Lo strumento serve a uccidere la teoria se lo merita, non a incoronarla.

## Scala di verdetto

- **S — solido**: l'elemento esiste nell'artefatto, ben formato e riconoscibile senza forzature.
- **D — debole**: esiste ma è sotto-sviluppato, implicito o sparso.
- **F — forzato**: l'accostamento regge solo piegando la realtà alla teoria; è il verdetto che falsifica.
- **? — da verificare**: non ancora ispezionato sul campo nel repo. Non un giudizio, un debito.

## La matrice — primo passaggio

Riempito solo dove esiste grounding diretto (`output.md`, `goal.md`, `mondo.md`, ispezione delle `presentations/`); il resto è marcato `?` per onestà, non per cautela.

| Elemento       | `nixos` | `bi` | `economia` | `salute` | `metodo` |
| -------------- | ------- | ---- | ---------- | -------- | -------- |
| Goal (polo)    | S       | S    | S          | S        | S        |
| Plan · o1      | S       | S    | S          | D        | S        |
| Specify · o2   | D       | S    | D          | D        | D        |
| Perform · o3   | S       | S    | S          | S        | S        |
| Perceive · i1  | S       | S    | S          | S        | S        |
| Interpret · i2 | ?       | ?    | ?          | D        | D        |
| Compare · i3   | ?       | ?    | D          | D        | D        |
| Mondo (polo)   | S       | S    | S          | S        | S        |

Conteggio: 25 S, 10 D, 5 ?, 0 F.

## Cosa dice il primo passaggio (lettura spietata)

Il conteggio sembra confortante. Non lo è, e leggerlo come una vittoria sarebbe esattamente la complicità contro cui avverte il riquadro.

- **Venti dei venticinque S sono quasi tautologici.** Le quattro righe-bordo — Goal, Perform (o3), Perceive (i1), Mondo — sono solide _perché le abbiamo definite noi_ per ciascun artefatto in `goal.md` e `mondo.md`. Un elemento che combacia perché l'abbiamo ritagliato su misura non è prova della simmetria: è la simmetria messa lì a mano. Vanno scontate.
- **Tolti i bordi, l'interno è in larga parte debole o vuoto.** Plan (4 S, 1 D), Specify/o2 (1 S, 4 D), Interpret/i2 (2 D, 3 ?), Compare/i3 (3 D, 2 ?). La teoria regge meglio proprio dove è meno falsificabile, e gli artefatti sono fragili proprio dove il test morde. Questo non conferma la simmetria: dice due cose diverse — che finora è più impalcatura definitoria che risultato empirico, e che gli artefatti condividono una debolezza reale negli stadi mediani.
- **Lo zero forzati è sospetto, non rassicurante.** Le caselle più a rischio di analogia forzata — i2 e i3, l'interpretazione e il confronto — sono quelle ancora vuote. Non abbiamo guadagnato un solo «F» perché non abbiamo ancora fatto la parte difficile. Il primo `F` onesto varrà più di tutti gli `S`.
- **`o2` è la colonna-spia.** Debole in quattro artefatti su cinque (solo `bi` con Reveal.js la salva). È lo strato di rappresentazione/decisione: la conferma che il collo di bottiglia di tutti gli artefatti è la vista che dovrebbe generare azione. È la stessa diagnosi della stasi di `salute`, l'unico artefatto debole su _entrambi_ o1 e o2 — quasi tutto l'arco di output assente, eppure o3 «medio»: agisce per intuizione senza che l'artefatto lo sostenga, che è il profilo del loop a vuoto.
- **`metodo` non è stato segnato tutto-S di proposito.** Un artefatto che dà il massimo a sé stesso si sta adulando. Anche così sta in alto, e proprio per questo merita la revisione esterna più dura, non la più indulgente.

## Protocollo di riempimento

Le caselle `?` e i verdetti deboli si verificano sul campo, non a tavolino qui. Il luogo della verifica è la prima slide di ciascun artefatto — il suo autoritratto attraverso i sei atti e i due poli, applicati al proprio dominio: dove l'accostamento è debole o forzato, tanto meglio, costringe a guardare l'artefatto in modo analitico. `metodo` non orchestra questo lavoro nei repo adottanti (cfr. `confronto-progetti-adottanti`): ogni repo riempie la propria colonna, e il verdetto risale qui come fotografia aggregata. Questo nodo resta `bozza` finché le righe i2 e i3 non sono ispezionate in tutti e cinque.

Connessioni:

- [ciclo-azione](ciclo-azione.md)
- [mondo](mondo.md)
- [goal](goal.md)
- [output](output.md)
- [system-image](system-image.md)
- [confronto-progetti-adottanti](confronto-progetti-adottanti.md)
- [fedelta-cognitiva](fedelta-cognitiva.md)
