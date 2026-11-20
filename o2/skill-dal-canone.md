---
sintesi: "Le skill del metodo passano da copie forkate negli adottanti a canone parametrizzato, come è già successo ai builder delle viste: ogni repo tiene solo la propria identità in un file locale, e la skill la legge. È anche la condizione perché adottare il metodo costi poco a chi non è il custode."
ciclo: dev
decidere: "Le skill restano fork parametrizzati negli adottanti (kb/skill.md) o diventano canone condiviso con i parametri in un file locale?"
---

# Skill dal canone

## Origine

Aperto dal custode il 2026-11-20, riflettendo sulla relazione fra `method` e
l'istanza `casa` ([coordinatore-di-gruppi](coordinatore-di-gruppi.md)).
`casa` adotta il canone come gli altri repo: nodi e strumenti li legge dal
vivo (`method/` è un symlink, builder e gate si lanciano dal checkout del
canone), lo stato è suo. Le skill invece sono copie: circa 1460 righe forkate
al commit `ff9af10` con i soli percorsi adattati, da riallineare a mano con
`/method` a ogni modifica del canone. Lo stesso vale per gli otto adottanti.

Un fork git di `method` come base delle istanze è stato scartato: porterebbe
con sé storia, stato di sviluppo e copie di `kb/` e `o3/`, con conflitti a
ogni merge sui file che entrambi modificano (`world.md`, `goal.md`, plan,
indici) e copie del canone che derivano senza che nessuno lo veda.

## Precedente

Le viste hanno già fatto questo passo: i builder stavano negli adottanti come
copie, ora sono canone e il repo tiene solo `o3/view/project.py`
(`kb/view-publishing.md`, «HTML apribile direttamente e build minima»).

## Forma proposta

- le skill canoniche sono scritte per un repo qualunque, senza dire
  `method` dove intendono «il repo»;
- le differenze di un repo (nome, Mondo, ricorrenze, eccezioni di dominio,
  strumenti locali) stanno in un file locale versionato, letto dalla skill;
- nell'adottante la skill è un symlink o un wrapper di poche righe verso la
  copia canonica, per ogni harness (`.claude/skills/`, `.codex/skills/`);
- le skill che restano di dominio (`/adottanti` qui, gli eventuali
  equivalenti di gruppo in `casa`) restano locali;
- gli strumenti che oggi leggono il `world.md` di `method` (`o3/adottanti.py`,
  `o3/dinieghi.py`) accettano una radice, come `build.py --root`.

## Relazioni

- [snellimento-skill](snellimento-skill.md): i tagli a `eval` ed `exec`
  aspettano il riesame del 2026-12-01; questo task cambia dove vivono le
  skill, non quanto sono lunghe, ma tocca gli stessi file e va ordinato con
  quello;
- [diffusione-oltre-custode-unico](diffusione-oltre-custode-unico.md): un
  adottante che non è il custode non può riallineare fork a mano;
- in `casa`, `o2/parametrizzare-le-skill.md` è il lato dell'adottante.

## Decisione richiesta

Cambiare la regola di `kb/skill.md` («gli adottanti le forkano e le
parametrizzano») è una modifica del canone: la decide il custode.
