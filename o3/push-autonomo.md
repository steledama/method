---
data: 2026-10-08
stato: attiva
ciclo: runtime
target: nixos, bi, economia, salute, crm, danea-auto, baserow
---

# Il push segue ogni commit senza richiesta

## Cosa e perché

Il custode ha deciso il 2026-10-08: **dopo ogni commit riuscito l'agente fa
il push del branch corrente su `origin`, senza richiesta**. Restano su
richiesta esplicita `--force`, `amend` di commit già pubblicati e il push di
altri branch; un push rifiutato non si forza, ci si ferma e si riferisce.
In `method` la regola vive in `CLAUDE.md` («Push remoto») e nel passo 7
della [skill canonica di commit](../.claude/skills/commit/SKILL.md).
`danea-auto` la applica già dal 2026-10-07 ed è il precedente.

È il primo passo verso un ciclo `eval` → `exec` che gira da solo e chiude con
un commit: finché il push resta un gesto del custode, ogni giro autonomo si
ferma sulla macchina che l'ha prodotto e gli altri checkout non lo vedono.

L'autorizzazione riguarda **solo il push git del repository**. Non copre gli
atti sul Mondo runtime: deploy, `nixos-rebuild`, comandi con `sudo`, push
di dati verso sistemi esterni. Quelli restano sotto le regole locali
([consent](../kb/consent.md)).

## Ricetta per il /method locale

1. Cercare le riserve sul push nelle bussole (`CLAUDE.md`, `AGENTS.md`),
   nei nodi `kb/` locali e nei fork delle skill (`commit`, `eval`, `exec` e
   quelle di dominio). Sostituirle con la regola sopra; nel fork di
   `/commit` aggiungere il passo di push dopo la verifica del commit.
2. **Residui di dominio**: verificare se un push sul remoto innesca qualcosa
   nel Mondo, ad esempio un host o un ciclo automatico che fa `pull` e poi
   esegue, una CI, un deploy. Dove succede, il push autonomo diventa un
   rilascio autonomo. Due vie: limitare l'autonomia a ciò che il ciclo
   automatico non esegue, oppure dichiarare che il rilascio segue il push.
   La scelta spetta al custode dell'adottante; finché non decide, quel push
   resta su richiesta e il motivo si scrive nella bussola.
3. Distinguere le riserve che parlano d'altro: «push» di dati verso servizi
   esterni (catalogo, notifiche) non è il push git e resta com'è.
4. Dove una skill giustificava un push automatico come eccezione alla regola
   generale (es. stato condiviso tra host), semplificare la giustificazione
   senza perdere i suoi limiti.
5. Registrare nel marker locale il recepimento o l'adattamento motivato.

## Indizi da verificare sul posto

Ricognizione su `.md` del 2026-10-08, da confrontare con i file correnti:

- **nixos**: `CLAUDE.md` (elenco «Richiedono autorizzazione esplicita» e
  «Push remoto»), `kb/common-commands.md`, `kb/development-workflow.md`,
  fork di `commit` e di `exec` (il push è escluso «in ogni caso»),
  `i3/allineamento-metodo.md`. In `manutenzione` il commit e il push sono
  già autonomi per lock condiviso e bump di `flake.lock`: quel paragrafo
  smette di essere un'eccezione. `sudo` e `nixos-rebuild` restano fuori.
- **bi**: nessuna riserva testuale trovata, ma `o3/scripts-auto.sh` e
  `o3/scripts-auto-morning.sh` fanno `pull` prima di girare: ogni push è
  un rilascio degli strumenti in produzione (cfr. `baserow`,
  `kb/bi-boundary.md`). È il caso del passo 2; il «push del catalogo» è
  dominio e non c'entra.
- **crm**: `CLAUDE.md` mette insieme push, deploy e operazioni distruttive.
  Separare il push git; deploy e distruttive restano su richiesta. Anche
  il fork di `commit`.
- **baserow**: `CLAUDE.md` («Push solo su richiesta esplicita») e il fork
  di `commit`. Verificare che nessun host faccia `pull` ed esegua.
- **danea-auto**: già allineato dal 2026-10-07 (`CLAUDE.md`, fork di
  `commit`). Basta confermare l'allineamento nel marker.
- **economia**, **salute**: non osservati in locale; cercare sul posto.
