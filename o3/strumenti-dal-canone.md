---
data: 2026-11-12
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto
---

# Builder delle viste e audit KB lanciati dal canone

Prescrizione del 2026-11-12, dal task «Strumenti dal canone» (chiuso il 2026-11-13, in git),
decisa dal custode in sessione con `method` su una domanda della sessione
`nixos`.

## Il segnale

Una revisione di `nixos` ha trovato due duplicazioni col canone. In
`o3/view/` dieci file su dodici erano identici a quelli di `method`, e gli
altri due differivano per l'identità del repo. `kb_tools.py` era un fork di
1377 righe contro le 881 del canone, che aveva perso il comando `tasks` e
la gestione delle traduzioni. Su `economia` e `salute` la misura è la
stessa specie: copie ferme e fork che non ricevono più il nucleo. Una copia
deriva senza che nessuno lo veda; `commit_gate.py` e `skill_tools.py` si
lanciano già dal checkout del canone e non hanno questo difetto.

## Cosa cambia nel canone

- `o3/view/build.py` e `serve.py` accettano `--root DIR` e rendono un altro
  repo coi builder di `method`. La cartella `o3/view/` del repo va davanti
  ai builder: lì stanno `project.py` e i moduli di dominio. Una copia dei
  builder rimasta accanto ferma la build.
- `project.py` ha il campo `DESCRIZIONI`: le descrizioni degli stadi sulla
  home che il repo dice diversamente dal canone. `build_system_image.py`
  non si modifica più.
- La pubblicazione di un commit senza builder usa quelli del commit `HEAD`
  di `method`, esportati puliti. La versione servita è la coppia dei due
  commit: sta in `provenance.json`, sulla home e nel nome della release, e
  un canone avanzato la fa ricostruire.
- `o3/kb_tools.py` accetta `--root DIR` e legge dal repo due file
  opzionali: il profilo `o3/kb_tools.toml` (cartelle, catalogo, facet,
  estensioni ed esclusioni del codice) e il modulo `o3/kb_domain.py` coi
  controlli che sono codice. Il modulo aggiunge sottocomandi, entra nel
  report di `audit` e può sostituire `inventory` e `coverage`; gli altri
  comandi base restano del nucleo.
- `kb_profile.py` aveva già `--root`: le copie negli adottanti sono solo
  ferme.

## Cosa fa l'adottante

Indizi da verificare in loco, col proprio `/method`:

1. **Viste.** Porta in `project.py` le descrizioni che aveva cambiato in
   `build_system_image.py` (`DESCRIZIONI`). Rimuove da `o3/view/` i builder
   canonici, `assets/` e `ruff.toml`; restano `project.py`, i moduli di
   dominio e i test propri. Dove citava `python3 o3/view/build.py` o
   `serve.py` (skill, `CLAUDE.md`, `o3/commit_gate.toml`, permessi, unità
   dell'host) scrive `python3 method/../o3/view/build.py --root .`. Chi ha
   un `build.py` divergente (`salute`) porta prima la differenza in un
   modulo di dominio o la propone al canone.
2. **Servizio.** L'innesco che riavvia `serve.py` sull'impronta di
   `o3/view/` guarda anche `o3/view/` del checkout di `method`. È materia
   dell'host: per i repo serviti da un `nixos` il cambio va lì.
3. **Audit KB.** Sposta le costanti cambiate nel fork in `o3/kb_tools.toml`
   e i controlli propri (`facts`, `fidelity`, controlli di struttura) in
   `o3/kb_domain.py`, poi rimuove il fork e la copia di `kb_profile.py`.
   I comandi diventano `python3 method/../o3/kb_tools.py --root . <comando>`.
   Il nucleo può segnalare ciò che il fork non vedeva: si corregge o si
   dichiara, non si spegne.
4. Dichiara il recepimento nel marker `i3/allineamento-metodo.md`, nella
   forma «`strumenti-dal-canone` … recepita».

## Verifica

`python3 method/../o3/view/build.py --root . --check` e
`python3 method/../o3/kb_tools.py --root . audit` passano dal gate di
commit dell'adottante, e `o3/view/` non contiene più file uguali a quelli
del canone. Dove la vista è pubblicata, la home mostra il commit di
`method` accanto a quello del repo.
