---
ciclo: dev
---

# Il marker di allineamento trasloca in `i3/`; il nome del produttore vince solo senza collisione

Ratificato (custode, 2026-08-02) dalla percezione «il nome di un file di
output dovrebbe ereditare il nome del produttore» (nixos, consumata qui):
resta il principio, cade l'istanza concreta che l'ha innescato — sostituita
da una correzione più radicale.

## Il principio: nome-eredita-produttore, con una clausola di precedenza

Quando un output ha un produttore singolo e deterministico (uno script, una
skill) e nessun nome già vivo nello stesso spazio dei nomi confligge, il nome
del file dovrebbe riflettere il produttore: generalizza il criterio già in
canone in `kb/skill.md` — il "signifier onesto" giudicato per
`nix-overlay-update` — dai nomi delle skill ai file che le skill scrivono.
Corollario inciso in `kb/affordance-signifier.md`.

Il nome-funzione stabile vince quando l'eredità del nome del produttore
produrrebbe collisione o ambiguità con un nome già canone nello stesso
spazio dei nomi. È il caso concreto che ha innescato la percezione.

## Il caso concreto: perché `method-review.md` → `method.md` non regge

`nixos` (istruita dal custode) ha rinominato `method-review.md` →
`method.md`, in deroga alla clausola §3 di
`o3/skill-nomi-verbo-sostantivo.md` («il marker non cambia nome»). Verifica
sul materiale reale (`ls ~/nixos`): `method.md` siede accanto al symlink
`method` (→ `../method/kb`), già presente e identico nei quattro adottanti.
La coppia `method`/`method.md` è più ambigua di quella che sostituiva
(`method` symlink + `method-review.md`) — il nome nuovo non è un signifier
più onesto, lo è meno, proprio nella root che deve raccontare l'anatomia
senza aprire nulla (`kb/project-structure.md`).

La clausola §3 originale aveva la conclusione giusta (non rinominare in
root) ma la motivazione debole (stabilità del ledger nel tempo). La
motivazione vera è più radicale: **il marker non dovrebbe stare in root
affatto.** È lo stato corrente di una relazione (l'allineamento col canone),
non un cursore d'atrio come `goal.md`/`world.md` — la sua forma (cursore +
prosa di stato, aggiornata in place, non un log) è esattamente quella che il
canone già dà a **i3** (`kb/project-structure.md`, riga 117: «stato
attuale... non una sequenza di entry datate»).

`nixos` aveva già anticipato lo split, tenendo il verdetto narrativo in
`i3/allineamento-metodo.md` locale e solo il cursore in root. Questa
ratifica generalizza lo split fino in fondo: il cursore trasloca anch'esso
in `i3/`, un solo file per adottante, **nome uniforme tra i progetti**
(`i3/allineamento-metodo.md`, sul principio già in canone che le collezioni
standard portano nomi uniformi — `kb/project-structure.md`, riga 131) invece
del file ad hoc in root.

## Casi decisi

- Il marker (`method-review.md`/`method.md`) trasloca da root a
  `i3/allineamento-metodo.md` nei quattro adottanti: cursore
  (`method_commit`, `reviewed_at`, `status`) e verdetto narrativo fusi in un
  solo file, stessa forma-i3 di ogni altro filo.
- Il principio nome-eredita-produttore resta canone generale per output a
  produttore singolo, con la clausola di precedenza sul nome-funzione
  stabile quando collide.
- `nixos` è avanti sullo split concettuale ma sul posto sbagliato (root, non
  `i3/`): la correzione è nella prescrizione, non un rimprovero.

## Prossimi passi (fuori da questo filo, materia `exec`)

- Aggiornare `o3/skill-nomi-verbo-sostantivo.md` §3 (o emettere una
  prescrizione dedicata) col nuovo canone di posizione del marker, propagata
  ai quattro adottanti.
- `.claude/skills/method/SKILL.md` e `kb/skill.md` (riga 112) da aggiornare
  per riflettere `i3/allineamento-metodo.md` come sede canonica.
- `world.md` (riga 8) cita la superficie «marker `method-review.md`» — da
  aggiornare al nuovo path.
