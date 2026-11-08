---
sintesi: "Un solo controllo di scadenze e ricorrenze nel canone, o3/scadenze.py, che attua il contratto di kb/plan.md con un profilo locale minimo; gli strumenti degli adottanti restano alle voci di dominio."
ciclo: dev
---

# Strumento delle scadenze

## Origine

Inoltro della sessione `nixos` su `deck`, 2026-11-08, su richiesta del custode.
`kb/plan.md`, «Ricorrenze» (`06938c0`, `f6d9a50`), fissa il contratto del
controllo ma il canone non fornisce lo strumento. Analisi portata al custode e
approvata in sessione il 2026-11-08, con le tre decisioni qui sotto. Non c'è
urgenza: la prima `Prossima` di `nixos` è 2027-11.

## Perché non basta adottare `check_scadenze.py`

Stato letto il 2026-11-08. Una sessione di `economia` ha recepito nel frattempo
il contratto, in modifiche non ancora committate: `## Ricorrenze` e rilievi di
forma ci sono. Lo strumento del canone serve comunque, perché una copia per
adottante non regge le differenze che seguono.

- La sua regex non riconosce nessuna delle 19 voci di `## Scadenze` di `bi`,
  `nixos-lavoro` e `salute`, che scrivono le date ciascuno a modo suo: con quel
  parser sarebbero tutte rilievi.
- La sua legenda accetta una sola forma di chiosa, e la colonna del task è letta
  per posizione.
- `economia` e `nixos` danno già due letture del `by:` col solo mese: primo
  giorno la prima, ultimo la seconda.
- `maintenance-due.sh` di `nixos` non legge `Prossima`, e
  `.claude/skills/exec/plan.md` di quel repo dichiara il controllo a lettura.

La grammatica del plan c'è già in `o3/view/sources.py` (`_PROSSIMA`,
`_CADENZE`, `_LEGEND_ENTRY`, che accetta entrambe le forme di legenda). Lo
strumento non la importa, perché `o3/view/` la forkano gli adottanti e lui deve
girare col solo stdlib: `tests/test_scadenze.py` verifica che coincidano.

## Decisioni del custode (2026-11-08)

1. **`by:` col solo mese:** vale il suo ultimo giorno, come `Prossima`. In
   `economia` i riesami arrivano fino a un mese dopo.
2. **Date passate in `## Scadenze`:** ogni data passata della sezione è scaduta,
   perché lì stanno solo date imposte dal Mondo. `entro` distingue solo in
   `## Ricorrenze`. Gli appuntamenti passati si tolgono dal plan.
3. **Date di `salute`:** il profilo ammette il formato `it`, perché quelle date
   le legge una persona; non si riscrivono in ISO.

## Forma dello strumento

- `o3/scadenze.py`, lanciato dal checkout del canone come il gate:
  `python3 method/../o3/scadenze.py`. È distinto da `commit_gate.py` e chiede
  una riga in ogni `o3/ciclo/permessi.json`.
- Copre la catena di `## Scadenze` e `## Ricorrenze`, le finestre `!`, i `by:`
  passati e i rilievi di forma. Non valuta le `probe:`.
- In quelle due sezioni ogni voce è una data interpretata o un rilievo col suo
  testo, senza euristica sull'«aspetto di scadenza».
- Il profilo `o3/scadenze.toml` è opzionale e riguarda solo il formato delle
  righe: formati di data aggiuntivi da un elenco chiuso e marcatori di riga
  chiusa. Stati, codice di uscita e divieto di scarti silenziosi non si
  configurano.
- La saltata stampa quante occorrenze ha perso, calcolate da `Prossima` e
  cadenza: `eval compare` ha il dato senza storico.

## Come lo riceve il giro

- È un segnale, non un gate: non entra nei `[[controllo]]` di
  `commit_gate.toml`. Esce con 1 solo per le scadute e con 2 per un errore dello
  strumento.
- Lo lanciano `exec plan` ed `eval compare`, senza scambiarsi file.
- Se il checkout del canone manca sull'host, il giro lo dice in `Attenzione:` e
  non salta il controllo in silenzio.

## Da fare

1. Fatto il 2026-11-08: `o3/scadenze.py` e `tests/test_scadenze.py`. Provato
   sugli otto plan: su ognuno le righe delle due sezioni sono date, `config` o
   rilievi, nessuna sparisce.
2. `kb/plan.md`: il canone fornisce lo strumento, con le decisioni 1 e 2.
3. `/exec` ed `/eval` canoniche lo lanciano, `o3/ciclo/permessi.json` di
   `method` lo concede.
4. Prescrizione agli adottanti, ciascuno col proprio `/method`, senza cambio
   simultaneo:
   - `economia` sposta in `## Ricorrenze` le righe con cadenza, che portano via
     le `~`, poi cancella `check_scadenze.py` senza wrapper e aggiorna i
     riferimenti; da fare quando la sessione aperta lì sul file ha chiuso;
   - `nixos` e `nixos-lavoro` tolgono da `maintenance-due.sh` il ramo `by:`, e
     tengono registro e voci orfane;
   - `bi` sposta il timetable e gli orologi manuali, che i rilievi faranno
     emergere.

## Verifica di riuscita

- Sul plan di prova ogni voce è una data o un rilievo, e le righe di
  `## Ricorrenze` hanno il loro stato.
- Lanciato su ogni adottante con sezioni datate, nessuna voce sparisce: il
  numero di voci interpretate più i rilievi è il numero di voci della sezione.
- La Prova annuale del seed di `nixos` compare nella catena senza controlli a
  lettura.
