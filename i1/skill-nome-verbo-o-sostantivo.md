---
ciclo: runtime
---

# Segnale: il nome di una skill di dominio è verbo o sostantivo?

Data: 2026-08-01 · Fonte: nixos — terza rinomina della stessa skill di
dominio in poche settimane (`update` → `aggiorna` → `manutenzione`)

## Il segnale

`method/skill.md` («La regola dei nomi») fissa la forma delle canoniche — un
nome solo, mai la cadenza — ma non dice nulla sulla **classe grammaticale**
del nome per le skill di dominio, e il canone stesso non è uniforme:

- `eval`, `exec` — verbi (infinito troncato, il telos inglese dichiarato)
- `kb-review`, `method-review` — sostantivi composti (nome + review)
- `commit` — ambiguo, coincide in inglese con verbo e sostantivo

Sulle skill di dominio l'incoerenza è più visibile perché **oscilla nel
tempo sulla stessa skill**, non solo tra skill diverse:

- `nixos`: `update-review` → `update` → `aggiorna` (verbo imperativo,
  2026-07-12) → `manutenzione` (sostantivo, proposto 2026-08-01) — tre rename
  in meno di un mese sulla stessa capacità
- `nixos`: `nix-overlay-update` → `aggiorna-overlay` (sostantivo composto)
- `economia`: `monthly-review` → `finanze-review` (sostantivo composto,
  2026-07-12, «rinominata proprio per il corollario del nome: l'oggetto
  tenuto onesto sono le finanze, non il mese» — stesso corollario di
  `skill.md`, non decide però tra verbo e sostantivo)
- `economia`: `ordini <fornitore>` (sostantivo plurale + argomento) citato
  in `skill.md` come caso vicino a `aggiorna <scope>`, mai confrontato sulla
  forma

## L'attrito osservato

Ogni rename in `nixos` è stato motivato da un argomento valido e locale (il
nome deve dire l'oggetto tenuto onesto, non lo strumento; l'ambito è
cresciuto e il vecchio nome copriva solo metà del lavoro). Nessuno dei tre
argomenti però ha mai toccato la domanda "verbo o sostantivo" — è rimasta
implicita, decisa per gusto ogni volta. Il costo visibile: tre commit di
rename sulla stessa skill in un mese, ognuno che tocca `CLAUDE.md`, `README`,
`o3/prescriptions.md`, i fili `i3/` pertinenti — lo stesso costo di
propagazione che la regola-nomi del canone cerca altrove di evitare
dichiarando un nome stabile una volta per tutte.

Un'ipotesi affiorata in sessione (non verificata contro altri adottanti): le
canoniche sono verbi perché **compiono uno stadio del ciclo** (`eval`
valuta, `exec` esegue); una skill di dominio che **osserva un'area** più che
compiere un'azione singola (`manutenzione` sorveglia versioni e debito
upstream, non "fa" una cosa sola) tenderebbe al sostantivo. Resta
un'ipotesi, non un criterio: non distingue chiaramente `commit` (canonica,
compie un gate, eppure il nome è ambiguo) né spiega perché `kb-review` sia
sostantivo pur compiendo un solo atto diagnostico.

Nessun verdetto qui (i1 è valenza-neutro): se la forma del nome debba
seguire la natura della capacità (azione singola → verbo, area/ciclo di
sorveglianza → sostantivo), se sia solo gusto locale non generalizzabile, o
se serva una terza regola esplicita in `skill.md` accanto a quella sulla
cadenza, è valutazione i2→i3 in `method`.
