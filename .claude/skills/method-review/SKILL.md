---
description: Revisiona il drift di un repo adottante rispetto ai commit del metodo.
user-invocable: true
---

# method-review

Esegui questa skill dalla root di un repository che adotta `method`. La copia
canonica vive nel repo `method`; ogni adottante la forka e può aggiungere
superfici locali, senza cambiare il protocollo del marker.

La revisione confronta l'evoluzione del metodo con lo stato locale corrente. Non
è un diff meccanico tra repository: i nodi metodologici arrivano normalmente via
symlink, mentre README, CLAUDE, AGENTS, porte root, skill e strumenti sono fork
locali che richiedono giudizio.

## Confini

- Non modificare altri repo adottanti.
- Non sostituire `/plan-review`: qui si valuta la relazione adottante-metodo;
  l'eventuale lavoro futuro entra in `o1/plan.md`/`o2/` locale.
- Non applicare automaticamente differenze editoriali o di dominio.
- Non certificare configurazioni host esterne ai repository.
- Non usare la data come cursore: il cursore è sempre uno SHA completo di
  `method`.

## Marker versionato

Il marker vive in `method-review.md` nella root dell'adottante. È insieme cursore
machine-readable e ledger umano:

```markdown
---
method_commit: <SHA completo di method>
reviewed_at: YYYY-MM-DD
status: aligned
---

# Method review

Cursore del canale col canone: il marker nel frontmatter è l'ultimo commit di
`method` recepito. Questo register tiene solo il contratto durevole
(divergenze e adattamenti che la prossima review non deve ri-segnalare); il
verdetto sull'allineamento vive in un filo `i3/`, la cronaca dei giri nella
storia git di questo file.

## Adattamenti intenzionali

- Nessuno.

## Limiti

- Configurazioni host esterne ai repository non verificate.
```

Valori ammessi per `status`:

- `aligned`: ogni cambiamento pertinente nell'intervallo è già soddisfatto,
  applicato, preservato come divergenza intenzionale o tracciato in un task
  locale;
- `action-required`: report intermedio; il marker `method_commit` deve restare
  fermo al precedente commit revisionato.

Gli adattamenti intenzionali devono dire quale superficie diverge, perché e, se
utile, da quale commit del metodo deriva la decisione. Non usare il ledger come
changelog: la storia delle revisioni resta in Git. Il file non ha una sezione
«Esiti»: la tabella per commit è output di sessione (passo 5) e non entra mai
nel file; il verdetto sull'allineamento vive in un filo `i3/` dell'adottante,
aggiornato in place. Una divergenza riassorbita si cancella dal ledger, non si
annota come evento: la sua storia è il diff.

## Procedura

### 1. Risolvi il repository del metodo

Individua il checkout tramite il symlink locale `method/`, che normalmente punta
alla directory `kb/` del repo:

```bash
method_kb="$(readlink -f method)"
method_repo="$(git -C "$method_kb" rev-parse --show-toplevel)"
git -C "$method_repo" status --short
git -C "$method_repo" log -1 --format='%H %ad %s' --date=short
```

Se il checkout di `method` è dirty, la revisione usa comunque `HEAD` e dichiara
che le modifiche non committate sono fuori intervallo. Non fare fetch o pull
automatici: il confronto è con il checkout disponibile.

### 2. Determina l'intervallo

Leggi `method_commit` dal frontmatter di `method-review.md` e verifica:

```bash
git -C "$method_repo" cat-file -e "<SHA>^{commit}"
git -C "$method_repo" merge-base --is-ancestor "<SHA>" HEAD
git -C "$method_repo" log --reverse --format='%H%x09%ad%x09%s' \
  --date=short "<SHA>..HEAD"
```

Per ogni commit pertinente, usa `git show --stat --oneline <SHA>` e
`git show --format=fuller <SHA> -- <path>` solo sui path necessari.

Se `method-review.md` non esiste, non inventare un baseline silenziosamente.
Ricostruisci l'ultimo allineamento verificabile dalla storia locale e da quella
di `method`, proponi lo SHA iniziale all'utente e crea il marker solo dopo
conferma. Un commit locale con stesso soggetto o timestamp è un indizio, non una
prova sufficiente da solo.

### 3. Controlla le superfici

Confronta i commit dell'intervallo con lo stato locale attuale:

- `README.md`, `CLAUDE.md`, `AGENTS.md`;
- cruscotto e porte (`o1/plan.md`, fili `i3/`, `kb/kb.md`, register `goal.md`/`world.md`,
  collezioni `i1/`-`o3/`, `presentation/`);
- riferimenti locali ai nodi metodologici condivisi;
- `.claude/skills/` e `.codex/skills/`;
- strumenti forkati in `o3/`;
- convenzioni strutturali applicabili;
- eventuali adattamenti intenzionali già registrati.

Usa ricerche mirate (`rg`) e diff dei singoli file. Non copiare alla cieca le
skill canoniche: conserva formatter, comandi, fonti di verità e checklist di
dominio locali.

### 4. Classifica ogni cambiamento

Assegna uno dei seguenti esiti:

- `gia-soddisfatto`: lo stato locale implementa già il cambiamento;
- `diretto`: va applicato senza reinterpretazione di dominio;
- `adattamento`: il principio è pertinente, la forma locale va decisa;
- `non-pertinente`: il cambiamento riguarda solo `method` o un altro dominio;
- `divergenza-intenzionale`: la differenza locale va preservata e registrata;
- `task-locale`: il cambiamento è pertinente ma non va completato nella sessione.

Un commit può produrre più righe se tocca superfici con esiti diversi. I nodi
condivisi via symlink sono `gia-soddisfatto` salvo riferimenti locali stantii.

### 5. Presenta e applica

Prima delle modifiche presenta una tabella sintetica:

| Commit | Cambiamento | Esito | Azione locale |
| ------ | ----------- | ----- | ------------- |
| ...    | ...         | ...   | ...           |

La tabella è output di sessione: si presenta nella conversazione e resta nel
riepilogo finale, **non si scrive in `method-review.md`**.

Applica cambiamenti diretti solo dopo conferma esplicita. Per gli adattamenti,
proponi la forma locale e attendi conferma. Se una voce resta futura, crea o
aggiorna un task nel repo adottante e usa `/plan-review` per inserirlo nel plan.

### 6. Chiudi la revisione

Il marker può avanzare a `HEAD` di `method` solo quando ogni voce pertinente è:

- applicata;
- già soddisfatta;
- registrata come divergenza intenzionale; oppure
- affidata a un task locale esistente e linkato nel riepilogo della sessione.

Aggiorna `method-review.md` in place, mantenendo solo lo stato corrente. Se resta
una voce pertinente senza una delle risoluzioni sopra, imposta
`status: action-required` e non cambiare `method_commit`.

Concludi riportando:

- intervallo revisionato;
- conteggio per esito;
- file modificati;
- task locali creati o aggiornati;
- nuovo marker, oppure motivo per cui è rimasto fermo;
- limite esplicito sulle configurazioni host non verificate.
