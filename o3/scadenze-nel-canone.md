---
data: 2026-11-08
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto
---

# Il controllo di scadenze e ricorrenze è uno strumento del canone

## Cosa e perché

`kb/plan.md`, «Ricorrenze», fissava il contratto del controllo ma lasciava a
ogni adottante lo strumento. Le copie avevano già divergenze: un `by:` col solo
mese valeva il primo giorno in `economia` e l'ultimo in `nixos`, e il parser di
`economia` non riconosceva nessuna delle voci degli altri repo. Il 2026-11-08 il
custode ha deciso uno strumento solo, `o3/scadenze.py` (`d7ab2d2`, `b098a1b`;
contesto in `o2/strumento-scadenze.md`).

Decisioni che cambiano la lettura del plan:

- un `by:` col solo mese vale il suo ultimo giorno, come `Prossima`;
- in `## Scadenze` ogni data passata è scaduta, perché la sezione tiene solo date
  imposte dal Mondo; un appuntamento passato si toglie;
- una data nostra che deve restare visibile sta nel `by:`: entro 45 giorni entra
  nella catena come riesame in arrivo, senza contare come scadenza.

## Ricetta di recepimento

1. Lancia `python3 method/../o3/scadenze.py` nella radice del repo e leggi
   l'uscita. Ogni voce di `## Scadenze` e `## Ricorrenze` deve risultare una data
   o un rilievo; la riga finale `Lette:` dà i conti.
2. Porta il plan alla forma, partendo dai rilievi:
   - una riga che tornerebbe, fatta la cosa, va in `## Ricorrenze`;
   - una data nostra esce da `## Scadenze` e resta nel `by:` della sua chiosa,
     col giorno scritto se il giorno conta. Prima di togliere la riga verifica
     che i suoi dettagli stiano nella chiosa o nel task;
   - una voce di `## Scadenze` comincia con la data, ISO col giorno o il solo
     mese, eventualmente in grassetto e preceduta da `entro`, e un `—` o un `→`
     la separa dal testo. Niente `~`.
3. Solo se serve, crea `o3/scadenze.toml`: `formati_data = ["it"]` se il dominio
   scrive le date per una persona, `marcatori_chiusura` per le righe fatte da
   togliere. Assente il file valgono i default.
4. Nei fork di `exec plan` ed `eval compare` lancia lo strumento come fanno le
   skill canoniche, e leggi la catena a 45 giorni dalla sua uscita. Non entra
   nei `[[controllo]]` di `commit_gate.toml`: è un segnale, esce con 1 se c'è una
   scaduta e non ferma il commit. Con la skill che lo lancia aggiungi al
   `o3/ciclo/permessi.json` il solo permesso
   `Bash(python3 method/../o3/scadenze.py)`, concesso dal custode con questa
   prescrizione. Se il checkout del canone manca sull'host, il giro lo dice in
   `Attenzione:` e non salta il controllo in silenzio.
5. Se il repo ha uno strumento proprio che legge le stesse sezioni, togli la
   parte sovrapposta senza lasciare un wrapper. Le voci di dominio restano
   locali.
6. Registra il recepimento nel marker `i3/allineamento-metodo.md`, in una riga
   che nomina `scadenze-nel-canone` come recepita.

## Note per repo

Indizi dal confronto del 2026-11-08, da verificare in loco.

- `economia`: i `by:` col solo mese passano all'ultimo giorno. Le tre righe con
  la `~` escono da `## Scadenze` (Caprioli, Arsini, consuntivo Tigli), non prima
  dell'adozione, e il `by:` di Arsini diventa `2027-01-05`. Il consuntivo Tigli
  torna ogni anno: aggiungi la riga `task` in `## Ricorrenze`, già valutata con
  la sessione. Poi si cancellano `o3/check_scadenze.py` e il suo test, e si
  aggiornano i rimandi in `CLAUDE.md`, `goal.md`, skill, `o3/tools.md`,
  `o3/ciclo-finanze.md`, prompt e permessi del giro. I marcatori di riga chiusa
  servono solo se restano righe fatte in `## Scadenze`.
- `nixos` e `nixos-lavoro`: `maintenance-due.sh` perde il ramo dei `by:`, coi
  suoi test (`riesame.`); tiene registro e voci orfane. La legenda gli serve
  ancora per le `probe:`. In `exec plan` cade la nota sul controllo a lettura.
- `bi`: «raccolta prezzi» e «verifica inventari» sono ricorrenze rimaste in
  `## Scadenze`, e finché ci stanno risultano scadute con uscita 1. Il timetable
  dei run automatizzati esce come rilievo: righe `config` in `## Ricorrenze` o
  calendario di dominio.
- `salute`: serve il profilo con `formati_data = ["it"]`; con quello le voci si
  leggono tutte.
- `baserow`: nessuna sezione datata nel plan; bastano i fork di `exec` ed `eval`.
- `danea-auto`: nessuna sezione datata, 8 chiose con `**by:**`, che lo strumento
  legge. Da verificare che il comando giri su `danea2`.

## Verifica

`python3 o3/prescrizioni.py verifica scadenze-nel-canone` dà la prescrizione
recepita in ogni adottante. Nel repo, `python3 method/../o3/scadenze.py` non
stampa `RIGA_NON_RICONOSCIUTA`, oppure il giro le ha portate nel plan come
rilievi da correggere.
