---
data: 2026-06-14
stato: aperto
---

# Nome della collezione i1: `sources/` o `perceptions/`

Emerso dall'adozione in `economia`, mentre si migrano le catture i1 piene (JSON
di estratti, buste paga, investimenti) verso la collezione i1 prescritta. Il
nome attuale della collezione è `sources/`, con porta `sources.md` ("il manifest
delle fonti i1"). Il sospetto è che sia un nome per **provenienza** dove il
metodo, altrove, nomina le collezioni per **funzione cognitiva** — e quindi un
residuo da sciogliere, non una scelta verificata.

## L'asimmetria osservata

Sul lato output ([[output]]) le collezioni portano il nome dello stadio
cognitivo: o2 → `interpretations/` (Interpret), o3 → `prescriptions/`
(Prescrivi/Perform-ahead). Sul lato input ([[input]]) lo stadio i1 è la
**cattura** e corrisponde al Perceive di Norman, ma la sua collezione si chiama
`sources/` — un nome sull'origine del dato, non sull'atto cognitivo. Per la
regola di [[project-structure]] «il carattere vive nel contenuto, un nome che
contraddice il contenuto è un signifier che mente», la simmetria spingerebbe
verso `perceptions/` o `captures/`.

## Verifica comparata (il lavoro)

- censire ogni occorrenza in cui il metodo nomina la collezione i1: `sources/` e
  `sources.md` in [[project-structure]], [[world]], [[input]], [[output]],
  [[processing-layers]] e nelle porte/atrio dei repo (`method` stesso include
  `sources.md` e `sources/`);
- ricostruire la genesi del nome: la rifondazione input/output (commit
  `f45762c`, «strato input dogfoodato — sources/») scelse `sources/`
  deliberatamente o per inerzia? distinguere scelta motivata da residuo;
- mettere a confronto i tre candidati — `sources/` (provenienza), `perceptions/`
  (stadio Norman), `captures/` (la parola che [[input]] già usa: «i1 — cattura»)
  — contro il principio di nominare-per-funzione e contro la simmetria i/o;
- pesare la controparte: il lessico delle **fonti** è load-bearing nella teoria
  i1 («le due sorgenti di i1», feedback ed esogeno) e tocca il nodo
  [[source-of-truth]]. Verificare però se la _fonte di verità_ punti davvero
  alla collezione i1 o piuttosto a [[world]] (il grezzo non versionato), nel qual
  caso `sources/` confonde due confini distinti;
- decidere: confermare `sources/` con rationale esplicito, oppure rinominare. Se
  si rinomina, lo sweep tocca i nodi sopra, le porte/atrio di ogni adottante
  (`sources.md`), `.gitignore`, gli script e `map.md` locali.

## Ricaduta sugli adottanti

`economia` sta per migrare `data/json/` verso la collezione i1 (tasks locali 15
/ 16 / 22) e adotterebbe il nome corrente. La scelta del nome della collezione
dovrebbe atterrare **prima** che gli adottanti la fissino, per non pagare due
rinomine. Finché il task è aperto, `economia` può procedere con la migrazione
adottando provvisoriamente il nome del metodo e lasciando un puntatore a questo
task, così che un'eventuale rinomina sia un singolo sweep coordinato.

Task gemello: [[collocazione-file-dominio]] decide _che cosa_ entra nella
collezione i1 (la membership dei file-ciclo di dominio, es. `diario`); questo
decide _come si chiama_. Vanno risolti coerentemente.
