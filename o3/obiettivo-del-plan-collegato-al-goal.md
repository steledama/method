---
data: 2026-09-30
stato: attiva
ciclo: dev
target: nixos, bi, economia, salute, crm, danea-auto
---

# La chiave `Ob.` della vista del plan porta al suo obiettivo

## Cosa e perché

La vista `tasks.html` rendeva la colonna `Ob.` del plan come testo nudo: un
`1` o una `S` che, dalla presentazione, non dicevano quale obiettivo il task
serve. Il numero va decifrato aprendo `goal.md` a mano. È un segnale
dell'utente: la direzione task→obiettivo c'è nel plan (`kb/plan.md`), ma la
vista non la rendeva percorribile.

Ora ogni chiave, nella tabella e nella riga di metadati della slide di
dettaglio, è un link all'intestazione corrispondente di `goal.md`. Una chiave
multipla (`1,2`) diventa un link per chiave. L'ancora non si scrive a mano: la
libreria condivisa la ricava dallo stesso parsing che già verificava le chiavi
contro il register (`goal_anchors`, di cui `goal_keys` è ora una vista), con lo
stesso `heading_slug` che la home usa per i link agli obiettivi runtime. Una
chiave che il register non ha continua a rompere la build nel contratto del
plan, prima di arrivare al rendering.

## Ricetta di recepimento

1. Nella libreria condivisa (`o3/presentation.py` o equivalente locale):
   sposta `heading_slug` dal generatore della home alla libreria, e sostituisci
   `goal_keys` con `goal_anchors` (chiave → ancora), tenendo `goal_keys` come
   insieme delle sue chiavi. Il generatore della home importa `heading_slug`
   dalla libreria invece di definirlo.
2. Nel generatore della vista (`o3/build_views.py`): la funzione `goal_links`
   rende le chiavi come link a `../goal.md#<ancora>`, in HTML nella tabella e
   in Markdown nella riga di metadati del dettaglio.
3. **Indizi per repo**, da verificare in loco: un fork senza colonna `Ob.` nel
   plan, o senza vista del plan generata, non ha nulla da recepire. Se il tuo
   `goal.md` intitola il Goal di sviluppo diversamente, o numera gli obiettivi
   a un altro livello di intestazione, l'adattamento vive nelle due regex della
   libreria, non nella vista.
4. Rigenera le viste: la home deve restare identica (il refactor di
   `heading_slug` non la tocca) e `git status` deve essere vuoto alla seconda
   rigenerazione consecutiva.

## Chiusura

La prescrizione resta attiva finché i sei adottanti non l'hanno recepita nel
proprio fork, dove esiste una vista del plan con la colonna `Ob.`, e non hanno
aggiornato il marker `i3/allineamento-metodo.md`.
