---
ciclo: runtime
---

# Economia — indice o2/tasks.md sottoutilizzato

Segnale dall'adottante `economia`: la collezione `o2/` aveva un indice interno `o2/tasks.md`, ma il suo contenuto dichiarava che il dettaglio operativo era indicizzato da `o1/plan.md`. In pratica la sezione `## Dettagli task` di `o1/plan.md` duplicava l'indice dei file task, mentre il register dello stadio restava quasi vuoto.

Intervento locale effettuato: `o2/tasks.md` è diventato il vero indice dei task aperti; `o1/plan.md` conserva solo il rimando a `../o2/tasks.md`.

Questione metodologica da valutare: il canone deve chiarire se il footer dei link ai task vive in `o1/plan.md` o nell'indice interno `o2/tasks.md`. La forma attuale dei nodi `plan` e `tasks` conserva una tensione: il plan è descritto come cruscotto leggero, ma anche come punto che indicizza i dettagli.
