---
description: Revisiona il drift di un repo adottante rispetto ai commit del metodo.
user-invocable: true
---

# method

Esegui questa skill dalla root di un repository che adotta `method`. La copia
canonica vive nel repo `method`; ogni adottante la forka e può aggiungere
superfici locali, senza cambiare il protocollo del marker.

La revisione confronta l'evoluzione del metodo con lo stato locale corrente. Non
è un diff meccanico tra repository: i nodi metodologici arrivano normalmente via
symlink, mentre README, CLAUDE, AGENTS, porte root, skill e strumenti sono fork
locali che richiedono giudizio.

## Confini

- Non modificare altri repo adottanti.
- Non sostituire `/exec plan`: qui si valuta la relazione adottante-metodo;
  l'eventuale lavoro futuro entra in `o1/plan.md`/`o2/` locale.
- Non applicare automaticamente differenze editoriali o di dominio.
- Non certificare configurazioni host esterne ai repository.
- Non usare la data come cursore: il cursore è sempre uno SHA completo di
  `method`.

## Marker versionato

Il marker vive in `i3/allineamento-metodo.md` nell'adottante — non in root:
la root ospita il symlink `method` verso il canone (`../method/kb`), e un
marker con nome simile accanto ad esso è un signifier ambiguo, non un ledger
onesto (`i3/allineamento-marker-stadio.md` nel repo `method`). È insieme
cursore machine-readable e verdetto — cursore e narrazione fusi in un solo
file-i3, forma «stato attuale aggiornato in place», non un log. `ciclo: dev`
perché la relazione con `method` è materia del proprio artefatto (dev),
non del Mondo runtime che l'adottante gestisce nel proprio dominio:

```markdown
---
ciclo: dev
method_commit: <SHA completo di method>
reviewed_at: YYYY-MM-DD
status: aligned
---

# Allineamento con method

Cursore del canale col canone: il marker nel frontmatter è l'ultimo commit di
`method` recepito. Il corpo tiene il contratto durevole (divergenze e
adattamenti che la prossima review non deve ri-segnalare) e il verdetto
sull'allineamento, aggiornato in place; la cronaca dei giri resta nella
storia git di questo file.

## Adattamenti intenzionali

- Nessuno.

## Limiti

- Configurazioni host esterne ai repository non verificate.
```

Valori ammessi per `status`:

- `aligned`: ogni cambiamento pertinente nell'intervallo **e ogni
  prescrizione aperta in `o3/` di `method`** è già soddisfatto, applicato,
  preservato come divergenza intenzionale o tracciato in un task locale;
- `action-required`: report intermedio; il marker `method_commit` deve restare
  fermo al precedente commit revisionato.

Il marker resta anche quando lo stato è `aligned` e non ci sono tensioni:
il cursore e il contratto servono alla prossima revisione. La chiusura dei fili
ordinari non ne autorizza la rimozione (`kb/verdict.md` nel canone).

Gli adattamenti intenzionali devono dire quale superficie diverge, perché e, se
utile, da quale commit del metodo deriva la decisione. Non usare il ledger come
changelog: la storia delle revisioni resta in Git. Il file non ha una sezione
«Esiti»: la tabella per commit è output di sessione (passo 6) e non entra mai
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

Leggi `method_commit` dal frontmatter di `i3/allineamento-metodo.md` e verifica:

```bash
git -C "$method_repo" cat-file -e "<SHA>^{commit}"
git -C "$method_repo" merge-base --is-ancestor "<SHA>" HEAD
git -C "$method_repo" log --reverse --format='%H%x09%ad%x09%s' \
  --date=short "<SHA>..HEAD"
```

Per ogni commit pertinente, usa `git show --stat --oneline <SHA>` e
`git show --format=fuller <SHA> -- <path>` solo sui path necessari.

Se `i3/allineamento-metodo.md` non esiste (né, per repo non ancora migrati,
`method-review.md` in root), non inventare un baseline silenziosamente.
Ricostruisci l'ultimo allineamento verificabile dalla storia locale e da quella
di `method`, proponi lo SHA iniziale all'utente e crea il marker solo dopo
conferma. Un commit locale con stesso soggetto o timestamp è un indizio, non una
prova sufficiente da solo.

### 3. Rileggi le prescrizioni aperte

Il delta dei commit non basta: una prescrizione nata prima del cursore e
rimasta aperta esce dall'intervallo, e il marker che avanza la coprirebbe
senza che nessuno l'abbia riletta. A ogni giro, quindi, leggi l'elenco in
`## Contenuti` di `o3/prescriptions.md` nel repo `method` e apri ogni
prescrizione elencata:

```bash
sed -n '/^## Contenuti/,$p' "$method_repo/o3/prescriptions.md"
```

Per ciascuna verifica **nei file** dell'adottante, non nel marker né nella
storia dei giri precedenti, se è pertinente e se è recepita. La prescrizione
dice cosa cercare e dove; un `rg` mirato sulle superfici che nomina di solito
basta. Una prescrizione già soddisfatta costa una ricerca; una registrata come
divergenza intenzionale nel ledger non si ri-segnala. Le prescrizioni entrano
nella tabella del passo 6 con la colonna `Commit` sostituita dal nome del
file (`o3/<nome>.md`) e si classificano con gli stessi esiti del passo 5.

### 4. Controlla le superfici

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

### 5. Classifica ogni cambiamento

Assegna a ogni cambiamento e a ogni prescrizione aperta uno dei seguenti
esiti:

- `gia-soddisfatto`: lo stato locale implementa già il cambiamento;
- `diretto`: va applicato senza reinterpretazione di dominio;
- `adattamento`: il principio è pertinente, la forma locale va decisa;
- `non-pertinente`: il cambiamento riguarda solo `method` o un altro dominio;
- `divergenza-intenzionale`: la differenza locale va preservata e registrata;
- `task-locale`: il cambiamento è pertinente ma non va completato nella sessione.

Un commit può produrre più righe se tocca superfici con esiti diversi. I nodi
condivisi via symlink sono `gia-soddisfatto` salvo riferimenti locali stantii.

### 6. Presenta e applica

Prima delle modifiche presenta una tabella sintetica:

| Commit | Cambiamento | Esito | Azione locale |
| ------ | ----------- | ----- | ------------- |
| ...    | ...         | ...   | ...           |

La tabella è output di sessione: si presenta nella conversazione e resta nel
riepilogo finale, **non si scrive in `i3/allineamento-metodo.md`**.

Applica cambiamenti diretti solo dopo conferma esplicita. Per gli adattamenti,
proponi la forma locale e attendi conferma. Se una voce resta futura, crea o
aggiorna un task nel repo adottante e usa `/exec plan` per inserirlo nel plan.

### 7. Chiudi la revisione

Il marker può avanzare a `HEAD` di `method` solo quando ogni voce pertinente,
commit dell'intervallo o prescrizione aperta, è:

- applicata;
- già soddisfatta;
- registrata come divergenza intenzionale; oppure
- affidata a un task locale esistente e linkato nel riepilogo della sessione.

Aggiorna `i3/allineamento-metodo.md` in place, mantenendo solo lo stato
corrente. Se resta una voce pertinente senza una delle risoluzioni sopra,
imposta `status: action-required` e non cambiare `method_commit`. Se il
repo ha ancora `method-review.md`/`method.md` in root, spostalo in
`i3/allineamento-metodo.md` come parte di questa chiusura, non come voce
separata.

Concludi riportando:

- intervallo revisionato;
- prescrizioni aperte rilette e loro esito;
- conteggio per esito;
- file modificati;
- task locali creati o aggiornati;
- nuovo marker, oppure motivo per cui è rimasto fermo;
- limite esplicito sulle configurazioni host non verificate.
