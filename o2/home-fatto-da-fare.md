---
sintesi: "La home della vista apre con due sezioni: «fatto», gli ultimi commit con autonomia e colore, e «da fare», scadenze e dipendenze del plan in ordine di data."
ciclo: dev
---

# Home con fatto e da fare

Più autonomia all'agente chiede un controllo che il custode legge in un
colpo d'occhio. La vista web è il luogo: le due sezioni stanno in cima alla
home, prima dei poli Goal e World.

## Le due sezioni

- **Fatto**: gli ultimi 5 commit, con data e ora, titolo, autonomia e
  colore. La fonte è `git log` con i trailer, letto dall'host che pubblica
  dal commit.
- **Da fare**: le prossime mosse in ordine di scadenza, cioè `## Scadenze` e
  le dipendenze `w`/`p` di `o1/plan.md`. Oggi si leggono solo aprendo il
  plan.

## Vincoli

- È un cambio del canone delle viste (`kb/view.md`, builder in `o3/view/`):
  si prescrive agli adottanti come gli altri.
- «Da fare» non dipende da nulla e può partire subito. «Fatto» mostra
  `Esiti:` finché non arrivano i trailer di autonomia e incisione.
- La pubblicazione costruisce da `git archive`: verificare come il builder
  legge la storia senza rompere il contratto del commit pulito.
