---
data: 2026-06-13
stato: aperto
---

# Documentare la sezione Scadenze di plan.md in salute

Il 2026-06-13, in `salute`, `scadenze.md` (tabella di appuntamenti sanitari
datati, già convertita in elenco per la regola "tabelle vs elenchi") è stata
assorbita in `plan.md` come sezione `## Scadenze`. Nella stessa sessione
`salute/plan.md` è stato riportato alla forma tabellare canonica (`# · Priorità
· Task · Dipende da` + footer "Dettagli task" per titolo), che prima non
seguiva (usava sezioni `## Alta`/`## Media`/`## Bassa`). Restano quindi due
sezioni in `plan.md`: `## Task` (tabella canonica) e `## Scadenze` (elenco
cronologico di appuntamenti sanitari).

## Cosa NON fare in salute

`salute/plan.md` non deve contenere la descrizione di come è strutturato il
file e perché contiene entrambe le sezioni: questa è la responsabilità del
nodo metodo `plan`, applicata uniformemente — "cambiare la forma è un edit
solo, ereditato da tutti gli adottanti". `salute/plan.md` ora ha solo l'intro
minimale comune (cfr. `economia/plan.md`) più le due sezioni.

## Tensione con la forma canonica

`plan.md` (nodo metodo) descrive oggi solo `## Task` (tabella) + `## Dettagli
task` (footer). Non prevede una sezione "Scadenze". `salute` ha ora due adottanti
con un componente calendariale (cfr. anche `economia`, che però tiene
`scadenze.md` separato da `plan.md`, componente locale aggiuntivo per
`confronto-progetti-adottanti`). `salute` ha scelto invece di integrare le
scadenze datate dentro `plan.md`, motivazione locale: task e scadenze sono due
facce della stessa pianificazione e si influenzano a vicenda (una scadenza
vicina può alzare la priorità di un task collegato, e viceversa).

## Domande da chiarire

- La sezione `## Scadenze` di `salute/plan.md` è un adattamento locale da
  annotare in `confronto-progetti-adottanti` (variante della forma canonica
  per domini con componente calendariale), o il nodo `plan` dovrebbe ammettere
  esplicitamente una sezione opzionale "Scadenze" dopo `## Dettagli task` per
  i domini che la richiedono?
- Se si generalizza, va chiarito il criterio: quando un dominio ha scadenze
  datate che interagiscono con le priorità dei task (`salute`), la sezione
  vive in `plan.md`; quando ha solo un calendario di adempimenti non
  necessariamente legato alle priorità (`economia`), resta in un file
  separato come `scadenze.md`? O è solo preferenza locale?

## Esito atteso

- Aggiornare il nodo `plan` (`method/kb/plan.md`) con la posizione esplicita
  per le scadenze datate nella pianificazione: variante ammessa (sezione
  `## Scadenze` opzionale) o adattamento locale da annotare altrove.
- Aggiornare `confronto-progetti-adottanti` con l'esito per `salute` (forma
  ora canonica per `## Task`, più eventuale sezione Scadenze) ed `economia`
  (`scadenze.md` separato).

Connessioni:

- [plan](../kb/plan.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
- [tasks](../kb/tasks.md)
