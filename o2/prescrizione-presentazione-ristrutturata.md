---
sintesi: "Chiusura della ristrutturazione della presentazione: una sola prescrizione o3 che porta ai sei adottanti stile unico, accento e sigla di progetto, compartimento stagno, indice dei Confronti con obiettivo verificato, condizioni di risveglio nella vista e server LAN. Ogni /method locale la recepisce e mappa l'ultimo miglio."
ciclo: dev
---

# Prescrizione della presentazione ristrutturata

Ultimo task della ristrutturazione della presentazione (2026-10-02). Si
scrive dopo che i quattro task di implementazione si sono chiusi in `metodo`:
[presentazione-autonoma-e-uniforme](presentazione-autonoma-e-uniforme.md),
[indice-dei-confronti](indice-dei-confronti.md),
[condizioni-di-risveglio-nella-vista](condizioni-di-risveglio-nella-vista.md)
e [server-lan-della-presentazione](server-lan-della-presentazione.md).

## Perché una prescrizione sola

I quattro cambi toccano gli stessi builder e lo stesso CSS. Se ogni
adottante li recepisse uno alla volta, aprirebbe i fork quattro volte e
passerebbe per stati intermedi incoerenti, per esempio uno stile nuovo con
i link ancora verso le fonti. Un solo runbook, con note per repo, li porta
insieme (`o3/prescriptions.md`, «Divisione del lavoro»).

## Indizi per repo, da verificare sul posto

- **`nixos`:** è la fonte dello stile. Sposta le classi di diagramma nel
  CSS locale, accento #c2410c, sigla «NixOS», in inglese. Gli arriva anche
  il segnale per aprire la porta del server solo verso la LAN su `svezia`
  e `deck`.
- **`bi`, `crm`:** passano dallo stile sketch al CSS unico. Accento #0f766e
  per `bi` e #a16207 per `crm`, sigle «BI» e «CRM», in italiano. I builder
  stanno in `o3/tools/`.
- **`danea-auto`:** come sopra, con accento #7e22ce e sigla «Danea». I
  builder stanno in `o3/`. Il server va collaudato su Windows (`danea2`).
- **`economia`, `salute`:** hanno un renderer proprio. Per loro valgono
  accento (#15803d, #be123c) e sigla sulle superfici che hanno, e
  compartimento stagno e server se servono la cartella. Il resto può essere
  una divergenza motivata.
- **Tutti:** `obiettivo:` nel frontmatter dei fili `i3/`. Il giudizio su
  quale obiettivo dare a ogni filo spetta all'adottante.

## Criterio di chiusura

La prescrizione sta in `o3/` con la sua voce d'indice, e il task si consuma
quando è scritta. Il recepimento nei sei lo segue il battito `/adottanti`, e
la prescrizione si pota quando ogni adottante ha un esito.
