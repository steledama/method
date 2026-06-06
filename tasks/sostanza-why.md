---
data: 2026-06-06
stato: aperto
---

# Runbook — `why.md` per motivazione: completare il refactor da `log` su ogni repo

La migrazione del layout aveva cambiato il **nome** (`log.md → why.md`), non la **forma**:
gli adottanti restano log datati, append-only, con la decisione relegata a sottotitolo
dell'header `## [DATA] tipo | titolo`. Questo runbook porta la **sostanza** a coincidere col
nome — memoria interpretativa indicizzata per _motivazione_, non per data — replicando su
ogni repo il refactor già eseguito su `metodo` e `bi` (2026-06-06). Prossimo target: **`nixos`**.

## La decisione (forma A — già applicata a `metodo`, fissata nel nodo)

La forma e le convenzioni vivono nel nodo canonico [[why]] (`kb/why.md`), propagato via
**symlink** agli adottanti. **Conseguenza operativa chiave: lavorando in un repo adottante
NON si tocca il nodo** — lo si eredita già aggiornato. Si interviene solo sul `why.md` _di
quel repo_. Riassunto della forma:

1. **Chiave primaria = motivazione** (gruppo `##`, con una riga di intro in corsivo); la
   data è asse secondario _dentro_ il gruppo (`### [YYYY-MM-DD] tesi`, dalla più recente).
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
   **Euristica destinazione:** lo snapshot va dove il repo _già_ tiene output macchina
   rigenerabile e gitignored (in `bi`: `output/kb-audit-snapshot.md`). Se quel posto non
   esiste e l'audit è rigenerabile da un comando, il default è **non conservare i dump stantii
   affatto** — git tiene la storia nel vecchio `why.md` — e documentare il comando di
   rigenerazione nell'intro del gruppo audit.

## Regola di esecuzione — una sessione per repo, dentro il repo

Si apre una sessione _nel_ repo target, si bootstrappa sul suo dominio
(`README → map → CLAUDE → nodo`), si esegue questo runbook, si committa lì. Ragione: la
clusterizzazione è **giudizio interpretativo dei fili concettuali di quel repo** — le
motivazioni emergono dalla storia delle sue decisioni, e i nomi dei gruppi vanno scelti col
contesto di dominio caricato. Il nodo `why` è condiviso via symlink: nessuna modifica
cross-repo, nessun coordinamento.

## Procedura (replicata da `metodo`, voce per voce)

1. **Recon.** Leggere il `why.md` del repo. Contare le entry; mappare i tag `tipo` esistenti
   (indizio di clustering); individuare le entry-dump di audit/lint (corpo = output grezzo
   incollato) separandole dalle entry interpretative. **I conteggi nelle schede per-repo sono
   indicativi: ri-derivali qui** (su `bi` i «12 dump» erano in realtà 4 corpi-dump + ~5
   righe-riassunto a corpo vuoto). Attenzione alle righe-riassunto a **corpo vuoto** (il dump
   le seguiva subito): l'informazione sta nel titolo, restano come entry `###` senza corpo.
2. **Clusterizzare per motivazione** (giudizio di dominio). Raggruppare le entry nei fili
   concettuali _già stabilizzati_ del repo. Una entry per gruppo-chiave; multi-tema con
   rimando. Ordine intra-gruppo: dalla più recente.
3. **Riorganizzazione meccanica con corpo verbatim — via script** (vedi sotto). Il corpo di
   ogni entry si **sposta**, non si riscrive: garantisce fedeltà e rende il diff revisionabile.
4. **Marcatori di supersessione** dove un'entry successiva ritratta/raffina una precedente;
   **link incrociati** per le multi-tema.
5. **Dump audit/lint fuori dal `why`** → snapshot rigenerabile (vedi decisione 5). Destinazione
   decisa contro la struttura reale del repo. **Può essere un no-op:** se il repo ha già potato
   i suoi dump (caso `nixos`, entry «log pruning») non c'è nulla da estrarre e nessuno snapshot
   da creare — confermalo in recon e salta.
6. **Preambolo del `why.md` del repo** riscritto alla nuova forma (togliere «append-only»,
   «ex log.md», «Formato voce: ## [DATA] tipo | titolo» → convenzioni del nodo). **Il nodo
   `kb/why.md` NON si tocca: è ereditato.**
7. **Entry di sessione** in testa al gruppo pertinente, che registra _questo_ refactor (è
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
covered = [i for _,_,idxs in clusters for i in idxs]
assert len(covered) == len(set(covered)), 'indici duplicati nei cluster'
assert sorted(covered + list(dump_idx)) == list(range(len(entries)))  # ordina l'UNIONE: non concatenare due liste già ordinate
# ... emit: preambolo + '---' + per cluster: '## titolo','*intro*', per idx '### [date] title' (+marker) + body
open(SRC,'w',encoding='utf-8').write(result)
```

**Verifica verbatim (obbligatoria, come su `metodo`):** non confrontare il multiset _completo_
prima/dopo con eccezioni da scontare a mano (preambolo, dump) — è fragile. Più robusto: prendere
le righe di corpo (non-header, non-`---`, non vuote) delle **sole entry tenute** (escluse quelle
in `dump_idx`) e verificare che siano un _sottoinsieme_ del nuovo file. Niente eccezioni: il
preambolo è sostituito per costruzione, i dump sono esclusi a monte.

```python
def body_lines(s):
    return [l.strip() for l in s.split('\n') if l.strip() and not l.strip().startswith('---')]
from collections import Counter
kept = [e for e in entries if e['idx'] not in dump_idx]
old = Counter(l for e in kept for l in body_lines(e['body']))
miss = old - Counter(body_lines(result))
assert not miss, miss            # 0 righe di corpo tenute perse
print('righe-dump estratte (attese FUORI dal why):',
      sum(len(body_lines(entries[i]['body'])) for i in dump_idx))
```

## Verifica (gate, prima del commit)

- check verbatim: 0 righe di corpo perse (al netto di preambolo e dump estratti).
- `python3 scripts/kb_tools.py audit` → 0 link rotti, 0 nodi isolati.
- grep header del `why.md`: nessun residuo `append-only`, `ex log.md`, `tipo |`.
- dump audit/lint non più nel `why.md`; snapshot al suo posto.
- entry di sessione in testa al gruppo giusto, con puntatore al commit `metodo` di riferimento.
- commit in-repo `refactor(why): ribalta la memoria per motivazione`. **Push mai automatico.**

## Schede per-repo

### `bi` ✅ fatto (2026-06-06, commit `59059c43`)

- Era ~736 righe, 55 entry, header `## [DATA] tipo | titolo`, asse `tipo`.
- I dump erano **4 corpi-dump** (`audit-kb-bi` + 3 `audit-kb`, ~178 righe) più 5 righe-riassunto
  a corpo vuoto, _non_ 12 — estratti in `output/kb-audit-snapshot.md` (gitignored, rigenerato da
  `kb_tools.py audit`); le righe-riassunto sono rimaste come entry brevi.
- 7 gruppi emersi bottom-up: modello unico delle sorgenti di disponibilità · orfani commerciali
  di fornitore · freschezza del feed · Baserow fonte di verità e arretramento di Danea ·
  strumenti/ambiente/automazione · metodo, KB e documentazione · audit e lint.
- 3 marcatori `> ↳` (rotta `ecomm1 → wl1`, dead code canonico, forma del file stesso).

### `nixos` ✅ fatto (2026-06-06, commit `d318485`)

- Era ~370 righe, **40 entry**, header `## [DATA] tipo | titolo`, asse `tipo`; 8 `[storico]`
  senza data (confermavano la forma: data già demota).
- Step 5 **no-op confermato in recon**: i dump erano già potati (entry «log pruning»). Le 4
  voci `audit kb-nixos` erano già righe-riassunto interpretative (1 riga ciascuna), non corpi
  grezzi — rimaste come entry brevi. Nessuno snapshot creato.
- **9 gruppi** emersi bottom-up: simmetria dei server gemelli e fonti uniche di verità ·
  livello e trasparenza della configurazione di sistema · rete, accessi e servizi esposti ·
  disponibilità dei Drive personali via rclone · la KB come interfaccia cognitiva · il metodo
  come dipendenza trans-repo · CLAUDE.md come costituzione operativa · strumenti per agenti AI ·
  audit, lint e disciplina della memoria interpretativa.
- 2 marcatori `> ↳` (GUI-at-system → simmetria server; forma append-only → indicizzazione per
  motivazione). Verifica verbatim: 0 righe di corpo perse. Audit: 41 nodi, 0 link rotti, 0 orfani.

### `economia` / `salute`

- **Non presenti su questo host.** Quando raggiungibili, stessa procedura. (Si assume il
  layout già migrato; se il `why.md` fosse ancora `log.md`, fare prima la rinomina `git mv`.)

## Filing back / chiusura

Il nodo [[why]] è la fonte canonica della forma. Quando `bi`, `nixos` (ed `economia`/`salute`
quando raggiungibili) sono allineati e verificati, il task si chiude: la riga sparisce da
`plan.md`, lo storico resta in git e nei `why.md`. La maturazione del nodo `why` da `bozza` a
`maturo` è il filing back atteso a refactor completo.

**Stato:** `metodo` ✅ fatto (2026-06-06, commit `a9fbb82`) — caso di riferimento. `bi` ✅ fatto
(2026-06-06, commit `59059c43`). `nixos` ✅ fatto (2026-06-06, commit `d318485`). Restano
`economia`/`salute`, fuori host: il task si chiude (e il nodo `why` matura da `bozza` a `maturo`)
quando saranno raggiungibili e allineati.
