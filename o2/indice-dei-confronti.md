---
sintesi: "La vista Confronti (verdict.html) parte subito coi fili, senza indice. Le si dà un indice uguale a quello del plan (Ciclo · Ob. · Filo) e ogni filo riceve un obiettivo nel frontmatter, verificato contro goal.md come la colonna Ob. del plan. Così si toglie la misura scritta a mano nell'indice i3, che è già andata alla deriva."
ciclo: dev
---

# Indice dei Confronti con obiettivo verificato

Secondo task della ristrutturazione della presentazione (2026-10-02). Dipende
da [presentazione-autonoma-e-uniforme](presentazione-autonoma-e-uniforme.md)
per lo stile, la sigla nel titolo e la legenda interna degli obiettivi.

## Indice iniziale

- La vista apre con una slide-indice intitolata «Method Verdicts» (negli
  adottanti italiani «BI Confronti» e simili). Ha la stessa forma della
  tabella del plan: **Ciclo · Ob. · Filo**. Ogni filo è un link alla propria
  slide, e ogni slide di filo si chiude con «Torna all'indice».
- L'ordine è quello di `i3/verdicts.md`, l'indice curato. Oggi la vista
  ordina i file per nome (`sorted(glob)`) e l'indice non lo legge.
- **Contratto**, come per plan e `o2/`: ogni file di `i3/` deve stare
  nell'indice e ogni voce dell'indice deve avere il suo file, altrimenti la
  build rompe.

## Obiettivo nel frontmatter

Valutazione del 2026-10-02: la simmetria coi task conviene, ed è già quasi
canone.

- `kb/verdict.md` chiede che ogni voce dell'indice dichiari con `misura:`
  quale obiettivo osserva. È però testo libero, e la deriva c'è già: sei
  voci misurano contro «Canale-perception funzionante», che oggi non è un
  obiettivo di `goal.md` (gli obiettivi sono 1, 2, 3 e S).
- È lo stesso difetto che la colonna `Ob.` ha tolto dal plan. Il rimedio è
  lo stesso: frontmatter `obiettivo: 1|2|3|S` (più chiavi separate da
  virgola), verificato con `goal_keys` dalla libreria condivisa. Una chiave
  vuota o assente dal register rompe la build.
- Il `misura:` testuale nell'indice diventa un doppione dello stesso fatto
  e si toglie (`i3/igiene-stadi-output.md`, una rappresentazione per
  fatto).
- **Da decidere col custode:** a quale obiettivo vanno i sei fili orfani di
  «Canale-perception funzionante». È un giudizio per filo, non una
  sostituzione meccanica.
- Nell'indice la chiave `Ob.` porta alla legenda interna degli obiettivi
  (compartimento stagno), come nel plan.

## Ciclo dev/runtime

- La colonna `Ciclo` si mostra: il frontmatter `ciclo:` c'è già in ogni
  filo (canone dal 2026-07-04), quindi non costa nulla. Ha anche un senso
  proprio, perché separa le tensioni sul metodo stesso da quelle sul Mondo
  (oggi in `metodo` 12 `dev` e 4 `runtime`).
- **Nessun filtro:** la lente dev/runtime come filtro resta rimandata
  all'uso reale (`i3/home-minimalista.md`).

## Casi limite

- I file di `i3/` che non sono fili, come i cursori (negli adottanti
  `i3/allineamento-metodo.md`): vanno decisi all'implementazione, se
  portano anch'essi `obiettivo:` o se si escludono in modo esplicito. Mai
  in silenzio.

## Canone da toccare

- `kb/verdict.md`: `obiettivo:` nel frontmatter al posto di `misura:`
  nell'indice.
- `.claude/skills/eval/SKILL.md` (scope `compare`) e `commit`, se citano
  `misura:`.

## Criterio di chiusura

`verdict.html` di `metodo` apre con l'indice. Ogni filo ha `obiettivo:`
verificato, e un filo senza obiettivo o con una chiave inesistente fa
fallire la build. Nell'indice i3 non resta nessun `misura:`.
