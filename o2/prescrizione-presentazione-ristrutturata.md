---
sintesi: "Chiusura della ristrutturazione della presentazione: una sola prescrizione o3 che porta ai sei adottanti i builder in o3/presentation/, stile unico, accento e sigla di progetto, compartimento stagno, revisione dei verdetti contro gli obiettivi, indice dei Confronti, condizioni di risveglio nella vista e server LAN. Ogni /method locale la recepisce e mappa l'ultimo miglio."
ciclo: dev
---

# Prescrizione della presentazione ristrutturata

Ultimo task della ristrutturazione della presentazione (2026-10-02). Si
scrive dopo che gli altri task si sono chiusi in `metodo`:
`presentazione-autonoma-e-uniforme` (chiuso: canone in `kb/presentation.md`),
`revisione-verdetti-contro-obiettivi` (chiuso),
`indice-dei-confronti` (chiuso),
`condizioni-di-risveglio-nella-vista` (chiuso)
e `server-lan-della-presentazione` (chiuso).

## Perché una prescrizione sola

I cambi di resa toccano gli stessi builder e lo stesso CSS. Se ogni
adottante li recepisse uno alla volta, aprirebbe i fork più volte e
passerebbe per stati intermedi incoerenti, per esempio uno stile nuovo con
i link ancora verso le fonti. Un solo runbook, con note per repo, li porta
insieme (`o3/prescriptions.md`, «Divisione del lavoro»).

La revisione dei verdetti non è resa grafica: è la parte che pesa di più e
che può cambiare i progetti (fili chiusi, motivazioni spostate in `kb/`,
obiettivi mancanti in `goal.md`). Nel runbook va per prima, perché
l'indice dei Confronti rende quello che decide.

## Indizi per repo, da verificare sul posto

- **`nixos`:** è la fonte dello stile. Builder da `o3/tools/` a
  `o3/presentation/`. Sposta le classi di diagramma nel
  CSS locale, accento #c2410c, sigla «NixOS», in inglese. Gli arriva anche
  il segnale per aprire la porta del server (8765) solo verso la LAN su
  `svezia` e `deck`: verificato il 2026-10-02, il firewall dei
  `home-clients` è attivo e la porta non è ammessa, quindi da un altro PC il
  server non risponde finché `nixos` non la dichiara.
- **`bi`, `crm`:** passano dallo stile sketch al CSS unico. Accento #0f766e
  per `bi` e #a16207 per `crm`, sigle «BI» e «CRM», in italiano. I builder
  si spostano da `o3/tools/` a `o3/presentation/`.
- **`danea-auto`:** come sopra, con accento #7e22ce e sigla «Danea». I
  builder si spostano da `o3/` a `o3/presentation/`. `build.sh` e server
  vanno collaudati su Windows (`danea2`).
- **`economia`, `salute`:** hanno un renderer proprio. Per loro valgono
  accento (#15803d, #be123c) e sigla sulle superfici che hanno, e
  compartimento stagno e server se servono la cartella. Il resto può essere
  una divergenza motivata.
- **Tutti:** revisione dei propri fili `i3/` contro il proprio `goal.md`,
  col criterio inciso in `kb/verdict.md` (confronto vero, motivazione da
  spostare, cursore). Ne esce `obiettivo:` nel frontmatter. Il giudizio
  spetta al `/method` dell'adottante, non a `metodo`. Le skill locali che
  citano i path dei builder si riallineano su `o3/presentation/build.py`.
- **Il contratto i3 × goal sui sei, oggi** (prova a secco in sola lettura,
  2026-10-02): nessun adottante ha ancora `obiettivo:` nei fili, quindi la
  build li fermerebbe tutti. Le violazioni sono 7 in `nixos`, `bi` ed
  `economia`, 8 in `salute`, 3 in `crm` e 5 in `danea-auto`. In `bi` il
  cursore `i3/allineamento-metodo.md` è anche fuori indice. Il cursore
  dichiara un obiettivo come ogni altro file di `i3/`: negli adottanti la
  sua `misura:` era già il Goal di sviluppo.

## Criterio di chiusura

La prescrizione sta in `o3/` con la sua voce d'indice, e il task si consuma
quando è scritta. Il recepimento nei sei lo segue il battito `/adottanti`, e
la prescrizione si pota quando ogni adottante ha un esito.
