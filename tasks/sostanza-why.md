---
data: 2026-06-06
stato: aperto
---

# Runbook — `why.md` per motivazione: completare il refactor da `log` su ogni repo

La migrazione del layout aveva cambiato il **nome** (`log.md → why.md`), non la **forma**:
gli adottanti restano log datati, append-only, con la decisione relegata a sottotitolo
dell'header `## [DATA] tipo | titolo`. Questo runbook porta la **sostanza** a coincidere col
nome — memoria interpretativa indicizzata per *motivazione*, non per data — replicando su
ogni repo il refactor già eseguito su `metodo` (2026-06-06). Prossimo target: **`bi`**.

## La decisione (forma A — già applicata a `metodo`, fissata nel nodo)

La forma e le convenzioni vivono nel nodo canonico [[why]] (`kb/why.md`), propagato via
**symlink** agli adottanti. **Conseguenza operativa chiave: lavorando in un repo adottante
NON si tocca il nodo** — lo si eredita già aggiornato. Si interviene solo sul `why.md` *di
quel repo*. Riassunto della forma:

1. **Chiave primaria = motivazione** (gruppo `##`, con una riga di intro in corsivo); la
   data è asse secondario *dentro* il gruppo (`### [YYYY-MM-DD] tesi`, dalla più recente).
   Git possiede l'asse del tempo; `why` aggiunge quello del significato. **Guardia
   bottom-up:** solo temi già stabilizzati, niente scaffali vuoti.
2. **Asse `tipo` eliminato** dalla forma finale, ma **usato come indizio di clustering**
   durante il refactor (i tag `architettura|pattern|fix|integrazione|…` aiutano a raggruppare).
3. **Supersessione esplicita:** un'entry superata resta in posizione e riceve una riga
   `> ↳ …` verso quella che la corregge. Mai cancellare (git conserva).
4. **Multi-tema:** entry nel gruppo più pertinente + rimandi agli altri.
5. **Dump audit/lint FUORI dal `why`:** sono output macchina (i1), rigenerabili — non
   memoria interpretativa. Vanno spostati in una collocazione dedicata all'output operativo,
   come **snapshot sovrascritto** (non storia append-only). Non reintrodurre un archivio di
   report che cresce (`bi` aveva già rimosso `kb/reports/`). Le righe-riassunto
   interpretative («audit completo — 0 orfane, 0 link rotti») possono restare come entry.

## Regola di esecuzione — una sessione per repo, dentro il repo

Si apre una sessione *nel* repo target, si bootstrappa sul suo dominio
(`README → map → CLAUDE → nodo`), si esegue questo runbook, si committa lì. Ragione: la
clusterizzazione è **giudizio interpretativo dei fili concettuali di quel repo** — le
motivazioni emergono dalla storia delle sue decisioni, e i nomi dei gruppi vanno scelti col
contesto di dominio caricato. Il nodo `why` è condiviso via symlink: nessuna modifica
cross-repo, nessun coordinamento.

## Procedura (replicata da `metodo`, voce per voce)

1. **Recon.** Leggere il `why.md` del repo. Contare le entry; mappare i tag `tipo` esistenti
   (indizio di clustering); individuare le entry-dump di audit/lint (corpo = output grezzo
   incollato) separandole dalle entry interpretative.
2. **Clusterizzare per motivazione** (giudizio di dominio). Raggruppare le entry nei fili
   concettuali *già stabilizzati* del repo. Una entry per gruppo-chiave; multi-tema con
   rimando. Ordine intra-gruppo: dalla più recente.
3. **Riorganizzazione meccanica con corpo verbatim — via script** (vedi sotto). Il corpo di
   ogni entry si **sposta**, non si riscrive: garantisce fedeltà e rende il diff revisionabile.
4. **Marcatori di supersessione** dove un'entry successiva ritratta/raffina una precedente;
   **link incrociati** per le multi-tema.
5. **Dump audit/lint fuori dal `why`** → snapshot rigenerabile (vedi decisione 5). Destinazione
   decisa contro la struttura reale del repo.
6. **Preambolo del `why.md` del repo** riscritto alla nuova forma (togliere «append-only»,
   «ex log.md», «Formato voce: ## [DATA] tipo | titolo» → convenzioni del nodo). **Il nodo
   `kb/why.md` NON si tocca: è ereditato.**
7. **Entry di sessione** in testa al gruppo pertinente, che registra *questo* refactor (è
   l'i3 del ciclo di sviluppo della sessione), con puntatore al commit `metodo` di riferimento.

## Lo script (template riusabile — adattare `clusters`, `markers`, e il regex dell'header)

Per gli adottanti l'header è `## [DATA] tipo | titolo` (con `[storico]` / `[storico ~AAAA]`
al posto della data, e entry-dump `## [DATA] audit-kb` senza `tipo |`). Per `metodo` era
`## DATA — titolo`. Adattare `HDR` di conseguenza.

```python
import re
SRC = 'why.md'
text = open(SRC, encoding='utf-8').read(); lines = text.split('\n')
# adottanti: bracket + 'tipo | titolo'. metodo: r'^## (\d{4}-\d{2}-\d{2}) — (.*)$'
HDR = re.compile(r'^## \[([^\]]+)\]\s*(.*)$')
hs = [(i, m.group(1), m.group(2)) for i,l in enumerate(lines) for m in [HDR.match(l)] if m]
entries = []
for k,(i,date,rest) in enumerate(hs):
    end = hs[k+1][0] if k+1 < len(hs) else len(lines)
    body = '\n'.join(lines[i+1:end])
    body = re.sub(r'^-{3,}\s*\n?','',body.strip()); body = re.sub(r'\n?-{3,}\s*$','',body.strip())
    tipo, _, title = rest.partition(' | ')
    if not title: tipo, title = '', rest          # entry-dump o senza tipo
    entries.append({'date':date,'tipo':tipo,'title':title.strip(),'body':body,'idx':k})
# 1) stampare entries per decidere clusters; 2) marcare i dump da estrarre
# clusters = [("Titolo gruppo","intro",[idx,...]), ...]   markers = {idx: "> ↳ ..."}
# dump_idx = {idx,...}  -> scritti altrove (snapshot), non nel why
assert sorted(i for _,_,idxs in clusters for i in idxs) + sorted(dump_idx) == list(range(len(entries)))
# ... emit: preambolo + '---' + per cluster: '## titolo','*intro*', per idx '### [date] title' (+marker) + body
open(SRC,'w',encoding='utf-8').write(result)
```

**Verifica verbatim (obbligatoria, come su `metodo`):** confrontare il multiset delle righe
di corpo (non-header, non-`---`, non vuote) prima/dopo. *Mancanti dal nuovo = 0* (eccetto il
vecchio preambolo, sostituito); le aggiunte sono solo nuovo preambolo + intro dei cluster +
righe spostate nello snapshot.

## Verifica (gate, prima del commit)

- check verbatim: 0 righe di corpo perse (al netto di preambolo e dump estratti).
- `python3 scripts/kb_tools.py audit` → 0 link rotti, 0 nodi isolati.
- grep header del `why.md`: nessun residuo `append-only`, `ex log.md`, `tipo |`.
- dump audit/lint non più nel `why.md`; snapshot al suo posto.
- entry di sessione in testa al gruppo giusto, con puntatore al commit `metodo` di riferimento.
- commit in-repo `refactor(why): ribalta la memoria per motivazione`. **Push mai automatico.**

## Schede per-repo

### `bi` (prossimo)
- ~736 righe, ~55 entry, header `## [DATA] tipo | titolo`, asse `tipo`
  (`integrazione|architettura|refactoring|rimozione|pattern|lint|metodo|fix`).
- **12 dump grezzi `audit-kb`** (es. `## [DATA] audit-kb`, `audit-kb-bi`) → estrarre in
  snapshot; le righe `lint | audit completo — 0/0/0` possono restare come entry brevi.
- Fili tematici candidati (da confermare bottom-up nella sessione, *non* prescritti qui):
  modello disponibilità e sorgenti · orfani commerciali di fornitore · freschezza/feed
  fornitori · integrazione Baserow/Danea · metodo, KB e refactoring documentazione · audit/lint.
- Destinazione snapshot dump: decidere contro la struttura di `bi` (no nuovo `kb/reports/`).

### `nixos`
- ~370 righe, ~40 entry, stesso header. **8 entry `[storico]`** (data assente → la data è
  già demota: confermano la forma). `nixos` aveva già potato i suoi dump (entry «log pruning»).

### `economia` / `salute`
- **Non presenti su questo host.** Quando raggiungibili, stessa procedura. (Si assume il
  layout già migrato; se il `why.md` fosse ancora `log.md`, fare prima la rinomina `git mv`.)

## Filing back / chiusura

Il nodo [[why]] è la fonte canonica della forma. Quando `bi`, `nixos` (ed `economia`/`salute`
quando raggiungibili) sono allineati e verificati, il task si chiude: la riga sparisce da
`plan.md`, lo storico resta in git e nei `why.md`. La maturazione del nodo `why` da `bozza` a
`maturo` è il filing back atteso a refactor completo.

**Stato:** `metodo` ✅ fatto (2026-06-06) — caso di riferimento. Resta `bi` (prossimo),
`nixos`, e `economia`/`salute` fuori host.
