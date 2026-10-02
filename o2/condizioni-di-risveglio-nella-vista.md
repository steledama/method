---
sintesi: "La vista del plan chiude la tabella con un rimando al «plan sorgente» per le dipendenze esterne e le condizioni di risveglio. Le si rende invece nella vista, sotto la tabella, con la stessa resa fedele alla fonte delle liste prescrizioni/percezioni, senza intestazioni cablate. Il rimando, che con presentation/ chiusa su se stessa porterebbe fuori, sparisce."
ciclo: dev
---

# Condizioni di risveglio nella vista del plan

Terzo task della ristrutturazione della presentazione (2026-10-02). Dipende da
[presentazione-autonoma-e-uniforme](presentazione-autonoma-e-uniforme.md):
senza link verso le fonti, il rimando al plan sorgente non ha più dove portare.

## Cosa si rende

- Dopo la tabella del plan, la vista rende quello che segue la tabella in
  `o1/plan.md`: la legenda delle dipendenze esterne (`p<n>`, `w<n>`, con le
  loro condizioni di risveglio) e `## Scadenze`.
- La resa usa la stessa tecnica di `build_lists.py`: AST di Pandoc,
  struttura della fonte conservata (paragrafi, liste, codice), link gestiti
  secondo il compartimento stagno.
- **Nessun nome di intestazione cablato.** È la lezione di
  `liste-o3-i1-fedeli-alla-fonte`: il builder non cerca «Legenda dipendenze
  esterne», prende la fonte per struttura (per esempio tutto quello che
  segue la tabella).
- Legenda e scadenze vanno su una o più slide dopo quella della tabella. Se
  la legenda è lunga, scorre come la tabella (`max-height` + `overflow`).

## Rifiniture da valutare

- Le chiavi nella colonna `Dip.` (`p1`, `w2`) come link alla voce della
  legenda. `kb/plan.md` vuole la chiosa ancorata alla chiave
  (`i3/igiene-stadi-output.md`), quindi l'ancora si ricava dalla chiave e
  non si indovina. Se una chiave in tabella non ha la sua voce in legenda,
  la build rompe.

## Criterio di chiusura

`tasks.html` di `metodo` mostra la legenda di `p1` e la scadenza del
2026-11-01 senza nessun rimando al plan sorgente. Una forma diversa della
legenda (lista invece di paragrafi, come negli adottanti) si rende senza
modificare il builder.
