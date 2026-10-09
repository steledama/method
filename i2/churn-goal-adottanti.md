---
ciclo: dev
---

# Il churn di goal.md viene dallo stato del lavoro più che dai numeri

Sintesi della percezione `i1/fotografie-ad-alto-churn.md` (`0e5c6e8`,
consumata dal verdetto nel task di `6a5ef01`, ora attuato nella
[prescrizione](../o3/goal-senza-fotografia.md)): il custode
propone che in `goal.md` stiano solo gli obiettivi e che le fotografie
numeriche, ad alto churn, escano dal register e forse da git. Qui si misura
quanto e cosa cambia davvero nel `goal.md` degli otto repo.

## Misura

Storia di `goal.md` su `origin/main` dal 2026-08-09 al 2026-10-08, dopo un
`git fetch` del 2026-10-08. Ogni commit è classificato confrontando lo
**scheletro del nord** prima e dopo: motivo (intro), titoli, descrizione
degli obiettivi, titoli in grassetto dei sotto-obiettivi. Se lo scheletro e
il Goal di sviluppo non cambiano, il commit ha toccato solo segnali e stato
del lavoro: lo chiamo «solo fotografia». Tutte le quantità sono **misurate**
sulla storia git; la classificazione è euristica, con sei commit verificati a
mano.

- **Quanto**: 118 commit su `goal.md`, il 9% dei 1.062 commit degli otto
  repo nella finestra. Il peso varia molto: `danea-auto` 20 su 81 (25%),
  `method` 32 su 145 (22%), `crm` 11 su 66, `baserow` 3 su 26, `economia` 8
  su 83, `salute` 13 su 126, `bi` 16 su 230, `nixos` 15 su 305 (5%).
- **Cosa**: 87 commit (74%) sono solo fotografia, 16 toccano solo il Goal di
  sviluppo, 15 (13%) cambiano il nord.
- **Numeri**: dei 87, solo 16 introducono misure copiate da una fonte —
  rapporti, percentuali, conteggi, durate — e sono concentrati in
  `danea-auto` (10, il clean-rate) e `bi` (5, i conteggi della potatura e
  del drift). Negli altri sei repo le misure compaiono in un solo commit.
- **Il resto**: 71 commit cambiano lo stato qualitativo — una prescrizione
  aperta o chiusa, un fronte che passa «a regime», un RPO verificato, un
  fatto datato. In `method` tutti e 29 i commit di sola fotografia sono di
  questa specie; 16 dei 32 commit su `goal.md` di `method` toccano righe su
  prescrizioni o recepimenti, uno stato che vive già in
  `o3/prescriptions.md` e in `i3/audit-adottanti.md`.

## Letture

- **I numeri ad alto churn esistono, ma sono locali.** In `danea-auto` la
  metà dei commit su `goal.md` aggiorna una misura che il log di
  `export_master` già contiene: è il caso della percezione, e lì la
  derivazione al momento della vista toglierebbe la maggior parte del churn.
  Altrove i numeri sono rari.
- **Il churn diffuso è lo stato del lavoro, ed è il canone a chiederlo.**
  `kb/goal-register.md` nella versione misurata chiedeva per ogni obiettivo «lo stato del lavoro che lo
  serve — a regime, event-driven o con un fronte aperto». Lo stato non è un
  numero ma una valutazione, e il custode chiede di versionare le
  valutazioni. Il problema che la misura mostra è un altro: quella
  valutazione vive spesso anche nel filo `i3/`, nel plan o in `o3/`, e
  `goal.md` la ricopia. Il churn viene dalla **seconda copia**, non dalla
  natura del dato.
- **Il nord cambia poco ed è riconoscibile.** 15 commit su 118 toccano lo
  scheletro, e un confronto deterministico sullo scheletro li separa dagli
  altri. Nel contratto allora vigente un criterio di autonomia sul solo file
  avrebbe confuso spesso nord e stato; lo scheletro li separava con i limiti
  sotto. Dopo la separazione dello stato dal register non si trasferisce
  automaticamente quel rapporto al nuovo contratto: restano da distinguere
  modifiche agli scopi e manutenzione dei puntatori ai segnali.

## Limiti

- La regola delle misure è stretta: esclude date, SHA, percorsi, e può
  perdere un rapporto scritto come una data (`24/24`). Il conteggio di 16 è
  un minimo.
- Lo scheletro non distingue un ritocco di forma da un cambio di sostanza:
  dei 15 commit sul nord non si è letto quanti spostino davvero un
  obiettivo.
- Non si è verificato, commit per commit, quale altra superficie porti già
  lo stato ricopiato: la seconda copia è dimostrata in `method` e indicata
  negli altri dal campione.
- Finestra di due mesi, nella quale `baserow` e `danea-auto` sono entrati da
  poco nell'osservatorio.
