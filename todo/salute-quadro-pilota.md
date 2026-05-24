---
data: 2026-05-24
stato: aperto
---

# Osservazioni dal pilota salute/quadro/

`salute/quadro/` è il primo pilota concreto dello strato output (ponte). Il nodo `kb/ponte.md` è stato scritto prima dell'evidenza completa. Il pilota non deve limitarsi a produrre una sintesi leggibile: deve mostrare se lo strato output genera azioni, fonti di ritorno e aggiornamenti del quadro.

## Azione

- verificare che `salute/quadro/` implementi i tre livelli L1, L2, L3 come descritti in `ponte.md`
- verificare che i file in `quadro/` linkino `metodo/ponte.md` e `metodo/ciclo-azione.md`
- verificare che esista un registro delle azioni aperte, con area, fonte, esito atteso, prossimo controllo e stato
- verificare che l'overview esponga le prossime decisioni, non solo le aree cliniche
- raccogliere almeno 2-3 cicli completi: L2 decisione nel quadro → L3 azione nel mondo → fonte prodotta → aggiornamento KB/scadenze → quadro aggiornato
- raccogliere: cosa funziona, cosa manca, cosa è stato aggiunto rispetto alla specifica teorica
- aggiornare `kb/ponte.md` con le osservazioni empiriche

## Criterio di chiusura

`kb/ponte.md` contiene evidenze concrete dall'uso reale di `quadro/`, non solo la specifica teorica. La tabella "Stato dei progetti adottanti" è aggiornata con dati reali. Il task si chiude solo dopo almeno 2-3 cicli L2→L3→fonte→KB→quadro documentati.
