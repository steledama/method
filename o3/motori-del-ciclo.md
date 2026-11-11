---
data: 2026-11-11
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto
---

# Motori del ciclo e fallback

Prescrizione del 2026-11-11, decisa dal custode in sessione con `method`.

## Cosa cambia nel canone

- Il profilo del repo, `o3/ciclo/lanciatore.toml`, sceglie il motore:
  `motori = ["claude", "codex"]` (il primo lavora, il secondo subentra una
  volta sola se il primo è indisponibile prima di qualunque atto), anche nel
  verso opposto, oppure un motore solo. Senza la chiave vale `["claude"]`:
  chi non la scrive non cambia comportamento.
- `budget_usd` è il tetto dove il motore lo sa imporre. Codex non ne ha uno:
  il giro procede e la chiusura dichiara `budget_usd_imposto: false`.
- Codex passa dall'esecutore canonico `o3/esecutore_codex.py`, che traduce i
  permessi di `o3/ciclo/permessi.json` e l'hook sul commit. Nessun host scrive
  un proprio esecutore.
- Le opzioni host `--codex-adapter` e `--codex-senza-tetto-usd`, pubblicate
  poche ore prima e non usate da nessuno, sono tolte. L'host dà solo i
  binari (`--claude`, `--codex`), il recinto, l'arresto e il trigger.
- Contratto completo: [fallback](ciclo/fallback.md).

## Il confine: chi configura cosa

Ogni repo configura solo sé stesso, nel proprio `o3/ciclo/`: prompt,
permessi, profilo (motori, minuti, tetto). Un repo `nixos` è l'host dei giri
degli altri, ma della loro politica non tiene nulla: dà binari, recinto,
arresto, orario e un paracadute fisico dell'unità (`RuntimeMaxSec`) sopra i
`minuti` del profilo, ricavato e non deciso. Per sé stesso, come adottante,
`nixos` ha il proprio `lanciatore.toml` come ogni altro repo.

Casa e lavoro hanno due `nixos` distinti; in comune c'è solo `method`.
La ricetta è la stessa, la eseguono due sessioni diverse.

## Ricetta per un repo adottante (tutti)

Da fare nella sessione del repo, con `/method`:

1. Recepire il canone: nessun cambio di comportamento senza `motori`.
2. Quando il custode decide di accendere il secondo motore: aggiungere
   `motori` al profilo (crearlo se manca, con i soli valori che si
   discostano dai default) e committarlo. Il profilo è in `o3/ciclo/`,
   protetto: lo cambia la sessione col custode, non il giro.
3. Verificare che `permessi.json` regga anche per Codex: gli strumenti senza
   regola di nome (per esempio `Skill(…)`) in Codex non esistono, le skill si
   leggono come file; un comando che il giro usa con sostituzioni (`$(…)`)
   l'esecutore lo rifiuta.

## Ricetta per l'host (ciascun nixos, e danea-auto)

1. Nello script che lancia `o3/lanciatore.py`: passare `--codex` col percorso
   del binario quando non è nel PATH dell'unità; togliere `--codex-adapter` se
   mai aggiunto.
2. Nel recinto: `CODEX_HOME` (con `auth.json`) leggibile dall'agente, la rete
   consentita, l'interprete Python del lanciatore raggiungibile (l'esecutore
   gira con lo stesso `sys.executable`).
3. Togliere dal registro dei cicli la politica per repo che appartiene al
   profilo: budget (`maxBudgetUsd`) e durata dell'agente. L'unità tiene un
   paracadute sopra i `minuti` del profilo, ricavato da esso o con un margine
   unico, non un valore per repo.
4. Primo giro col secondo motore: a mano, col custode presente. L'attivazione
   del timer resta della sessione locale.

### Casa: `nixos` su `deck`

Giri di `method`, `nixos`, `economia`, `salute`. Task locale già aperto:
`o2/ciclo-fallback-codex.md` di `nixos`, che va aggiornato: niente
`--codex-adapter` né `--codex-senza-tetto-usd`, il motore lo sceglie ciascun
repo. `cicli.nix` passa `--codex` nello script `lancia` e smette di tenere
`maxBudgetUsd` per gli altri repo.

### Lavoro: `nixos-lavoro` su `norvegia`/`svezia`

Giri di `nixos-lavoro`, `bi`, `baserow`. L'adattatore host
`o3/modules/home/ciclo/ciclo-canonico.py` copre già recinto, arresto e
controlli d'ingresso: aggiunge solo `--codex`. Il task locale
`o2/lanciatore-canonico.md`, passo 4, chiedeva un esecutore Codex: ora è
canonico, e il passo diventa la verifica nel proprio recinto.

### Lavoro: `danea-auto` su `danea2` (Windows)

Host e adottante coincidono: il trigger è dello scheduler di Windows. Passa
`--codex` se serve. L'esecutore è Python come il lanciatore; restano da
verificare su Windows la sandbox di Codex e la quotatura del comando
dell'hook.

## Verifiche aperte prima di contare sul fallback

Elencate nel contratto, sezione «Verified and still open»: giro completo dal
vivo attraverso il lanciatore, forma reale di un errore di quota di Codex,
`git push` dalla sandbox di Codex, Windows.
