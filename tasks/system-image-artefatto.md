---
data: 2026-06-22
stato: aperto
sintesi: "Il system image è l'intero artefatto, non la KB; la KB ne è il nucleo di conoscenza formalizzata. Allineare system-image, cognitive-system e action-cycle in una passata."
---

# Unificare il system image sull'artefatto

## Problema

Emerso rivedendo `action-cycle` (sessione 2026-06-22). Il nodo usa «KB» in due
sensi a poche righe di distanza:

- **senso largo** (riga ~37): «La KB è il _system image_ di Norman… due medium
  persistenti — la KB all'interno, il Mondo all'esterno». Qui KB = tutto il
  deposito interno = il modello mentale dell'agente.
- **senso stretto** (sezione «I due medium e i prodotti del loop», riscritta in
  questa sessione): la KB è una _regione_ dell'artefatto — la conoscenza
  formalizzata vicina al polo Goal — mentre i prodotti degli atti
  (o1→`plan.md`, o2→`tasks/`, o3→`prescriptions/`, i1→`perceptions/`…) sono
  sparsi nell'intero artefatto, non in `kb/`.

Il senso largo appiattisce il ciclo verso il polo Goal (dove sta la KB) — proprio
l'errore che la revisione della sezione prodotti ha corretto a valle adottando
«artefatto» come medium interno. Resta da correggerlo a monte, e la correzione
ricade su altri nodi: per questo è un task, non un edit locale.

## Tesi da ratificare

Il **system image** — ciò che l'agente legge per costruirsi il modello — è
l'**intero artefatto** (README, `plan.md`, `tasks/`, `kb/`, le collezioni-stadio,
…), non la sola `kb/`. È la lettura fedele a Norman (il system image è _tutto ciò
che il sistema presenta_) e al fatto che l'LLM legge l'intero repo, non solo i
nodi. La **KB è il nucleo di conoscenza formalizzata** dell'artefatto, non il suo
sinonimo.

## Nodi da allineare (una passata sola)

- `system-image` — nodo titolare: il system image è l'artefatto; la KB ne è il
  nucleo formalizzato.
- `cognitive-system` — riga ~28: «Per l'LLM la KB _è_ il modello mentale… lo
  user's model coincide col system image» → riformulare su «artefatto», o
  esplicitare che lì «KB» è il senso largo.
- `action-cycle` — più istanze, non solo riga ~37 («La KB è il _system image_…
  la KB all'interno»): anche la descrizione degli archi («output … che scende
  dalla KB al Mondo … input … che risale dal Mondo alla KB») e «Lo specchio per
  altitudine» (o1↔i3 «alla KB») fanno coincidere il medium interno con la sua
  sola regione alta. Decidere la forma coerente — «l'artefatto è il system
  image, di cui la KB è il nucleo formalizzato», e gli archi corrono tra il Goal
  (apice) e il Mondo (fondo) — e applicarla a tutte le occorrenze.

## Cautela

Prima di propagare, verificare che `knowledge-base`, `output`, `input` e gli altri
nodi che nominano la KB-come-medium non poggino sul senso largo; se sì, entrano
nella stessa passata. Audit `tools/kb_tools.py` pulito a chiusura.

## Criterio di chiusura

I nodi coinvolti dicono la stessa cosa su system-image / KB / artefatto; nessun
residuo di «KB» in senso largo dove si intende l'intero medium interno; audit
senza link rotti.
