---
description: Revisione dei fili i3 contro goal.md e i segnali reali; bonifica del plan dalla narrativa di stato
user-invocable: true
---

Rivedi i fili `i3/` come supervisione corrente della valutazione. È la skill
simmetrica di `plan-review`: quella tiene onesto il piano (braccio di
esecuzione), questa tiene onesto il confronto (braccio di valutazione); il
register `goal.md` è la cerniera che entrambe controllano da versanti opposti.
Usala quando un giro del ciclo produce esiti (una propagazione recepita, una
percezione valutata, un verdetto ratificato), a inizio sessione strategica, o
quando fili e note sembrano crescere senza controllo. Questa è la copia
canonica della skill (nata in `bi`): gli adottanti la forkano e la
parametrizzano sui propri segnali di dominio.

## Procedura

**1. Raccogli il contesto corrente**

Leggi `goal.md`, `i3/verdicts.md` e ogni filo `i3/*.md`; poi `o1/plan.md` e
`git log --oneline -15` per gli eventi dall'ultima revisione. Nel `metodo` i
segnali reali sono l'audit (`o3/kb_tools.py audit`), i marker `method-review.md`
degli adottanti (via `world/`) e le percezioni `i1/` non ancora valutate.

**2. Quattro domande per ogni filo**

- **È ancora vero?** Confronta il verdetto col segnale reale (audit, marker,
  nodo), non con la memoria. Un filo che contraddice il suo segnale va
  aggiornato in place prima di ogni altra cosa.
- **È ancora aperto?** Verdetto stabile e nessuna tensione → il filo si chiude:
  file rimosso, voce tolta da `i3/verdicts.md`, storia in git.
- **È ancora _un_ filo?** Se è cresciuto multi-tema, proponi lo split; ogni
  filo tiene una tensione sola.
- **È stato, non log?** Pota paragrafi storici e sequenze datate: la cronologia
  è il git history del file, non il suo corpo.

**3. Copertura bidirezionale con `goal.md`**

- Ogni obiettivo del register ha un **segnale vivo** (filo, audit, marker) e —
  se c'è tensione aperta — un filo che la tiene. Un obiettivo senza segnale è
  un buco di misura da dichiarare nel register, non da nascondere.
- Ogni filo dichiara **quale obiettivo misura** (annotazione `misura:` nella
  voce di `i3/verdicts.md`). Un filo che non misura nessun obiettivo è
  materiale da triage: o rivela un obiettivo mancante nel register (proponilo),
  o non è un verdetto.
- Segnali orfani (percezioni `i1/` che nessun filo valuta, marker che nessuno
  legge) vanno fatti emergere.

**4. Bonifica del plan (e dei task)**

Il plan è coda pura: tabella, dipendenze, legenda. Note e «cause» che sono
narrativa di stato del mondo (debrief, letture, posizioni, fondazioni
consegnate) migrano nel filo pertinente — o nel task `o2/` se sono contesto
operativo di esecuzione. Stessa lente sui task `o2/`: i diari di sessione si
potano a chiusura. È il gemello del passo «igiene» di `plan-review`, guardato
dal versante opposto.

**5. Formazione goal (modo due dell'i3)**

Input esogeni che non chiudono loop noti ma ne aprono di nuovi (una percezione
da un adottante che non rientra in nessun obiettivo, una cornice teorica
importata) → proponi il filo nuovo o il ritocco al register. Sempre in
proposta: decidere cosa conta è del custode umano (`kb/goal.md`).

**6. Proponi, poi applica**

Presenta le modifiche come elenco — una voce per filo/obiettivo, con azione
(aggiorna/chiudi/split/crea, migra dal plan) e motivo. Se non c'è nulla da
proporre, dillo esplicitamente. Applica a `i3/`, `goal.md` e `o1/plan.md` solo
dopo conferma dell'utente; chiudi suggerendo `/commit`.

## Note operative

- I fili chiusi si rimuovono, non si archiviano: la storia resta in git.
- L'annotazione `misura:` vive nell'indice `i3/verdicts.md`, non nel
  frontmatter dei fili (il frontmatter tiene solo la facet `ciclo`).
- La revisione non cambia mai un segnale (audit, marker): se il segnale è
  sbagliato, il fix è un task, non un ritocco al verdetto.
- Aggiornamenti del register `goal.md` in questa sede sono fotografie
  (obiettivo a regime, buco di misura dichiarato), non nuovi obiettivi: quelli
  li porta il custode.
