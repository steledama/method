---
data: 2026-11-23
stato: attiva
ciclo: runtime
target: nixos, nixos-lavoro, bi, economia, salute, baserow, danea-auto, abbinatore
---

# Versioni del canone

Prescrizione del 2026-11-23, decisa dal custode in sessione con `method`
(`o2/diffusione-oltre-custode-unico.md`, «Decisione del 2026-11-23»). La
regola vive in [method-development](../kb/method-development.md),
«Versioni» e «Contribuire al canone».

## Cosa cambia nel canone

- **Il canone ha versioni.** Tag `vMAJOR.MINOR.PATCH` con un rilascio GitHub
  e le note delle prescrizioni da recepire; un tag pubblicato non si sposta.
- **`tt-sviluppo` è il primo adottante trattato da estraneo.** Non ha più
  scrittura su `steledama/method`: un push da quell'utenza è rifiutato.
- **Il segnale dal basso diventa issue o PR**: issue col modello «segnale da
  adottante» per i segnali, PR per le proposte. Si aprono in sessione col
  custode, mai in un giro autonomo.
- **`/adottanti` è ritirato**: `method` non legge più gli adottanti di lavoro
  via ssh. Il marker `i3/allineamento-metodo.md` resta il modo in cui un
  adottante dichiara cosa ha recepito.
- **Ogni gruppo ha un coordinatore che è uno dei suoi repo**: `nixos` per
  casa (`salute`, `economia`), `nixos-lavoro` per il lavoro (`bi`,
  `baserow`, `abbinatore`, `danea-auto`). Il codice di sito e chat resta nel
  canone.

## Ricetta per gruppo

**Lavoro** (`nixos-lavoro`, `bi`, `baserow`, `abbinatore` su `svezia`,
`danea-auto` su `danea2`), in sessione col custode e coi giri fermi:

1. `/method` dal proprio marker al tag, nel coordinatore per il checkout
   condiviso di `svezia`;
2. `git -C ~/method fetch --tags` e `git -C ~/method switch --detach <tag>`:
   su `svezia` sposta insieme i quattro adottanti che leggono quel checkout;
   su `danea2` lo stesso nel checkout suo;
3. `method_version: <tag>` nel marker di ogni adottante;
4. nelle regole locali: il pull `--ff-only` del checkout di `method` lascia
   il posto a fetch dei tag e switch al tag rivisto; `/method` rivede fino
   all'ultimo tag, non fino a `main`; i segnali per `method` diventano issue
   o PR, in sessione;
5. `nixos-lavoro` dichiara nel proprio `world.md` e `README.md` il ruolo di
   coordinatore, coi membri e la versione di ciascuno.

**Casa** (`nixos`, `salute`, `economia` su `deck`): restano sul symlink a
`main`, dogfooding del custode. Recepiscono:

1. il ritiro di `/adottanti` e il canale per issue o PR, dove le regole
   locali ne parlano;
2. `nixos` come coordinatore: già fatto in `nixos` `afd5e8d`; resta il suo
   `goal.md`, decisione del custode;
3. `salute` ed `economia`: il loro `world.md` e `README.md` nominano
   `nixos`, non più `casa`, se ne parlano.

## Recepimento

Un adottante la dà recepita nel proprio marker; esce dall'indice quando tutti
l'hanno recepita.
