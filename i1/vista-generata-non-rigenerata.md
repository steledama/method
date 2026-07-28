---
ciclo: runtime
---

# Segnale: una vista generata può essere stale senza che nulla diverga

Data: 2026-07-29 · Fonte: custode, su ispezione delle superfici di `economia`
(lente «superfici e viste» di `/adopters-review`, anticipata rispetto al battito
dell'11 agosto) e sull'esito del `method-review` di `bi` dello stesso giorno.

## Il segnale

Due viste, in due adottanti diversi, erano vecchie rispetto alle proprie fonti
senza che nessuna fonte si contraddicesse.

**`economia`, la home.** `presentation/index.html` è ferma al commit `2e7d9c5`
(11 luglio). Il paragrafo che dichiara la lente trasversale del progetto — il
criterio con cui `goal.md` dice che ogni scelta va giudicata — è entrato nel
register il 24 luglio (`4f5391f`), e nella home non c'è, insieme al link al filo
`i3/` che lo regge. Rigenerata la home in una copia isolata del repo, il diff
contro quella versionata è di sola **aggiunta**: nella superficie non c'è nulla
di falso, manca il fatto più recente. Cinque giorni e tre commit di `goal.md`.

**`bi`, la vista dei verdetti.** `presentation/verdict.html` è risultata stantia
rispetto ai fili `i3/` correnti durante il `method-review` del 29 luglio, ed è
stata rigenerata in quella sessione. Il ledger dei limiti di `bi` registra il
punto scoperto: il contratto appena recepito copre il legame plan × `o2/`, ma
`verdict.html` resta una vista derivata senza vincolo proprio sulla freschezza
dei fili.

Osservazioni:

- **nessuno dei due è il caso-contratto.** Non c'è divergenza fra due fonti dello
  stesso fatto: i generatori sono corretti e le fonti coerenti. La vista è
  semplicemente il prodotto di un'esecuzione che non è più stata rifatta;
- **il presidio che esiste è riflessivo.** Il check i2 del gate `/commit` («il
  deck va ri-derivato, non lasciato stale») avrebbe coperto entrambi i casi: in
  `economia` non ha sparato per tre commit consecutivi del register;
- **il dato per accorgersene è già in git.** L'ultimo commit che tocca la vista
  contro l'ultimo commit che tocca le sue fonti: confronto meccanico, nessuna
  lettura del contenuto;
- **gli audit strutturali continuavano a dire che va tutto bene** in entrambi i
  repo, come nei casi già noti: non attraversano il confine vista↔fonte;
- **le due viste hanno una forma di sorgente diversa.** La home di `economia`
  deriva da file nominati (`README.md`, i due register); `verdict.html` di `bi`
  deriva da una **collezione intera** (`i3/*.md`), cioè da un glob: l'insieme
  delle fonti non è un elenco fisso.

## Domande per i2 (nessun verdetto qui, i1 è valenza-neutro)

- coerenza fra le fonti e freschezza rispetto alle fonti sono lo stesso vincolo o
  due? Il primo si verifica **dentro** il generatore; il secondo non può, perché
  il difetto è proprio che il generatore non è stato eseguito;
- dove vivrebbe il presidio: il gate `/commit`, un hook, un check in `kb_tools`
  accanto all'audit strutturale? E chi **dichiara** le fonti di una vista — oggi
  l'elenco vive in prosa in `view` e implicitamente nel codice del generatore,
  in nessun posto leggibile da uno strumento;
- rigenerare tutte le viste a ogni commit renderebbe il check superfluo: è più o
  meno costoso del check? Il prezzo è rumore nei diff a ogni commit;
- se il rimedio fosse «rigenerare sempre», una vista versionata resta un
  artefatto del repo o diventa un prodotto di build che non si versiona? Il
  canone oggi le versiona perché devono aprirsi dal checkout;
- una vista che deriva da una collezione via glob ha una nozione di «fonte
  dichiarata» diversa da una che deriva da file nominati: il check è lo stesso o
  cambia forma?
- il modo di guasto è stato trovato **guardando**, non subendolo: in `economia`
  nessuno si era accorto di nulla, e in `bi` è emerso dentro un'altra revisione.
  Cambia qualcosa, per il metodo, che un segnale arrivi da un'ispezione invece
  che da un danno?
