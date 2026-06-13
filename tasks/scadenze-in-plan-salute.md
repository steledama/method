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

## Larghezza tabella e riferimenti dipendenze

Nella stessa sessione, la tabella `## Task` di `salute/plan.md` è stata
accorciata con tre accorgimenti, non ancora presenti nella forma canonica del
nodo `plan`:

- vincolo di **larghezza di riga ≈ 80 caratteri** (la riga della tabella,
  pipe e padding inclusi, non solo il titolo) — vicino alla convenzione
  storica delle 80 colonne, portabile a prescindere da quante colonne ha la
  tabella in un dato repo. Per `salute` (colonne `#`, Priorità, Task, Dipende)
  questo dà un titolo massimo di 51 caratteri nella cella `Task`; i titoli più
  lunghi sono abbreviati nella tabella ma restano per intero nel footer
  `## Dettagli task` e nell'H1 del file `tasks/`.
- colonna **Dipende** ridotta a `#n` per dipendenze interne (un'altra riga
  della stessa tabella) o un marcatore `[a]`, `[b]`, … per dipendenze esterne
  (nodi `method`/`kb`, condizioni non-task), con una "Legenda dipendenze
  esterne" subito sotto la tabella che spiega i marcatori.
- le righe di ingest senza file `tasks/` (titoli troppo lunghi se contengono
  il path completo) usano un titolo breve descrittivo in tabella; i path
  completi delle fonti da elaborare sono raccolti in un elenco separato
  `## Fonti da elaborare`, subito dopo `## Dettagli task`.

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
- Il vincolo di larghezza riga (~80 caratteri), la legenda dipendenze `[a]`/`[b]`
  e la sezione `## Fonti da elaborare` sono accorgimenti generalizzabili a
  tutti gli adottanti (tabella `## Task` più stretta e leggibile ovunque), o
  restano specificità locali di `salute` da annotare in
  `confronto-progetti-adottanti`?

## Esito atteso

- Aggiornare il nodo `plan` (`method/kb/plan.md`) con la posizione esplicita
  per le scadenze datate nella pianificazione: variante ammessa (sezione
  `## Scadenze` opzionale) o adattamento locale da annotare altrove.
- Decidere se il vincolo di larghezza riga ≈ 80 caratteri, la legenda
  dipendenze esterne `[a]`/`[b]` e `## Fonti da elaborare` entrano nella forma
  canonica del nodo `plan` (con beneficio per tutti gli adottanti) o restano
  adattamento locale di `salute`.
- Aggiornare `confronto-progetti-adottanti` con l'esito per `salute` (forma
  ora canonica per `## Task`, più eventuale sezione Scadenze) ed `economia`
  (`scadenze.md` separato).

Connessioni:

- [plan](../kb/plan.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
- [tasks](../kb/tasks.md)
