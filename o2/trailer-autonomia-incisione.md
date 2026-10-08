---
sintesi: "Ogni commit dichiara nei trailer se è concordato o autonomo e, se autonomo, il grado di incisione (verde, giallo, rosso), con esempi concreti condivisi col custode prima di diventare canone."
ciclo: dev
---

# Trailer di autonomia e incisione

Il registro di ciò che il battito fa vive nei commit, non in un file md
tenuto a mano: un file scritto a ogni giro genera conflitti tra checkout e
duplica `git log`. Il trailer `Esiti:` c'è già; se ne aggiungono due.

## Proposta da discutere con esempi

- `Autonomia: concordato` (agente e custode in sessione) oppure `agente`
  (giro senza custode).
- `Incisione: verde|giallo|rosso`, solo per i commit dell'agente. Verde è
  raccolta e routine, giallo è applicato ma chiede uno sguardo, rosso è una
  **proposta committata e non applicata**: il commit porta la proposta
  (ad esempio in `o2/` o nel filo), il register resta com'era. Così il
  rosso arriva alla vista e agli altri checkout senza incidere.

Esempi su cui il custode ha chiesto di ragionare prima di decidere:

- un giro che aggiunge grezzo in `i1/` e nessun verdetto cambia → verde;
- un giro che riordina il plan dopo un verdetto nuovo in `i3/` → giallo;
- un giro che vorrebbe cambiare un obiettivo in `goal.md` → rosso, con la
  proposta scritta e `goal.md` intatto.

## Aperto

- I criteri dei colori non vivono qui: vivono nel register dei criteri
  (task «Criteri di autonomia nel trittico costitutivo»). Qui si fissano
  solo forma e lettura dei trailer.
- Criterio verificabile sui file toccati o giudizio dell'agente: il primo si
  controlla, il secondo tende a sottovalutare.
