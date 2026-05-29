---
data: 2026-05-24
stato: aperto
---

# Formalizza pattern file-dominio in struttura-progetto

`economia` ha tre file di dominio (`stato.md`, `scadenze.md`, `diario.md`) che non appartengono alla ricetta universale ma sono legittimi e specifici del dominio documentale. Il metodo deve rendere esplicito questo pattern: la ricetta ammette componenti locali senza assorbirli nel nucleo portabile.

## Azione

- verificare in `economia` quali di questi file hanno una funzione cognitiva distinta e non sovrapposta a README, log o nodi
- formalizzare in `kb/struttura-progetto.md` il principio: la ricetta include una categoria "componenti locali di dominio" che dichiarano funzione e non duplicano i file root
- aggiungere criteri per distinguere un componente locale sano da drift (duplica README, log o nodi)

## Criterio di chiusura

`kb/struttura-progetto.md` ha una sezione esplicita sui componenti locali di dominio con esempi reali e criteri di distinzione da drift.
