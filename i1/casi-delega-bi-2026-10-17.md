---
ciclo: runtime
---

# Casi della delega: primo giro autonomo di `bi` su `svezia`

Data: 2026-10-17 · Fonte: `bi` `i1/ciclo-autonomo-primo-giro-2026-10-17.md`
a `e423e8b1`, letto nel checkout di `svezia` allineato a `origin`, e lo
stato dell'unità in `~/.local/state/ciclo/bi/` (giro `4faa17f8`). Portato
in `method` su richiesta del custode nella sessione che ha avviato il giro.
Nel repo di origine il caso resta «da inoltrare» finché il giro locale non
lo segna «acquisita da method».

## Contesto

Primo giro di `ciclo-bi`, gradino 0, avviato dal custode con
`systemctl --user start ciclo-bi` dopo la sonda superata. Voce in `nixos`
`d55da57` con `requiresProduction`: l'unità parte solo se esiste
`/run/server-role/production` (`ConditionPathExists`). Esito riuscito,
commit e push, 3,18 USD su 5, 123 turni, 3 dinieghi.

## Il caso

**Il marker di ruolo che il bootstrap chiede di rileggere.** Il passo 4 del
bootstrap di `bi` (`CLAUDE.md`) chiede, prima del primo atto, `hostname` e il
marker `/run/server-role/production`. Nel giro autonomo `ls /run/server-role/`
è negato due volte: `.claude/ciclo.json` concede `ls` solo sui path del repo e
delle cartelle aggiuntive. L'agente non ha aggirato il diniego, ha dedotto il
ruolo da `hostname` e dal prompt e l'ha dichiarato nel resoconto e nella riga
`Attenzione:`. Questione dell'adottante: o `ciclo.json` concede la lettura del
marker (`Bash(ls /run/server-role/*)` o `Read(/run/server-role/**)`), o il
bootstrap del giro autonomo dichiara che il ruolo è garantito dall'unità.

## Fatti accanto al caso

- La skill canonica `cycle`, «Avvio», dice già che l'unità ha controllato
  host, lock, branch e working tree, e ricontrolla solo `git status --short`
  e `git pull --ff-only`. La doppia verifica del marker viene dal bootstrap
  locale di `bi`, non dal canone.
- In `nixos` `o3/cicli.nix` anche `crm` e `baserow` hanno
  `requiresProduction`; i loro `CLAUDE.md` e `ciclo-prompt.md` non nominano il
  marker. Un solo adottante su tre con la condizione la ripete nel bootstrap.
- Il terzo diniego, un `jq` con apici annidati nel filtro, non è legato al
  marker: la stessa trasformazione è passata da Read e Write sul file di
  batch.
