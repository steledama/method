---
data: 2026-08-01
stato: attiva
ciclo: runtime
target: economia (per primo), bi, salute, nixos
---

# La quinta domanda di `verdicts-review`: «è più sicuro del suo materiale?»

## Cosa e perché

Con la ratifica di «il verdetto non è più sicuro del materiale» (2026-07-31,
filo `i3/verdetto-piu-sicuro-del-materiale.md`, canone in `kb/verdict.md` e
commit `64f0ec0`) il passo 2 di `verdicts-review` canonica è passato da quattro
a **cinque domande**, con due cambi:

- la prima domanda («è ancora vero?») include ora fra i segnali reali il **file
  `o2/` che alimenta il filo** — spesso la registrazione più fresca e più
  cauta, e il filo più ottimista del proprio task ha già in casa la propria
  smentita;
- la domanda nuova, «**è più sicuro del suo materiale?**»: sul filo che suona
  meglio degli altri si fa un passo in più, non uno in meno — provenienza
  delle quantità (misurata / dichiarata da terzi / derivata da dichiarazioni),
  materiale di casa guardato prima, e la tesi che cade se cade una cifra
  derivata retrocede a congettura.

I quattro fork portano ancora quattro domande. Il backport viaggia **da solo**,
sganciato dalla ristrutturazione `eval`/`exec` in corso
(`o2/skill-archi-tripartite.md`, decisione del custode 2026-08-01): la domanda
è la guardia contro un modo di fallimento già osservato — la cifra dei
«400 €/mese» propagata in `economia` dopo essere stata smentita — e attendere
la rinomina l'avrebbe lasciata spenta negli adottanti per settimane note.

## La ricetta (nel lessico del metodo)

1. **Diff dal canone.** Nel fork locale
   (`.claude/skills/verdicts-review/SKILL.md` più il wrapper
   `.codex/skills/`): portare il passo 2 da «Quattro domande» a «Cinque
   domande» col contenuto del canone — via `method/` il diff esatto è
   `git show 64f0ec0 -- .claude/skills/verdicts-review/SKILL.md`.
2. **Parametrizzare il «materiale di casa».** La domanda chiede di guardare ciò
   che il progetto ha prodotto di suo prima di credere alla storia migliore:
   ogni fork dichiara le proprie fonti primarie interne (posta in uscita,
   valutazioni di credibilità già in KB, file `o2/`, artefatti di dominio) —
   indizi da verificare in loco, non un elenco da copiare.
3. **Recepimento ordinario.** Il canale è il `method-review` locale: la voce si
   classifica, si applica, il marker avanza. Nessun pilota: il diff è piccolo e
   la forma è già collaudata in `metodo`.

## Touchpoint per-repo (indizi da verificare in loco, non ordini)

- **`economia` — per primo**: è l'adottante dove i tre episodi sono avvenuti e
  il più esposto (quantità derivate da dichiarazioni di fonti valutate poco
  credibili in KB, corrispondenza in uscita come smentita disponibile). Il suo
  artefatto delle ritrattazioni resta watchpoint locale, non entra nel canone.
- **`bi`** — origine della coppia: il fork è probabilmente il più vicino al
  canone, il diff dovrebbe essere pulito.
- **`nixos`, `salute`** — adattare gli esempi della domanda al dominio (in
  `nixos` le quantità sono versioni e misure di sistema, in `salute` i dati
  del diario e delle trascrizioni); `salute` ha il frontmatter skill di
  vecchio stile — normalizzarlo **non** è materia di questa prescrizione, resta
  alla prescrizione della rifilatura.

## Ordine e chiusura

`economia` per primo, `bi` in coda al suo prossimo `method-review`. `nixos` e
`salute` l'hanno già chiusa recependo la rifilatura `skill-per-arco`
(2026-08-01: il fork di `eval` porta le cinque domande con le quantità di
dominio). La prescrizione resta attiva finché i quattro non l'hanno recepita; recepita da tutti, si rimuove dalla collezione — la storia resta in
git. La prescrizione della rifilatura `eval`/`exec` che seguirà sposterà le
cinque domande sotto `eval compare`: recepire questa non anticipa quella, e la
rinomina troverà la quinta domanda già al suo posto.
