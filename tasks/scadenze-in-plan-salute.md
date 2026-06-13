---
data: 2026-06-13
stato: aperto
---

# Valutare la forma di plan.md dopo l'integrazione delle scadenze in salute

Il 2026-06-13, in `salute`, `scadenze.md` (tabella di appuntamenti sanitari
datati, già convertita in elenco per la regola "tabelle vs elenchi") è stata
assorbita in `plan.md` come nuova sezione `## Scadenze`. La motivazione locale:
task e scadenze sono due facce della stessa pianificazione e si influenzano a
vicenda (una scadenza vicina può alzare la priorità di un task collegato).

## Tensione con la forma canonica

`plan.md` (nodo metodo) descrive la forma canonica come una tabella stretta
`# · Priorità · Task · Dipende da` con footer di link per titolo — "uniforme su
tutti i repo adottanti: la granularità del dominio vive nel contenuto ... non
nella forma". `salute/plan.md` **non** usava già questa forma (sezioni
`## Alta`/`## Media`/`## Bassa` con elenchi, non la tabella), uno scostamento
preesistente non ancora discusso esplicitamente in `confronto-progetti-adottanti`.
L'aggiunta di `## Scadenze` è un secondo scostamento, nello stesso file, motivato
dal dominio (calendario sanitario datato, correlato ai task).

Caso di confronto: `economia` ha sia `plan.md` in forma tabellare canonica sia
un `scadenze.md` separato (componente locale, cfr.
`confronto-progetti-adottanti` riga sui "componenti locali aggiuntivi"). Quindi
due adottanti con domini calendariali (`economia`, `salute`) hanno preso strade
diverse: file separato vs. sezione dentro `plan.md`.

## Domande da chiarire

- La forma a sezioni (`## Alta/Media/Bassa` + `## Scadenze`) di `salute/plan.md`
  è un adattamento di dominio da annotare in `confronto-progetti-adottanti`
  (insieme allo scostamento preesistente dalla tabella), o dovrebbe essere
  riportata alla forma canonica (tabella `# · Priorità · Task · Dipende da` +
  una colonna/sezione scadenze)?
- Le scadenze datate meritano una posizione nella forma canonica del nodo
  `plan` (es. una sezione opzionale "Scadenze" ammessa quando il dominio ha una
  componente calendariale), o restano per definizione fuori dal plan
  (`economia` le tiene in `scadenze.md` separato)?
- Se emerge un pattern comune a `economia` e `salute` (entrambi domini con
  scadenze datate che interagiscono con le priorità dei task), vale la pena
  generalizzarlo nel nodo `plan`; se restano scelte locali legittime, basta
  documentarle in `confronto-progetti-adottanti`.

## Esito atteso

- Decisione su come trattare lo scostamento di `salute/plan.md` dalla forma
  canonica (annotare come adattamento vs. riportare alla forma tabellare).
- Se emerge un pattern condiviso tra `economia` e `salute`, arricchire il nodo
  `plan` con una posizione esplicita per le scadenze datate nella pianificazione.
- Aggiornare `confronto-progetti-adottanti` con l'esito, qualunque sia.

Connessioni:

- [plan](../kb/plan.md)
- [confronto-progetti-adottanti](../kb/confronto-progetti-adottanti.md)
- [tasks](../kb/tasks.md)
