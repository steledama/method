---
sintesi: "Gli adottanti copiano i builder delle viste e forkano kb_tools.py: le copie derivano e perdono il nucleo. Deciso dal custode il 2026-11-12: all'adottante restano solo identità, moduli di dominio e test; builder e nucleo dell'audit si lanciano dal checkout del canone, come già commit_gate.py. Fatti i passi sulle viste (descrizioni in project.py, build e serve con --root); restano l'audit KB e la prescrizione."
ciclo: dev
---

# Strumenti dal canone

## Origine

Domanda di sola lettura della sessione `nixos` su `deck`, inoltrata su
richiesta del custode il 2026-11-12, dopo una revisione del repo `nixos`.
Il custode ha adottato la risposta nella stessa sessione. Il messaggio non
porta autorizzazioni sugli adottanti: il loro recepimento passa da una
prescrizione e dal loro `/method`.

## Misura del 2026-11-12

Sui tre adottanti con checkout su `deck`, contro `method` a `cbd4c4e`:

- `o3/view/`: in `nixos` ed `economia` tutti i builder sono identici al
  canone tranne `project.py` e `build_system_image.py`, che differiva per le
  sole descrizioni degli stadi sulla home; `economia` aggiunge il modulo di
  dominio `deck.py`. `salute` ha anche un `build.py` divergente e tre moduli
  propri (`build_dashboard.py`, `build_deck.py`, `checks.py`);
- `kb_tools.py`: 881 righe nel canone, 1377 in `nixos`, 928 in `economia`,
  920 in `salute`. Il fork `nixos` non ha il comando `tasks`, la gestione
  delle traduzioni né `catalog_path`, e riscrive `inventory` e `coverage` per
  Nix; aggiunge `facts`, `fidelity` e i controlli system/home;
- `kb_profile.py` diverge in tutti e tre (differenze non lette).

Gli adottanti di lavoro (`nixos-lavoro`, `bi`, `baserow`, `danea-auto`) non
sono stati letti.

## Vincoli che oggi impongono la copia

- `publish.py` esporta il commit con `git archive` e lancia
  `<export>/o3/view/build.py`: i builder sono quelli del commit, e la
  provenienza dichiara un solo hash (`kb/view.md`, «Pubblicazione»);
- `build.py` e `serve.py` deducono la root da `Path(__file__).parents[2]` e
  importano `project` dalla propria cartella;
- `DECK_BUILDER` carica un modulo di dominio dalla stessa cartella;
- l'innesco dell'host riavvia `serve.py` sull'impronta di `o3/view/`;
- `kb_tools.py` deduce la root da `parents[1]` e non ha agganci oltre la
  costante `EXTENDED_FACETS`: `kb/kb-tools.md` prevede che l'adottante
  aggiunga `facts` e `fidelity` nel proprio file, cioè che forki.

## Passi

1. **Fatto il 2026-11-12.** Le descrizioni degli stadi sulla home passano
   da `build_system_image.py` a `project.py` (`DESCRIZIONI`, solo gli slot
   che il repo dice diversamente). Il file canonico torna uguale in ogni
   repo; un `project.py` senza il campo resta valido.
2. **Fatto in `method` il 2026-11-12.** `build.py` e `serve.py` accettano
   `--root DIR` (`radice.py`): la root è esplicita, non dedotta dalla
   cartella corrente, e `o3/view/` del repo reso va davanti ai builder per
   `project` e i moduli di dominio. Una copia dei builder accanto a
   `project.py` ferma la build invece di coprire il canone. La pubblicazione
   di un commit senza builder esporta `o3/view/` dal commit `HEAD` del
   canone: la versione è la coppia dei due commit, in `provenance.json`,
   sulla home e nel nome della release, e un canone avanzato la fa
   ricostruire. Provato su un export di `nixos` a cui restava il solo
   `project.py`: resa identica a quella della sua copia, salvo la
   descrizione di `o3` che aspetta `DESCRIZIONI`. Non ancora provata la
   pubblicazione reale dal canone esportato: `HEAD` deve prima contenere
   `radice.py`. Resta all'host l'impronta di riavvio, che deve guardare
   anche `o3/view/` del canone.
3. **Nucleo dell'audit con profilo e modulo di dominio.** `kb_tools.py`
   con `--root`, un profilo dichiarativo `o3/kb_tools.toml` (cartelle,
   catalogo, facet, estensioni ed esclusioni del codice) e un modulo di
   dominio opzionale che aggiunge sottocomandi e controlli all'`audit` e può
   sostituire `inventory` e `coverage`. Il solo toml non basta: i controlli
   di `nixos` sono codice. Stessa sorte per `kb_profile.py`, dopo aver letto
   le differenze.
4. **Una sola prescrizione** agli adottanti, aperta quando 2 e 3 girano in
   `method`: un giro di recepimento invece di tre. Fino ad allora il passo 1
   arriva a chi ricopia `build_system_image.py` senza altro da fare.

## Criterio di chiusura

I builder e il nucleo dell'audit girano dal canone su `method` e su un
adottante, con `kb/view.md` e `kb/kb-tools.md` aggiornati e la prescrizione
aperta. Riga del plan, voce in `o2/tasks.md` e questo file si rimuovono
nello stesso commit.

Connessioni:

- [view](../kb/view.md)
- [kb-tools](../kb/kb-tools.md)
- [method-development](../kb/method-development.md)
