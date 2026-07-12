---
ciclo: dev
---

# Le review comunicano per protocollo post-evento, non per fusione

Ratificato (2026-07-12), dalla valutazione i2→i3 della percezione «le due
review dei bracci sembrano compartimenti stagni» (sollevata dal custode su
`economia`, commit `994a9b5`, consumata da questo filo) e dal pilota
post-evento eseguito lo stesso giorno in `economia`.

Il dubbio del custode: dopo eventi del mondo le due review girano come audit
separati; serviva un doppio movimento verdetti↔piano e un canale che affili
gli scopi (l'«alberello»: mission → goal → piano → task → esecuzioni).

**Verdetto: i compartimenti erano il progetto, non il difetto.** La coppia
simmetrica resta separata — fonderla ricreerebbe la mega-review e il
ragionamento motivato (il piano che giustifica i verdetti e viceversa). Il
difetto reale era duplice: mancava il canale i1 per gli eventi (in
`economia`: le email), e il protocollo tra le review non era mai stato
scritto. Il pilota (skill `email` istituita → cattura → `verdicts-review` →
`plan-review`) ha convalidato:

- l'**ordine post-evento**: percezione → verdetti → piano, la verità prima
  delle priorità;
- gli **handoff** come passo di chiusura: «impatti sul piano» all'andata,
  «verdetti da rivalutare» al ritorno — asimmetrici: l'andata è ordinaria, il
  ritorno è l'eccezione da giustificare al custode (nel pilota è tornato
  vuoto proprio perché l'ordine era giusto);
- l'handoff è **input, non comando**: la review ricevente conserva il
  giudizio (nel pilota: la dipendenza world rimasta tale a dispetto
  dell'attesa puntuale sciolta);
- il canale **verso l'alto esisteva già** e funziona: il passo
  formazione-goal di `verdicts-review` ha prodotto la proposta sull'obiettivo
  4 di `economia` senza scrivere sul register — l'alberello comunica per
  misure verso il basso e proposte verso l'alto, mai per scritture
  automatiche sugli scopi.

Trattamento applicato: protocollo inciso nelle copie canoniche di
`verdicts-review` e `plan-review` (posizione nel protocollo nel cappello,
passo di handoff in chiusura) e nel paragrafo della coppia simmetrica in
`skill.md`. Gli adottanti lo recepiranno al prossimo giro di `method-review`.

Watchpoint aperti: il pattern «email come superficie i1» ha una sola istanza
(`economia`); il secondo segnale atteso è la casella `acquisti@` della skill
`ordini` di `bi` — allora si valuterà nodo o estensione del canone, con in
dote i raffinamenti già emersi nel pilota (un fatto per segnale; flag «già
consumato dal ciclo» quando il segnale è a valle di un ingest già fatto; la
ridondanza tra handoff consecutivi è ciò che preserva il contesto a giri
separati).
