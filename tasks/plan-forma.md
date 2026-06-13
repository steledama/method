---
data: 2026-06-13
stato: aperto
---

# Forma canonica di `plan.md`: scadenze e colonne

Emerso da salute (2026-06-13) e raffinato in sessione. Aggiorna il nodo `plan`
(la forma è descritta una volta sola lì, ereditata da tutti gli adottanti) su
quattro punti. Tutti servono lo stesso fine: una tabella `## Task` più stretta e
una pianificazione che integra le scadenze datate.

## 1. Sezione `## Scadenze` (ammessa, opzionale)

Le scadenze datate e i task sono i due bracci di "cosa deve succedere": i task
sono il _feedback_ (ciò che scegliamo di fare), le scadenze l'_esogeno_ (il mondo
che impone una data — l'IMU). Cfr. le due sorgenti di i1 in `input.md`. Tenerli
in una sola vista supervisionabile rende azionabile l'accoppiamento: una scadenza
vicina alza la priorità del task collegato.

Il nodo `plan` ammette una sezione `## Scadenze` **opzionale** dopo `## Dettagli
task`, con **discriminante stretto** per non far diventare `plan.md` un'agenda:
le scadenze entrano in `plan.md` solo quando **interagiscono con la priorità dei
task** (salute); un calendario di adempimenti slegato dalle priorità resta in
file separato (`scadenze.md`, economia). Da annotare in
`confronto-progetti-adottanti`.

## 2. Togliere la colonna `Priorità`

Oggi il nodo tiene separati `#` (ordine effimero) e `Priorità` (importanza). A
video sono ridondanti: nel caso **non bloccato** l'ordine di esecuzione _è_
l'importanza; nel caso **bloccato** la colonna `Dipende` spiega già il perché.
`Priorità` è derivabile da `# + Dipende` (basso senza dipendenza = meno
importante; basso con dipendenza = importante ma bloccato). Si toglie la colonna
e si guadagna larghezza per il titolo. Registrare nel nodo il modello: **ordine +
dipendenze codificano la priorità**.

## 3. Intestazione ultima colonna → `Dip.`

`Dipende da` spreca larghezza. Accorciare a `Dip.` (o simbolo `↑` che punta alla
riga da cui dipende). Tabella risultante: `# · Task · Dip.`

## 4. Legenda dipendenze e fonti da elaborare

Già in uso in salute, da valutare per la forma canonica:

- colonna `Dip.`: `#n` per dipendenze interne, marcatori `[a]`, `[b]`, … per
  quelle esterne (nodi/condizioni non-task), con "Legenda dipendenze esterne"
  sotto la tabella. Sostituisce il "testo libero" attuale → più stretto.
- righe di ingest senza file `tasks/`: titolo breve in tabella, path completi
  delle fonti in un elenco `## Fonti da elaborare` dopo `## Dettagli task`
  (stesso principio del footer: dettaglio voluminoso fuori dalle celle).

Il vincolo di **larghezza riga ≈ 80 caratteri** resta **guida**, non regola: il
numero esatto di caratteri-titolo dipende da quante colonne ha il repo (cosa che
il nodo dice già variare).

## Deliverable

- aggiornare `kb/plan.md`: sezione `## Scadenze` opzionale + discriminante; drop
  `Priorità` (ordine+dipendenze codificano la priorità); intestazione `Dip.`;
  legenda esterne `[a]`/`[b]`; `## Fonti da elaborare`; guida larghezza ~80.
- applicare la nuova forma al `plan.md` di method stesso (dogfooding), in
  un'unica mossa col nodo per non creare uno stato intermedio incoerente.
- `confronto-progetti-adottanti`: salute (forma canonica + sezione Scadenze),
  economia (`scadenze.md` separato).

Connessioni:

- [plan](../kb/plan.md)
- [input](../kb/input.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
- [tasks](../kb/tasks.md)
