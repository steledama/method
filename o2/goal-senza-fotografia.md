---
sintesi: "goal.md tiene solo il nord: motivo, obiettivi e segnali come puntatori. Lo stato del lavoro resta nei fili e nel plan, i numeri nella loro fonte; il canone si riscrive e poi si prescrive agli otto."
ciclo: dev
---

# Goal senza fotografia

Verdetto del `compare` del 2026-10-08 sulla sintesi
[churn-goal-adottanti](../i2/churn-goal-adottanti.md): il canone si
contraddice. `kb/goal-register.md` chiede in `goal.md` lo stato del lavoro di
ogni obiettivo; `kb/pace-layering.md` dice che una superficie che mescola un
modello durevole con stato transitorio va riaperta a ogni aggiornamento e
deriva. Il 74% dei commit su `goal.md` negli otto repo tocca solo lo stato. Il
custode decide la direzione: in `goal.md` solo gli obiettivi; i numeri ad
alto churn non si versionano, si versionano le decisioni prese su di essi.

## La forma

- **`goal.md`**: motivo, obiettivi con descrizione, segnali come puntatori
  (quale filo, report o vista misura l'obiettivo). Cambia solo quando cambia
  il nord, e ogni sua modifica è impatto alto (`kb/consent.md`).
- **Stato del lavoro**: dove vive già, il verdetto nel filo `i3/` e il lavoro
  in `o1/plan.md`. Non si ricopia.
- **Numeri**: nella fonte (log, export); la vista li rende al momento dove
  sono derivabili.

## Lavoro

1. Riscrivere `kb/goal-register.md` senza lo stato del lavoro, coi segnali
   come puntatori.
2. Rendere coerenti `kb/goal.md`, `kb/development-goal.md` («casa della
   fotografia») e la Disciplina di `goal.md`, che lo dice «fotografia
   aggiornata in place».
3. Ripulire il `goal.md` di `method`: l'Obiettivo 2 ricopia posizioni e
   prescrizioni che vivono in `i3/audit-adottanti.md` e in
   `o3/prescriptions.md`, ed è già invecchiato.
4. Prescrizione `o3/` agli otto. In `danea-auto` (clean-rate) e `bi`
   (conteggi) resta una scelta locale: come la vista rende i numeri dalla
   fonte, o dove vivono finché non lo fa.

## Aperto

- Il Goal di sviluppo è una posizione auspicata (nord) o una fotografia
  (stato)? `kb/development-goal.md` oggi lo chiama in tutti e due i modi.
- Se la home deve mostrare lo stato per obiettivo, lo ricava dai fili che
  `goal.md` punta, non da `goal.md`.
