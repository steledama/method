---
data: 2026-06-06
stato: aperto
---

# Runbook — `why.md` per motivazione: completare il refactor da `log` su ogni repo

La migrazione del layout aveva cambiato il **nome** (`log.md → why.md`), non la **forma**:
gli adottanti restano log datati, append-only, con la decisione relegata a sottotitolo
dell'header `## [DATA] tipo | titolo`. Questo runbook porta la **sostanza** a coincidere col
nome — memoria interpretativa indicizzata per _motivazione_, non per data — replicando su
ogni repo il refactor già eseguito su `metodo`, `bi` e `nixos` (2026-06-06). Restano **`economia`**
e **`salute`**, fuori dall'host corrente.

## La decisione (forma A — già applicata a `metodo`, fissata nel nodo)

La forma e le convenzioni vivono nel nodo canonico [[why]] (`kb/why.md`), propagato via
**symlink** agli adottanti. **Conseguenza operativa chiave: lavorando in un repo adottante
NON si tocca il nodo** — lo si eredita già aggiornato. Si interviene solo sul `why.md` _di
quel repo_. Riassunto della forma:

1. **Chiave primaria = motivazione** (gruppo `##`, con una riga di intro in corsivo); la
   data è asse secondario _dentro_ il gruppo (`### [YYYY-MM-DD] tesi`, dalla più recente).
   Git possiede l'asse del tempo; `why` aggiunge quello del significato. **Guardia
   bottom-up:** solo temi già stabilizzati, niente scaffali vuoti — e nemmeno l'opposto.
   **Entry orfane:** un'entry isolata si **accorpa al filo più vicino per motivazione**; un
   gruppo mono-entry è ammesso solo se il filo è un principio guida riconosciuto del repo;
   mai un gruppo "varie". **Tie-break dell'ordine intra-gruppo:** a parità di data (o più
   `[storico]` senza data) vale l'ordine narrativo; una **sequenza numerata** (es. Fasi 1/2/3)
   resta adiacente e nell'ordine che si legge meglio, anche se viola il recent-first.
2. **Asse `tipo` eliminato** dalla forma finale, ma **usato come indizio di clustering**
   durante il refactor (i tag `architettura|pattern|fix|integrazione|…` aiutano a raggruppare).
3. **Supersessione esplicita:** un'entry superata resta in posizione e riceve una riga
   `> ↳ …` verso quella che la corregge. Mai cancellare (git conserva).
4. **Multi-tema:** entry nel gruppo più pertinente + rimandi agli altri. Anche il rimando è
   una riga `> ↳ …` sotto l'header: stesso meccanismo della supersessione, **verbo diverso** —
   «superata da …» per la supersessione, «vedi anche …» / «conseguenza di …» per il cross-link.
   Il dict `markers` dello script ospita entrambi gli usi.
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
   concettuali _già stabilizzati_ del repo. Una entry per gruppo-chiave; orfane e multi-tema
   secondo le regole di forma sopra (accorpa al filo vicino, rimando `> ↳`). Ordine
   intra-gruppo: dalla più recente, con i tie-break del punto 1.
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
   l'i3 del ciclo di sviluppo della sessione), con puntatori ai commit di riferimento (`metodo`
   `a9fbb82` e i repo già fatti).

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
# clusters = [("Titolo gruppo","intro",[idx,...]), ...]
# markers = {idx: "> ↳ ..."}  # supersessione («superata da…») o cross-link («vedi anche…»)
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

**Attenzione all'ordine col formatter:** lo script qui sotto verifica `result` _in memoria_,
prima di scrivere. Ma CLAUDE.md impone i formatter pre-commit, che girano **dopo**. Quindi la
verifica decisiva è la **seconda**, dopo `prettier`/`alejandra`/`ruff`, fatta contro il file su
disco rispetto a `git show HEAD:why.md` (vedi gate). Se `prose-wrap` non è `preserve`, prettier
reflowa il prosa e romperebbe il verbatim senza che il primo check se ne accorga.

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

- check verbatim (1ª, in memoria): 0 righe di corpo perse (al netto di preambolo e dump estratti).
- **formatter, poi 2ª verifica:** esegui i formatter pre-commit (`prettier --write why.md`, ecc.),
  poi **ri-controlla il verbatim contro `git show HEAD:why.md`** — è questa, sul file finale, a
  fare fede. (Vedi nota sull'ordine col formatter sopra.)
- `python3 scripts/kb_tools.py audit` → 0 link rotti, 0 nodi isolati.
- grep residui di forma vecchia: **ancorare a `^## \[`** (un `### [data]` contiene la
  sottostringa `## [`, falso positivo garantito); le menzioni di `append-only` / `tipo |`
  **tra virgolette** nei corpi verbatim e nell'entry di sessione sono attese, non residui.
- dump audit/lint non più nel `why.md`; snapshot al suo posto (o no-op se già potati).
- entry di sessione in testa al gruppo giusto, con puntatori ai commit di riferimento.
- commit in-repo `refactor(why): ribalta la memoria per motivazione`. **Push mai automatico.**
- **chiusura:** aggiorna la scheda per-repo e la riga `Stato` di questo runbook col commit
  appena fatto (commit separato nel repo `metodo`).

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

### `economia` / `salute` (rimasti, fuori host)

- **Non presenti su questo host.** Aprire la sessione _nel_ repo dove sono raggiungibili.
- **Precondizione:** se il file è ancora `log.md` invece di `why.md`, fare prima `git mv
log.md why.md` (il layout potrebbe non essere migrato).
- **`economia` ha file affiancati** `stato.md` / `scadenze.md` / `diario.md`: **NON** assorbire
  stato corrente, scadenze o materiale di diario dentro `why.md` — il `why` è memoria
  interpretativa, lo stato vive in quei file. Clusterizza solo le decisioni. Il `why` di
  economia è più breve: attesi **meno gruppi**, non forzare scaffali (vedi «Entry orfane»).
- **`salute`** ha `why.md` + `diario.md` (più personale/riflessivo): stessa cautela — why =
  memoria del progetto, diario = materiale personale.

## Filing back / chiusura

Il nodo [[why]] è la fonte canonica della forma. Quando `bi`, `nixos` (ed `economia`/`salute`
quando raggiungibili) sono allineati e verificati, il task si chiude: la riga sparisce da
`plan.md`, lo storico resta in git e nei `why.md`. La maturazione del nodo `why` da `bozza` a
`maturo` è il filing back atteso a refactor completo.

**Stato:** `metodo` ✅ fatto (2026-06-06, commit `a9fbb82`) — caso di riferimento. `bi` ✅ fatto
(2026-06-06, commit `59059c43`). `nixos` ✅ fatto (2026-06-06, commit `d318485`). Restano
`economia`/`salute`, fuori host: il task si chiude (e il nodo `why` matura da `bozza` a `maturo`)
quando saranno raggiungibili e allineati.
